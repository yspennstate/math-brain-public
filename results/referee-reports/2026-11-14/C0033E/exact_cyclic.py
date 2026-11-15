"""Independent nine-direction Hessian determinant derivation, without D's f_ij."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[k]='1'
import json,time,resource
from pathlib import Path
import sympy as s
from interval_core import expr,x

def main():
    start=time.monotonic()
    r,L=s.symbols('r L',real=True)
    q=[s.Rational(1,2)]*3+[0,r,0,-r,0,r]
    p=s.Matrix([z.subs(dict(zip(x,q))) for z in expr])
    G=s.Matrix(expr).jacobian(x).subs(dict(zip(x,q)))
    F=s.simplify(G.T*s.diag(*[1/z for z in p])*G)
    metric=s.diag(1,1,1,2,2,2,2,2,2);v=s.Matrix([1,1,1,0,0,0,0,0,0])
    # Direct atom Hessian: the log(A) term cancels by normalization.
    hh=[sp_h.subs(dict(zip(x,q))) for sp_h in [s.hessian(z,x) for z in expr]]
    correction=sum((hh[i] for i in range(1,7)),s.zeros(9))
    assert correction==metric-v*v.T
    N=F+L*correction
    J=N+L*v*v.T
    # Complement/conjugation block separation is read off, not assumed.
    re=[0,1,2,3,5,7];im=[4,6,8]
    assert J.extract(re,im)==s.zeros(6,3)
    blocks={}
    for name,A in [('J',J),('N',N)]:
        blocks[name+'real']=s.factor(A.extract(re,re).det(method='domain-ge'))
        blocks[name+'imag']=s.factor(A.extract(im,im).det(method='domain-ge'))
    margin=s.factor(blocks['Nreal']/blocks['Jreal'])
    k=s.symbols('k',positive=True)
    mk=s.factor(margin.subs(r*r,(k-1)/(4*(3*k+1))))
    d=36*(-L**2+(6*k*k+6*k-4)/(k*(3*k+1))*L+3*(k-1)**2/k)
    f22=9*(k-1)**2*(k+3)/(k*(3*k+1))
    inherited=d/(9*L*(f22+6*L)+d)
    assert s.cancel(mk-inherited)==0
    out={k:str(v) for k,v in blocks.items()}
    out.update(atoms=list(map(str,p)),gradient=str(G),margin_r=str(margin),margin_k=str(mk),difference_from_D='0',seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
    Path('data/exact_cyclic.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()
