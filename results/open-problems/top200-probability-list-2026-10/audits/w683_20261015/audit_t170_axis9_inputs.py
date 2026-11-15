"""Own exact d=18 nine-slab rate, Gamma and diagonal comparison checks."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from audit_t170_axis_own import gamma_units

SOLVER = Path(r"~/brain_workers/w676/T170")
FLOORS = Path(r"~/brain_workers/w685/T170/logs/chord5_exact_certificates.json")
BASE = SOLVER / "inputs/axis6_d18_64306e98022b1e92.txt"
EXT = SOLVER / "inputs/axisn_exact_d18_m9_87333babe8007f97.txt"
OUT = Path(r"~/brain_workers/w683/checks/t170_axis9_inputs_own.json")
SCALE = 1 << 40


def main():
    a = BASE.read_text(encoding="utf-8").splitlines()
    b = EXT.read_text(encoding="utf-8").splitlines()
    record = json.loads((SOLVER / "logs/axisn_exact_d18_m9_87333babe8007f97.json").read_text(encoding="utf-8"))
    preflight = json.loads((SOLVER / "logs/S5_D18_PREFLIGHT.json").read_text(encoding="utf-8"))
    assert sha256(EXT.read_bytes()).hexdigest() == record["input_sha256"]
    assert sha256(FLOORS.read_bytes()).hexdigest() == preflight["floor_source"]["source_sha256"]
    assert list(map(int, b[0].split())) == [18, 40, 10000, 9]
    assert list(map(int, a[0].split()))[:2] == [18, 40]
    assert a[2] == b[2]
    rates = list(map(int, b[2].split()))
    assert len(rates) == 10001 and rates[0] == 0
    factor = 34**17
    for i in range(1, 10001):
        assert (rates[i] - 1)**17 < factor * i**16 <= rates[i]**17, i

    base_gamma = list(map(int, a[1].split()))
    extension_gamma = list(map(int, b[1].split()))
    assert len(base_gamma) == 6 and len(extension_gamma) == 4
    assert extension_gamma[0] == base_gamma[5]
    expected = base_gamma + extension_gamma[1:]
    count_by_shape = {1: 1000, 2: 10000}
    checked = []
    for n in range(1, 10):
        paths = count_by_shape.get(n, 1000)
        value, degree = gamma_units(n, paths)
        assert value == expected[n - 1] == preflight["gamma_boundaries"][n - 1]["upper_units"], n
        checked.append({"shape": n, "paths": paths, "degree": degree, "upper_units": value})

    roots = []
    for n in range(1, 10):
        p = OUT.parent / f"t170_d18_stage_{n}.txt"
        if p.exists():
            fields = dict(part.split("=", 1) for part in p.read_text(encoding="utf-8").strip().split()[2:])
            roots.append(int(fields["root_units"]))
    assert len(roots) == 9
    assert roots[5:] == [r["raw_upper_units"] for r in record["rows"]]
    floor_row = next(r for r in json.loads(FLOORS.read_text(encoding="utf-8"))["rows"] if r["d"] == 18)
    exact_floor = Fraction(int(floor_row["lower"]["n"]), int(floor_row["lower"]["d"]))
    assert exact_floor.numerator * 10**12 // exact_floor.denominator == 80065422991
    floor = Fraction(80065422991, 10**12)
    assert floor <= exact_floor
    axis = Fraction(record["rows"][-1]["raw_upper_units"], 9 * SCALE)
    margin = floor - axis
    assert axis == Fraction(788924918939, 9895604649984)
    assert margin == Fraction(822962185955923189, 2415919104000000000000) and margin > 0
    out = {"d": 18, "rate_checks": 10001, "base_input_sha256": sha256(BASE.read_bytes()).hexdigest(), "extension_input_sha256": sha256(EXT.read_bytes()).hexdigest(), "gamma_checks": checked, "recorded_roots": [r["raw_upper_units"] for r in record["rows"]], "own_roots_available": roots, "axis_upper": str(axis), "diagonal_floor": str(floor), "strict_margin": str(margin), "legacy_d20_floor_ignored": True}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "gamma_checks"}))


if __name__ == "__main__":
    main()
