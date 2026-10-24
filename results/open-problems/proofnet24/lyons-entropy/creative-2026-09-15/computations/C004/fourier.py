from explore import *
from fractions import Fraction
n=6
Q=np.exp(2j*np.pi*np.arange(6)[:,None]*np.arange(6)[None,:]/6)/np.sqrt(6)
levels,diamonds,D=setup(); p,b=laws(Q)
for lev,tab in zip(levels,p):print([(tuple(i+1 for i in s),str(Fraction(float(x)).limit_denominator(10000))) for s,x in zip(lev,tab)])
c=np.r_[np.zeros(90),-1]
res=linprog(c,A_eq=np.c_[D,np.zeros(50)],b_eq=b,A_ub=np.c_[-np.eye(90),np.ones(90)],b_ub=np.zeros(90),bounds=[(0,None)]*91,method='highs')
print('minweight',res.fun, Fraction(-res.fun).limit_denominator(100000))
print('weights',[(a,Fraction(float(w)).limit_denominator(100000)) for a,w in zip(diamonds,res.x) if w>1e-10])
