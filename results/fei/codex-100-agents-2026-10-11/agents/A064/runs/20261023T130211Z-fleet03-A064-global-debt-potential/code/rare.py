from pathlib import Path
import json,time
import exact as x
from check import make,add,ge
F=x.F
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()

def main():
 h=x.core(2);G=x.carrier((1,)*len(h));H=x.carrier(h)
 f=tuple((H if s&1 else G)[s>>1] for s in range(2*len(G)));base=make(f,f)
 K=x.constant(F(5,2));HH=x.constant(F(17,2));B=add((1,x.constant(3)),(-F(1,2),x.log(F(7))))
 O=add((1,B),(-1,x.constant(1)));S=x.constant(F(27,2));records=[]
 for k in (1,2):
  current=base*(1<<k);Q=x.product(x.stats(current)[1]);initial=add((1,K),(F(1,1<<k),B))
  x.eq(x.kl(x.stats(current)[0],Q),K,'dummy extension initial KL')
  x.eq(x.stats(current)[2],HH,'dummy extension full entropy')
  for j in range(k):
   out=x.transport(current,11,Q)
   x.ck(out[2]==[F(1,2),F(1,2)],'actual dummy prediction fair')
   x.eq(out[3],{});x.eq(out[5],{})
   for b in (0,1):
    x.ck(out[0][b]==base*(1<<(k-j-1)),'actual dummy child source')
    x.ck(out[1][b]==x.product(x.stats(out[0][b])[1]),'FULL dummy reference unchanged')
    x.eq(out[4][b],K)
   next_potential=add((1,K),(F(1,1<<(k-j-1)),B))
   parent_potential=add((1,K),(F(1,1<<(k-j)),B))
   x.eq(parent_potential,add((F(1,2),next_potential),(F(1,2),K)),'rare-branch exact potential allocation')
   current,Q=out[0][0],out[1][0]
  eps=F(1,1<<k)
  meanK=add((1,K),(1,x.constant(eps)));meanO=add((eps,O));meanH=add((1,HH),(-1,x.constant(4*eps)))
  x.eq(add((1,meanK),(1,meanO)),initial,'full terminal KL plus cost equality')
  ge(add((1,K),(1,B)),initial,'potential grows on rare all-zero branch')
  ge(x.constant(6),initial,'G terminal potential exceeds initial value')
  ge(add((F(3,4),S),(-1,initial)),add((F(1,8),S)),'old quarter remains in SAME owner')
  records.append({'dummy_bits':k,'rare_activation_probability':str(eps),'G_terminal_probability':str(eps/2),'root_potential':x.enc(initial),'active_preselector_potential':x.enc(add((1,K),(1,B))),'G_terminal_K':6,'mean_terminal_K':x.enc(meanK),'mean_terminal_H':x.enc(meanH),'mean_outcome_KL':x.enc(meanO)})
 x.ck(time.perf_counter()-START<55,'frozen rare check runtime')
 out={'status':'PASS','actual_dummy_counts':[1,2],'maximum_actual_dimension':13,'all_k_extension':'proved analytically in PROOF.md section4; no dimension escalation','exact_assertions':x.COUNT,'seconds':time.perf_counter()-START,'records':records}
 (ROOT/'out/RARE_BRANCH.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'}))
if __name__=='__main__':main()
