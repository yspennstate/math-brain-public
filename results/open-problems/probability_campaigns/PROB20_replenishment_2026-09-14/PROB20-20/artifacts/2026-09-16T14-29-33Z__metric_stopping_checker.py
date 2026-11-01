from fractions import Fraction
from functools import lru_cache
from itertools import product

# Exact finite checker for PROB20-20.
# It has two roles:
# (1) verify the purely finite stopping/Jensen inequality used in the new metric theorem;
# (2) perform an exact counterexample-first scan of finite staircase prefixes that can be
#     extended by an arbitrarily light sparse radius-one tail while keeping boundary mean < lambda.
# No finite calculation is claimed to decide the asymptotic Janson problem.


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from compositions(total - x, parts - 1, prefix + (x,))


@lru_cache(None)
def tau_dist(state, rem):
    """Exact law of number of size-biased box removals needed to remove >= rem balls.

    state is a sorted tuple of positive occupancies. At each step one ball is chosen
    uniformly from the residual balls and its entire box is removed.
    """
    total = sum(state)
    assert total >= rem > 0
    out = {}
    for idx, b in enumerate(state):
        p = Fraction(b, total)
        nxt = state[:idx] + state[idx + 1:]
        if b >= rem:
            out[1] = out.get(1, Fraction()) + p
        else:
            sub = dict(tau_dist(tuple(sorted(nxt)), rem - b))
            for t, pt in sub.items():
                out[t + 1] = out.get(t + 1, Fraction()) + p * pt
    assert sum(out.values(), Fraction()) == 1
    return tuple(sorted(out.items()))


def stopping_test(weights, n, m, threshold):
    Z = 0
    emax_num = 0
    etau_num = Fraction()
    einv_num = Fraction()
    states = 0
    for y in compositions(m, n):
        wt = 1
        for v in y:
            if v >= len(weights) or weights[v] == 0:
                wt = 0
                break
            wt *= weights[v]
        if wt == 0:
            continue
        states += 1
        Z += wt
        emax_num += wt * max(y)
        state = tuple(sorted(v for v in y if v > 0))
        dist = dict(tau_dist(state, threshold))
        et = sum(Fraction(t) * p for t, p in dist.items())
        ei = sum(Fraction(1, t) * p for t, p in dist.items())
        etau_num += wt * et
        einv_num += wt * ei

    Emax = Fraction(emax_num, Z)
    Etau = etau_num / Z
    Einv = einv_num / Z
    lhs = Emax / n
    c = Fraction(threshold, n)
    rhs_path = c * Einv
    rhs_jensen = c / Etau
    assert lhs >= rhs_path >= rhs_jensen
    return {
        "states": states,
        "Z": Z,
        "Emax_over_n": lhs,
        "c_Einv_tau": rhs_path,
        "c_over_Etau": rhs_jensen,
        "Etau": Etau,
    }


def partition_leq(weights, n, m, K):
    """Exact ordered allocation partition function with all coordinates <= K."""
    dp = [0] * (m + 1)
    dp[0] = 1
    for _ in range(n):
        ndp = [0] * (m + 1)
        for s, a in enumerate(dp):
            if a == 0:
                continue
            for k in range(min(K, m - s, len(weights) - 1) + 1):
                wk = weights[k]
                if wk:
                    ndp[s + k] += a * wk
        dp = ndp
    return dp[m]


def exact_emax_ratio(weights, n, m):
    Z = partition_leq(weights, n, m, m)
    assert Z > 0
    # E M = sum_{r=1}^m P(M >= r) = m - sum_{K=0}^{m-1} P(M <= K)
    sum_cdf_num = sum(partition_leq(weights, n, m, K) for K in range(m))
    Emax = Fraction(m * Z - sum_cdf_num, Z)
    return Emax / n, Z


def prefix_mean(weights):
    den = sum(weights)
    num = sum(k * w for k, w in enumerate(weights))
    return Fraction(num, den)


