import sympy as sp

# Exact symbolic verification for the codimension-one spectral-spike family.
e = sp.symbols("e", positive=True)
q = sp.symbols("q", positive=True)
tau = sp.symbols("tau", real=True)

v = sp.Matrix([sp.sqrt(q), sp.sqrt(1-q), 0, 0])
A = 2*sp.eye(4) + (tau-2)*(v*v.T)
a = sp.factor(A[0, 0])
b = A[1:, 0]
C = A[1:, 1:]
S = sp.simplify(C - b*b.T/a)

assert sp.simplify(a - (2*(1-q) + tau*q)) == 0
assert sp.simplify(S[0, 0] - 2*tau/a) == 0
assert sp.simplify(S[1, 1]-2) == 0
assert sp.simplify(S[2, 2]-2) == 0
assert all(sp.simplify(S[i, j]) == 0 for i in range(3) for j in range(3) if i != j)

# The complementary physical triple always has two exact eigenvalues 2.
B = A[1:, 1:]
assert (B - 2*sp.eye(3)).rank() <= 1

# Small-spike near-cancellation: q=1-epsilon, final pivot epsilon^2.
tau_small = sp.factor((e**2 - 2*e)/(1-e))
a_small = sp.simplify(2*e + tau_small*(1-e))
s_small = sp.factor(2*tau_small/a_small)
assert sp.simplify(a_small-e**2) == 0
assert sp.simplify(s_small + 2*(2-e)/(e*(1-e))) == 0

# Large-spike near-cancellation: q=epsilon, final pivot epsilon.
tau_large = sp.factor((e - 2*(1-e))/e)
a_large = sp.simplify(2*(1-e) + tau_large*e)
s_large = sp.factor(2*tau_large/a_large)
assert sp.simplify(a_large-e) == 0
assert sp.simplify(tau_large-(3-2/e)) == 0
assert sp.simplify(s_large-(6/e-4/e**2)) == 0

print("PASS")
print("generic_pivot =", a)
print("generic_Schur_diag =", [sp.factor(S[i, i]) for i in range(3)])
print("small_tau =", tau_small)
print("small_final_pivot =", a_small)
print("small_Schur_special =", s_small)
print("large_tau =", tau_large)
print("large_final_pivot =", a_large)
print("large_Schur_special =", s_large)
