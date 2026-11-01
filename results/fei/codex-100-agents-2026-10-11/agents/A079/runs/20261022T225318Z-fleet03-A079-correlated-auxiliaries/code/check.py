"""v1. Independent exact controller DP and complete source-reference lifting."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd,lcm
import json,time,sys,hashlib

ROOT=Path(__file__).resolve().parents[1]
A=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
B=tuple(1-a*a for a in A)
assertions=0
def ok(test):
 global assertions
 assertions+=1
 assert test,assertions

def fw(v):
 w=list(v);k=1
 while k<len(w):
  for a in range(0,len(w),2*k):
   for j in range(a,a+k):
    x,y=w[j],w[j+k];w[j],w[j+k]=x+y,x-y
  k*=2
 return w
def prob(v):return tuple(F(x*x,len(v)**2) for x in fw(v))
def plus(*terms):
 d={}
 for weight,vec in terms:
  for p,c in vec.items():d[p]=d.get(p,F(0))+weight*c
 return {p:c for p,c in d.items() if c}
@lru_cache(None)
def factor(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
@lru_cache(None)
def log(q):return plus((1,factor(q.numerator)),(-1,factor(q.denominator)))
def ce(p,q):
 out={}
 for a,b in zip(p,q):
  if a:
   ok(b>0);out=plus((1,out),(-a,log(b)))
 return out
def entropy(p):return ce(p,p)
def sign(v):
 if not v:return 0
 d=lcm(*(x.denominator for x in v.values()));pos=1;neg=1
 for p,c in v.items():
  e=int(d*c)
  if e>0:pos*=p**e
  else:neg*=p**(-e)
 return (pos>neg)-(pos<neg)
def influence(p,i):return sum((x for j,x in enumerate(p) if j>>i&1),F(0))
def energy(p):return sum((x*j.bit_count() for j,x in enumerate(p)),F(0))
def remove(v,i,b):return tuple(x for j,x in enumerate(v) if j>>i&1==b)
def marginal(p,i):
 n=len(p)//2;out=[]
 for j in range(n):
  base=(j&((1<<i)-1))+((j>>i)<<(i+1))
  out.append(p[base]+p[base+(1<<i)])
 return tuple(out)
def erasure(p,i):return plus((1,entropy(p)),(-1,entropy(marginal(p,i))))
def edges(v):
 return sum((F(x!=v[j^(1<<i)],len(v)) for j,x in enumerate(v)
             for i in range(len(v).bit_length()-1)),F(0))
def profile(n,kind=0):
 raw=[1 if kind==0 else 1+(i+1)**2 for i in range(1<<n)]
 total=sum(raw);return tuple(F(x,total) for x in raw)

@lru_cache(None)
def structure(state):
 free=[i for i,x in enumerate(state) if x==-1]; ar=[];br=[]
 for v in range(1<<len(free)):
  orig=sum((b<<i) for i,b in enumerate(state) if b!=-1)
  orig+=sum(((v>>j)&1)<<i for j,i in enumerate(free))
  ar.append(A[orig]);br.append(B[orig])
 pa,pb=prob(ar),prob(br)
 p=pa+pb
 return tuple(ar),tuple(br),p,sum(pb),entropy(p),energy(p)
def wrap(state,h):
 a,b,*_=structure(state)
 return tuple(x+z*y*h[t] for z in (1,-1) for t in range(len(h)) for x,y in zip(a,b))
def reference(state,r):
 a,b,p,beta,k,j=structure(state);size=len(a);pa,pb=p[:size],p[size:]
 return tuple(pa[u]*(t==0) for t in range(len(r)) for u in range(size))+tuple(pb[u]*r[t] for t in range(len(r)) for u in range(size))
def dump(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):dump(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [dump(v) for v in x]
 return x
def save(n,x):(ROOT/'out'/n).write_text(json.dumps(dump(x),indent=2)+'\n',encoding='utf-8',newline='')

def controller_review():
 states=sorted(product((-1,0,1),repeat=4),key=lambda s:s.count(-1))
 values={};counts={};local_fail=0;transitions=0;records=[]
 for s in states:
  a,b,p,beta,h,j=structure(s);actual=wrap(s,(1,))
  ok(prob(actual)==p);ok(energy(p)==edges(actual))
  best={};number=1;acts=[]
  for q,i in enumerate(k for k,x in enumerate(s) if x==-1):
   children=[tuple(x if k!=i else bit for k,x in enumerate(s)) for bit in (0,1)]
   h0,j0=structure(children[0])[-2:];h1,j1=structure(children[1])[-2:]
   inf=influence(p,q);ok(j-(j0+j1)/2==inf)
   ok((structure(children[0])[3]+structure(children[1])[3])/2==beta)
   delta=plus((1,h),(-F(1,2),h0),(-F(1,2),h1))
   debit=plus((1,delta),(-4*inf,{2:F(1)}))
   if sign(debit)>0:local_fail+=1
   candidate=plus((1,debit),(F(1,2),values[children[0]]),(F(1,2),values[children[1]]))
   if sign(plus((1,candidate),(-1,best)))>0:best=candidate
   eb=erasure(p,q)
   ok(sign(plus((1,delta),(-1,eb)))>=0)
   acts.append(dict(bit=i,cost=debit));transitions+=1
   number+=counts[children[0]]*counts[children[1]]
  values[s]=best;counts[s]=number
  records.append(dict(state=s,best=best,actions=acts))
 root=(-1,)*4
 ok(values[root]=={2:F(1),3:F(-9,16)})
 ok(counts[root]==238145);ok(local_fail==10);ok(transitions==108)
 ok(sign(plus((1,{2:F(1,8)}),(-1,values[root])))>0)
 save('review_controller.json',dict(status='PASS',states=81,transitions=transitions,
      represented_trees=counts[root],locally_failing_rate4=local_fail,root_max=values[root],states_certificate=records))

def generic_lift(pilot=False):
 states=list(product((-1,0,1),repeat=4)) if not pilot else [(-1,)*4,(0,-1,-1,-1)]
 ns=range(3) if not pilot else [1]
 cases=0;steps=0
 for n in ns:
  codes=range(1<<(1<<n)) if not pilot else [0,1,3]
  for code in codes:
   h=tuple(1-2*((code>>i)&1) for i in range(1<<n));ph=prob(h)
   for s in states:
    a,b,ps,beta,k,j=structure(s);m=len(a).bit_length()-1
    v=wrap(s,h);pv=prob(v);ok(all(x in (-1,1) for x in v))
    ok(entropy(pv)==plus((1,k),(beta,entropy(ph))))
    ok(energy(pv)==j+beta*energy(ph))
    for kind in [0,1]:
     r=profile(n,kind);qr=reference(s,r)
     ok(sum(qr)==1);c=ce(pv,qr)
     ok(c==plus((1,k),(beta,ce(ph,r))))
     for i in range(n):
      h0,h1=remove(h,i,0),remove(h,i,1);p0,p1=prob(h0),prob(h1)
      r0=profile(n-1,kind);r1=profile(n-1,1-kind)
      child0,child1=wrap(s,h0),wrap(s,h1)
      eb=erasure(pv,m+i);source_eb=erasure(ph,i)
      ok(eb==plus((beta,source_eb)))
      ok(influence(pv,m+i)==beta*influence(ph,i))
      c0=ce(prob(child0),reference(s,r0));c1=ce(prob(child1),reference(s,r1))
      actual=plus((1,eb),(F(1,2),c0),(F(1,2),c1),(-1,c))
      src=plus((1,source_eb),(F(1,2),ce(p0,r0)),(F(1,2),ce(p1,r1)),(-1,ce(ph,r)))
      ok(actual==plus((beta,src)));steps+=1
    cases+=1
 save('pilot.json' if pilot else 'generic_lift.json',dict(status='PASS',gate_cases=cases,source_step_cases=steps,states=len(states)))

def point(a,b,r):
 n=a+b+r
 return tuple(1-2*((x&((1<<a)-1))==0)+2*(x==0) for x in range(1<<n))
def source_g(a,b):return tuple(1-2*((x&((1<<a)-1))==0) for x in range(1<<(a+b)))
def floor(a,b,r,reference):
 true=prob(point(a,b,r));s=F(1,1<<a);e=F(2,1<<(a+b+r));mu=1-2*s;N=1<<(a+b)
 dat=tuple(sum(true[t+N*u] for u in range(1<<r)) for t in range(N))
 rd=tuple((1-e/s)*reference[t]+(e/s)*mu*(t==0)+2*e/N for t in range(N))
 out=tuple(rd[t]*true[t+N*u]/dat[t] for u in range(1<<r) for t in range(N))
 ok(sum(out)==1)
 return out
def calibrate(r,empty):
 if empty==1:return tuple(F(i==0) for i in range(len(r)))
 return tuple(empty if i==0 else x*(1-empty)/(1-r[0]) for i,x in enumerate(r))
def sourced():
 cases=[];root=(-1,)*4
 states=[root,(-1,-1,-1,0),(-1,-1,-1,1)]+list(product((0,1),repeat=4))
 for a,b,r in product((2,3),(0,1),(1,2)):
  h=point(a,b,r);ph=prob(h);ref=prob(source_g(a,b));q=floor(a,b,r,ref)
  e=F(2,len(h));N=a+b+r
  c=entropy(ref);W=plus((1,c),(10*e*N,{2:F(1)}))
  ok(sign(plus((1,W),(-1,ce(ph,q))))>=0)
  v=marginal(ref,0);mu0=1-F(2,1<<(a-1));rc=calibrate(v,mu0*mu0)
  h0,h1=remove(h,0,0),remove(h,0,1)
  q0=floor(a-1,b,r,rc);q1=marginal(q,0)
  ok(h0==point(a-1,b,r));ok(all(x==1 for x in h1))
  c0=ce(prob(source_g(a-1,b)),rc)
  W0=plus((1,c0),(20*e*(N-1),{2:F(1)}));off=ce(prob(h1),q1)
  debit=plus((1,erasure(ph,0)),(F(1,2),W0),(F(1,2),off))
  ok(sign(plus((1,W),(-1,debit),(-e,{2:F(1)})))>=0)
  # Reference-only atoms survive in q1; a constant child is not reset to a point.
  ok(sum(q1)==1 and q1[0]<1);ok(sign(off)>0)
  for st in states:
   aa,bb,ps,beta,k,j=structure(st)
   parent=wrap(st,h);child0,child1=wrap(st,h0),wrap(st,h1)
   ok(ce(prob(parent),reference(st,q))==plus((1,k),(beta,ce(ph,q))))
   ok(ce(prob(child0),reference(st,q0))==plus((1,k),(beta,ce(prob(h0),q0))))
   ok(ce(prob(child1),reference(st,q1))==plus((1,k),(beta,off)))
   eb=erasure(prob(parent),len(aa).bit_length()-1)
   ok(eb==plus((beta,erasure(ph,0))))
   ok(sign(plus((1,k),(beta,W),(-1,k),(-beta,debit),(-beta*e,{2:F(1)})))>=0)
  cases.append(dict(a=a,b=b,r=r,seed_norm=e,source_floor_cost=ce(ph,q),source_envelope=W,
                    off_full_cost=off,child_envelope=W0,source_increment=debit))
 save('sourced_step.json',dict(status='PASS',source_roots=8,controller_states_per_root=19,
       old_terminal_retained=True,normalizers_retained=True,roots=cases))

def collision_guard():
 h=( -1,1,1,1,1,1,1,1 );root=(-1,)*4
 v=wrap(root,h);p=prob(v);zi=len(v).bit_length()-2
 p0,p1=prob(remove(v,zi,0)),prob(remove(v,zi,1))
 ok((p0[0],p1[0])==(F(169,1024),F(25,1024)))
 ok(p0!=p1)
 q=reference(root,profile(3,1));qm=marginal(q,zi)
 lhs=plus((1,erasure(p,zi)),(F(1,2),ce(p0,qm)),(F(1,2),ce(p1,qm)))
 ok(sign(plus((1,ce(p,q)),(-1,lhs)))>=0)
 save('collision_guard.json',dict(status='PASS',seed=h,child_vacua=[p0[0],p1[0]],
      child_spectra_equal=False,no_reset_preserves_bank=True,
      unsupported='Fresh reset after address deletion; tagged factorization fails for biased seeds'))

def main():
 start=time.monotonic();pilot='--pilot' in sys.argv
 if pilot:generic_lift(True)
 else:controller_review();generic_lift();sourced();collision_guard()
 output=dict(status='PASS',pilot=pilot,assertions=assertions,seconds=time.monotonic()-start,
             helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 save('pilot_summary.json' if pilot else 'validation.json',output);print(json.dumps(output))
if __name__=='__main__':main()
