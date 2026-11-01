"""Checkpointed outward-rounded certificate for Sly's q=3 Gaussian map.

No downloaded code, floating-point decisions, or unbounded loops. The analytic
quadrature error and monotonicity reduction are proved separately in the claim.
Each endpoint is saved immediately. A run resumes only matching source hashes.
"""
from __future__ import annotations
import argparse
import datetime
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

START = time.monotonic()
ROOT = Path(__file__).resolve().parent
SOURCE_HASH = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def exact_ball(x):
    """Save directed dyadic endpoints, not a display string used as a bound."""
    assert x.is_finite()
    lo, hi = x.lower(), x.upper()
    assert lo.is_exact() and hi.is_exact()
    lm, le = lo.man_exp()
    hm, he = hi.man_exp()
    return {"lower": [int(lm), int(le)], "upper": [int(hm), int(he)],
            "display": str(x)}


def as_fraction(pair):
    m, e = pair
    return F(m * (1 << e)) if e >= 0 else F(m, 1 << (-e))


def frac_text(x):
    return f"{x.numerator}/{x.denominator}"


def save(path, item):
    part = path.with_suffix(path.suffix + ".part")
    part.write_text(json.dumps(item, indent=2) + "\n", encoding="utf-8", newline="")
    part.replace(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=240)
    parser.add_argument("--count", type=int, default=85)
    args = parser.parse_args()
    assert 1 <= args.seconds <= 480 and 1 <= args.count <= 85
    import flint
    from flint import arb, ctx
    ctx.prec = 160
    outdir = ROOT / "gaussian_gap_v1"
    outdir.mkdir(exist_ok=True)
    radius, width, c, gamma = F(6), F(1, 8), F(2, 5), F(3, 50)
    grid = [1 / (F(10) - F(i, 10)) for i in range(86)]
    assert grid[0] == F(1, 10) and grid[-1] == F(2, 3)
    assert all(1 / grid[i] - 1 / grid[i+1] == F(1, 10) for i in range(85))
    config = {"source_sha256": SOURCE_HASH, "python_flint_version": flint.__version__,
              "precision_bits": ctx.prec, "radius": frac_text(radius),
              "bin_width": frac_text(width), "gap_constant": frac_text(c),
              "linear_gap_constant": frac_text(gamma),
              "interval_count": 85, "dimension": 2,
              "arithmetic": "Arb outward-rounded real balls; exact dyadic exports",
              "working_memory_estimate_bytes": 10_000_000, "cpu_workers": 1}
    old_config = outdir / "config.json"
    if old_config.exists():
        assert json.loads(old_config.read_text(encoding="utf-8")) == config
    else:
        save(old_config, config)

    def A(x):
        return arb(x.numerator) / x.denominator

    sqrt2 = arb(2).sqrt()
    normalizer = (2 * arb.pi()).sqrt()

    def phi(z):
        return (-z*z/2).exp() / normalizer

    bins = []
    for j in range(48):
        a, b = A(j * width), A((j+1) * width)
        w = ((b/sqrt2).erf() - (a/sqrt2).erf())/2
        first = phi(a) - phi(b)
        second = w + a*phi(a) - b*phi(b)
        mean = first/w
        var = second - first*first/w
        assert w > 0 and mean > a and mean < b and var > 0
        bins.append((w, mean, var))
    P = 2 * sum((w for w, _, _ in bins), arb(0))
    D = 2 * sum((v for _, _, v in bins), arb(0))
    tail = 1-P*P
    assert P > 0 and P < 1 and D > 0 and tail > 0
    bin_record = {"P": exact_ball(P), "D": exact_ball(D),
                  "outside_square_probability": exact_ball(tail),
                  "positive_half_bins": [
                      {"weight": exact_ball(w), "conditional_mean": exact_ball(m),
                       "unnormalized_variance": exact_ball(v)} for w,m,v in bins]}
    save(outdir / "bins.json", bin_record)
    completed_now = 0
    for i, (a,b) in enumerate(zip(grid,grid[1:])):
        dest = outdir / f"endpoint_{i:03d}.json"
        if dest.exists():
            old = json.loads(dest.read_text(encoding="utf-8"))
            assert old["source_sha256"] == SOURCE_HASH and old["a"] == frac_text(a)
            assert old["b"] == frac_text(b) and old["passed"] is True
            continue
        if completed_now >= args.count or time.monotonic()-START >= args.seconds:
            break
        s = A(b)
        slope1 = 3*(3*s).sqrt()/2
        slope2 = 3*s.sqrt()/2
        coshes = [(slope2*m).cosh() for _,m,_ in bins]
        Q = arb(0)
        for wi,mi,_ in bins:
            ap = 2 * (-9*s/2-slope1*mi).exp()
            am = 2 * (-9*s/2+slope1*mi).exp()
            row = arb(0)
            for (wj,_,_), bj in zip(bins,coshes):
                row += 2*wj * (1/(1+ap*bj) + 1/(1+am*bj))
            Q += wi*row
        remainder = 9*s*P*D/4
        g_upper_ball = Q + remainder + tail - arb(1)/3
        g_lower_ball = Q - remainder - arb(1)/3
        margin = A(a) - g_upper_ball - A(c*b*b)
        linear_margin = A(a) - g_upper_ball - A(gamma*b)
        record = {"source_sha256": SOURCE_HASH, "a": frac_text(a), "b": frac_text(b),
                  "Q": exact_ball(Q), "quadrature_error": exact_ball(remainder),
                  "g_upper": exact_ball(g_upper_ball), "g_lower": exact_ball(g_lower_ball),
                  "margin_a_minus_g_upper_minus_c_b_squared": exact_ball(margin),
                  "linear_margin_a_minus_g_upper_minus_gamma_b": exact_ball(linear_margin),
                  "passed": bool(margin > 0) and bool(linear_margin > 0)}
        # A second, exact rational comparison checks the saved upper endpoint.
        rational_margin = a-as_fraction(record["g_upper"]["upper"])-c*b*b
        rational_linear_margin = a-as_fraction(record["g_upper"]["upper"])-gamma*b
        record["exact_rational_margin_from_saved_upper"] = frac_text(rational_margin)
        record["exact_rational_linear_margin_from_saved_upper"] = frac_text(rational_linear_margin)
        assert record["passed"] and rational_margin > 0 and rational_linear_margin > 0, record
        save(dest, record)
        completed_now += 1
        print(json.dumps({"endpoint": i, "b": frac_text(b), "passed": True,
                          "margin": str(margin)}), flush=True)

    rows = []
    for i in range(85):
        path = outdir / f"endpoint_{i:03d}.json"
        if path.exists():
            record = json.loads(path.read_text(encoding="utf-8"))
            assert record["source_sha256"] == SOURCE_HASH
            rows.append({"index": i, "file": path.name,
                         "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                         "exact_margin": record["exact_rational_margin_from_saved_upper"],
                         "exact_linear_margin": record["exact_rational_linear_margin_from_saved_upper"],
                         "passed": record["passed"]})
    report = {**config, "status": "PASS" if len(rows)==85 else "PARTIAL",
              "completed": len(rows), "new_this_run": completed_now, "endpoints": rows,
              "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "elapsed_seconds": time.monotonic()-START,
              "claim_if_complete": "s-g_3(s) >= max((2/5)s^2,(3/50)s) for every 1/10<=s<=2/3",
              "scope": "Numerical certificate conditional on the separate analytic error proof"}
    save(outdir / "report.json", report)
    print(json.dumps({"status": report["status"], "completed": len(rows),
                      "new_this_run": completed_now}), flush=True)


if __name__ == "__main__":
    main()
