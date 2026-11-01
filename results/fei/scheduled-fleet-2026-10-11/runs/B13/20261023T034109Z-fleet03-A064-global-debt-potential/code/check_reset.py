from pathlib import Path
from fractions import Fraction as F
import json,time,sys,hashlib
import exact as e
R=Path(__file__).resolve().parents[1]; start=time.perf_counter()
pilot='--pilot' in sys.argv
queries=children=fixtures=0
def nonneg(x,label):
 e.ck(not x or e.interval(x)[0]>=0,label)
def drift(t,Q,indices):
 global queries,children
 p,ds,H,M,TC=e.stats(t);K=e.kl(p,Q);V=e.plus((1,K),(1,M))
 for i in indices:
  cc,qq,rr,O,KK,E,z=e.transport(t,i,Q);queries+=1
  MC=[e.stats(c)[3] for c in cc]
  nonneg(e.plus((1,M),(-F(1,2),MC[0]),(-F(1,2),MC[1])),'physical full-M concavity')
  vv=[e.plus((1,KK[b]),(1,MC[b])) for b in (0,1)]
  nonneg(e.plus((1,V),(-1,O),(-F(1,2),vv[0]),(-F(1,2),vv[1])),'continued drift pays O')
  for b,c in enumerate(cc):
   children+=1
   pc,dc,hc,mc,tc=e.stats(c)
   e.eq(tc,e.kl(pc,e.product(dc)),'actual final second product reset')
   nonneg(e.plus((1,vv[b]),(-1,tc)),'all final KL retained')
   e.eq(e.plus((1,hc),(1,tc)),mc,'full final cross entropy kept')
def field(l):
 h=e.core(l);m=3*l;q=1<<l
 G=e.carrier((1,)*len(h));H=e.carrier(h)
 t=tuple((G if not s&1 else H)[s>>1] for s in range(2*len(G)))
 p,d,hh,mm,Kroot=e.stats(t);_,_,Hh,Mh,_=e.stats(h)
 e.ck(all(x==F(1,2) for x in d),'root actual product is uniform')
 cc,qq,rr,O,KK,E,z=e.transport(t,0,[F(1,len(t))]*len(t))
 e.eq(E,{})
 e.ck(rr==[F(1,2*q),1-F(1,2*q)],'original prediction includes reference-only rows')
 S=e.plus((1,e.constant(2*m+2)),(-F(1,2),Hh));W=e.constant(m+2)
 e.ck(e.interval(e.plus((F(5,7),S),(-1,W)))[0]>0,'original 5/7 cap')
 e.ck(e.interval(e.plus((F(3,4)-F(1,28),S),(-1,W)))[0]>0,'old-quarter residual > S/28')
 P0=e.plus((1,Kroot),(1,W));P1=[e.plus((1,k),(1,W)) for k in KK]
 e.eq(e.plus((1,P0),(-F(1,2),P1[0]),(-F(1,2),P1[1])),O,'fixed selector paid')
 records=[]
 for b,c in enumerate(cc):
  e.eq(e.stats(c)[3],W,'OLD full-M pending allocation')
  vcc,vqq,vrr,vO,vKK,vE,vz=e.transport(c,1,qq[b]);e.eq(vO,{})
  e.eq(vE,{},'carrier erasure credit exactly zero')
  e.ck(vrr==[F(1,2),F(1,2)],'inherited carrier outcome fair')
  resetVs=[];signed=[]
  for k,leaf in enumerate(vcc):
   e.eq(vKK[k],KK[b],'EACH before-reset cut retains inherited core KL')
   pl,dl,hl,ml,tcl=e.stats(leaf);fresh=e.product(dl)
   e.eq(tcl,e.kl(pl,fresh),'actual INTERMEDIATE product reference')
   e.eq(hl,Hh if b else {},'full entropy at intermediate reset')
   e.eq(ml,Mh if b else {},'unused u deterministic, character complement entropy invariant')
   resetVs.append(e.plus((1,tcl),(1,ml)))
   signed.append(e.plus((1,tcl),(-1,vKK[k])))
   n=len(leaf).bit_length()-1
   # Keep physical unused u present, including its deterministic spectral boundary.
   drift(leaf,fresh,[1] if pilot else list(range(1,n)))
  resetGap=e.plus((1,P1[b]),(-1,vO),(-F(1,2),resetVs[0]),(-F(1,2),resetVs[1]))
  nonneg(resetGap,'splice paid by OLD allocation, no renewal')
  combined=e.plus((1,vO),(F(1,2),resetVs[0]),(F(1,2),resetVs[1]),(-1,KK[b]))
  target=e.plus((2,Mh),(-1,e.constant(m)),(-1,e.log(rr[1]))) if b else e.plus((-1,KK[0]))
  e.eq(combined,target,'complete signed reset-plus-continuation debit')
  records.append({'selector_branch':b,'inherited_KL':e.enc(KK[b]),'old_pending':m+2,'actual_reset_signed_debits':[e.enc(x) for x in signed],'reset_continuation_debit':e.enc(combined),'splice_spare_interval':e.enciv(resetGap),'reference_only_mass':str(vz)})
 return {'l':l,'original_Sbar':e.enc(S),'W':m+2,'after_old_quarter_minus_W':e.enciv(e.plus((F(3,4),S),(-1,W))),'records':records}
def generic():
 global fixtures
 for mask in ([0,7] if pilot else range(16)):
  t=tuple(1 if mask&(1<<s) else -1 for s in range(4))
  for Q in ([F(1,4)]*4,[F(x,11) for x in (1,2,3,5)]):
   fixtures+=1;drift(t,Q,range(2))
generic();fields=[field(l) for l in ([2] if pilot else [2,3])]
# Analytical affine guards, using only integer inequalities for all l>=3.
e.ck(3*3-8>=1,'all-l guard grows with l')
e.ck(F(5,7)*F(23,2)-8==F(3,14),'separate l2 guard')
e.ck(F(7,8)>F(1,2),'strict original H prediction bound')
e.ck(queries==(12 if pilot else 124),'nonempty exact domain count')
e.ck(children==2*queries,'both actual terminal children')
e.ck(fixtures==(4 if pilot else 32),'generic cases not missing')
elapsed=time.perf_counter()-start;e.ck(elapsed<55,'frozen runtime')
out={'status':'PASS','pilot':pilot,'assertions':e.COUNT,'seconds':elapsed,'query_nodes':queries,'actual_query_children':children,'generic_fixtures':fixtures,'field_widths':[x['l'] for x in fields],'records':fields,'helper_sha256':hashlib.sha256((R/'code/exact.py').read_bytes()).hexdigest()}
(R/'out'/('PILOT.json' if pilot else 'MAIN.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
