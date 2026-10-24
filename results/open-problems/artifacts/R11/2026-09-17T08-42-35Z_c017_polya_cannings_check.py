#!/usr/bin/env python3
"""
Exact self-check for R11 / I0054 / C017.

C017 is the Pólya-Cannings mutation-refinement hierarchy:
each forward Cannings generation allocates N offspring among N parents by a
Pólya urn started with one ball of each parent color.  Backward, r sampled
lineages choose parents by the same exchangeable Pólya sequence.  Rare marks
on ancestral lineages are refined into a discrete hierarchy.

This file checks only finite/algebraic claims.  The theorem-sized convergence
argument is written in the immutable R11 run report.
"""
from fractions import Fraction
from itertools import product
from collections import defaultdict, deque
from math import factorial, comb

CHECKS = 0

def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def falling(n, b):
    z = 1
    for j in range(b):
        z *= n-j
    return z

def rising(n, r):
    z = 1
    for j in range(r):
        z *= n+j
    return z

def set_partitions(seq):
    """All set partitions of a finite tuple, canonically represented."""
    seq = tuple(seq)
    if not seq:
        yield ()
        return
    first = seq[0]
    for p in set_partitions(seq[1:]):
        yield ((first,),) + p
        for j in range(len(p)):
            q = list(p)
            q[j] = tuple(sorted((first,) + q[j]))
            q = tuple(sorted(q, key=lambda b: b[0]))
            yield q

def unique_partitions(r):
    seen = set()
    out = []
    for p in set_partitions(tuple(range(r))):
        p = tuple(sorted((tuple(sorted(b)) for b in p), key=lambda b: b[0]))
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out

def polya_partition_prob(N, part):
    r = sum(len(b) for b in part)
    b = len(part)
    num = falling(N, b)
    for block in part:
        num *= factorial(len(block))
    return Fraction(num, rising(N, r))

def induced_partition(assignment):
    groups = defaultdict(list)
    for i, a in enumerate(assignment):
        groups[a].append(i)
    return tuple(sorted((tuple(v) for v in groups.values()), key=lambda b: b[0]))

def sequential_polya_assignment_prob(N, assignment):
    counts = [1]*N
    total = N
    p = Fraction(1)
    for a in assignment:
        p *= Fraction(counts[a], total)
        counts[a] += 1
        total += 1
    return p

def canon_partition(blocks):
    return tuple(sorted(
        [tuple(sorted(b)) for b in blocks if b],
        key=lambda x: (x[0], len(x), x)
    ))

def refine_partition(R, S):
    S = set(S)
    out = []
    for block in R:
        b = set(block)
        x = b & S
        y = b - S
        if x:
            out.append(tuple(sorted(x)))
        if y:
            out.append(tuple(sorted(y)))
    return canon_partition(out)

def coarsen_by_assignment(A, ass):
    groups = defaultdict(set)
    for block, parent in zip(A, ass):
        groups[parent].update(block)
    return canon_partition(groups.values())

def assignment_probs(N, r, model):
    out = {}
    for ass in product(range(N), repeat=r):
        if model == "polya":
            p = sequential_polya_assignment_prob(N, ass)
        elif model == "wf":
            p = Fraction(1, N**r)
        else:
            raise ValueError(model)
        out[ass] = p
    check(sum(out.values()) == 1, f"{model} assignment normalization N={N},r={r}")
    return out

def mark_outcomes(A, R, u):
    out = defaultdict(Fraction)
    r = len(A)
    for bits in product([0, 1], repeat=r):
        k = sum(bits)
        p = (u**k) * ((1-u)**(r-k))
        Rp = R
        for bit, block in zip(bits, A):
            if bit:
                Rp = refine_partition(Rp, block)
        out[Rp] += p
    check(sum(out.values()) == 1, "mark normalization")
    return out

def final_refinement_distribution(N, u, model, m=3):
    U = tuple(range(m))
    A0 = canon_partition([{i} for i in U])
    R0 = canon_partition([set(U)])

    seen = {(A0, R0)}
    q = deque([(A0, R0)])
    pa_cache = {}
    while q:
        A, R = q.popleft()
        if len(A) == 1:
            continue
        r = len(A)
        pa = pa_cache.setdefault(r, assignment_probs(N, r, model))
        md = mark_outcomes(A, R, u)
        for Rp, pm in md.items():
            for ass, pp in pa.items():
                Ap = coarsen_by_assignment(A, ass)
                s = (Ap, Rp)
                if s not in seen:
                    seen.add(s)
                    q.append(s)

    trans = [s for s in seen if len(s[0]) > 1]
    absor = [s for s in seen if len(s[0]) == 1]
    ti = {s:i for i,s in enumerate(trans)}
    outs = sorted({R for A,R in absor}, key=str)
    oi = {R:i for i,R in enumerate(outs)}
    nt, no = len(trans), len(outs)

    M = [[Fraction(int(i==j)) for j in range(nt)] for i in range(nt)]
    B = [[Fraction(0) for _ in range(no)] for _ in range(nt)]
    for s, i in ti.items():
        A, R = s
        pa = pa_cache[len(A)]
        md = mark_outcomes(A, R, u)
        for Rp, pm in md.items():
            for ass, pp in pa.items():
                p = pm*pp
                Ap = coarsen_by_assignment(A, ass)
                sp = (Ap, Rp)
                if len(Ap) > 1:
                    M[i][ti[sp]] -= p
                else:
                    B[i][oi[Rp]] += p

    aug = [M[i] + B[i] for i in range(nt)]
    cols = nt + no
    for c in range(nt):
        piv = next(r for r in range(c, nt) if aug[r][c])
        aug[c], aug[piv] = aug[piv], aug[c]
        z = aug[c][c]
        aug[c] = [x/z for x in aug[c]]
        for r in range(nt):
            if r != c and aug[r][c]:
                f = aug[r][c]
                aug[r] = [aug[r][j] - f*aug[c][j] for j in range(cols)]

    x0 = aug[ti[(A0,R0)]][nt:]
    dist = {R:x0[oi[R]] for R in outs}
    check(sum(dist.values()) == 1, f"absorbing distribution normalization {model}")
    return dist, len(seen), nt

