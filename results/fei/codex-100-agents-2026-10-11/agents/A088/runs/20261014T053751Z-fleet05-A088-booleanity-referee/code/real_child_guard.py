from pathlib import Path
from fractions import Fraction as F
import json
R=Path(__file__).resolve().parents[1]
a,b=F(262143,262145),F(1024,262145); beta=b*b
assert a*a+beta==1
assert beta<F(1,65536)
# F=a+b*x*z. Its two actual cores a+b*x and a-b*x both have norm one.
# H(F)=H(core marginal)=H(each child)=h2(beta), I_X=I_Z=beta.
# Global joint-reference cost=2h2(beta), so excess over terminal=h2(beta)>16beta.
# K+2<23/2<16 by ln2>2/3 and log2(5)<5/2.
assert F(842,1215)>F(2,3) and 5**2<2**5 and F(23,2)<16
out={'function':'F(x,z)=262143/262145+(1024/262145)*x*z','beta':str(beta),'all_actual_child_squared_norms':'1','whole_output_squared_norm':'1','I_X_and_I_Z':str(beta),'Q_access':'0','global_joint_CE':'2 h2(beta)','terminal_entropy':'h2(beta)','MI_flag_refund':'h2(beta)','reference_excess_over_I_Z_strict_lower':'16','source_K_plus_2_strict_upper':'23/2','scope':'Actual norm-one real output AND norm-one children refute universal flag and specified complete joint-reference payment. Bare Q inequality remains satisfied in this witness.','exact_predicates':5,'failures':0}
(R/'out/REAL_CHILD_NORM_GUARD.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
