from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import json,time,math
P=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def check(v):
 global checks
 assert v;checks+=1
 if time.monotonic()-start>60:raise TimeoutError('frozen 60 second cap')
def point_literal(width):return [-1 if x==0 else 1 for x in range(1<<(width+1))]
def inf(vals,i):return Q(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals))
def ledger(widths,direct=False):
 alphas=[Q(1,1<<s) for s in widths];delta=math.prod(alphas);S=sum(widths);reach=Q(1);debit=Q(0);rows=[]
 for j,(s,a) in enumerate(zip(widths,alphas)):
  future=math.prod(alphas[j+1:]);ri=2*a*(1-a)*future;debit+=reach*ri
  if direct:
   vals=point_literal(sum(widths[j+1:]));actual=inf(vals,sum(widths[j+1:]));check(actual==future);check(2*a*(1-a)*actual==ri)
  rows.append({'j':j+1,'width':s,'reach':str(reach),'source_terminal_z_influence':str(future),'exact_local_z_reserve':str(ri),'physical_debit':str(reach*ri)});reach*=a
 flat=2*delta*(1-delta);ratio=debit/delta;check(reach==delta);check(ratio==2*sum(1-a for a in alphas));check(ratio>=len(widths));check(flat<2*delta);check(debit>=flat)
 if len(widths)==2:check(debit-flat==2*delta*(1-alphas[0])*(1-alphas[1]))
 if all(s==1 for s in widths):check(ratio==len(widths));check(debit/((S+1)*delta)==Q(len(widths),len(widths)+1))
 if direct:
  vals=point_literal(S);check(inf(vals,S)==delta);check(sum(inf(vals,i) for i in range(S+1))==(S+1)*delta);check(Q(sum(v==-1 for v in vals),len(vals))==delta/2)
 return {'widths':list(widths),'n':S+1,'delta':str(delta),'D_z':str(debit),'T_z':str(delta),'D_z_over_T_z':str(ratio),'flat_R_z':str(flat),'D_z_over_I':str(debit/((S+1)*delta)),'nodes':rows}
symbolic=[w for L in range(1,5) for w in product((1,2,3),repeat=L)]+[(1,)*L for L in range(1,129)]
rows=[]
with (P/'out/FAMILY_ROWS.jsonl').open('w') as out:
 for widths in symbolic:
  row=ledger(widths);rows.append(row);out.write(json.dumps(row)+'\n');out.flush()
direct=[ledger(w,True) for L in range(1,4) for w in product((1,2),repeat=L)]
# Independent sign replay: different Taylor length/rounding, no audit imports.
SCALE=1<<104
def series(t):
 z=(t-1)/(t+1);p=z;zz=z*z;a=Q(0)
 for k in range(36):a+=2*p/(2*k+1);p*=zz
 return a,a+2*p/(73*(1-zz))
LN2=series(Q(2))
@lru_cache(None)
def logarithm(n):
 k=n.bit_length()-1
 if n==1<<k:return k*SCALE,k*SCALE
 a,b=series(Q(n,1<<k));lo=(k+a/LN2[1])*SCALE;hi=(k+b/LN2[0])*SCALE
 return lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)
source=json.loads((P/'out/REVIEW_RESULTS.json').read_text());replayed=0
for cert in source['certificates']:
 low=high=0
 for p,c in cert['terms']:
  p=int(p);c=int(c);a,b=logarithm(p);low+=c*(a if c>=0 else b);high+=c*(b if c>=0 else a)
 check(not cert['terms'] or low>0 or high<0);sign=0 if not cert['terms'] else (1 if low>0 else -1);check(sign==cert['sign']);replayed+=1
# Independent exact all-width scalar constants in A023 v3.
c=Q(81,56)
for s in range(1,6):
 a=Q(1,1<<s);b=2*(1-2*a)+2*c*(1-a)/s;check(b<Q(5,2));check(b+2*c<Q(11,2))
check(2+Q(12,5)*c<Q(11,2));check(2+c/3<Q(5,2))
result={'status':'PASS','symbolic_cases':len(rows),'direct_cases':len(direct),'max_symbolic_dimension':max(x['n'] for x in rows),'assertions':checks,'certificates_replayed':replayed,'seconds':time.monotonic()-start,'direct_rows':direct,'sample_rows':[x for x in rows if all(s==1 for s in x['widths']) and len(x['widths']) in (1,2,3,8,32,128)],'scope':'exact terminal-coordinate reserve renewal fails; flat compatible chain paid; no global influence or FEI refutation'}
(P/'out/FAMILY_RESULTS.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k not in ('direct_rows','sample_rows')}))
