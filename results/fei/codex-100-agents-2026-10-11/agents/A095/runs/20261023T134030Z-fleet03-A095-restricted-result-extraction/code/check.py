from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util,json,hashlib,sys,time
R=Path(__file__).resolve().parents[1];AOWN=R.parents[1]
HP=AOWN/'runs/20261021T180853Z-fleet03-A095-restricted-result-extraction/code/check.py'
sp=importlib.util.spec_from_file_location('own_primitive',HP);T=importlib.util.module_from_spec(sp);sp.loader.exec_module(T)
START=time.perf_counter();N=0
def ck(x):
 global N
 assert x
 N+=1
 if time.perf_counter()-START>55:raise RuntimeError('frozen55s guard')
def plus(x,y):return x[0]+y[0],x[1]+y[1]
def minus(x,y):return x[0]-y[1],x[1]-y[0]
def scale(p,x):return p*x[0],p*x[1]
def rnd(x):
 d=2**80
 return F((x[0]*d).__floor__(),d),F((x[1]*d).__ceil__(),d)
def sm(xs):
 z=(F(0),F(0))
 for x in xs:z=rnd(plus(z,x))
 return z
def bounds(x):
 d=2**65
 return [str(F((x[0]*d).__floor__(),d)),str(F((x[1]*d).__ceil__(),d))]
@lru_cache(maxsize=512)
def law(v):return tuple(a*a for a in T.walsh(v))
@lru_cache(maxsize=1024)
def ce(P,Q):
 groups={}
 for p,q in zip(P,Q):
  if p:ck(q>0);groups[q]=groups.get(q,F(0))+p
 return sm(scale(p,T.log2(1/q)) for q,p in groups.items())
def normalize(v):return tuple(x*v[0] for x in v)
def tables(a):
 for f in range(1<<(1<<a)):yield tuple(1 if f>>x&1 else -1 for x in range(1<<a))
def compressed(g,m):
 a=len(g).bit_length()-1;g=normalize(g);amps=T.walsh(g);e=F(1,1<<(a+m));u=F(1,1<<m)
 nz=[x for x in amps if x];num=len(nz);off=(1<<(a+m))-num
 rows=[((z-e)**2+e*e,(z*z+3*e*e)/(1+3*e),1) for z in nz]
 rows.append((2*e*e,3*e*e/(1+3*e),off))
 ck(sum(q*c for q,r,c in rows)==1);ck(sum(r*c for q,r,c in rows)==1)
 chi=sum((F(c)*(q-r)**2/r for q,r,c in rows),F(0))
 D=sm(scale(c*q,T.log2(q/r)) for q,r,c in rows if c)
 coeff=(27*e+12*u*(1+3*e)**2+(1-6*e)**2)/(1+3*e)
 ck(chi<=e*coeff);ck(coeff<=4+21*e);ck(chi<=F(37,4)*e)
 ck(D[1]<F(111,8)*e)
 plain=[((z-2*e)**2,(z*z+4*e*e)/(1+4*e),1) for z in nz]+[(4*e*e,4*e*e/(1+4*e),off)]
 ck(sum(q*c for q,r,c in plain)==1);ck(sum(r*c for q,r,c in plain)==1)
 chip=sum((F(c)*(q-r)**2/r for q,r,c in plain),F(0))
 Dp=sm(scale(c*q,T.log2(q/r)) for q,r,c in plain if c and q)
 ck(chip<=12*e*(1+8*e));ck(Dp[1]<54*e)
 return {'a':a,'m':m,'D_interval':bounds(D),'chi2':str(chi),'plain_D_interval':bounds(Dp),'plain_chi2':str(chip),'epsilon':str(e)}
def pointed(g,m):
 a=len(g).bit_length()-1;v=[g[x&((1<<a)-1)] for x in range(1<<(a+m+1))]
 ck(v[0]==1);v[0]=-1
 return tuple(v)
