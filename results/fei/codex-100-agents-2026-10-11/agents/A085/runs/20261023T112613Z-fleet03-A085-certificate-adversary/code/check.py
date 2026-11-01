from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
import json,time,sys,hashlib
import algebra as C
R=Path(__file__).resolve().parents[1]
def save(n,x):C.save(n,x)
def timeout():
 if time.monotonic()>deadline:raise TimeoutError('frozen55s cap')
def actual(a,b,h,s):return C.law(C.wrap(a,b,h,s))
def ghost(h,j,theta,a,b,s):
 p=C.law(h);z=p[0];t=1-z;N=len(h);single=1<<j;C.ck(p[single]==0)
 if not t:r=(F(1),)+tuple(F(0) for _ in range(N-1));theta=F(0)
 else:r=tuple(z if k==0 else theta*t if k==single else (1-theta)*t/(N-2) for k in range(N))
 C.ck(sum(r)==1)
 ds={}
 for k in range(1,N//2):
  lo=(k&((1<<j)-1))|((k>>j)<<(j+1));hi=lo|single;w=p[lo]+p[hi];q=r[lo]+r[hi]
  if w:ds=C.add((1,ds),(w,C.kl((p[lo]/w,p[hi]/w),(r[lo]/q,r[hi]/q))))
 v=C.wrap(a,b,h,s);P=C.law(v);Q=C.coherent(a,b,h,r,s);i=len(a).bit_length()-1+j
 Pbar=C.marginal(P,i);Qbar=C.marginal(Q,i);B=C.add((1,C.ent(P)),(-1,C.ent(Pbar)))
 rr=C.cal(C.marginal(r,j),z);pcs=[];qcs=[];hs=[]
 for bit in (0,1):
  hh=C.restrict(h,j,bit);C.ck(C.mean(hh)==C.mean(h));hs.append(hh)
  pp=actual(a,b,hh,s);qq=C.coherent(a,b,hh,rr,s);pcs.append(pp);qcs.append(qq)
  C.ck(C.wrap(a,b,hh,s)==C.restrict(v,i,bit))
 inc=C.add((1,B),(F(1,2),C.ce(pcs[0],qcs[0])),(F(1,2),C.ce(pcs[1],qcs[1])),(-1,C.ce(P,Q)))
 predicted=C.add((-C.beta(b),ds),(-C.beta(b)*t,C.log(1/(1-theta))))
 C.ck(inc==predicted);C.ck(C.sign(ds)>=0)
 for lam in (F(0),theta/2,theta):
  costs=[]
  for hh,pp in zip(hs,pcs):
   if t:
    target=tuple(F(k==len(hh)-2) for k in range(len(hh)-1));new=C.mix(rr,z,lam,target)
   else:new=rr
   qq=C.coherent(a,b,hh,new,s);costs.append(C.ce(pp,qq))
  changed=C.add((1,B),(F(1,2),costs[0]),(F(1,2),costs[1]),(-1,C.ce(P,Q)))
  C.ck(C.sign(C.add((1,changed),(C.beta(b),ds)))<=0)
 return 1
def ghost_domain(pilot):
 count=0;eligible=0
 seeds=[]
 for n in range(2 if pilot else 3):
  seeds.extend(tuple(1-2*((code>>k)&1) for k in range(1<<n)) for code in range(1<<(1<<n)))
 seeds.append(tuple((-1)**k.bit_count() for k in range(8)))
 if not pilot:seeds.append(tuple(((-1)**((k>>2)&1))*(-1 if k%4==0 else 1) for k in range(8)))
 for h in seeds:
  ph=C.law(h)
  for j in range(len(h).bit_length()-1):
   if ph[1<<j]:continue
   eligible+=1
   for theta in (F(0),F(1,8),F(1,2)):
    for a in (C.ROW,(1,),(0,)):
     b=tuple(1-v*v for v in a)
     for s in (1,-1):count+=ghost(h,j,theta,a,b,s)
   timeout()
 return {'eligible_seed_queries':eligible,'incoming_instances':count,'mixture_transactions':3*count}
def source(g,model):
 p=C.law(g);z=p[0]
 if not model or z==1:return p
 return (z,)+tuple((1-z)*x for x in C.profile(len(g)-1,0))
def build(g,L,fixed):
 m=len(g).bit_length()-1;N=m*L;remain=[j for j in range(N) if j not in fixed];pos={j:k for k,j in enumerate(remain)}
 masks=[];signs=[]
 for j in range(m):
  masks.append(sum(1<<pos[i] for i in range(j*L,(j+1)*L) if i in pos))
  signs.append(sum(fixed.get(i,0) for i in range(j*L,(j+1)*L))%2)
 h=[]
 for x in range(1<<len(remain)):
  core=sum((((x&mask).bit_count()+sgn)%2)<<j for j,(mask,sgn) in enumerate(zip(masks,signs)))
  h.append(g[core])
 return tuple(h),masks,signs,remain
def push(v,masks):
 N=1<<sum(x.bit_count() for x in masks);out=[F(0)]*N
 for k,x in enumerate(v):out[sum(mask for j,mask in enumerate(masks) if (k>>j)&1)]=x
 return tuple(out)
def embedding_domain(pilot):
 states=queries=0;nonflat=None
 cores=[]
 for m in range(2 if pilot else 3):
  cores.extend((tuple(1-2*((code>>k)&1) for k in range(1<<m)),L) for code in range(1<<(1<<m)) for L in ((2,) if pilot else (2,3)))
 if not pilot:cores.append((tuple(-1 if k==0 else 1 for k in range(8)),2))
 for g,L in cores:
  m=len(g).bit_length()-1;N=m*L;gp=C.law(g);gc=C.coef(g);C.ck(gc==C.direct(g))
  for model in (0,1):
   S=source(g,model);rootCE=C.ce(gp,S)
   for k in range(min(L-1,N)+1):
    for chosen in combinations(range(N),k):
     for bits in product((0,1),repeat=k):
      fixed=dict(zip(chosen,bits));h,masks,signs,remain=build(g,L,fixed);states+=1
      ph=C.law(h);rr=push(S,masks);C.ck(ph==push(gp,masks));C.ck(C.ce(ph,rr)==rootCE)
      expected=[F(0)]*len(h)
      for J,c in enumerate(gc):expected[sum(mask for j,mask in enumerate(masks) if (J>>j)&1)]=c*((-1)**sum(signs[j] for j in range(m) if (J>>j)&1))
      C.ck(tuple(expected)==C.coef(h))
      if k==0:
       Ih=sum(F(sum(g[x]!=g[x^(1<<j)] for x in range(len(g))),len(g)) for j in range(m))
       C.ck(sum(F(sum(h[x]!=h[x^(1<<j)] for x in range(len(h))),len(h)) for j in range(N))==L*Ih)
      if k>=L-1:continue
      for j,physical in enumerate(remain):
       queries+=1;C.ck(C.coef(h)[1<<j]==0);C.ck(rr[1<<j]==0)
       pb=C.marginal(ph,j);qb=C.marginal(rr,j)
       for pair in range(len(h)//2):
        lo=(pair&((1<<j)-1))|((pair>>j)<<(j+1));hi=lo|(1<<j)
        C.ck(not(C.coef(h)[lo]*C.coef(h)[hi]));C.ck(not(rr[lo] and rr[hi]))
       for bit in (0,1):
        hh=C.restrict(h,j,bit);C.ck(C.law(hh)==pb);C.ck(C.mean(hh)==C.mean(h));C.ck(C.ce(pb,qb)==rootCE)
      timeout()
 return {'source_prefix_states':states,'zero_credit_source_queries':queries}
def wrapper_fixture(pilot):
 g=tuple(-1 if x==0 else 1 for x in range(8));h,masks,_,_=build(g,2,{})
 a=C.ROW;b=tuple(1-x*x for x in a);records=[]
 for model in (0,1):
  if pilot and model:continue
  rr=push(source(g,model),masks)
  for s in ((1,) if pilot else (1,-1)):
   v=C.wrap(a,b,h,s);P=C.law(v);Q=C.coherent(a,b,h,rr,s)
   for j in ((0,5) if pilot else range(6)):
    i=4+j;pb=C.marginal(P,i);qb=C.marginal(Q,i)
    # Check occupied fiber equality atomwise; this certifies ZERO KL without interval overlap.
    for k in range(len(v)//2):
     lo=(k&((1<<i)-1))|((k>>i)<<(i+1));hi=lo|(1<<i)
     C.ck(not(P[lo] and P[hi]));C.ck(not(Q[lo] and Q[hi]))
    C.ck(C.ent(P)==C.ent(pb));C.ck(C.ce(P,Q)==C.ce(pb,qb))
    terms=[]
    for bit in (0,1):
     hh=C.restrict(h,j,bit);pp=actual(a,b,hh,s);qq=C.coherent(a,b,hh,C.marginal(rr,j),s)
     C.ck(pp==pb);C.ck(qq==qb);C.ck(C.wrap(a,b,hh,s)==C.restrict(v,i,bit))
     terms.append({'outcome':bit,'truth':C.wrap(a,b,hh,s),'spectrum':pp,'reference':qq})
    if model==0 and s==1 and j==0:records=terms
 save('NONFLAT_ZERO_CREDIT.json',{'status':'PASS','core_truth':g,'seed_truth':h,'core_spectrum':C.law(g),'seed_spectrum':C.law(h),'seed_influence':'3/2','seed_entropy_exact':'4-(9/16)log2(9)','complete_wrapper_children':records,'all_six_relevant_seed_queries_zero_phase':True,'no_conversion_necessary_for_inherited_continuation':True})
 return 2 if pilot else 24
def sharp():
 h=tuple((-1)**k.bit_count() for k in range(8));a=C.ROW;b=tuple(1-x*x for x in a);rows=[]
 for rho in (F(0),F(1,128),F(1,32)):
  rr=tuple(rho if k==1 else 1-rho if k==7 else F(0) for k in range(8));Q=C.coherent(a,b,h,rr,1);P=actual(a,b,h,1)
  for lam in (F(0),F(1,64),F(1,32),F(1,16)):
   costs=[]
   for bit in (0,1):
    hh=C.restrict(h,0,bit);new=(F(0),lam,F(0),1-lam);qq=C.coherent(a,b,hh,new,1);pp=actual(a,b,hh,1);costs.append(C.ce(pp,qq))
   inc=C.add((F(1,2),costs[0]),(F(1,2),costs[1]),(-1,C.ce(P,Q)))
   expected=C.add((F(3,8),C.log((1-rho)/(1-lam))))
   C.ck(inc==expected);C.ck(C.sign(inc)==((lam>rho)-(lam<rho)))
   rows.append({'rho':rho,'lambda':lam,'increment_prime_log':inc,'sign':C.sign(inc)})
 save('SHARP_GHOST.json',{'status':'PASS','cases':rows,'creation_credit_is_exact_prepaid_cost':True})
 return len(rows)
if __name__=='__main__':
 start=time.monotonic();deadline=start+55;pilot='--pilot' in sys.argv
 ghost_counts=ghost_domain(pilot);embedded=embedding_domain(pilot);wrappers=wrapper_fixture(pilot);sh=sharp();timeout()
 out={'status':'PASS','pilot':pilot,'assertions':C.checks,'ghost':ghost_counts,'embedding':embedded,'full_wrapper_query_transactions':wrappers,'sharp_cases':sh,'seconds':time.monotonic()-start,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'formal_verification':'NOT_CLAIMED'}
 save('PILOT.json' if pilot else 'VALIDATION.json',out);print(json.dumps(out))
