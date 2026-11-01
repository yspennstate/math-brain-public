from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util,json,time,sys,hashlib
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
primitive=R.parent/'20261023T021528Z-fleet03-A003-minimal-target-formulation/code/verify_absorption.py'
spec=importlib.util.spec_from_file_location('a003_previous_primitives',primitive);v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
pilot='--pilot' in sys.argv;START=time.perf_counter();CAP=55 if pilot else 180
CHECKS=0;stats={'cases':0,'zero_actual_singleton_funded':0,'strict_shape_changes':0,'positive_shape_bills':0,'zero_energy':0,'sparse_source_cases':0}
def ck(x):
 global CHECKS
 CHECKS+=1
 if not x:raise AssertionError(CHECKS)
 if time.perf_counter()-START>CAP:raise TimeoutError(CAP)
 # Reused helper has an independent short guard; reset its timer per case.
v.ck=ck
def coef(f):
 z=list(f);step=1
 while step<len(z):
  for a in range(0,len(z),step*2):
   for i in range(a,a+step):p,q=z[i],z[i+step];z[i],z[i+step]=p+q,p-q
  step*=2
 return [F(x,len(z)) for x in z]
def P(f):return [x*x for x in coef(f)]
def m(q,j):return v.marg(q,j)
def ce(p,q):return v.ce(p,q)
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def coherent(a,h,sg,Rseed):
 b=[1-x*x for x in a];A=coef(a);B=coef(b);mu=F(sum(h),len(h));nc=len(a)
 q=[(A[u]+sg*mu*B[u])**2 if t==0 else B[u]**2*Rseed[t] for t in range(len(h)) for u in range(nc)]
 g=[a[u]+sg*b[u]*h[t] for t in range(len(h)) for u in range(nc)]
 ck(set(g)<={-1,1});ck(sum(q)==1);ck(min(q)>=0)
 return g,q,A,B
BASE=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
controllers=[BASE]+[tuple(v.restrict(BASE,j,bit)) for j in range(4) for bit in [0,1]]
def cases():
 ans=[]
 for n in [1,2]:
  for mask in range(1<<(1<<n)):
   h=tuple(1 if mask>>i&1 else -1 for i in range(1<<n))
   for a in controllers:
    for sg in [-1,1]:
     for ref in range(3):
      for j in range(n):ans.append((a,h,sg,ref,j,'exhaustive'))
 for h,label in [(tuple((-1)**i.bit_count() for i in range(8)),'parity3'),(tuple(-1 if i in [0,1,2,4] else 1 for i in range(16)),'nonpoint4')]:
  for sg in [-1,1]:
   for ref in range(3):
    for j in range((len(h)-1).bit_length()):ans.append((BASE,h,sg,ref,j,label))
 return ans
