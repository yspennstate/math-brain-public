# Independent check of the computer claims in "Adding one permutation to a transposition and a long cycle"
# (E0094, posted 13 Nov 2026). Written from the paper's text only, not from the repo's code.
# 1) the words of Lemmas 2.2-2.3 evaluate to c^i and to (i, i+d), and their lengths are within 3h-2 and 12h-9;
#    reports the longest transposition word for n = 5 and n = 101.
# 2) exact half-lazy mixing times (TV <= 1/4 and <= 1/100) for n = 5, 7, 9, base walk and P_T.
# 3) n = 5: every added pi, the smallest time to TV <= 1/4 and how many pi attain it.
import sys, itertools, math
import numpy as np

def comp(g, k):  # (g k)(x) = g(k(x))
    return tuple(g[k[x]] for x in range(len(g)))

def inv(g):
    r = [0] * len(g)
    for x, y in enumerate(g):
        r[y] = x
    return tuple(r)

def gens(n):
    tau = tuple([1, 0] + list(range(2, n)))
    c = tuple((x + 1) % n for x in range(n))
    s = tuple((2 * x) % n for x in range(n))
    return {"t": tau, "c": c, "C": inv(c), "s": s, "S": inv(s)}

def evalw(w, G, n):
    g = tuple(range(n))
    for a in w:
        g = comp(g, G[a])
    return g

INV = {"t": "t", "c": "C", "C": "c", "s": "S", "S": "s"}
def winv(w):
    return [INV[a] for a in reversed(w)]

def word_cpow(i):  # Lemma 2.2: c^{2q+b} = s c^q S c^b
    bits = bin(i)[3:]
    w = ["c"]
    for b in bits:
        w = ["s"] + w + ["S"] + (["c"] if b == "1" else [])
    return w

def word_transp(i, d, n):  # Lemma 2.3
    js = [k for k in range(d.bit_length()) if (d >> k) & 1]
    B = ["s"] * js[0]
    for a, b in zip(js, js[1:]):
        B += ["t", "c"] + ["s"] * (b - a)
    w = B + ["t"] + winv(B)
    if i % n:
        wc = word_cpow(i)
        w = wc + w + winv(wc)
    return w

def evalw_np(w, A, n):
    g = np.arange(n)
    for a in w:
        g = g[A[a]]          # g o G[a], same order as comp
    return g

def check_words(n):
    G = gens(n); h = math.ceil(math.log2(n)); e = np.arange(n)
    A = {k: np.array(v) for k, v in G.items()}
    for i in range(1, n):
        w = word_cpow(i)
        assert len(w) <= 3 * h - 2 and (evalw_np(w, A, n) == (e + i) % n).all(), (n, i)
    longest = 0
    for i in range(n):                      # lengths for every (i, d)
        for d in range(1, n):
            L = len(word_transp(i, d, n))
            assert L <= 12 * h - 9, (n, i, d, L)
            longest = max(longest, L)
    rng = np.random.default_rng(n)
    iset = sorted(set([0, 1, n - 1] + list(rng.integers(0, n, 3))))
    for i in iset:                          # evaluate every d for these i (all i when n <= 61)
        pass
    if n <= 61:
        iset = range(n)
    for i in iset:
        for d in range(1, n):
            g = evalw_np(word_transp(i, d, n), A, n)
            j = (i + d) % n
            want = e.copy(); want[i], want[j] = want[j], want[i]
            assert (g == want).all(), (n, i, d)
    return h, longest

def mixing(n, moves, eps_list=(0.25, 0.01), tmax=5000):
    perms = list(itertools.permutations(range(n)))
    idx = {p: k for k, p in enumerate(perms)}
    N = len(perms)
    maps = [np.fromiter((idx[comp(p, m)] for p in perms), dtype=np.int64, count=N) for m in moves]
    p = np.zeros(N); p[idx[tuple(range(n))]] = 1.0
    out = {}; w = 0.5 / len(moves)
    for t in range(1, tmax + 1):
        q = 0.5 * p
        for mp in maps:
            q[mp] += w * p   # mp is a bijection, so fancy-index assignment is exact
        p = q
        tv = 0.5 * np.abs(p - 1.0 / N).sum()
        for eps in eps_list:
            if eps not in out and tv <= eps:
                out[eps] = t
        if len(out) == len(eps_list):
            break
    return out

if __name__ == "__main__":
    for n in list(range(5, 302, 2)):
        h, L = check_words(n)
        if n in (5, 7, 9, 101, 301):
            print(f"words n={n} h={h} longest transposition word {L} (bound {12*h-9})", flush=True)
    print("words: odd n 5..301 - every c^i word and every (i,i+d) word length within 3h-2 / 12h-9; "
          "transposition words evaluated for all i when n <= 61, six i per n above", flush=True)
    for n in (5, 7, 9):
        G = gens(n)
        base = mixing(n, [G["t"], G["c"], G["C"]])
        full = mixing(n, [G["t"], G["c"], G["C"], G["s"], G["S"]])
        print(f"n={n} base {base[0.25]} {base[0.01]}  P_T {full[0.25]} {full[0.01]}", flush=True)
    n = 5; G = gens(n); e = tuple(range(n)); best = {}
    for pi in itertools.permutations(range(n)):
        T = []
        for m in (G["t"], G["c"], G["C"], pi, inv(pi)):
            if m != e and m not in T:
                T.append(m)
        best[pi] = mixing(n, T, eps_list=(0.25,))[0.25]
    m = min(best.values()); arg = [p for p, v in best.items() if v == m]
    print(f"n=5 all pi: min time {m}, attained by {len(arg)}; (1,2,4,0,3) -> {best[(1,2,4,0,3)]}; doubling -> {best[G['s']]}", flush=True)
