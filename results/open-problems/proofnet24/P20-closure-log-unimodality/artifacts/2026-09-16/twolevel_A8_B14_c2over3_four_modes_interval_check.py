#!/usr/bin/env python3
"""Certified interval core for P20 / I0081.

Input log-density:
    h(y)=1/24 for |y|<=8,
         1/36 for 8<|y|<=14,
         0 otherwise.
For rho=mu box-times mu, certify physical-boundary derivative signs
    g'(6)>0, g'(10)<0, g'(20)>0, g'(22)<0.

The finite rational normalization is checked exactly with Fraction.
The analytic root boxes are certified by a Krawczyk/contraction argument
using mpmath interval arithmetic with outward rounding.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 100
mp.iv.dps = 70
iv = mp.iv

# Exact finite core for the input law.
assert Fraction(16, 24) + Fraction(12, 36) == 1
assert Fraction(1, 24) >= Fraction(1, 36) > 0

# Decimal rationals defining certificate centers and fixed contraction scalars.
# Every listed decimal is treated as data; no floating root finder is used.
DATA = {
    6: {
        "qre": "0.0057904399813301579731348324361628781495937473399357",
        "qim": "0.037427178997821955938854995096985126472978945138054",
        "cre": "1.21667585566302557378334985144838620717105987974315216524249180868811114918060214946027556",
        "cim": "8.2831845130768822797858410522588496776673270734408297936968873698730341209436481079264519",
        "sign": 1,
    },
    10: {
        "qre": "0.00074015304822466058726766533918175660142028116703015",
        "qim": "0.0041077284863999117092708486158685291605502132355432",
        "cre": "8.30795906140145865262356151886220846951628250189923156381481155628836963401917656332427118",
        "cim": "50.432065345761473795989134758357075545556234271560086874931825402323762184669157157096549",
        "sign": -1,
    },
    20: {
        "qre": "0.00000452489291455126114156663854028669695064110836617217602959667",
        "qim": "0.0000137747752468639449412257929747764981600367738393160671124835",
        "cre": "958.547478127614348143273829254845322978001550548779961272427911223507673266377395200966374",
        "cim": "3991.35932003507783067280893907550399609375792898421732260978594849852119705488522685399931",
        "sign": 1,
    },
    22: {
        "qre": "0.000001957460503996979290040979408085251120615501439529",
        "qim": "0.0000040022753491200247522814056756503034961131565746721",
        "cre": "2811.07422508919386366198559086974429782698993623561977223033352111675615604360961038916376",
        "cim": "9270.89338930388120251249434630041951768404872932038349342524384299919973747439092912596927",
        "sign": -1,
    },
}
RADIUS = iv.mpf("1e-25")


def positive(x):
    return x.a > 0


def negative(x):
    return x.b < 0


def less_than(x, c):
    return x.b < iv.mpf(str(c))


def strict_contains(outer, inner):
    return (
        outer.real.a < inner.real.a
        and inner.real.b < outer.real.b
        and outer.imag.a < inner.imag.a
        and inner.imag.b < outer.imag.b
    )


def abs2(z):
    return z.real**2 + z.imag**2


def F(X, z):
    X = iv.mpf(X)
    ep = iv.exp(X)
    em = iv.exp(-X)
    return 2 * X - iv.log(1 - z * ep) + iv.log(1 - z * em)


def Fp(X, z):
    X = iv.mpf(X)
    ep = iv.exp(X)
    em = iv.exp(-X)
    return ep / (1 - z * ep) - em / (1 - z * em)


def M(z):
    # h = (1/72) 1_{[-8,8]} + (1/36) 1_{[-14,14]}.
    return (F(8, z) + 2 * F(14, z)) / 72


def Mp(z):
    return (Fp(8, z) + 2 * Fp(14, z)) / 72


def eta(z):
    mz = M(z)
    return 1 - 1 / mz


def etap(z):
    mz = M(z)
    return Mp(z) / mz**2


def H(z):
    ez = eta(z)
    return z**2 / ez


def Hp(z):
    ez = eta(z)
    ep = etap(z)
    return 2 * z / ez - z**2 * ep / ez**2


def density_and_derivative(y, z):
    # For s=e^{-y}=1/x and w=eta_mu(q)=eta_rho(s+i0),
    # g(y)=x f_rho(x)=Im(1/(1-w))/pi.
    s = iv.exp(-iv.mpf(y))
    w = eta(z)
    qy = -s / Hp(z)
    wy = etap(z) * qy
    g = iv.im(1 / (1 - w)) / iv.pi
    gp = iv.im(wy / (1 - w) ** 2) / iv.pi
    return g, gp, w


print("P20 I0081 A=8 B=14 c=2/3 four-mode certified interval core")
print("mpmath version:", mp.__version__)
print("interval dps:", mp.iv.dps)
print("exact normalization: 16/24 + 12/36 =", Fraction(16, 24) + Fraction(12, 36))
print("exact monotonic input levels: 1/24 >= 1/36 > 0 : PASS")
print("root-box radius:", RADIUS)

all_ok = True
for y in (6, 10, 20, 22):
    d = DATA[y]
    r0 = iv.mpf(d["qre"])
    i0 = iv.mpf(d["qim"])
    q0 = iv.mpc(r0, i0)
    C = iv.mpc(iv.mpf(d["cre"]), iv.mpf(d["cim"]))
    X = iv.mpc([r0.a - RADIUS.b, r0.b + RADIUS.b],
               [i0.a - RADIUS.b, i0.b + RADIUS.b])
    s = iv.exp(-iv.mpf(y))

    # Verify the logarithms used in F_8,F_14 stay off their principal branch cut.
    branch_ok = True
    for R in (8, 14):
        ep = iv.exp(iv.mpf(R))
        em = iv.exp(-iv.mpf(R))
        branch_ok &= negative((1 - X * ep).imag)
        branch_ok &= negative((1 - X * em).imag)

    mz = M(X)
    ez = eta(X)
    hp = Hp(X)
    denominator_ok = positive(abs2(mz)) and positive(abs2(ez)) and positive(abs2(hp))

    # Rigorous contraction/Krawczyk box for H(q)=exp(-y).
    f0 = H(q0) - s
    contraction_factor = 1 - C * hp
    K = q0 - C * f0 + contraction_factor * (X - q0)
    krawczyk_inclusion = strict_contains(X, K)
    contraction_sq = abs2(contraction_factor)
    contraction_ok = less_than(contraction_sq, 1)

    g, gp, w = density_and_derivative(y, X)
    one_minus_w_ok = positive(abs2(1 - w))
    w_inside_unit = less_than(abs2(w), 1)
    density_positive = positive(g)
    derivative_sign = positive(gp) if d["sign"] > 0 else negative(gp)
    upper_half_plane = positive(X.imag)

    ok = all([
        branch_ok,
        denominator_ok,
        krawczyk_inclusion,
        contraction_ok,
        upper_half_plane,
        one_minus_w_ok,
        w_inside_unit,
        density_positive,
        derivative_sign,
    ])
    all_ok &= ok

    print("\ny =", y)
    print("X.real =", X.real)
    print("X.imag =", X.imag)
    print("principal-log branch safe:", branch_ok)
    print("denominators nonzero:", denominator_ok)
    print("K.rawczyk.real =", K.real)
    print("K.rawczyk.imag =", K.imag)
    print("K(X) subset int(X):", krawczyk_inclusion)
    print("|1-C Hprime(X)|^2 =", contraction_sq, " <1:", contraction_ok)
    print("Im X > 0:", upper_half_plane)
    print("|w|^2 =", abs2(w), " <1:", w_inside_unit)
    print("|1-w|^2 =", abs2(1 - w), " nonzero:", one_minus_w_ok)
    print("g(y) =", g, " positive:", density_positive)
    print("gprime(y) =", gp, " expected sign:", d["sign"], " PASS:", derivative_sign)
    print("H(q0)-exp(-y) =", f0)
    print("POINT CERTIFICATE PASS:", ok)

assert all_ok
print("\nALL_INTERVAL_CHECKS_PASS")
print("Certified sign pattern: gprime(6)>0, gprime(10)<0, gprime(20)>0, gprime(22)<0.")
