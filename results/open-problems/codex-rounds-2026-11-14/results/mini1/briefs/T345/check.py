#!/usr/bin/env python3
"""Small independent checks for PROOF.md; standard library only."""
import collections
import json
import math
import os
from pathlib import Path
import random
import resource
import time

for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Run under nice -n 15 or lower priority"
RESOURCE_GUARDS = {}
for limit, amount, label in ((resource.RLIMIT_AS, 768*1024**2, "address_space"),
                             (resource.RLIMIT_CPU, 90, "cpu_seconds")):
    try:
        soft, hard = resource.getrlimit(limit)
        resource.setrlimit(limit, (min(soft, amount), hard))
        RESOURCE_GUARDS[label] = "soft limit installed"
    except (ValueError, OSError) as error:
        RESOURCE_GUARDS[label] = str(error)
BASE = Path(__file__).resolve().parent
rng = random.Random(34520261114)


def norm(v):
    return math.sqrt(sum(x*x for x in v))


def simpson(fun, left, right, steps=6000):
    step = (right-left)/steps
    value = fun(left)+fun(right)
    value += 4*sum(fun(left+step*i) for i in range(1, steps, 2))
    value += 2*sum(fun(left+step*i) for i in range(2, steps, 2))
    return value*step/3


def geometry():
    worst = 0.0
    cases = 0
    for d in (2, 3, 7, 31):
        for j in range(80):
            t = rng.uniform(-2, 2)
            w = [rng.gauss(0, 1) for _ in range(d-1)]
            if j % 10 == 0:
                w = [0.0]*(d-1)
            r = norm(w)
            theta = [v/r for v in w] if r else [1.0]+[0.0]*(d-2)
            s = rng.uniform(-2, 2)
            rp = 0.0 if j % 11 == 0 else rng.uniform(0, 4)
            u = [rp*a for a in theta]
            original = math.sqrt((s-t)**2+sum((a-b)**2 for a, b in zip(w, u)))
            quotient = math.hypot(s-t, r-rp)
            worst = max(worst, abs(original-quotient))
            assert abs(original-quotient) < 1e-12
            # An arbitrary direction can never beat the aligned direction.
            rand_dir = [rng.gauss(0, 1) for _ in w]
            size = norm(rand_dir)
            uu = [rp*a/size for a in rand_dir]
            other = math.sqrt((s-t)**2+sum((a-b)**2 for a, b in zip(w, uu)))
            assert quotient <= other+1e-12
            cases += 1
    # Negative control: this quotient is not 1-Lipschitz for l_infinity.
    radial_change = math.hypot(1.1, 0.1)-1
    assert radial_change > 0.1
    return {"cases": cases, "maximum_aligned_distance_error": worst,
            "linfinity_negative_control_radial_change": radial_change,
            "linfinity_perturbation": 0.1}


