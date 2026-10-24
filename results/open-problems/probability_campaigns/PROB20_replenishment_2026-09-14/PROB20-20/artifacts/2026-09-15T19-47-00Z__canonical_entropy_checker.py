import itertools, math

pi = [0.4, 0.3, 0.2, 0.1]  # support {0,1,2,3}
n = 5
m = 7
U = 3


def mean_at_t(t):
    ws = [pi[k] * math.exp(t*k) for k in range(U+1)]
    z = sum(ws)
    return sum(k*ws[k] for k in range(U+1))/z


lo, hi = -10.0, 10.0
for _ in range(200):
    mid = (lo + hi) / 2
    if mean_at_t(mid) < m/n:
        lo = mid
    else:
        hi = mid

t = (lo + hi) / 2
ws = [pi[k] * math.exp(t*k) for k in range(U+1)]
Z = sum(ws)
pcan = [w/Z for w in ws]

states = []
raw = []
for x in itertools.product(range(U+1), repeat=n):
    if sum(x) == m:
        p = 1.0
        for y in x:
            p *= pi[y]
        states.append(x)
        raw.append(p)

P_A = sum(raw)
Q = [p/P_A for p in raw]

a_can = 0.0
for x in states:
    p = 1.0
    for y in x:
        p *= pcan[y]
    a_can += p

lam = m/n
I = lam*t - math.log(Z)
factorized = math.exp(-n*I) * a_can


def kl_vec(a, b):
    return sum(x*math.log(x/y) for x, y in zip(a, b) if x > 0)


mu = [0.0]*(U+1)
for x, q in zip(states, Q):
    mu[x[0]] += q

D_mu = kl_vec(mu, pcan)
TC = 0.0
for x, q in zip(states, Q):
    prod_mu = 1.0
    for y in x:
        prod_mu *= mu[y]
    TC += q*math.log(q/prod_mu)

ell = -math.log(a_can)

print("canonical tilt t =", repr(t))
print("target mean =", lam)
print("canonical mean =", sum(k*pcan[k] for k in range(U+1)))
print("original capped-sum probability =", P_A)
print("tilt factorization RHS =", factorized)
print("factorization abs error =", abs(P_A-factorized))
print("local cost -log(a) =", ell)
print("TC + n D(mu||p_can) =", TC+n*D_mu)
print("Pythagorean abs error =", abs(ell-(TC+n*D_mu)))

assert abs(P_A-factorized) < 1e-12
assert abs(ell-(TC+n*D_mu)) < 1e-12

for r in range(1, n):
    marg = {}
    for x, q in zip(states, Q):
        key = x[:r]
        marg[key] = marg.get(key, 0.0) + q
    Dr = 0.0
    for key, q in marg.items():
        pp = 1.0
        for y in key:
            pp *= pcan[y]
        Dr += q*math.log(q/pp)
    bound = (r/n)*ell
    print(f"r={r}: D_r={Dr:.15g}, (r/n)ell={bound:.15g}, margin={bound-Dr:.15g}")
    assert Dr <= bound + 1e-12

print("ALL CHECKS PASSED")
