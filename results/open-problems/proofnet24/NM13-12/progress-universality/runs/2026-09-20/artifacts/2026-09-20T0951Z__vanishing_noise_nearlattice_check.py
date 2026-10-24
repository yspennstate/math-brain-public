import math


def central_atom_prob(q: int) -> float:
    return math.comb(q, q // 2) / (2.0 ** q)


def conv_peak_lower(q: int, sigma: float) -> float:
    # q-fold sum of xi=(R+sigma Z)/sqrt(1+sigma^2).
    # Evaluate at a most likely lattice center and keep only that nonnegative mixture component.
    p = central_atom_prob(q)
    tau = sigma * math.sqrt(q / (1.0 + sigma * sigma))
    return p / (math.sqrt(2.0 * math.pi) * tau)


def fourth_moment(sigma: float) -> float:
    s2 = sigma * sigma
    return (1.0 + 6.0 * s2 + 3.0 * s2 * s2) / ((1.0 + s2) ** 2)


def flat_density_zero(m: int, sigma: float) -> float:
    # Exact binomial-Gaussian mixture density at zero for u=(1,...,1)/sqrt(m).
    tau = sigma / math.sqrt(1.0 + sigma * sigma)
    maxlog = -1e300
    logs = []
    for j in range(m + 1):
        logw = (
            math.lgamma(m + 1)
            - math.lgamma(j + 1)
            - math.lgamma(m - j + 1)
            - m * math.log(2.0)
        )
        mu = (2 * j - m) / math.sqrt(m) / math.sqrt(1.0 + sigma * sigma)
        lp = -0.5 * math.log(2.0 * math.pi) - math.log(tau) - 0.5 * (mu / tau) ** 2
        z = logw + lp
        logs.append(z)
        maxlog = max(maxlog, z)
    return math.exp(maxlog) * sum(math.exp(z - maxlog) for z in logs)


print("SMOOTHED_RADEMACHER_CHECK")
for s in [1.0, 0.5, 0.1, 1e-3]:
    fm = fourth_moment(s)
    print(f"sigma={s:g} fourth_moment={fm:.15g}")
    assert 1.0 <= fm <= 3.0 + 1e-12

print("\nFIXED_Q_FINITE_CONVOLUTION_DIVERGENCE")
for q in [1, 2, 3, 4, 5, 10]:
    a = conv_peak_lower(q, 1e-3)
    b = conv_peak_lower(q, 1e-4)
    print(
        f"q={q:2d} peak_lb_sigma1e-3={a:.12g} "
        f"peak_lb_sigma1e-4={b:.12g} ratio={b/a:.12g}"
    )
    assert b / a > 9.99

print("\nRATE_CONDITIONS sigma=m^(-1/3)")
for m in [10**3, 10**6, 10**9, 10**12]:
    sigma = m ** (-1 / 3)
    A = m * sigma * sigma / math.log(math.e / sigma)
    k = m ** 0.70
    B = k * (math.log(m) + math.log(math.e / sigma)) / m
    print(f"m={m:>13d} sigma={sigma:.6e} A={A:.9g} B_k=m^.70={B:.9g}")

print("\nNEAR_CRITICAL_SMOOTHING sigma=L*sqrt(log m/m), L=log log m")
for m in [10**6, 10**9, 10**12, 10**18]:
    L = math.log(math.log(m))
    sigma = L * math.sqrt(math.log(m) / m)
    A = m * sigma * sigma / math.log(math.e / sigma)
    print(f"m={m:>19d} L={L:.6g} sigma={sigma:.6e} A={A:.9g}")

print("\nFLAT_DIRECTION_DENSITY_AT_ZERO sigma=m^(-1/3)")
target = 1.0 / math.sqrt(2.0 * math.pi)
for m in [100, 500, 2000, 10000]:
    sigma = m ** (-1 / 3)
    f0 = flat_density_zero(m, sigma)
    print(
        f"m={m:5d} f0={f0:.15g} gaussian={target:.15g} "
        f"abs_err={abs(f0-target):.6e}"
    )
    assert abs(f0 - target) < 0.002

print("\nANTI_CONCENTRATION")
print("For sigma<=1, conditional Gaussian means are separated by >=sqrt(2).")
print("Any interval of radius 1/2 has length 1<sqrt(2), hence contains at most one conditional mean.")
print("The component whose mean is outside the interval contributes <=1/2 conditionally; the other <=1.")
print("Thus Q_xi(1/2)<= (1/2)*1 + (1/2)*(1/2) = 3/4.")

print("\nALL_VANISHING_NOISE_CHECKS_PASS")
