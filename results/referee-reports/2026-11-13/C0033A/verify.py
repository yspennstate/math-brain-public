"""Independent mathematical audits, including arbitrary-precision sign checks."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,itertools
from pathlib import Path
import numpy as np
import mpmath as mp
from dpp import stats,probabilities,basis,hessian,random_kernel,mp_stats,mp_matrix

root=Path(__file__).resolve().parent;data=root/'data';rng=np.random.default_rng(330015)
results={'seed':330015,'independent_checks':[],'high_precision':[]}

def mobius(q):
    n=len(q);m=[]
    for s in range(1<<n):
        ids=[i for i in range(n) if s>>i&1]
        m.append(np.linalg.det(q[np.ix_(ids,ids)]).real if ids else 1.)
    p=np.array(m)
    for i in range(n):
        for s in range(1<<n):
            if not(s>>i&1):p[s]-=p[s|(1<<i)]
    return p

max_atom_error=0.;max_hess_error=0.;max_mass_error=0.;max_derivative_mass=0.
for n in range(2,8):
    for cx in (False,True):
        for trial in range(8):
            q=random_kernel(rng,n,cx,'uniform');bb=basis(n,cx)
            x=rng.normal(size=len(bb));x/=np.linalg.norm(x);a=np.einsum('b,bij->ij',x,bb)
            val=stats(q,a);p,_=probabilities(q);p2=mobius(q)
            err=np.max(abs(p-p2));max_atom_error=max(max_atom_error,float(err))
            assert err<1e-12
            assert abs(val[0]+sum(p2*np.log(p2)))<1e-11
            hh=hessian(q,bb);v=np.einsum('i,ij,j->',x,hh,x);err=abs(v-val[1])
            max_hess_error=max(max_hess_error,float(err));assert err<1e-9
            max_mass_error=max(max_mass_error,abs(val[2]-1));max_derivative_mass=max(max_derivative_mass,abs(val[4]),abs(val[5]))
results['independent_checks'].append(dict(name='96 kernels: Mobius atoms versus signed determinants; C++ directional curvature versus full Hessian',max_atom_error=max_atom_error,max_hessian_error=max_hess_error,max_mass_error=max_mass_error,max_derivative_mass=max_derivative_mass))

# Every saved optimized candidate is checked at two independent precisions.
for path in sorted(data.glob('*optimized*.npz')):
    d=np.load(path);q=d['Q'];a=d['A'];rec={'file':str(path.relative_to(root)),'double_claim':float(d['value'])}
    rec['mp80']=mp_stats(q,a,80);rec['mp120']=mp_stats(q,a,120)
    rec['lambda_min']=float(np.linalg.eigvalsh(q).min());rec['lambda_max']=float(np.linalg.eigvalsh(q).max())
    with mp.workdps(120):
        v=mp.mpf(rec['mp120']['second']);assert v<=mp.mpf('1e-65'),rec
    results['high_precision'].append(rec);print(path.name,rec['double_claim'],rec['mp80']['second'][:30],flush=True)

# An independent entropy difference for one rational complex 3x3 example.
with mp.workdps(100):
    q=mp.matrix([[mp.mpf('0.4'),mp.mpc('.08','.03'),mp.mpc('-.02','.04')],
                 [mp.mpc('.08','-.03'),mp.mpf('.6'),mp.mpc('.05','-.02')],
                 [mp.mpc('-.02','-.04'),mp.mpc('.05','.02'),mp.mpf('.5')]])
    a=mp.matrix([[mp.mpf('.1'),mp.mpc('.2','-.1'),mp.mpf('-.1')],
                 [mp.mpc('.2','.1'),mp.mpf('-.2'),mp.mpc('.1','.03')],
                 [mp.mpf('-.1'),mp.mpc('.1','-.03'),mp.mpf('.05')]])
    def direct_entropy(q):
        total=mp.mpf(0)
        for s in range(1<<q.rows):
            b=q.copy()
            for i in range(q.rows):
                if not(s>>i&1):b[i,i]-=1
            p=mp.re(mp.det(b))*(-1)**(q.rows-s.bit_count())
            total-=p*mp.log(p)
        return total
    derivative=mp.diff(lambda t:direct_entropy(q+t*a),mp.mpf(0),2)
    jacobi=mp.mpf(mp_stats(q,a,100)['second'])
    assert abs(derivative-jacobi)<mp.mpf('1e-90')
    results['independent_checks'].append({'name':'rational complex n=3: direct arbitrary-precision entropy differentiation versus Jacobi formula','second':mp.nstr(derivative,90),'absolute_error':mp.nstr(abs(derivative-jacobi),5)})

assert all(np.isfinite(np.load(p)['Q']).all() for p in data.glob('*.npz'))
(data/'verification.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results['independent_checks'],indent=2),flush=True)
