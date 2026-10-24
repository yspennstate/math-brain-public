from itertools import combinations, product


def find(p, x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x


def forest_and_partition(n, edges, terminals=(0,1,2)):
    p = list(range(n))
    for u,v in edges:
        a,b = find(p,u), find(p,v)
        if a == b:
            return None
        p[a] = b
    r = [find(p,t) for t in terminals]
    if r[0] == r[1] == r[2]:
        return "t"
    if r[0] == r[1]:
        return "a"
    if r[0] == r[2]:
        return "b"
    if r[1] == r[2]:
        return "c"
    return "d"


def signature(n, E, weights=None):
    if weights is None:
        weights = [1]*len(E)
    out = {k:0 for k in "dabct"}
    for mask in range(1 << len(E)):
        S = []
        w = 1
        for i,e in enumerate(E):
            if (mask >> i) & 1:
                S.append(e)
                w *= weights[i]
        typ = forest_and_partition(n,S)
        if typ is not None:
            out[typ] += w
    return tuple(out[k] for k in "dabct")


def tau_and_gap(sig):
    d,a,b,c,t = sig
    tau = d*t - (a*b + a*c + b*c)
    gap = a*b*c - tau*t
    return tau,gap


def all_simple_graphs(n):
    K = list(combinations(range(n),2))
    for mask in range(1 << len(K)):
        yield [K[i] for i in range(len(K)) if (mask >> i) & 1]


checked = 0
min_tau = None
min_gap = None
for n in (3,4,5):
    local = 0
    for E in all_simple_graphs(n):
        sig = signature(n,E)
        tau,gap = tau_and_gap(sig)
        assert tau >= 0, (n,E,sig,tau)
        assert gap >= 0, (n,E,sig,tau,gap)
        min_tau = tau if min_tau is None else min(min_tau,tau)
        min_gap = gap if min_gap is None else min(min_gap,gap)
        checked += 1
        local += 1
    print(f"PASS all_simple_graphs n={n} graphs={local}")

# K4 gadget: terminal triangle x=01,y=02,z=12 and star u=30,v=31,w=32.
K4 = [(0,1),(0,2),(1,2),(3,0),(3,1),(3,2)]
for vals in product((0,1,2), repeat=6):
    x,y,z,u,v,w = vals
    sig = signature(4,K4,list(vals))
    d,a,b,c,t = sig
    assert d == 1+u+v+w
    assert a == d*x + u*v
    assert b == d*y + u*w
    assert c == d*z + v*w
    tau,gap = tau_and_gap(sig)
    assert tau == u*v*w
    assert gap >= 0
print("PASS K4_response_formula grid=3^6")
print(f"PASS response_cone_small_graphs total_graphs={checked} min_tau={min_tau} min_gap={min_gap}")
