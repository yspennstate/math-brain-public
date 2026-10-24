import itertools,json,time,pathlib
from fractions import Fraction
from decimal import Decimal,localcontext
root=pathlib.Path(__file__).resolve().parent
start=time.time()
def p1(A,w,n):
 return {i for i in range(n) if (w&~(1<<i)) not in A and (w|(1<<i)) in A}
def p2_definition(A,w,n):
 ans=p1(A,w,n)
 for j in range(n):
  if w>>j&1: ans |= p1(A,w&~(1<<j),n)
 return ans

def p2_pair(A,w,n):
 first={i for i in range(n) if w>>i&1 and (w&~(1<<i)) not in A}
 ans=set(first)
 for i in range(n):
  if not w>>i&1:continue
  for j in range(n):
   if i!=j and w>>j&1 and (w&~(1<<j)) in A and (w&~(1<<j)&~(1<<i)) not in A:ans.add(i)
 return ans

def upsets(n):
 if n==0:return [0,1]
 prev=upsets(n-1);shift=1<<(n-1)
 return [a|(b<<shift) for a in prev for b in prev if a&~b==0]
results=[]
for n in range(1,6):
 max2=max21=-1;counts=[0,0];bad=[0,0];num=0
 for mask in upsets(n):
  A={w for w in range(1<<n) if mask>>w&1};v2=v21=0
  for w in A:
   direct=p2_definition(A,w,n);pair=p2_pair(A,w,n)
   assert direct & {i for i in range(n) if w>>i&1} == pair,(n,mask,w,direct,pair)
   v2+=len(direct);v21+=len(direct-p1(A,w,n))
  inband=all(w in A for w in range(1<<n) if 2*w.bit_count()>=n+2) and all(2*w.bit_count()>=n-4 for w in A)
  for idx,value in enumerate([v2,v21]):
   current=[max2,max21][idx]
   if value>current:
    if idx==0:max2=value
    else:max21=value
    counts[idx]=1;bad[idx]=int(not inband)
   elif value==current:counts[idx]+=1;bad[idx]+=int(not inband)
  num+=1
 row=dict(n=n,upsets=num,max_phi2=max2,max_phi21=max21,maximizer_counts=counts,outside_band_maximizer_counts=bad)
 results.append(row);print(row,flush=True)
# The literal source formula differs from its occupied-coordinate tables.


# Fully enumerate n=3, r=2, M=3 arrays, including positive duplicates.
n=3;r=2;M=3;arrays=0;states=0
for tup in itertools.product(range(n),repeat=r*M):
 clauses=[tup[k*r:(k+1)*r] for k in range(M)]
 A={w for w in range(1<<n) if all(any(w>>i&1 for i in c) for c in clauses)}
 for w in A:
  S=set();edges=[]
  for c in clauses:
   pos=[i for i in c if w>>i&1]
   distinct=set(pos)
   if len(distinct)==1:S |= distinct
   if len(pos)==2 and len(distinct)==2:edges.append(distinct)
  C=set().union(*edges) if edges else set()
  bad=[e for e in edges if e&S]
  Vbad=set().union(*bad) if bad else set()
  assert S==p1(A,w,n)
  secondonly=p2_definition(A,w,n)-S
  assert C-Vbad <= secondonly
  assert len(secondonly)>=len(C)-2*len(bad)
  states+=1
 arrays+=1
print('clause_graph_exhaustive',arrays,states,flush=True)

# Exact arithmetic margins, no huge objects instantiated.
n=10**14;h=10**7;r=10**6
checks={
 'graph_lower':str(Fraction(r*r,12)-Fraction(288*r**3,n)),
 'conditional_lower_target':str(Fraction(r*r,24)),
 'averaged_lower':str(Fraction(r*r,2592)),
 'band_upper':10*h,
 'strict_margin':str(Fraction(r*r,2592)-10*h),
 'upper_coverage_parameter':str(Fraction(32*r*r,3*n)),
 'shifted_power_parameter':str(r*(Fraction(2,h)+Fraction(2,n)))}
assert Fraction(r*r,12)-Fraction(288*r**3,n)>=Fraction(r*r,24)
assert Fraction(r*r,2592)>10*h
assert r*(Fraction(2,h)+Fraction(2,n))<Fraction(1,4)
# Stable decimal evaluation of the exact conditional first moments at central endpoints.
numeric=[]
with localcontext() as ctx:
 ctx.prec=60
 for s in [n//2-h,n//2,n//2+h]:
  z=Decimal(1)-Decimal(s)/n
  scale=(2*z)**r # equals M*q0
  ma=Decimal(4*r*(r-1)*(s-1))/Decimal(n*n)*(2*z)**(r-2)
  # q0 itself is < 10^(-300000); replacing 1-q0 by 1 affects
  # these displayed decimals below the 60-digit precision.
  coverage=Decimal(s)*(1-(-ma).exp())
  numeric.append(dict(s=s,Mq0=str(scale),Ma_i=str(ma),coverage_poisson_approx=str(coverage)))
output=dict(small_cube=results,clause_arrays=arrays,successful_array_supports=states,exact_margins=checks,numerical_sanity=numeric,seconds=time.time()-start)
(root/'verification.json').write_text(json.dumps(output,indent=2),encoding='utf8')
print('exact_margins',checks,flush=True)
print('ALL CHECKS PASSED',flush=True)
