#!/usr/bin/env python3
"""Small deterministic audits; no sampling, external packages, or worker threads."""
import json
import math
import os
from pathlib import Path
import resource
import threading
import time
from fractions import Fraction as F

START = time.monotonic()
ROOT = Path(__file__).resolve().parent
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
assert threading.active_count() == 1
assert os.environ.get("OMP_NUM_THREADS") == "1"
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))


class Sum:
    def __init__(self):
        self.total = 0.0
        self.correction = 0.0

    def add(self, value):
        adjusted = value - self.correction
        new = self.total + adjusted
        self.correction = (new - self.total) - adjusted
        self.total = new


def quadrature(n, a=0.4, b=0.2):
    # V=(x^2+y^2)/2+a(1-cos(x)cos(y))+b(sin(x)-x).
    # Its Hessian lies between (1-a-b)I and (1+a+b)I.
    radius = 10.0
    step = 2 * radius / n
    sums = [Sum() for _ in range(13)]
    L = 1 + a + b
    ts = [-1 / (4 * L), -1 / (8 * L), 1 / (8 * L), 1 / (4 * L)]
    mgfs = [Sum() for _ in ts]
    for i in range(n + 1):
        x = -radius + i * step
        sx, cx = math.sin(x), math.cos(x)
        wx = 1 if i in (0, n) else 2 if i % 2 == 0 else 4
        for j in range(n + 1):
            y = -radius + j * step
            sy, cy = math.sin(y), math.cos(y)
            wy = 1 if j in (0, n) else 2 if j % 2 == 0 else 4
            V = (x*x + y*y)/2 + a*(1-cx*cy) + b*(sx-x)
            gx, gy = x+a*sx*cy+b*(cx-1), y+a*cx*sy
            k11, k22, k12 = 1+a*cx*cy-b*sx, 1+a*cx*cy, -a*sx*sy
            D = k11 + k22
            S = gx*gx + gy*gy
            K2 = k11*k11 + k22*k22 + 2*k12*k12
            gKg = k11*gx*gx + 2*k12*gx*gy + k22*gy*gy
            gen = D-S
            B = 2*D-S
            vals = (1, D, S, K2, gKg, D*D, D*S, S*S,
                    gen*gen, gen*S, B, B*B,
                    (4*D*D+8*K2-4*D*S+S*S)/576)
            weight = wx * wy * math.exp(-V)
            for acc, value in zip(sums, vals):
                acc.add(weight*value)
            for acc, t in zip(mgfs, ts):
                acc.add(weight*math.exp(t*gen))
    norm = sums[0].total
    (one, D, S, K2, gKg, D2, DS, S2, gen2, genS, B, B2,
     raw_A2) = [acc.total/norm for acc in sums]
    varS = S2-S*S
    varA_direct = raw_A2-(B/24)**2
    varA_identity = (12*K2-4*gKg+varS)/576
    errors = {
        "ES_minus_ED": S-D,
        "bochner": gen2-K2-gKg,
        "cross_generator_S": genS+2*gKg,
        "variance_identity": varA_direct-varA_identity,
        "variance_B_identity": (B2-B*B)-(4*K2-4*gKg+varS),
    }
    assert max(map(abs, errors.values())) < 1e-10, errors
    assert K2/72 <= varA_direct <= K2/48
    assert varS <= 4*gKg
    mgf_results = []
    for t, acc in zip(ts, mgfs):
        logmgf = math.log(acc.total/norm)
        upper = 4 * 2 * L*L*t*t
        assert logmgf <= upper + 1e-12
        mgf_results.append({"t": t, "log_mgf_F": logmgf, "bound": upper})
    return {"n_per_axis": n, "box": [-radius, radius],
            "potential_parameters": {"a": a, "b": b, "m": 1-a-b, "L": L},
            "moments": {"ED": D, "ES": S, "EtrK2": K2, "EgKg": gKg,
                        "VarS": varS, "VarA_direct": varA_direct,
                        "VarA_identity": varA_identity,
                        "lower": K2/72, "upper": K2/48},
            "identity_errors": errors, "mgf_checks": mgf_results}


