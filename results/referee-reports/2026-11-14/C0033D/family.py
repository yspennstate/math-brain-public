"""Exact identities and numerical tables for the imaginary cyclic family."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp
from reduced import criterion

def main():
    k,L=sp.symbols('k L',positive=True)
    u=(k-1)/(4*(3*k+1));p0=1/(2*(3*k+1));p1=k*p0;c=3*(k+1)/(2*(3*k+1))
    f11=sp.factor(2*c*c/p0+6*(c-1)**2/p1)
    f12=sp.factor(-12*c*u/p0-36*u*(c-1)/p1)
    f22=sp.factor(72*u*u/p0+216*u*u/p1)
    determinant=sp.factor((f11-6*L)*(f22+6*L)-f12*f12)
    target=36*(-L*L+(6*k*k+6*k-4)/(k*(3*k+1))*L+3*(k-1)**2/k)
    assert sp.cancel(determinant-target)==0
    check=[]
    for r in (.01,.05,.15,.25,.28):
        q=np.array([[.5,1j*r,-1j*r],[-1j*r,.5,1j*r],[1j*r,-1j*r,.5]])
        kk=(1+4*r*r)/(1-12*r*r);ll=np.log(kk)
        ff=[float(z.subs(k,kk)) for z in (f11,f12,f22)]
        theta=9*ll/(ff[0]+3*ll-ff[1]**2/(ff[2]+6*ll))
        check.append(dict(r=r,theta_formula=theta,theta_full=criterion(q),error=abs(theta-criterion(q))))
    mp.mp.dps=180;rows=[]
    for e in (1,2,4,8,16,32,100):
        kk=mp.mpf(10)**e;ll=mp.log(kk)
        A=(6*kk*kk+6*kk-4)/(kk*(3*kk+1))
        det=36*(-ll*ll+A*ll+3*(kk-1)**2/kk)
        ff22=9*(kk-1)**2*(kk+3)/(kk*(3*kk+1))
        schur=det/(ff22+6*ll);margin=schur/(9*ll+schur)
        rows.append(dict(k='10^'+str(e),margin=mp.nstr(margin,40),leading=mp.nstr(4/(ll+4),40),L_times_margin=mp.nstr(ll*margin,30)))
    out=dict(symbolic_determinant=str(sp.factor(determinant)),symbolic_remainder='0',
             full_formula_checks=check,boundary_rows=rows)
    Path('data/family.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
