from arith import *
from pathlib import Path
from itertools import product
import json,time,sys
root=Path(__file__).resolve().parents[1];out=root/'out';t0=time.perf_counter();checks=0
pilot='--pilot' in sys.argv
def ck(x):
 global checks
 checks+=1;assert x,checks
 assert time.perf_counter()-t0<(55 if pilot else 60),'frozen runtime exceeded'
def save(name,x):(out/name).write_text(json.dumps(enc(x),indent=2)+'\n',encoding='utf-8')
tables=queries=zero=iso=endpoints=review_resets=0
for n in range(1,3 if pilot else 4):
 for h in product([-1,1],repeat=1<<n):
  tables+=1;ph=law(h);ch=coeff(h)
  for i in range(n):
   queries+=1;kids=[restrict(h,i,z) for z in [0,1]];pc=[law(v) for v in kids]
   c0=coeff(kids[0]);c1=coeff(kids[1]);ca=[(x+y)/2 for x,y in zip(c0,c1)];cb=[(x-y)/2 for x,y in zip(c0,c1)]
   disjoint=all(x*y==0 for x,y in zip(ca,cb));isospectral=pc[0]==pc[1]
   graph=all(not(x and y) for x,y in zip(restrict(ph,i,0),restrict(ph,i,1)))
   ck(disjoint==isospectral==graph);ck((erasure(ph,i)=={})==graph)
   if graph:iso+=1;ck(H(ph)==H(pc[0])==H(pc[1]))
   if ch[1<<i]!=0:continue
   zero+=1;m=ch[0];r=m*m;t=1-r
   ck(all(Q(sum(v),len(v))==m for v in kids))
   if not t:
    endpoints+=1
    for sig in [1,-1]:
     f=wrap(h,sig);pf=law(f);rr=[Q(1)]+[Q(0)]*(len(h)-1);qr=reference(h,rr,sig)
     ck(pf==qr);ck(erasure(pf,4+i)=={})
    continue
   for profile in [ [Q(1,len(h)-1)]*(len(h)-1),[Q(j,len(h)*(len(h)-1)//2) for j in range(1,len(h))] ]:
    R=[r]+[t*x for x in profile];ck(sum(R)==1);rho=R[1<<i];theta=rho/t
    Rbar=marginal(R,i);R0=[r]+[t*x/(t-rho) for x in Rbar[1:]];ck(sum(R0)==1)
    p0=restrict(ph,i,0);p1=restrict(ph,i,1);q0=restrict(R,i,0);q1=restrict(R,i,1)
    ds={}
    for v in range(1,len(p0)):
     w=p0[v]+p1[v];qq=q0[v]+q1[v]
     if w:ds=add((1,ds),(w,D([p0[v]/w,p1[v]/w],[q0[v]/qq,q1[v]/qq])))
    for sig in [1,-1]:
     f=wrap(h,sig);pf=law(f);Qold=reference(h,R,sig);bquery=erasure(pf,4+i)
     ck(bquery==add((beta,erasure(ph,i))))
     old=CE(pf,Qold)
     for lam in [Q(0),theta/2]:
      fresh=[];tails=[]
      target=[Q(0)]*(len(R0)-1);target[-1]=1
      L=[x/t for x in R0[1:]];N=[(1-lam)*x+lam*y for x,y in zip(L,target)]
      Rnew=[r]+[t*x for x in N];ck(sum(Rnew)==1);ck(all(v>=(1-lam)*u for u,v in zip(L,N)))
      for kid in kids:
       pk=law(kid);pkw=law(wrap(kid,sig));qnew=reference(kid,Rnew,sig)
       fresh.append(CE(pkw,qnew));tails.append(add((1,D([x/t for x in pk[1:]],N)),(-1,D([x/t for x in pk[1:]],L))))
      actual=add((1,bquery),(Q(1,2),fresh[0]),(Q(1,2),fresh[1]),(-1,old))
      expected=add((-beta,ds),(-beta*t,logq(t/(t-rho))),(beta*t/2,tails[0]),(beta*t/2,tails[1]))
      ck(actual==expected);review_resets+=1
      if lam==0:ck(actual==add((-beta,ds),(-beta*t,logq(1/(1-theta)))))
 save('CHECKPOINT.json',{'status':'RUNNING_NOT_CERTIFICATE','completed_dimension':n,'queries':queries,'checks':checks})
ck(tables==(20 if pilot else 276));ck(queries==(36 if pilot else 804));ck(zero==(14 if pilot else 224));ck(endpoints==(6 if pilot else 12))
# Nullspace embeddings for every small Boolean core, plus fixed tensor fixtures.
cores=[list(k) for n in range(3) for k in product([-1,1],repeat=1<<n)]
def tensor_defect(r):
 return [(-1)**sum(((x>>(3*j))&7)==0 for j in range(r)) for x in range(1<<(3*r))]
if not pilot:cores += [tensor_defect(1),tensor_defect(2)]
embeddings=0;fixtures=[];tau={2:Q(2),3:-Q(9,8)}
for core in cores:
 embeddings+=1;pg=law(core);q=product_marginals(pg);div=D(pg,q);nc=len(core)
 h=[(-1 if (x&7).bit_count()%2 else 1)*core[x>>3] for x in range(8*nc)]
 ph=law(h);ck(ph==[pg[t>>3] if (t&7)==7 else Q(0) for t in range(len(h))]);ck(ph[0]==0)
 ck(all(coeff(h)[1<<i]==0 for i in range(3)))
 childh=[restrict(h,0,z) for z in [0,1]]
 ck(law(childh[0])==law(childh[1]));ck(all(len(set(v))==2 for v in childh))
 Rtarget=[q[t>>2] if (t&3)==3 else Q(0) for t in range(4*nc)]
 branch=[]
 for sig in [1,-1]:
  f=wrap(h,sig);pf=law(f);qq=reference(h,ph,sig);ck(qq==pf);ck(erasure(pf,4)=={})
  ck(influence(pf,4)==beta);ck(D(pf,qq)=={})
  childp=[law(wrap(k,sig)) for k in childh];ck(childp[0]==childp[1]==marginal(pf,4))
  ck(D(pf,qq)==D(marginal(pf,4),marginal(qq,4)))
  terminal=[]
  for chh,pc in zip(childh,childp):
   qt=reference(chh,Rtarget,sig);ck(D(pc,qt)==add((beta,div)))
   terminal.append({'truth_table':wrap(chh,sig),'spectrum':pc,'reference':qt,'CE':CE(pc,qt)})
  actual=add((Q(1,2),terminal[0]['CE']),(Q(1,2),terminal[1]['CE']),(-1,CE(pf,qq)));ck(actual==add((beta,div)))
  # Actual singleton ghost injection, preserving original prepaid cost.
  for rho in [Q(0),Q(1,8),Q(1,2)]:
   ref=[(1-rho)*x for x in ph];ref[1]+=rho;ck(sum(ref)==1)
   injected=reference(h,ref,sig);cost=add((1,CE(pf,injected)),(-1,CE(pf,pf)));ck(cost==add((-beta,logq(1-rho))))
   inc=add((Q(1,2),terminal[0]['CE']),(Q(1,2),terminal[1]['CE']),(-1,CE(pf,injected)))
   ck(inc==add((beta,div),(beta,logq(1-rho))))
  if embeddings in [23,24]:branch.append({'sigma':sig,'parent_truth_table':f,'parent_spectrum':pf,'incoming_reference':qq,'parent_CE':CE(pf,qq),'query_erasure':{},'query_influence':beta,'terminals':terminal,'conversion_increment':actual})
 if embeddings in [23,24]:
  r=embeddings-22;ck(div==add((r,tau)));ck(sum(t.bit_count()*v for t,v in enumerate(pg))==Q(3*r,4))
  fixtures.append({'tensor_blocks':r,'core_truth_table':core,'core_spectrum':pg,'product_target':q,'core_conversion_KL':div,'branches':branch})
ck(embeddings==(22 if pilot else 24));ck(3**3<2**5);ck(3**9>2**14)
if fixtures:save('tensor_fixtures.json',fixtures)
result={'PASS':True,'pilot':pilot,'checks':checks,'seconds':time.perf_counter()-t0,'truth_tables':tables,'physical_queries':queries,'isospectral_queries':iso,'zero_singleton_queries':zero,'constant_endpoints':endpoints,'A079_full_reference_resets':review_resets,'core_embeddings':embeddings,'formal_status':'NOT_CLAIMED'}
save('pilot.json' if pilot else 'validation.json',result);save('CHECKPOINT.json',{'status':'COMPLETE_PILOT' if pilot else 'COMPLETE','result':result});print(json.dumps(result))
