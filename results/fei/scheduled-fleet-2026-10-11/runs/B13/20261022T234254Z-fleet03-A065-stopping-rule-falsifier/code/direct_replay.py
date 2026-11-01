"""Separate direct Fourier / GF4 construction and normalized reference transport."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import reference as k
import json,time
ROOT=Path(__file__).resolve().parents[1]

@lru_cache(None)
def spectrum(t):
 n=len(t)
 return tuple(F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t))**2,n*n) for s in range(n))

def restrict(t,i,b):
 n=len(t)//2
 return tuple(t[((x>>i)<<(i+1))|(x&((1<<i)-1))|(b<<i)] for x in range(n))

def transport(t,Q,i):
 p=spectrum(t);tt=[restrict(t,i,b) for b in (0,1)];pc=[spectrum(x) for x in tt]
 es=[];eq=[];weights=[[],[]]
 for x in range(len(t)//2):
  index=((x>>i)<<(i+1))|(x&((1<<i)-1))
  source=p[index]+p[index+(1<<i)];ref=Q[index]+Q[index+(1<<i)]
  es.append(source);eq.append(ref)
  for b in (0,1):weights[b].append(ref*(pc[b][x]/(2*source) if source else F(1,2)))
 reaches=[sum(w) for w in weights];QQ=[tuple(x/reaches[b] for x in weights[b]) for b in (0,1)]
 O=k.kl((F(1,2),F(1,2)),reaches);Ks=[k.kl(pc[b],QQ[b]) for b in (0,1)]
 E=k.plus((1,k.kl(p,Q)),(-1,k.kl(es,eq)))
 k.eq(k.kl(p,Q),k.plus((1,E),(1,O),(F(1,2),Ks[0]),(F(1,2),Ks[1])))
 return tt,QQ,O,Ks,E

def tc(t):
 p=spectrum(t);n=len(t).bit_length()-1
 ds=[sum((v for s,v in enumerate(p) if s&(1<<i)),F()) for i in range(n)]
 return k.plus(*[(1,k.ent((d,1-d))) for d in ds],(-1,k.ent(p)))

def main():
 start=time.perf_counter()
 gf4=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
 parent=[]
 for x in range(512):
  s=x&1;u=(x>>1)&1;v=(x>>2)&1;z=x>>3
  a=z&3;b=(z>>2)&3;xx=z>>4
  h=(-1 if a&1 else 1)*(-1 if xx==gf4[a][b] else 1)
  carrier=-1 if ((u^v^(z.bit_count()%2))&v) else 1
  parent.append(carrier*(h if s else 1))
 parent=tuple(parent);Q=(F(1,512),)*512
 source_mass=sum((q for p,q in zip(spectrum(parent),Q) if p),F())
 k.ck(source_mass==F(25,32),'reference mass on actual source support')
 predicted_two=source_mass*F(1,8)+(1-source_mass)*F(1,2)
 k.ck(predicted_two==F(53,256) and predicted_two!=F(1,8),'global fair-extension transport does NOT tensorize')
 (ROOT/'out/NON_TENSOR.json').write_text(json.dumps({'module_source_support_reference_mass':str(source_mass),'module_selector_prediction':'1/8','two_module_FIRST_selector_prediction':str(predicted_two),'formula':'a*r+(1-a)/2; globally source-zero other-module rows are fair','conclusion':'No L-fold amplification of this reference-based cut is certified. Earlier entropy/influence tensor amplification is unaffected.'},indent=2),encoding='utf-8')
 children,refs,Os,Ks,Es=transport(parent,Q,0)
 K0=k.kl(spectrum(parent),Q)
 dchildren,drefs,Od,Kd,Ed=transport(children[1],refs[1],2)
 k.eq(Ed,{},'actual data erasure credit is zero')
 terminals=[];OT=[];Hterm=[]
 for t,R in zip(dchildren,drefs):
  vv,_,Ov,_,_=transport(t,R,1);k.eq(Ov,{})
  k.eq(tc(vv[0]),tc(vv[1]))
  terminals.extend(vv);OT.extend([tc(vv[0]),tc(vv[1])]);Hterm.extend([k.ent(spectrum(vv[0])),k.ent(spectrum(vv[1]))])
 old=k.plus((1,k.constant(11)),(-F(3,2),k.log(F(3))),(-F(5,2),k.log(F(5))),(-1,k.log(F(7))))
 oldW=k.plus((F(1,2),old))
 new=k.plus((1,k.constant(F(13,2))),(-F(9,8),k.log(F(3))),(-F(5,8),k.log(F(5))),(-1,k.log(F(7))))
 increase=k.plus((1,new),(-1,old))
 # Asymmetric actual cut: G STOP with its current KL, H completes data/v conversion.
 Kcut=k.plus((F(1,2),Ks[0]),*[(F(1,8),tc0) for tc0 in OT])
 Ocut=k.plus((1,Os),(F(1,2),Od))
 gap=k.plus((1,Kcut),(1,Ocut),(-1,K0),(-1,oldW))
 k.eq(gap,k.plus((F(1,2),increase)),'complete stopping-cut shortfall')
 k.ck(3**75*5**375>2**988,'increase>11/25 exact power certificate')
 k.ck(3**225*5**125*7**200>2**1208,'new total expected booking<original S/50')
 k.ck(k.interval(increase)[0]>F(11,25))
 k.ck(k.interval(gap)[0]>F(11,50))
 newW=k.plus((F(1,2),new));S=F(23,2)
 owner={}
 for cc in children:
  pc=spectrum(cc);n=len(cc).bit_length()-1
  I=sum((sum((mass for freq,mass in enumerate(pc) if freq&(1<<i)),F()) for i in range(n)),F())
  edges=sum(F(sum(cc[x]!=cc[x^(1<<i)] for x in range(len(cc))),len(cc)) for i in range(n))
  k.ck(I==edges==4,'same physical original owner, independent edge count')
  owner=k.plus((1,owner),(F(1,2),k.plus((1,k.constant(4*I)),(-1,k.ent(pc)))))
 k.eq(owner,k.constant(S),'original S is actual mean4I-H, not a renewed bank')
 k.ck(k.interval(newW)[1]<S/50)
 k.ck(S*F(3,4)-k.interval(newW)[1]>S*F(73,100),'oldquarter retained in same bank')
 rows=json.loads((ROOT/'out/INTERPOSITION.json').read_text(encoding='utf-8'))['records']
 for row in rows:
  newrow={int(p):F(c) for p,c in row['new_parent_booking']['exact'].items()}
  if row['l']==3:k.eq(newrow,{},'all fixed l3 directions zero')
  elif row['selector_branch']==0:k.eq(newrow,{})
  else:k.ck(k.interval(newrow)[1]<F(23,50),'all l2 directions paid by original 1/50')
 k.ck(time.perf_counter()-start<55)
 out={'status':'PASS','exact_assertions':k.COUNT,'seconds':time.perf_counter()-start,'branch_increase':k.enc(increase),'complete_cut_gap':k.enc(gap),'complete_cut_gap_interval':k.enciv(gap),'new_root_booking':k.enc(newW),'new_root_booking_interval':k.enciv(newW),'old_booking':k.enc(oldW),'original_owner':str(S),'cut_mean_H':k.enc(k.plus((F(1,2),k.ent(spectrum(children[0]))),*[(F(1,8),H) for H in Hterm])),'cut_mean_KL':k.enc(Kcut),'cut_outcome_cost':k.enc(Ocut),'root_KL':k.enc(K0),'G_current_KL':k.enc(Ks[0]),'data_erasure_credit':k.enc(Ed),'all_fixed_cases_paid_fraction':'1/50','after_OLD_quarter_fraction_greater_than':'73/100','all_widths_invariance':'written proof only; payment certificate only l2,l3'}
 (ROOT/'out/DIRECT_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print({key:out[key] for key in ['status','exact_assertions','seconds','complete_cut_gap_interval','new_root_booking_interval']})
if __name__=='__main__':main()
