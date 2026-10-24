"""Bounded exact arithmetic checks; these do not certify the infinite target."""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
gate = json.loads((ROOT / "COMPUTE_GATE.json").read_text(encoding="utf-8"))
assert Path(gate["outputs_root"]).resolve() == ROOT
assert gate["max_workers"] == 1 and not gate["network"] and not gate["gpu"]
started = time.monotonic()
states = 0

def budget():
    assert time.monotonic() - started < gate["max_wall_seconds"]
    assert states <= gate["max_states"]

def mask_weight(mask, parameter):
    return parameter ** sum(mask) * (1 - parameter) ** (len(mask) - sum(mask))

# The full retained four-edge configuration must have product law, not just
# the correct one-edge marginals. Check all 256 (X,Y) pairs exactly.
p, q = Fraction(3, 5), Fraction(2, 3)
masks = tuple(product((0, 1), repeat=4))
retained = defaultdict(Fraction)
for x in masks:
    for y in masks:
        z = tuple(a * b for a, b in zip(x, y))
        retained[z] += mask_weight(x, p) * mask_weight(y, q)
        states += 1
assert all(retained[z] == mask_weight(z, p * q) for z in masks)
assert sum(retained.values()) == 1
budget()

# Shared-edge increasing events show that multiplying marginals can fail.
joint = marginal_a = marginal_b = Fraction(0)
for bits in product((0, 1), repeat=3):
    weight = Fraction(1, 8)
    a, b = bits[0] and bits[1], bits[1] and bits[2]
    marginal_a += weight * bool(a)
    marginal_b += weight * bool(b)
    joint += weight * bool(a and b)
    states += 1
assert joint == Fraction(1, 8)
assert marginal_a * marginal_b == Fraction(1, 16)

# For d=1,R=1 enumerate every ordering of the five labels that are read.
open_count = 0
for ranks in permutations(range(5)):
    labels = dict(zip(range(-2, 3), ranks))
    winners = {x: min(range(x - 1, x + 2), key=labels.__getitem__) for x in (-1, 0, 1)}
    open_count += winners[-1] == winners[0] == winners[1]
    states += 1
assert open_count == 24

def box(center, radius):
    return set(product(*(range(a - radius, a + radius + 1) for a in center)))

# Direct finite-set counts check the geometric quantities in the exact formula.
controls = []
for d, radius in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 1)):
    origin = (0,) * d
    centers = [origin]
    for coordinate in range(d):
        for sign in (-1, 1):
            centers.append(tuple(sign if j == coordinate else 0 for j in range(d)))
    boxes = [box(c, radius) for c in centers]
    intersection = set.intersection(*boxes)
    union = set.union(*boxes)
    expected_intersection = (2 * radius - 1) ** d
    expected_union = (2 * radius + 1) ** d + 2 * d * (2 * radius + 1) ** (d - 1)
    assert len(intersection) == expected_intersection
    assert len(union) == expected_union
    probability = Fraction(len(intersection), len(union))
    controls.append({"d": d, "R": radius, "probability": str(probability)})
    states += len(union)
    budget()

radius = 399
probability = Fraction((2 * radius - 1) ** 2, (2 * radius + 1) ** 2 + 4 * (2 * radius + 1))
assert probability > Fraction(99, 100)
budget()
tree_bounds = []
for degree in range(3, 9):
    b = degree - 1
    c = Fraction(b - 1, 2 * b) * Fraction(b - 1, b) ** (b - 2)
    old_bound = degree * (1 + 2 / c)
    tightened_bound = degree / c
    assert 0 < c < 1 and tightened_bound < old_bound
    tree_bounds.append({"D": degree, "c_b": str(c), "paired_bound": str(old_bound), "tightened_bound": str(tightened_bound)})
    states += 1
budget()
result = {
    "status": "PASS",
    "command": "python -X utf8 ~/brain_workers/w433/check_obstructions.py",
    "scope": "exact finite arithmetic; not a formal proof or a proof of P0043",
    "thinning_input_states": 256,
    "thinning_output_masks_checked": 16,
    "shared_edge_joint": str(joint),
    "shared_edge_product": str(marginal_a * marginal_b),
    "one_dimensional_orderings": 120,
    "one_dimensional_open_orderings": open_count,
    "geometric_controls": controls,
    "regular_tree_constant_comparison": tree_bounds,
    "degree_3_bound_reduction_fraction": str(1 - Fraction(12, 27)),
    "degree_3_old_parameter_interval": [0.25, 0.5],
    "degree_3_new_parameter_interval": [0.0, 0.5],
    "high_density_obstruction": {
        "d": 2, "R": radius,
        "one_site_probability_exact": str(probability),
        "one_site_probability_decimal": float(probability),
        "component_size_upper_bound": (2 * radius + 1) ** 2,
        "dependence_range_sup_norm": 2 * radius + 2,
        "conservative_dependence_range_graph_distance": 4 * (radius + 1),
        "percolates": False,
        "percolates_basis": "written component-color argument in ATTEMPT.md; not inferred from finite arithmetic"
    },
    "enumerated_states_total": states,
    "elapsed_seconds": time.monotonic() - started
}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
