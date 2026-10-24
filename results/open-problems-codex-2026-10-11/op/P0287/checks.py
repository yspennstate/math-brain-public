from fractions import Fraction as F
from itertools import product
import json,pathlib
P=pathlib.Path(__file__).parent
results=[]

# Exact independent forward equation on a finite half-line approximation.
for n in range(1,9):
 for r in (F(1,4),F(1,2),F(3,4)):
  k=1-r; mass=[]; residual=[F(0) for _ in range(2**n)]
  for s in range(2**n):
   w=F(1)
   for i in range(n): w*=r if (s>>i)&1 else 1-r
   mass.append(w)
  for s,w in enumerate(mass):
   transitions=[]
   if not s&1: transitions.append((s|1,r))
   if (s>>(n-1))&1: transitions.append((s^(1<<(n-1)),k))
   for i in range(n-1):
    if ((s>>i)&3)==1: transitions.append((s^(3<<i),F(1)))
   for t,rate in transitions: residual[t]+=w*rate; residual[s]-=w*rate
  assert all(x==0 for x in residual),(n,r,residual)
  results.append({'check':'finite_product_forward_equation','n':n,'r':str(r),'states':2**n,'max_residual':'0'})

# Compute derivatives from the 16 configurations, not from the claimed formula.
covariance_tests=0
values=(F(0),F(1,3),F(2,3),F(1))
for density in product(values,repeat=4):
 for killed in (None,1,2):
  k=F(3,5); deriv=[F(0),F(0),F(0)]
  for bits in product((0,1),repeat=4):
   w=F(1)
   for z,r in zip(bits,density): w*=r if z else 1-r
   events=[]
   for j in range(3):
    if bits[j]==1 and bits[j+1]==0:
     t=list(bits); t[j]=0; t[j+1]=1; events.append((t,F(1)))
   if killed is not None and bits[killed]:
    t=list(bits); t[killed]=0; events.append((t,k))
   for t,rate in events:
    deriv[0]+=w*rate*(t[1]-bits[1]); deriv[1]+=w*rate*(t[2]-bits[2])
    deriv[2]+=w*rate*(t[1]*t[2]-bits[1]*bits[2])
  a,b,c,d=density
  actual=deriv[2]-c*deriv[0]-b*deriv[1]
  assert actual==b*(1-c)*(c-b),(density,killed,actual)
  covariance_tests+=1
results.append({'check':'four_site_covariance_derivative','cases':covariance_tests,'arithmetic':'exact rational','result':'PASS, including densities 0 and 1'})

# Negative control: mismatch between extraction and complementary density.
n=3;r=F(2,3);k=F(1,2)
empty_incoming=k*r*(1-r)**(n-1);empty_outgoing=r*(1-r)**n
assert empty_incoming-empty_outgoing!=0
results.append({'check':'negative_control_wrong_extraction','empty_state_residual':str(empty_incoming-empty_outgoing),'result':'nonzero as required'})
(P/'checks.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps({'finite_stationarity_checks':24,'covariance_cases':covariance_tests,'negative_control':'PASS','result':'PASS'}))
