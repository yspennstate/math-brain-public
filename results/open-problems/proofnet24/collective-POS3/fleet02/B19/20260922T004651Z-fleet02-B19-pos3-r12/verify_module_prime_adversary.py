#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

N = 15
CHAINS = [tuple(range(0,5)), tuple(range(5,10)), tuple(range(10,15))]
LSTAR = (0,10,5,6,1,11,2,7,12,3,13,8,9,4,14)
COVERS = (
    (0,1),(0,5),
    (1,2),
    (2,3),(2,12),
    (3,4),(3,9),
    (5,6),(5,11),
    (6,2),(6,7),
    (7,4),(7,8),
    (8,9),
    (9,14),
    (10,1),(10,11),
    (11,12),
    (12,8),(12,13),
    (13,4),(13,14),
)

def closure():
    reach = [0]*N
    for u,v in COVERS:
        reach[u] |= 1<<v
    for k in range(N):
        bit = 1<<k
        for i in range(N):
            if reach[i] & bit:
                reach[i] |= reach[k]
    return reach

REACH = closure()

def pred_masks():
    p = [0]*N
    for u in range(N):
        for v in range(N):
            if (REACH[u]>>v)&1:
                p[v] |= 1<<u
    return p

PRED = pred_masks()

def enumerate_extensions():
    out=[]
    def rec(mask, seq):
        if mask == (1<<N)-1:
            out.append(tuple(seq)); return
        for x in range(N):
            bx=1<<x
            if mask & bx: continue
            if PRED[x] & ~mask: continue
            seq.append(x); rec(mask|bx,seq); seq.pop()
    rec(0,[])
    return out

EXTS = enumerate_extensions()
E=len(EXTS)

def comparable(a,b):
    return ((REACH[a]>>b)&1) or ((REACH[b]>>a)&1)

INCOMPARABLE = [(a,b) for a in range(N) for b in range(a+1,N) if not comparable(a,b)]

def frac_str(n,d):
    f=Fraction(n,d)
    return f"{f.numerator}/{f.denominator}"

positions=[None]*E
for k,e in enumerate(EXTS):
    p=[0]*N
    for i,x in enumerate(e): p[x]=i
    positions[k]=p

pair_counts={}
balanced=[]
for a,b in INCOMPARABLE:
    n=sum(1 for p in positions if p[a]<p[b])
    pair_counts[(a,b)]=n
    q=Fraction(n,E)
    if Fraction(1,3) <= q <= Fraction(2,3):
        balanced.append((a,b,q))

def antichain(sub):
    return all(not comparable(a,b) for a,b in combinations(sub,2))

anti3=next(c for c in combinations(range(N),3) if antichain(c))
anti4=next((c for c in combinations(range(N),4) if antichain(c)),None)

inc_adj={x:set() for x in range(N)}
for a,b in INCOMPARABLE:
    inc_adj[a].add(b); inc_adj[b].add(a)
seen=set()
stack=[0]
while stack:
    x=stack.pop()
    if x in seen: continue
    seen.add(x); stack.extend(inc_adj[x]-seen)
inc_connected=(len(seen)==N)

def autonomous(A):
    A=set(A)
    for z in range(N):
        if z in A: continue
        rel=set()
        for a in A:
            if (REACH[z]>>a)&1: rel.add(-1)
            elif (REACH[a]>>z)&1: rel.add(1)
            else: rel.add(0)
        if len(rel)!=1: return False
    return True

modules=[]
for mask in range(1,1<<N):
    k=mask.bit_count()
    if k<2 or k==N: continue
    A=tuple(i for i in range(N) if (mask>>i)&1)
    if autonomous(A): modules.append(A)

posL={x:i for i,x in enumerate(LSTAR)}
assert all(posL[u]<posL[v] for u in range(N) for v in range(N) if (REACH[u]>>v)&1)

nonbalanced_agree=True
for a,b in INCOMPARABLE:
    n=pair_counts[(a,b)]
    q=Fraction(n,E)
    if q<Fraction(1,3):
        winner=(b,a)
    elif q>Fraction(2,3):
        winner=(a,b)
    else:
        continue
    if not (posL[winner[0]]<posL[winner[1]]):
        nonbalanced_agree=False

