"""Exact actual eleven-bit source, global reference and every declared cut."""
from pathlib import Path
from fractions import Fraction as F
import json,time
import arith as A
R=Path(__file__).resolve().parents[1];START=time.perf_counter()
def add(*x):return A.plus(*x)
def product(ds):
 out=[]
 for s in range(1<<len(ds)):
  a=F(1)
  for j,d in enumerate(ds):a*=d if s>>j&1 else 1-d
  out.append(a)
 return tuple(out)
def source():
 h=A.core(2);inner=[]
 for x in range(512):
  s=x&1;z=x>>1;u=z&1;v=(z>>1)&1;y=z>>2
  carrier=-1 if (((u+v+(y.bit_count()&1))&1)*v) else 1
  inner.append(carrier*(h[y] if s else 1))
 return tuple(inner[x>>2]*(-1 if (x&1)*((x>>1)&1) else 1) for x in range(2048))
def main():
 t=source();p,ds,H,M,TC=A.stats(t);Q=product(ds)
 A.ck(all(d==F(1,2) for d in ds),'actual11 physical influences');A.ck(Q==(F(1,2048),)*2048,'genuine actual root product')
 A.ck(H==A.const(F(17,2)) and TC==A.const(F(5,2)),'actual root H/K');S=add((1,A.const(4*sum(ds))),(-1,H));A.ck(S==A.const(F(27,2)),'actual outer source owner')
 B=add((1,A.const(3)),(F(-1,2),A.log(F(7))));half=A.const(F(1,2))
 cs,Qs,r,O,E,Ks,z=A.transport(t,2,Q);A.ck(r==[F(1,8),F(7,8)] and not E,'ordinary prefix exact global prediction and erasure')
 A.ck(O==add((1,B),(-1,A.const(1))),'B=1+actual outcome KL')
 A.ck(Ks[0]==A.const(3) and Ks[1]==add((1,A.log(F(7))),(-1,A.const(2))),'actual inherited reference KLs')
 leaves=[];TCmean={};Hmean={};Jmean={};postcount=0
 for a in [0,1]:
  bs,Rs,rv,ov,ev,ks,zz=A.transport(cs[a],1,Qs[a]);A.ck(rv==[F(1,2)]*2 and not ov and not ev,'protected pivot actual KL boundary')
  for b in [0,1]:
   pp,dd,hh,mm,tt=A.stats(bs[b]);A.ck(ks[b]==Ks[a],'both inherited pivot KLs retained')
   A.ck(hh==A.const(2 if a==0 else 7) and mm==A.const(8),'full actual pivot H/M incl deterministic U')
   A.ck(tt==A.const(6 if a==0 else 1),'actual terminal product KL')
   J=add((1,tt),(-1,ks[b]));expected=A.const(3) if a==0 else add((1,A.const(3)),(-1,A.log(F(7))))
   A.ck(J==expected,'actual signed reset debit');A.strict(J,'both optional resets positively required')
   q=product(dd);A.ck(A.kl(pp,q)==tt,'actual normalized product reset')
   A.nonneg(add((1,ks[b]),(1,J),(-1,tt)),'full terminal cut paid')
   TCmean=add((1,TCmean),(F(1,4),tt));Hmean=add((1,Hmean),(F(1,4),hh));Jmean=add((1,Jmean),(F(1,4),J))
   qs,RR,rr,oo,ee,kk,zpost=A.transport(bs[b],1,q);A.ck(dd[1]==F(1,2),'post-reset query has nonzero influence')
   A.nonneg(add((1,tt),(F(-1,2),kk[0]),(F(-1,2),kk[1]),(-1,oo)),'post-reset arbitrary inherited continuation paid')
   for bb in [0,1]:
    postcount+=1;A.nonneg(kk[bb],'post-reset full inherited KL')
   leaves.append({'s':a,'V':b,'H':A.value(hh),'M':A.value(mm),'TC':A.value(tt),'inherited_K':A.value(ks[b]),'J':A.value(J),'reference_sha256':A.refhash(Rs[b]),
    'reference_only_mass':str(sum((v for x,v in enumerate(Rs[b]) if not pp[x]),F())),'postquery_K':[A.value(x) for x in kk],'postquery_H':[A.value(A.stats(x)[2]) for x in qs],'postquery_O':A.value(oo)})
 A.ck(Jmean==B,'exact positive-before-average minimal reserve')
 A.ck(not add((1,TCmean),(1,O),(-1,TC),(-1,B)),'complete signed endpoint reference identity')
 A.ck(not add((1,Hmean),(1,TCmean),(1,O),(-1,TC),(-1,B),(-1,Hmean)),'same FULL terminal H in old/new ledgers')
 shortfall=add((1,B),(-1,half));A.strict(add((1,shortfall),(-1,A.const(1))),'actual halfbit policy shortfall>1')
 A.strict(add((F(1,8),S),(-1,B)),'same owner pays entire B from S/8')
 A.strict(add((F(1,2),S),(-1,TC)),'full root pipeline K<S/2')
 A.strict(add((F(3,4),S),(-1,TC),(-1,B),(F(-1,8),S)),'same source balance>S/8 after oldquarter+pipeline+B')
 # Root protected-V-first policy is a real negative control: no required booking.
 vs,VQ,vr,vo,ve,vks,vz=A.transport(t,1,Q)
 for b in [0,1]:A.ck(A.stats(vs[b])[4]==vks[b],'V-first actual reset deficit zero')
 A.ck(len(t)==2048 and len(leaves)==4 and postcount==8,'frozen actual-source/cut coverage')
 seconds=time.perf_counter()-START;A.ck(seconds<55,'frozen runtime')
 out={'status':'PASS','exact_assertions':A.COUNT,'seconds':seconds,'actual_source_rows':len(t),'pivot_reset_children':4,'postquery_children':postcount,
 'root_H':A.value(H),'root_I':str(sum(ds)),'root_K':A.value(TC),'S_outer':A.value(S),'B_minimal':A.value(B),'halfbit_shortfall':A.value(shortfall),
 'actual_total_outcome_O':A.value(O),'full_mean_terminal_H':A.value(Hmean),'mean_terminal_KL':A.value(TCmean),'V_first_required_extra':0,'leaves':leaves}
 (R/'out/FULL_SOURCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in out.items() if k!='leaves'}))
if __name__=='__main__':main()
