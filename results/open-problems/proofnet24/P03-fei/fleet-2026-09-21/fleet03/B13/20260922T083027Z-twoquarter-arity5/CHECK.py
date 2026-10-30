#!/usr/bin/env python3
"""
Exact-combinatorial / high-precision self-check for fleet03/B13's
balanced arity-5 two-quarter slice:
    p = (1/4,1/4,1/2,1/2,1/2), p_out = 1/2.

The exhaustive orbit reduction and every spectral numerator/influence
quantity are integer/exact. Candidate ranking is first screened in
float64, then every signature above 6.0 is replayed at Decimal precision.
This is a self-check, not an independent formal proof.
"""
from collections import Counter
from decimal import Decimal, getcontext
from itertools import permutations
from math import comb, log2
import numpy as np

DEN = 16384
C0 = 6.4548

# Three-bit Walsh data for all 256 branch truth tables.
pts = [[(x >> i) & 1 for i in range(3)] for x in range(8)]
W = np.empty((8, 8), dtype=np.int16)
for T in range(8):
    tb = [(T >> i) & 1 for i in range(3)]
    W[T] = [1 if sum(tb[i]*x[i] for i in range(3)) % 2 == 0 else -1 for x in pts]

F = np.empty((256, 8), dtype=np.int16)
cnt = np.empty(256, dtype=np.int8)
for m in range(256):
    vals = np.array([1 if (m >> x) & 1 else -1 for x in range(8)], dtype=np.int16)
    cnt[m] = m.bit_count()
    F[m] = W @ vals

# Simultaneous automorphism group of Q_3, size 3! 2^3 = 48.
maps = []
for perm in permutations(range(3)):
    for t in range(8):
        mp = []
        for x in range(8):
            xb = [(x >> i) & 1 for i in range(3)]
            yb = [xb[perm[i]] ^ ((t >> i) & 1) for i in range(3)]
            mp.append(sum(yb[i] << i for i in range(3)))
        maps.append(mp)
assert len({tuple(x) for x in maps}) == 48

def tmask(mask, mp):
    out = 0
    for x, y in enumerate(mp):
        if (mask >> x) & 1:
            out |= 1 << y
    return out

canon = {}
by_count = {k: [] for k in range(9)}
orbits = {k: [] for k in range(9)}
for m in range(256):
    canon[m] = min(tmask(m, mp) for mp in maps)
for k in range(9):
    by_count[k] = [m for m in range(256) if cnt[m] == k]
    orbits[k] = sorted({canon[m] for m in by_count[k]})

# Balance under branch weights 9:3:3:1:
# 9 k00 + 3 k01 + 3 k10 + k11 = 64.
feasible = []
raw_balanced = 0
orbit_representatives = 0
for k00 in range(9):
    for k01 in range(9):
        for k10 in range(9):
            for k11 in range(9):
                ks = (k00, k01, k10, k11)
                if 9*k00 + 3*k01 + 3*k10 + k11 != 64:
                    continue
                feasible.append(ks)
                raw_balanced += np.prod([comb(8, k) for k in ks], dtype=object)
                options = []
                for j, k in enumerate(ks):
                    n = len(orbits[k])
                    for ell, kk in enumerate(ks):
                        if ell != j:
                            n *= len(by_count[kk])
                    options.append((n, j))
                orbit_representatives += min(options)[0]

assert len(feasible) == 81
assert raw_balanced == 119_655_384
assert orbit_representatives == 7_492_264

nums = np.arange(DEN + 1, dtype=np.float64)
ent = np.zeros(DEN + 1, dtype=np.float64)
nz = nums > 0
ent[nz] = (nums[nz]/DEN) * (14.0 - np.log2(nums[nz]))
deg = np.array([T.bit_count() for T in range(8)], dtype=np.int16)
lam = 0.75 * log2(3.0)

