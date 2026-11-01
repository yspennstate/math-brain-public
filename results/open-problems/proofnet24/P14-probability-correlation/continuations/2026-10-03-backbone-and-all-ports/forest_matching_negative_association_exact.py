"""Exact matching-law, increasing-event, and conditioning checks for NA.

The matching configuration masses come from explicit three-spoke subset
transitions. They are compared with the forced-subset/Bernoulli representation.
All NA checks use exact integers after clearing a common denominator.
"""
from fractions import Fraction as F
from itertools import product
from math import lcm
from pathlib import Path
import json


STATES = ((0, 1, 2), (0, 0, 1), (0, 1, 0), (0, 1, 1), (0, 0, 0))


def canonical(state):
    names = {}
    return tuple(names.setdefault(v, len(names)) for v in state)


def terminal(frontier, row, columns):
    out = {}
    for state, mass in frontier.items():
        for chosen in range(8):
            selected = [i for i in range(3) if chosen >> i & 1]
            labels = [state[i] for i in selected]
            if len(labels) != len(set(labels)):
                continue
            touched = set(labels)
            target = canonical([labels[0] if x in touched else x for x in state]) if labels else state
            value = mass
            for i in selected:
                value *= row * columns[i]
            out[target] = out.get(target, F(0)) + value
    return out


def matching_table(rows, columns, core, activities):
    """All matching indicators, direct subset-transition coefficients."""
    rows, columns, core, activities = [list(map(F, v)) for v in (rows, columns, core, activities)]
    p, q, r = core
    k = len(activities)
    weights = []
    for matching_mask in range(1 << k):
        frontier = dict(zip(STATES, (F(1), p, q, r, p*q+p*r+q*r)))
        factor = F(1)
        for i, activity in enumerate(activities):
            a, b = rows[2*i:2*i+2]
            if matching_mask >> i & 1:
                factor *= activity
                frontier = terminal(frontier, a+b, columns)
            else:
                frontier = terminal(terminal(frontier, a, columns), b, columns)
        for row in rows[2*k:]:
            frontier = terminal(frontier, row, columns)
        weights.append(factor * sum(frontier.values(), F(0)))
    return weights


def forced_parameters(rows, columns, core, activities):
    rows, columns, core, activities = [list(map(F, v)) for v in (rows, columns, core, activities)]
    B, J = sum(columns), columns[0]*columns[1]*columns[2]
    p, q, r = core
    b0, b1, b2 = columns
    S = 1+p+q+r+p*q+p*r+q*r
    L = b0*b1+b0*b2+b1*b2+p*b2*(b0+b1)+q*b1*(b0+b2)+r*b0*(b1+b2)
    d = lambda x: 1+B*x
    alpha = lambda x: x*x/d(x)
    gamma = lambda x: x**3/d(x)**2
    U, G = sum(map(alpha, rows)), sum(map(gamma, rows))
    A = S+L*U+J*G+B*J*U*U
    M, K = L+2*B*J*U, 2*B*J
    theta, t, h = [], [], []
    for i, activity in enumerate(activities):
        a, b = rows[2*i:2*i+2]
        delta = alpha(a+b)-alpha(a)-alpha(b)
        epsilon = gamma(a+b)-gamma(a)-gamma(b)
        c = d(a+b)/(d(a)*d(b))
        theta.append(c*activity/(1+c*activity))
        t.append(delta*theta[-1])
        h.append(M+J*epsilon/delta+B*J*delta)
        assert 0 < delta < 1/B**2
        assert 0 < epsilon/delta < 2/B
    assert min(h)**2 > K*A
    assert max(h) < 2*min(h)
    return A, K, theta, t, h


def forced_bernoulli_table(A, K, theta, t, h):
    k = len(t)
    y = [F(0)] * (1 << k)
    y[0] = A
    for i in range(k):
        y[1 << i] = h[i]*t[i]
        for j in range(i+1, k):
            y[(1 << i)|(1 << j)] = K*t[i]*t[j]
    normalizer = sum(y)
    output = [F(0)] * (1 << k)
    for selected, weight in enumerate(y):
        if not weight:
            continue
        for outcome in range(1 << k):
            if selected & ~outcome:
                continue
            value = weight/normalizer
            for i in range(k):
                if not selected >> i & 1:
                    value *= theta[i] if outcome >> i & 1 else 1-theta[i]
            output[outcome] += value
    return output, y


UPSETS = {0: [0, 1]}


def upsets(n):
    if n not in UPSETS:
        half = 1 << (n-1)
        out = []
        previous = upsets(n-1)
        for low in previous:
            for high in previous:
                if not low & ~high:
                    out.append(low | (high << half))
        UPSETS[n] = out
    return UPSETS[n]


def clear_denominators(weights):
    denominator = lcm(*(w.denominator for w in weights))
    return [int(w*denominator) for w in weights]


