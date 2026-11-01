from pathlib import Path
import sympy as S
c=S.symbols('c',real=True);I=S.I
L=S.Matrix([[S.Rational(1,4),I/4,c],[I/4,S.Rational(1,4),I/4],[c,I/4,S.Rational(1,4)]])
actual=(S.eye(3)+S.diag(I-1,-2,-I-1)*L).det()
assert S.expand(actual-(S.Rational(7,16)+c/2-c*c))==0
assert S.expand(L.det()-(S.Rational(3,64)-c/8-c*c/4))==0
print('Actual (i,-1,-i) determinant and occupation determinant checked exactly.')
Path('local_fusion_exact_check.log').write_text('SymPy exact check: u=(i,-1,-i), det(I+diag(u-1)L)=7/16+c/2-c^2; det L=3/64-c/8-c^2/4. Both polynomial differences vanish identically.\n',encoding='utf8')
