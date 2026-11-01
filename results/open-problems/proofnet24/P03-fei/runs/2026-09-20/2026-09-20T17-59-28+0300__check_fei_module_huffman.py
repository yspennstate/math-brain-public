#!/usr/bin/env python3
import math, itertools, random, functools, json
import numpy as np

RHO = 2.0 / math.log(2.0)
TOL = 2e-12

def fwht_norm(vals):
    a = np.array(vals, dtype=float)
    N = len(a)
    h = 1
    while h < N:
        for i in range(0, N, 2*h):
            x = a[i:i+h].copy()
            y = a[i+h:i+2*h].copy()
            a[i:i+h] = x+y
            a[i+h:i+2*h] = x-y
        h *= 2
    return a / N

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1.0-x)*math.log2(1.0-x)

@functools.lru_cache(maxsize=None)
def entropy(vals):
    c = fwht_norm(vals)
    p = c*c
    nz = p[p > 1e-18]
    return float(-(nz*np.log2(nz)).sum())

@functools.lru_cache(maxsize=None)
def influences(vals):
    vals = tuple(vals)
    N = len(vals)
    n = int(round(math.log2(N)))
    out = []
    for i in range(n):
        diff = sum(1 for x in range(N) if vals[x] != vals[x ^ (1<<i)])
        out.append(diff / N)
    return tuple(out)

@functools.lru_cache(maxsize=None)
def B(vals, i):
    c = fwht_norm(vals)
    p = c*c
    N = len(p)
    total = 0.0
    for s in range(N):
        if (s >> i) & 1:
            continue
        p0 = p[s]
        p1 = p[s | (1<<i)]
        w = p0+p1
        if w > 1e-18:
            total += w*h2(p1/w)
    return float(total)

def restrict_one(vals, local_i, bit):
    N = len(vals)
    n = int(round(math.log2(N)))
    rem = [j for j in range(n) if j != local_i]
    out = []
    for rmask in range(1 << len(rem)):
        x = 0
        for k,j in enumerate(rem):
            if (rmask >> k) & 1:
                x |= 1 << j
        if bit:
            x |= 1 << local_i
        out.append(vals[x])
    return tuple(out), tuple(rem)

def tree_coords(tree):
    if tree[0] == "leaf":
        return tuple(tree[1])
    return tree_coords(tree[0]) + tree_coords(tree[1])

def remap_tree(tree, original_labels):
    mp = {c:i for i,c in enumerate(original_labels)}
    if tree[0] == "leaf":
        return ("leaf", tuple(mp[c] for c in tree[1]))
    return (remap_tree(tree[0], original_labels),
            remap_tree(tree[1], original_labels))

def base_cost(vals):
    n = int(round(math.log2(len(vals))))
    if n <= 1:
        return 0.0
    assert n == 2
    return min(B(vals,0), B(vals,1))

def compile_cost(vals, tree):
    if tree[0] == "leaf":
        return base_cost(vals)

    left, right = tree
    A = tuple(sorted(tree_coords(left)))
    Y = tuple(sorted(tree_coords(right)))

    def prefix_then(vals0, current_labels, query_labels, residual_tree):
        if not query_labels:
            return compile_cost(vals0, remap_tree(residual_tree, current_labels))
        c = query_labels[0]
        li = current_labels.index(c)
        cost = B(vals0, li)
        tail = 0.0
        for bit in (0,1):
            child, rem_pos = restrict_one(vals0, li, bit)
            new_labels = tuple(current_labels[j] for j in rem_pos)
            tail += 0.5 * prefix_then(child, new_labels, query_labels[1:], residual_tree)
        return cost + tail

    labels = tuple(range(int(round(math.log2(len(vals))))))
    a_first = prefix_then(vals, labels, A, right)
    y_first = prefix_then(vals, labels, Y, left)
    return min(a_first, y_first)

def leaf_depths(tree, depth=0, out=None):
    if out is None:
        out = {}
    if tree[0] == "leaf":
        out[tuple(tree[1])] = depth
    else:
        leaf_depths(tree[0], depth+1, out)
        leaf_depths(tree[1], depth+1, out)
    return out

def bounds(vals, tree):
    inf = influences(vals)
    direct = 0.0
    hered = 0.0
    for module,d in leaf_depths(tree).items():
        Iu = sum(inf[i] for i in module)
        if len(module) == 1:
            C0,K0 = 0.0,0.0
        elif len(module) == 2:
            C0,K0 = 2.0,1.0
        else:
            raise AssertionError("base modules must have size 1 or 2")
        c = C0 + RHO*d
        k = C0 + RHO*(d-1) + (K0-C0+RHO)*(2.0**(-d))
        direct += c*Iu
        hered += k*Iu
    return direct, hered

