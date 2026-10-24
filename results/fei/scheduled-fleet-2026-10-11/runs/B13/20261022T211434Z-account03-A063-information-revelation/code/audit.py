from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];checks=0

def ck(x):
 global checks
 checks+=1
 assert x,checks

def add(x,y):return x[0]+y[0],x[1]+y[1]
def scale(a,x):return (a*x[0],a*x[1]) if a>=0 else (a*x[1],a*x[0])
def ln_series(y):
 z=(y-1)/(y+1);s=F(0)
 for k in range(40):s+=2*z**(2*k+1)/(2*k+1)
 return s,s+2*z**81/(81*(1-z*z))
LN2=ln_series(F(2))
def lg(x):
 assert x>0
 k=0;y=x
 while y<1:y*=2;k-=1
 while y>=2:y/=2;k+=1
 if y==1:return F(k),F(k)
 u=ln_series(y);return F(k)+u[0]/LN2[1],F(k)+u[1]/LN2[0]
def entropy(p):
 a=(F(0),F(0))
 for x in p:
  if x:a=add(a,scale(-x,lg(x)))
 return a

def law(tab):
 N=len(tab)
 return [F(sum(v*(-1 if (t&x).bit_count()%2 else 1) for x,v in enumerate(tab))**2,N*N) for t in range(N)]
def restrict(tab,i,y):return [tab[x] for x in range(len(tab)) if (x>>i&1)==y]
def facts(tab):
 p=law(tab);n=len(tab).bit_length()-1;d=[sum((v for s,v in enumerate(p) if s>>i&1),F(0)) for i in range(n)]
 H=entropy(p);TC=scale(-1,H)
 for x in d:TC=add(TC,entropy([x,1-x]))
 for j in range(n):ck(d[j]==F(sum(tab[x]!=tab[x^(1<<j)] for x in range(len(tab))),len(tab)))
 return p,H,TC,add((4*sum(d),4*sum(d)),scale(-1,H))
start=time.perf_counter();scalars=[]
for m in range(2,13):
 d=F(1,2**(m-1));p0=(1-d)**2;r=2*d-d*d
 H=add(scale(-p0,lg(p0)),scale(-r,lg(d*d)))
 TC=add(scale(m,entropy([d,1-d])),scale(-1,H));S=add((4*(1+(m-2)*d),)*2,scale(-1,H))
 ck(TC[1]<F(3,5));ck(S[0]>=2)
 scalars.append({'m':m,'TC_lt_3_over_5':True,'S4_twist_ge_2':True})
rows=[]
for n in [2,3,4]:
 v=[-1]+[1]*(2**n-1)
 tab=[-1 if not(t&1) and t&2 else (v[t>>3] if t&1 and t&4 else 1) for t in range(2**(n+3))]
 ck(sum(law(tab))==1)
 aa=[restrict(tab,1,y) for y in [0,1]]
 f0=facts(aa[0]);f1=facts(aa[1]);ck(f1[0]==[f0[0][s^1] for s in range(len(f0[0]))])
 leaves=[restrict(t,2,y) for t in aa for y in [0,1]];ff=[facts(t) for t in leaves];tc=(F(0),F(0))
 for f in ff:tc=add(tc,scale(F(1,4),f[2]))
 ck(tc[1]<F(3,10));ck(ff[2][3][0]>=2 and ff[3][3][0]>=2)
 inactive=leaves[3];ck(sum(1 for z in law(inactive) if z)==1)
 for y in [0,1]:ck(facts(restrict(inactive,0,y))[3]==(0,0))
 rows.append({'n':n,'literal_character_sum_check':True,'twisted_lineage_verified':True,'terminal_TC_lt_3_over_10':True,'querying_x_destroys_reserve_control':True})
d=F(1,16);p0=(1-d)**2;r=2*d-d*d;H=add(scale(-p0,lg(p0)),scale(-r,lg(d*d)));TC=add(scale(5,entropy([d,1-d])),scale(-1,H));ck(TC[0]>F(3,10))
for a in range(-2,3):
 for b in range(-2,3):
  for c in range(-2,3):
   for d in range(-2,3):ck(a*b*(c*c+d*d)-c*d*(a*a+b*b)==(a*c-b*d)*(b*c-a*d))
result={'status':'PASS','checks':checks,'runtime_seconds':time.perf_counter()-start,'method':'separate literal character sums and rational atanh remainder; no campaign helper imported','scalar_dimensions':scalars,'physical_fixtures':rows,'signed_packet_integer_cases':625,'external_independent_review':'PENDING'}
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in result.items() if k not in ['scalar_dimensions','physical_fixtures']}))
