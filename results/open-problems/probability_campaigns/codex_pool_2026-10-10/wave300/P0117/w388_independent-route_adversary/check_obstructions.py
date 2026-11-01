"""Small exact diagnostics, not a simulation or certificate for the open target."""
from fractions import Fraction
import heapq
import itertools
import json
from pathlib import Path
import random
import time

ROOT = Path(__file__).resolve().parent
GATE = {"fresh_gate": "w388-exact-diagnostics-20261010-v1", "max_cpu_seconds": 3,
        "max_wall_seconds": 30, "max_vertices_per_graph": 361, "bounded_weight_seeds": 6,
        "no_gpu": True, "purpose": "check exact witness counts and finite deterministic examples only"}
wall, cpu = time.monotonic(), time.process_time()

def guard():
    if time.process_time() - cpu > GATE["max_cpu_seconds"] or time.monotonic() - wall > GATE["max_wall_seconds"]:
        raise RuntimeError("fresh compute gate exceeded")

def edge(x, y):
    return tuple(sorted((x, y)))

def distance(radius, weights, start, default=30):
    assert (2*radius+1)**2 <= GATE["max_vertices_per_graph"]
    d, queue = {start: 0}, [(0, start)]
    while queue:
        value, x = heapq.heappop(queue)
        if value != d[x]:
            continue
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            y = (x[0]+dx, x[1]+dy)
            if max(abs(y[0]),abs(y[1])) > radius:
                continue
            candidate = value + weights.get(edge(x,y), default)
            if candidate < d.get(y, float("inf")):
                d[y] = candidate
                heapq.heappush(queue, (candidate,y))
    guard()
    return d

output = {"gate": GATE, "command": "python -X utf8 check_obstructions.py", "cases": []}
for n in (2,4,8,16,32):
    # Disjoint equal cells of [0,1), represented by their exact measures.
    pair_measure = Fraction(1,n*n)
    union_measure = n*n*pair_measure
    assert union_measure == 1
    output["cases"].append({"case": "endpoint-partition", "n": n, "witnesses": n*n,
        "max_marginal": str(pair_measure), "union": str(union_measure),
        "naive_union_upper": str(n*n*pair_measure)})
    # Each of 4n cells is assigned to a pair of distinct boundary vertices.
    ray_measure = Fraction(1,4*n)
    mean_incidence = 8*n*ray_measure
    shell_bound = Fraction(1,2)*mean_incidence
    assert mean_incidence == 2 and shell_bound == 1
    output["cases"].append({"case": "paired-shell-partition", "n": n, "boundary_vertices":8*n,
        "max_marginal": str(ray_measure), "union": "1", "mean_incidence": str(mean_incidence),
        "shell_bound": str(shell_bound)})

unit_pairs = 0
for i in range(-3,4):
    d = distance(3, {}, (i,0), default=1)
    for j in range(i+1,4):
        assert d[(j,0)] == j-i
        unit_pairs += 1
output["unit_weight_horizontal_pairs"] = unit_pairs

localization_pairs = 0
boundary = [(x,y) for x in range(-1,2) for y in range(-1,2) if max(abs(x),abs(y))==1]
for seed in range(GATE["bounded_weight_seeds"]):
    rng = random.Random(seed)
    weights = {}
    for x in itertools.product(range(-9,10), repeat=2):
        for step in ((1,0),(0,1)):
            y = (x[0]+step[0],x[1]+step[1])
            if max(abs(y[0]),abs(y[1])) <= 9:
                weights[edge(x,y)] = rng.choice((2,3))
    # n=1,a=2,b=3: the proved deterministic radius is R=7.
    for i,x in enumerate(boundary):
        d7, d9 = distance(7,weights,x), distance(9,weights,x)
        for y in boundary[i+1:]:
            assert d7[y] == d9[y]
            localization_pairs += 1
output["bounded_localization_pair_checks"] = localization_pairs
output["localization_scope"] = "Finite B7 versus B9 checks only; the deterministic proof in ATTEMPT.md establishes global equality."

u, v = (-1,0), (1,0)
detour = [u,(-2,0),(-2,1),(-2,2),(-1,2),(0,2),(1,2),(2,2),(2,1),(2,0),v]
weights = {edge(u,(0,0)):10, edge((0,0),v):10}
for x,y in zip(detour,detour[1:]):
    weights[edge(x,y)] = 1
inside = distance(1,weights,u)[v]
outside = distance(3,weights,u)[v]
assert inside == 20 and outside == 10
output["false_box_geodesic_example"] = {"cost_inside_B1":inside,"cost_inside_B3":outside,
    "root_path_cost":20,"explicit_detour_cost":10,"detour":detour}
delta, pa, pb = Fraction(1,16), Fraction(1,4), Fraction(1,4)
# G is uniform[0,1], low=[0,1/4], middle=(1/4,3/4), high=[3/4,1].
output_masses = {"low":pa-delta, "middle":Fraction(1,2), "high":pb+delta}
raised_joint = {"low":Fraction(0), "middle":Fraction(0), "high":delta}
posterior_checks = selector_checks = 0
for state1,state2 in itertools.product(output_masses,repeat=2):
    states = (state1,state2)
    denominator = output_masses[state1]*output_masses[state2]
    theta = [raised_joint[s]/output_masses[s] for s in states]
    for flag1,flag2 in itertools.product((0,1),repeat=2):
        flags = (flag1,flag2)
        numerator = Fraction(1)
        kernel = Fraction(1)
        for s,t,flag in zip(states,theta,flags):
            numerator *= raised_joint[s] if flag else output_masses[s]-raised_joint[s]
            kernel *= t if flag else 1-t
        assert numerator/denominator == kernel
        posterior_checks += 1
    chosen = 0 if state1=="high" else 1
    selected_raise_mass = Fraction(0)
    for flags in itertools.product((0,1),repeat=2):
        if not flags[chosen]:
            continue
        numerator = Fraction(1)
        for s,flag in zip(states,flags):
            numerator *= raised_joint[s] if flag else output_masses[s]-raised_joint[s]
        selected_raise_mass += numerator/denominator
    assert selected_raise_mass == theta[chosen]
    selector_checks += 1
output["posterior_product_checks"] = posterior_checks
output["output_measurable_selector_checks"] = selector_checks
output["posterior_example"] = {"law":"uniform[0,1]", "a0":"1/4", "b0":"3/4", "delta":"1/16",
    "theta_on_high_output":str(delta/(pb+delta)), "conditioning":"the entire individual modified output; no other site's output"}
output["wall_seconds"] = round(time.monotonic()-wall,6)
output["cpu_seconds"] = round(time.process_time()-cpu,6)
output["scope"] = "No asymptotic iid-FPP theorem, formal proof, or live brain improvement is inferred from these controls."
guard()
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(output,indent=2), encoding="utf-8")
print(json.dumps({"partition_cases":len(output["cases"]),"unit_pairs":unit_pairs,
    "bounded_pair_checks":localization_pairs,"false_box_example":[inside,outside],
    "posterior_product_checks":posterior_checks,"selector_checks":selector_checks,
    "wall_seconds":output["wall_seconds"],"cpu_seconds":output["cpu_seconds"]}))