def eval_block(ms):
    s00 = F[ms[:,0]].astype(np.int32)
    s01 = F[ms[:,1]].astype(np.int32)
    s10 = F[ms[:,2]].astype(np.int32)
    s11 = F[ms[:,3]].astype(np.int32)

    n0  = (9*s00 + 3*s01 + 3*s10 + s11)**2
    n1  = 3*(3*(s10-s00) + (s11-s01))**2
    n2  = 3*(3*(s01-s00) + (s11-s10))**2
    n12 = 9*(s00-s01-s10+s11)**2

    # 32 squared biased Fourier masses are n*/16384.
    assert np.all((n0+n1+n2+n12).sum(axis=1) == DEN)

    H = (ent[n0]+ent[n1]+ent[n2]+ent[n12]).sum(axis=1)

    # A=(It_y1+It_y2)/V_1/4.  The y1y2 layer contributes to BOTH influences.
    A = (n1+n2+2*n12).sum(axis=1)/(DEN*0.75)
    total = n0+n1+n2+n12
    B = (total*deg).sum(axis=1)/DEN

    currency = A+B-1.0
    Creq = np.full(len(ms), -np.inf)
    good = currency > 1e-14
    Creq[good] = (H[good] + lam*A[good])/currency[good]

    Igate = 0.75*A+B
    Wq = (Igate-1.0)/4.0
    D0 = currency*C0-H-lam*A
    cg = np.full(len(ms), -np.inf)
    pos = Wq > 1e-14
    cg[pos] = -D0[pos]/Wq[pos]
    return Creq, cg, H, A, B, (n0,n1,n2,n12)

bestC = (-np.inf, None, None)
bestcg = (-np.inf, None, None)
n_eval = 0
n_gt_615 = 0
high = {}

for ks in feasible:
    options = []
    for j, k in enumerate(ks):
        n = len(orbits[k])
        for ell, kk in enumerate(ks):
            if ell != j:
                n *= len(by_count[kk])
        options.append((n, j))
    _, j = min(options)

    choices = [by_count[k] for k in ks]
    choices[j] = orbits[ks[j]]

    # Loop the two smallest lists, vectorise over the two largest.
    order = sorted(range(4), key=lambda q: len(choices[q]))
    a,b,c,d = order
    cc,dd = np.meshgrid(np.array(choices[c],dtype=np.int16),
                        np.array(choices[d],dtype=np.int16), indexing="ij")
    base = np.empty((cc.size,4),dtype=np.int16)
    base[:,c] = cc.ravel()
    base[:,d] = dd.ravel()

    for ma in choices[a]:
        for mb in choices[b]:
            ms = base.copy()
            ms[:,a] = ma
            ms[:,b] = mb
            Creq,cg,H,A,B,layers = eval_block(ms)
            n_eval += len(ms)

            i = int(np.argmax(Creq))
            if Creq[i] > bestC[0]:
                bestC = (float(Creq[i]), tuple(map(int,ms[i])),
                         (float(H[i]),float(A[i]),float(B[i]),ks))
            i = int(np.argmax(cg))
            if cg[i] > bestcg[0]:
                bestcg = (float(cg[i]), tuple(map(int,ms[i])),
                          (float(H[i]),float(A[i]),float(B[i]),ks))

            hit = np.flatnonzero(Creq > 6.15)
            n_gt_615 += len(hit)

            # Retain every distinct signature above 6.0 for high-precision replay.
            for idx in np.flatnonzero(Creq > 6.0):
                alln = tuple(sorted(map(int, np.concatenate(
                    [layers[q][idx] for q in range(4)]))))
                rawQ = int((layers[1][idx]+layers[2][idx]+2*layers[3][idx]).sum())
                rawB = int(((layers[0][idx]+layers[1][idx]+
                             layers[2][idx]+layers[3][idx])*deg).sum())
                sig = (alln, rawQ, rawB)
                high[sig] = (float(Creq[idx]), tuple(map(int,ms[idx])))

assert n_eval == orbit_representatives
assert n_gt_615 == 24
assert len(high) == 10