def na_event_check(weights):
    n = (len(weights)-1).bit_length()
    Z = sum(weights)
    full = (1 << (1 << n))-1
    lifted = {}
    masses = {0: 0, full: Z}

    def event_mask(block, event):
        key = (block, event)
        if key not in lifted:
            indices = [i for i in range(n) if block >> i & 1]
            mask = 0
            for outcome in range(1 << n):
                local = sum(((outcome >> index)&1) << j for j, index in enumerate(indices))
                if event >> local & 1:
                    mask |= 1 << outcome
            lifted[key] = mask
        return lifted[key]

    def mass(mask):
        if mask not in masses:
            masses[mask] = sum(weights[i] for i in range(1 << n) if mask >> i & 1)
        return masses[mask]

    count = 0
    for allocation in product(range(3), repeat=n):
        left = sum(1 << i for i, a in enumerate(allocation) if a == 1)
        right = sum(1 << i for i, a in enumerate(allocation) if a == 2)
        if not left or not right:
            continue
        for e in upsets(left.bit_count()):
            if e in (0, (1 << (1 << left.bit_count()))-1):
                continue
            E = event_mask(left, e)
            for f in upsets(right.bit_count()):
                if f in (0, (1 << (1 << right.bit_count()))-1):
                    continue
                Fmask = event_mask(right, f)
                assert mass(E)*mass(Fmask) >= Z*mass(E & Fmask), (n, allocation, e, f)
                count += 1
    return count


def conditional_na_check(weights):
    n = (len(weights)-1).bit_length()
    conditionings, events = 0, 0
    for condition in product((-1, 0, 1), repeat=n):
        free = [i for i, c in enumerate(condition) if c == -1]
        conditional = [0] * (1 << len(free))
        for outcome, weight in enumerate(weights):
            if any(c != -1 and ((outcome >> i)&1) != c for i, c in enumerate(condition)):
                continue
            local = sum(((outcome >> i)&1) << j for j, i in enumerate(free))
            conditional[local] += weight
        if not sum(conditional):
            continue
        events += na_event_check(conditional)
        conditionings += 1
    return conditionings, events


def main():
    graph_cases = [
        ([1,2,3,4,5,6], [2,3,5], [2,3,5], [F(1,2),2,F(3,5)]),
        ([F(j+1,j+2) for j in range(8)], [F(2,3),F(3,4),F(5,7)],
         [F(1,3),0,F(2,5)], [F(2,3),F(4,5),F(6,7),F(8,9)]),
        ([F(1,100)]*10, [1,1,1], [0,0,0], [1,2,3,4,5]),
        ([1,2,1,3,2,4,3,5,7], [1,2,4], [1,3,2], [F(1,3),2,7,11]),
    ]
    output = {"arithmetic": "exact Fraction / denominator-cleared integers",
              "complete_matching_law_checks": [], "forced_subset_checks": []}
    for rows, columns, core, activities in graph_cases:
        actual = matching_table(rows, columns, core, activities)
        parameters = forced_parameters(rows, columns, core, activities)
        represented, y = forced_bernoulli_table(*parameters)
        normalizer = sum(actual)
        assert represented == [w/normalizer for w in actual]
        integers = clear_denominators(actual)
        conditionings, events = conditional_na_check(integers)
        y_events = na_event_check(clear_denominators(y))
        output["complete_matching_law_checks"].append({
            "rows": list(map(str, rows)), "columns": list(map(str, columns)),
            "core": list(map(str, core)), "matching_activities": list(map(str, activities)),
            "matching_configurations": len(actual), "matching_weights": list(map(str, actual)),
            "forced_representation_exact": True, "conditional_laws": conditionings,
            "all_disjoint_increasing_event_checks": events,
            "forced_subset_increasing_event_checks": y_events})
        print("Exact conditional NA / forced-law check passed for " + str(len(activities)) + " matching edges.", flush=True)

    for A, K, t, h in [(F(1),F(2),[F(1),F(2),F(3),F(4),F(5),F(6)],[F(2),F(3),F(2),F(5,2),F(3),F(2)]),
                        (F(4),F(1),[F(1),F(2),F(3),F(4),F(5)],[F(2),F(2),F(4),F(3),F(2)])]:
        weights = [F(0)] * (1 << len(t))
        weights[0] = A
        for i in range(len(t)):
            weights[1 << i] = h[i]*t[i]
            for j in range(i+1, len(t)):
                weights[(1 << i)|(1 << j)] = K*t[i]*t[j]
        assert min(h)**2 >= K*A and max(h) <= 2*min(h)
        events = na_event_check(clear_denominators(weights))
        output["forced_subset_checks"].append({"indices": len(t), "A": str(A), "K": str(K),
                                              "all_increasing_event_checks": events})

    # A real-stability shortcut is not implied by NA. Five equal tiny rows
    # yield a matching-diagonal quadratic with strictly negative discriminant.
    rows = [F(1,100)]*10
    A, K, theta, t, h = forced_parameters(rows, [1,1,1], [0,0,0], [1]*5)
    Bsum, J = F(3), F(1)
    a = rows[0]
    delta = (2*a)**2/(1+Bsum*2*a)-2*a*a/(1+Bsum*a)
    discriminant = delta**2 * 5 * (5*h[0]**2 - 12*4*A)
    assert discriminant < 0
    output["strong_Rayleigh_not_claimed"] = {"matching_edges": 5, "row_activity": "1/100",
                                              "diagonal_theta_quadratic_discriminant": str(discriminant)}
    Path(__file__).with_name("forest_matching_negative_association_exact_results.json").write_text(json.dumps(output, indent=2)+"\n")
    print("All exact matching-law, NA, conditioning and scope checks passed.")


if __name__ == "__main__":
    main()
