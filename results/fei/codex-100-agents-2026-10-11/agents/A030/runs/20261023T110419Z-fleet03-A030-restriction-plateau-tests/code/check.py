from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import hashlib,json,time,sys,itertools
RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1]
OLD=OWN/'runs/20261023T041014Z-fleet03-A030-restriction-plateau-tests/code/check.py'
h={'__file__':str(OLD)}
exec(OLD.read_text(encoding='utf-8').split('rows=[]')[0],h)
add,const,phi,positive,ZERO,enc,coeff,kl,ent,transport=[h[k] for k in ['add','const','phi','positive','ZERO','enc','coeff','kl','ent','transport']]
pilot='--pilot' in sys.argv;start=time.perf_counter();limit=55 if pilot else 180
checks=nodes=0
def ck(x):
 global checks
 checks+=1;assert x,checks;assert time.perf_counter()-start<limit,'frozen runtime'
def nonneg(e):ck(positive(add((-1,e)))==ZERO)
LOG3=h['logf'](F(3));LOG2=const(1)
@lru_cache(None)
def stat(labels,cores):
 nc=len(labels).bit_length()-1;amp={};q={}
 for j,core in enumerate(cores):
  for u,c in coeff(tuple(int(x==j) for x in labels)).items():
   for t,b in coeff(core).items():
    key=u|(t<<nc);v=c*b;amp[key]=amp.get(key,F(0))+v;q[key]=q.get(key,F(0))+v*v
 amp={k:v for k,v in amp.items() if v};p={k:v*v for k,v in amp.items()}
 ck(sum(p.values())==sum(q.values())==1);ck(all(v<=len(cores)*q[k] for k,v in p.items()))
 C=kl(p,q);nonneg(C);nonneg(add((1,h['logf'](F(len(cores)))),(-1,C)))
 return amp,q,C,ent(p)
def cut(t,i,s):return tuple(t[x] for x in range(len(t)) if ((x>>i)&1)==s)
def childstate(state,i,s):
 labels,cores,remaining,nc=state;pos=remaining.index(i)
 if pos<nc:labels=cut(labels,pos,s);nc-=1
 else:cores=tuple(cut(c,pos-nc,s) for c in cores)
 return labels,cores,tuple(x for x in remaining if x!=i),nc
def reset(state,i):
 global nodes
 nodes+=1
 labels,cores,remaining,nc=state;amp,q,C,H=stat(labels,cores)
 actual=transport(amp,q,remaining.index(i));kids=[]
 for s in (0,1):
  st=childstate(state,i,s);aa,qq,cc,hh=stat(st[0],st[1]);ck(aa==actual[s][0]);kids.append((st,cc,hh))
 avgC=add((F(1,2),kids[0][1]),(F(1,2),kids[1][1]))
 avgD=add((F(1,2),actual[0][2]),(F(1,2),actual[1][2]))
 sigma=add((1,avgC),(-1,C));raw=add((1,avgC),(-1,avgD));refund=add((1,C),(-1,avgD))
 nonneg(refund);ck(raw==add((1,sigma),(1,refund)))
 # Full terminal costs and actual entropy decrement, neither child discarded.
 avgH=add((F(1,2),kids[0][2]),(F(1,2),kids[1][2]));delta=add((1,H),(-1,avgH))
 ck(add((1,delta),(1,avgH),(1,avgC))==add((1,H),(1,C),(1,sigma)))
 return kids,sigma,raw,refund
def root_bent(r):
 lab=h['ns']['controller'](r)[3];PD=h['PD'];MAJ=h['MAJ'];TAG=h['TAG'];nc=r+1
 # All sources embedded on the SAME physical nine-bit data cube.
 cs=tuple(tuple(core[(x>>off)&(len(core)-1)] for x in range(512)) for core,off in [(TAG,0),(MAJ,3),(TAG,6)])
 return lab,cs,tuple(range(r+10)),nc
def verify_raw(state,expectedI=None):
 lab,cores,rem,nc=state;truth=tuple(cores[lab[y]][x] for x in range(len(cores[0])) for y in range(len(lab)))
 ck(coeff(truth)==stat(lab,cores)[0])
 if expectedI is not None:ck(h['edges'](truth)==expectedI)
