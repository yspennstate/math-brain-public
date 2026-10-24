from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time,sys
RUN=Path(__file__).resolve().parents[1]
OWN=RUN.parents[1]
OLD=OWN/'runs/20261022T231924Z-account03-A030-restriction-plateau-tests/code/check.py'
ns={'__file__':str(OLD)}
exec(OLD.read_text(encoding='utf-8').split('direct=[]')[0],ns)
add,phi,const,positive,ZERO,walsh,enc=[ns[k] for k in ['add','phi','const','positive','ZERO','walsh','enc']]
start=time.perf_counter();pilot='--pilot' in sys.argv;limit=55 if pilot else 180;checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
 assert time.perf_counter()-start<limit,'runtime guard'
def logf(q):
 d={}
 for p,e in ns['ns']['factors'](q.numerator).items():d[p]=F(e)
 for p,e in ns['ns']['factors'](q.denominator).items():d[p]=d.get(p,F(0))-e
 return ns['expr'](d)
def kl(p,q):
 ck(sum(p.values())==sum(q.values())==1)
 return add(*((v,logf(v/q[k])) for k,v in p.items() if v))
def ent(p):return add(*((1,phi(v)) for v in p.values() if v))
def nonneg(e):ck(positive(add((-1,e)))==ZERO)
def coeff(t):return {i:F(v,len(t)) for i,v in enumerate(walsh(t)) if v}
PD=(1,1,1,-1);MAJ=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
TAG=tuple(PD[x>>1]*(1 if not x&1 else -1) for x in range(8))
def build(labels,cores):
 nc=len(labels).bit_length()-1;off=0;amps={};inc={};q={}
 for j,core in enumerate(cores):
  cj=coeff(tuple(int(l==j) for l in labels));bj=coeff(core)
  pj=F(labels.count(j),len(labels))
  for t,b in bj.items():
   qt=t<<off;q[qt]=q.get(qt,F(0))+pj*b*b
   for u,c in cj.items():
    key=u|(qt<<nc);a=b*c
    amps[key]=amps.get(key,F(0))+a;inc[key]=inc.get(key,F(0))+a*a
  off+=len(core).bit_length()-1
 amps={k:v for k,v in amps.items() if v};p={k:v*v for k,v in amps.items()}
 ck(sum(p.values())==sum(inc.values())==1)
 marg={};margq={}
 for k,v in p.items():marg[k>>nc]=marg.get(k>>nc,F(0))+v
 for k,v in inc.items():margq[k>>nc]=margq.get(k>>nc,F(0))+v
 ck(marg==margq==q)
 return amps,p,inc,nc+off
def raw(labels,cores):
 nc=len(labels).bit_length()-1;offs=[];off=nc
 for core in cores:offs.append(off);off+=len(core).bit_length()-1
 return tuple(cores[labels[x&(len(labels)-1)]][(x>>offs[labels[x&(len(labels)-1)]])&(len(cores[labels[x&(len(labels)-1)]])-1)] for x in range(2**off))
def edges(t):
 return sum((F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(len(t).bit_length()-1)),F(0))
def remove(k,i):return (k&((1<<i)-1))|((k>>(i+1))<<i)
def transport(amp,ref,i):
 keys={k&~(1<<i) for k in set(amp)|set(ref)};children=[];rhos=[]
 for s in (0,1):
  aout={};sub={}
  for k in keys:
   a,b=amp.get(k,F(0)),amp.get(k|(1<<i),F(0));v=a+(-1)**s*b;new=remove(k,i)
   if v:aout[new]=v
   den=2*(a*a+b*b);kernel=v*v/den if den else F(1,2)
   mass=(ref.get(k,F(0))+ref.get(k|(1<<i),F(0)))*kernel
   if mass:sub[new]=mass
  rho=sum(sub.values());ck(rho>0);rhos.append(rho)
  rchild={k:v/rho for k,v in sub.items()};pchild={k:v*v for k,v in aout.items()}
  ck(sum(pchild.values())==1);ck(set(pchild)<=set(rchild))
  children.append((aout,rchild,kl(pchild,rchild)))
 ck(sum(rhos)==1)
 dp=kl({k:v*v for k,v in amp.items()},ref)
 gap=add((1,dp),(-F(1,2),children[0][2]),(-F(1,2),children[1][2]))
 nonneg(gap)
 # Fair true outcomes versus ACTUAL reference branch masses are retained.
 outcome=kl({0:F(1,2),1:F(1,2)},{0:rhos[0],1:rhos[1]})
 nonneg(add((1,gap),(-1,outcome)))
 return children

