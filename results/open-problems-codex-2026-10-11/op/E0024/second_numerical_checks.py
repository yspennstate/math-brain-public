from pathlib import Path
import json,math,random
import numpy as np
random.seed(24)
for _ in range(20000):
 p,q,s=[random.uniform(-10,10) for _ in range(3)]
 lhs=2*((p-s)**2+(q-s)**2)-(p-q)**2
 assert lhs>=-1e-10
 assert abs(lhs-(p+q-2*s)**2)<1e-9
roots,w=np.polynomial.hermite.hermgauss(40)
U,V=np.meshgrid(roots,roots,indexing='ij');W=w[:,None]*w[None,:]
kappa=2/math.pi; results=[]
for logT in [2.,4.,8.,12.,16.,20.]:
 T=math.exp(logT);delta=T**-.5;lam=kappa*T*logT
 centers=[(0.,0.),(T,1.),(-T,-1.)];amps=[1.,.5,.5]
 E=[]
 for level in [1.,lam]:
  total=0.
  for i,ci in enumerate(centers):
   for j,cj in enumerate(centers):
    distance=(ci[0]-cj[0])**2+(ci[1]-cj[1])**2
    overlap=math.exp(-distance/(4*delta*delta)) if distance/(4*delta*delta)<745 else 0.
    if not overlap:continue
    x=(ci[0]+cj[0])/2+delta*U;y=(ci[1]+cj[1])/2+delta*V
    r=np.abs(x)+y*y
    b=kappa*x*np.log(np.maximum(np.abs(x),1e-300))
    A=level+r;kernel=A/(A*A+b*b)
    cutoff=-np.expm1(-y*y/2)
    total+=amps[i]*amps[j]*overlap*delta*delta*float(np.sum(W*cutoff*cutoff*kernel))
  normalizer=1+math.exp(-(T*T+1)/(2*delta*delta))
  E.append(total/(normalizer*normalizer))
 results.append({'logT':logT,'E1_residual':E[0],'E_lambda_residual':E[1],'ratio':E[1]/E[0],'asymptotic_ratio':kappa*logT/2})
hellinger=[]
alpha=.5;cplus=1.;cminus=0.;coefficient=.5*(math.sqrt(cplus)-math.sqrt(cminus))**2
for n in [2,4,8,16,32]:
 eps=2.**-n;lower=coefficient*(eps**-alpha-1)/alpha
 hellinger.append({'cutoff':eps,'minimal_hellinger_integral':lower,'Poisson_affinity_at_T1':math.exp(-lower/2)})
out={'hellinger_identity_random_tests':20000,'smoothing_residual_gauss_hermite_order':40,'smoothing_residual':results,'stable_hellinger_obstruction':hellinger}
Path('second_numerical_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
