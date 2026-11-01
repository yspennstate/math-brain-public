import sympy as S
import numpy as np
from itertools import product
for m in [2,3]:
 p=S.symbols('p:'+str(m), positive=True); s=S.symbols('s:'+str(m), positive=True)
 V=p+s
 f=0
 for x in product([0,1],repeat=m):
  mu=S.prod(p[i] if x[i] else 1-p[i] for i in range(m))
  q=1-sum(s[i]*(1/p[i] if x[i] else -1/(1-p[i])) for i in range(m))
  f+=mu*q*S.log(q)
 H=S.hessian(f,V)
 fun=S.lambdify(V,H,'numpy',cse=True)
 for pp in [[.2,.7],[.05,.8],[.3,.5,.8]][:]:
  if len(pp)!=m:continue
  for strength in [.1,.5,.95]:
   ss=[strength*pp[i]/m for i in range(m)]
   h=fun(*(pp+ss)); ev=np.linalg.eigvalsh(h)
   print(m,pp,strength,ev)
