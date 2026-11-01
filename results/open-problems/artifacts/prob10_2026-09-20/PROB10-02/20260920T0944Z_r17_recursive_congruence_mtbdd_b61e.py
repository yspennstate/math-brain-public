#!/usr/bin/env python3
"""
Exact finite checker for PROB10-02 / R17 recursive Bellman congruence.

All arithmetic in the Bellman iterate is integer arithmetic with common
denominator 4^n.  The finite-state recurrence is the genuine binary
lookahead recurrence: appended bits are source bits; no independent
Bernoulli match array is introduced.

Claims checked:
  1. recursive congruence class count through ell=8;
  2. every recursive class has a single exact Bellman transition signature;
  3. ordinary monotone partition refinement agrees with this quotient
     through ell=8 (finite evidence for coarseness, not used in the theorem);
  4. exact T^29(0) terminal counts and reduced ordered MTBDD node counts
     for ell=4,...,9, under three fixed variable orders.
"""
from functools import lru_cache
import numpy as np

def comp(x, ell):
    return x ^ ((1 << ell) - 1)

def shift(x, u, ell):
    if ell == 1:
        return u
    return ((x & ((1 << (ell - 1)) - 1)) << 1) | u

@lru_cache(None)
def rec_key(ell, a, b):
    if ell == 0:
        return ("Z",)
    ha = (a >> (ell - 1)) & 1
    hb = (b >> (ell - 1)) & 1
    if ha == hb:
        mask = (1 << (ell - 1)) - 1
        return ("M", rec_key(ell - 1, a & mask, b & mask))
    orbit = (
        (a, b),
        (comp(a, ell), comp(b, ell)),
        (b, a),
        (comp(b, ell), comp(a, ell)),
    )
    return ("X", min(orbit))

def formula_count(ell):
    if ell == 0:
        return 1
    return (2 * (4 ** (ell - 1)) + 3 * (2 ** (ell - 1)) + 1) // 3

def quotient_ids(ell):
    n = 1 << (2 * ell)
    ids = np.empty(n, dtype=np.int32)
    key_to_id = {}
    mask = (1 << ell) - 1
    for s in range(n):
        a, b = s >> ell, s & mask
        k = rec_key(ell, a, b)
        q = key_to_id.get(k)
        if q is None:
            q = len(key_to_id)
            key_to_id[k] = q
        ids[s] = q
    return ids, key_to_id

def successor_states(ell, a, b):
    ha = (a >> (ell - 1)) & 1
    hb = (b >> (ell - 1)) & 1
    if ha == hb:
        ss = []
        for u in (0,1):
            au = shift(a,u,ell)
            for v in (0,1):
                ss.append((au << ell) | shift(b,v,ell))
        return ("M", tuple(ss))
    A = tuple((shift(a,u,ell) << ell) | b for u in (0,1))
    B = tuple((a << ell) | shift(b,v,ell) for v in (0,1))
    return ("X", A, B)

def quotient_signature(ell, s, ids):
    mask = (1 << ell) - 1
    a, b = s >> ell, s & mask
    dat = successor_states(ell, a, b)
    if dat[0] == "M":
        return ("M", tuple(sorted(int(ids[t]) for t in dat[1])))
    A = tuple(sorted(int(ids[t]) for t in dat[1]))
    B = tuple(sorted(int(ids[t]) for t in dat[2]))
    return ("X", tuple(sorted((A,B))))

def check_congruence(ell):
    ids, keys = quotient_ids(ell)
    seen = {}
    n = len(ids)
    for s in range(n):
        q = int(ids[s])
        sig = quotient_signature(ell, s, ids)
        if q in seen:
            assert seen[q] == sig, (ell, q, seen[q], sig, s)
        else:
            seen[q] = sig
    assert len(seen) == formula_count(ell)
    return ids

def stable_refinement(ell):
    n = 1 << (2 * ell)
    mask = (1 << ell) - 1
    cls = np.empty(n, dtype=np.int32)
    for s in range(n):
        a,b=s>>ell,s&mask
        cls[s] = int(((a>>(ell-1))&1) != ((b>>(ell-1))&1))
    counts=[len(set(int(x) for x in cls))]
    while True:
        key_to_id={}
        new=np.empty_like(cls)
        for s in range(n):
            a,b=s>>ell,s&mask
            dat=successor_states(ell,a,b)
            if dat[0]=="M":
                trans=("M", tuple(sorted(int(cls[t]) for t in dat[1])))
            else:
                A=tuple(sorted(int(cls[t]) for t in dat[1]))
                B=tuple(sorted(int(cls[t]) for t in dat[2]))
                trans=("X",tuple(sorted((A,B))))
            key=(int(cls[s]),trans)
            q=key_to_id.get(key)
            if q is None:
                q=len(key_to_id); key_to_id[key]=q
            new[s]=q
        counts.append(len(key_to_id))
        if counts[-1] == counts[-2]:
            return new, counts
        cls=new

