from pathlib import Path
from fractions import Fraction as F
from itertools import product,permutations
from math import factorial,comb
from collections import Counter
import json,time,sys
BASE=Path(__file__).resolve().parents[1]; CHECKS=0
def ck(x):
 global CHECKS
 CHECKS+=1
 assert x,CHECKS
def comps(s,k,positive=False):
 low=1 if positive else 0
 if k==1:
  if s>=low:yield(s,)
 else:
  for j in range(low,s-low*(k-1)+1):
   for tail in comps(s-j,k-1,positive):yield(j,)+tail
def parts(s,low=1):
 if s==0:yield();return
 for j in range(low,s+1):
  for tail in parts(s-j,j):yield(j,)+tail
def rising(s,j):
 v=1
 for i in range(j):v*=s+i
 return v
def fifth(x):
 if x==1:return F(1),F(1)
 hi=1
 while F(hi)**5<x:hi*=2
 den=1<<64; a=0;b=hi*den
 while b-a>1:
  mid=(a+b)//2
  if F(mid,den)**5<x:a=mid
  else:b=mid
 ck(F(a,den)**5<=x<=F(b,den)**5)
 return F(a,den),F(b,den)
def budget(sizes,kappa,u):
 s=sum(sizes); k=len(sizes); a=F(1); Kpow=F(1)
 for v,h in zip(sizes,kappa):
  a*=F(v,s)**v
  Kpow*=F(s,h)**(s*v)*F(h+u,s+u)**((s+u)*v)
 ck(Kpow>=1)
 zlo=zhi=F(0)
 for occ in comps(u,k):
  multi=factorial(u); ratio=F(1)
  for v,h,b in zip(sizes,kappa,occ):
   multi//=factorial(b)
   ratio*=F(v+b,h+u)**(v+b)/F(v,h)**v
  lo,hi=fifth(ratio**6);zlo+=multi*lo;zhi+=multi*hi
 ck(zlo**(5*s)*Kpow**6>=a**u)
 return 1
def tail_records(maxs):
 records=0; cases=0
 for s in range(1,maxs+1):
  C=sum(F(comb(s-1,k-1)*rising(s,k-1),factorial(k)) for k in range(1,s+1))
  ck(C<=6**(s-1)); ordered=0
  for sizes in parts(s):
   k=len(sizes); perm=factorial(k)
   for c in Counter(sizes).values():perm//=factorial(c)
   ordered+=perm
   a=F(1); multi=factorial(s)
   for v in sizes:a*=F(v,s)**v;multi//=factorial(v)
   ck(multi*a<=1)
   for N in sorted({1,2,4,16,1<<s}):
    if k>N:continue
    coeff=F(comb(N,k)*rising(s,k-1)*multi,N**k)
    # W=coeff*A^(6/5), bound=(s)_(k-1)/k!*A^(1/5).
    ck(coeff**5*a**6<=F(rising(s,k-1),factorial(k))**5*a)
    records+=perm
  ck(ordered==2**(s-1));cases+=len({1,2,4,16,1<<s})
 return records,cases
def coefficients():
 # Delannoy grid recurrence is independent of the author's binomial sum.
 D=[[0]*49 for _ in range(49)]
 for i in range(49):
  for j in range(49):D[i][j]=1 if i==0 or j==0 else D[i-1][j]+D[i][j-1]+D[i-1][j-1]
 rows=[]
 for n in range(49):
  c=sum(F(comb(n,j)*rising(n+1,j),factorial(j+1)) for j in range(n+1))
  d=sum(comb(n,j)**2*2**j for j in range(n+1))
  ck(d==D[n][n]);ck(c<=d<=6**n)
  rows.append({'n':n,'C':str(c),'D':d})
 ck(6**5<2**13)
 return rows
def rootcredits():
 cases=0
 for c in [1,2,3]:
  for widths in product(range(1,5),repeat=c):
   pi=[F(1,1<<w) for w in widths];den=F(1)
   for q in pi:den*=q
   credit=min(pi)/den
   for u in [1,2,3]:
    for ua in comps(u,c):
     mult=[1] if c==1 else [v*rising(u+1,c-2) for v in ua]
     ck(sum(mult)==rising(u,c-1))
     ck(sum(F(m)*q/den for m,q in zip(mult,pi))>=rising(u,c-1)*credit)
     cases+=1
 return cases
def fwht(a):
 a=list(a);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
  h*=2
 return a
