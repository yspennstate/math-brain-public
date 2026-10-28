"""Full actual source/reference replay at every frozen affine-pivot cut."""
from pathlib import Path
from fractions import Fraction as F
import json,time,sys
import arith as A
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter();COUNTS={'prefix_nodes':0,'prefix_queries':0,'pivot_queries':0,'reset_children':0,'post_reset_queries':0}
RECORDS=[]
def ck(b,s): A.ck(b,s)
def add(*x): return A.plus(*x)
def scalar(a,x): return add((a,x))
def prod(ds):
 return tuple(__import__('functools').reduce(lambda a,j:a*(ds[j] if s>>j&1 else 1-ds[j]),range(len(ds)),F(1)) for s in range(1<<len(ds)))
def before(t,R,g,ids,coreids,path,depth,pilot):
 COUNTS['prefix_nodes']+=1
 p,ds,H,M,TC=A.stats(t);gp,gd,gH,gM,gTC=A.stats(g);K=A.kl(p,R);P=add((1,K),(2,gM))
 A.nonneg(add((1,P),(-1,K)),'pre-pivot inherited stop retains full KL')
 vi=ids.index(1);cs,Rs,r,O,E,Ks,zmass=A.transport(t,vi,R);COUNTS['pivot_queries']+=1
 # The pivot is a physical query: neither prediction fairness nor zero erasure is assumed.
 Pi=[add((1,Ks[b]),(2,gM)) for b in [0,1]]
 ck(not add((1,P),(F(-1,2),Pi[0]),(F(-1,2),Pi[1]),(-1,E),(-1,O)),'exact pivot increment')
 for b in [0,1]:
  cp,cd,cH,cM,cTC=A.stats(cs[b]);ck(cH==gH and cM==gM and cTC==gTC,'actual pivot children are character translates; full H/M/TC')
  Q=prod(cd);ck(sum(Q)==1,'actual product reference normalized');ck(A.kl(cp,Q)==cTC,'reset actual KL=TC')
  V=add((1,cTC),(1,cM));ck(not add((1,Pi[b]),(-1,V),(-1,Ks[b]),(-1,gH)),'exact signed reset drop Kchild+Hcore')
  A.nonneg(add((1,Pi[b]),(-1,V)),'same original allocation dominates actual reset and continuation')
  A.nonneg(add((1,Pi[b]),(-1,Ks[b]),(-1,cM)),'unreset continuation also admitted')
  COUNTS['reset_children']+=1
  for j in range(len(cd)):
   ts,Qs,rr,oo,ee,kk,zz=A.transport(cs[b],j,Q);COUNTS['post_reset_queries']+=1
   Vc=[]
   for bb in [0,1]:
    pp,dd,hh,mm,tt=A.stats(ts[bb]);vc=add((1,kk[bb]),(1,mm));Vc.append(vc)
    A.nonneg(add((1,vc),(-1,kk[bb])),'full inherited terminal KL')
    A.nonneg(add((1,vc),(-1,tt)),'full actual terminal product KL retained')
    ck(not add((1,hh),(1,vc),(-1,hh),(-1,kk[bb]),(-1,mm)),'full terminal H+KL not dropped')
   A.nonneg(add((1,V),(F(-1,2),Vc[0]),(F(-1,2),Vc[1]),(-1,oo)),'actual post-reset continuation drift')
 RECORDS.append({'path':path,'reference_sha256':A.refhash(R),'K':A.value(K),'M_core':A.value(gM),'H_core':A.value(gH),
  'pivot_r':[str(x) for x in r],'pivot_E':A.value(E),'pivot_O':A.value(O),'pivot_reference_only_mass':str(zmass),
  'pre_reset_K':[A.value(x) for x in Ks],'full_terminal_H_preserved':True})
 if depth==0:return
 allowed=[i for i,x in enumerate(ids) if x!=1]
 if pilot:allowed=[ids.index(0)] if 0 in ids else []
 for j in allowed:
  who=ids[j];ts,Qs,rr,oo,ee,kk,zz=A.transport(t,j,R);COUNTS['prefix_queries']+=1
  gs=[g,g] if who==0 else [A.child(g,coreids.index(who),b) for b in [0,1]]
  ncoreids=coreids if who==0 else [x for x in coreids if x!=who]
  Ps=[add((1,kk[b]),(2,A.stats(gs[b])[3])) for b in [0,1]]
  drop=add((1,gM),(F(-1,2),A.stats(gs[0])[3]),(F(-1,2),A.stats(gs[1])[3]))
  A.nonneg(drop,'core M supermartingale, mask coordinate decrement zero')
  ck(not add((1,P),(F(-1,2),Ps[0]),(F(-1,2),Ps[1]),(-1,ee),(-1,oo),(-2,drop)),'exact pre-pivot increment')
  for b in [0,1]:before(ts[b],Qs[b],gs[b],ids[:j]+ids[j+1:],ncoreids,path+[[who,b]],depth-1,pilot)
def main():
 pilot='pilot' in sys.argv;h=A.core(2);tables=[]
 for g in [(1,)*64,h]:
  tables.append(tuple(g[s>>2]*(-1 if (((s&1)+((s>>1)&1)+((s>>2).bit_count()&1))&1)*((s>>1)&1) else 1) for s in range(256)))
 root=tuple(tables[s&1][s>>1] for s in range(512));Qroot=(F(1,512),)*512
 cs,Rs,r,O,E,Ks,z=A.transport(root,0,Qroot)
 ck(cs==tables,'actual9-bit selector children');ck(not E,'selector erasure exactly zero');ck(r==[F(1,8),F(7,8)],'original selector reaches')
 hh=A.stats(h)[2];Mh=A.stats(h)[3];S=A.const(F(23,2));W=8
 ck(hh==A.const(5),'actual core entropy');A.strict(add((1,A.const(W)),(-1,Mh)),'same old W covers new expected reserve')
 A.strict(add((F(5,7),S),(-1,A.const(W))),'same old5/7 bound');A.strict(add((F(3,4),S),(-1,A.const(W)),(F(-1,28),S)),'same owner spare>S/28 after old quarter')
 Kroot=A.kl(A.stats(root)[0],Qroot);Proot=add((1,Kroot),(1,Mh));Pbranch=[Ks[0],add((1,Ks[1]),(2,Mh))]
 ck(not add((1,Proot),(F(-1,2),Pbranch[0]),(F(-1,2),Pbranch[1]),(-1,O)),'one original expected allocation at selector')
 for b in [0,1]:before(cs[b],Rs[b],[(1,)*64,h][b],list(range(8)),list(range(2,8)),[['selector',b]],1 if pilot else 2,pilot)
 expected={'prefix_nodes':6,'prefix_queries':2,'pivot_queries':6,'reset_children':12,'post_reset_queries':76} if pilot else {'prefix_nodes':366,'prefix_queries':182,'pivot_queries':366,'reset_children':732,'post_reset_queries':3724}
 ck(COUNTS==expected,'frozen exact coverage')
 elapsed=time.perf_counter()-START;ck(elapsed<55,'frozen runtime')
 out={'status':'PASS','exact_assertions':A.COUNT,'counts':COUNTS,'seconds':elapsed,'S_original':'23/2','W_old':8,
 'expected_core_reserve':A.value(Mh),'new_owner_topup_if_W_already_booked':0,'spare_after_old_quarter':'>S_original/28',
 'u_ordinary_orders_both_present':not pilot,'records':RECORDS}
 (ROOT/'out').mkdir(exist_ok=True)
 (ROOT/'out'/('PILOT.json' if pilot else 'FIELD.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'}))
if __name__=='__main__':main()
