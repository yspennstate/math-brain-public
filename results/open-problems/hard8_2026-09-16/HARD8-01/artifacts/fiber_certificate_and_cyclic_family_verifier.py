from collections import deque, Counter
from itertools import product
from math import gcd
from fractions import Fraction


def apply_mask(mask, t, n):
    out = 0
    for i in range(n):
        if (mask >> i) & 1:
            out |= 1 << t[i]
    return out


def compose(t, u):
    # first t, then u
    return tuple(u[x] for x in t)


def max_fiber(t, n):
    counts = [0] * n
    for x in t:
        counts[x] += 1
    return max(counts)


def harmonic(k):
    return sum((Fraction(1, i) for i in range(1, k + 1)), Fraction(0))


def fs_reach_bound_worst_orbit(n, r):
    # Ferens--Szykula Theorem 5.7 with ell <= n.
    x = n - r
    return 2 * n * x - n * harmonic(x)


def completely_reachable(n, gens):
    start = (1 << n) - 1
    seen = {start}
    q = deque([start])
    while q:
        s = q.popleft()
        for g in gens:
            u = apply_mask(s, g, n)
            if u not in seen:
                seen.add(u)
                q.append(u)
    return len(seen) == (1 << n) - 1


def min_word_length_by_max_fiber(n, gens):
    ident = tuple(range(n))
    dist = {ident: 0}
    q = deque([ident])
    best = {1: 0}
    while q:
        t = q.popleft()
        d = dist[t]
        r = max_fiber(t, n)
        best[r] = min(best.get(r, 10**9), d)
        for g in gens:
            u = compose(t, g)
            if u not in dist:
                dist[u] = d + 1
                q.append(u)
    return best


def cycle_defect(n, d):
    a = tuple((i + 1) % n for i in range(n))
    b = tuple(d if i == 0 else i for i in range(n))
    return a, b


def shortest_subset_distances(n, gens):
    N = 1 << n
    preds = [[] for _ in range(N)]
    for s in range(1, N):
        for g in gens:
            preds[apply_mask(s, g, n)].append(s)
    dist = [None] * N
    q = deque()
    for i in range(n):
        s = 1 << i
        dist[s] = 0
        q.append(s)
    while q:
        y = q.popleft()
        for x in preds[y]:
            if dist[x] is None:
                dist[x] = dist[y] + 1
                q.append(x)
    return dist


def apply_word_to_state(x, word, a, b):
    for ch in word:
        x = a[x] if ch == 'a' else b[x]
    return x


def verify_cyclic_rank2_word(n, d):
    assert gcd(n, d) == 1
    a, b = cycle_defect(n, d)
    h = n - d
    word = 'b' + ('a' * h + 'b') * (n - 3)
    images = [apply_word_to_state(x, word, a, b) for x in range(n)]
    c = Counter(images)
    assert sorted(c.values()) == [1, n - 1]
    S = [x for x in range(n) if x != h]
    assert {images[x] for x in S} == {d}
    assert images[h] == (2 * d) % n
    assert len(word) == (n - 3) * (n - d) + (n - 2)
    return len(word)


def exact_cyclic_subset_check(max_n=16):
    checked = 0
    for n in range(3, max_n + 1):
        for d in range(1, n):
            if gcd(n, d) != 1:
                continue
            L = verify_cyclic_rank2_word(n, d)
            dist = shortest_subset_distances(n, cycle_defect(n, d))
            full = (1 << n) - 1
            exact = min(dist[full ^ (1 << miss)] for miss in range(n))
            formula = (n - 3) * (n - d) + (n - 2)
            assert L == formula == exact, (n, d, L, exact)
            checked += 1
    return checked


def exhaustive_n4_complete_reachability_check():
    n = 4
    transformations = list(product(range(n), repeat=n))
    count_cr = 0
    worst_certificate = Fraction(-1)
    tight_examples = []
    for a in transformations:
        for b in transformations:
            gens = (a, b)
            if not completely_reachable(n, gens):
                continue
            count_cr += 1
            best = min_word_length_by_max_fiber(n, gens)
            # use ell <= n, so no group computation is required
            cert = min(Fraction(L) + fs_reach_bound_worst_orbit(n, r)
                       for r, L in best.items() if 2 <= r < n)
            assert cert <= (n - 1) ** 2, (a, b, best, cert)
            if cert > worst_certificate:
                worst_certificate = cert
                tight_examples = [(a, b, best)]
            elif cert == worst_certificate and len(tight_examples) < 3:
                tight_examples.append((a, b, best))
    return count_cr, worst_certificate, tight_examples


if __name__ == '__main__':
    checked = exact_cyclic_subset_check(16)
    print('cyclic coprime (n,d) pairs checked through n=16:', checked)
    count_cr, worst, examples = exhaustive_n4_complete_reachability_check()
    print('ordered binary completely reachable n=4 automata:', count_cr)
    print('worst fiber-certificate bound using ell<=n:', worst)
    print('Cerny target for n=4:', 9)
    print('sample tight certificate automaton:', examples[0])