def same_partition(x,y):
    x_to_y={}
    y_to_x={}
    for a,b in zip(x,y):
        a=int(a);b=int(b)
        if a in x_to_y and x_to_y[a] != b: return False
        if b in y_to_x and y_to_x[b] != a: return False
        x_to_y[a]=b;y_to_x[b]=a
    return True

def precompute_numpy(ell):
    n=1<<(2*ell)
    mask=(1<<ell)-1
    states=np.arange(n,dtype=np.uint32)
    a=(states>>ell).astype(np.uint32)
    b=(states&mask).astype(np.uint32)
    match=(((a>>(ell-1))&1)==((b>>(ell-1))&1))
    tailmask=(1<<(ell-1))-1 if ell>1 else 0
    def sh(x,u):
        if ell==1: return np.full_like(x,u)
        return ((x&tailmask)<<1)|u
    au=[sh(a,u) for u in (0,1)]
    bv=[sh(b,v) for v in (0,1)]
    Ms=np.stack([(au[u]<<ell)|bv[v] for u in (0,1) for v in (0,1)])
    As=np.stack([(au[u]<<ell)|b for u in (0,1)])
    Bs=np.stack([(a<<ell)|bv[v] for v in (0,1)])
    return match,Ms,As,Bs

def value_iterate(ell, steps=29):
    match,Ms,As,Bs=precompute_numpy(ell)
    n=len(match)
    h=np.zeros(n,dtype=np.uint64)
    den=1
    min_inc=0
    for _ in range(steps):
        den_next=den*4
        new=np.empty_like(h)
        sm=h[Ms[0]]+h[Ms[1]]+h[Ms[2]]+h[Ms[3]]
        sa=2*(h[As[0]]+h[As[1]])
        sb=2*(h[Bs[0]]+h[Bs[1]])
        new[match]=den_next+sm[match]
        new[~match]=np.maximum(sa[~match],sb[~match])
        inc=new-4*h
        min_inc=int(inc.min())
        h=new; den=den_next
    return h,min_inc,den

def mtbdd_count(vals, ell, order):
    tensor=np.asarray(vals).reshape((2,)*(2*ell))
    if order=="interleaved":
        axes=[]
        for i in range(ell): axes += [i,ell+i]
        tensor=np.transpose(tensor,axes)
    elif order=="a_then_b":
        pass
    elif order=="reverse_interleaved":
        axes=[]
        for i in reversed(range(ell)): axes += [i,ell+i]
        tensor=np.transpose(tensor,axes)
    else:
        raise ValueError(order)
    flat=tensor.reshape(-1)
    termmap={}
    ids=np.empty(len(flat),dtype=np.int64)
    nextid=0
    for i,v in enumerate(flat):
        z=int(v)
        q=termmap.get(z)
        if q is None:
            q=nextid;nextid+=1;termmap[z]=q
        ids[i]=q
    terminals=len(termmap)
    internal=0
    for _level in range(2*ell-1,-1,-1):
        pairs=ids.reshape(-1,2)
        mp={}
        new=np.empty(len(pairs),dtype=np.int64)
        for i in range(len(pairs)):
            lo,hi=int(pairs[i,0]),int(pairs[i,1])
            if lo==hi:
                new[i]=lo
            else:
                key=(lo,hi)
                q=mp.get(key)
                if q is None:
                    q=nextid;nextid+=1;mp[key]=q;internal+=1
                new[i]=q
        ids=new
    assert len(ids)==1
    return terminals,internal

print("R17 PROB10-02 exact recursive-congruence / MTBDD checker")
print("SECTION quotient_congruence")
for ell in range(1,9):
    qids=check_congruence(ell)
    expected=formula_count(ell)
    print(f"CONGRUENCE ell={ell} classes={len(set(map(int,qids)))} formula={expected} PASS")
print("SECTION coarsest_refinement_finite")
for ell in range(1,9):
    qids,_=quotient_ids(ell)
    stable,counts=stable_refinement(ell)
    assert same_partition(qids,stable)
    print(f"REFINEMENT ell={ell} counts={counts} agrees_recursive_quotient=YES")
print("SECTION exact_value_iterate_mtbdd")
for ell in range(4,10):
    h,min_inc,den=value_iterate(ell,29)
    distinct=len(np.unique(h))
    rows=[]
    for order in ("interleaved","a_then_b","reverse_interleaved"):
        term,internal=mtbdd_count(h,ell,order)
        assert term==distinct
        rows.append((order,term,internal,term+internal))
    print(f"VALUE ell={ell} step=29 denom={den} min_increment_num={min_inc} distinct_terminals={distinct}")
    for order,term,internal,total in rows:
        print(f"MTBDD ell={ell} order={order} terminals={term} internal={internal} total={total}")
c22=formula_count(22)
raw22=4**22
old_group22=2**42+2**21
print(f"ELL22 raw_states={raw22} recursive_classes={c22} old_CS_orbits={old_group22}")
assert c22==2932033104555
assert old_group22==4398048608256
print("ALL_EXACT_CHECKS_PASS")
