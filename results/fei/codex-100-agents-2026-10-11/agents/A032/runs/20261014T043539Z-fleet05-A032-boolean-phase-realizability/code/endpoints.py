import json,time,math
from fractions import Fraction as F
from audit import ROOT,log_interval,bound
start=time.monotonic();counts=[]
for ratio,fair in [(2,0),(4,0),(4,1),(4,2)]:
    n=1+fair;P=1<<n;minheight=None
    for signs in range(1<<P):
        W=[(ratio if not s&1 else 1)*(-1 if signs>>s&1 else 1) for s in range(P)]
        inverse=[sum(v*(-1 if (s&x).bit_count()%2 else 1) for s,v in enumerate(W)) for x in range(P)]
        gcd=math.gcd(*inverse);height=F(max(map(abs,inverse)),gcd);assert height>2
        minheight=height if minheight is None else min(height,minheight)
    counts.append({'primitive_ratio':ratio,'other_fair_coordinates':fair,'all_signs_checked':1<<P,'minimum_primitive_integer_height':str(minheight)})
# Actual sharp endpoint: point defect on two addresses and one data bit.
truth=[-1]+[1]*7;W=[sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(truth)) for s in range(8)]
weights=[sum(W[J+4*s]**2 for s in range(2)) for J in range(4)]
assert weights==[40,8,8,8]
assert sum(sum(truth[x]!=truth[x^(1<<j)] for x in range(8)) for j in [2])==2
# Inequality constants used in the all-dimensional analytic proof.
checks={'conditional_K_gt_51_20':[(2,F(29,20)),(5,F(5,2)),(3,F(-9,2))],
 'ratio2_joint_below_Kjoint':[(2,F(66,7)),(3,F(-41,7))],
 'ratio4_joint_below_Kjoint':[(2,F(454,53)),(3,F(-3)),(5,F(-68,53))],
 'Cstar_below_Kjoint':[(2,F(14,3)),(3,F(-3,2))],
 'Kall_below_7':[(2,F(13)),(5,F(-2)),(13,F(-2))]}
certificates=[]
for name,sig in checks.items():
    lo,hi=bound(sig);assert lo>0
    certificates.append({'comparison':name,'positive_lower_bound':str(lo)})
# Non-Boolean one-coordinate control remains in the spectral hypothesis.
# h2(1/256)/(1/256)>8 from its first entropy term; both constants below7.
assert F(121,64)<2 # source Gibbs c=5/2 logarithm bound: sqrt2>11/8
out={'status':'PASS','finite_low_dimension_phase_checks':counts,'actual_three_bit_truth':truth,'Walsh_integers':W,'address_mass_numerators_over64':weights,'I_Y':'1/4','sharp_conditional_entropy':'3/8+(5/8)h2(1/10)','constant_comparisons':certificates,'normalized_non_Boolean_control':'psi=(sqrt255+x)/16, one nonfair marginal1/256, H/I>8 but Kcond and Kall<7; inverse value at+1 exceeds1','seconds':time.monotonic()-start}
(ROOT/'out/endpoints.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='constant_comparisons'}))
