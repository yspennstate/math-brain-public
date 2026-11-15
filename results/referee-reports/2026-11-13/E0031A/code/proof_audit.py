#!/usr/bin/env python3
"""Independent finite checks of identities used in the proof; not proof by sampling."""
import os,json,math
from fractions import Fraction as F
from pathlib import Path
assert os.getpriority(os.PRIO_PROCESS,0)>=10

def square(p):
 q={}
 for (i,j),a in p.items():
  for (k,l),b in p.items():q[i+k,j+l]=q.get((i+k,j+l),F(0))+a*b
 return q
# For n=2,d=1, h(x,y)=-x^2-y^2+2y-2/3 on x<=y.
h={(2,0):F(-1),(0,2):F(-1),(0,1):F(2),(0,0):F(-2,3)}
J=2*sum(a/F((i+1)*(i+j+2)) for (i,j),a in square(h).items())
u={(2,0):F(1),(1,0):F(-1),(0,0):F(1,6)}
gvar=sum(a/F(i+1) for (i,j),a in square(u).items())
assert J==F(2,45) and gvar==F(1,180)
assert 2*gvar+J==F(1,18)
checks=[]
for n in range(2,202,2):
 m=n//2
 mu=F(m,n+1)
 beta=F(m*(m+1),(n+1)**2*(n+2))
 spacing=F(m*n-m*(m-1),(n+1)**2*(n+2))
 simplified=F(n,4*(n+1)**2)
 assert beta==spacing==simplified
 prev=F(m-1,n-1);delta=mu-prev
 assert delta==F(1,n*n-1)
 # Exact integrated one-point conditional mean:
 # g_n(x)=(n-1)/(2n)+(2x-1)^n/(2n).
 integrated=F(n-1,2*n)+F(1,2*n*(n+1))
 boundary=F(1,2)-mu
 assert integrated==mu and n*boundary==mu
 var_g=F(1,4*n*n)*(F(1,2*n+1)-F(1,(n+1)**2))
 assert n*var_g<=beta
 lowerA=F(n*(n-1),32)*delta**3
 lowerC=F(n,4)*(mu/n)**3
 assert lowerA<=beta and lowerC<=beta
 checks.append(n)
result={'rational_n2_d1':{'mu':'1/3','variance':'1/18','first_projection_variance':str(gvar),'second_kernel_L2_squared':str(J),'orthogonal_sum':'2*(1/180)+2/45=1/18'},'exact_1d_checks_even_n':checks,'checks':['beta variance independently from Dirichlet spacing covariance','mean increment 1/(n^2-1)','boundary identity independently from conditional mean polynomial','first and second projection lower inequalities','bounds A and C for exact 1d model'],'limitations':'Finite checks supplement the written analytic arguments; they do not establish asymptotics in d>=2.'}
Path('data/proof_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
