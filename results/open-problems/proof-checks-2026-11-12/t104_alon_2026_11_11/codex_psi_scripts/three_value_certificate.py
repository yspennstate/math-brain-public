"""Exact symbolic multiplicity experiments for three distinct coordinate values."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import sympy as sp
import sys,signal,time,json,resource
from cone_certificate import log

def stop(*args):raise TimeoutError('240 seconds')
signal.signal(signal.SIGALRM,stop);signal.alarm(240)
case=sys.argv[1];start=time.monotonic()
log(f'## Symbolic three-value certificate attempt: {case}')
R,U,V,z,w=sp.symbols('R U V z w');gens=(R,U,V,z,w)
def poly(e):return sp.Poly(e,*gens,domain=sp.ZZ)
r=poly(R+1)
if case=='heavy-bottom':
    s=poly(U+1);t=r+s+poly(V);d=z;e=w
elif case=='bottom-at-least-top':
    t=r+poly(U);s=poly(U+V+1);d=z+(V+1)*w;e=(2*U+V+1)*w
elif case=='top-at-least-bottom':
    t=r;r=t+poly(U);s=poly(U+V+1);d=z+(2*U+V+1)*w;e=(V+1)*w
else:raise ValueError(case)
d=poly(d);e=poly(e);n=r+s+t
a=(s+t)*d+t*e;b=-r*d+t*e;c=-r*d-(r+s)*e
assert (r*a+s*b+t*c).is_zero
assert a-b==n*d and b-c==n*e
assert all(v>=0 for v in (a+c).coeffs())
try:
    T=r*a*a+s*b*b+t*c*c;P=r*a**3+s*b**3+t*c**3;Q=r*a**4+s*b**4+t*c**4
    K=(n*n-6*n+6)*T*T+2*n*Q
    H=K*(n*(n-1)*(T*T-Q+2*a*P-2*a*a*T)+T*T)+2*(n-3)*(n*(n-1)*a*a-T)*(n*Q*T-T**3-n*P*P)
    neg=[(m,int(c)) for m,c in H.terms() if c<0]
    if case=='heavy-bottom':assert not neg
    print('terms',len(H.terms()),'negative',len(neg),'seconds',time.monotonic()-start,'peak RSS bytes',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,flush=True)
    print('negative examples',neg[:15],flush=True)
    with open(f'three_value_{case}.json','w') as f:json.dump({'case':case,'terms':len(H.terms()),'negative':neg},f)
    log(f'Exact three-value attempt {case}: {len(H.terms())} terms, {len(neg)} negative coefficients, {time.monotonic()-start:.2f} s. '+('Coefficient identity succeeds; parameter coverage needs checking.' if not neg else 'Simple positive-coefficient attempt fails; no conclusion about inequality.'))
    if '--partition' in sys.argv:
        from itertools import product
        failed=[]
        for cell in product((0,1,2),repeat=3):
            # Each count variable is 0, 1, or at least 2. This covers every integer.
            HH=H.shift_list([2 if c==2 else 0 for c in cell]+[0,0])
            for v,c in zip((R,U,V),cell):
                if c<2:HH=HH.eval(v,c)
            nn=sum(1 for c in HH.coeffs() if c<0)
            if nn:failed.append((cell,nn))
        print('Lattice partition failed cells:',failed,flush=True)
        unresolved=[]
        refinements=[]
        for cell,nn in failed:
            free=[j for j,c in enumerate(cell) if c==2]
            if len(free)!=1:unresolved.append((cell,nn));continue
            j=free[0];v=(R,U,V)[j];HH=H
            for u,c in zip((R,U,V),cell):
                if c<2:HH=HH.eval(u,c)
            for threshold in range(3,21):
                shift=[threshold if u==v else 0 for u in HH.gens]
                tail=HH.shift_list(shift)
                if all(c>=0 for c in tail.coeffs()) and all(all(c>=0 for c in HH.eval(v,k).coeffs()) for k in range(2,threshold)):
                    refinements.append((cell,threshold));break
            else:unresolved.append((cell,nn))
        print('Exact one-variable refinements:',refinements,'unresolved:',unresolved,flush=True)
        if case=='top-at-least-bottom':assert not unresolved
        if case=='bottom-at-least-top':assert failed==[((0,1,2),10)] and unresolved==failed
        log(f'Exact lattice partition experiment {case}: {len(failed)} of 27 initial cells required refinement; refinements {refinements}; unresolved {unresolved}. '+('Certificate succeeds for all nonnegative integer multiplicity parameters.' if not unresolved else 'Does not close the proof.'))
except TimeoutError:log(f'Three-value attempt {case} FAILED: 240 second limit. No conclusion.')
