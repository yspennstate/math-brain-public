#!/usr/bin/env python3
from math import comb
from itertools import product
from collections import Counter

# Exact finite certificate for C30, n=11, m=28,29,30.
# No floating point is used.

DEN = 19
MU = 309420
LAM = {4:0,5:0,6:9020,7:0,8:0,9:0,10:0}
A = {
(4,4):-638130,(4,5):-607350,(4,6):-598500,(4,7):-546640,(4,8):-533720,(4,9):-519280,(4,10):-503320,
(5,5):-576570,(5,6):-567720,(5,7):-538280,(5,8):-525360,(5,9):-510920,(5,10):-494960,
(6,6):-575880,(6,7):-546440,(6,8):-533520,(6,9):-519080,(6,10):-503120,
(7,7):-517000,(7,8):-504080,(7,9):-489640,(7,10):-473680,
(8,8):-491160,(8,9):-476720,(8,10):-460760,
(9,9):-462280,(9,10):-446320,
(10,10):-430360,
}

def p2(d,e,c):
    return 10*c**5 + 5*(d+e)*c**4 + 5*(d*d+e*e)*c**3

def wpair(d,e,c):
    return p2(d,e,c) + 5280*comb(c,3)

def all_degree_sequences(total):
    out=[]
    def rec(pos,last,left,a):
        if pos==11:
            if left==0: out.append(tuple(a))
            return
        rem=11-pos
        for d in range(last,11):
            if left-d < d*(rem-1) or left-d > 10*(rem-1):
                continue
            rec(pos+1,d,left-d,a+[d])
    rec(0,4,total,[])
    return out

# 1. Word-pattern checks used in the support decomposition.
bin_types=Counter()
for w in product(range(2), repeat=5):
    if len(set(w)) != 2: continue
    mono=[0,0]
    for i in range(5):
        S={w[i],w[(i+1)%5],w[(i+2)%5]}
        if len(S)==1: mono[next(iter(S))]+=1
    bin_types[tuple(mono)] += 1
assert bin_types == Counter({(0,0):10,(2,0):5,(1,0):5,(0,1):5,(0,2):5})

tri_no_mono=0
tri_unique=[0,0,0]
for w in product(range(3), repeat=5):
    if set(w)!={0,1,2}: continue
    monos=[]
    for i in range(5):
        S={w[i],w[(i+1)%5],w[(i+2)%5]}
        if len(S)==1: monos.append(next(iter(S)))
    if not monos:
        tri_no_mono += 1
    else:
        assert len(monos)==1
        tri_unique[monos[0]] += 1
assert tri_no_mono == 120 and tri_unique == [10,10,10]

surj4=sum(1 for w in product(range(4), repeat=5) if set(w)==set(range(4)))
surj5=sum(1 for w in product(range(5), repeat=5) if set(w)==set(range(5)))
assert surj4 == 240 and surj5 == 120

# 2. Support-three scalar minorant for delta >=4.
minorant_min=None
for t in range(0,11):
    q=max(4,t)
    lhs=120*t**5 + 30*q*t**4
    rhs=240*t + 5280*comb(t,2)
    slack=lhs-rhs
    assert slack >= 0
    minorant_min=slack if minorant_min is None else min(minorant_min,slack)

# 3. Universal exact pair-profile dual inequality.
pointwise_min=None
pointwise_arg=None
for d in range(4,11):
    for e in range(d,11):
        for c in range(0,min(d,e)+1):
            slack = DEN*wpair(d,e,c) - (A[(d,e)] + MU*c + (LAM[d]+LAM[e])*c)
            assert slack >= 0
            if pointwise_min is None or slack < pointwise_min:
                pointwise_min,pointwise_arg=slack,(d,e,c)

# 4. Exact deletion branch and high-min-degree degree-profile certificate.
print('C30 support-profile exact certificate for n=11, m=28,29,30')
print('arithmetic=integer_exact; floating_point_decisions=NONE')
print(f'binary_word_types={dict(sorted(bin_types.items()))} PASS')
print(f'triple_words_no_mono={tri_no_mono} unique_mono_by_symbol={tri_unique} PASS')
print(f'surjective_word_counts: support4={surj4} support5={surj5} PASS')
print(f'support3_minorant_min_slack={minorant_min} PASS')
print(f'pair_dual_pointwise_min_slack={pointwise_min} at={pointwise_arg} PASS')

for m in (28,29,30):
    deletion_margins=[]
    for d in range(0,4):
        # ((m-d)/m)^15 >= (10/11)^20
        margin=(m-d)**15 * 11**20 - m**15 * 10**20
        assert margin > 0
        deletion_margins.append(margin)

    seqs=all_degree_sequences(2*m)
    worst=None
    for seq in seqs:
        cnt=Counter(seq)
        delta=min(seq)
        T2=sum(comb(d,2) for d in seq)
        T3=sum(comb(d,3) for d in seq)
        T4=sum(comb(d,4) for d in seq)
        T5=sum(comb(d,5) for d in seq)
        support_other=sum(d**5 for d in seq) + 240*T3 + 240*T4 + 120*T5

        pair_scaled=MU*T2
        pair_scaled += sum(LAM[d]*cnt[d]*d*(delta-1) for d in range(4,11))
        for d in range(4,11):
            for e in range(d,11):
                N = cnt[d]*(cnt[d]-1)//2 if d==e else cnt[d]*cnt[e]
                pair_scaled += A[(d,e)]*N

        # DEN*hom >= DEN*support_other + pair_scaled.
        lhs_scaled=DEN*support_other + pair_scaled
        source_margin = lhs_scaled * 11**20 - DEN*(2*m)**15
        assert source_margin > 0
        item=(source_margin,lhs_scaled,seq)
        if worst is None or item < worst:
            worst=item

    margin,lhs_scaled,seq=worst
    print(f'm={m} deletion_min_margin={min(deletion_margins)} PASS')
    print(f'm={m} degree_sequences_checked={len(seqs)} worst_sequence={seq}')
    print(f'm={m} worst_scaled_lower={lhs_scaled}/{DEN} source_cross_margin={margin} PASS')

print('ALL_EXACT_CHECKS_PASS')
