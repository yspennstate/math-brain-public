import pathlib,json,math
from fractions import Fraction
R=pathlib.Path(__file__).resolve().parent
rows=[];count=0
for n in [1,2,4,8,16]:
 q=n/(n+1);r=2**(-1/q);g=1-2*r
 assert 0<r<.5 and abs(2*r**q-1)<1e-12
 for k in range(1,11):
  starts=[0.]
  for j in range(k):starts=[r*x for x in starts]+[1-r+r*x for x in starts]
  starts.sort();length=r**k
  gaps=[starts[j+1]-starts[j]-length for j in range(len(starts)-1)]
  assert min(gaps)>=g*r**(k-1)-1e-12
  count+=len(gaps)
 rows.append({'n':n,'q':q,'r':r,'cylinder_mass':2**(-10),'length_power_q':(r**10)**q,'upper_cover_cost_s_q_plus_point_one':(2*r**(q+.1))**10})
for n in range(1,100):
 assert Fraction(5,4)*Fraction(1,2)**(n+1)<Fraction(1,2)**n
assert all(Fraction(n,n+1)<1 for n in range(1,100))
result={'purpose':'Checks of the explicit deterministic counterexample, not LQG simulation','cantor_adjacent_gaps_checked':count,'rows':rows,'disjoint_component_interval_checks':99,'memory':'At most 1024 cylinder starts per iteration; far below 1 GB'}
(R/'band_numerical_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
claims=[
{'claim':'For each nonconstant finite subcritical geodesic, in each of the Euclidean and D_h metrics separately, the shrinking-band thickness spectrum F_m is upper semicontinuous and attains the full geodesic dimension on a nonempty compact maximizing set. Every neighbourhood of a maximizing thickness has full geodesic dimension.','status':'proved','proof_location':'SECOND_ATTEMPT.md H1','remaining_gap':'F_m is a regularized band spectrum, not the exact-level spectrum; no uniqueness or common maximizer for both metrics established.','checks':['Full finite-union and nested-interval proof','Uniform boundedness and Borel measurability of source-limsup thickness verified','Finite selection step in BandReduction.lean; formal run pending']},
{'claim':'Every Euclidean shrinking-band maximizer obeys |a|<=sqrt(4-2 dim_E P) and a<=Q-dim_E P/xi. At gamma=sqrt(8/3) it lies in [-sqrt(2),-1/sqrt(6)]. Metric shrinking-band maximizers lie strictly inside (-2,2).','status':'proved_special_case','proof_location':'SECOND_ATTEMPT.md H2-H3','remaining_gap':'No matching claim for any exact thickness level; bound uses subcritical hypotheses.','checks':['Band inclusion in annulus threshold sets','Reflected ambient limsup tail bound and positive Holder exponent','Formal Brownian feasibility run pending']},
{'claim':'There is a compact deterministic subset of R with a continuous injective labeling and unique full-dimensional shrinking-band maximizer, while every exact label level has dimension zero.','status':'counterexample','proof_location':'SECOND_ATTEMPT.md I','remaining_gap':'Counterexample to the band-to-fiber upgrade only; not a GFF or geodesic counterexample to D0051.','checks':['Explicit separated Cantor sets q_n=n/(n+1)','Full cylinder-cover upper and Bernoulli-measure lower dimension proofs','band_numerical_checks.json verifies finite gap and separation algebra']},
{'claim':'An atom at a in the thickness pushforward of a finite-s-energy Euclidean Frostman measure on P implies dim_E(P intersect T_h^a)>=s. An atom in the normalized D_h-arclength thickness law implies dim_D(P intersect T_h^a)=1.','status':'proved','proof_location':'SECOND_ATTEMPT.md J','remaining_gap':'Neither occupation atoms nor a common atom for near-optimal Euclidean Frostman measures have been established; this is a sufficient criterion only.','checks':['Restriction and normalization preserve finite energy when the fiber has positive mass','Full potential-bound proof of the Hausdorff lower bound','Metric isometry with the length-parameter interval']}
]
with (R/'CLAIMS.jsonl').open('a',encoding='utf8') as f:
 for x in claims:x['problem_id']='D0051';f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('Saved four second-attempt claims.')
