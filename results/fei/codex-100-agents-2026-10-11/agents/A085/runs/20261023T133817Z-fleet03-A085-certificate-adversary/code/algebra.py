from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,time,json,hashlib
import log_intervals as IV
ROOT=Path(__file__).resolve().parents[1]
ROW=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
checks=actions=positive=0
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
def save(name,obj):
 def conv(x):
  if isinstance(x,F):return str(x)
  if isinstance(x,dict):return {str(k):conv(v) for k,v in x.items()}
  if isinstance(x,(list,tuple)):return [conv(v) for v in x]
  return x
 (ROOT/'out'/name).write_text(json.dumps(conv(obj),indent=2)+'\n',encoding='utf-8')
def add(*terms):
 z={}
 for c,v in terms:
  for p,e in v.items():z[p]=z.get(p,F(0))+c*e
 return {p:e for p,e in z.items() if e}
@lru_cache(None)
def fac(n):
 z={};p=2
 while p*p<=n:
  while n%p==0:z[p]=z.get(p,0)+1;n//=p
  p+=1
 if n>1:z[n]=z.get(n,0)+1
 return z
@lru_cache(None)
def log(x):return add((1,fac(x.numerator)),(-1,fac(x.denominator)))
@lru_cache(None)
def prime_iv(p):return IV.lg(F(p))
def interval(v):
 z=(0,0)
 for p,c in v.items():z=IV.add(z,IV.mul(IV.exact(c),prime_iv(p)))
 return z
def sign(v):
 if not v:return 0
 lo,hi=interval(v)
 if lo>0:return 1
 if hi<0:return -1
 raise ArithmeticError('Uncertified sign; no automatic precision increase')
def ce(p,q):
 out={}
 for x,y in zip(p,q):
  if x:ck(y>0);out=add((1,out),(-x,log(y)))
 return out
def ent(p):return ce(p,p)
def kl(p,q):return add((1,ce(p,q)),(-1,ent(p)))
@lru_cache(None)
def coef(v):
 w=list(v);stride=1
 while stride<len(w):
  for base in range(0,len(w),stride*2):
   for j in range(base,base+stride):w[j],w[j+stride]=w[j]+w[j+stride],w[j]-w[j+stride]
  stride*=2
 return tuple(F(x,len(w)) for x in w)
def direct(v):return tuple(F(sum(x*((-1)**((i&t).bit_count()%2)) for i,x in enumerate(v)),len(v)) for t in range(len(v)))
@lru_cache(None)
def law(v):
 w=coef(v);p=tuple(x*x for x in w);ck(sum(p)==1);return p
