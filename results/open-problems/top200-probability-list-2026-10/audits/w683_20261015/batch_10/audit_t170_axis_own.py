"""Independent exact input checks for the six-slab T170 claim.

Derived from the Gamma survival polynomial and the rate formula in the proof.
No solver source is imported or executed.
"""
import json
from fractions import Fraction
from math import factorial
from pathlib import Path

ROOT = Path(r"~\brain_workers\w676\T170")
OUT = Path(__file__).parent / "checks" / "t170_axis_own_inputs.json"
NAMES = {20: "axis6_d20_93d3537bbf815cc7", 21: "axis6_d21_7e6db2a22c9666b0"}
SCALE = 1 << 40


def gamma_units(n: int, count: int) -> tuple[int, int]:
    m = n - 1
    q = [factorial(m) // factorial(j) for j in range(m + 1)]
    degree = m * count
    a = [q[0] ** count]
    # Q*C'=count*Q'*C, Q=(n-1)! sum(t^j/j!), C=Q^count.
    for k in range(degree):
        numerator = sum(((count + 1) * j - k - 1) * q[j] * a[k + 1 - j]
                        for j in range(1, min(m, k + 1) + 1))
        denominator = q[0] * (k + 1)
        assert numerator >= 0 and numerator % denominator == 0
        a.append(numerator // denominator)
    assert a[-1] == 1  # Q is monic.
    total = 0
    fac = 1
    for k, coeff in enumerate(a):
        if k:
            fac *= k
        total = total * count + coeff * fac
    denominator = count ** (degree + 1) * q[0] ** count
    upper = (SCALE * total + denominator - 1) // denominator
    return upper, degree


def main() -> None:
    result = {}
    for d, name in NAMES.items():
        meta = json.loads((ROOT / "inputs" / f"{name}.json").read_text(encoding="utf8"))
        lines = (ROOT / "inputs" / f"{name}.txt").read_text(encoding="utf8").splitlines()
        header = list(map(int, lines[0].split()))
        gammas = list(map(int, lines[1].split()))
        s = list(map(int, lines[2].split()))
        assert header[:2] == [d, 40] and header[4] == 1 and len(s) == 10001
        assert gammas == meta["gammas"] and meta["scale"] == SCALE
        assert s[0] == 0
        base = pow(2 * (d - 1), d - 1)
        for i in range(1, len(s)):
            target = base * pow(i, d - 2)
            assert pow(s[i] - 1, d - 1) < target <= pow(s[i], d - 1), (d, i)
        exact = []
        for n, counts in enumerate(meta["profiles"], 1):
            u, degree = gamma_units(n, counts[0])
            assert u == gammas[n - 1], (d, n, u, gammas[n - 1])
            exact.append({"n": n, "N": counts[0], "degree": degree, "ceil_units": u})
        num = int(meta["gamma6_exact_numerator_hex"], 16)
        den = int(meta["gamma6_exact_denominator_hex"], 16)
        assert (SCALE * num + den - 1) // den == gammas[5]
        result[d] = {"header": header, "gammas_checked": exact, "s_checked": len(s),
                     "gamma6_stored_rational_ceiling": True}
    # The latter strictly exceeds the former in Euclidean units.
    floors = {20: Fraction(75761952989, 10**12), 21: Fraction(73855233803, 10**12)}
    uppers = {20: Fraction(41513476821, 549755813888),
              21: Fraction(159802371323, 2199023255552)}
    for d in NAMES:
        assert uppers[d] < floors[d]
        result[d]["exact_crossing_numerator"] = (floors[d] - uppers[d]).numerator
        result[d]["exact_crossing_denominator"] = (floors[d] - uppers[d]).denominator
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf8")
    print(json.dumps({d: {"gamma6": result[d]["gammas_checked"][-1]["ceil_units"],
                           "s_checked": result[d]["s_checked"],
                           "gap": str(Fraction(result[d]["exact_crossing_numerator"], result[d]["exact_crossing_denominator"]))}
                      for d in NAMES}))


if __name__ == "__main__":
    main()