rows=[];target=None
for r in ([2,4] if pilot else [4,6,8]):
 _,_,_,labels=ns['controller'](r);eps=F(1,2**r);t=F(1,2**(r//2));nc=r+1
 a,p,inc,n=build(labels,(TAG,MAJ,TAG));ck(p==inc) # no overlap at balanced root
 Hroot=ent(p);nonneg(add((1,const(r+5)),(-1,Hroot)))
 pi=[F(labels.count(j),len(labels)) for j in range(3)]
 If=F(r,4)+F(r+1,2)*eps+2-pi[1]/2
 if r>=4:ck(If>=F(r,4)+F(27,16));nonneg(add((1,const(4*If-F(7,4))),(-1,Hroot)))
 if r==(2 if pilot else 4):
  rt=raw(labels,(TAG,MAJ,TAG));ck(coeff(rt)==a);ck(edges(rt)==If)
 leaves=[]
 for sa in (1,-1):
  for sb in (1,-1):
   aa,pp,qq,nn=build(labels,(tuple(sa*x for x in PD),MAJ,tuple(sb*x for x in PD)))
   C=kl(pp,qq);nonneg(C);qvac=(pi[0]+pi[2])/4
   nonneg(add((1,const(qvac)),(-1,C)))
   if sa==1 and sb==-1:
    ck(C!=ZERO);ck(qvac<F(1,8));target=(aa,qq,nn)
    chi=sum(((pp.get(k,F(0))-v)**2/v for k,v in qq.items()),F(0))
    ck(chi<=eps/4);nonneg(add((1,const(3*eps/8)),(-1,C)))
    rootcost=add((1,Hroot),(F(1,4),C),(1,const(F(1,4))))
    if r>=4:nonneg(add((1,const(4*If-F(765,512))),(-1,rootcost)))
    chosenC=C
   leaves.append(ent(pp))
 # Exact reference source choice has W=Z=0; no inherited Z is invented.
 ck(kl(p,p)==ZERO)
 rows.append({'r':r,'root_I':str(If),'root_H':enc(Hroot),'reset_C':enc(chosenC),'C_bounds':ns['smallbounds'](chosenC),'qvac':str(qvac),'root_weighted_reset_bounds':ns['smallbounds'](add((F(1,4),chosenC))),'same_quota':'4*I_root','old_debit':'1/4','all_four_tag_outcomes_retained':True,'source_Z':'0'})

# Actual Boolean shared-source sharpness fixtures, L=2 and4 uniform labels.
for L in (2,4):
 # Shared data: every source is PD, so actual F is PD independent of label.
 cs=[coeff(tuple(int(j==l) for l in range(L))) for j in range(L)]
 pp={k*L:v*v for k,v in coeff(PD).items()};qq={}
 for c in cs:
  for u,v in c.items():
   for t,b in coeff(PD).items():qq[u+L*t]=qq.get(u+L*t,F(0))+v*v*b*b
 ck(kl(pp,qq)==const(L.bit_length()-1))

continuation_nodes=0
if not pilot:
 # Rebuild r4 target; main rows deliberately ended at r8.
 _,_,_,lab=ns['controller'](4);amp,pp,ref,n=build(lab,(PD,MAJ,tuple(-x for x in PD)))
 ck(coeff(raw(lab,(PD,MAJ,tuple(-x for x in PD)) ))==amp)
 for i in range(n):transport(amp,ref,i);continuation_nodes+=1
 # Four complete depth-three policies, including mixed control/source queries.
 for order in ((0,1,2),(5,0,6),(7,9,0),(11,4,6)):
  frontier=[(amp,ref,list(range(n)))];total=ZERO
  for original in order:
   new=[]
   for aa,rr,remaining in frontier:
    i=remaining.index(original);kids=transport(aa,rr,i);continuation_nodes+=1
    rem=[k for k in remaining if k!=original]
    new.extend((a,r,rem) for a,r,d in kids)
   frontier=new
  avgD=add(*((F(1,len(frontier)),kl({k:v*v for k,v in aa.items()},rr)) for aa,rr,_ in frontier))
  nonneg(add((1,kl(pp,ref)),(-1,avgD)))

out={'status':'PASS','pilot':pilot,'checks':checks,'rows':rows,'physical_continuation_nodes':continuation_nodes,'sharp_shared_source_L':[2,4],'max_post_reset_depth':0 if pilot else 3,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256(ns['OLD'].read_bytes()).hexdigest(),'external_review':'PENDING','full_fei':'OPEN'}
(RUN/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
print(json.dumps([{'r':v['r'],'C':v['C_bounds'],'root_cost':v['root_weighted_reset_bounds']} for v in rows],indent=2))
