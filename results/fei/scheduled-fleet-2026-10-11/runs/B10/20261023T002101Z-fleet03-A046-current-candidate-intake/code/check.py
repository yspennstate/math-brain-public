"""Post-controller correlated resets; independently written finite certificate."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import time,json,sys
R=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0;NODES=0;GHOSTS=0
GRID=1<<110;Z=(F(0),F(0))
def ck(p):
 global COUNT
 assert p
 COUNT+=1
 assert time.perf_counter()-START<55
def roundout(a):return F(a[0].numerator*GRID//a[0].denominator,GRID),F(-((-a[1].numerator*GRID)//a[1].denominator),GRID)
def add(a,b):return roundout((a[0]+b[0],a[1]+b[1]))
def mul(a,c):return roundout((a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c))
def sub(a,b):return add(a,mul(b,-1))
def point(x):return (x,x)
def lnunit(x):
 z=(x-1)/(x+1);v=z;s=F(0)
 for k in range(32):s+=v/(2*k+1);v*=z*z
 return 2*s,2*s+2*v/(65*(1-z*z))
L2=lnunit(F(2))
@lru_cache(None)
def log(x):
 assert x>0
 k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
 if y<1:y*=2;k-=1
 a,b=lnunit(y);return roundout((a/L2[1]+k,b/L2[0]+k))
def entropy(p):
 a=Z
 for x in p.values():
  if x:a=add(a,mul(log(x),-x))
 return a
def kl(p,q):
 a=Z
 for s,x in p.items():
  if x:
   ck(q.get(s,0)>0);a=add(a,mul(sub(log(x),log(q[s])),x))
 return a
def overlap(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))
@lru_cache(None)
def spec(t,co):
 v=list(t);N=len(v);step=1
 while step<N:
  for start in range(0,N,2*step):
   for k in range(start,start+step):a,b=v[k],v[k+step];v[k],v[k+step]=a+b,a-b
  step*=2
 p={};infl={i:F(0) for i in co}
 for u,a in enumerate(v):
  if not a:continue
  mask=sum(1<<co[j] for j in range(len(co)) if (u>>j)&1);p[mask]=F(a*a,N*N)
  for i in co:
   if mask>>i&1:infl[i]+=p[mask]
 ck(sum(p.values())==1)
 return p,infl
def direct(t,co,p):
 N=len(t)
 for u in range(N):
  a=sum(x*(-1 if (k&u).bit_count()%2 else 1) for k,x in enumerate(t))
  mask=sum(1<<co[j] for j in range(len(co)) if u>>j&1)
  ck(p.get(mask,0)==F(a*a,N*N))
def restrict(t,co,i,b):
 j=co.index(i);return tuple(x for k,x in enumerate(t) if (k>>j)&1==b),tuple(k for k in co if k!=i)
def erase(p,i):
 out={}
 for mask,w in p.items():out[mask&~(1<<i)]=out.get(mask&~(1<<i),F(0))+w
 return out
def freshcore(m,r,assignment,tilt=F(1,8)):
 q={0:F(1)};variance=F(0)
 for block in range(m):
  bits=list(range(3+block*r,3+(block+1)*r))
  active=[i for i in bits if i not in assignment]
  if any(assignment.get(i)==0 for i in bits) or not active:factor={0:F(1)}
  elif len(active)==1:factor={1<<active[0]:F(1)}
  else:
   k=len(active);d=F(1,1<<k);v=4*d*(1-d);variance+=v
   factor={0:(1-2*d)**2};full=sum(1<<i for i in active)
   for u in range(1,1<<k):
    mask=sum(1<<active[j] for j in range(k) if u>>j&1)
    factor[mask]=(1-tilt)*4*d*d+(v*tilt if mask==full else 0)
  # A width-one surviving point is a character of variance one.
  if not any(assignment.get(i)==0 for i in bits) and len(active)==1:variance+=1
  q={s|t:w*z for s,w in q.items() for t,z in factor.items()}
 ck(sum(q.values())==1)
 return {s:v for s,v in q.items() if v},variance
def core(m,r):
 return tuple((-1)**sum(all(z>>(j*r+k)&1 for k in range(r)) for j in range(m)) for z in range(1<<(m*r)))
def family(h):return tuple(1-2*(u>>1&1) if not(u&1) else h[u>>3] if u&4 else 1 for u in range(8*len(h)))
def liftroot(t,q,co):
 p,_=spec(t,co);out={s:w for s,w in p.items() if s<8}
 for s,w in q.items():
  if s:
   for c in (0,1,4,5):out[s|c]=w/16
 ck(sum(out.values())==1);return out
def freshmux(p,q):
 out={s:w for s,w in p.items() if s<8}
 for s,w in q.items():
  if s:out[s]=w/4;out[s|1]=w/4
 ck(sum(out.values())==1);return out
def node(t,co,q,i):
 global NODES,GHOSTS
 NODES+=1;p,ii=spec(t,co);pe=erase(p,i);qe=erase(q,i)
 kids=[restrict(t,co,i,b)[0] for b in (0,1)];cn=tuple(j for j in co if j!=i)
 P=[spec(k,cn)[0] for k in kids];refs=[];zs=[]
 for s,w in qe.items():
  ck(pe.get(s,0)==(P[0].get(s,0)+P[1].get(s,0))/2)
  if w and not pe.get(s,0):GHOSTS+=1
 for b in (0,1):
  un={s:w*(P[b].get(s,0)/(2*pe[s]) if pe.get(s,0) else F(1,2)) for s,w in qe.items()}
  z=sum(un.values());ck(z>0);zs.append(z);refs.append({s:w/z for s,w in un.items() if w})
 ck(sum(zs)==1)
 for s,w in p.items():
  u=s&~(1<<i);er=(w/pe[u])/(q[s]/qe[u])
  for b in (0,1):
   if P[b].get(u,0):ck(w/q[s]==er*(F(1,2)/zs[b])*(P[b][u]/refs[b][u]))
 childi=sum(sum(spec(k,cn)[1].values()) for k in kids)/2
 ck(sum(ii.values())==ii[i]+childi)
 release=sub(kl(p,q),mul(add(kl(P[0],refs[0]),kl(P[1],refs[1])),F(1,2)))
 return kids,cn,refs,release,zs
def record(t,co,q,w,kind):
 p,ii=spec(t,co);return {'w':w,'P':p,'Q':q,'H':entropy(p),'I':sum(ii.values()),'K':kl(p,q),'kind':kind,'co':co}
def datafront(t,co,q,w,path,mode,depth=0):
 if mode=='none':return [(t,co,q,w,path)],Z
 if depth==1 and (mode=='first' or path.get(3)==1):return [(t,co,q,w,path)],Z
 if depth==2:return [(t,co,q,w,path)],Z
 i=3+depth
 if i not in co:return [(t,co,q,w,path)],Z
 kids,cn,refs,rel,_=node(t,co,q,i);rows=[];total=mul(rel,w)
 for b in (0,1):
  out,rr=datafront(kids[b],cn,refs[b],w/2,{**path,i:b},mode,depth+1)
  rows+=out;total=add(total,rr)
 return rows,total
def run(m,r,prefix,controller):
 h=core(m,r);t=family(h);co=tuple(range(3+m*r));p,ii=spec(t,co)
 qc,vroot=freshcore(m,r,{});q=liftroot(t,qc,co)
 if m==1 and r==2:direct(t,co,p)
 H=entropy(p);A=kl(p,q);I=sum(ii.values());margin=sub(point(4*I),add(H,A))
 delta=F(1,1<<r);tminus=F(sum(x<0 for x in h),len(h))
 ck(margin[0]>1+2*tminus+F(m,4)*delta)
 bs,bco,B,brel,_=node(t,co,q,2)
 rows=[record(bs[0],bco,B[0],F(1,2),'retained_b0')]
 frontier,drel=datafront(bs[1],bco,B[1],F(1,2),{},prefix)
 releases=add(brel,drel);V=F(0);sigma=Z;freshcost=Z;resetrows=[];positive=0
 for index,(leaf,lco,lq,w,path) in enumerate(frontier):
  fq,v=freshcore(m,r,path,F(1,7));V+=2*w*v
  which=controller if controller!='mixed' else ('x' if index%2==0 else 'a')
  i=0 if which=='x' else 1
  kids,cn,C,rel,zs=node(leaf,lco,lq,i);releases=add(releases,mul(rel,w))
  for b in (0,1):
   old=record(kids[b],cn,C[b],w/2,'inherited_complement')
   if which=='x' and b==0:rows.append(old);continue
   P=old['P'];newq=fq if which=='x' else freshmux(P,fq)
   new=record(kids[b],cn,newq,w/2,'exercised_reset_'+which+str(b))
   inc=sub(new['K'],old['K']);sigma=add(sigma,mul(inc,w/2));freshcost=add(freshcost,mul(new['K'],w/2))
   if inc[0]>0:positive+=1
   rows.append(new);resetrows.append({'w':w/2,'controller':which,'outcome':b,'data_path':path,'old_Q':C[b],'new_Q':newq,'P':P,'old_K':old['K'],'new_K':new['K'],'sigma':inc,'normalizers_before_reset':zs})
 ck(V<=vroot);ck(vroot==4*m*delta*(1-delta))
 cap=mul(log(F(7,6)),vroot/4)
 ck(freshcost[1]<cap[0]);ck(cap[1]<F(m,4)*delta)
 ck(sigma[1]<=freshcost[1])
 Hf=Z;If=F(0);Kf=Z
 for row in rows:Hf=add(Hf,mul(row['H'],row['w']));If+=row['w']*row['I'];Kf=add(Kf,mul(row['K'],row['w']))
 overlap(add(A,sigma),add(releases,Kf))
 S=sub(point(4*If),Hf);edge=sub(sub(H,Hf),point(4*(I-If)));net=add(add(A,edge),sigma)
 paid=sub(sub(S,(max(F(0),net[0]),max(F(0),net[1]))),point(F(1,4)))
 ck(paid[0]>F(7,10))
 overlap(sub(S,net),sub(margin,sigma))
 out={'m':m,'r':r,'prefix':prefix,'controller':controller,'root_P':p,'root_Q':q,'root_I':I,'root_H':H,'root_KL':A,'root_inclusive_margin':margin,'original_variance_sum':vroot,'conditional_variance_expectation':V,'fresh_KL_cap':cap,'actual_fresh_KL':freshcost,'signed_reset_total':sigma,'positive_reset_nodes':positive,'old_booking':F(1,4),'final_S':S,'full_signed_transaction':net,'after_old_booking':paid,'old_source_releases':releases,'complete_new_terminal_KL':Kf,'final_rows':rows,'exercised_resets':resetrows}
 return out
def serial(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(v) for v in x]
 return x
pilot='--pilot' in sys.argv
cases=[(1,2,'none','x')] if pilot else [(m,r,p,c) for m,r in [(1,2),(2,2),(2,3)] for p in ['none','first','adaptive'] for c in ['x','a','mixed']]
positives=0
for m,r,p,c in cases:
 out=run(m,r,p,c);positives+=out['positive_reset_nodes']
 (R/'out'/f'{"PILOT_" if pilot else ""}m{m}r{r}_{p}_{c}.json').write_text(json.dumps(serial(out),indent=2)+'\n',encoding='utf-8')
ck(8**4<2*7**4);ck(7**4<2*6**4);ck(positives>0)
summary={'status':'PASS','cases':len(cases),'checks':COUNT,'nodes':NODES,'reference_only_rows_retained':GHOSTS,'positive_reset_nodes':positives,'runtime_seconds':time.perf_counter()-START,'domain':'amended-frozen27' if not pilot else 'one-amended-frozen-pilot','arithmetic':'Integer Walsh/direct character/Fraction/rational32-term logs'}
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8');print(json.dumps(summary))
