"""Sharp one-query top-up: an algebraic corollary, not an FEI bound."""
import review_admission as a
from fractions import Fraction as F
import json,itertools,time
START=time.perf_counter();cases=0
for R0,R1 in itertools.product(range(3),repeat=2):
 for L0,L1 in itertools.product(range(R0+1),range(R1+1)):
  for q in (F(0),F(1,2),F(1)):
   parent=F(R0+R1,2)+q;g=[F(R0-L0),F(R1-L1)]
   delta=[F(L0-L1,2),F(L1-L0,2)]
   raw=[F(R0)-parent-delta[0],F(R1)-parent-delta[1]]
   charge=max(F(0),abs(g[0]-g[1])/2-q)
   a.ck(charge==max(F(0),*raw))
   a.ck(all(parent+charge+delta[b]>=[R0,R1][b] for b in (0,1)))
   if charge:a.ck(any(parent+delta[b]<[R0,R1][b] for b in (0,1)))
   cases+=1
a.ck(cases==108)
# Independently reconstruct the actual Boolean fail path, not an abstract account.
t=a.family(1);tag=(0,-1,-1,-1);childtag=(0,0,-1,-1)
H,I,ds,W=a.spectrum(t)
after=a.truth_restrict(t,tag);H3,I3,_,_=a.spectrum(after)
bad=a.truth_restrict(t,childtag);H2,I2,_,_=a.spectrum(bad)
a.ck(a.compare(a.sub(a.const(I3),H3),{})>0)
a.ck(H2==a.const(2) and I2==1)
globalroot=F(1,4);childfull=[F(1,2),F(0)];childlocal=[F(0),F(0)]
q=globalroot-sum(childfull)/2;g=childfull
charge=max(F(0),abs(g[0]-g[1])/2-q)
a.ck(q==0 and charge==F(1,4))
# Selector-only hull increments vanish; after admitting all parity bits, the
# next zero outcome has need1 and local increment+1/2.
credit_on_bad=globalroot+F(1,2)
bad_debit=a.sub(a.add(a.const(I2),a.const(credit_on_bad)),H2)
a.ck(bad_debit==a.const(F(-1,4)))
a.dump('COHERENCE_VALIDATION.json',dict(passed=True,rational_accounts=cases,checks=a.COUNT,log_primitive_checks=a.c.COUNT-64,runtime_seconds=time.perf_counter()-START,general_formula='extra=max(0,abs((R0-rho0)-(R1-rho1))/2-(Rparent-mean(R0,R1)))',Boolean_witness=dict(d=1,truth=t,integer_Walsh=W,root_I=I,root_H=a.pack(H),intermediate_S=a.pack(a.sub(a.const(I3),H3)),full_hull=globalroot,child_full_hulls=childfull,child_local_hulls=childlocal,global_query_surplus=q,minimum_extra_credit=charge,second_query_bad_child_credit=credit_on_bad,second_query_bad_child_debit=a.pack(bad_debit),bad_child_true_root_reach=F(1,4)),source_output_used_as_input=False,independent_external_review='PENDING_FOR_NEW_GENERAL_COROLLARY',full_FEI='OPEN'))
a.ck(time.perf_counter()-START<55)
print(json.dumps(dict(passed=True,rational_accounts=cases,checks=a.COUNT,runtime_seconds=time.perf_counter()-START,Boolean_negative_debit='-1/4')))
