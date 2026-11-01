# Exact finite certificate for R16 I0036 phase-Fourier/Perron obstruction.
# Integer/modular arithmetic only.

P = 97
g = 5
omega = pow(g, 2, P)  # order 48 because g has order 96

def mult_order(a, p):
    x = 1
    for n in range(1, p):
        x = (x * a) % p
        if x == 1:
            return n
    raise RuntimeError("no order")

assert mult_order(g, P) == 96
assert mult_order(omega, P) == 48

# Uniform phase profile annihilates every non-trivial Fourier mode.
for k in range(1, 48):
    s = sum(pow(omega, k*r, P) for r in range(48)) % P
    assert s == 0, (k, s)

# The trivial mode sees total mass 48.
s0 = sum(1 for _ in range(48)) % P
assert s0 == 48

# J is the 48x48 all-ones matrix. On a Fourier character v_k,
# J v_k = 0 for k != 0, and J v_0 = 48 v_0.
# We certify these identities over F_97 exactly.
for k in range(48):
    v = [pow(omega, k*r, P) for r in range(48)]
    total = sum(v) % P
    Jv = [total] * 48
    if k == 0:
        assert all(Jv[r] == (48 * v[r]) % P for r in range(48))
    else:
        assert all(x == 0 for x in Jv)

# Hence M_a = a J has identical non-trivial Fourier blocks (all zero)
# for every a, while its real Perron eigenvalue is 48a.
for a in (1, 7, 1000):
    row_sum = 48 * a
    assert row_sum > 0
    v0 = [1] * 48
    Mv0 = [a * sum(v0)] * 48
    assert Mv0 == [row_sum] * 48

# Stronger phase-profile obstruction: adding c to every coordinate changes
# only k=0, so all nontrivial Fourier data are unchanged while total mass
# grows by 48c.
Z = [r*r + 3*r + 5 for r in range(48)]
for c in (1, 13, 100):
    Zc = [z + c for z in Z]
    for k in range(1, 48):
        fk = sum(Z[r] * pow(omega, k*r, P) for r in range(48)) % P
        fkc = sum(Zc[r] * pow(omega, k*r, P) for r in range(48)) % P
        assert fk == fkc
    assert sum(Zc) - sum(Z) == 48*c

print("prime =", P)
print("primitive_96_root =", g)
print("primitive_48_root =", omega)
print("all 47 nontrivial Fourier sums of uniform profile vanish exactly")
print("all-ones matrix annihilates all nontrivial Fourier characters")
print("uniform phase shift preserves all nontrivial Fourier data and changes total mass by 48c")
print("ALL_EXACT_CHECKS_PASS")
