"""Exact constant checks and bounded diagnostics for the full-dimensional region.
The analytic proof is in agents/C001.md. Floating-point diagnostics are not proof.
"""
from fractions import Fraction as F
import itertools, json, math, pathlib
import numpy as np
from explore import calc
checks={
 'h_lower':1-2*F(1,4)-F(1,200)==F(99,200),
 'h_upper':1-2*F(2401,10000)+F(1,200)==F(328,625),
 'tau_lower':F(594,953)-F(1,15000)>F(3,5),
 'tau_upper':F(269,128)>F(200,99),
 'd_lower':F(2401,10000)>F(6,25),
 'd_upper':1/(4-F(1,10000))<F(13,50),
 'Z_upper':F(168,25)+F(2541,1000)*F(1,10000)<7,
 'B_lower':1+F(9,10)*(1-F(1,40000))>F(15,8),
 'N_upper':F(11,10)*(1+F(11,10)*F(328,625))<F(7,4),
 'BN_upper':F(21,10)+F(7,4)*F(1,10000)<F(9,4),
 'p_lower':F(9,10)*F(15,8)/7>F(1,5),
 'alpha':F(11,9)/(1-F(1,40000))<F(36,25),
 'v_norm':F(1,9)+F(9,25)<F(1,2),
 'b1_upper':F(13,50)*F(1,10000)+F(9,20)<F(1,2),
 'b2_upper':F(13,50)*F(5,2)+F(3,4)==F(7,5),
 'h23_upper':F(9,20)+F(13,50)*F(1,10000)<F(1,2),
 'gamma12':F(6084,3000)<3,
 'gamma13':F(169,2700)<F(1,15),
 'kappa1':F(175,48)<4,
 'kappa2':F(125,16)<8,
 'kappa3':F(7,8)<1,
 'R_lower':1-F(3,10000)-F(5,64)>F(9,10),
 'E_upper':4+(1+F(2,15))/64<5,
 'surplus':F(81,100)-F(9,20)==F(9,25),
}
assert all(checks.values()), checks
rows=[]
for t in [1e-4,1e-6]:
 for l1,l2,l3,beta,gamma,cs in itertools.product([.9,1.1],[.9,1.1],[.9,1.1],[.49,.5],[.49,.5],[-.01,.01]):
  phi=math.acos(cs);a=math.sqrt(1-t);s=math.sqrt(t);D=np.diag(np.sqrt([l1,l2,l3]))
  R=np.array([[1,a,gamma*s*np.exp(-1j*phi)],[a,1,beta*s],[gamma*s*np.exp(1j*phi),beta*s,1]])
  dat=calc(D@R@D); ids=[0,2,5]
  W=dat['w'][:,ids];M=dat['M'];delta=dat['delta'];om=dat['om'][ids]
  H=W.conj().T@M@W;b=np.diag(H).real;gam=abs(H)**2/(b[:,None]*b[None,:]);kap=delta/(om*b*b)
  rstar=1-gam[0,1]-gam[1,2];ee=kap[0]+kap[2]+2*gam[0,2];trial=2-ee+rstar*rstar/(1+kap[1])
  lb=2+1/(25*-math.log(t)); assert trial>lb
  assert gam[0,1]<=3*t and gam[0,2]<=t**3/(15*-math.log(t)) and gam[1,2]<=5/(8*-math.log(t))
  assert kap[0]<=4*t*-math.log(t) and kap[1]<=8*-math.log(t) and kap[2]<=t/-math.log(t)
  rows.append({'t':t,'ell':[l1,l2,l3],'beta':beta,'gamma':gamma,'cosphi':cs,'trial':trial,'proved_lower':lb})
result={'exact_rational_checks':checks,'finite_diagnostics_not_proof':{'count':len(rows),'least_trial':min(rows,key=lambda r:r['trial'])}}
print(json.dumps(result,indent=2));pathlib.Path(__file__).with_name('region_output.json').write_text(json.dumps(result,indent=2)+'\n')
