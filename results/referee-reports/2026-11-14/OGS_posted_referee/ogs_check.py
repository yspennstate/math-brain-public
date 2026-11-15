# Independent check of one-generator-shuffle (Section 5 table, n=5 search, word lengths).
# Written without reading the repo's code. Convention: (gk)(x) = g(k(x)); walk g -> g s.
import itertools, math, sys
import numpy as np

def rank_all(perms, n):
    # lexicographic rank of each row (rows are permutations of 0..n-1)
    m = perms.shape[0]
    r = np.zeros(m, dtype=np.int64)
    used = np.zeros((m, n), dtype=bool)
    for pos in range(n):
        v = perms[:, pos]
        smaller_unused = np.zeros(m, dtype=np.int64)
        for k in range(n):
            smaller_unused += ((~used[:, k]) & (k < v)).astype(np.int64)
        r += smaller_unused * math.factorial(n - 1 - pos)
        used[np.arange(m), v] = True
    return r

def setup(n):
    perms = np.array(list(itertools.permutations(range(n))), dtype=np.int8)  # lex order, rank = row index
    return perms

def right_mult_map(perms, s, n):
    gs = perms[:, np.array(s)]          # (g s)(x) = g(s(x))
    return rank_all(gs.astype(np.int64), n)

def mix_times(perms, n, gens, eps_list, tmax=5000):
    N = perms.shape[0]
    maps = [right_mult_map(perms, s, n) for s in gens]
    w = 0.5 / len(gens)
    p = np.zeros(N); p[0] = 1.0       # row 0 is the identity
    out = {}
    for t in range(1, tmax + 1):
        q = 0.5 * p
        for mp in maps:
            q += w * p[mp]            # set of gens closed under inverses, so this is the forward step
        p = q
        tv = 0.5 * np.abs(p - 1.0 / N).sum()
        for e in eps_list:
            if e not in out and tv <= e:
                out[e] = t
        if len(out) == len(eps_list):
            break
    return out

def gens_for(n, extra):
    tau = list(range(n)); tau[0], tau[1] = 1, 0
    c = [(x + 1) % n for x in range(n)]
    ci = [(x - 1) % n for x in range(n)]
    ident = list(range(n))
    out = []
    for g in [tau, c, ci] + extra:
        if g != ident and g not in out:
            out.append(g)
    return out

def inv(p):
    q = [0] * len(p)
    for i, v in enumerate(p): q[v] = i
    return q

if __name__ == "__main__":
    for n in (5, 7, 9):
        perms = setup(n)
        sig = [(2 * x) % n for x in range(n)]
        base = mix_times(perms, n, gens_for(n, []), [0.25, 0.01])
        pt = mix_times(perms, n, gens_for(n, [sig, inv(sig)]), [0.25, 0.01])
        h = math.ceil(math.log2(n))
        print(f"n={n} h={h} base(1/4)={base[0.25]} PT(1/4)={pt[0.25]} base(1/100)={base[0.01]} PT(1/100)={pt[0.01]}", flush=True)
    # n=5: every added permutation
    n = 5; perms = setup(n)
    res = {}
    for pi in itertools.permutations(range(n)):
        pi = list(pi)
        res[tuple(pi)] = mix_times(perms, n, gens_for(n, [pi, inv(pi)]), [0.25])[0.25]
    best = min(res.values())
    winners = [k for k, v in res.items() if v == best]
    print("n=5 best time", best, "attained by", len(winners), "e.g.", winners[:3],
          "(1,2,4,0,3) ->", res[(1, 2, 4, 0, 3)], "doubling ->", res[(0, 2, 4, 1, 3)], flush=True)
