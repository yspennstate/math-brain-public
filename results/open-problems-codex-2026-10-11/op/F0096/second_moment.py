"""Exact fixed-degree Hamilton-cycle second moments by overlap transfer matrices.
All polynomial coefficients and finite enumerations use integers/Fractions.
"""
import math,itertools,json,time
from fractions import Fraction
from pathlib import Path
P=Path(__file__).parent

def add(x,y):
 z=[0]*max(len(x),len(y))
 for i,v in enumerate(x):z[i]+=v
 for i,v in enumerate(y):z[i]+=v
 return z
def scale(x,a,shift=0):return [0]*shift+[a*v for v in x]
def ident():return [[ [1],[0] ],[ [0],[1] ]]
def times_matrix(B,a):
 # M_a(x)=[[a(a-1),2ax],[a,x]].
 return [[add(scale(B[i][0],a*(a-1)),scale(B[i][1],a)),
          add(scale(B[i][0],2*a,1),scale(B[i][1],1,1))] for i in range(2)]
def matrix_add(B,C):return [[add(B[i][j],C[i][j]) for j in range(2)] for i in range(2)]
def weights(degrees):
 B=ident()
 for d in degrees:B=times_matrix(B,d-2)
 return add(B[0][0],B[1][1])
def mixed_weights(n3,n4):
 # Sum ordered matrix products over all degree multisets, divided later
 # by binomial(n,n4). Only one DP row is stored.
 row=[None]*(n4+1);row[0]=ident()
 for b in range(1,n4+1):row[b]=times_matrix(row[b-1],2)
 for a in range(1,n3+1):
  new=[None]*(n4+1);new[0]=times_matrix(row[0],1)
  for b in range(1,n4+1):new[b]=matrix_add(times_matrix(row[b],1),times_matrix(new[b-1],2))
  row=new
 return add(row[n4][0][0],row[n4][1][1]),math.comb(n3+n4,n4)
def first(degrees):
 n=len(degrees);S=sum(degrees)
 assert S%2==0, 'Configuration pairing requires even total degree'
 return Fraction(math.factorial(n-1)*math.prod(d*(d-1) for d in degrees),2*math.prod(S-(2*j+1) for j in range(n)))
def conditional_mean(degrees,W=None,divisor=1):
 n=len(degrees);R=sum(degrees)-2*n
 assert R%2==0, 'Residual pairing requires even total degree'
 if W is None:W=weights(degrees)
 out=Fraction(1)
 for k in range(n):
  r=n-k
  if 2*r>R:continue
  out+=Fraction(W[k]*math.factorial(r-1),2*divisor*math.prod(R-(2*j+1) for j in range(r)))
 return out
def brute_weights(degrees):
 n=len(degrees);W=[0]*(n+1)
 for bits in itertools.product([0,1],repeat=n):
  p=sum(bits[i-1]==0 and bits[i]==1 for i in range(n));val=2**p
  for i,d in enumerate(degrees):
   k=bits[i-1]+bits[i];a=d-2
   val*=1 if k==2 else a if k==1 else a*(a-1)
  W[sum(bits)]+=val
 return W
def cycle_orders(n):return [(0,)+p for p in itertools.permutations(range(1,n)) if p[0]<p[-1]]
def exact_pairings(degrees):
 owners=[i for i,d in enumerate(degrees) for _ in range(d)];cycles=cycle_orders(len(degrees))
 count=sumH=sumH2=loop3=0;simplecount=simpleH=simpleH2=0
 def rec(stubs,edges):
  nonlocal count,sumH,sumH2,loop3,simplecount,simpleH,simpleH2
  if not stubs:
   count+=1;mult={};loops=False;simple=True
   for a,b in edges:
    u,v=owners[a],owners[b];key=tuple(sorted((u,v)))
    if u==v or key in mult:simple=False
    if u==v and degrees[u]==3:loops=True
    mult[key]=mult.get(key,0)+1
   h=sum(math.prod(mult.get(tuple(sorted((cyc[i],cyc[(i+1)%len(cyc)]))),0) for i in range(len(cyc))) for cyc in cycles)
   sumH+=h;sumH2+=h*h;loop3+=loops
   if simple:simplecount+=1;simpleH+=h;simpleH2+=h*h
   return
  a=stubs[0]
  for i in range(1,len(stubs)):rec(stubs[1:i]+stubs[i+1:],edges+[(a,stubs[i])])
 rec(list(range(len(owners))),[])
 n=len(degrees)
 average_F=sum((conditional_mean([degrees[i] for i in order]) for order in cycles),Fraction(0))/len(cycles)
 mean=first(degrees);second=mean*average_F
 assert Fraction(sumH,count)==mean
 assert Fraction(sumH2,count)==second
 return {'degrees':degrees,'pairings':count,'sumH':sumH,'sumH2':sumH2,'E_H':str(mean),'E_H2':str(second),
         'ratio':float(second/(mean*mean)),'loop3_probability':str(Fraction(loop3,count)),
         'simple_pairings':simplecount,'simple_sumH':simpleH,'simple_sumH2':simpleH2}
def row(n3,n4):
 degrees=[3]*n3+[4]*n4;n=len(degrees)
 W,divisor=mixed_weights(n3,n4)
 mean=first(degrees);F=conditional_mean(degrees,W,divisor);ratio=F/mean
 return {'n':n,'n3':n3,'n4':n4,'second_over_first_squared':float(ratio),
         'log_ratio_per_vertex':(math.log(ratio.numerator)-math.log(ratio.denominator))/n,
         'paley_zygmund_lower_bound_configuration':float(1/ratio)}
def main():
 out={'transfer_checks':[],'exact_pairings':[],'mixed_rows':[]}
 for ds in [[3]*4,[4,4,3,3],[3,4,5,3,4],[5]*5]:
  assert weights(ds)==brute_weights(ds)
  out['transfer_checks'].append({'degrees':ds,'coefficients':weights(ds),'passed':True})
 for ds in [[3]*4,[4,4,3,3]]:
  r=exact_pairings(ds);out['exact_pairings'].append(r);print(r,flush=True)
  (P/'second_moment.json').write_text(json.dumps(out,indent=2))
 for n in [12,24,48,96]:
  for fraction in [0.,.25,.5,1.]:
   n4=2*(int(n*fraction)//2);r=row(n-n4,n4);out['mixed_rows'].append(r);print(r,flush=True)
   (P/'second_moment.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':main()
