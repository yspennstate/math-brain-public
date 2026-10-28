from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product,combinations
import json,sys,time,math
R=Path(__file__).resolve().parent.parent
start=time.monotonic();checks=0;SCALE=1<<44
def ck(x):
 global checks
 checks+=1
 assert x,checks
def lnunit(y):
 z=(y-1)/(y+1);v=z;s=F(0)
 for j in range(24):s+=2*v/(2*j+1);v*=z*z
 return s,s+2*v/(49*(1-z*z))
L2=lnunit(F(2))
@lru_cache(None)
def log2(x):
 x=F(x);ck(x>0);k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
 if y<1:k-=1;y*=2
 ck(1<=y<2);lo,hi=lnunit(y);lo=k+lo/L2[1];hi=k+hi/L2[0]
 return (lo.numerator*SCALE//lo.denominator,-((-hi.numerator*SCALE)//hi.denominator))
def walsh(v):
 v=v[:];h=1
 while h<len(v):
  for i in range(0,len(v),2*h):
   for j in range(i,i+h):v[j],v[j+h]=v[j]+v[j+h],v[j]-v[j+h]
  h*=2
 return v
def physical_influence(v,n):return F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v)) for j in range(n)),len(v))
def source_primes(v,widths,clauses):
 # Full monotone truth-table reconstruction, no candidate-only acceptance.
 n=sum(widths)*2;allbits=(1<<n)-1;pos=set();neg=set()
 for x,value in enumerate(v):
  if value==1 and all(v[x^(1<<j)]==-1 for j in range(n) if x>>j&1):pos.add(x)
  if value==-1 and all(v[x^(1<<j)]==1 for j in range(n) if not(x>>j&1)):neg.add(allbits^x)
 r=len(widths);X=clauses[:r];Y=clauses[r:]
 xt=[sum(1<<j for j in z) for z in product(*[[i for i in range(n) if m>>i&1] for m in X])]
 yt=[sum(1<<j for j in z) for z in product(*[[i for i in range(n) if m>>i&1] for m in Y])]
 ck(pos=={a|b for a in xt for b in Y});ck(neg==set(X)|set(yt))
 transitions=0
 for pa in pos:
  for ch in pos:
   for cm in X:
    if pa&cm==ch&cm:continue
    for dm in Y:
     if pa&ch&(cm|dm):ck(ch&dm==dm);transitions+=1
 return {'positive_primes':len(pos),'negative_primes':len(neg),'marked_transitions':transitions}
def fixture(widths):
 r=len(widths);wtotal=sum(widths);n=2*wtotal;N=1<<n;t=[F(1,2**w) for w in widths];p=[1-x for x in t]
 q=math.prod(p);rho=sum(t,F(0));D=sum((w*x/y for w,x,y in zip(widths,t,p)),F(0))
 clauses=[];offset=0
 for w in widths*2:clauses.append(((1<<w)-1)<<offset);offset+=w
 truth=[]
 for x in range(N):
  U=all(x&m for m in clauses[:r]);V=any(x&m==m for m in clauses[r:]);truth.append(1 if U and V else -1)
 W=walsh(truth);I=physical_influence(truth,n);v=F(sum(z*z for z in W[1:]),N*N)
 ck(I==2*q*D);ck(v==4*q*(1-q)*(1-q*(1-q)))
 # Construct reference only from local widths. No Fourier coefficients enter it.
 norm=F(0);badnorm=F(0);occ=[0]*r;run_count=0;cost_lo=cost_hi=0;pre_lo=pre_hi=0;refund_lo=refund_hi=0
 ts=t*2;ps=p*2;ws=widths*2
 for a in range(1,N):
  active=[j for j,m in enumerate(clauses) if a&m];K=len(active)
  factors=[ts[j]**2/ps[j] if j in active else ps[j] for j in range(2*r)]
  mu=math.prod(factors);density=F(0)
  # Sum actual first-anchor events independently via conditional local draws.
  # Prefix/suffix products avoid division by a copied output density.
  prefix=[F(1)]
  for z in factors:prefix.append(prefix[-1]*z)
  suffix=[F(1)]*(2*r+1)
  for j in range(2*r-1,-1,-1):suffix[j]=suffix[j+1]*factors[j]
  ck(len(active)==len(set(active)))
  for j in active:
   joint=ts[j]/(2*rho)*F(1,2**ws[j]-1)*prefix[j]*suffix[j+1]
   ck(joint==mu/(2*rho));density+=joint;run_count+=1
  Q=K*mu/(2*rho);ck(density==Q and 0<Q<=1)
  ck(Q/(mu/(2*rho))==K) # actual posterior is uniform, entropy refund log K
  norm+=density;badnorm+=K*density
  for j in active:occ[j%r]+=W[a]*W[a]
  if W[a]:
   lo,hi=log2(1/Q);cost_lo+=W[a]*W[a]*lo;cost_hi+=W[a]*W[a]*hi
   lo,hi=log2(2*rho/mu);pre_lo+=W[a]*W[a]*lo;pre_hi+=W[a]*W[a]*hi
   lo,hi=log2(F(K));refund_lo+=W[a]*W[a]*lo;refund_hi+=W[a]*W[a]*hi
 ck(norm==1);ck(badnorm>1)
 ck(run_count==sum((2**w-1)*2**(n-w) for w in ws))
 ck(all(F(z,N*N)==4*q*tj for z,tj in zip(occ,t)))
 ck(I==sum((F(z,N*N)*w/(2*pj) for z,w,pj in zip(occ,widths,p)),F(0)))
 den=N*N*SCALE
 ck(cost_hi<7*I*den);ck(cost_lo<=pre_hi-refund_lo and pre_lo-refund_hi<=cost_hi)
 # Independently evaluate the exact aggregate identity (4) using interval arithmetic.
 b0lo=b0hi=0
 for pj in p:
  lo,hi=log2(1/pj);b0lo+=2*lo;b0hi+=2*hi
 lo,hi=log2(2*rho);b0lo+=lo;b0hi+=hi
 formlo=v*b0lo;formhi=v*b0hi
 for tj,pj,z in zip(t,p,occ):
  lo,hi=log2(pj/tj);formlo+=F(2*z,N*N)*lo;formhi+=F(2*z,N*N)*hi
 formlo-=F(refund_hi,N*N);formhi-=F(refund_lo,N*N)
 ck(F(cost_lo,N*N)<=formhi and formlo<=F(cost_hi,N*N))
 row={'widths':widths,'n':n,'truth_inputs':N,'actual_anchor_runs':run_count,'I':str(I),'v':str(v),'Q_total_mass':str(norm),'invalid_double_anchor_mass':str(badnorm),'C_interval':[str(F(cost_lo,den)),str(F(cost_hi,den))],'refund_interval':[str(F(refund_lo,den)),str(F(refund_hi,den))]}
 if widths in ([1,1],[2,2,2,2]):row['source_prime_review']=source_primes(truth,widths,clauses)
 ck(time.monotonic()-start<180)
 return row