WITNESSES=[]
def check(row,index):
 a,h,sg,ref,j,label=row;ph=P(h);mu=F(sum(h),len(h));d=coef(h)[1<<j];N=len(h)
 if ref==0:rs=ph;stats['sparse_source_cases']+=1
 else:
  w=[F(1) if ref==1 else F(k) for k in range(1,N)];rs=[mu*mu]+[(1-mu*mu)*x/sum(w) for x in w]
 g,q,A,B=coherent(a,h,sg,rs);pg=P(g);nc=(len(a)-1).bit_length();beta=sum(b*b for b in B)
 C=sum(x*x*y*y for x,y in zip(A,B));D=sum(x*y**3 for x,y in zip(A,B));E=sum(y**4 for y in B)
 Gamma=C-D*D/E if E else F(0);delta=rs[1<<j]-d*d
 fm=sum(y*y*(sg*x+mu*y)**2 for x,y in zip(A,B))
 x=Gamma*d*d+delta*delta*(E+beta*beta)/4
 xe=d*d*(fm+beta*beta*mu*mu)+delta*delta*(E+beta*beta)/4
 ck(Gamma>=0);ck(xe>=x>=0)
 if a==BASE:ck((beta,C,D,E,Gamma)==(F(3,8),F(3,512),F(3,256),F(21,512),F(9,3584)))
 qbar=m(q,nc+j);pm=m(pg,nc+j);rbar=m(rs,j)
 qc=[qbar[u] for u in range(len(a))]+[sum(qbar[len(a):])]
 childps=[];oldCE=[];calCE=[];newCE=[];kcoarse=[];zs=[];vectors=[];eps=[]
 for bit in [0,1]:
  hh=v.restrict(h,j,bit);p=P(hh);mt=F(sum(hh),len(hh));rt=v.cal(rbar,p[0])
  gg,qq,AA,BB=coherent(a,hh,sg,rt);pp=P(gg)
  ck(gg==v.restrict(g,nc+j,bit));ck(mt==mu+(d if bit==0 else -d))
  coarse=[pp[u] for u in range(len(a))]+[sum(pp[len(a):])]
  ck(sum(coarse)==sum(qc)==1)
  for u in range(len(a)):ck(qc[u]==(A[u]+sg*mu*B[u])**2+B[u]**2*rs[1<<j])
  ck(qc[-1]==beta*(1-mu*mu-rs[1<<j]))
  childps.append(pp);vectors.append(coarse)
  raw=ce(pp,qbar);cal=ce(pp,qq);k=v.sub(ce(coarse,qc),ce(coarse,coarse))
  ck(overlap(v.sub(raw,cal),k));oldCE.append(raw);calCE.append(cal);kcoarse.append(k)
  t=beta*(1-mt*mt);ee=x/(t+x) if x and t else F(0);eps.append(ee)
  newr=list(rt)
  if ee:
   target=[F(0)]*len(p);target[1]=F(1)
   newr=[rt[0]]+[(1-ee)*rt[z]+ee*(1-mt*mt)*target[z] for z in range(1,len(p))]
   if newr!=rt:stats['strict_shape_changes']+=1
  _,new,_,_=coherent(a,hh,sg,newr);newcost=ce(pp,new);z=v.sub(newcost,cal)
  if z[0]>0:stats['positive_shape_bills']+=1
  newCE.append(newcost);zs.append(z)
  if x:ck(z[1]<=x/v.LN2[0])
  else:ck(newr==rt)
  ck(sum(new)==1)
  if ee:ck(0<ee<1)
 meanvec=[(u+w)/2 for u,w in zip(*vectors)];diff=[(u-w)/2 for u,w in zip(*vectors)]
 sq=sum((u-w)**2 for vv in vectors for u,w in zip(vv,qc))/2
 ck(sq==sum(y*y for y in diff)+sum((u-w)**2 for u,w in zip(meanvec,qc)))
 ck(sq==4*xe)
 for u in range(len(a)):ck(meanvec[u]-qc[u]==-delta*B[u]**2)
 ck(meanvec[-1]-qc[-1]==beta*delta)
 meanK=v.mul(F(1,2),v.add(*kcoarse))
 if x:ck(meanK[0]>=2*x/v.LN2[0])
 rootce=ce(pg,q);erasure=v.sub(ce(pg,pg),ce(pm,pm));avgold=v.mul(F(1,2),v.add(*oldCE));avgnew=v.mul(F(1,2),v.add(*newCE))
 rho=v.sub(rootce,v.add(erasure,avgold));increment=v.sub(v.add(erasure,avgnew),rootce)
 reconstructed=v.add(v.mul(-1,rho),v.mul(F(1,2),v.add(v.sub(zs[0],kcoarse[0]),v.sub(zs[1],kcoarse[1]))))
 ck(overlap(increment,reconstructed))
 if x:ck(increment[1]<=-x/v.LN2[1])
 if not x:stats['zero_energy']+=1
 if d==0 and x>0:stats['zero_actual_singleton_funded']+=1
 if label=='parity3' and a==BASE and sg==1 and j==0:
  if ref==0:
   ck(x==0);ck(pg==q);ck(vectors[0]==vectors[1]==qc)
   for interval in [erasure,rho,meanK,increment]:ck(interval[0]<=0<=interval[1])
  if ref==1:
   ck(x==F(93,100352));ck(eps==[F(31,12575)]*2);ck(all(z[0]>0 for z in zs))
  WITNESSES.append({'source_kind':ref,'d':str(d),'reference_singleton':str(rs[1]),'x':str(x),'epsilon':[str(z) for z in eps],'mean_block_refund':[str(z) for z in meanK],'shape_bills':[[str(y) for y in z] for z in zs],'full_transaction_increment':[str(z) for z in increment]})
 stats['cases']+=1
def main():
 rows=cases();frozen=json.loads((R/'FROZEN_SPEC.json').read_text(encoding='utf-8'));ck(len(rows)==1986)
 indices=[i*1986//64 for i in range(62)]+[1956,1985] if pilot else range(len(rows))
 for i in indices:check(rows[i],i)
 ck(stats['zero_actual_singleton_funded']>0);ck(stats['strict_shape_changes']>0)
 result={'status':'EXACT_PASS','mode':'pilot' if pilot else 'full','helper':frozen['helper_version'],'counts':stats,'assertions':CHECKS,'runtime_seconds':time.perf_counter()-START,'primitive_path':str(primitive),'primitive_sha256':hashlib.sha256(primitive.read_bytes()).hexdigest(),'rung':'finite exact certificates plus separate all-dimensional analytic proof; no Lean or independent acceptance claimed'}
 (R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 if not pilot:(R/'out/PARITY_WITNESSES.json').write_text(json.dumps(WITNESSES,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result))
if __name__=='__main__':main()
