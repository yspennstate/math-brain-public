"""Second derivation: symbolic certificates, exact projection and couplings."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import signal, time, json
signal.alarm(280)
from fractions import Fraction as F
import sympy as sp
import numpy as np
from audit import polymer, cut_generator, radial, reversible_spectrum

start=time.monotonic()
n,b,k,a,l,r,u,v=sp.symbols('n b k a l r u v',positive=True)
checks=[]
def check(name,x):
    assert sp.factor(x)==0,(name,sp.factor(x))
    checks.append(name)

def Aquot(forward,backward):
    return b*(n-k-1)*(1-forward)+k*(k-1)/n*(1-backward)+b+2*k/n
def Lquot(forward,backward):
    return b*(n-k-l)*(1-forward)+(k-1)*(k-l)/n*(1-backward)+l*b+l*(k-1)/n
check('count reciprocal',Aquot((k+a)/(k+a+1),(k+a)/(k+a-1))-(b*(n-k-1)/(k+a+1)-k*(k-1)/(n*(k+a-1))+b+2*k/n))
check('count upper reciprocal',Aquot((k+a)/(k+a+2),(k+a+1)/(k+a-1))-(2*b*(n-k-1)/(k+a+2)+b+2*k*a/(n*(k+a-1))))
check('sector reciprocal',Lquot((k+a)/(k+a+1),(k+a)/(k+a-1))-(b*(n-k-l)/(k+a+1)+l*b+(k-1)*((l-1)*k+l*a)/(n*(k+a-1))))
check('degree factorial certificate',Lquot((k+a)/(k+a+l),(k+a+l-1)/(k+a-1))-l*(b*(n-k-l)/(k+a+l)+b+(k-1)*(a+l-1)/(n*(k+a-1))))
check('sharp count', (Aquot((k+a)/(k+a+2),(k+a+1)/(k+a-1))-(2*a/n-b-6*a*(a-1)/(n*(k+a-1)*(k+a+2)))).subs(b,a*(a-1)/(n*(n+a+1))))
check('sharp degree one',(Lquot((k+a)/(k+a+1),(k+a)/(k+a-1)).subs(l,1)-(a/n-2*a*a/(n*(k+a-1)*(k+a+1)))).subs(b,a*a/(n*(n+a))))
check('higher sector',Lquot(u,v).subs(k,r+l-1)-(Aquot(u,v).subs(k,r)+(l-1)*b*(2*u-1)+(l-2)/n*(r+l-(r-1)*(v-1))))
check('tower', (r-1)*(n-2*l-r+2)+n-2*(l+r-1)-r*(n-2*l-r+1))
check('Lyapunov fourth powers',u**4+v**4-u*v**3-v*u**3-(u-v)**2*(u*u+u*v+v*v))
check('critical finite correction',(n*Aquot(u,v).subs(b,b/n**2))-(b*(1-u)+k*(k-1)*(1-v)+2*k+b/n*(1+(k+1)*(u-1))))
j=sp.symbols('j',nonnegative=True)
check('critical degree-one correction',(n*Lquot(u,v).subs({l:1,k:j+1,b:b/n**2}))-(b*(1-u)+j*j*(1-v)+j+b/n*(1+(j+2)*(u-1))))
check('critical degree-one reciprocal',(b*(1-(j+1+a)/(j+2+a))+j*j*(1-(j+1+a)/(j+a))+j).subs(b,a*a)-(a-2*a*a/((j+a)*(j+a+2))))
check('stageII reciprocal', b*(n-r-2)/(r+a+1)-r*r/(n*(r+a-1))+b+r/n-(b*(n-r-2)/(r+a+1)+b+r*(a-1)/(n*(r+a-1))))

def cut_rates(n,b,s):
    k=s.bit_count();out={}
    for i in range(n):
        t=s^(1<<i)
        rate=F(k-1,n) if s&(1<<i) else b
        if rate:out[t]=rate
    return out
def image(n,s):
    c=[i for i in range(n) if s&(1<<i)]
    lengths=[c[(i+1)%len(c)]-c[i] if i+1<len(c) else n+c[0]-c[i] for i in range(len(c))]
    return tuple(lengths.count(j) for j in range(1,n+1))

projection_entries=0;spectral_cases=0;maxspec=0
for nn in range(2,9):
    for bb in (F(1,7),F(3)):
        states,q,w=polymer(nn,bb);ix={m:i for i,m in enumerate(states)}
        fibers={m:[] for m in states}
        for s in range(1,2**nn):fibers[image(nn,s)].append(s)
        for m,sets in fibers.items():
            aidx=ix[m];out=[F(0) for _ in states]
            assert len(sets)==F(nn*sp.factorial(sum(m)-1),int(sp.prod(sp.factorial(x) for x in m)))
            for s in sets:
                for t,rate in cut_rates(nn,bb,s).items():out[ix[image(nn,t)]]+=rate/len(sets)
            out[aidx]=-sum(out)
            assert out==q[aidx]
            projection_entries+=len(out)
        _,qb,wb=cut_generator(nn,float(bb));vals=reversible_spectrum(qb,wb)[0]
        expected=[]
        for degree in range(nn//2+1):
            d,e=radial(nn,float(bb),ell=degree)
            from scipy.linalg import eigh_tridiagonal
            spectrum=eigh_tridiagonal(d,e,eigvals_only=True)
            mult=1 if degree==0 else int(sp.binomial(nn,degree)-sp.binomial(nn,degree-1))
            expected.extend(list(spectrum)*mult)
        err=max(abs(vals-np.array(sorted(expected))));assert err<1e-9
        maxspec=max(maxspec,float(err));spectral_cases+=1

couplings={'I':0,'II':0}
def verify(n,b,X,Y,events,stage):
    for side,s in enumerate((X,Y)):
        out={}
        for newx,newy,rate in events:
            dest=(newx,newy)[side]
            if dest!=s and rate:out[dest]=out.get(dest,F(0))+rate
        assert out==cut_rates(n,b,s),(stage,n,X,Y,side,out,cut_rates(n,b,s))
    couplings[stage]+=1
for nn in range(2,8):
    bb=F(1,7);full=(1<<nn)-1
    for X in range(1,2**nn):
        for Y in range(X+1,2**nn):
            ex=X&~Y;ey=Y&~X;common=X&Y;vacant=full&~(X|Y)
            if ex==0 and ey.bit_count()==1:
                kk=X.bit_count();ev=[]
                for i in range(nn):
                    mask=1<<i
                    if vacant&mask:ev.append((X|mask,Y|mask,bb))
                    if common&mask:
                        ev.append((X^mask,Y^mask,F(kk-1,nn)))
                        ev.append((X,Y^mask,F(1,nn)))
                ev.extend([(Y,Y,bb),(X,X,F(kk,nn))])
                verify(nn,bb,X,Y,ev,'I')
            if ex.bit_count()==ey.bit_count()==1:
                rr=common.bit_count();ev=[]
                for i in range(nn):
                    mask=1<<i
                    if vacant&mask:ev.append((X|mask,Y|mask,bb))
                    if common&mask:ev.append((X^mask,Y^mask,F(rr,nn)))
                ev.extend([(X|Y,X|Y,bb),(common,common,F(rr,nn))])
                verify(nn,bb,X,Y,ev,'II')

result=dict(symbolic_identities=checks,projection_entries=projection_entries,spectral_cases=spectral_cases,max_spectrum_error=maxspec,coupling_pairs=couplings,elapsed_seconds=time.monotonic()-start)
with open('algebra_checks.json','w') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))