def review_certificates():
 x=F(17,20);phi=sum((x**c/F((c+1)*(c+2)) for c in range(17)),F(0))+x**17/18
 ck(phi<F(4,5));ck(L2[0]>F(2,3));ck(sum((F(1,math.factorial(k)) for k in range(5)),F(0))>F(8,3))
 rootcases=0
 for m in range(1,5):
  activity=[F(i+1,4096) for i in range(m)];D=math.prod(1+a for a in activity)-1
  for z in (1,2,4,8):
   ck(z*sum(activity)<=F(1,16));mass=F(0)
   for bits in range(1,1<<m):
    count=bits.bit_count();mass+=math.prod(activity[i] for i in range(m) if bits>>i&1)*z**(count-1)*F(4,5)**count/D
   ck(mass<=F(16,19));rootcases+=1
 budgetcases=0
 for w in range(32,129):
  ck((48*w)**2<=2**w)
  if w>=64:
   ck((48*w)**4<=2**w);ck(8*(2**w-1)>=w*w)
   for L in (1,2,2**(w//4)):
    Z=F(2**w,48*L*w);ck(Z*Z>=2**w);budgetcases+=1
 for w in range(1,257):
  t=F(1,2**w);ck((1-t)*(1+F(3,2*w))<=F(4,3));ck(F(w)/(1-t)>=2)
 # Exact common-good-clause checks and the source boundary beyond its budget proof.
 vectors=[[F(3,4) if j==ell else F(1,60) for j in range(16)] for ell in range(16)]
 for L in range(1,9):
  ck(all(sum(row)<=4 for row in vectors[:L]));threshold=F(2*L*4,16)
  common=[j for j in range(16) if all(row[j]<=threshold for row in vectors[:L])];ck(len(common)>=8)
 ck(not any(all(row[j]<=F(1,2) for row in vectors) for j in range(16)))
 return {'offspring_upper_certificate':str(phi),'root_product_cases':rootcases,'budget_pairs':budgetcases,'entropy_widths':256,'common_clause_cases':9}
def main():
 spec=json.loads((R/'FROZEN_SPEC.json').read_text(encoding='utf-8'));pilot='--pilot' in sys.argv
 cert=review_certificates();rows=[]
 for widths in spec['pilot_width_lists' if pilot else 'full_width_lists']:rows.append(fixture(widths))
 elapsed=time.monotonic()-start;ck(elapsed<(55 if pilot else 180))
 result={'status':'PASS','helper_version':spec['helper_version'],'pilot':pilot,'rows':rows,'review_certificates':cert,'functions':len(rows),'truth_inputs':sum(z['truth_inputs'] for z in rows),'actual_anchor_runs':sum(z['actual_anchor_runs'] for z in rows),'assertions':checks,'seconds':elapsed}
 (R/'out').mkdir(exist_ok=True);tag='PILOT' if pilot else 'CHECK'
 (R/'out'/f'{tag}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('rows','review_certificates')}))
if __name__=='__main__':main()