def main():
    max_bad_ratio = Fraction(0)
    partition_checks = 0
    for N in range(2, 31):
        for r in range(2, min(7, N)+1):
            parts = unique_partitions(r)
            probs = {p: polya_partition_prob(N, p) for p in parts}
            check(sum(probs.values()) == 1, f"partition normalization N={N},r={r}")
            partition_checks += 1

            c = Fraction(2, N+1)
            p01 = sum(p for part,p in probs.items()
                      if any(0 in b and 1 in b for b in part))
            check(p01 == c, f"pair collision N={N},r={r}")
            partition_checks += 1

            no = tuple((i,) for i in range(r))
            p_no = probs[no]
            check(p_no == Fraction(falling(N,r), rising(N,r)),
                  f"no collision formula N={N},r={r}")
            partition_checks += 1

            target = tuple(sorted(((0,1),) + tuple((i,) for i in range(2,r)),
                                  key=lambda b:b[0]))
            p_exact = probs[target]
            expected = Fraction(2*falling(N,r-1), rising(N,r))
            check(p_exact == expected, f"single-pair formula N={N},r={r}")
            partition_checks += 1

            bad = 1 - p_no - comb(r,2)*p_exact
            check(bad >= 0, f"bad merger mass nonnegative N={N},r={r}")
            ratio = bad/(c*c)
            if ratio > max_bad_ratio:
                max_bad_ratio = ratio
            check(ratio <= 10**5, f"bad/c^2 unexpected N={N},r={r}")
            partition_checks += 1

    assignment_partition_checks = 0
    for N in range(2, 7):
        for r in range(2, min(5,N)+1):
            induced = defaultdict(Fraction)
            for ass in product(range(N), repeat=r):
                induced[induced_partition(ass)] += sequential_polya_assignment_prob(N, ass)
            check(sum(induced.values()) == 1, f"direct urn normalization N={N},r={r}")
            for part in unique_partitions(r):
                check(induced[part] == polya_partition_prob(N, part),
                      f"direct urn partition mismatch N={N},r={r},part={part}")
                assignment_partition_checks += 1

    scale_checks = 0
    for N in range(2, 1001):
        c = Fraction(2, N+1)
        delta = Fraction(1,N)
        u = Fraction(1, N*(N+1))
        check(u == delta*c/2, f"mark scale N={N}")
        for m in range(2, 8):
            q = m-1
            geom_sum_second = Fraction(q*q + q*(1-c), c*c)
            check(c*c * m*m * geom_sum_second <= m*m*q*(q+1),
                  f"second moment domination N={N},m={m}")
            scale_checks += 1

    N = 3
    u = Fraction(1, N*(N+1))
    dist, states, trans = final_refinement_distribution(N, u, "polya", 3)
    bydeg = defaultdict(Fraction)
    for R,p in dist.items():
        bydeg[len(R)] += p
    check(states == 25 and trans == 20, "unexpected C017 state count")
    check(bydeg[1] == Fraction(1633137,2663483), "C017 no-split probability")
    check(bydeg[2] == Fraction(890076,2663483), "C017 degree-2 probability")
    check(bydeg[3] == Fraction(140270,2663483), "C017 degree-3 probability")
    first_visible_deg3 = bydeg[3]/(1-bydeg[1])
    check(first_visible_deg3 == Fraction(70135,515173), "C017 visible degree-3 witness")

    wf_dist, wf_states, wf_trans = final_refinement_distribution(
        3, Fraction(1,18), "wf", 3
    )
    wf_bydeg = defaultdict(Fraction)
    for R,p in wf_dist.items():
        wf_bydeg[len(R)] += p
    wf_visible = wf_bydeg[3]/(1-wf_bydeg[1])
    check(wf_visible == Fraction(40589,352998), "archived C016 witness mismatch")

    retained = [
        Fraction(0), Fraction(1,10), Fraction(1,22), Fraction(1,6),
        Fraction(1,728), Fraction(1,7), Fraction(1,71), Fraction(1,71),
        Fraction(0), Fraction(0), Fraction(2,105),
        Fraction(21521,4909716), Fraction(35,1296), Fraction(14,2201),
        Fraction(2,17), Fraction(40589,352998)
    ]
    for old in retained:
        check(first_visible_deg3 != old, f"C017 witness collides with {old}")

    print("R11 I0054 C017 Pólya-Cannings exact self-check")
    print(f"checks = {CHECKS}")
    print(f"partition_formula_grid_checks = {partition_checks}")
    print(f"direct_urn_partition_checks = {assignment_partition_checks}")
    print(f"scale_second_moment_grid_checks = {scale_checks}")
    print(f"max_bad_merger_mass_over_cN_squared_grid = {max_bad_ratio}")
    print(f"N=3 reachable_states = {states}; transient_states = {trans}")
    print(f"N=3 raw_no_split = {bydeg[1]}")
    print(f"N=3 raw_degree2 = {bydeg[2]}")
    print(f"N=3 raw_degree3 = {bydeg[3]}")
    print(f"N=3 first_visible_degree3 = {first_visible_deg3}")
    print(f"archived_C016_first_visible_degree3_recomputed = {wf_visible}")
    print("ALL_EXACT_CHECKS_PASS")

if __name__ == "__main__":
    main()
