from fractions import Fraction as F
from pathlib import Path
import json

RUN=Path(__file__).resolve().parents[1]
a0=F(127,128)
delta0=F(1,1<<14)
growth=((F(14)+F(37,10))*(1-F(1,1<<28))-4)*a0*a0-F(7)-F(9,4)-4
checks={
    'data_tail_excess_over_delta_gt_one_fifth':growth>F(1,5),
    'linear_tail_slope_positive':(1-F(1,1<<28))*a0*a0-F(1,2)>0,
    'a2_over_a2_plus_m2_gt_27_over_28':a0*a0/(a0*a0+F(1,128)**2)>F(27,28),
    'control_tail_correction_lt_delta_over_100':delta0*(4*14+F(9,2))<F(1,100),
    'all_k_control_correction_at_4_eq_41_over_512':F(1,256)*(16+F(9,2))==F(41,512),
    'selector_lower_at_6_exceeds_uniform_control_bound':(1-F(1,64))*5>4+F(41,512),
    'B_data_excess_constant_at_6_gt_8_over_25':((1-F(1,4096))*7-2)*F(49,64)-F(7,2)>F(8,25),
    'B_data_tail_after_division_gt_3_over_5':F(8,25)/F(33,64)>F(3,5),
    'B_control_tail_delta_factor_at_6_eq_7_over_16':F(28,64)==F(7,16),
    'B_selector_lower_at_4_gt_uniform_control_upper':F(45,16)>2+F(20,256)
}
assert all(checks.values()),checks
result=dict(checks=checks,assertions=len(checks),failures=0,tail_excess_rational=str(growth),scope='Rational anchors only; monotonicity and scalar logarithm inequalities are proved in REPORT.md')
(RUN/'out'/'TAIL_ANCHORS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
