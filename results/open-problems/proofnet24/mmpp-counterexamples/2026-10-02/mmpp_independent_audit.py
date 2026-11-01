from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import factorial
import json

n=16
offsets=(1000,924,707,383,0,-383,-707,-924,-1000,-924,-707,-383,0,383,707,924)
lam=[F(10000+x,10**6) for x in offsets]
Q=[[F(0) for _ in range(n)] for _ in range(n)]
for i in range(n):
    Q[i][i]=-1
    Q[i][(i+1)%n]=1
assert all(sum(row)==0 for row in Q)
pi=[F(1,n)]*n
assert all(sum(pi[i]*Q[i][j] for i in range(n))==0 for j in range(n))
mean=sum(pi[i]*lam[i] for i in range(n))
alpha=[pi[i]*lam[i]/mean for i in range(n)]
assert sum(alpha)==1
w=[pi[i]-alpha[i] for i in range(n)]
C=[[Q[i][j]-F(i==j)*lam[i] for j in range(n)] for i in range(n)]
assert all(sum(pi[i]*C[i][j] for i in range(n))==-pi[j]*lam[j] for j in range(n))
t=F(12);r=F(1011,1000)
B=[[t*(C[i][j]+F(i==j)*r) for j in range(n)] for i in range(n)]
assert min(x for row in B for x in row)>=0
L=max(sum(abs(x) for x in row) for row in B)
v=[F(1)]*n
S=sum(w[i]*v[i] for i in range(n))
K=80
for k in range(1,K+1):
    # Column-vector propagation from B^k 1/k!, independently of the
    # source certificate's specialized row-vector recurrence.
    v=[sum(B[i][j]*v[j] for j in range(n))/k for i in range(n)]
    S+=sum(w[i]*v[i] for i in range(n))
E=sum(abs(x) for x in w)*L**(K+1)/factorial(K+1)/(1-L/(K+2))
assert E<F(1,10**31)
assert S+E<-F(39,10)
assert S-E>-F(4)
with localcontext() as ctx:
    ctx.prec=70
    sd=str(Decimal(S.numerator)/Decimal(S.denominator))
    ed=str(Decimal(E.numerator)/Decimal(E.denominator))
    rt=-r*t
    lower=Decimal(S.numerator)/Decimal(S.denominator)*(Decimal(rt.numerator)/Decimal(rt.denominator)).exp()
report={'independent_method':'dense column-vector Fraction recurrence','Q_stationary_checked':True,'alpha_orientation_checked':True,'t':'12','S_80':sd,'absolute_tail_bound':ed,'difference_display':str(lower),'exact_sign_verified':S+E<0,'exact_upper_bound':str(-F(39,10*3**13))}
print(json.dumps(report,indent=2))
