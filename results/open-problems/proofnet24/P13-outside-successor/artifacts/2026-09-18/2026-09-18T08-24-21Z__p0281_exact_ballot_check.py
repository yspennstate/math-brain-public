from collections import defaultdict
from fractions import Fraction
from math import comb, factorial

MAX_K = 24
MAX_N = 4


def event_counts(n, k):
    """Exact integer clock-word counts for n-particle step TASEP after k uniformized events.

    Displacement state a=(a_1,...,a_n) satisfies a_1>=...>=a_n>=0.
    Each event selects one particle clock. A legal jump increments its displacement;
    a blocked clock leaves the state unchanged.
    """
    dist = {tuple([0] * n): 1}
    for _ in range(k):
        nxt = defaultdict(int)
        for a, c in dist.items():
            for i in range(n):
                b = list(a)
                if i == 0 or a[i - 1] > a[i]:
                    b[i] += 1
                nxt[tuple(b)] += c
        dist = dict(nxt)
    return dist


def ballot(k, b):
    if b < 0 or 2 * b > k:
        return 0
    return comb(k, b) - (comb(k, b - 1) if b else 0)


def check_two_particle_ballot_formula():
    checked = 0
    for k in range(MAX_K + 1):
        dist = event_counts(2, k)
        for (a, b), c in dist.items():
            want = ballot(k, b)
            if c != want:
                raise AssertionError(("ballot formula", k, a, b, c, want))
            if not (b <= a and a + b <= k):
                raise AssertionError(("support", k, a, b))
            checked += 1
        for b in range(k // 2 + 1):
            for a in range(b, k - b + 1):
                got = dist.get((a, b), 0)
                want = ballot(k, b)
                if got != want:
                    raise AssertionError(("support completeness", k, a, b, got, want))
                checked += 1
    return checked


def kernel_no_t(k, b):
    """h_t(k,b)/t^k = B(k,b)/k!, exactly."""
    if b < 0 or 2 * b > k:
        return Fraction(0, 1)
    return Fraction(ballot(k, b), factorial(k))


def check_kernel_floor_ceil_midpoint():
    checked = 0
    for k1 in range(MAX_K + 1):
        for b1 in range(k1 // 2 + 1):
            for k2 in range(MAX_K + 1):
                for b2 in range(k2 // 2 + 1):
                    if (b1 + b2) & 1:
                        continue
                    bm = (b1 + b2) // 2
                    km = (k1 + k2) // 2
                    kp = (k1 + k2 + 1) // 2
                    left = kernel_no_t(k1, b1) * kernel_no_t(k2, b2)
                    right = kernel_no_t(km, bm) * kernel_no_t(kp, bm)
                    checked += 1
                    if left > right:
                        raise AssertionError(("kernel midpoint", (k1,b1),(k2,b2),(km,bm),(kp,bm),left,right))
    return checked


def check_fixed_event_midpoint_lc():
    checked = 0
    details = []
    for n in range(1, MAX_N + 1):
        per_n = 0
        max_states = 0
        for k in range(MAX_K + 1):
            dist = event_counts(n, k)
            if sum(dist.values()) != n ** k:
                raise AssertionError(("word total", n, k, sum(dist.values()), n**k))
            max_states = max(max_states, len(dist))
            states = sorted(dist)
            for i, a in enumerate(states):
                for b in states[i:]:
                    sums = tuple(x + y for x, y in zip(a, b))
                    if any(v & 1 for v in sums):
                        continue
                    m = tuple(v // 2 for v in sums)
                    if m not in dist:
                        raise AssertionError(("convex support", n, k, a, b, m))
                    per_n += 1
                    if dist[m] * dist[m] < dist[a] * dist[b]:
                        raise AssertionError(("fixed-event midpoint LC", n, k, a, b, m, dist[a], dist[b], dist[m]))
        details.append((n, max_states, per_n))
        checked += per_n
    return checked, details


if __name__ == "__main__":
    c_ballot = check_two_particle_ballot_formula()
    print(f"two-particle ballot/support identities through k={MAX_K}: {c_ballot} exact state checks; PASS")

    c_kernel = check_kernel_floor_ceil_midpoint()
    print(f"two-particle ballot-kernel floor/ceil midpoint inequalities through k1,k2={MAX_K}: {c_kernel} exact rational checks; PASS")

    c_mid, details = check_fixed_event_midpoint_lc()
    for n, max_states, count in details:
        print(f"n={n}: k=0..{MAX_K}; max_states={max_states}; fixed-event exact midpoint inequalities={count}; PASS")
    print(f"TOTAL fixed-event exact midpoint inequalities checked: {c_mid}")
    print("SELF-CHECK ONLY: bounded fixed-event enumeration is not a proof of continuous-time P0281.")
    print("ALL_EXACT_ARITHMETIC_CHECKS_PASS")
