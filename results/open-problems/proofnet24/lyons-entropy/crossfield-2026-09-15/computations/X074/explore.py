import numpy as np
from math import atanh,log,sqrt

def mats(r,s):
 a,b,c=1-r*r,1-s*s,1-r*r*s*s
 R,S,D=atanh(r),atanh(s),atanh(r*s)
 k=.5*log(c/(a*b))
 U=np.array([[2*(2*c-b)/(a*c),2/c-2*k],[2/c-2*k,2*(2*c-a)/(b*c)]])
 T=np.array([[R+s*D,S-s*k],[R-r*k,S+r*D]])
 return U,T,U-T@T.T
for r,s in [(0.2,0.1),(.8,.2),(.99,.2),(.99,.9),(.999999,.1),(.999999,.99),(.1,0)]:
 U,T,M=mats(r,s)
 print((r,s),'M',M,'eval',np.linalg.eigvalsh(M),'dd',np.diag(M)-abs(M[0,1]))