def floor(g,m,sourceQ=None):
 v=pointed(g,m);Pg=law(g);P=law(v);M=len(v)//2;e=F(1,M)
 if sourceQ is None:sourceQ=Pg
 data=[((sourceQ[s] if s<len(sourceQ) else F(0))+3*e*e)/(1+3*e) for s in range(M)]
 marg=[P[s]+P[s+M] for s in range(M)]
 ck(min(marg)>0)
 Q=tuple(data[s%M]*P[s]/marg[s%M] for s in range(len(v)))
 ck(sum(Q)==(sum(sourceQ)+3*e)/(1+3*e))
 return v,Q
def direct(g,m,order,ref,depth):
 original=list(g);g=normalize(g);a=len(g).bit_length()-1;Pg=law(g);Ig=T.influence(g);ck(Ig>0)
 sourceQ=Pg if ref==0 else tuple((p+F(1,len(Pg)))/4 for p in Pg)
 c=ce(Pg,sourceQ);C0=F(a+2)/Ig;ck(c[1]<=C0*Ig)
 v,Q=floor(g,m,sourceQ);P=law(v);e=F(1,1<<(a+m));d=sum(g[1<<i]!=g[0] for i in range(a))
 E=e*d;G=e*(a+m+1-d);If=T.influence(v);K=4*C0+15;U=(C0+F(37,8))*Ig
 ck(If==Ig+G-E);ck(E<=Ig/8)
 root=ce(P,Q);ck(root[1]<=2*c[0]+15*(E+G))
 leaves=[(F(1),v,Q,tuple(range(a+m+1)))];rel=(F(0),F(0));sig=(F(0),F(0));pos=F(0)
 frontiers=0;events=[]
 def verify():
  nonlocal frontiers
  ck(sum(p for p,z,q,l in leaves)==1)
  terms=sm(scale(p,ce(law(z),q)) for p,z,q,l in leaves)
  B=plus(rel,terms);err=minus(B,plus(root,sig));ck(err[0]<=0<=err[1])
  ck(B[1]<=root[1]+pos+F(1,1<<55))
  target=(C0/2+F(35,128))*Ig+4*C0*G
  ck(K*If-U-B[1]>target)
  frontiers+=1
 def reset(k):
  nonlocal sig,pos
  p,z,old,ll=leaves[0]
  fixed=set(order[:k]);unfixed=[i for i in range(a) if i not in fixed]
  remg=tuple(g[sum(((x>>j)&1)<<i for j,i in enumerate(unfixed))] for x in range(1<<len(unfixed)))
  fv,new=floor(remg,m);ck(fv==z)
  fresh=ce(law(z),new);oldcost=ce(law(z),old);ee=scale(p,minus(fresh,oldcost))
  ck(ee[1]<F(111,8)*e)
  localD=minus(fresh,ce(law(z),law(z)));ck(localD[1]<F(111,8)*e*2**k)
  sig=plus(sig,ee);pos+=max(F(0),ee[1]);leaves[0]=(p,z,new,ll)
  events.append({'depth':k,'charge':bounds(ee),'reach':str(p),'positive_upper':str(max(F(0),ee[1]))})
  verify()
 verify();reset(0)
 for k,label in enumerate(order[:depth],1):
  p,z,old,ll=leaves[0];i=ll.index(label);vs,qs=T.transport(z,old,i);vs=[tuple(x) for x in vs];qs=[tuple(x) for x in qs]
  loss=minus(ce(law(z),old),scale(F(1,2),sm(ce(law(vs[b]),qs[b]) for b in (0,1))))
  ck(loss[1]>=0);rel=plus(rel,scale(p,loss));nl=ll[:i]+ll[i+1:]
  leaves[0:1]=[(p/2,vs[b],qs[b],nl) for b in (0,1)]
  verify();reset(k)
 ck(pos<F(111,8)*(depth+1)*e)
 ck(pos<e*(6*(depth+1)+F(63,2)*e*(2**(depth+1)-1)))
 ck(pos<F(381,128)*Ig)
 # Expose selector using the CURRENT floor; actual child0 has NO selector left.
 p,z,old,ll=leaves[0];i=ll.index(a+m);vs,qs=T.transport(z,old,i);vs=[tuple(x) for x in vs];qs=[tuple(x) for x in qs]
 loss=minus(ce(law(z),old),scale(F(1,2),sm(ce(law(vs[b]),qs[b]) for b in (0,1))))
 rel=plus(rel,scale(p,loss));nl=ll[:i]+ll[i+1:];leaves[0:1]=[(p/2,vs[b],qs[b],nl) for b in (0,1)];verify()
 fixed=set(order[:depth]);unfixed=[i for i in range(a) if i not in fixed]
 remg=tuple(g[sum(((x>>j)&1)<<i for j,i in enumerate(unfixed))] for x in range(1<<len(unfixed)))
 rp=law(remg);loc=e*2**depth;new=tuple(((rp[s] if s<len(rp) else F(0))+4*loc*loc)/(1+4*loc) for s in range(len(vs[0])))
 amps=T.walsh(vs[0]);ck(all(amp==(T.walsh(remg)[s] if s<len(remg) else F(0))-2*loc for s,amp in enumerate(amps)))
 ck(sum(new)==1);fresh=ce(law(vs[0]),new);oldcost=ce(law(vs[0]),qs[0])
 dd=minus(fresh,ce(law(vs[0]),law(vs[0])));ck(dd[1]<54*loc)
 ee=scale(p/2,minus(fresh,oldcost));ck(ee[1]<27*e)
 sig=plus(sig,ee);pos+=max(F(0),ee[1]);leaves[0]=(p/2,vs[0],new,nl)
 events.append({'depth':depth,'kind':'ACTUAL_POST_SELECTOR_DATA_ONLY','charge':bounds(ee),'reach':str(p/2),'positive_upper':str(max(F(0),ee[1]))});verify()
 ck(pos<F(813,128)*Ig)
 return {'a':a,'original_labelled_source':original,'source':list(g),'m':m,'order':list(order),'reference':ref,'source_depth':depth,'frontiers':frontiers,'resets':len(events),'sum_positive_upper':str(pos),'Ig':str(Ig),'C0':str(C0),'old_U':str(U),'reserve_lower':str((C0/2+F(35,128))*Ig+4*C0*G),'events':events}