def finite_slices():
    # Four angular directions in the perpendicular plane; 3 quotient nodes.
    quotient = [(-0.6, 0.5), (0.3, 0.5), (0.1, 1.5)]
    theta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    points = [(t, r*a, r*b) for t, r in quotient for a, b in theta]
    weights = [[6, 1, 1], [1, 3, 4]]
    denominator = sum(sum(w) for w in weights)*len(theta)
    rows = []
    for radius in (0.0, 0.25, 0.75, 1.1, 2.0):
        neighbors = []
        for p in points:
            mask = 0
            for j, z in enumerate(points):
                if sum((a-b)**2 for a, b in zip(p, z)) <= radius**2+1e-13:
                    mask |= 1 << j
            neighbors.append(mask)

        def score(mask):
            correct = 0
            for i, nmask in enumerate(neighbors):
                hit = mask & nmask
                if hit == 0:
                    correct += weights[0][i//4]
                if hit == nmask:
                    correct += weights[1][i//4]
            return correct

        unrestricted = max(score(mask) for mask in range(1 << len(points)))
        invariant_masks = [sum((15 << (4*i)) for i in range(3) if mask >> i & 1)
                           for mask in range(8)]
        invariant = max(score(mask) for mask in invariant_masks)
        assert unrestricted == invariant
        rows.append({"radius": radius, "unrestricted_error_numerator": denominator-unrestricted,
                     "invariant_error_numerator": denominator-invariant,
                     "denominator": denominator, "classifiers_enumerated": 4096})
    # Negative control: if the label depends on angle at a single orbit,
    # radius-zero angular classification is perfect but invariance costs 1/2.
    angle_labels = [0, 0, 1, 1]
    def angular_risk(mask):
        return sum((mask >> i & 1) != y for i, y in enumerate(angle_labels))/4
    negative = {"unrestricted_risk": min(angular_risk(mask) for mask in range(16)),
                "invariant_risk": min(angular_risk(0), angular_risk(15))}
    assert negative["unrestricted_risk"] < negative["invariant_risk"]
    return {"common_angular_law_cases": rows, "label_dependent_angle_negative_control": negative}


def flow_independent(left, right, edges, return_sets=False):
    n, m = len(left), len(right)
    total = sum(left)+sum(right)
    source, sink = n+m, n+m+1
    count = n+m+2
    residual = [[0]*count for _ in range(count)]
    for i, w in enumerate(left):
        residual[source][i] = w
    for j, w in enumerate(right):
        residual[n+j][sink] = w
    for i, j in edges:
        residual[i][n+j] = total+1
    flow = 0
    while True:
        parent = [-1]*count
        parent[source] = source
        queue = collections.deque([source])
        while queue:
            u = queue.popleft()
            for v, cap in enumerate(residual[u]):
                if cap > 0 and parent[v] < 0:
                    parent[v] = u
                    queue.append(v)
        if parent[sink] < 0:
            break
        v, increment = sink, total+1
        while v != source:
            u = parent[v]
            increment = min(increment, residual[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= increment
            residual[v][u] += increment
            v = u
        flow += increment
    chosen_left = {i for i in range(n) if parent[i] >= 0}
    chosen_right = {j for j in range(m) if parent[n+j] < 0}
    assert not any(i in chosen_left and j in chosen_right for i, j in edges)
    weight = sum(left[i] for i in chosen_left)+sum(right[j] for j in chosen_right)
    assert weight == total-flow
    return (weight, chosen_left, chosen_right) if return_sets else weight


def graph_checks():
    records = []
    for trial in range(80):
        n = 5
        centers = [(rng.randrange(4), rng.randrange(4)) for _ in range(n)]
        threshold_sq = (0, 1, 2, 4, 8, 100)[trial % 6]
        edges = [(i, j) for i, x in enumerate(centers) for j, y in enumerate(centers)
                 if sum((a-b)**2 for a, b in zip(x, y)) <= threshold_sq]
        left = [rng.randrange(8) for _ in range(n)]
        right = [rng.randrange(8) for _ in range(n)]
        weights = left+right
        brute = -1
        for mask in range(1 << (2*n)):
            if any((mask >> i & 1) and (mask >> (n+j) & 1) for i, j in edges):
                continue
            brute = max(brute, sum(w for i, w in enumerate(weights) if mask >> i & 1))
        flowed = flow_independent(left, right, edges)
        assert flowed == brute
        records.append({"trial": trial, "edges": len(edges), "maximum_weight": brute})
    # Two centers separated by 1.5 at radius 1 have intersecting attack balls.
    correct = flow_independent([1], [1], [(0, 0)])
    wrong = flow_independent([1], [1], [])
    assert correct == 1 and wrong == 2
    return {"cases": len(records), "classifiers_per_case": 1024,
            "records": records, "omitting_factor_two_negative_control":
            {"correct_independent_weight": correct, "incorrect_weight": wrong}}


def density_and_kl():
    chi_rows = []
    for k in (1, 2, 4, 9):
        scale = 1.3
        constant = 1/(2**(k/2-1)*math.gamma(k/2)*scale**k)
        def density(r):
            return constant*r**(k-1)*math.exp(-r*r/(2*scale*scale))
        upper = scale*(math.sqrt(k)+12)
        mass = simpson(density, 0, upper)
        second = simpson(lambda r: r*r*density(r), 0, upper)
        assert abs(mass-1) < 1e-8
        assert abs(second-k*scale*scale) < 1e-7
        chi_rows.append({"chi_degrees": k, "integrated_mass": mass,
                         "integrated_second_moment": second, "exact_second_moment": k*scale*scale})
    kl_rows = []
    for mu, sigma, a in ((0.0, 1.0, 1.01), (3.0, 0.7, 1.4), (-2.0, 2.0, 2.0)):
        qm, qs = mu/a, sigma/a
        def integrand(g):
            x = qm+qs*g
            log_ratio = math.log(sigma/qs)+(x-mu)**2/(2*sigma*sigma)-g*g/2
            return math.exp(-g*g/2)/math.sqrt(2*math.pi)*log_ratio
        integrated = simpson(integrand, -12, 12)
        closed = 0.5*(a**-2-1+2*math.log(a)+(mu/sigma)**2*(1-1/a)**2)
        assert abs(integrated-closed) < 1e-11
        kl_rows.append({"mu": mu, "sigma": sigma, "a": a,
                        "integrated_log_density_ratio": integrated, "formula": closed})
    scalar_ratio = 0.0
    fit_ratio = 0.0
    for i in range(1, 1001):
        t = i/1000
        a = 1+t
        value = a**-2-1+2*math.log1p(t)
        scalar_ratio = max(scalar_ratio, value/(2*t*t))
        assert value <= 2*t*t+1e-14
    for d in (1, 2, 10, 100, 10000):
        for b in (0.001, 0.01, 0.125):
            for sign in (-1, 1):
                v = sign*b/math.sqrt(d)
                q = 1+v
                kl = 0.5*(d*(math.log1p(v)-v/q)+b*b/q)
                fit_ratio = max(fit_ratio, kl/(2*b*b))
                assert kl <= 2*b*b+1e-14
    return {"chi_integrals": chi_rows, "independent_kl_integrals": kl_rows,
            "maximum_dilation_scalar_bound_ratio": scalar_ratio,
            "maximum_fit_kl_bound_ratio": fit_ratio}


def interval_check():
    # An independent end-to-end check of (8), using exact normal CDFs and
    # interval unions instead of empirical risk on the training grid.
    cdf = lambda x: 0.5*math.erfc(-x/math.sqrt(2))
    mean, radius, h, bound, n = 2.0, 0.25, 0.2, 6.0, 30
    width = 2*bound/n
    centers = [-bound+(i+0.5)*width for i in range(n)]
    true = []
    for sign in (1, -1):
        true.append([0.5*(cdf(-bound+(i+1)*width-sign*mean)
                          -cdf(-bound+i*width-sign*mean)) for i in range(n)])
    denominator = 1000000
    counts = [[round(denominator*w) for w in row] for row in true]
    delta = sum(abs(counts[y][i]/denominator-true[y][i])
                for y in (0, 1) for i in range(n))
    edges = [(i, j) for i in range(n) for j in range(n)
             if abs(centers[i]-centers[j]) <= 2*(radius+h)+1e-12]
    _, positive, _ = flow_independent(counts[0], counts[1], edges, True)

    def merge(intervals):
        result = []
        for left, right in sorted(intervals):
            if result and left <= result[-1][1]:
                result[-1][1] = max(right, result[-1][1])
            else:
                result.append([left, right])
        return result

    intervals = merge([(centers[i]-radius-h, centers[i]+radius+h) for i in positive])
    eroded = [(left+radius, right-radius) for left, right in intervals
              if right-left >= 2*radius]
    expanded = merge([(left-radius, right+radius) for left, right in intervals])
    correct_positive = sum(cdf(right-mean)-cdf(left-mean) for left, right in eroded)
    wrong_negative = sum(cdf(right+mean)-cdf(left+mean) for left, right in expanded)
    risk = 0.5*(1-correct_positive+wrong_negative)
    tail = 1-sum(sum(row) for row in true)
    comparison = cdf(radius+2*h-mean)
    rhs = comparison+tail+2*delta
    assert risk <= rhs+1e-12
    assert risk < 0.1 and rhs < 0.1  # ensure this check is not vacuous
    return {"mean_separation": 2*mean, "source_radius": radius, "cell_radius": h,
            "positive_interval_union": intervals, "exact_robust_risk": risk,
            "optimal_risk_at_comparison_radius": comparison, "tail_mass": tail,
            "weight_l1_error": delta, "proved_upper_bound": rhs}


def main():
    started = time.monotonic()
    result = {"seed": 34520261114, "geometry": geometry(), "finite_symmetry": finite_slices(),
              "graph": graph_checks(), "density_and_kl": density_and_kl(),
              "continuous_interval_classifier": interval_check()}
    result["elapsed_seconds"] = time.monotonic()-started
    result["max_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result["inherited_nice"] = os.getpriority(os.PRIO_PROCESS, 0)
    result["resource_guards"] = RESOURCE_GUARDS
    assert result["max_rss_bytes"] < 1024**3
    assert result["elapsed_seconds"] < 1200
    result["status"] = "all assertions passed"
    (BASE/"checks.json").write_text(json.dumps(result, indent=2)+"\n")
    print("Geometry: 320 cases; exact aligned distances and lower bounds passed.")
    print("Symmetry: 5 finite problems, 4096 unrestricted classifiers each; optima agree.")
    print("Graph: 80 weighted problems, 1024 subsets each; max-flow equals exhaustive optimum.")
    print("Density/KL: 4 chi integrals, 3 independent KL integrals, scalar and fit bounds passed.")
    print("Continuous classifier: exact Gaussian interval risk satisfies the radius-slack bound.")
    print("Negative controls: angular dependence, l_infinity geometry, missing factor 2 detected.")
    print("Data: checks.json")
    print("Status: all assertions passed")
    print(f"Elapsed: {result['elapsed_seconds']:.3f} seconds; max RSS: {result['max_rss_bytes']} bytes")


if __name__ == "__main__":
    main()
