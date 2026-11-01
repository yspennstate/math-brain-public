from fractions import Fraction
from itertools import product


def solve_fraction_system(A, b):
    A = [list(map(Fraction, row)) for row in A]
    b = list(map(Fraction, b))
    n = len(A)
    for col in range(n):
        pivot = next(r for r in range(col, n) if A[r][col] != 0)
        if pivot != col:
            A[col], A[pivot] = A[pivot], A[col]
            b[col], b[pivot] = b[pivot], b[col]
        piv = A[col][col]
        A[col] = [x / piv for x in A[col]]
        b[col] /= piv
        for r in range(n):
            if r == col:
                continue
            fac = A[r][col]
            if fac:
                A[r] = [A[r][j] - fac * A[col][j] for j in range(n)]
                b[r] -= fac * b[col]
    return b


def graph_from_edges(edges):
    V = sorted(set(sum(([a, b] for a, b in edges), [])))
    nbr = {v: [] for v in V}
    for a, b in edges:
        nbr[a].append(b)
        nbr[b].append(a)
    return V, nbr


def first_hit_probs(edges, boundary, start_after_step):
    V, nbr = graph_from_edges(edges)
    B = set(boundary)
    transient = [v for v in V if v not in B]
    idx = {v: k for k, v in enumerate(transient)}
    ans = {}
    for target in boundary:
        A = [[Fraction(int(r == c)) for c in range(len(transient))] for r in range(len(transient))]
        b = [Fraction(0) for _ in transient]
        for v in transient:
            r = idx[v]
            deg = len(nbr[v])
            for w in nbr[v]:
                p = Fraction(1, deg)
                if w in B:
                    if w == target:
                        b[r] += p
                else:
                    A[r][idx[w]] -= p
        x = solve_fraction_system(A, b) if transient else []
        if start_after_step in B:
            ans[target] = Fraction(int(start_after_step == target))
        else:
            ans[target] = x[idx[start_after_step]]
    return ans


def positive_excursion_types(edges, terminals):
    V, nbr = graph_from_edges(edges)
    s, t = terminals
    out = {}
    for x in terminals:
        for y in terminals:
            out[(x, y)] = Fraction(0)
        for w in nbr[x]:
            p_step = Fraction(1, len(nbr[x]))
            if w in terminals:
                out[(x, w)] += p_step
            else:
                hit = first_hit_probs(edges, terminals, w)
                for y in terminals:
                    out[(x, y)] += p_step * hit[y]
    return out


def excursion_mask_distribution(edges, terminals, start, end):
    V, nbr = graph_from_edges(edges)
    interiors = [v for v in V if v not in terminals]
    bit = {v: 1 << k for k, v in enumerate(interiors)}
    # State after the mandatory first step: (vertex, visited interior mask).
    transient = []
    index = {}
    for v in interiors:
        for mask in range(1 << len(interiors)):
            if mask & bit[v]:
                index[(v, mask)] = len(transient)
                transient.append((v, mask))
    # Absorption probabilities into requested end, stratified by final visited mask.
    result = {mask: Fraction(0) for mask in range(1 << len(interiors))}
    for final_mask in range(1 << len(interiors)):
        A = [[Fraction(int(r == c)) for c in range(len(transient))] for r in range(len(transient))]
        b = [Fraction(0) for _ in transient]
        for (v, mask), r in index.items():
            deg = len(nbr[v])
            for w in nbr[v]:
                p = Fraction(1, deg)
                if w in terminals:
                    if w == end and mask == final_mask:
                        b[r] += p
                else:
                    m2 = mask | bit[w]
                    A[r][index[(w, m2)]] -= p
        x = solve_fraction_system(A, b) if transient else []
        val = Fraction(0)
        for w in nbr[start]:
            p_step = Fraction(1, len(nbr[start]))
            if w in terminals:
                if w == end and final_mask == 0:
                    val += p_step
            else:
                val += p_step * x[index[(w, bit[w])]]
        result[final_mask] = val
    type_prob = sum(result.values())
    if type_prob:
        result = {m: p / type_prob for m, p in result.items() if p}
    else:
        result = {}
    return type_prob, result, interiors


def union_probability_of_masks(mask_distributions, full_mask):
    dist = {0: Fraction(1)}
    for md in mask_distributions:
        new = {}
        for a, pa in dist.items():
            for b, pb in md.items():
                new[a | b] = new.get(a | b, Fraction(0)) + pa * pb
        dist = new
    return dist.get(full_mask, Fraction(0))


def effective_resistance(edges, a, b):
    V, nbr = graph_from_edges(edges)
    unknown = [v for v in V if v != b]
    idx = {v: k for k, v in enumerate(unknown)}
    A = [[Fraction(0) for _ in unknown] for _ in unknown]
    rhs = [Fraction(0) for _ in unknown]
    for v in unknown:
        r = idx[v]
        A[r][r] = len(nbr[v])
        for w in nbr[v]:
            if w != b:
                A[r][idx[w]] -= 1
    rhs[idx[a]] = 1
    volts = solve_fraction_system(A, rhs)
    return volts[idx[a]]


def fmt(q):
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


# Two child networks in series, each with one pendant vertex that must be covered.
# H1 terminals L,M: L-u-M and pendant y at u.
# H2 terminals M,R: M-v-R and pendant z at v.
edges1 = [('L', 'u'), ('u', 'M'), ('u', 'y')]
edges2 = [('M', 'v'), ('v', 'R'), ('v', 'z')]
edges = edges1 + edges2

