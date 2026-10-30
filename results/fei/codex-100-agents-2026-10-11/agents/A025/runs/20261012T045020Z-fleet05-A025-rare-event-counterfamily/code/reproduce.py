"""Independent full-table reproduction and rational replay of all saved log signs."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import json,time
R=Path(__file__).resolve().parents[1];START=time.monotonic();CK=0;SCALE=1<<104
def check(a):
 global CK
 assert a;CK+=1
 if time.monotonic()-START>60:raise TimeoutError('reproduction cap')
def ln_series(x):
 # A different truncation length from the original checker, with exact tails.
 z=(x-1)/(x+1);p=z;s=Q(0)
 for j in range(35):s+=2*p/(2*j+1);p*=z*z
 return s,s+2*p/(71*(1-z*z))
LN2=ln_series(Q(2))
@lru_cache(None)
def log_bounds(x):
 e=x.bit_length()-1
 if x==1<<e:return e*SCALE,e*SCALE
 a,b=ln_series(Q(x,1<<e));lo=(e+a/LN2[1])*SCALE;hi=(e+b/LN2[0])*SCALE
 return lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)
def interval(expr):
 lo=hi=0
 for x,c in expr.items():
  if not c:continue
  a,b=log_bounds(x)
  if c>=0:lo+=c*a;hi+=c*b
  else:lo+=c*b;hi+=c*a
 return lo,hi
def Walsh(vals):
 v=list(vals);step=1
 while step<len(v):
  for j in range(0,len(v),2*step):
   for i in range(j,j+step):a,b=v[i],v[i+step];v[i]=a+b;v[i+step]=a-b
  step*=2
 return v
def edges(vals):
 n=len(vals).bit_length()-1
 return sum(vals[x]!=vals[x^(1<<j)] for j in range(n) for x in range(len(vals)) if x>>j&1==0)
def table(k,r,L,order):
 ans=[]
 for t in range(1<<len(order)):
  xx=[0]*L;yy=[0]*L;zz=[0]*L
  for bit,(j,kind,i) in enumerate(order):
   b=(t>>bit)&1
   if kind=='x':xx[j]|=b<<i
   elif kind=='y':yy[j]=b
   else:zz[j]|=b<<i
  event=1
  for j in range(L):
   neg=sum(((xx[j]>>(2*i))&1)*((xx[j]>>(2*i+1))&1) for i in range(k//2))%2
   event=0 if zz[j] else neg+int(xx[j]==0)*yy[j]*event
   check(event in (0,1))
  ans.append(1-2*event)
 return tuple(ans)
@lru_cache(maxsize=8192)
def direct_ledger(f):
 N=len(f)
 if min(f)==max(f):return 0,0,0
 g=f[::2];h=f[1::2];mismatch=sum(a!=b for a,b in zip(g,h))
 w=Walsh(f);expr=Counter();dn=0
 for s in range(0,N,2):
  A,B=w[s]**2,w[s+1]**2;dn+=B
  for x,c in [(A+B,A+B),(A,-A),(B,-B)]:
   if x:expr[x]+=c
 expr[2]-=4*dn;lo,hi=interval(expr)
 if not any(expr.values()):bad=False
 else:check(lo>0 or hi<0);bad=lo>0
 check(dn==2*N*mismatch)
 boundary=edges(tuple(a*b for a,b in zip(g,h)))
 l=direct_ledger(g);rr=direct_ledger(h)
 return 2*mismatch+l[0]+rr[0],2*boundary+l[1]+rr[1],(2*boundary if bad else 0)+l[2]+rr[2]

full=json.loads((R/'out'/'full_RESULTS.json').read_text());rows=[]
for k,r,L in [(2,1,2),(2,0,3),(4,0,2),(4,1,2)]:
 levels=list(reversed(range(L)));x=[(j,'x',i) for j in levels for i in range(k)];y=[(j,'y',0) for j in levels];z=[(j,'z',i) for j in levels for i in range(r)]
 names={'selector_first':y+z+x,'control_first':z+y+x,'data_first':x+z+y,'control_data_selector':z+x+y}
 expected=next(row for row in full['rows'] if (row['k'],row['r'],row['depth'])==(k,r,L))
 for name,order in names.items():
  f=table(k,r,L,order);N=len(f);vals=direct_ledger(f);e=expected['orders'][name]
  check(Q(vals[0],N)==Q(e['I']));check(Q(vals[1],N)==Q(e['Q']));check(Q(vals[2],N)==Q(e['bad_credit']))
  rows.append({'k':k,'r':r,'depth':L,'order':name,'I':str(Q(vals[0],N)),'Q':str(Q(vals[1],N)),'bad_credit':str(Q(vals[2],N))})
print('Independent full-cube ledgers:',len(rows),flush=True)
for cert in full['sign_certificates']:
 expr={int(x):int(c) for x,c in cert['expression']};lo,hi=interval(expr)
 check(lo>0 if cert['sign']>0 else hi<0 if cert['sign']<0 else not expr)
res={'status':'PASS','method':'independent full truth tables, direct Walsh/edges, 35-term rational log replay at 104-bit scale','full_cube_tree_ledgers':len(rows),'log_sign_certificates_replayed':len(full['sign_certificates']),'assertions_passed':CK,'seconds':time.monotonic()-START,'rows':rows,'independent_agent_review':'NOT_CLAIMED: second implementation by A025'}
(R/'out'/'REPRODUCTION_RESULTS.json').write_text(json.dumps(res,indent=2));print(json.dumps({k:v for k,v in res.items() if k!='rows'}))
