#!/usr/bin/env python3
"""
Exact-q-binomial variational certificate for the Kirousis--Kranakis--Krizanc--Stamatiou
radius-two local-max upper-bound scheme for iid random 3-SAT.

The paper's equations (17)--(19) give
  E|A_2#| <= (7/8)^(rn) sum_A X_n^sf(A) Y_n^df(A)
with X_n -> X=1-u^3 and
  Y_n = 1-c/n+o(1/n),
u=exp(-r/7),
c = 6 u^6 L/(1-u^3) * (1 - 3 u^3 L/(1-u^3)), L=r/7.

The exact identity
  sum_A X^sf(A) q^df(A) = sum_k [n choose k]_q X^k
gives the thermodynamic variational exponent
  R(r)=r log(7/8)+max_{0<=p<=1} F_r(p).
F is strictly concave and its maximizer is explicit.

This script uses mpmath interval arithmetic. Li_2 is bounded by its positive
power series plus a rigorous geometric tail bound. The interval check at
r=4.5923 is the certificate used in the report. The optimized zero printed
afterward is a high-precision diagnostic, not needed for the theorem.
"""
import mpmath as mp

IV_DPS = 60
SERIES_N = 6000
mp.iv.dps = IV_DPS
mp.mp.dps = 60

def li2_iv(z, N=SERIES_N):
    """Rigorous Li_2(z) enclosure for 0 <= z < 1."""
    s = mp.iv.mpf([0, 0])
    zk = mp.iv.mpf([1, 1])
    for k in range(1, N + 1):
        zk *= z
        s += zk / (k * k)
    # For positive z<1:
    # sum_{k>N} z^k/k^2 <= z^(N+1)/((N+1)^2(1-z)).
    tail = zk * z / ((N + 1) ** 2 * (1 - z))
    return s + mp.iv.mpf([0, 1]) * tail

def interval_rate(r_string):
    r = mp.iv.mpf([r_string, r_string])
    u = mp.iv.exp(-r / 7)
    X = 1 - u**3
    L = r / 7
    c = (6 * u**6 * L / (1 - u**3)
         * (1 - 3 * u**3 * L / (1 - u**3)))
    ec = mp.iv.exp(-c)

    # F'(p)=0 iff X(1-exp(-c(1-p)))=1-exp(-cp).
    # With a=exp(-cp), a is the positive root of
    # a^2 + (X-1)a - X exp(-c)=0.
    a = ((1 - X) + mp.iv.sqrt((1 - X)**2 + 4 * X * ec)) / 2
    p = -mp.iv.log(a) / c

    z_left = mp.iv.exp(-c * (1 - p))
    z_right = mp.iv.exp(-c * p)
    J = (li2_iv(ec) - li2_iv(z_left) - li2_iv(z_right)
         + mp.iv.pi**2 / 6) / c
    F = p * mp.iv.log(X) + J
    R = r * mp.iv.log(mp.iv.mpf(7) / 8) + F
    return X, c, p, F, R

def li2(x):
    return mp.polylog(2, x)

def point_rate(r):
    r = mp.mpf(r)
    u = mp.exp(-r / 7)
    X = 1 - u**3
    L = r / 7
    c = (6 * u**6 * L / (1 - u**3)
         * (1 - 3 * u**3 * L / (1 - u**3)))
    ec = mp.exp(-c)
    a = ((1 - X) + mp.sqrt((1 - X)**2 + 4 * X * ec)) / 2
    p = -mp.log(a) / c
    J = (li2(ec) - li2(mp.exp(-c * (1 - p)))
         - li2(mp.exp(-c * p)) + mp.pi**2 / 6) / c
    F = p * mp.log(X) + J
    return p, r * mp.log(mp.mpf(7) / 8) + F

if __name__ == "__main__":
    r_cert = "4.5923"
    X, c, p, F, R = interval_rate(r_cert)
    print("CERTIFICATE")
    print("r =", r_cert)
    print("X interval =", X)
    print("c interval =", c)
    print("p_star interval =", p)
    print("F(p_star) interval =", F)
    print("R(r)=r*log(7/8)+F interval =", R)
    print("CERTIFIED_NEGATIVE =", bool(R.b < 0))
    print()
    root = mp.findroot(lambda rr: point_rate(rr)[1],
                       (mp.mpf("4.5922"), mp.mpf("4.5924")))
    p0, rr0 = point_rate(root)
    print("DIAGNOSTIC_OPTIMIZED_ZERO_NOT_NEEDED_FOR_THEOREM")
    print("r_zero =", mp.nstr(root, 40))
    print("p_star_at_zero =", mp.nstr(p0, 40))
    print("residual =", mp.nstr(rr0, 20))
