from fractions import Fraction as F


def b(n, lam):
    n = F(n)
    lam = F(lam)
    return 1 / ((F(2) - lam) * (n - lam * (n - F(1)) / F(2)))


def a(n, D, lam):
    n = F(n)
    D = F(D)
    lam = F(lam)
    return (D - F(1)) / ((D - lam) * (n + lam * (D - n - F(1)) / D))


def g(n, D, lam):
    return F(n) * a(n, D, lam)


def chord_coeff(x0, x1, y0, y1):
    s = (y1 - y0) / (F(x1) - F(x0))
    c = y0 - s * F(x0)
    return c, s


def max_concave_quadratic(A, B, C, lo, hi):
    lo = F(lo)
    hi = F(hi)
    cand = [(A * lo * lo + B * lo + C, lo),
            (A * hi * hi + B * hi + C, hi)]
    if A < 0:
        rv = -B / (2 * A)
        if lo <= rv <= hi:
            cand.append((A * rv * rv + B * rv + C, rv))
    return max(cand, key=lambda x: x[0])


def broad_certificate(D, L):
    D = int(D)
    L = F(L)
    bd = b(2, L)
    bD = b(D, L)
    gd = g(2, D, L)
    gD = g(D, D, F(1))
    b0, bs = chord_coeff(2, D, bd, bD)
    g0, gs = chord_coeff(2, D, gd, gD)
    # H(r)=r*(b0+bs*r)-(g0+gs*r), Psi=L*H-r.
    A = L * bs
    B = L * b0 - L * gs - F(1)
    C = -L * g0
    mx, rv = max_concave_quadratic(A, B, C, 2, D)
    delta = -mx
    margin = 2 * delta / (F(D) + L) ** 2 if delta > 0 else None
    return dict(D=D, L=L, bd=bd, bD=bD, gd=gd, gD=gD,
                A=A, B=B, C=C, maxpsi=mx, rstar=rv,
                delta=delta, margin=margin)


def two_support_certificate(D, L):
    D = int(D)
    L = F(L)
    b2 = b(2, L)
    aD_min = a(D, D, F(1))
    gap = b2 - aD_min
    K = L * F(D - 2) * gap
    w = F(D - 2)
    # Phi(theta)=K theta(1-theta)-2-w theta.
    A = -K
    B = K - w
    C = -F(2)
    mx, th = max_concave_quadratic(A, B, C, 0, 1)
    delta = -mx
    margin = 2 * delta / (F(D) + L) ** 2 if delta > 0 else None
    return dict(D=D, L=L, b2=b2, aD_min=aD_min, gap=gap, K=K,
                maxphi=mx, theta=th, delta=delta, margin=margin)


# Main arbitrary-support breadth theorem.
main = broad_certificate(580, F(6, 5))
b0, bs = chord_coeff(2, 580, main["bd"], main["bD"])
g0, gs = chord_coeff(2, 580, main["gd"], main["gD"])
for n in range(2, 581):
    Bsec = b0 + bs * n
    Gsec = g0 + gs * n
    assert b(n, F(6, 5)) <= Bsec
    assert g(n, 580, F(6, 5)) >= Gsec
# For D=580, g_2(lambda) is decreasing on [1,6/5]: its denominator
# h(lambda)=(D-lambda)*(2+lambda*(D-3)/D) has h'>0 there.
assert F(580 - 5) - 2 * F(6, 5) * F(577, 580) > 0
assert main["maxpsi"] < -F(1, 3000)
assert main["margin"] > F(1, 506690160)

# Method boundary at the same endpoint.
fail581 = broad_certificate(581, F(6, 5))
assert fail581["maxpsi"] > 0

# Deeper arbitrary-support rectangle.
deep = broad_certificate(75, F(31, 25))
assert deep["maxpsi"] < -F(7, 100)
assert deep["margin"] > F(175, 7265672)

# Nonadjacent two-point all-mixture extension.
two = two_support_certificate(13, F(3, 2))
assert two["maxphi"] < -F(3, 200)
assert two["margin"] > F(3, 21025)
two14 = two_support_certificate(14, F(3, 2))
assert two14["maxphi"] > 0

print("P01 T06 conditional-degree secant exact checker")
for name, cert in [("broad_D580_L6/5", main),
                   ("deep_D75_L31/25", deep)]:
    print(name)
    for k in ["bd", "bD", "gd", "gD", "A", "B", "C",
              "rstar", "maxpsi", "delta", "margin"]:
        print(" ", k, "=", cert[k], "~", float(cert[k]))
print("boundary_D581_L6/5 maxpsi =", fail581["maxpsi"],
      "~", float(fail581["maxpsi"]))
print("two_point_D13_L3/2")
for k in ["b2", "aD_min", "gap", "K", "theta", "maxphi",
          "delta", "margin"]:
    print(" ", k, "=", two[k], "~", float(two[k]))
print("boundary_two_point_D14_L3/2 maxphi =", two14["maxphi"],
      "~", float(two14["maxphi"]))
print("clean margins:")
print(" D580 L=6/5: ell' <= -1/506690160")
print(" D75 L=31/25: ell' <= -175/7265672")
print(" {2,13} L=3/2: ell' <= -3/21025")
print("ALL_EXACT_CHECKS_PASS")
