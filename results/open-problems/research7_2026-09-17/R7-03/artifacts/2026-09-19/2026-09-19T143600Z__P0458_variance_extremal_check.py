from fractions import Fraction as F
from math import factorial


def add(a, b, s=F(1)):
    c = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += s * x
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c


def integ(a):
    return [F(0)] + [a[i] / F(i + 1) for i in range(len(a))]


def int01(a):
    return sum((x / F(i + 1) for i, x in enumerate(a)), F(0))


def down(a, d):
    assert all(x == 0 for x in a[:d])
    return a[d:]


def beta(a, b):
    return F(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))


def beta_pdf(a, b):
    from math import comb
    z = beta(a, b)
    c = [F(0)] * (a + b - 1)
    for j in range(b):
        c[a - 1 + j] = F(((-1) ** j) * comb(b - 1, j), 1) / z
    return c


def exact_var(n, k):
    # Exact polynomial implementation of the finite-n variance formula proved
    # in the preceding R7-03 run.  Valid for 1 <= k <= n-2.
    r = n - 1 - k
    ft = beta_pdf(k, r)
    cdf = integ(ft)
    icdf = integ(cdf)
    Q = down(icdf, 1)

    J1 = add([F(0)] + cdf, icdf, F(-1))
    cdf2 = mul(cdf, cdf)
    J2 = add(add([F(0)] + cdf2, mul(cdf, icdf), F(-2)), integ(cdf2))
    bnum = add(J2, mul(J1, J1), F(-1))
    b = [x / F((n - 2) ** 2) for x in down(bnum, 2)]

    fx = beta_pdf(k + 1, r)
    EQ = int01(mul(Q, fx))
    EQ2 = int01(mul(mul(Q, Q), fx))
    Eb = int01(mul(b, fx))
    delta = F(k) * EQ
    return delta - delta * delta + F(k * (k - 1)) * (EQ2 + Eb)


vals = {}
for k in range(1, 7):
    vals[k] = F(0) if k == 6 else exact_var(7, k)
    print(f"Var_D(7,{k})={vals[k]}")

m = max(vals, key=vals.get)
print(f"argmax={m}")
print(f"balanced_k=3 variance={vals[3]}")
print(f"k=4 variance={vals[4]}")
print(f"difference={vals[4] - vals[3]}")

assert m == 4
assert vals[4] - vals[3] == F(49669, 3468465)
print("BALANCED_NOT_MAX_CERTIFICATE=PASS")