def fixtures():
 out=[g for a in (1,2) for g in tables(a) if len(set(g))>1]
 out += [tuple(1 if x==0 else -1 for x in range(8)),tuple((-1)**x.bit_count() for x in range(8)),tuple(1 if x.bit_count()<2 else -1 for x in range(8)),(1,1,-1,1,-1,-1,1,-1)]
 return out
def main():
 mode=sys.argv[1];records=[]
 if mode=='pilot':
  for g in tables(1):compressed(g,2)
  records=[direct((1,-1),2,(0,),ref,d) for ref in (0,1) for d in (0,1)]
 elif mode=='compressed':
  records=[compressed(g,m) for a in range(4) for g in tables(a) for m in (2,3,7,8)]
 else:
  m=int(mode[0]);group=int(mode[1])
  for g in fixtures():
   a=len(g).bit_length()-1;orders=[tuple(range(a))] if a==1 else [tuple(range(a)),tuple(reversed(range(a)))]
   if (a==3)!=bool(group):continue
   for order in orders:
    for ref in (0,1):
     for d in range(a+1):records.append(direct(g,m,order,ref,d))
  ck(len(records)==(64 if group else 176))
 result={'status':'PASS','mode':mode,'cases':len(records),'assertions':N+T.NCHK,'frontiers':sum(x.get('frontiers',0) for x in records),'resets':sum(x.get('resets',0) for x in records),'seconds':time.perf_counter()-START,'helper_sha256':hashlib.sha256(HP.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'records':records}
 (R/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='records'}))
if __name__=='__main__':main()
