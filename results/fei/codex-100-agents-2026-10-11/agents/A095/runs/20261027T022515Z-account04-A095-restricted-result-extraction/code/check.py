from pathlib import Path
from fractions import Fraction as F
import importlib.util, sys, json, time, hashlib
R=Path(__file__).resolve().parents[1]
P=R.parents[1]/'runs/20261023T134030Z-account03-A095-restricted-result-extraction/code/check.py'
sp=importlib.util.spec_from_file_location('prior',P); B=importlib.util.module_from_spec(sp);sp.loader.exec_module(B)
T=B.T; start=time.perf_counter(); checks=0
def ck(v):
 global checks
 assert v
 checks+=1
 if time.perf_counter()-start>55: raise RuntimeError('frozen 55 second guard')
def exact(g,m):
 g=B.normalize(g); amps=T.walsh(g);a=len(g).bit_length()-1;e=F(1,2**(a+m));u=F(1,2**m)
 nz=[x for x in amps if x];M=1/e;N=len(nz);zero=int(M)-N
 rows=[(x,1) for x in nz]+[(F(0),zero)]
 q=lambda x:(x-2*e)**2
 r=lambda x:(x*x+4*e*e)/(1+4*e)
 ck(sum(c*q(x) for x,c in rows)==1);ck(sum(c*r(x) for x,c in rows)==1)
 chi=sum(c*(q(x)-r(x))**2/r(x) for x,c in rows)
 J=sum(F(c)/(x*x+4*e*e) for x,c in rows)
 ck(chi==16*e+48*e*e-64*e**4*(1+4*e)*J)
 ck(chi<=16*u*e+(-16+64*u)*e*e)
 if m>=2: ck(chi<=16*u*e)
 D=B.sm(B.scale(c*q(x),T.log2(q(x)/r(x))) for x,c in rows if c and q(x))
 if m>=2:ck(D[1]<24*u*e)
 if a==0:
  ck(chi==64*e**3*(1-e)/(1+4*e*e))
  if m==0:ck(chi==0);ck(D[0]<=0<=D[1])
  if m==1:ck(D[1]<2);ck(q(F(1))==0)
 return {'a':a,'m':m,'chi2':str(chi),'D':B.bounds(D)}
def history(g,m,order,ref,depth):
 g=B.normalize(g);a=len(g).bit_length()-1;Ig=T.influence(g);ck(Ig>0)
 Pg=B.law(g);sourceQ=Pg if ref==0 else tuple((p+F(1,len(Pg)))/4 for p in Pg)
 c=B.ce(Pg,sourceQ);C0=F(a+2)/Ig;ck(c[1]<=C0*Ig)
 v,Q=B.floor(g,m,sourceQ);root=B.ce(B.law(v),Q);e0=F(1,2**(a+m))
 d0=sum(g[1<<i]!=g[0] for i in range(a));G=e0*(a+m+1-d0)
 K=4*C0+15;U=(C0+F(37,8))*Ig;If=T.influence(v)
 ck(If==Ig+G-e0*d0)
 leaves=[(F(1),v,Q,tuple(range(a+m+1)))];releases=(F(0),F(0));signed=(F(0),F(0));pos=[F(0)]*3
 frontiers=0;events=[]
 def verify():
  nonlocal frontiers
  ck(sum(p for p,z,q,ll in leaves)==1)
  full=B.plus(releases,B.sm(B.scale(p,B.ce(B.law(z),q)) for p,z,q,ll in leaves))
  err=B.minus(full,B.plus(root,signed));ck(err[0]<=0<=err[1])
  ck(full[1]<=root[1]+sum(pos)+F(1,2**50))
  ck(K*If-U-full[1]>(C0/2+F(275,128))*Ig+4*C0*G)
  frontiers+=1
 def query(label):
  nonlocal releases
  p,z,q,ll=leaves[0];i=ll.index(label);vs,qs=T.transport(z,q,i)
  vs=list(map(tuple,vs));qs=list(map(tuple,qs));nl=ll[:i]+ll[i+1:]
  loss=B.minus(B.ce(B.law(z),q),B.scale(F(1,2),B.sm(B.ce(B.law(vs[b]),qs[b]) for b in (0,1))))
  ck(loss[1]>=0);releases=B.plus(releases,B.scale(p,loss))
  leaves[0:1]=[(p/2,vs[b],qs[b],nl) for b in (0,1)];verify()
 def reset(source_selector,category):
  nonlocal signed
  p,z,old,ll=leaves[0];remaining=[i for i in ll if i<a]
  h=tuple(g[sum(((x>>j)&1)<<i for j,i in enumerate(remaining))] for x in range(2**len(remaining)))
  padding=sum(a<=i<a+m for i in ll);e=F(1,2**(len(remaining)+padding))
  if source_selector:
   vv,new=B.floor(h,padding);ck(vv==z)
  else:
   hp=B.law(h);new=tuple(((hp[s] if s<len(hp) else F(0))+4*e*e)/(1+4*e) for s in range(len(z)))
   ha=T.walsh(h);ck(all(x==(ha[s] if s<len(ha) else F(0))-2*e for s,x in enumerate(T.walsh(z))))
  ck(sum(new)==1)
  fresh=B.ce(B.law(z),new);oldce=B.ce(B.law(z),old);ee=B.scale(p,B.minus(fresh,oldce))
  signed=B.plus(signed,ee);pos[category]+=max(F(0),ee[1]);leaves[0]=(p,z,new,ll)
  events.append({'kind':category,'remaining_source':len(remaining),'padding':padding,'charge':B.bounds(ee)})
  verify()
 verify();reset(True,0)
 for label in order[:depth]:query(label);reset(True,0)
 ck(pos[0]<F(381,128)*Ig)
 query(a+m);reset(False,1)
 for label in order[depth:]:query(label);reset(False,1)
 ck(pos[1]<F(3,4)*Ig)
 for label in range(a,a+m):query(label);reset(False,2)
 ck(pos[2]<F(3,4)*Ig);ck(len(leaves[0][1])==1)
 ck(sum(pos)<F(573,128)*Ig)
 return {'a':a,'m':m,'source':list(g),'order':list(order),'ref':ref,'selector_depth':depth,'frontiers':frontiers,'positive_totals':list(map(str,pos)),'events':events}
mode=sys.argv[1]; records=[]
if mode=='compressed':
 records=[exact(g,m) for a in range(4) for g in B.tables(a) for m in (0,1,2,3,7,8)]
 ck(len(records)==1668)
elif mode=='pilot':
 records=[exact((1,),m) for m in range(4)]+[history((1,-1),2,(0,),ref,d) for ref in (0,1) for d in (0,1)]
else:
 m=int(mode[0]);group=int(mode[1])
 for g in B.fixtures():
  a=len(g).bit_length()-1
  if (a==3)!=bool(group):continue
  orders=[tuple(range(a))] if a==1 else [tuple(range(a)),tuple(reversed(range(a)))]
  for order in orders:
   for ref in (0,1):
    for d in range(a+1):records.append(history(g,m,order,ref,d))
 ck(len(records)==(64 if group else 176))
result={'status':'PASS','mode':mode,'cases':len(records),'assertions':checks+B.N+T.NCHK,'frontiers':sum(x.get('frontiers',0) for x in records),'seconds':time.perf_counter()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'prior_checker_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'primitive_sha256':hashlib.sha256(B.HP.read_bytes()).hexdigest(),'records':records}
(R/'out').mkdir(exist_ok=True)
(R/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'}))
