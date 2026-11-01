
import sympy as sp
from itertools import combinations

H = sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
c = sp.Rational(3,4)
alpha = sp.sqrt(1-c)

def build(m):
    assert m % 4 == 0
    rows = [[sp.sqrt(c),0,0]]
    pats = [(1,1),(1,-1),(-1,1),(-1,-1)]
    for sig,tau in pats:
        for _ in range(m//4):
            rows.append([alpha/sp.sqrt(m), sp.Rational(sig,1)/sp.sqrt(m), sp.Rational(tau,1)/sp.sqrt(m)])
    R = sp.Matrix(rows)
    A = sp.simplify(R*H*R.T)
    return R,A

R,A = build(8)
assert sp.simplify(R.T*R) == sp.eye(3)
assert A.rank() == 3
lam = sp.symbols('lam')
cp = sp.factor(A.charpoly(lam).as_expr())
assert cp == lam**6*(lam - 1)**2*(lam + 1)
assert A[0,0] == 0
cross_energy = sp.simplify(sum(A[0,j]**2 for j in range(1,A.cols)))
assert cross_energy == c

det_bank_sum = sp.Rational(0)
max_det = sp.Rational(0)
max_weight = sp.Rational(0)
argmax = None
for I in combinations(range(A.rows),3):
    B = A.extract(I,I)
    d = abs(sp.simplify(B.det()))
    max_det = max(max_det,d)
    if 0 in I:
        det_bank_sum += d
    for p in range(3):
        a = abs(sp.simplify(B[p,p]))
        if a*d != 0:
            w = sp.simplify((a*d)**sp.Rational(1,4))
            if float(w) > float(max_weight):
                max_weight = w
                argmax=(I,p,a,d)

assert sp.simplify(det_bank_sum) == c
assert max_det == sp.Rational(3,64)
assert sp.simplify(max_weight) == sp.root(3,4)/4

Rb = sp.Matrix([
    [sp.sqrt(c),0,0],
    [alpha/2,sp.Rational(1,2),sp.Rational(1,2)],
    [alpha/2,sp.Rational(1,2),-sp.Rational(1,2)]
])
Bbank = sp.simplify(Rb*H*Rb.T)
assert sp.simplify(Bbank.det()) == -c/4
pivot = sp.simplify(Bbank[1,1])
assert pivot == sp.Rational(1,2)
prod = sp.simplify(abs(Bbank.det())*pivot)
assert prod == sp.Rational(3,32)

for m in [4,8,12,16]:
    Rm,Am = build(m)
    md = sp.Rational(0)
    mw = sp.Rational(0)
    for I in combinations(range(Am.rows),3):
        B = Am.extract(I,I)
        d = abs(sp.simplify(B.det()))
        md = max(md,d)
        for p in range(3):
            a = abs(sp.simplify(B[p,p]))
            if a*d:
                ww = sp.simplify((a*d)**sp.Rational(1,4))
                if float(ww)>float(mw):
                    mw=ww
    print("m",m,"max_abs_det",md,"max_partner_scale",mw, "numeric", float(mw))

K = sp.sqrt(sp.E)
uniform_bound = sp.N(16*K**sp.Rational(3,2), 15)
print("RtR", R.T*R)
print("charpoly",cp)
print("cross_energy",cross_energy)
print("heavy_triple_det_bank_sum",det_bank_sum)
print("m8_max_abs_principal_det",max_det)
print("m8_max_partner_scale",max_weight,"argmax",argmax)
print("bank_block",Bbank)
print("bank_det",Bbank.det(),"bank_pivot",pivot,"pivot_times_absdet",prod)
print("universal_density_bound_lt",uniform_bound)
print("QFORM_NULL_WALSH_BANK_CHECK_PASS")
