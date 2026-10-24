import numpy as np
from math import comb
from pathlib import Path
import json
rng=np.random.default_rng(31)
results=[]
for n in [3,4,5,6,8,12,20]:
 minval=1e99; worst=None; tested=0
 for _ in range(3000):
  a=1/(1+np.exp(rng.uniform(-9,9))); c=a+(1-a)/(1+np.exp(rng.uniform(-12,12)))
  if c-a<1e-10:continue
  q=np.convolve([comb(n-1,j)*a**j*(1-a)**(n-1-j) for j in range(n)], [1-c,c])
  lp=np.log(q)-np.log([comb(n,j) for j in range(n+1)])
  daq=np.convolve([comb(n-2,j)*a**j*(1-a)**(n-2-j) for j in range(n-1)],[-1,1])*(n-1)
  dap=np.convolve(daq,[1-c,c]);dcp=np.convolve([comb(n-1,j)*a**j*(1-a)**(n-1-j) for j in range(n)],[-1,1])
  d2ap=np.convolve(np.convolve([comb(n-3,j)*a**j*(1-a)**(n-3-j) for j in range(n-2)],[1,-2,1]),[1-c,c])*(n-1)*(n-2)
  d2ac=np.convolve(daq,[-1,1])
  frozen=-np.array([[d2ap@lp,d2ac@lp],[d2ac@lp,0]])
  mu=(n-1)*a+c;v=(n-1)*a*(1-a)+c*(1-c);p=q[0]
  C=np.array([[v,-p*mu],[-p*mu,p*(1-p)]]);J=np.array([[n-1,1],[-(n-1)*p/(1-a),-p/(1-c)]])
  try: F=J.T@np.linalg.solve(C,J)
  except:continue
  tested+=1
  eig=np.linalg.eigvalsh(F-frozen)[0]
  if eig<minval:minval=eig;worst=(a,c)
  if eig<-1e-5:break
 print(n,minval,worst)
 results.append({'n':n,'random_draws':3000,'evaluated_cases':tested,'minimum_eigenvalue_observed':minval,'parameters_at_minimum':worst})
Path(__file__).with_name('alln_count_empty_search_results.json').write_text(json.dumps(results,indent=2)+'\n')