def marginal(v,j):
 return tuple(v[(k&((1<<j)-1))|((k>>j)<<(j+1))]+v[(k&((1<<j)-1))|((k>>j)<<(j+1))|(1<<j)] for k in range(len(v)//2))
def restrict(v,j,t):return tuple(x for k,x in enumerate(v) if (k>>j)&1==t)
def mean(v):return F(sum(v),len(v))
def beta(b):return F(sum(x*x for x in b),len(b))
def tau(b,h):return beta(b)*(1-mean(h)**2)
def wrap(a,b,h,s):return tuple(x+s*y*z for z in h for x,y in zip(a,b))
def profile(n,k):
 if n==0:return ()
 w=list(range(1,n+1));w=w if k==0 else w[::-1]
 return tuple(F(x,sum(w)) for x in w)
def cal(q,z):
 if z==1:return (F(1),)+tuple(F(0) for _ in q[1:])
 ck(q[0]<1)
 return (z,)+tuple((1-z)*x/(1-q[0]) for x in q[1:])
def mix(q,z,eps,target):
 if z==1:return cal(q,z)
 ck(sum(target)==1 and len(target)==len(q)-1)
 return (z,)+tuple((1-eps)*x+eps*(1-z)*t for x,t in zip(q[1:],target))
def coherent(a,b,h,r,s):
 ac,bc=coef(a),coef(b);m=mean(h);ck(r[0]==m*m)
 out=tuple((ac[u]+s*m*bc[u])**2 if t==0 else bc[u]**2*r[t] for t in range(len(h)) for u in range(len(a)))
 ck(sum(out)==1);return out
def partition(p,n,kind):
 if kind=='seed':return p[:n]+(sum(p[n:]),)
 return p[:n]+tuple(sum(p[t*n+u] for t in range(1,len(p)//n)) for u in range(n))
def step(node,kind,j):
 global actions
 actions+=1
 a,b,h,r,s=node;v=wrap(a,b,h,s);p=law(v);q=coherent(a,b,h,r,s)
 i=j if kind=='controller' else len(a).bit_length()-1+j
 qb=marginal(q,i);pb=marginal(p,i);occ=add((1,kl(p,q)),(-1,kl(pb,qb)))
 ck(sign(occ)>=0);kids=[];cost=[];credits=[];pc=[]
 for bit in (0,1):
  if kind=='seed':aa,bb,hh,rr=a,b,restrict(h,j,bit),marginal(r,j)
  else:aa,bb,hh,rr=restrict(a,j,bit),restrict(b,j,bit),h,r
  vv=wrap(aa,bb,hh,s);ck(vv==restrict(v,i,bit));pp=law(vv);pc.append(pp)
  rr=cal(rr,mean(hh)**2);qq=coherent(aa,bb,hh,rr,s)
  credit=kl(partition(pp,len(aa),kind),partition(qb,len(aa),kind))
  ck(add((1,ce(pp,qb)),(-1,ce(pp,qq)))==credit);ck(sign(credit)>=0)
  kids.append((aa,bb,hh,rr,s));cost.append(ce(pp,qq));credits.append(credit)
 ck(all((x+y)/2==z for x,y,z in zip(pc[0],pc[1],pb)))
 ck(sum(F(p0)*((k>>i)&1) for k,p0 in enumerate(p))==F(sum(v[k]!=v[k^(1<<i)] for k in range(len(v))),len(v)))
 inc=add((1,ent(p)),(-1,ent(pb)),(F(1,2),cost[0]),(F(1,2),cost[1]),(-1,ce(p,q)))
 ck(inc==add((-1,occ),(-F(1,2),credits[0]),(-F(1,2),credits[1])));ck(sign(inc)<=0)
 childtau=sum(tau(k[1],k[2]) for k in kids)/2
 gap=tau(b,h)-childtau
 ck(gap>=0)
 ck(gap==(beta(b)*(mean(kids[0][2])-mean(kids[1][2]))**2/4 if kind=='seed' else 0))
 return inc,kids
def tag(a,b,h,r,k):
 ac,bc=coef(a),coef(b);v=wrap(a,b,h,1)+wrap(a,b,h,-1);p=law(v);i=len(v).bit_length()-2
 q=tuple(ac[u]**2*(t==0) for t in range(len(h)) for u in range(len(a)))+tuple(bc[u]**2*r[t] for t in range(len(h)) for u in range(len(a)))
 ck(sum(q)==1);kids=[];cost=[];pp=[]
 z=mean(h)**2;rr=cal(r,z);rr=mix(rr,z,F(1,8),profile(len(h)-1,1-k)) if z<1 else rr
 for s in (1,-1):
  qq=coherent(a,b,h,rr,s);pc=law(wrap(a,b,h,s));pp.append(pc);cost.append(ce(pc,qq));kids.append((a,b,h,rr,s))
 pb=marginal(p,i);js=add((1,ent(pb)),(-F(1,2),ent(pp[0])),(-F(1,2),ent(pp[1])))
 old=add((1,ent(p)),(-1,ent(pb)),(F(1,2),cost[0]),(F(1,2),cost[1]),(-1,ce(p,q)))
 if z<1:
  true=law(h)[1:];true=tuple(x/(1-z) for x in true)
  rt=tuple(x/(1-r[0]) for x in r[1:]);mt=tuple(x/(1-z) for x in rr[1:])
  excess=add((1,ce(true,mt)),(-1,ce(true,rt)))
  ck(sign(add((1,log(F(8,7))),(-1,excess)))>=0)
  pred=add((-1,js),(-beta(b),kl((z,1-z),(r[0],1-r[0]))),(tau(b,h),excess))
  ck(pred==old)
 if z==F(1,4) and r[0]==F(1,2) and beta(b)>0:ck(sign(add((-1,old),(-beta(b)/24,log(F(2)))))>0)
 return old,kids
def change(node,eps,k):
 global positive
 a,b,h,r,s=node;z=mean(h)**2
 if z==1:return {},node
 # Fixed nonempty point target, not a search over targets.
 target=tuple(F(i==k%(len(h)-1)) for i in range(len(h)-1))
 rr=mix(r,z,eps,target);p=law(wrap(a,b,h,s));q=coherent(a,b,h,r,s);qq=coherent(a,b,h,rr,s)
 inc=add((1,ce(p,qq)),(-1,ce(p,q)));bound=add((tau(b,h),log(1/(1-eps))),(-1,inc))
 ck(sign(bound)>=0);positive+=int(sign(inc)>0);ck(any(x!=y for x,y in zip(r,rr)) or len(h)==2)
 return inc,(a,b,h,rr,s)
def domain(pilot):
 states=[None,0,1] if pilot else [None,16,17,0,1]
 cases=0
 for n in range(2 if pilot else 3):
  for code in range(1<<(1<<n)):
   h=tuple(1-2*((code>>x)&1) for x in range(1<<n));ck(coef(h)==direct(h))
   for state in states:
    if state is None:a=ROW
    elif state in (16,17):a=restrict(ROW,0,state-16)
    else:a=(ROW[state],)
    b=tuple(1-x*x for x in a);ck(coef(a)==direct(a));ck(coef(b)==direct(b))
    for k in (0,1):
     if time.monotonic()>deadline:raise TimeoutError('frozen cap')
     r=(F(1,2),)+tuple(x/2 for x in profile(len(h)-1,k)) if len(h)>1 else (F(1),)
     old,kids=tag(a,b,h,r,k)
     for kid in kids:
      cases+=1
      for kind,N in [('seed',len(h)),('controller',len(a))]:
       for j in range(N.bit_length()-1):step(kid,kind,j)
 return cases
def fixture():
 a=ROW;b=tuple(1-x*x for x in a);h=tuple(-1 if x in (0,1,2,4) else 1 for x in range(16))
 ck(coef(h)==direct(h));r=(F(1,2),)+tuple(x/2 for x in profile(15,0));old,kids=tag(a,b,h,r,0)
 total=old;terminals=[];records=[]
 for signnode in kids:
  inc,children=step(signnode,'seed',0);total=add((1,total),(F(1,2),inc))
  ck(set(mean(k[2]) for k in children)=={F(1,4),F(3,4)})
  for child in children:
   inc,second=change(child,F(1,64),0);total=add((1,total),(F(1,4),inc));records.append({'round':2,'increment':inc,'reach':'1/4'})
   inc,grand=step(second,'seed',0);total=add((1,total),(F(1,4),inc))
   for grandchild in grand:
    inc,third=change(grandchild,F(1,64),1);total=add((1,total),(F(1,8),inc));records.append({'round':3,'increment':inc,'reach':'1/8'})
    aa,bb,hh,rr,s=third;pp=law(wrap(aa,bb,hh,s));qq=coherent(aa,bb,hh,rr,s)
    terminals.append({'seed':hh,'sign':s,'reference':qq,'spectrum':pp,'seed_reference':rr,'reach':'1/8'})
 ck(sign(add((-1,total),(-F(3,1024),log(F(2)))))>0)
 save('THREE_CHANGE_HISTORY.json',{'status':'PASS','seed':h,'source':r,'original_tag_increment':old,'total_added_increment':total,'total_interval':IV.serial(interval(total)),'changes':records,'complete_terminals':terminals,'old_source_renewed':False})
def scalar():
 ck(21**18>2**79);ck(64**32<2*63**32)
 ck(21**288*63**576>2**1251*64**576)
 ck(21**3*63**9<2**13*64**9)
 rho=add((F(9,32),log(F(21))),(-F(39,32),log(F(2))))
 delta=add((1,rho),(-F(9,16),log(F(64,63))))
 ck(sign(add((1,delta),(-F(3,1024),log(F(2)))))>0)
 # An adaptive uneven split of a total path budget, with distinct tau losses.
 for a in (F(0),F(1,4),F(1)):
  for b0,b1 in ((F(0),F(0)),(F(1,8),F(3,8)),(F(1),F(1))):
   if (b0+b1)/2>a:continue
   for l in (F(0),F(1,3),F(1)):
    used=a*l+(b0*(1-l)+b1*(1-l))/2;ck(used<=a)
 save('SCALAR.json',{'status':'PASS','tau0':'9/32','rho_interval':IV.serial(interval(rho)),'two_later_round_reserve':IV.serial(interval(delta)),'strict_reserve':'3/1024','three_later_round_sufficient_envelope':'NEGATIVE_NOT_A_COUNTEREXAMPLE'})
if __name__=='__main__':
 start=time.monotonic();deadline=start+55;pilot='--pilot' in sys.argv
 cases=domain(pilot);scalar()
 if not pilot:fixture()
 out={'status':'PASS','pilot':pilot,'signed_fixtures':cases,'physical_query_actions':actions,'assertions':checks,'positive_profile_changes':positive,'seconds':time.monotonic()-start,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'formal_verification':'NOT_CLAIMED'}
 save('PILOT.json' if pilot else 'VALIDATION.json',out);print(json.dumps(out))
