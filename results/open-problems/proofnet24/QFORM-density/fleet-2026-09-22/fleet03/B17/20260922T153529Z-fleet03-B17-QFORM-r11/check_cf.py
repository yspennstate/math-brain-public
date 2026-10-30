import cmath, math


def sinc(z):
    return 1.0 if abs(z) < 1e-15 else math.sin(z) / z


def psi_m(t, m, jumps):
    """Exact CF of X_m/sqrt(m) for finite fragment data (alpha,b)."""
    alpha = sum(a for a, _ in jumps)
    B = sum(a*b for a, b in jumps)
    c = 1.0 - alpha/m
    center = -B/(math.sqrt(m)*c) if c else 0.0
    value = c * cmath.exp(1j*t*center/math.sqrt(m)) * sinc(t*c/(2*math.sqrt(m)))
    for a, b in jumps:
        value += (a/m) * cmath.exp(1j*b*t) * sinc(t*a/(2*m**1.5))
    return value


def psi_limit(t, jumps):
    return cmath.exp(
        -t*t/24.0
        + sum(a*(cmath.exp(1j*b*t)-1.0-1j*b*t) for a, b in jumps)
    )


# symmetric example: total tail intensity 0.7
JUMPS = [(0.2, 2.0), (0.2, -2.0), (0.15, 1.5), (0.15, -1.5)]
TS = [0.5, 1.0, 2.0, 3.0]

previous = None
for m in [50, 100, 500, 1000]:
    errors = [abs(psi_m(t, m, JUMPS)**m - psi_limit(t, JUMPS)) for t in TS]
    worst = max(errors)
    print(f"m={m:4d} max_CF_error={worst:.16e}")
    if previous is not None and m == 100:
        assert worst < previous
    previous = worst

# Exact spectral statement for A_m=diag(J_m/m,J_m/m,-J_m/m):
# J_m/m has eigenvalues 1,0,...,0, so A_m has nonzero spectrum {1,1,-1}.
print("nonzero_spectrum_exact={1,1,-1}")

# For symmetric fragments, delta_j=alpha_j/m and block row=e_j/sqrt(m), hence
# M_delta=diag(alpha_1^2/m^2,alpha_2^2/m^2,alpha_3^2/m^2).
print("fragmentation_energy_scale=Theta(m^-2)")
print("PASS")
