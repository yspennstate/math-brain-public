from pathlib import Path
from fractions import Fraction as Q
import json,time
import exact as e
import check as c
R=Path(__file__).resolve().parents[1]
spec={'helper_version':'prefix.py v1; exact.py P180','actual_Boolean_family':'m4 paired-bent exterior, one unqueried parity tag, product of128 actual AND2 factors on256 core bits','domain':'one specified constant-child spine, at most64 paid queries, one extra original-core-funded query; all complementary full stopping terminals','case_count':'at most65 query nodes and66 stopping terminals; fixed source dimension, factor compression only','symmetry':'Fourier product law, each factor table checked directly; no sampling or growing dimension','arithmetic':'Fraction and outward2^-180 logarithms; strict rational-interval admission tests; exact factor influence/entropy laws','memory_estimate_MB':30,'max_runtime_seconds':55,'automatic_dimension_escalation':False}
(R/'PREFIX_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8',newline='')
start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x;checks+=1
K,C,b=c.source();E=c.prof(K,C,Q(0));c0=Q(1,16);fee=2*c0;N=128;B0=Q(7);floor=Q(1,2);L0=e.add(c.rational(B0),e.neg(E))
g=(-1,1,1,1);ck(c.I(g)==1);ck(c.inf(g,0)==Q(1,2));ck(c.overlap(c.H(g),c.rational(2)));ck(c.overlap(c.D(g,0),c.rational(2)))
leaves=[];k=0;cash=L0
while k<64:
 admission=e.add(cash,e.neg(c.rational(fee+floor)))
 if admission[1]<0:break
 ck(admission[0]>0)
 cash=e.add(cash,e.neg(c.rational(fee)));k+=1
 # Complementary literal child: queried factors' entropy0, one literal I1.
 leaves.append({'weight':Q(1,1<<k),'depth':k,'coreH':2*(N-k),'coreI':Q(N-k+1),'extra':False})
 ck(cash[0]>=c.rational(floor)[1]);ck(Q(N-k+1)+Q(N-k)==2*Q(N-k+1)-1)
ck(0<k<64);ck(e.add(cash,e.neg(c.rational(fee+floor)))[1]<0)
ck(cash[0]>=c.rational(floor)[1])
# One extra query, past the ACTUAL predictable source-cash boundary.
pending=c0*(N-k);released=c0*Q(k,2)
left=e.add(c.rational(c.kap()[0]*(pending+released)),e.neg(c.rational(fee)));ck(left[0]>0)
for literal in (0,1):
 leaves.append({'weight':Q(1,1<<(k+1)),'depth':k+1,'coreH':2*(N-k-1),'coreI':Q(N-k-1+literal),'extra':True})
ck(sum(x['weight'] for x in leaves)==1)
term=(0,0);banks=(0,0);weighted_fees=Q(0)
rows=[]
for x in leaves:
 w=x['weight'];depth=x['depth'];term=e.add(term,e.times(e.add(E,c.rational(c0*x['coreH'])),w))
 if x['extra']:
  ext=cash;corebank=e.add(c.rational(c.kap()[0]*(pending+released)),e.neg(c.rational(fee)))
 else:
  ext=e.add(L0,e.neg(c.rational(fee*depth)))
  corebank=c.rational(c.kap()[0]*c0*(x['coreI']+Q(depth,2)))
 bank=e.add(ext,E,corebank);banks=e.add(banks,e.times(bank,w));ck(bank[0]>=c.rational(floor)[1])
 rows.append({'weight':str(w),'full_terminal_H':e.serial(e.add(E,c.rational(c0*x['coreH']))),'original_owner_remaining':e.serial(bank),'extra':x['extra']})
for j in range(k+1):weighted_fees+=Q(1,1<<j)*fee
rootH=e.add(E,c.rational(2*c0*N));rootbank=c.rational(B0+c.kap()[0]*c0*N)
ck(c.overlap(rootH,e.add(term,c.rational(weighted_fees))))
ck(c.overlap(rootbank,e.add(banks,c.rational(weighted_fees))))
ck(weighted_fees>fee)
out={'status':'PASS','checks':checks,'elapsed_s':time.perf_counter()-start,'paid_source_core_queries_on_spine':k,'source_admission_failed':True,'cash_at_failed_admission':e.serial(cash),'next_source_fee':str(fee),'original_core_pending_at_frontier_without_kappa':str(pending),'released_core_capacity_without_kappa':str(released),'extra_query_from_original_core':True,'all_full_terminals':rows,'full_terminal_mean':e.serial(term),'actual_total_reach_weighted_debit':str(weighted_fees),'first_actual_old_debit':str(fee),'initial_core_factors':N,'core_dimension':2*N}
ck(out['elapsed_s']<55);out['checks']=checks
(R/'out/CHECK_prefix.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='')
print(json.dumps({k:out[k] for k in ['status','checks','elapsed_s','paid_source_core_queries_on_spine','source_admission_failed','cash_at_failed_admission']}))