TREES = {
    1: [
        ("leaf",(0,))
    ],
    2: [
        ("leaf",(0,1)),
        (("leaf",(0,)), ("leaf",(1,)))
    ],
    3: [
        (("leaf",(0,1)), ("leaf",(2,))),
        (("leaf",(0,2)), ("leaf",(1,))),
        (("leaf",(1,2)), ("leaf",(0,))),
        ((("leaf",(0,)), ("leaf",(1,))), ("leaf",(2,))),
        (("leaf",(0,)), (("leaf",(1,)), ("leaf",(2,))))
    ],
    4: [
        (("leaf",(0,1)), ("leaf",(2,3))),
        (("leaf",(0,2)), ("leaf",(1,3))),
        (("leaf",(0,3)), ("leaf",(1,2))),
        ((("leaf",(0,1)), ("leaf",(2,))), ("leaf",(3,))),
        ((("leaf",(0,)), ("leaf",(1,))), (("leaf",(2,)), ("leaf",(3,))))
    ]
}

def exhaustive():
    total = 0
    max_direct = -1e100
    max_hered = -1e100
    max_cost_ratio = 0.0
    counts = {}
    for n in range(1,5):
        N = 1 << n
        nf = 1 << (N-1)  # global sign fixed by vals[0]=+1
        tc = 0
        for mask in range(nf):
            vals = [1]*N
            for j in range(1,N):
                if (mask >> (j-1)) & 1:
                    vals[j] = -1
            vals = tuple(vals)
            H = entropy(vals)
            I = sum(influences(vals))
            for tree in TREES[n]:
                db,hb = bounds(vals,tree)
                cc = compile_cost(vals,tree)
                max_direct = max(max_direct, H-db)
                max_hered = max(max_hered, cc-hb)
                if I > 0:
                    max_cost_ratio = max(max_cost_ratio, cc/I)
                tc += 1
                total += 1
        counts[str(n)] = {"functions_mod_global_sign": nf, "tree_cases": tc}
    return {
        "counts": counts,
        "total_tree_cases": total,
        "max_direct_violation": max_direct,
        "max_hereditary_violation": max_hered,
        "max_actual_compiler_cost_over_I": max_cost_ratio
    }

def seq_modules(n):
    mods=[]
    i=0
    while i+1<n:
        mods.append((i,i+1))
        i += 2
    if i<n:
        mods.append((i,))
    return mods

def balanced(nodes):
    if len(nodes)==1:
        return nodes[0]
    m=len(nodes)//2
    return (balanced(nodes[:m]), balanced(nodes[m:]))

def random_stress(num=600, seed=20260920):
    rng=random.Random(seed)
    max_direct=-1e100
    max_hered=-1e100
    byn={}
    for _ in range(num):
        n=rng.randint(5,7)
        vals=tuple(1 if rng.getrandbits(1)==0 else -1 for _ in range(1<<n))
        if vals[0] < 0:
            vals=tuple(-v for v in vals)
        tree=balanced([("leaf",m) for m in seq_modules(n)])
        H=entropy(vals)
        db,hb=bounds(vals,tree)
        cc=compile_cost(vals,tree)
        max_direct=max(max_direct,H-db)
        max_hered=max(max_hered,cc-hb)
        byn[str(n)]=byn.get(str(n),0)+1
    return {
        "seed": seed,
        "cases": num,
        "by_n": byn,
        "max_direct_violation": max_direct,
        "max_hereditary_violation": max_hered
    }

def recurrence_checks():
    max_pair=0.0
    max_single=0.0
    max_closed=0.0
    # Recurrences c' = c+rho, k'=(c+k+rho)/2.
    for baseC,baseK,kind in [(2.0,1.0,"pair"),(0.0,0.0,"single")]:
        c=baseC
        k=baseK
        for d in range(0,31):
            c_formula=baseC+RHO*d
            k_formula=baseC+RHO*(d-1)+(baseK-baseC+RHO)*(2.0**(-d))
            err=max(abs(c-c_formula),abs(k-k_formula))
            if kind=="pair": max_pair=max(max_pair,err)
            else: max_single=max(max_single,err)
            c,k=c+RHO,(c+k+RHO)/2.0
    # Perfect pair-module tree recovers newest balanced closed forms.
    for L in range(1,21):
        d=L-1
        D_pair=2.0+RHO*d
        K_pair=2.0+RHO*(d-1)+(RHO-1.0)*(2.0**(-d))
        D_bal=2.0+(L-1)*RHO
        K_bal=2.0+(L-2)*RHO+(RHO-1.0)*(2.0**(1-L))
        max_closed=max(max_closed,abs(D_pair-D_bal),abs(K_pair-K_bal))
    return {
        "max_pair_recurrence_error": max_pair,
        "max_singleton_recurrence_error": max_single,
        "max_balanced_closed_form_error": max_closed
    }

out = {
    "theorem": "certified-module hereditary coding compiler",
    "rho": RHO,
    "exhaustive": exhaustive(),
    "random_stress": random_stress(),
    "recurrence": recurrence_checks(),
}
out["status"] = "PASS" if (
    out["exhaustive"]["max_direct_violation"] <= TOL and
    out["exhaustive"]["max_hereditary_violation"] <= TOL and
    out["random_stress"]["max_direct_violation"] <= TOL and
    out["random_stress"]["max_hereditary_violation"] <= TOL and
    out["recurrence"]["max_pair_recurrence_error"] <= TOL and
    out["recurrence"]["max_singleton_recurrence_error"] <= TOL and
    out["recurrence"]["max_balanced_closed_form_error"] <= TOL
) else "FAIL"

print(json.dumps(out, sort_keys=True, indent=2))
