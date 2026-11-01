from pathlib import Path
from fractions import Fraction as F
import json
r=Path(__file__).resolve().parents[1]
a,b=F(1023,1025),F(64,1025)
p=b*b
assert a*a+p==1 and p<F(1,256)
# The normalized real seed a+b*x has U=0, I=p and H=h2(p).
# H/I >= log2(1/p)>8.  ln2>2/3 implies K=4+2/ln2<7.
lower_ln2=F(842,1215)
assert lower_ln2>F(2,3) and 4+2/lower_ln2<7
out={'seed_fourier':[str(a),str(b)],'squared_norm':'1','U':'0','I':str(p),'H_over_I_strict_lower_bound':8,'source_k1_r2_K_strict_upper_bound':7,'controls':2,'edit_set':'empty','child_norms':'all 1','scope':'Refutes normalized-real extension of the U-leaf entropy corollary; Boolean theorem unaffected','assertions':4,'failures':0}
(r/'out/REAL_TERMINAL_GUARD.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
