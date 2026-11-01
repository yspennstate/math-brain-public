import json
from pathlib import Path
from fractions import Fraction as Q
R=Path(__file__).resolve().parents[1]
tests={
 'N4_norm_base':5**4>2*4**4,
 'N3_m1_exclusion':5**3>4*2**4,
 'N2_m0_exclusion':5**2>4*2**2,
 'primitive_pair_type_bound':5*7>32,
 'Kcond_lower_log5':5**10>2**23,
 'Kcond_upper_log3':3**5<2**8,
 'quarter_Gibbs_comparison':128>121,
 'Kall_less_than7':65**2<2*64**2,
 'N3_signed_convolution_rejection':96%27!=0,
 'exception_conditional_symbolic_b_coefficient':Q(5,8)==Q(5,2)*Q(1,4),
 'exception_conditional_symbolic_constant':Q(3,8)==Q(3,2)*Q(1,4),
 'exception_Q_price':Q(5,8)==Q(5,2)*Q(1,4),
 'witness_H_entropy':2*Q(1,4)*2+8*Q(1,16)*4==3,
 'witness_I_energy':Q(1,2)+Q(1,2)*Q(1,2)+Q(1,2)*Q(3,2)==Q(3,2),
 'witness_R_sqrt_sum':2*Q(1,2)+8*Q(1,4)==3
}
assert all(tests.values())
out={'status':'PASS','assertions':len(tests),'tests':tests,
 'arithmetic':'integers and Fractions; transcendental comparisons reduced analytically to listed integer inequalities'}
(R/'out'/'scalar_validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