# High precision replay of all screened signatures.
getcontext().prec = 80
D = Decimal
ln2 = D(2).ln()
log2D = lambda x: D(x).ln()/ln2
lamD = D(3)/D(4)*log2D(3)

def replay(sig):
    masses, rawQ, rawB = sig
    H = D(0)
    for n, mult in Counter(masses).items():
        if n:
            p = D(n)/D(DEN)
            H += D(mult)*p*(D(14)-log2D(n))
    A = D(rawQ)/(D(DEN)*D(3)/D(4))
    B = D(rawB)/D(DEN)
    C = (H+lamD*A)/(A+B-D(1))
    return C,H,A,B

replayed = sorted([(replay(sig)[0], sig, meta) for sig,meta in high.items()],
                  reverse=True, key=lambda x:x[0])
Cexact = D(51)/D(5) - D(27)/D(40)*log2D(3) - D(5)/D(4)*log2D(5)
assert abs(replayed[0][0]-Cexact) < D("1e-70")
assert abs(replayed[1][0]-Cexact) < D("1e-70")
assert abs(replayed[2][0]-Cexact) < D("1e-70")
assert replayed[3][0] < D("6.133")
assert abs(D(str(bestC[0]))-Cexact) < D("1e-12")

# One especially transparent maximizing signature.
witness = (7,15,119,127)
Cw,cgw,Hw,Aw,Bw,lw = eval_block(np.array([witness],dtype=np.int16))
hist = Counter(map(int,np.concatenate([lw[q][0] for q in range(4)])))
assert hist == Counter({0:9,192:14,256:3,1024:3,1728:2,6400:1})
assert abs(float(Aw[0])-1/2) < 1e-15
assert abs(float(Bw[0])-9/8) < 1e-15

# Direct physical realization: replace each quarter input by a fresh AND_2.
vals = np.empty(128,dtype=np.float64)
for x in range(128):
    bit = [(x>>i)&1 for i in range(7)]
    y1 = bit[0]&bit[1]
    y2 = bit[2]&bit[3]
    z = bit[4] | (bit[5]<<1) | (bit[6]<<2)
    m = witness[(y1<<1)|y2]
    vals[x] = 1 if (m>>z)&1 else -1
a = vals.copy()
h = 1
while h < 128:
    for i in range(0,128,2*h):
        u=a[i:i+h].copy()
        v=a[i+h:i+2*h].copy()
        a[i:i+h]=u+v
        a[i+h:i+2*h]=u-v
    h *= 2
p = (a/128.0)**2
Hphys = -sum(q*log2(q) for q in p if q)
Iphys = sum(S.bit_count()*p[S] for S in range(128))
assert abs(Iphys-13/8) < 1e-15
assert abs(Hphys/(Iphys-1)-float(Cexact)) < 1e-12

# The same witness maximizes the owner-comparable quadratic margin at C0;
# with A=1/2,B=9/8 its currency is 1/8 and c_G=5(Cexact-C0).
cg_exact = D(5)*(Cexact-D(str(C0)))
assert abs(D(str(bestcg[0]))-cg_exact) < D("1e-12")
assert cg_exact < 0

print("PASS two-quarter balanced arity-5 certificate")
print("feasible_count_tuples", len(feasible))
print("raw_balanced_gates", raw_balanced)
print("orbit_representatives_evaluated", n_eval)
print("screened_Creq_gt_6.15", n_gt_615)
print("distinct_signatures_Creq_gt_6.0", len(high))
print("Creq_max_exact", Cexact)
print("Creq_next_distinct_upper_screen", replayed[3][0])
print("maximizing_witness", witness)
print("witness_hist_numerators_over_16384", sorted(hist.items()))
print("witness_A_B", Aw[0], Bw[0])
print("physical_AND2_composite_H_I_ratio", Hphys, Iphys, Hphys/(Iphys-1))
print("c_G_max_at_C0_6.4548", cg_exact)
