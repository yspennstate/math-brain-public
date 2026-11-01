from fractions import Fraction as F
from pathlib import Path
import json,time
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def check(b):
 global checks
 checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('internal pilot cutoff')
 if not b:raise AssertionError(checks)
def walsh(t):
 a=list(t);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):
    u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
  h*=2
 return [F(x,len(a)) for x in a]
def influences(t,n):
 return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(n)]
# Bits one represent physical positives; z is bit0, y1 bit1, y2 bit2.
core=[1 if x&1 and (x&2 or x&4) else -1 for x in range(8)]
coeff=walsh(core);p=[x*x for x in coeff];iv=influences(core,3)
check(coeff[0]==-F(1,4));check(iv==[F(3,4),F(1,4),F(1,4)])
check(p[7]==F(1,16));check(p[2]==p[4]==p[6]==F(1,16))
# Every nonempty Fourier set is covered by one gate unless both private bits occur.
labels=sum((p[s]*(2 if s&2 and s&4 else 1) for s in range(1,8)),F(0))
check(labels==F(17,16))
rank=sum((p[s]*((bool(s&2)+bool(s&4)) if not s&1 else 0) for s in range(1,8)),F(0))
check(rank==F(1,4))
subset_lower=p[7];r=10;actp=F(1,1<<r); actI=actp*(sum(iv)+r*(1-coeff[0]))
check(actI==F(55,4096));check(13<16)
L_upper=5*actp;S_upper=4*actI;R_upper=(F(6,5)*4+12)*actI
check(L_upper<labels);check(S_upper<subset_lower);check(R_upper<F(6,5)*rank)
depths=[]
for d in range(1,5):
 n=d+2;table=[]
 for u in range(1<<n):
  x=1 if u&1 else -1;y=1 if u&2 else -1; val=y
  for k in range(1,d+1):
   zk=1 if u&(1<<(k+1)) else -1
   val=val if x==1 else zk
  check(val==(y if x==1 else (1 if u&(1<<(d+1)) else -1)))
  table.append(val)
 spectrum=walsh(table);mass=[v*v for v in spectrum]
 check(sorted(z for z in mass if z)==[F(1,4)]*4)
 inf=influences(table,n)
 check(sum(inf)==F(3,2));check(inf[0]==inf[1]==inf[-1]==F(1,2))
 check(all(v==0 for v in inf[2:-1]))
 depths.append({'depth':d,'formal_positive_clauses':d+1,'formal_selector_read':d+1,
  'noncontradictory_clauses':2,'reduced_selector_read':2,'gate_probabilities':['1/4','1/4'],
  'feasible_lambda':['1/2','1/2'],'root_odds':['1/8','1/8'],'root_probabilities':['1/9','1/9'],
  'root_normalizer_exact':'2 log2(9/8)','root_vector_entropy_exact':'2 h2(1/9)',
  'attachment_label_entropy_selector':1,'attachment_label_entropy_data':0,
  'spectrum_nonzero_masses':['1/4']*4,'H_bits':2,'I':str(sum(inf)),
  'influence_vector':list(map(str,inf))})
result={'helper':'A013-lead-ledger-v1','status':'PASS','exact_assertions':checks,
 'elapsed_seconds':time.perf_counter()-start,'core_spectrum':list(map(str,coeff)),
 'restriction_obstruction':{'r':10,'child_L':str(labels),'parent_L_upper':str(L_upper),
  'child_S_lower':str(subset_lower),'parent_S_upper':str(S_upper),
  'child_rank_rarity_lower':str(F(6,5)*rank),'parent_rank_rarity_upper':str(R_upper),
  'parent_I':str(actI),'physical_restriction_probability':str(actp)},'shared_selector_depths':depths}
(RUN/'out/LEAD_LEDGER_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['shared_selector_depths','core_spectrum']},indent=2))
