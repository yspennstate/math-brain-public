import math,json

def fwht(a):
 a=list(a);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
  h*=2
 return a

def h(t):return -t*math.log2(t)-(1-t)*math.log2(1-t) if 0<t<1 else 0.
C_B=(1+2/math.sqrt(math.e))/math.log(2);C_D=C_B+2/math.log(2)
cases=0;max_gap_B=0.;max_gap_D=0.
for n in range(1,5):
 N=1<<n
 for code in range(1<<N):
  f=[1-2*((code>>j)&1) for j in range(N)];a=[x/N for x in fwht(f)];v=1-a[0]**2
  for i in range(n):
   bit=1<<i;d=sum(a[t]**2 for t in range(N) if t&bit)
   if not d:continue
   B=0.;JS=0.
   for t in range(N):
    if t&bit:continue
    u,z=a[t],a[t|bit];q=u*u+z*z
    if not q:continue
    B+=q*h(z*z/q)
    JS+=q*(1-h((u+z)**2/(2*q)))
   rhs_B=d*(math.log2(v/d)+C_B);rhs_D=d*(math.log2(v/d)+C_D)
   assert B<=rhs_B+1e-12
   assert B+JS<=rhs_D+1e-12
   max_gap_B=max(max_gap_B,B-rhs_B);max_gap_D=max(max_gap_D,B+JS-rhs_D);cases+=1
print(json.dumps(dict(positive_influence_cases=cases,C_B=C_B,C_D=C_D,max_violation_B=max_gap_B,max_violation_D=max_gap_D,scope='Finite numerical self-checks; analytic proof is separate'),indent=2))
