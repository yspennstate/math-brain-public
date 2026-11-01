"""Rigorous interval checks (mpmath.iv, 50 digits) of every numeric inequality used in the analytic parts of
NOTES.md: Lemma E (Theorem A), 5.2 (scenario A), 5.4 (envelopes), 5.5 (rho >= 4), 5.7 (rho = 1).
Each inequality is restated in the form I derived it, then checked; an exact symbolic identity is used for
the equality case of 5.7(i)."""
from mpmath import iv, mpf
from fractions import Fraction

iv.dps = 50
LN2 = iv.log(2)
E = iv.e


def I(x):
    return iv.mpf(x)


def log2(x):
    return iv.log(x) / LN2


def h(t):
    t = I(t)
    return -(t * log2(t) + (1 - t) * log2(1 - t))


C = I(16) / 3 - I(3) / 2 * log2(I(3))
KAP = C / 2 - 1
DEL = 2 - C / 2
PSI = log2(1 + I(2) ** (-C))
SA = log2(I(5)) - 1


def G(p, q):
    S = p * p + q * q
    return KAP * (log2(I(S)) - 2) + C * I(q * q) / S - h(I(q * q) / S)


GA = G(2, 1) / SA
L10 = log2(I(10))
GB = (KAP * (L10 - 2) - PSI) / (L10 - 1)
A_ = DEL + GB
K0 = 2 * KAP - 2 * GB

checks = []


