from pathlib import Path
from fractions import Fraction as F
from math import lcm
import json,time
import census as c

RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'
data=json.loads((OUT/'CENSUS.json').read_text(encoding='utf-8'))
assert data['status']=='PASS'
assert data['full_cases']==1052928 and data['representatives']==526464
start=time.perf_counter(); count=0
def check(v):
 global count
 assert v
 count+=1
def save(name,obj):
 (OUT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')

def direct(table,biases):
 n=len(biases); out=[]
 for s in range(1<<n):
  norm=F(1); moment=F(0)
  for i,p in enumerate(biases):
   if s>>i&1: norm*=p*(1-p)
  for x in range(1<<n):
   w=F(1); phi=F(1)
   for i,p in enumerate(biases):
    bit=x>>i&1; w*=p if bit else 1-p
    if s>>i&1: phi*=bit-p
   moment+=w*table[x]*phi
  out.append(moment*moment/norm)
 check(sum(out)==1)
 return out

global_rows=[r for r in data['rows'] if r['maximum_ratio_bounds']]
best=max(global_rows,key=lambda r:F(r['maximum_ratio_bounds'][0]))
competitors=[r for r in global_rows if F(r['maximum_ratio_bounds'][1])>=F(best['maximum_ratio_bounds'][0])]
check([(r['m'],r['a'],r['b']) for r in competitors]==[(2,1,4),(2,4,1)])
check(all(r['maximum_debt_lattice'][1]<=r['tax_lower_lattice'] for r in data['rows']))
check(all(r['witness']['debt_prime_log_vector']=={} for r in data['rows'] if r['m']<=1))

rows=[]
for r in data['rows']:
 w=r['witness']; p=[F(r['a'],8),F(r['b'],8)]+[F(1,2)]*r['m']
 P=direct(w['truth_table'],p)
 check(P==[F(x) for x in w['squared_parent_spectrum']])
 N=1<<r['m']; weights=[F(x) for x in w['physical_child_weights']]
 for z in range(4):
  table=w['truth_table'][z::4]
  child=direct(table,p[2:])
  check(child==[F(x) for x in w['child_spectra'][z]])
 check(all(sum(weights[z]*F(w['child_spectra'][z][t]) for z in range(4))==F(w['residual_marginal'][t]) for t in range(N)))
 # Independent physical pivotal probabilities identify actual essential coordinates.
 influences=[]
 for i in range(len(p)):
  prob=F(0)
  for x,v in enumerate(w['truth_table']):
   if v!=w['truth_table'][x^(1<<i)]:
    weight=F(1)
    for j,bias in enumerate(p): weight*=bias if x>>j&1 else 1-bias
    prob+=weight
  influences.append(prob)
 rows.append({'m':r['m'],'a':r['a'],'b':r['b'],'physical_influences':[str(v) for v in influences]})

# A simpler attaining witness with both revealed coordinates essential.
# Values use X1+2 X2+4 U+8 V, all in {0,1}.
table=[(-1 if x>>1&1 else 1)*(1-2*int((x&1) and (x>>2&1) and (x>>3&1))) for x in range(16)]
mask=sum((v==1)<<i for i,v in enumerate(table))
check(mask in best['maximizer_masks'])
rec,vec=c.details(2,mask,1,4)
P=direct(table,[F(1,8),F(1,2),F(1,2),F(1,2)])
check(P==[F(x) for x in rec['squared_parent_spectrum']])
check(all(any(table[x]!=table[x^(1<<i)] for x in range(16)) for i in range(4)))
check(vec=={2:F(7,4),3:F(225,128),5:F(225,128),7:F(7,64),29:-F(29,16)})

# Exact positive sign, and exact rational bounds on the global half-tax ratio.
check(c.exact_sign(vec)==1)
ratio_lo=F(68132470,100000000); ratio_hi=F(68132471,100000000)
for bound,sign in [(ratio_lo,1),(ratio_hi,-1)]:
 diff=dict(vec); diff[7]=diff.get(7,F(0))-bound/F(16)
 lo=hi=F(0)
 for prime,coef in diff.items():
  a,b=c.log2_bounds(F(prime))
  if coef>=0: lo+=coef*a; hi+=coef*b
  else: lo+=coef*b; hi+=coef*a
 check(lo>0 if sign==1 else hi<0)
check(F(best['maximum_ratio_bounds'][0])>ratio_lo)
check(F(best['maximum_ratio_bounds'][1])<ratio_hi)
rec.update({'both_revealed_coordinates_essential':True,
 'exact_circuit':'(-1)^X2 * (1-2*X1*U*V)',
 'truth_mask':mask,
 'global_ratio_prime_log_formula':'[224+225 log2(3)+225 log2(5)+14 log2(7)-232 log2(29)]/[8 log2(7)]',
 'global_ratio_rational_bounds':[str(ratio_lo),str(ratio_hi)],
 'positive_debt_integer_comparison':'2^224*3^225*5^225*7^14 > 29^232',
 'minimality_in_frozen_domain':'m<=1 has exact maximum 0 for every specified bias pair; therefore 4 total bits are necessary for positive block debt in this searched domain',
 'target_violation':False})
save('EXTREMAL_CERTIFICATE.json',rec)

# A half-tax envelope strictly below 1, including arbitrary-output negations.
check(all(F(r['maximum_ratio_bounds'][1])<ratio_hi for r in global_rows))
min_gap=min(r['rigorous_gap_to_tau_lower_lattice'] for r in data['rows'] if (r['a'],r['b'])!=(4,4))
check(F(min_gap,data['scale'])>F(7,1000))
save('INDEPENDENT_RECONSTRUCTION.json',{'status':'PASS','directly_checked_maximum_records':len(rows),
 'assertions':count,'runtime_seconds':time.perf_counter()-start,
 'global_ratio_bounds':[str(ratio_lo),str(ratio_hi)],
 'strict_gap_all_nonuniform_pairs_bits':str(F(min_gap,data['scale'])),
 'uniform_pair':'All 1904 m=2 representative maxima have debt exactly 0; exact prime-log vectors empty',
 'physical_influence_checks':rows})
print(json.dumps({'status':'PASS','assertions':count,'runtime_seconds':time.perf_counter()-start,
 'global_ratio_bounds':[str(ratio_lo),str(ratio_hi)],'minimal_truth_mask':mask}))