DEG = 10


def const(c):
    return [F(c)] + [F(0)]*DEG


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def scale(a, c):
    return [x*c for x in a]


def mul(a, b):
    return [sum((a[j]*b[k-j] for j in range(k+1)), F(0))
            for k in range(DEG+1)]


def power(a, n):
    result = const(1)
    for _ in range(n):
        result = mul(result, a)
    return result


H = [F(0), F(1)] + [F(0)]*(DEG-1)
H2 = power(H, 2)


def rational_local_checks():
    records = []
    for g, k, c, e, p in [(F(2, 3), F(7, 5), F(-3, 7), F(1, 4), F(5, 6)),
                          (F(-4, 5), F(1, 2), F(2, 3), F(-1, 7), F(-3, 2))]:
        dx = add(scale(H, p), scale(H2, -g/2))
        grad_new = const(g)
        Vdiff = const(0)
        for order, derivative in enumerate([g, k, c, e], start=1):
            Vdiff = add(Vdiff, scale(power(dx, order), derivative/F(math.factorial(order))))
            if order > 1:
                grad_new = add(grad_new, scale(power(dx, order-1), derivative/F(math.factorial(order-1))))
        pnew = add(const(p), scale(mul(H, add(const(g), grad_new)), F(-1, 2)))
        denergy = add(Vdiff, scale(add(power(pnew, 2), const(-p*p)), F(1, 2)))
        predicted = p*k*g/4-c*p**3/12
        assert denergy[1] == denergy[2] == 0
        assert denergy[3] == predicted
        knew = add(const(k), add(scale(dx, c), scale(power(dx, 2), e/2)))
        anew = add(scale(mul(power(pnew, 2), knew), F(1, 12)),
                   scale(power(grad_new, 2), F(-1, 24)))
        aold = p*p*k/12-g*g/24
        modified_diff = add(denergy, mul(H2, add(anew, const(-aold))))
        assert all(modified_diff[j] == 0 for j in range(4))
        records.append({"g,k,c,e,p": list(map(str, (g, k, c, e, p))),
                        "h3_energy_coefficient": str(denergy[3]),
                        "modified_energy_through_h3": "all zero"})
    return records


def gaussian_exact_checks():
    lam, x, p = F(7, 5), F(2, 3), F(-4, 5)
    xn = add(const(x), add(scale(H, p), scale(H2, -lam*x/2)))
    pn = add(const(p), scale(mul(H, add(const(lam*x), scale(xn, lam))), F(-1, 2)))
    dx2 = add(power(xn, 2), const(-x*x))
    dp2 = add(power(pn, 2), const(-p*p))
    invariant_difference = add(dp2, mul(add(const(lam), scale(H2, -lam*lam/4)), dx2))
    assert all(c == 0 for c in invariant_difference)
    dh = scale(add(dp2, scale(dx2, lam)), F(1, 2))
    da = add(scale(dp2, lam/12), scale(dx2, -lam*lam/24))
    remainder = add(dh, mul(H2, da))
    exact_remainder = scale(mul(power(H, 4), dx2), lam**3/48)
    assert remainder == exact_remainder
    gaussian_var = (lam/12)**2*2+(lam*lam/24)**2*2/(lam*lam)
    assert gaussian_var == F(5, 288)*lam*lam
    return {"lambda": str(lam), "variance_per_coordinate": str(gaussian_var),
            "variance_over_lambda_squared": str(gaussian_var/(lam*lam)),
            "exact_leapfrog_invariant": "p^2+lambda*(1-h^2*lambda/4)*x^2",
            "invariant_polynomial_difference": "all zero",
            "exact_modified_remainder": "h^4*lambda^3*(x_n^2-x^2)/48"}


