from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import json,sys,time
import check_rigidity as c
e=c.e;ROOT=Path(__file__).resolve().parents[1];MODE=sys.argv[1];START=time.perf_counter()
records=[]
for m in ([1] if MODE=='pilot' else [1,2]):
 f,hm,r=c.activation(m);k=len(hm).bit_length()-1
 g=f*4;vertex=1<<(k+1);c.ck(g[vertex]==1);g[vertex]=-1
 n=len(g).bit_length()-1
 c.ck(sum(x<0 for x in g)%2==1)
 w=c.fw(g);c.ck(all(x%4==2 for x in w));c.ck(all(w))
 row=c.evaluate(g,f'punctured_activation_m{m}')
 p=Q(1,1<<r);weight=Q(1,1<<(r+3));pd=[-1]+[1]*(len(hm)-1)
 _,hcore,icore=c.stats(hm);_,hpd,ipd=c.stats(pd)
 EH={};EI=Q(0)
 children=Counter(tuple(g[x*len(hm):(x+1)*len(hm)]) for x in range(len(g)//len(hm)))
 for child,cnt in children.items():
  _,H,I=c.stats(list(child));wt=Q(cnt,len(g)//len(hm))
  EH=e.add(EH,e.scale(H,wt));EI+=wt*I
 c.ck(EH==e.add(e.scale(hcore,p),e.scale(hpd,weight)))
 c.ck(EI==p*icore+weight*ipd)
 SA=e.scale(e.add(EH,{2:-2*EI}),-1);c.ck(e.iv(SA)[1]<0)
 _,H,I=c.stats(g);D=e.add(H,{2:-2*I});c.ck(e.iv(D)[0]>0)
 row.update({'all_essential':all(Q(sum(w[s]*w[s] for s in range(len(w)) if s>>i&1),len(w)**2)>0 for i in range(n)),'prime_certificate':'odd negative truth count excludes every nontrivial coordinate product','full_support_certificate':'all Walsh integers 2 mod4','vertex':vertex,'m':m,'r':r,'complete_child_reserve_interval':e.bits(SA),'root_D_K2_interval':e.bits(D),'terminal_H':e.enc(EH),'terminal_I':str(EI),'point_defect_child_weight':str(weight)})
 c.ck(row['all_essential'])
 (ROOT/'out'/f'{MODE}_PUNCTURE_m{m}.json').write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8')
 records.append(row)
out={'status':'PASS','helper_version':'A055-punctured-weak-refund-v1','mode':MODE,'roots':len(records),'assertions':c.CHECKS+e.N,'runtime_seconds':time.perf_counter()-START,'certificates':records}
(ROOT/'out'/f'{MODE.upper()}_PUNCTURE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='certificates'}))
