"""Test only the proposed sufficient submodularity bridge, not Lyons."""
import numpy as np,json
from scipy.optimize import linprog
from recovery import *
from pathlib import Path

def main():
 rng=np.random.default_rng(7008); n=4; ns=1<<n
 sub=[]
 for i in range(n):
  for j in range(i+1,n):
   for t in range(ns):
    if (t&(1<<i)) or (t&(1<<j)):continue
    row=np.zeros(ns);row[t]=row[t|(1<<i)|(1<<j)]=1;row[t|(1<<i)]=row[t|(1<<j)]=-1;sub.append(row)
 sub=np.array(sub);eq=np.zeros((n+1,ns));eq[0,0]=1
 for i in range(n):eq[i+1,1<<i]=1
 best=None
 for repeat in range(8):
  z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));u,_=np.linalg.qr(z);k=(u*np.array([.08,.28,.65,.91]))@u.conj().T
  L=np.linalg.solve(np.eye(n)-k,k);lh=spectral(L,np.sqrt);p=atoms(k)
  compounds=[]
  for s in subsets(n):
   pi=lh[:,s]@np.linalg.inv(L[np.ix_(s,s)])@lh[s,:] if s else np.zeros_like(k)
   compounds.append(compound(pi-k,2))
  for trial in range(12):
   w=rng.normal(size=6)+1j*rng.normal(size=6);w/=np.linalg.norm(w)
   coeff=p*np.array([np.vdot(w,c@w).real for c in compounds])
   fit=linprog(-coeff,A_ub=np.r_[sub,-sub],b_ub=np.r_[np.zeros(len(sub)),np.ones(len(sub))],A_eq=eq,b_eq=np.zeros(n+1),bounds=[(None,None)]*ns,method='highs')
   if fit.success and (best is None or -fit.fun>best['value']):
    best={'value':float(-fit.fun),'f':fit.x.tolist(),'K_real':k.real.tolist(),'K_imag':k.imag.tolist(),'w_real':w.real.tolist(),'w_imag':w.imag.tolist()}
 print(json.dumps(best,indent=2));Path(__file__).with_name('submodular_probe.json').write_text(json.dumps(best,indent=2))
if __name__=='__main__':main()
