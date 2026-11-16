"""OPEN candidate until exact coefficient checks pass."""
import sympy as s
from pathlib import Path

def construct():
    z=s.symbols('z0:4');U=[sum(((5-j)if i<j else -j)*z[j-1]for j in range(1,5))for i in range(5)]
    assert sum(U)==0 and all(s.expand(U[i]-U[i+1]-5*z[i])==0 for i in range(4))
    t=sum(v*v for v in U);A=sum(v**4 for v in U);d=sum(v**3 for v in U)
    return z,s.Poly(d*d+s.Rational(3,2)*t**3-3*A*t,z)
if __name__=='__main__':
    z,p=construct();boundary=5625*z[0]**2*z[3]**2*(z[0]-z[3])**2
    rem=s.Poly(p.as_expr()-boundary,z)
    negatives=[(m,int(c))for m,c in rem.terms()if c<0]
    print('OPEN: sextic candidate terms',len(p.terms()),'negative remainder coefficients',negatives,flush=True)
    import os
    os.environ['OPENBLAS_NUM_THREADS']='1'
    import numpy as np
    rng=np.random.default_rng(12);x=rng.normal(size=(100000,5));x-=x.mean(axis=1)[:,None];x/=np.linalg.norm(x,axis=1)[:,None]
    v=np.sum(x**3,axis=1)**2+1.5-3*np.sum(x**4,axis=1)
    print('NUMERICAL: sampled minimum',v.min(),flush=True)
    Path('cubic_probe.txt').write_text('OPEN: negative remainder coefficients '+str(negatives)+'\nNUMERICAL: 100000-vector minimum '+str(v.min())+'\n')
    with open('LOG.md','a')as f:f.write('\nOPEN: Candidate sextic d^2 >= 3A-3/2 examined in cubic_moment.py. NUMERICAL random minimum '+str(v.min())+' over 100000 centered unit vectors. Exact ordered-cone boundary factor removed; '+str(len(negatives))+' negative coefficients still need an SOS certificate. Two inline diagnostics failed on SymPy BooleanAtom counting before reaching computations; fixed in this script. No proof claimed.\n')
