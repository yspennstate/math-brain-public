"""v2: independent direct character sums; exact rational prime-log certificates."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import lcm
import json, time, hashlib, sys
ROOT=Path(__file__).resolve().parents[1]
A=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
B=tuple(1-x*x for x in A)
checks=0
def ok(x):
 global checks
 checks+=1
 assert x,checks
def dump(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):dump(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [dump(v) for v in x]
 return x
def save(n,x):
 (ROOT/'out'/n).write_text(json.dumps(dump(x),indent=2)+'\n',encoding='utf-8',newline='')
@lru_cache(None)
def coeff(v):
 N=len(v)
 return tuple(F(sum(x*(-1 if (s&t).bit_count()%2 else 1) for t,x in enumerate(v)),N) for s in range(N))
def prob(v):return tuple(x*x for x in coeff(tuple(v)))
def add(*terms):
 out={}
 for k,d in terms:
  for p,c in d.items():out[p]=out.get(p,F(0))+k*c
 return {p:c for p,c in out.items() if c}
@lru_cache(None)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
@lru_cache(None)
def log(q):return add((1,factors(q.numerator)),(-1,factors(q.denominator)))
def ce(p,q):
 out={}
 for a,b in zip(p,q):
  if a:
   ok(b>0);out=add((1,out),(-a,log(b)))
 return out
def ent(p):return ce(p,p)
def kl(p,q):return add((1,ce(p,q)),(-1,ent(p)))
@lru_cache(None)
def _sign(v):
 if not v:return 0
 d=lcm(*(c.denominator for p,c in v));pos=1;neg=1
 for p,c in v:
  e=int(d*c)
  if e>0:pos*=p**e
  else:neg*=p**(-e)
 return (pos>neg)-(pos<neg)
def sign(v):return _sign(tuple(sorted(v.items())))
def marginal(p,i):
 out=[]
 for x in range(len(p)//2):
  j=(x&((1<<i)-1))+((x>>i)<<(i+1));out.append(p[j]+p[j+(1<<i)])
 return tuple(out)
def restrict(v,i,b):return tuple(x for j,x in enumerate(v) if (j>>i)&1==b)
def erasure(p,i):return add((1,ent(p)),(-1,ent(marginal(p,i))))
def mean(v):return F(sum(v),len(v))
def cal(r,z):
 if z==1:return tuple(F(t==0) for t in range(len(r)))
 ok(r[0]<1)
 return tuple(z if t==0 else (1-z)*v/(1-r[0]) for t,v in enumerate(r))
def tail(r):return tuple(v/(1-r[0]) for v in r[1:])
def profile(N,k):
 v=tuple(F(1+(t+1)**(k+1)) for t in range(N));return tuple(x/sum(v) for x in v)
def mix(r,s,e):return tuple((1-e)*x+e*y for x,y in zip(r,s))
@lru_cache(None)
def rows(state):
 free=[i for i,b in enumerate(state) if b==-1];a=[];b=[]
 for x in range(1<<len(free)):
  j=sum(v<<i for i,v in enumerate(state) if v!=-1)+sum(((x>>k)&1)<<i for k,i in enumerate(free))
  a.append(A[j]);b.append(B[j])
 return tuple(a),tuple(b)
def truth(a,b,h,s):return tuple(x+s*y*z for z in h for x,y in zip(a,b))
def coherent(a,b,h,r,s):
 ac,bc=coeff(a),coeff(b);m=mean(h)
 ok(r[0]==m*m)
 q=tuple((ac[u]+s*m*bc[u])**2 if t==0 else bc[u]**2*r[t] for t in range(len(r)) for u in range(len(a)))
 ok(sum(q)==1)
 return q
def fresh(a,b,h,r,s,eps=F(0),target=None):
 z=mean(h)**2
 c=cal(r,z)
 if z<1 and eps:
  t=mix(tail(c),target,eps);c=(z,)+tuple((1-z)*x for x in t)
 return coherent(a,b,h,c,s),c
def tagged(a,b,h,r):
 ac,bc=coeff(a),coeff(b)
 return tuple(ac[u]**2*(t==0) for t in range(len(h)) for u in range(len(a)))+tuple(bc[u]**2*r[t] for t in range(len(h)) for u in range(len(a)))
def coarse(p,m,kind):
 # Exact vacuum atoms plus one tail block (seed query), or one tail block per U (controller query).
 if kind=='seed':return tuple(p[:m])+(sum(p[m:]),)
 return tuple(p[:m])+tuple(sum(p[t*m+u] for t in range(1,len(p)//m)) for u in range(m))
def step(a,b,h,r,s,kind,i):
 v=truth(a,b,h,s);p=prob(v);q=coherent(a,b,h,r,s);m=len(a);j=i if kind=='controller' else m.bit_length()-1+i
 qb=marginal(q,j);pb=marginal(p,j)
 occ=add((1,kl(p,q)),(-1,kl(pb,qb)))
 ok(sign(occ)>=0)
 costs=[];credits=[];children=[]
 for bit in (0,1):
  if kind=='seed':aa,bb,hh,rr=a,b,restrict(h,i,bit),marginal(r,i)
  else:aa,bb,hh,rr=restrict(a,i,bit),restrict(b,i,bit),h,r
  vv=truth(aa,bb,hh,s);pp=prob(vv);ok(vv==restrict(v,j,bit));ok(all(x in (-1,1) for x in vv))
  qq,rc=fresh(aa,bb,hh,rr,s)
  cr=kl(coarse(pp,len(aa),kind),coarse(qb,len(aa),kind))
  delta=add((1,ce(pp,qb)),(-1,ce(pp,qq)))
  ok(delta==cr);ok(sign(cr)>=0)
  costs.append(ce(pp,qq));credits.append(cr);children.append((aa,bb,hh,rc,pp,qq))
 actual=add((1,erasure(p,j)),(F(1,2),costs[0]),(F(1,2),costs[1]),(-1,ce(p,q)))
 predicted=add((-1,occ),(-F(1,2),credits[0]),(-F(1,2),credits[1]))
 ok(actual==predicted);ok(sign(actual)<=0)
 return actual,children,credits,occ
def review(a,b,h,r,target):
 v=tuple(truth(a,b,h,1)+truth(a,b,h,-1));p=prob(v);q=tagged(a,b,h,r);z=len(v).bit_length()-2
 pc=[prob(truth(a,b,h,s)) for s in (1,-1)]
 pbar=marginal(p,z);js=add((1,ent(pbar)),(-F(1,2),ent(pc[0])),(-F(1,2),ent(pc[1])))
 beta=F(sum(b),len(b));rr=mean(h)**2;t=r[0];eps=F(1,8)
 fresh_refs=[fresh(a,b,h,r,s,eps,target) for s in (1,-1)]
 binary=kl((rr,1-rr),(t,1-t));excess={}
 if rr<1:
  ph=prob(h);pt=tail(ph);rt=tail(r);mt=mix(rt,target,eps)
  excess=add((1,kl(pt,mt)),(-1,kl(pt,rt)))
 pred=add((-1,js),(-beta,binary),(beta*(1-rr),excess))
 actual=add((1,erasure(p,z)),(F(1,2),ce(pc[0],fresh_refs[0][0])),(F(1,2),ce(pc[1],fresh_refs[1][0])),(-1,ce(p,q)))
 ok(actual==pred)
 if rr<1:ok(sign(add((1,log(F(8,7))),(-1,excess)))>=0)
 if beta>0 and rr==F(1,4) and t==F(1,2):ok(sign(add((-1,actual),(-beta/F(24),{2:F(1)})))>0)
 return fresh_refs,actual
def domain(pilot):
 states=[(-1,)*4]+[tuple(bit if k==i else -1 for k in range(4)) for i in range(4) for bit in (0,1)]+list(product((0,1),repeat=4))
 if pilot:states=[(-1,)*4,(0,0,0,0)]
 cases=actions=0
 for n in range(3):
  codes=range(1<<(1<<n)) if not pilot else range(min(3,1<<(1<<n)))
  for code in codes:
   h=tuple(1-2*((code>>t)&1) for t in range(1<<n))
   for st in states:
    if time.monotonic()>deadline:raise TimeoutError("frozen runtime limit")
    a,b=rows(st)
    for k in (0,1):
     target=profile(len(h)-1,1-k) if len(h)>1 else ()
     r=(F(1,2),)+tuple(x/2 for x in profile(len(h)-1,k)) if len(h)>1 else (F(1),)
     refs,olddebit=review(a,b,h,r,target)
     for s,(_,rc) in zip((1,-1),refs):
      for kind,d in [('controller',len(a).bit_length()-1),('seed',n)]:
       for i in range(d):step(a,b,h,rc,s,kind,i);actions+=1
      cases+=1
 return cases,actions
def funded_fixture():
 # Both active-query seed children nonconstant, with means 1/4 and 3/4.
 a,b=rows((-1,)*4);h=tuple(-1 if t in (0,1,2,4) else 1 for t in range(16))
 ok(mean(h)==F(1,2));r=(F(1,2),)+tuple(x/2 for x in profile(15,0));target=profile(15,1)
 refs,old=review(a,b,h,r,target);first=[];following=[];allterminal=[]
 for s,(_,rc) in zip((1,-1),refs):
  inc,kids,credit,occ=step(a,b,h,rc,s,'seed',0)
  costs=[]
  for aa,bb,hh,rr,pp,qq in kids:
   ok(mean(hh) in (F(1,4),F(3,4)));ok(len(set(hh))==2)
   nxt=profile(len(hh)-1,1)
   qnew,rnew=fresh(aa,bb,hh,rr,s,F(1,64),nxt)
   extra=add((1,ce(pp,qnew)),(-1,ce(pp,qq)))
   bound=F(sum(bb),len(bb))*(1-mean(hh)**2)
   ok(sign(add((bound,log(F(64,63))),(-1,extra)))>=0)
   # A second query from the genuinely changed current profile, with both complete terminals.
   follow,grand,_,_=step(aa,bb,hh,rnew,s,'seed',0)
   ok(sign(follow)<=0);following.append(follow)
   costs.append(extra);allterminal.append(dict(sign=s,seed_mean=mean(hh),truth=truth(aa,bb,hh,s),reference=qnew,spectrum=pp,second_profile=rnew,extra=extra,post_reset_follow=follow))
  first.append(add((1,inc),(F(1,2),costs[0]),(F(1,2),costs[1])))
 whole=add((1,old),(F(1,2),first[0]),(F(1,2),first[1]))
 ok(sign(add((-1,whole),(-F(1,256),{2:F(1)})))>0)
 ok(21**18>2**79);ok(64**32<2*63**32)
 # The old source price is unchanged; all added transactions are paid by its saved refund.
 save('funded_fixture.json',dict(status='PASS',seed=h,source=r,first_target=target,first_reset_increment=old,post_query_increments=first,complete_added_increment=whole,reserve_strictly_greater_than='1/256',full_terminals=allterminal,old_source_bank_renewed=False))
def guard():
 a,b=rows((-1,)*4);h=(-1,1,1,1);ac,bc=coeff(a),coeff(b)
 actual=(ac[0]-mean(h)*bc[0])**2;naive=(ac[0]-F(1,3)*bc[0])**2
 ok(actual==F(1,256));ok(naive==0)
 save('support_guard.json',dict(status='PASS',actual=actual,naive=naive,finite_incoming_reference=['1/9','8/27','8/27','8/27']))
def main():
 global deadline
 start=time.monotonic();pilot='--pilot' in sys.argv;deadline=start+(55 if pilot else 180)
 cases,actions=domain(pilot)
 if not pilot:funded_fixture();guard()
 result=dict(status='PASS',pilot=pilot,assertions=checks,signed_cases=cases,query_actions=actions,seconds=time.monotonic()-start,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),arithmetic='Fraction prime-log identities; integer-power signs; direct character sums',dimension_escalated=False)
 save('pilot_summary.json' if pilot else 'validation.json',result);print(json.dumps(result))
if __name__=='__main__':main()
