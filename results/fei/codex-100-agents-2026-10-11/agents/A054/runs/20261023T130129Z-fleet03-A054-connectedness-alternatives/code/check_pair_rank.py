from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
from math import lcm
import json,time,sys
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=cases=critical_cases=positive_release=0;examples={}
def ck(x):
 global checks
 assert x
 checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('frozen runtime cap55')
def rank(vs):
 b={}
 for v in vs:
  while v:
   k=v.bit_length()
   if k in b:v^=b[k]
   else:b[k]=v;break
 return len(b)
@lru_cache(None)
def bases(d):return tuple(b for b in combinations(range(1,1<<d),d) if rank(b)==d)
@lru_cache(None)
def factor(x):
 out={};p=2
 while p*p<=x:
  while x%p==0:out[p]=out.get(p,0)+1;x//=p
  p+=1
 if x>1:out[x]=out.get(x,0)+1
 return out
def add(*terms):
 out={}
 for vec,m in terms:
  for p,q in vec.items():out[p]=out.get(p,F(0))+m*q
 return {p:q for p,q in out.items() if q}
def sign(vec):
 den=lcm(*(q.denominator for q in vec.values())) if vec else 1;a=b=1
 for p,q in vec.items():
  z=int(q*den)
  if z>=0:a*=p**z
  else:b*=p**(-z)
 return (a>b)-(a<b)
@lru_cache(maxsize=4096)
def stats(vals):
 N=len(vals);n=N.bit_length()-1;a=list(vals);k=1
 while k<N:
  for x in range(0,N,2*k):
   for j in range(k):u=a[x+j];v=a[x+j+k];a[x+j]=u+v;a[x+j+k]=u-v
  k*=2
 h={}
 for z in a:
  q=F(z*z,N*N)
  if q:
   h=add((h,1),(factor(q.denominator),q),(factor(q.numerator),-q))
 w=tuple(sum(vals[x]!=vals[x^v] for x in range(N)) for v in range(N))
 return tuple(a),w,h,sum(w[1<<i] for i in range(n))
def scatter(x,ids):return sum(((x>>j)&1)<<i for j,i in enumerate(ids))
def childvals(vals,A):
 n=len(vals).bit_length()-1;C=[i for i in range(n) if i not in A]
 return tuple(tuple(vals[scatter(u,A)|scatter(x,C)] for x in range(1<<len(C))) for u in range(4))
def amin(vals):
 _,w,_,_=stats(vals);N=len(vals);d=N.bit_length()-1
 return F(min(sum(min(w[v],N-w[v]) for v in b) for b in bases(d)),N)
def minimum(vals,A):
 N=len(vals);n=N.bit_length()-1;C=[i for i in range(n) if i not in A];d=len(C);w=stats(vals)[1]
 wc={v:w[scatter(v,C)] for v in range(1,1<<d)}
 bw=min(bases(d),key=lambda b:sum(wc[v] for v in b));mw=sum(wc[v] for v in bw)
 lift={q:min((w[scatter(q,A)|scatter(z,C)],scatter(q,A)|scatter(z,C)) for z in range(1<<d)) for q in range(1,4)}
 bq=min(bases(2),key=lambda b:sum(lift[q][0] for q in b));mq=sum(lift[q][0] for q in bq)
 b=tuple(lift[q][1] for q in bq)+tuple(scatter(v,C) for v in bw)
 ck(rank(b)==n);ck(sum(w[v] for v in b)==mw+mq)
 for costs,dim,val in [(wc,d,mw),({q:lift[q][0] for q in lift},2,mq)]:
  levels=sorted({0,N,*costs.values()})
  integ=sum((hi-lo)*(dim-rank([v for v,c in costs.items() if c<=lo])) for lo,hi in zip(levels,levels[1:]))
  ck(integ==val)
 return mw+mq,b,mw,mq
def rematch(vals,A,r,v,s):
 C=[i for i in range(len(vals).bit_length()-1) if i not in A];out=list(vals)
 for x in range(1<<len(C)):
  z=scatter(r,A)|scatter(x,C);out[z]*=s*(-1 if (v&x).bit_count()%2 else 1)
 return tuple(out)
def transform(vals,b):
 out=[]
 for y in range(len(vals)):
  x=0
  for j,v in enumerate(b):
   if y>>j&1:x^=v
  out.append(vals[x])
 return tuple(out)
def deficit(vals,K):
 _,_,h,i=stats(vals);return add((h,1),({2:F(K*i,len(vals))},-1))
small={n:[tuple(-1 if mask>>x&1 else 1 for x in range(1<<n)) for mask in range(1<<(1<<n))] for n in range(4)}
ck(all(sign(deficit(v,2))<=0 for n in range(3) for v in small[n]))
ck(all(sign(deficit(v,3))<=0 for n in range(4) for v in small[n]))
best={};bestmasks=[]
for mask,vals in enumerate(small[3]):
 D=deficit(vals,2);sgn=sign(add((D,1),(best,-1)))
 if not bestmasks or sgn>0:best=D;bestmasks=[mask]
 elif sgn==0:bestmasks.append(mask)
