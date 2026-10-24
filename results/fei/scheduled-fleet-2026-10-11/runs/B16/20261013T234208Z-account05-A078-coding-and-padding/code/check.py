from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import argparse,json,time,math
ROOT=Path(__file__).resolve().parents[1]; START=time.perf_counter(); CHECKS=0
def ck(ok):
 global CHECKS
 CHECKS+=1; assert ok
 if time.perf_counter()-START>55: raise TimeoutError('55 second frozen guard')
def walsh(t):
 a=list(t); h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h): a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
  h*=2
 return a
def pair(t,i):
 u=[];v=[]
 for a in range(len(t)//2):
  x=(a&((1<<i)-1))+((a>>i)<<(i+1)); y=x+(1<<i)
  u.append(F(t[x]+t[y],2));v.append(F(t[x]-t[y],2))
 return walsh(u),walsh(v),len(u)
def edge(t,i):return F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def ln_unit(q):
 z=(q-1)/(q+1); total=F(0)
 for j in range(40):total+=2*z**(2*j+1)/F(2*j+1)
 err=2*z**81/(81*(1-z*z))
 return total,total+err
LN2=ln_unit(F(2))
@lru_cache(None)
def log(q):
 q=F(q); e=q.numerator.bit_length()-q.denominator.bit_length()
 q/=F(2)**e
 if q<1:q*=2;e-=1
 lo,hi=ln_unit(q)
 return F(e)+lo/LN2[1],F(e)+hi/LN2[0]
def phi(p,q):
 if not p or not q:return F(0),F(0)
 return plus(plus(scale(log(p+q),p+q),scale(log(p),-p)),scale(log(q),-q))
def S(u,d,h):return plus(scale(plus(phi((u+h)**2,d*d),phi((u-h)**2,d*d)),F(1,4)),scale(phi(u*u,d*d),F(-1,2)))
def factors(n):
 a={};p=2
 while p*p<=n:
  while n%p==0:a[p]=a.get(p,0)+1;n//=p
  p+=1
 if n>1:a[n]=a.get(n,0)+1
 return a
def addlog(dst,q,c):
 if not q or not c:return
 q=F(q)
 for num,sgn in [(q.numerator,1),(q.denominator,-1)]:
  for p,e in factors(num).items():
   dst[p]=dst.get(p,F(0))+c*sgn*e
   if not dst[p]:del dst[p]
def combine(dst,src,c=F(1)):
 for p,q in src.items():
  dst[p]=dst.get(p,F(0))+q*c
  if not dst[p]:del dst[p]
def Bmap(t,i):
 u,v,D=pair(t,i); out={}
 for a,b in zip(u,v):
  p=F(a,D)**2;q=F(b,D)**2
  if p and q:
   addlog(out,p+q,p+q);addlog(out,p,-p);addlog(out,q,-q)
 return out
def nonnegative(d):
 if not d:return True
 result=(F(0),F(0))
 for p,c in d.items():result=plus(result,scale(log(F(p)),c))
 return result[0]>=0
def review():
 for gm in range(16):
  for hm in range(16):
   G=[1-2*((gm>>(s+2*x))&1) for y in range(2) for x in range(2) for s in range(2)]
   H=[1-2*((hm>>(s+2*y))&1) for y in range(2) for x in range(2) for s in range(2)]
   t=G+H
   for i in range(3):
    al=edge(t,i);ck(al==(edge(G,i)+edge(H,i))/2)
    d=Bmap(t,i);combine(d,Bmap(G,i),F(-1,2));combine(d,Bmap(H,i),F(-1,2))
    for sign in [1,-1]:
     bound={2:2*al} if al else {};combine(bound,d,F(sign));ck(nonnegative(bound))
 return {'source_claim':'A077-ONE-SHARED-BIT-SIGNED-TRANSPORT','version':1,'pairs':256,'data_splits':768,'verdict':'ACCEPT_AT_STATED_SCOPE','repair_supplied':False}
def run(pilot):
 rows=[]; direct_cases=0
 for k in ([2,4] if pilot else [2,4,6,8,10,12,32,64]):
  N=1<<k; al=F(1,N); beta=F(1,1<<(k//2)); private=al/2
  D=plus(scale(S(-al,al,beta),N-1),S(1-al,al,beta)); ratio=scale(D,1/private)
  analytic=F(k-4)
  if k>=4:ck(ratio[0]>=analytic)
  if k>=4:ck(F(3*k,1)/N<=1)
  if k==4:ck(ratio[0]>2)
  totalI=F(k,4)+F(k+1,2*N)+(1-beta+al)/2
  Hupper=2*F(k+1,N)+F(k,2)+2
  ck(Hupper<4*totalI);ck((1-beta+al)/2>=F(1,4))
  if k in [2,4,6]:
   h=[-1 if sum(((s>>(2*j))&1)*((s>>(2*j+1))&1) for j in range(k//2))%2 else 1 for s in range(N)]
   g=[-1 if s==0 and x==0 else 1 for x in range(2) for s in range(N)]
   # Explicit z branch selection, no extra copied truth-table rows.
   table=g+[h[s] for x in range(2) for s in range(N)]
   u,v,DD=pair(table,k); gh=walsh(g);hh=walsh(h)
   for C in range(N):
    ug=F(gh[C],2*N);dg=F(gh[C+N],2*N);hv=F(hh[C],N)
    ck(dg==-al);ck(ug==(1-al if C==0 else -al));ck(hv*hv==beta*beta)
    for zfreq in [0,1]:
     idx=C+zfreq*N;ck(F(u[idx],DD)==(ug+(hv if zfreq==0 else -hv))/2);ck(F(v[idx],DD)==dg/2)
   ck(edge(table,k)==private)
   ck(sum(edge(table,j) for j in range(k+2))==totalI)
   ck(edge(table,k+1)==(1-beta+al)/2)
   direct_cases+=1
  unit=1<<100; lo=F((ratio[0]*unit).__floor__(),unit); hi=F((ratio[1]*unit).__ceil__(),unit)
  ck(lo<=ratio[0] and hi>=ratio[1])
  rows.append({'shared_k':k,'Inf_private':str(private),'D_over_Inf_lower':str(lo),'D_over_Inf_upper':str(hi),'proved_lower_k_minus4':k-4 if k>=4 else None,'I_total':str(totalI),'L_private_over_Inf_analytic_lower':'3*2^(k/4)','selector_L_over_Inf_upper':8})
 rev=review() if not pilot else None
 return {'status':'PASS','helper':'shared-bent-spike-v1','pilot':pilot,'assertions':CHECKS,'seconds':time.perf_counter()-START,'closed_row_cases':len(rows),'actual_full_tables':direct_cases,'rows':rows,'independent_review':rev}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args(); result=run(args.pilot)
 out=ROOT/'out';out.mkdir(exist_ok=True)
 (out/('pilot.json' if args.pilot else 'full.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
