import numpy as np
from explore import mats
mi=(100,None)
for r in np.linspace(0,.5,101):
 for s in np.linspace(0,.5,101):
  if r+s==0: continue
  U,T,M=mats(r,s)
  h=r*r+s*s
  b=np.linalg.eigvalsh(M-3*h*np.eye(2))[0]
  if b<mi[0]:mi=(b,(r,s))
print('min',mi)
