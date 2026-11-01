from pathlib import Path
import json,time
import exact as x
from check import make,add,pos,ge
F=x.F
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()

def main():
 l=2;m=6;q=4;h=x.core(l);G=x.carrier((1,)*len(h));H=x.carrier(h)
 f=tuple((H if s&1 else G)[s>>1] for s in range(2*len(G)))
 t=make(f,f);p,ds,HH,MM,K=x.stats(t);Q=x.product(ds)
 x.ck(len(t)==2048,'11-bit actual Boolean family')
 x.ck(ds==(F(1,2),)*11,'all physical influences independently checked')
 x.ck(Q==[F(1,2048)]*2048,'GENUINE original source product')
 x.eq(x.stats(h)[2],x.constant(5),'independent field spectrum entropy')
 x.eq(HH,x.constant(F(17,2)),'full root entropy')
 x.eq(K,x.constant(F(5,2)),'full booked root KL')
 pre=x.transport(t,2,Q)
 x.ck(pre[2]==[F(1,8),F(7,8)],'actual ordinary selector prediction')
 x.eq(pre[5],{},'complete ordinary erasure credit zero')
 x.eq(pre[4][0],x.constant(3),'actual inherited G KL')
 x.eq(pre[4][1],add((1,x.constant(1)),(1,x.log(F(7,8)))),'actual inherited H KL')
 reset=[];termH=[];termK=[]
 for b in (0,1):
  piv=x.transport(pre[0][b],1,pre[1][b])
  x.ck(piv[2]==[F(1,2)]*2,'actual inherited protected-pivot prediction')
  x.eq(piv[3],{});x.eq(piv[5],{})
  for e in (0,1):
   x.eq(piv[4][e],pre[4][b],'outer bent mask preserves inherited KL')
   pp,dd,hh,mm,tc=x.stats(piv[0][e]);R=x.product(dd)
   x.eq(tc,x.kl(pp,R),'actual full terminal product KL')
   x.eq(tc,x.constant(1 if b else 6),'full terminal TC')
   x.eq(hh,x.constant(7 if b else 2),'both COMPLETE terminal entropies')
   J=add((1,tc),(-1,piv[4][e]));ge(J,{ },'both actual sibling debits positive')
   reset.append(J);termH.append(hh);termK.append(tc)
   # Proper core query after reset: query the inner mask u, not a dummy outer U.
   after=x.transport(piv[0][e],1,R)
   x.ck(x.stats(piv[0][e])[1][1]==F(1,2),'proper post-reset influence half')
   ge(tc,add((1,after[3]),(F(1,2),after[4][0]),(F(1,2),after[4][1])),'nontrivial post-reset continuation paid')
 B=add(*[(F(1,4),j) for j in reset]);expected=add((1,x.constant(3)),(-F(1,2),x.log(F(7))))
 x.eq(B,expected,'exact least additional root reserve')
 x.eq(add((1,pre[3]),*[(F(1,4),k) for k in termK],(-1,K)),B,'actual optional-reset endpoint attains minimum')
 ge(B,x.constant(F(3,2)),'strict positive lower bound via rigorous intervals')
 S=add((4,x.constant(sum(ds))),(-1,HH));x.eq(S,x.constant(F(27,2)))
 residual=add((F(3,4),S),(-1,K),(-1,B));ge(residual,add((F(1,8),S)),'SAME original owner retains old quarter and booked K')
 # Independent exact integer inequalities used by the all-l source proof.
 x.ck(7<8,'B2>3/2 integer sign')
 x.ck(8**4<2*7**4,'-log r<1/4 for all l>=2')
 x.ck(F(2,2)+F(5,8)<=F(18,16)+F(1,2),'all-l linear owner bound at smallest l=2; slope9/16>1/2')
 out={'status':'PASS','source_claim':'A061-FIXED-PRODUCT-ONE-PREFIX-HALFBIT-OBSTRUCTION@1','dimension':11,'truth_table_size':len(t),'root_H':x.enc(HH),'root_K':x.enc(K),'root_I':str(sum(ds)),'ordinary_prediction':[str(v) for v in pre[2]],'ordinary_reference_only_mass':str(pre[6]),'B':x.enc(B),'B_interval':x.enciv(B),'full_mean_terminal_H':x.enc(add(*[(F(1,4),v) for v in termH])),'residual':x.enc(residual),'exact_assertions':x.COUNT,'seconds':time.perf_counter()-START,'independence':'Own previous-stage FWHT/physical-edge/normalized-transport helper; no A061 executable imported. Independent all-l derivation in AUDIT.md.'}
 x.ck(out['seconds']<55,'frozen audit runtime')
 (ROOT/'out/A061_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['independence']}))
if __name__=='__main__':main()