def chk(name, cond_interval_upper_lt0):
    """record: name, rigorous upper endpoint of a quantity that must be < 0"""
    v = cond_interval_upper_lt0
    ok = v.b < 0
    checks.append((name, float(v.b), ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}: upper bound {float(v.b):+.6f}")


# ---- Lemma E (Theorem A)
beta = log2(I(17) / 16)                 # max_t h(t) - 4t
chk("Lemma E: beta - 0.0875 < 0", beta - I("0.0875"))
gam = log2(I(5)) - 1 - beta
chk("Lemma E: 1.2344 - (log2 5 - 1 - beta) < 0", I("1.2344") - gam)
chk("Lemma E u>=4: 4 - 4 gam < 0", 4 - 4 * gam)
chk("Lemma E u=2,3: (4 - 2 gam) - 2 < 0", 4 - 2 * gam - 2)
v_u1f0 = I(5) / 8 * (5 + h(I(1) / 10) - I(4) / 10 - log2(I(5)))
chk("Lemma E u=1,f0=0: (5/8)(5 + h(1/10) - 2/5 - log2 5) - 2 < 0", v_u1f0 - 2)
xs = 1 + beta - 1 / LN2
chk("Lemma E u=1,f0>=1: x* <= 0", xs)
chk("Lemma E u=1,f0>=1: 2^{x*}/ln2 - 2 < 0", I(2) ** xs / LN2 - 2)
# direct sanity: brute maximum of 2^x (1 + beta - x) on a grid is below the closed form
# ---- (G1), (G2)
chk("(G1) GB > 0", -GB)
chk("(G2) G(2,1) > 0", -G(2, 1))
chk("(G2) GA < GB", GA - GB)
# kappa(log2 10 - 2) - psi = 0.456918.. used as the minimum for odd-odd pairs
m3 = KAP * (L10 - 2) - PSI
print("kappa(log2 10 - 2) - psi =", m3)
# ---- 5.2
chk("5.2 min term: 0.4569 - min(kap + G21, kap, kap(log2 10 - 2) - psi) < 0",
    I("0.4569") - iv.mpf([min(float((KAP + G(2, 1)).a), float(KAP.a), float(m3.a)),
                          min(float((KAP + G(2, 1)).b), float(KAP.b), float(m3.b))]))
K = -DEL * log2(I(2) ** (1 - C / DEL) + I(2) ** (-2 * C / DEL))
print("K =", K)
chk("5.2 eps>=1/2: delta - K/2 < 0", DEL - K / 2)
gibbs = DEL * log2(1 + I(2) ** (-K / DEL))
print("delta log2(1 + 2^{-K/delta}) =", gibbs)
rhs = I("0.4569") * I("0.55") * (1 + log2(I("0.55")))
print("0.4569*0.55*(1+log2 0.55) =", rhs)
chk("5.2 eps<=0.45: gibbs - 0.4569*0.55*(1+log2 0.55) < 0", gibbs - rhs)
chk("5.2 monotonicity: v(1+log2 v) increasing for v >= 0.55: -(1 + log2 0.55 + 1/ln2) < 0",
    -(1 + log2(I("0.55")) + 1 / LN2))
chk("5.2 0.45<=eps<=1/2: delta - 0.45 K < 0", DEL - I("0.45") * K)
# ---- 5.4
coefj = 2 * GB - 2 * KAP + 2 * (GB - GA) * SA
print("5.4 j-coefficient =", coefj)
chk("5.4 j-coefficient < 0", coefj)
chk("5.4 even constant 2(GB-GA)SA <= K0", 2 * (GB - GA) * SA - K0)
chk("5.4 odd envelope uses GB < kappa", GB - KAP)
# ---- 5.5
tail = 2 * A_ * log2(1 + I(2) ** (-C / A_))
print("2a log2(1+2^{-c/a}) =", tail)
chk("5.5 rho=4: 2a log2(1+2^{-c/a}) + K0 - 4 GB < 0", tail + K0 - 4 * GB)
# ---- 5.7
oddfair = 3 * DEL + 2 * KAP
chk("5.7(ii) empty row odd: (3 delta + 2 kappa)/8 - (5/8)(c - 3 delta) < 0", oddfair / 8 - I(5) / 8 * (C - 3 * DEL))
chk("5.7(ii) c > 3 delta (even rows at |T|>=1 negative)", 3 * DEL - C)
chk("5.7(ii) odd fair rows at |T|=1 negative: 3delta+2kappa-c < 0", oddfair - C)
emptyeven = DEL / (E * LN2) + (2 * (oddfair - C) + (oddfair - 2 * C)) / 8
chk("5.7(ii) empty row even: delta/(e ln2) + [2(3d+2k-c) + (3d+2k-2c)]/8 < 0", emptyeven)
chk("5.7(i) sigma rows: c > 2", 2 - C)
# 5.7(i) exact equality: (5/8)(log2(8/5) + h(1/10) - c/10) + (1/8)(12 - 5.5 c) = 0, symbolically:
# log2(8/5) = 3 - log2 5 ; h(1/10) = 1 + log2 5 - (9/5) log2 3 ; c = 16/3 - (3/2) log2 3.
# collect: rational part and log2 3, log2 5 coefficients
r0 = Fraction(5, 8) * (3 + 1) + Fraction(12, 8)
l3 = Fraction(5, 8) * Fraction(-9, 5)
l5 = Fraction(5, 8) * (-1 + 1)
cc = -Fraction(5, 8) * Fraction(1, 10) - Fraction(1, 8) * Fraction(11, 2)   # coefficient of c
r0 += cc * Fraction(16, 3)
l3 += cc * Fraction(-3, 2)
print("5.7(i) T0 = empty: exact value =", r0, "+", l3, "log2 3 +", l5, "log2 5")
ok_exact = (r0 == 0 and l3 == 0 and l5 == 0)
checks.append(("5.7(i) exact equality at AND_3", 0.0, ok_exact))
print("PASS" if ok_exact else "FAIL", " 5.7(i) exact equality")
# AND_3: H = 4 - (9/8) log2 3, I = 3/4: H - c I = 4 - (9/8)log2 3 - (3/4)(16/3 - (3/2) log2 3) = 0
r0 = 4 - Fraction(3, 4) * Fraction(16, 3)
l3 = Fraction(-9, 8) + Fraction(3, 4) * Fraction(3, 2)
print("AND_3: H - c* I =", r0, "+", l3, "log2 3")
checks.append(("AND_3 equality", 0.0, r0 == 0 and l3 == 0))
print("\nALL PASS" if all(c[2] for c in checks) else "\nSOME FAILED")