def tree(root,order,oscillator=False):
 frontier=[(root,F(1))];total=rawsum=refundsum=possum=ZERO;startC=stat(root[0],root[1])[2];Hroot=stat(root[0],root[1])[3]
 profiles=[]
 for depth,i in enumerate(order):
  nxt=[]
  for st,reach in frontier:
   kids,sigma,raw,refund=reset(st,i)
   total=add((1,total),(reach,sigma));rawsum=add((1,rawsum),(reach,raw));refundsum=add((1,refundsum),(reach,refund))
   possum=add((1,possum),(reach,positive(sigma)))
   for child,C,hh in kids:nxt.append((child,reach/2))
  frontier=nxt
  avgC=add(*((w,stat(st[0],st[1])[2]) for st,w in frontier))
  ck(total==add((1,avgC),(-1,startC)));ck(rawsum==add((1,total),(1,refundsum)))
  avgCE=add(*((w,add((1,stat(st[0],st[1])[3]),(1,stat(st[0],st[1])[2]))) for st,w in frontier))
  path=add((1,Hroot),*((-w,stat(st[0],st[1])[3]) for st,w in frontier))
  ck(add((1,path),(1,avgCE))==add((1,Hroot),(1,avgC)))
  if oscillator:
   expect=0 if depth==len(order)-1 else (0 if depth%2==0 else 1)
   ck(avgC==const(expect));profiles.append(expect)
 return {'net':enc(total),'raw':enc(rawsum),'refunds':enc(refundsum),'positive':enc(possum),'profiles':profiles,'frontier_leaves':len(frontier)}

bent=[]
for r in ([2] if pilot else [2,4]):
 root=root_bent(r);lab,cs,rem,nc=root;eps=F(1,2**r);t=F(1,2**(r//2));pi1=(1+t-eps)/2
 If=F(r,4)+F(r+1,2)*eps+2-pi1/2
 amp,q,C,H=stat(lab,cs);ck(C==ZERO);verify_raw(root,If)
 if r>=4:
  nonneg(add((1,const(r+3)),(1,LOG3),(-1,H)))
  nonneg(add((1,const(4*If-F(1,4)) ),(-1,H),(-1,LOG3),(-1,const(F(1,4)))))
 base=nodes
 for i in rem:
  kids,*_=reset(root,i)
  if not pilot and r==2:
   for st,Cc,Hc in kids:
    for j in st[2]:reset(st,j)
 if not pilot and r==4:
  for order in [(5,11,0,6),(0,5,11,9),(6,8,1,11),(9,4,10,12)]:tree(root,order)
 bent.append({'r':r,'nodes':nodes-base,'root_I':str(If),'root_H':enc(H),'root_C':enc(C),'same_original_quota':'4Iroot','old_debit':'1/4','all_reset_reserve_lower':'7/2-2log2(3)>1/4' if r>=4 else 'boundary control only'})

osc=[]
for k in ([1,2] if pilot else [1,2,3,4]):
 v=(1,1,1,-1);w=(1,1,-1,1)
 def productcore(core):return tuple(__import__('math').prod(core[(x>>(2*j))&3] for j in range(k)) for x in range(2**(2*k)))
 cs=(productcore(v),productcore(w));root=((0,1),cs,tuple(range(2*k+1)),1)
 a,q,C,H=stat(root[0],root[1]);ck(C==const(1));ck(H==const(2*k));verify_raw(root,F(k)+F(1,2))
 order=tuple(range(1,2*k+1))+(0,);row=tree(root,order,True)
 ck(row['net']==enc(const(-1)));ck(row['positive']==enc(const(k)))
 osc.append({'k':k,'root_H':enc(H),'root_I':str(F(k)+F(1,2)),**row})
ck(3**8<2**13)
ck(nodes==(50 if pilot else 1026))
out={'status':'PASS','pilot':pilot,'checks':checks,'helper_assertions':h['checks'],'query_nodes':nodes,'cached_physical_states':stat.cache_info().currsize,'bent':bent,'oscillations':osc,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'imported_code_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest(),'external_review':'PENDING','full_fei':'OPEN'}
(RUN/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:value for key,value in out.items() if key not in ['bent','oscillations']},indent=2))
print(json.dumps([{'k':x['k'],'positive':x['positive'],'profiles':x['profiles']} for x in osc],indent=2))
