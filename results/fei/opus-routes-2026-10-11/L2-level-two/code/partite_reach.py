"""Which hard families Corollary K can reach (NOTES section 5e, after the D_K ladder).

For each truth table P (0/1 on n bits) compute the GF(2) polynomial by the Moebius transform, the graph joining two
coordinates that share a monomial, and whether that graph is complete (then every block partition with Corollary K's
property has singleton blocks, K = n). Families: tribes, alternating AND/OR trees, random read-once AND/OR formulas
with random negations, Hamming balls of every radius 0..n-1, majority. Controls that must NOT be complete: inner
product, bilinear forms, AND of K bits with dummies. Also records whether the top monomial x_1...x_n is present.
Usage: python -B partite_reach.py   (writes ../data/partite_reach.log)
"""
import itertools, os, random


def anf(tt, n):
    a = list(tt)
    for i in range(n):
        b = 1 << i
        for x in range(1 << n):
            if x & b:
                a[x] ^= a[x ^ b]
    return [m for m in range(1 << n) if a[m]]


def complete(mons, n):
    pairs = set()
    for m in mons:
        v = [i for i in range(n) if m >> i & 1]
        pairs.update(itertools.combinations(v, 2))
    return len(pairs) == n * (n - 1) // 2


def table(fn, n):
    return [fn([(x >> i) & 1 for i in range(n)]) for x in range(1 << n)]


def rand_formula(rng, vars_):
    if len(vars_) == 1:
        v = vars_[0]
        neg = rng.random() < 0.5
        return lambda x: x[v] ^ neg
    k = rng.randint(1, len(vars_) - 1)
    rng.shuffle(vars_)
    L, R = rand_formula(rng, vars_[:k]), rand_formula(rng, vars_[k:])
    op, neg = rng.choice(["and", "or"]), rng.random() < 0.3
    if op == "and":
        return lambda x: (L(x) & R(x)) ^ neg
    return lambda x: (L(x) | R(x)) ^ neg


def tree(depth, top_and=True):
    # alternating fan-in-2 tree over 2^depth leaves
    def f(x, lo=0, d=depth, a=top_and):
        if d == 0:
            return x[lo]
        h = 1 << (d - 1)
        l, r = f(x, lo, d - 1, not a), f(x, lo + h, d - 1, not a)
        return (l & r) if a else (l | r)
    return f


def main():
    out = []
    say = lambda s: (print(s, flush=True), out.append(s))
    rng = random.Random(20261012)
    fails = 0
    say("hard families (graph must be complete):")
    for w, s in [(2, 2), (2, 3), (3, 2), (3, 3), (2, 4), (4, 2), (2, 5)]:
        n = w * s
        P = table(lambda x: int(any(all(x[b * w + j] for j in range(w)) for b in range(s))), n)
        mons = anf(P, n)
        c, top = complete(mons, n), ((1 << n) - 1) in mons
        fails += (not c) + (not top)
        say(f"  tribes w={w} s={s}  n={n}  complete={c}  top monomial={top}")
    for d in [1, 2, 3]:
        for ta in (True, False):
            n = 1 << d
            mons = anf(table(tree(d, ta), n), n)
            c, top = complete(mons, n), ((1 << n) - 1) in mons
            fails += (not c) + (not top)
            say(f"  AND/OR tree depth={d} top={'AND' if ta else 'OR'}  n={n}  complete={c}  top monomial={top}")
    nro = 0
    for t in range(300):
        n = rng.randint(2, 10)
        f = rand_formula(rng, list(range(n)))
        mons = anf(table(f, n), n)
        c, top = complete(mons, n), ((1 << n) - 1) in mons
        fails += (not c) + (not top)
        nro += 1
    say(f"  random read-once AND/OR formulas with negations: {nro} on n = 2..10, failures so far {fails}")
    nb = 0
    for n in range(2, 11):
        for r in range(0, n):
            mons = anf(table(lambda x: int(sum(x) <= r), n), n)
            c = complete(mons, n)
            fails += not c
            nb += 1
    say(f"  Hamming balls 1{{|x| <= r}}, n = 2..10, r = 0..n-1: {nb} tables, failures so far {fails}")
    for n in (3, 5, 7, 9):
        c = complete(anf(table(lambda x: int(2 * sum(x) > n), n), n), n)
        fails += not c
        say(f"  majority n={n} complete={c}")
    say("controls (graph must NOT be complete):")
    ctrl_bad = 0
    for m in (2, 3, 4, 5):
        n = 2 * m
        c = complete(anf(table(lambda x: sum(x[i] & x[m + i] for i in range(m)) % 2, n), n), n)
        ctrl_bad += c
        say(f"  inner product n={n} complete={c}")
    for t in range(100):
        a, b = rng.randint(1, 4), rng.randint(1, 4)
        n = a + b
        M = [[rng.randint(0, 1) for _ in range(b)] for _ in range(a)]
        lin = [rng.randint(0, 1) for _ in range(n)]
        f = lambda x: (sum(M[i][j] & x[i] & x[a + j] for i in range(a) for j in range(b)) + sum(l & v for l, v in zip(lin, x))) % 2
        c = complete(anf(table(f, n), n), n)
        ctrl_bad += c and a + b > 2
    say(f"  100 random bilinear+affine forms on (a, b) blocks: complete on {ctrl_bad} beyond the trivial n = 2")
    say(f"failures among hard families: {fails}; controls wrongly complete: {ctrl_bad}")
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "partite_reach.log")
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
