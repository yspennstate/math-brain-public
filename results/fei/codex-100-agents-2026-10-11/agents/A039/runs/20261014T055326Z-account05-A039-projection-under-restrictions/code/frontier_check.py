import mixed as M
from fractions import Fraction as F
import json,time
L=M.L;start=time.perf_counter()
data=json.loads((M.R/'out/MIXED_CHECK.json').read_text())
rows=[(r['core_code'],p) for r in data['results'] for p in r['policies']]
M.ck(len(data['results'])==128 and len(rows)==1152)
for _,p in rows:M.ck(F(p['D'][1])<F(-19,100))
maximum=max(rows,key=lambda row:F(row[1]['D'][1]));cond=max(rows,key=lambda row:F(row[1]['conditional_sigma'][0]))
M.ck(F(cond[1]['conditional_sigma'][0])>F(1,4))
parity=[]
for n in range(2,5):
 tab=[-1 if not (s&1) and s&2 else ((-1 if (s>>3).bit_count()%2 else 1) if s&1 and s&4 else 1) for s in range(1<<(n+3))]
 p,d,_,_,_=M.info(tab);Q,c=M.rootref(p,d);A=M.kl(p,Q)
 tabs,refs,E,O,rr=M.step(tab,Q,1);endtc=[];endS=[];beforetc=[];befores=[];rows2=[]
 for y in range(2):
  f=M.info(tabs[y]);beforetc.append(f[3]);befores.append(f[4]);p=f[0]
  ts,qs,e,o,r=M.step(tabs[y],refs[y],2)
  fused=[p[t]+p[t|4] for t in range(len(p)) if not t&4]
  M.ck(L.law(ts[0])==L.law(ts[1])==fused)
  M.ck((r==0) if n==2 else (r>0));rows2.append(r)
  # O_second is analytically zero since k=1/2 on every source and reference fiber.
  for t in ts:
   ff=M.info(t);endtc.append(ff[3]);endS.append(ff[4]);M.ck(ff[4][0]>0)
   M.ck(L.ent(ff[0])==L.ent(f[0]))
  M.ck(o[0]<=0<=o[1])
 D1=M.sub(M.plus(O,M.scale(F(1,2),M.sumiv(beforetc))),A)
 D2=M.sub(M.plus(O,M.scale(F(1,4),M.sumiv(endtc))),A)
 expected=M.sub(D1,L.hiv(F(1,4)))
 M.ck(D2[0]<=expected[1] and expected[0]<=D2[1])
 S2=M.scale(F(1,4),M.sumiv(endS));M.ck(M.sub(M.scale(F(1,8),S2),D2)[0]>0)
 parity.append({'n':n,'D_first':M.enc(D1),'D_end':M.enc(D2),'mean_final_surplus':M.enc(S2),'second_reference_only_rows':rows2})
result={'status':'EXACT_FRONTIER_CHECK_PASS','checks':M.checks,'runtime_seconds':time.perf_counter()-start,'max_D_witness':{'core':maximum[0],**maximum[1]},'positive_conditional_witness':{'core':cond[0],**cond[1]},'parity_two_query_bases':parity,'analytic_n_ge_128_lower_bound':'D_end>(n+1)/64-2>0'}
(M.R/'out/FRONTIER_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if 'witness' not in k and k!='parity_two_query_bases'}))
