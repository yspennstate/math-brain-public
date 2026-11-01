from sympy import symbols, Rational, simplify, factor

n = symbols("n", integer=True, positive=True)
N = n - 1

sum_k = N*(N+1)/2
sum_k2 = N*(N+1)*(2*N+1)/6
den = n*(n-1)*(n-2)

p_hh = simplify((sum_k2 - sum_k)/den)
p_hl = simplify((N*sum_k - sum_k2)/den)

a,b,c,d = symbols("a b c d")
joint = Rational(1,3)*a*c + Rational(1,6)*(a*d+b*c) + Rational(1,3)*b*d
marginal_product = ((a+b)/2)*((c+d)/2)
wedge_defect = factor(joint - marginal_product)

p, lam = symbols("p lambda", real=True)
q = 1-p
axis_AA = simplify((p**2 + p*q + q**2)/3)
axis_defect = factor(axis_AA - Rational(1,4))

u = symbols("u", real=True)
m = p*(1-u) + q*u
Em = simplify(m.integrate((u,0,1)))
Varm = factor((m**2).integrate((u,0,1)) - Em**2)
out_var = factor(lam*Em + lam**2*Varm)

checks = {
    "P(H1=1,H2=1)": p_hh,
    "P(H1=1,H2=0)": p_hl,
    "wedge_defect": wedge_defect,
    "axis_AA_defect": axis_defect,
    "E_m": Em,
    "Var_m": Varm,
    "mixed_Poisson_outdegree_variance": out_var,
}

for name, value in checks.items():
    print(f"{name} = {value}")

assert p_hh == Rational(1,3)
assert p_hl == Rational(1,6)
assert simplify(wedge_defect - (a-b)*(c-d)/12) == 0
assert simplify(axis_defect - (2*p-1)**2/12) == 0
assert Em == Rational(1,2)
assert simplify(Varm - (2*p-1)**2/12) == 0
assert simplify(out_var - (lam/2 + lam**2*(2*p-1)**2/12)) == 0

print("ALL_EXACT_CHECKS_PASS = True")