def or_family():
 rows=[]
 for n in range(1,11):
  vals=[-1]+[1]*((1<<n)-1);w=fwht(vals);z=F(1,1<<n)
  ck(w[0]==(1<<n)-2);ck(all(v==-2 for v in w[1:]));ck(sum(v*v for v in w)==1<<(2*n))
  for j in range(n):ck(F(sum(vals[x]!=vals[x^(1<<j)] for x in range(1<<n)),1<<n)==2*z)
  # All positive implicants contain a positive literal, exactly the n primes.
  for j in range(n):ck(vals[1<<j]==1 and vals[0]==-1)
  activated=[vals[x>>1] if x&1 else -1 for x in range(1<<(n+1))]
  af=fwht(activated)
  ck(af[0]==-2);ck(af[1]==-((1<<(n+1))-2))
  ck(all(abs(v)==2 for v in af[2:]));ck(sum(v*v for v in af)==1<<(2*(n+1)))
  ai=[F(sum(activated[x]!=activated[x^(1<<j)] for x in range(1<<(n+1))),1<<(n+1)) for j in range(n+1)]
  ck(ai==[1-z]+[z]*n)
  ck(sum(comb(n,s) for s in range((n+1)//2,n+1))>=1<<(n-1))
  D=F(1)
  for j in range(n):D*=1+F(1,4*n)
  D-=1;ck(D<=F(1,3))
  alpha_lo,alpha_hi=fifth(F(1,64));ck(alpha_lo>F(1,4))
  b_lo=alpha_lo/(4*(1+alpha_lo));ck(b_lo>F(1,20))
  data=[]
  for s in range(1,n+1):
   J5=F(factorial(s)**5,n**(5*s)*2**(s-1))
   # General intersection envelope's exact gap: 2^(5gap)=[4(s/(s+1))^(s+1)]^6.
   gapbase=4*F(s,s+1)**(s+1);ck(1<=gapbase<2)
   # Exact complete selected star probability, interval from original factors.
   pref=F(factorial(s),24*n**s*s*s*(s+1))/D
   qlo=pref*b_lo**(s-1)
   ck(qlo>=F(factorial(s),8*n**s*s*s*(s+1)*20**(s-1)))
   traces=None
   if s<=6:
    keys=set()
    for root in range(s):
     for seq in permutations([j for j in range(s) if j!=root]):keys.add((root,seq))
    traces=len(keys);ck(traces==factorial(s))
   data.append({'s':s,'J_power5':str(J5),'selected_star_probability_lower':str(qlo),'actual_traces':traces})
  rows.append({'n':n,'D_activated':str(D),'s_records':data})
  (BASE/'out/OR_CHECKPOINT.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
 # Symbolic all-dimensional tail obstruction: no truth-table enumeration at 8192.
 ck(6**5<8192);ck(6**5<=7776)
 return rows
def general_records(maxs):
 count=0
 for s in range(1,maxs+1):
  for k in range(1,s+1):
   for sizes in comps(s,k,True):
    for kappa in product(*(range(v,s+1) for v in sizes)):
     for u in [1,2]:count+=budget(sizes,kappa,u)
 return count
def main():
 spec=json.loads((BASE/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
 if '--spec' in sys.argv:
  general=sum(2*prod_int(s-v+1 for v in sizes) for s in range(1,5) for k in range(1,s+1) for sizes in comps(s,k,True))
  spec['case_count']={'general_records':general,'physical_OR_functions':10,'coefficient_cases':49,'tail_records_domain':'s<=10, unique N in 1,2,4,16,2^s','pilot_general_s_max':2,'pilot_tail_s_max':4}
  (BASE/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8');print(json.dumps(spec['case_count']));return
 start=time.perf_counter();pilot='--pilot' in sys.argv
 tr,tc=tail_records(4 if pilot else 10)
 gen=general_records(2 if pilot else 4);coeff=coefficients();roots=rootcredits();ors=or_family()
 out={'status':'PASS','mode':'pilot' if pilot else 'full','assertions':CHECKS,'seconds':time.perf_counter()-start,'ordered_tail_records':tr,'tail_s_N_cases':tc,'general_records':gen,'root_credit_records':roots,'coefficients':coeff,'OR':ors}
 (BASE/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps({k:out[k] for k in ['status','mode','assertions','seconds','ordered_tail_records','general_records','root_credit_records']}))
def prod_int(xs):
 v=1
 for x in xs:v*=x
 return v
if __name__=='__main__':main()
