#!/usr/bin/env python3
from collections import Counter
from itertools import product
from math import comb

# Independent exact-arithmetic audit of C30-N11-M28-M30-SUPPORT-PROFILE-03.
# This checker is claim-scoped: n=11 and m in {28,29,30} only.
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

def degree_profiles(total):
    out=[]
    def rec(pos,last,left,acc):
        if pos==11:
            if left==0:
                out.append(tuple(acc))
            return
        rem=11-pos
        for d in range(last,11):
            new_left=left-d
            if new_left < d*(rem-1) or new_left > 10*(rem-1):
                continue
            rec(pos+1,d,new_left,acc+[d])
    rec(0,4,total,[])
    return out

# Recount the support-three cyclic words independently.
tri_no_mono=0
tri_one=[0,0,0]
for w in product(range(3), repeat=5):
    if set(w)!={0,1,2}:
        continue
    mono=[]
    for i in range(5):
        a,b,c=w[i],w[(i+1)%5],w[(i+2)%5]
        if a==b==c:
            mono.append(a)
    if not mono:
        tri_no_mono += 1
    else:
        assert len(mono)==1
        tri_one[mono[0]] += 1
assert tri_no_mono==120
assert tri_one==[10,10,10]

# Independently verify the pointwise dual inequality on its complete integer domain.
pointwise=(None,None)
for d in range(4,11):
    for e in range(d,11):
        for c in range(0,min(d,e)+1):
            slack = DEN*wpair(d,e,c) - (A[(d,e)] + (MU+LAM[d]+LAM[e])*c)
            assert slack >= 0
            if pointwise[0] is None or slack < pointwise[0]:
                pointwise=(slack,(d,e,c))
assert pointwise==(0,(4,4,3))

print('C29 independent audit of C30-N11-M28-M30-SUPPORT-PROFILE-03')
print('arithmetic=integer_exact; floating_point_decisions=NONE')
print(f'triple_words_no_mono={tri_no_mono}; unique_mono_by_symbol={tri_one}; PASS')
print(f'pair_dual_min_slack={pointwise[0]} at={pointwise[1]}; PASS')

expected={
28:(57,(5,5,5,5,5,5,5,5,5,5,6),5798504,727184093687848641494160360),
29:(86,(5,5,5,5,5,5,5,5,6,6,6),9833572,1243071632424315147339376164),
30:(124,(4,5,5,5,5,6,6,6,6,6,6),13800600,350838873122287662979320600),
}
for m in (28,29,30):
    profiles=degree_profiles(2*m)
    best=None
    for seq in profiles:
        cnt=Counter(seq)
        delta=min(seq)
        T2=sum(comb(d,2) for d in seq)
        T3=sum(comb(d,3) for d in seq)
        T4=sum(comb(d,4) for d in seq)
        T5=sum(comb(d,5) for d in seq)
        support_other=sum(d**5 for d in seq)+240*T3+240*T4+120*T5
        pair_scaled=MU*T2
        pair_scaled += sum(LAM[d]*cnt[d]*d*(delta-1) for d in range(4,11))
        for d in range(4,11):
            for e in range(d,11):
                mult=cnt[d]*(cnt[d]-1)//2 if d==e else cnt[d]*cnt[e]
                pair_scaled += A[(d,e)]*mult
        lhs_scaled=DEN*support_other+pair_scaled
        margin=lhs_scaled*11**20-DEN*(2*m)**15
        assert margin>0
        candidate=(margin,lhs_scaled,seq)
        if best is None or candidate<best:
            best=candidate
    count,wseq,wlhs,wmargin=expected[m]
    assert len(profiles)==count
    assert best==(wmargin,wlhs,wseq)
    print(f'm={m}; profiles={len(profiles)}; weakest={best[2]}; scaled_lower={best[1]}/{DEN}; source_cross_margin={best[0]}; PASS')

print('C29-AUDIT-C30-N11-M28-M30-SUPPORT-PROFILE-04 = PASS (claim-scoped)')
print('ALL_EXACT_CHECKS_PASS')