ck(sign(best)>0);ck(2**144>7**49)
pilot='--pilot' in sys.argv
domains=[(3,range(16) if pilot else range(256))]
if not pilot:domains.append((4,sorted({1,*((1103515245*j+12345)&65535 for j in range(16))})))
for n,masks in domains:
 N=1<<n;d=n-2;Nc=1<<d
 for mask in masks:
  root=tuple(-1 if mask>>x&1 else 1 for x in range(N));_,_,H0,I0=stats(root)
  critical=(n==3 and mask in bestmasks) or (n==4 and mask==1);K=2 if n==3 else 3
  for A in combinations(range(n),2):
   C=[i for i in range(n) if i not in A];ch=childvals(root,A)
   Hbar=add(*[(stats(h)[2],F(1,4)) for h in ch]);t=sum(map(amin,ch))/4
   S=add(({2:K*t},1),(Hbar,-1));D0=deficit(root,K)
   if critical:ck(sign(S)>=0);ck(minimum(root,A)[0]==I0)
   for r in range(4):
    h=ch[r];hc=stats(h);coeff=[stats(g)[0] for g in ch]
    for v in range(Nc):
     B=sum((1-2*F(hc[1][1<<j],Nc) for j in range(d) if v>>j&1),F(0))
     C0=sum((F(sum(ch[r^(1<<j)][x]*h[x] for x in range(Nc)),Nc) for j in range(2)),F(0))
     Cv=sum((F(sum(ch[r^(1<<j)][x]*h[x]*(-1 if (v&x).bit_count()%2 else 1) for x in range(Nc)),Nc) for j in range(2)),F(0))
     for s in [1,-1]:
      new=rematch(root,A,r,v,s);a,w,H,I=stats(new)
      ck(F(I-I0,N)==(B+C0-s*Cv)/4)
      for T in range(Nc):
       for z in range(4):
        rhs=sum((-1 if (z&u).bit_count()%2 else 1)*(s*coeff[u][T^v] if u==r else coeff[u][T]) for u in range(4))
        ck(a[scatter(z,A)|scatter(T,C)]==rhs)
      J,b,mw,mq=minimum(new,A);release=F(I-J,N);ck(release>=0)
      reset=transform(new,b);ck(stats(reset)[2]==H);ck(stats(reset)[3]==J)
      chnew=childvals(new,A);ck(add(*[(stats(h)[2],F(1,4)) for h in chnew])==Hbar);ck(sum(map(amin,chnew))/4==t)
      Pi=add((H0,1),(H,-1),({2:F(K*(J-I0),N)},1));L=add((H,1),(Hbar,-1))
      for u in [F(0),release]:
       rhs=add((L,1),({2:K*(F(J,N)+u-t)},-1),(Pi,1),({2:K*u},1))
       ck(rhs==add((D0,1),(S,1)))
      if critical:ck(sign(Pi)>=0);critical_cases+=1
      cases+=1;positive_release+=int(release>0)
      e={'n':n,'mask':mask,'A':A,'branch':r,'character':v,'sign':s,'K':K,'critical_fixture':critical,'I0_count':I0,'Inew_count':I,'J_count':J,'normalizer':N,'basis':b,'internal_count':mw,'quotient_count':mq,'phase_price_sign':sign(Pi)}
      keys=[]
      if release>0:keys.append('positive_rank_release')
      if critical and release>0:keys.append('critical_positive_rank_release')
      if critical and release>0 and sign(Pi)>0:keys.append('critical_strict_price')
      if sign(Pi)<0:keys.append('nonstationary_negative_price')
      if critical and sign(add((L,1),({2:K*(F(J,N)-t)},-1)))<=0 and sign(add((D0,1),(S,1)))>0:keys.append('apparent_payment_loses_original_price')
      if mask==0 and v==0 and s==-1:keys.append('pair_sign_entropy_guard')
      if n==4 and release>0:keys.append('four_bit_rank_oracle')
      if n==4 and critical and release>0:keys.append('four_bit_critical_release')
      for key in keys:
       if key not in examples:examples[key]=e
expected=768 if pilot else 15552;ck(cases==expected)
out={'status':'PASS','pilot':pilot,'assertions':checks,'competitors':cases,'critical_competitors':critical_cases,'positive_release_competitors':positive_release,'three_bit_global_D2_maxima':bestmasks,'seconds':time.perf_counter()-start,'arithmetic':'integer counts, Fraction prime-log vectors, exact integer-product sign certificates','examples':list(examples)}
(R/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
if not pilot:(R/'out/EXAMPLES.json').write_text(json.dumps(examples,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