def staircase_scan():
    # n=6, m=12 => lambda=2. Search 750 rational/integer finite prefixes.
    # Prefix form: w0=A, w1=1, w2..4=B, w5..8=C, w9..12=D.
    # Keep only prefixes with normalized prefix mean < 19/10. Such a finite prefix
    # can be extended by an arbitrarily light sparse tail with radius one and
    # finite first moment, preserving nu < 2. This is only a finite stress test.
    As = [32, 64, 128, 256, 512, 1024]
    vals = [1, 2, 4, 8, 16]
    best = None
    tested = 0
    admissible = 0
    for A, B, C, D in product(As, vals, vals, vals):
        weights = [A, 1] + [B] * 3 + [C] * 4 + [D] * 4
        tested += 1
        mu = prefix_mean(weights)
        if mu >= Fraction(19, 10):
            continue
        admissible += 1
        ratio, Z = exact_emax_ratio(weights, 6, 12)
        rec = (ratio, mu, (A, B, C, D), Z)
        if best is None or rec[0] < best[0]:
            best = rec
    assert best is not None
    return tested, admissible, best


def concentrated_fragment_scan():
    # Stronger finite stress test at n=10,m=20 (lambda=2).
    # Prefix: w0=A, w1=1, w2=w3=w4=B, and w5..w20=1.
    # We require normalized prefix mean < 19/10; then an arbitrarily light
    # sparse radius-one tail can be appended while keeping boundary mean < 2.
    As = [500, 1000, 2000, 5000]
    Bs = [100, 200, 300, 500, 800]
    best = None
    tested = 0
    admissible = 0
    for A, B in product(As, Bs):
        weights = [A, 1] + [B] * 3 + [1] * 16
        tested += 1
        mu = prefix_mean(weights)
        if mu >= Fraction(19, 10):
            continue
        admissible += 1
        ratio, Z = exact_emax_ratio(weights, 10, 20)
        rec = (ratio, mu, (A, B), Z)
        if best is None or ratio < best[0]:
            best = rec
    assert best is not None
    return tested, admissible, best


def main():
    print("PROB20-20 exact metric/stopping checker")
    tests = [
        ("uniform-prefix", [1] * 20, 5, 10, 3),
        ("staircase", [64,48,30,20,16,12,10,8,7,6,5,4,4,3,3,2,2,2,1,1], 5, 10, 3),
        ("irregular", [200,90,30,12,5,3,2,1,4,1,1,1,3,1,1,1,2,1,1,1], 5, 10, 3),
    ]
    for name, w, n, m, threshold in tests:
        r = stopping_test(w, n, m, threshold)
        print(name)
        for key in ("states", "Z", "Emax_over_n", "c_Einv_tau", "c_over_Etau", "Etau"):
            print(f"  {key}={r[key]}")
        print(f"  decimal_chain={float(r['Emax_over_n']):.12f} >= {float(r['c_Einv_tau']):.12f} >= {float(r['c_over_Etau']):.12f}")

    tested, admissible, best = staircase_scan()
    ratio, mu, params, Z = best
    print("counterexample_first_staircase_scan")
    print(f"  tested_prefixes={tested}")
    print(f"  mean_admissible_prefixes={admissible}")
    print(f"  best_params_A_B_C_D={params}")
    print(f"  best_prefix_mean={mu} ({float(mu):.12f})")
    print(f"  best_exact_Emax_over_n={ratio} ({float(ratio):.12f})")
    print(f"  best_partition_Z={Z}")
    print("  asymptotic_inference=NONE (finite prefix stress test only)")

    tested2, admissible2, best2 = concentrated_fragment_scan()
    ratio2, mu2, params2, Z2 = best2
    print("counterexample_first_concentrated_fragment_scan")
    print(f"  tested_prefixes={tested2}")
    print(f"  mean_admissible_prefixes={admissible2}")
    print(f"  best_params_A_B={params2}")
    print(f"  best_prefix_mean={mu2} ({float(mu2):.12f})")
    print(f"  best_exact_Emax_over_n={ratio2} ({float(ratio2):.12f})")
    print(f"  best_partition_Z={Z2}")
    print("  embeddability_note=finite prefix can be extended by a sparse tail w_Nj=2^(-j)/N_j^2 with N_j growing fast, giving radius one and arbitrarily small added first moment")
    print("  asymptotic_inference=NONE (finite prefix stress test only)")
    print("PASS")


if __name__ == "__main__":
    main()
