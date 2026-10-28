from pathlib import Path
from fractions import Fraction as F
import sys,json,time
import arith as A
R=Path(__file__).resolve().parents[1];START=time.perf_counter();ROWS=[];COUNTS={'pairs':0,'pivot_states':0,'data_queries':0,'halfbit_failures':0}
def add(*x):return A.plus(*x)
def prod(ds):
 q=[]
 for s in range(1<<len(ds)):
  a=F(1)
  for j,d in enumerate(ds):a*=d if s>>j&1 else 1-d
  q.append(a)
 return tuple(q)
def truth(n,c):return tuple(-1 if c>>x&1 else 1 for x in range(1<<n))
def source(g,h):return tuple((h[x>>2]*(-1 if x&1 else 1)) if x>>1&1 else g[x>>2] for x in range(4*len(g)))
def pivot(t,Q):
 COUNTS['pivot_states']+=1
 cs,Qs,r,O,E,Ks,z=A.transport(t,1,Q);Js=[];positives=[]
 for b in [0,1]:
  p,ds,H,M,TC=A.stats(cs[b]);J=add((1,TC),(-1,Ks[b]));Js.append(J);positives.append(A.positive(J))
 B=A.positive(add((F(1,2),positives[0]),(F(1,2),positives[1]),(-1,E)))
 for b in [0,1]:A.nonneg(add((1,Ks[b]),(1,positives[b]),(-1,A.stats(cs[b])[4])),'full pivot terminal KL paid')
 K=A.kl(A.stats(t)[0],Q);P=add((1,K),(1,B));Pb=[add((1,Ks[b]),(1,positives[b])) for b in [0,1]]
 A.nonneg(add((1,P),(F(-1,2),Pb[0]),(F(-1,2),Pb[1]),(-1,O)),'all full pivot terminal liabilities and actual O')
 return B,{'r':[str(x) for x in r],'E':A.value(E),'O':A.value(O),'K_children':[A.value(x) for x in Ks],'J_children':[A.value(x) for x in Js],'B':A.value(B),'reference_only_erased_mass':str(z)}
def run(n):
 count=0;fails=0;best={};witness=None;first=None
 for gc in range(0,1<<(1<<n),2):
  g=truth(n,gc)
  for hc in range(0,1<<(1<<n),2):
   h=truth(n,hc);t=source(g,h);p,ds,H,M,TC=A.stats(t);Q=prod(ds)
   A.ck(ds[0]==ds[1]==F(1,2),'actual fresh u/v influence');A.ck(A.kl(p,Q)==TC,'original actual marginal product')
   B0,rec0=pivot(t,Q);A.nonneg(add((1,A.const(F(1,2))),(-1,B0)),'A064 original halfbit bound')
   cs,Qs,r,O,E,Ks,z=A.transport(t,2,Q);COUNTS['data_queries']+=1;Bs=[];recs=[]
   for a in [0,1]:
    B,rec=pivot(cs[a],Qs[a]);Bs.append(B);recs.append(rec)
   after=A.positive(add((F(1,2),Bs[0]),(F(1,2),Bs[1]),(-1,E)))
   total=A.maximum(B0,after);excess=add((1,total),(-1,A.const(F(1,2))))
   if excess and A.interval(excess)[0]>0:fails+=1;COUNTS['halfbit_failures']+=1
   if A.maximum(best,total)!=best:
    best=total;witness={'n':n,'g_code':gc,'h_code':hc,'g':list(g),'h':list(h),'root_H':A.value(H),'root_M':A.value(M),'root_K':A.value(TC),'root_I':str(sum(ds)),
     'root_original_Q':[str(x) for x in Q],'B_original':A.value(B0),'B_after_data':A.value(after),'B_total':A.value(total),'halfbit_excess':A.value(excess),
     'data_r':[str(x) for x in r],'data_O':A.value(O),'data_E':A.value(E),'data_K_children':[A.value(x) for x in Ks],
     'root_pivot':rec0,'conditional_pivots':recs,'all_full_terminal_H_retained':True}
   if first is None and excess and A.interval(excess)[0]>0:first={'n':n,'g_code':gc,'h_code':hc,'B_total':A.value(total),'excess':A.value(excess)}
   count+=1;COUNTS['pairs']+=1
 A.ck(count==(1<<(2*((1<<n)-1))),'exact normalized pair census')
 return {'n':n,'pairs':count,'halfbit_failures':fails,'max_pending':A.value(best),'max_witness':witness,'first_failure':first}
def main():
 pilot='pilot' in sys.argv
 for n in ([2] if pilot else [2,3]):ROWS.append(run(n))
 expected=64 if pilot else 16448
 A.ck(COUNTS['pairs']==expected and COUNTS['pivot_states']==3*expected and COUNTS['data_queries']==expected,'frozen all-pair coverage')
 seconds=time.perf_counter()-START;A.ck(seconds<(55 if pilot else 360),'frozen runtime')
 out={'status':'PASS','exact_assertions':A.COUNT,'counts':COUNTS,'seconds':seconds,'rows':ROWS,'domain_complete':True,'full_fei':'OPEN'}
 (R/'out').mkdir(exist_ok=True);(R/'out'/('PILOT.json' if pilot else 'MAIN.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in out.items() if k!='rows'}));print(json.dumps([{'n':x['n'],'failures':x['halfbit_failures'],'max_pending':x['max_pending'],'first_failure':x['first_failure'],'max_codes':None if x['max_witness'] is None else [x['max_witness']['g_code'],x['max_witness']['h_code']]} for x in ROWS]))
if __name__=='__main__':main()
