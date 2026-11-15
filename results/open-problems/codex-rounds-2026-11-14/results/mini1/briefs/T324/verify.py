"""Independent, deterministic checks of the two-token formulas; standard library only."""
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DELTA, INITIAL = 0.4, 1.2


def drift(beta, s):
    return 2 * math.sin(s) / (1 + math.exp(beta * (1 - math.cos(s))))


def simpson(f, lo, hi, n=16384):
    dx = (hi - lo) / n
    total = f(lo) + f(hi)
    total += 4 * sum(f(lo + i * dx) for i in range(1, n, 2))
    total += 2 * sum(f(lo + i * dx) for i in range(2, n, 2))
    return total * dx / 3


def interpolate(values, dx):
    pos = (INITIAL - DELTA) / dx
    i = int(pos)
    return values[i] + (pos - i) * (values[i + 1] - values[i])


def kernel_mean(beta, nu, n):
    """Integrating-factor kernel, exact constant-drift transfer per mesh cell."""
    dx = (math.pi - DELTA) / n
    p = [0.0] * (n + 1)
    areas = [0.0] * n
    for i in range(n - 1, -1, -1):
        h = drift(beta, DELTA + (i + 0.5) * dx)
        exponent = h * dx / (2 * nu)
        attenuation = math.exp(-exponent)
        p[i] = -math.expm1(-exponent) / h + attenuation * p[i + 1]
        if exponent < 1e-4:
            one_minus_phi = (exponent / 2 - exponent**2 / 6
                             + exponent**3 / 24 - exponent**4 / 120)
            phi = 1 - one_minus_phi
        else:
            phi = -math.expm1(-exponent) / exponent
            one_minus_phi = 1 - phi
        areas[i] = dx * (one_minus_phi / h + p[i + 1] * phi)
    u = [0.0] * (n + 1)
    for i in range(n):
        u[i + 1] = u[i] + areas[i]
    return interpolate(u, dx)


def finite_difference_mean(beta, nu, n):
    """Separate central-difference solution of Lu=-1; ghost-point Neumann BC."""
    dx = (math.pi - DELTA) / n
    lower, diagonal, upper, rhs = [], [], [], []
    for i in range(1, n):
        h = drift(beta, DELTA + i * dx)
        assert h * dx < 4 * nu, 'central discretization must be monotone'
        lower.append(2 * nu / dx**2 + h / (2 * dx))
        diagonal.append(-4 * nu / dx**2)
        upper.append(2 * nu / dx**2 - h / (2 * dx))
        rhs.append(-1.0)
    lower.append(-1.0)
    diagonal.append(1.0)
    upper.append(0.0)
    rhs.append(dx**2 / (4 * nu))
    for i in range(1, n):
        factor = lower[i] / diagonal[i - 1]
        diagonal[i] -= factor * upper[i - 1]
        rhs[i] -= factor * rhs[i - 1]
    sol = [0.0] * (n + 1)
    sol[n] = rhs[-1] / diagonal[-1]
    for i in range(n - 2, -1, -1):
        sol[i + 1] = (rhs[i] - upper[i] * sol[i + 2]) / diagonal[i]
    return interpolate(sol, dx)


def main():
    deterministic = []
    for beta in (4, 20, 80, 160):
        angular = simpson(lambda s: 1 / drift(beta, s), DELTA, INITIAL)
        cosine = simpson(
            lambda c: (1 + math.exp(beta * (1 - c))) / (2 * (1 - c*c)),
            math.cos(INITIAL), math.cos(DELTA))
        relative = abs(angular / cosine - 1)
        assert relative < 1e-8
        asymptotic = math.exp(beta * (1 - math.cos(INITIAL))) / (
            2 * beta * math.sin(INITIAL)**2)
        deterministic.append(dict(beta=beta, angular=angular, cosine=cosine,
                                  relative_difference=relative,
                                  exact_over_asymptotic=angular/asymptotic))

    stochastic = []
    for beta, nu in ((4, 0.03), (12, 0.002), (0, 0.5)):
        for n in (4096, 8192):
            kernel = kernel_mean(beta, nu, n)
            bvp = finite_difference_mean(beta, nu, n)
            difference = abs(kernel / bvp - 1)
            assert difference < 2e-4
            stochastic.append(dict(beta=beta, nu=nu, intervals=n,
                                   kernel=kernel, finite_difference=bvp,
                                   relative_difference=difference))

    crossover = []
    for r in (0.3, 0.8):
        for beta in (20, 40, 80, 160):
            nu = math.exp(-r * beta)
            value = kernel_mean(beta, nu, 32768)
            refined = kernel_mean(beta, nu, 65536)
            assert abs(value / refined - 1) < 2e-3
            crossover.append(dict(r=r, beta=beta, mean=refined,
                                  log_mean_over_beta=math.log(refined)/beta,
                                  predicted_limit=min(r, 1-math.cos(INITIAL)),
                                  mesh_relative_difference=abs(value/refined-1)))

    audit = dict(delta=DELTA, initial=INITIAL,
                 deterministic=deterministic, stochastic=stochastic,
                 crossover=crossover)
    (ROOT / 'verification.json').write_text(json.dumps(audit, indent=2) + '\n')
    with (ROOT / 'crossover.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(crossover[0]))
        writer.writeheader()
        writer.writerows(crossover)
    print('Deterministic coordinate checks: max relative difference = '
          f'{max(row["relative_difference"] for row in deterministic):.3e}')
    print('Deterministic exact/asymptotic ratios: ' + ', '.join(
        f'beta={row["beta"]}: {row["exact_over_asymptotic"]:.6f}'
        for row in deterministic))
    print('Noisy kernel versus independent finite-difference BVP: '
          f'max relative difference = '
          f'{max(row["relative_difference"] for row in stochastic):.3e}')
    print('Crossover: r, beta, log(mean)/beta, predicted limit')
    for row in crossover:
        print(f'{row["r"]:.1f}, {row["beta"]}, '
              f'{row["log_mean_over_beta"]:.6f}, {row["predicted_limit"]:.6f}')
    print('All checks passed. Wrote verification.json and crossover.csv.')


if __name__ == '__main__':
    main()