def leapfrog_limit_check():
    a, x0, p0, T = 0.4, 0.7, 1.1, 1.0

    def grad(x):
        return x + a*math.sin(x)

    def energy(x, p):
        return x*x/2+a*(1-math.cos(x))+p*p/2

    def coef(x, p):
        return p*p*(1+a*math.cos(x))/12-grad(x)**2/24

    def rk4(n):
        dt = T/n
        x, p = x0, p0
        for _ in range(n):
            ax, ap = p, -grad(x)
            bx, bp = p+dt*ap/2, -grad(x+dt*ax/2)
            cx, cp = p+dt*bp/2, -grad(x+dt*bx/2)
            dx, dp = p+dt*cp, -grad(x+dt*cx)
            x += dt*(ax+2*bx+2*cx+dx)/6
            p += dt*(ap+2*bp+2*cp+dp)/6
        return x, p

    zref = rk4(8192)
    zref2 = rk4(16384)
    reference = coef(x0, p0)-coef(*zref2)
    assert max(abs(v-w) for v, w in zip(zref, zref2)) < 1e-11
    rows = []
    for n in (16, 32, 64, 128, 256):
        h = T/n
        x, p = x0, p0
        for _ in range(n):
            phalf = p-h*grad(x)/2
            x += h*phalf
            p = phalf-h*grad(x)/2
        normalized = (energy(x, p)-energy(x0, p0))/(h*h)
        rows.append({"n": n, "h": h, "energy_error_over_h2": normalized,
                     "coefficient_reference": reference,
                     "absolute_difference": abs(normalized-reference)})
    assert rows[-1]["absolute_difference"] < rows[0]["absolute_difference"]/100
    return {"potential": "x^2/2+0.4*(1-cos(x))", "x0": x0, "p0": p0,
            "T": T, "RK4_reference_steps": [8192, 16384],
            "reference_endpoint_difference": max(abs(v-w) for v, w in zip(zref, zref2)),
            "rows": rows}


def main():
    data = {"quadrature": [quadrature(128), quadrature(256)],
            "rational_local_checks": rational_local_checks(),
            "gaussian_exact_checks": gaussian_exact_checks(),
            "leapfrog_limit_check": leapfrog_limit_check()}
    moment_change = max(abs(data["quadrature"][0]["moments"][key] -
                            data["quadrature"][1]["moments"][key])
                        for key in data["quadrature"][0]["moments"])
    assert moment_change < 1e-10
    data["quadrature_refinement_max_moment_change"] = moment_change
    data["resources"] = {
        "nice": os.getpriority(os.PRIO_PROCESS, 0),
        "python_threads": threading.active_count(),
        "elapsed_seconds": time.monotonic()-START,
        "max_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    assert data["resources"]["max_rss_bytes_macos"] < 1024**3
    assert data["resources"]["elapsed_seconds"] < 120
    (ROOT / "audit_data.json").write_text(json.dumps(data, indent=2)+"\n")
    max_error = max(abs(v) for row in data["quadrature"] for v in row["identity_errors"].values())
    print("PASS: exact rational local expansion, Gaussian variance, and Gaussian invariant/remainder")
    print(f"PASS: nonproduct 2D integration-by-parts identities; max absolute residual {max_error:.3e}")
    print(f"PASS: 128 -> 256 Simpson refinement; max moment change {moment_change:.3e}")
    moments = data["quadrature"][-1]["moments"]
    print("Nonproduct Var(A): %.12g; proven interval [%.12g, %.12g]" %
          (moments["VarA_direct"], moments["lower"], moments["upper"]))
    print("PASS: generator mgf inequalities at four positive/negative t values")
    rows = data["leapfrog_limit_check"]["rows"]
    print("Leapfrog coefficient errors (n=16,32,64,128,256): " +
          ", ".join(f'{r["absolute_difference"]:.3e}' for r in rows))
    print("Resources: " + json.dumps(data["resources"], sort_keys=True))
    print("Data: audit_data.json")


if __name__ == "__main__":
    main()
