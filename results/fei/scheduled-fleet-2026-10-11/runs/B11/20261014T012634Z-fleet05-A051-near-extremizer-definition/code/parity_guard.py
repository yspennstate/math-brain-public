from fractions import Fraction as Q
from pathlib import Path
import json
import independent_arithmetic as a
ROOT=Path(__file__).resolve().parent.parent
t=tuple(((z&1)^((z>>1)&1))*((z>>2)&1) for z in range(8))
coeff=a.direct_coeffs(t)
single=[]
for i in (0,1):
    ci=Q(0)
    for s in range(8):
        if s>>i&1:continue
        u,v=coeff[s],coeff[s|(1<<i)];q=u*u+v*v
        if q:ci+=4*u*u*v*v/q
    single.append(ci)
C=Q(0);IA=Q(0)
for s in (0,4):
    aa,bb,cc,dd=[coeff[s|u] for u in range(4)];q=aa*aa+bb*bb+cc*cc+dd*dd
    if q:C+=4*((aa*bb+cc*dd)**2+(aa*cc+bb*dd)**2+(aa*dd+bb*cc)**2)/q
    IA+=bb*bb+cc*cc+2*dd*dd
assert single==[0,0] and C==1 and IA==1
out={'truth_table':list(t),'fourier_coefficients':[str(v) for v in coeff], 'C_x1':str(single[0]),'C_x2':str(single[1]),'C_pair':str(C),'I_pair':str(IA), 'status':'EXACT_UNCONDITIONAL_COMPARISON_REFUTATION; NOT_DIMENSION_MINIMAL'}
(ROOT/'out/PARITY_GUARD.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