def gap(extpos,x,chain):
    return sum(extpos[y]<extpos[x] for y in chain)

slice_rows=[]
for x in range(N):
    cx=next(i for i,c in enumerate(CHAINS) if x in c)
    for ci,c in enumerate(CHAINS):
        if ci==cx: continue
        arr=[0]*6
        for p in positions:
            arr[gap(p,x,c)] += 1
        g=sum(posL[y]<posL[x] for y in c)
        relevant=any(not comparable(x,y) for y in c)
        uniq=(arr.count(max(arr))==1 and arr[g]==max(arr))
        heavy=(3*arr[g] > E)
        before=sum(arr[:g])
        through=sum(arr[:g+1])
        band=(3*before < E and 3*through > 2*E)
        slice_rows.append((x,ci,g,tuple(arr),relevant,uniq,heavy,before,through,band))

cell_rows=[]
for x in range(N):
    cx=next(i for i,c in enumerate(CHAINS) if x in c)
    others=[i for i in range(3) if i!=cx]
    c1,c2=(CHAINS[i] for i in others)
    g1=sum(posL[y]<posL[x] for y in c1)
    g2=sum(posL[y]<posL[x] for y in c2)
    n=0
    for p in positions:
        if gap(p,x,c1)==g1 and gap(p,x,c2)==g2:
            n+=1
    cell_rows.append((x,others[0],g1,others[1],g2,n))

relevant_rows=[r for r in slice_rows if r[4]]
min_heavy=min((r[3][r[2]],r[0],r[1],r[2]) for r in relevant_rows)
min_cell=min((r[5],r[0],r[2],r[4]) for r in cell_rows)
band_pass=sum(r[9] for r in relevant_rows)

print("POS3 exact module-prime adversary verification")
print(f"N={N}")
print(f"E={E}")
print("covers="+" ".join(f"{u}<{v}" for u,v in COVERS))
print(f"width_witness_3={anti3}")
print(f"antichain_size_4={anti4}")
print(f"width=3")
print(f"incomparability_connected={inc_connected}")
print(f"incomparable_pairs={len(INCOMPARABLE)}")
print(f"nontrivial_autonomous_modules={len(modules)}")
print(f"Lstar={LSTAR}")
print(f"Lstar_is_linear_extension=True")
print(f"majority_orientations_of_all_nonbalanced_pairs_agree_with_Lstar={nonbalanced_agree}")
print(f"balanced_pairs={len(balanced)}")
print("ALL_INCOMPARABLE_PAIR_PROBABILITIES p(a<b):")
for a,b in INCOMPARABLE:
    n=pair_counts[(a,b)]
    q=Fraction(n,E)
    tag="BALANCED" if Fraction(1,3)<=q<=Fraction(2,3) else "UNBALANCED"
    print(f"  ({a},{b}) {q.numerator}/{q.denominator} count={n}/{E} {tag}")
print(f"relevant_chain_marginals={len(relevant_rows)}")
print(f"all_relevant_Lstar_gap_marginals_unique_max={all(r[5] for r in relevant_rows)}")
print(f"all_relevant_Lstar_gap_marginals_gt_1_3={all(r[6] for r in relevant_rows)}")
print(f"minimum_relevant_peak={min_heavy[0]}/{E}={frac_str(min_heavy[0],E)} at x={min_heavy[1]} other_chain={min_heavy[2]} gap={min_heavy[3]}")
print(f"all_Lstar_central_cells_ge_1_19683={all(19683*r[5] >= E for r in cell_rows)}")
print(f"minimum_Lstar_central_cell={min_cell[0]}/{E}={frac_str(min_cell[0],E)} at x={min_cell[1]} gaps=({min_cell[2]},{min_cell[3]})")
print(f"strict_band_rows_pass={band_pass}/{len(relevant_rows)}")
print(f"strict_band_rows_fail={len(relevant_rows)-band_pass}/{len(relevant_rows)}")
print("FAILED_STRICT_BAND_ROWS x other_chain gap before through:")
for r in relevant_rows:
    if not r[9]:
        print(f"  {r[0]} {r[1]} {r[2]} {r[7]} {r[8]}")