q1 = positive_excursion_types(edges1, ('L', 'M'))
q2 = positive_excursion_types(edges2, ('M', 'R'))
_, nbr1 = graph_from_edges(edges1)
_, nbr2 = graph_from_edges(edges2)
d1, d2 = len(nbr1['M']), len(nbr2['M'])
alpha, beta = Fraction(d1, d1 + d2), Fraction(d2, d1 + d2)
r = alpha * q1[('M', 'M')] + beta * q2[('M', 'M')]

# The series formulas at all marker variables = 1.
p_LL_formula = q1[('L', 'L')] + q1[('L', 'M')] * (1 / (1 - r)) * alpha * q1[('M', 'L')]
p_LR_formula = q1[('L', 'M')] * (1 / (1 - r)) * beta * q2[('M', 'R')]

q = positive_excursion_types(edges, ('L', 'R'))
p_LL_direct = q[('L', 'L')]
p_LR_direct = q[('L', 'R')]
assert p_LL_formula == p_LL_direct
assert p_LR_formula == p_LR_direct

# Direct conditional law of a full outer L->R excursion.
p_outer, md_outer, ints_outer = excursion_mask_distribution(edges, ('L', 'R'), 'L', 'R')
assert p_outer == p_LR_direct
full_outer = (1 << len(ints_outer)) - 1
p_cover_direct = md_outer.get(full_outer, Fraction(0))

# Series-law reconstruction. For this example every successful L->R excursion has:
# one H1 L->M episode, then J>=0 M->M loops, each selecting child 1 or 2,
# then one H2 M->R episode. Conditional on being an M-loop, child choice is
# proportional to alpha*q1_MM and beta*q2_MM; here both are 1/2.
_, md1_LM, ints1 = excursion_mask_distribution(edges1, ('L', 'M'), 'L', 'M')
_, md1_MM, _ = excursion_mask_distribution(edges1, ('L', 'M'), 'M', 'M')
_, md2_MM, ints2 = excursion_mask_distribution(edges2, ('M', 'R'), 'M', 'M')
_, md2_MR, _ = excursion_mask_distribution(edges2, ('M', 'R'), 'M', 'R')
full1 = (1 << len(ints1)) - 1
full2 = (1 << len(ints2)) - 1

# Sum the geometric series exactly by augmenting the state with whether each child
# interior has been fully covered. The state space is four booleans collapsed here
# to two coverage flags. First apply mandatory LM episode in H1.
def coverage_flag_transition(state_dist, mask_dist, fullmask, which):
    out = {}
    for (c1, c2), ps in state_dist.items():
        for mask, pm in mask_dist.items():
            nc1, nc2 = c1, c2
            if which == 1 and mask == fullmask:
                nc1 = True
            if which == 2 and mask == fullmask:
                nc2 = True
            out[(nc1, nc2)] = out.get((nc1, nc2), Fraction(0)) + ps * pm
    return out

state0 = coverage_flag_transition({(False, False): Fraction(1)}, md1_LM, full1, 1)
# Let T be the stochastic map for one conditional M-loop. Solve the absorbing
# geometric mixture sum (1-r) * sum_{j>=0} r^j T^j applied to state0, then final MR.
states = [(False, False), (True, False), (False, True), (True, True)]
si = {s: i for i, s in enumerate(states)}
T = [[Fraction(0) for _ in states] for _ in states]
loop1_weight = alpha * q1[('M', 'M')] / r
loop2_weight = beta * q2[('M', 'M')] / r
for s in states:
    d1s = coverage_flag_transition({s: Fraction(1)}, md1_MM, full1, 1)
    d2s = coverage_flag_transition({s: Fraction(1)}, md2_MM, full2, 2)
    for s2, p in d1s.items():
        T[si[s]][si[s2]] += loop1_weight * p
    for s2, p in d2s.items():
        T[si[s]][si[s2]] += loop2_weight * p

# Row vector x = state0 * (1-r)(I-rT)^(-1). Solve transpose system.
A = [[Fraction(int(i == j)) - r * T[j][i] for j in range(4)] for i in range(4)]
b = [(1 - r) * state0.get(states[i], Fraction(0)) for i in range(4)]
x = solve_fraction_system(A, b)
pre_final = {states[i]: x[i] for i in range(4)}
post_final = coverage_flag_transition(pre_final, md2_MR, full2, 2)
p_cover_series = post_final.get((True, True), Fraction(0))
assert p_cover_series == p_cover_direct

R1 = effective_resistance(edges1, 'M', 'L')
R2 = effective_resistance(edges2, 'M', 'R')
escape_L = Fraction(1, d1 + d2) / R1
escape_R = Fraction(1, d1 + d2) / R2
assert 1 - r == escape_L + escape_R
n = len(set(sum(([a, b] for a, b in edges), [])))
generic_bound = Fraction(2, (n - 1) ** 2)
assert 1 - r >= generic_bound

print('q1 =', q1)
print('q2 =', q2)
print('alpha,beta =', fmt(alpha), fmt(beta))
print('shared-terminal loop probability r =', fmt(r))
print('outer p_LL formula/direct =', fmt(p_LL_formula), fmt(p_LL_direct))
print('outer p_LR formula/direct =', fmt(p_LR_formula), fmt(p_LR_direct))
print('direct P(full interior | outer LR) =', fmt(p_cover_direct))
print('series P(full interior | outer LR) =', fmt(p_cover_series))
print('R1,R2 =', fmt(R1), fmt(R2))
print('escape_L,escape_R,1-r =', fmt(escape_L), fmt(escape_R), fmt(1-r))
print('generic simple-graph lower bound 2/(n-1)^2 =', fmt(generic_bound))
print('EXACT_CHECK_PASS')
