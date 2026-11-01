"""Is the pair-sum residual space ALWAYS admissible? Mass check against the campaign's valid_R.

The RC chain needs d_cb <= dim span{one pair-sum per triangle}. That is only a bound if the space is
admissible under the campaign's own `valid_R`. Nine hand-picked systems passed; nine is not a proof
and not even much evidence, since I chose them.

This runs random linear NAE triangle systems - including ones with 3-shared triangles, which the
hand-picked set had none of - and for each one:
   builds the fibre A, the dual D (campaign's full_dual), the pair-sum space, calls valid_R
and records pass/fail plus dim R against the rank prediction |V| - b on the sharing graph.

A single False is the useful outcome: it would say the pair-sum construction is not always
admissible and the d_cb bound needs a different residual family.

Also records, separately, whether dim R equals |V| - b, since that identity is what turns the bound
into the clean statement used in the RC write-up.
"""
import itertools
import random
import sys

SRC = "/srv/aiwork/rc_deep_box.py"
src = open(SRC, encoding="utf-8").read()
cut = src.index('print("dmax = %d"')
ns = {"__name__": "rc_lib", "sys": sys}
exec(compile(src[:cut], SRC, "exec"), ns)
full_dual = ns["full_dual"]
valid_R = ns["valid_R"]
rank_of = ns["rank_of"]
fib = ns["fib"]

rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 120


def is_linear(T):
    return all(len(set(x) & set(y)) < 2 for x, y in itertools.combinations(T, 2))


def random_system(r, kmax):
    allt = list(itertools.combinations(range(r), 3))
    rng.shuffle(allt)
    T = []
    for t in allt:
        if all(len(set(t) & set(u)) < 2 for u in T):
            T.append(t)
        if len(T) >= kmax:
            break
    return T


def pairsum_space(T, r):
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    sh = {x for x in cnt if cnt[x] >= 2}
    vs = []
    for t in T:
        s = [x for x in t if x in sh]
        pick = (s[0], s[1]) if len(s) >= 2 else (t[0], t[1])
        v = [0] * r
        v[pick[0]] += 1
        v[pick[1]] += 1
        vs.append(v)
    return vs


def sharing_graph_stats(T):
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    sh = {x for x in cnt if cnt[x] >= 2}
    edges = []
    n3 = 0
    for t in T:
        s = [x for x in t if x in sh]
        if len(s) == 3:
            n3 += 1
        if len(s) == 2:
            edges.append(tuple(s))
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    col, bip = {}, 0
    for s0 in adj:
        if s0 in col:
            continue
        col[s0] = 0
        st, ok = [s0], True
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in col:
                    col[v] = 1 - col[u]
                    st.append(v)
                elif col[v] == col[u]:
                    ok = False
        if ok:
            bip += 1
    return len(adj), bip, n3


ok = bad = skipped = 0
rank_match = rank_miss = 0
fails = []
with3 = 0
for _ in range(TRIALS):
    r = rng.choice([8, 9, 10, 11, 12])
    kmax = rng.choice([3, 4, 5, 6])
    T = random_system(r, kmax)
    used = sorted({x for t in T for x in t})
    if len(used) < 5 or len(T) < 2:
        skipped += 1
        continue
    lab = {x: i for i, x in enumerate(used)}
    T = [tuple(lab[x] for x in t) for t in T]
    rr = len(used)
    if rr > 14 or not is_linear(T):
        skipped += 1
        continue
    A = fib(rr, T)
    if not A:
        skipped += 1
        continue
    D = full_dual(A, rr)
    vs = pairsum_space(T, rr)
    dimR = rank_of(vs, rr)
    V, bip, n3 = sharing_graph_stats(T)
    if n3:
        with3 += 1
    res = valid_R(D, vs, rr)
    if res:
        ok += 1
    else:
        bad += 1
        if len(fails) < 6:
            fails.append((rr, len(T), tuple(T), dimR))
    if V:
        if dimR == V - bip + (len(T) - len([1 for t in T if sum(1 for x in t if sum(1 for u in T if x in u) >= 2) == 2])):
            rank_match += 1
        else:
            rank_miss += 1

print("systems tested : %d   skipped %d" % (ok + bad, skipped))
print("  of those, containing a 3-shared triangle: %d" % with3)
print()
print("valid_R(pair-sum space) TRUE  : %d" % ok)
print("valid_R(pair-sum space) FALSE : %d" % bad)
if fails:
    print()
    print("failures:")
    for rr, k, T, d in fails:
        print("   r=%d k=%d dimR=%d  %s" % (rr, k, d, T))
