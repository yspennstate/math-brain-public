from fractions import Fraction as Q
import numpy as np
from explore import info
for d1 in [Q(18,25),Q(3,4),Q(7,10)]:
 for u1 in [Q(9,20),Q(2,5)]:
  for u2 in [Q(2,5),Q(41,100)]:
   for d3 in [Q(1,1600),Q(1,100),Q(1,10)]:
    for u3 in [Q(7,200),Q(1,30),Q(1,10)]:
     r=[u1*u1,u2*u2,u3*u3]
     b=1-Q(1,10**7)-r[0]/(1-d1)-r[2]/(1-d3)
     if b<=0:continue
     d2=1-r[1]/b
     if d2<=0:continue
     D=[d1,d2,d3];u=[u1,u2,u3]
     K=np.diag([float(v) for v in D])+np.outer([float(v) for v in u],[float(v) for v in u])
     val,t,M=info(K)
     if val<1.95:
      print('obstruction',val,'D',list(map(str,D)),'u',list(map(str,u)), 'defect',1-sum(r[i]/(1-D[i]) for i in range(3)));quit()
