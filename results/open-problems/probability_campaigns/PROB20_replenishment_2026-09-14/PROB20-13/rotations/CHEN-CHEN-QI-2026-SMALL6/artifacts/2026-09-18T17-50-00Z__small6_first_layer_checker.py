from itertools import combinations, permutations
from fractions import Fraction
from collections import Counter

P = 1000003

ROWS = [
    (0,1,2),
    (0,3,4),
    (1,3,5),
    (2,4,5),
    (0,5),
    (1,4),
]
E1 = [(r,c) for r,cs in enumerate(ROWS) for c in cs]
E1SET = set(E1)
FREE = [(r,c) for r in range(6) for c in range(6) if (r,c) not in E1SET]

RPAIRS = [(r,s) for r in range(6) for s in range(r,6)]
CPAIRS = [(c,d) for c in range(6) for d in range(c,6)]
COORDS = [(rp,cp) for rp in RPAIRS for cp in CPAIRS]
COORD = {x:i for i,x in enumerate(COORDS)}


def prod_vec(form1, form2):
    out = {}
    for r,c in form1:
        for s,d in form2:
            k = COORD[((min(r,s),max(r,s)),(min(c,d),max(c,d)))]
            out[k] = out.get(k,0) + 1
    return out

BASE_FORMS = [(x,) for x in E1]
BASE_PRODUCTS = [prod_vec(BASE_FORMS[i],BASE_FORMS[j])
                 for i in range(len(BASE_FORMS)) for j in range(i+1,len(BASE_FORMS))]
assert len(BASE_PRODUCTS) == 120
assert all(len(v)==1 and next(iter(v.values()))==1 for v in BASE_PRODUCTS)
BASE_COORDS = {next(iter(v)) for v in BASE_PRODUCTS}
assert len(BASE_COORDS) == 120


def qvec(form1, form2):
    return {k:v for k,v in prod_vec(form1,form2).items()
            if k not in BASE_COORDS and v}


def additional_mixed_products(e2s):
    forms = [tuple(e) for e in e2s]
    out = []
    for f in forms:
        for b in BASE_FORMS:
            out.append(qvec(b,f))
    for i in range(len(forms)):
        for j in range(i+1,len(forms)):
            out.append(qvec(forms[i],forms[j]))
    return out


def rank_mod(rows, p=P):
    piv = {}
    rank = 0
    for row0 in rows:
        row = {k:(v % p) for k,v in row0.items() if v % p}
        while row:
            j = min(row)
            if j not in piv:
                inv = pow(row[j], p-2, p)
                row = {k:(v*inv) % p for k,v in row.items() if (v*inv) % p}
                piv[j] = row
                rank += 1
                break
            a = row[j]
            pr = piv[j]
            for k,v in pr.items():
                nv = (row.get(k,0) - a*v) % p
                if nv:
                    row[k] = nv
                elif k in row:
                    del row[k]
    return rank


def rank_q(rows):
    piv = {}
    rank = 0
    for row0 in rows:
        row = {k:Fraction(v) for k,v in row0.items() if v}
        while row:
            j = min(row)
            if j not in piv:
                a = row[j]
                row = {k:v/a for k,v in row.items() if v}
                piv[j] = row
                rank += 1
                break
            a = row[j]
            pr = piv[j]
            for k,v in pr.items():
                nv = row.get(k,Fraction(0)) - a*v
                if nv:
                    row[k] = nv
                elif k in row:
                    del row[k]
    return rank


def c4_free():
    for r,s in combinations(range(6),2):
        if len(set(ROWS[r]) & set(ROWS[s])) >= 2:
            return False
    return True


def layer(m, z, total):
    e2 = total-z
    H = 6*m - z - 2*e2
    return e2,H

TARGETS = {
    (6,25): layer(6,16,25),
    (6,26): layer(6,16,26),
    (7,29): layer(7,18,29),
    (7,30): layer(7,18,30),
}
assert TARGETS == {(6,25):(9,2),(6,26):(10,0),(7,29):(11,2),(7,30):(12,0)}
assert c4_free()
assert len(E1)==16 and len(FREE)==20

CAND = list(combinations(FREE,2))
assert len(CAND)==190
BAD_SINGLE=[]
GOOD=[]
for e in CAND:
    vs = additional_mixed_products([e])
    assert len(vs)==16
    rm = rank_mod(vs)
    if rm < 16:
        rq = rank_q(vs)
        assert rq == rm
        BAD_SINGLE.append((e,rq))
    else:
        GOOD.append(e)
assert len(BAD_SINGLE)==56
assert len(GOOD)==134
assert Counter(r for _,r in BAD_SINGLE)==Counter({15:56})

PAIR_BAD=[]
PAIR_GOOD=[]
PAIR_DISJOINT=0
for i,e in enumerate(GOOD):
    se=set(e)
    for f in GOOD[i+1:]:
        if not se.isdisjoint(f):
            continue
        PAIR_DISJOINT += 1
        vs = additional_mixed_products([e,f])
        assert len(vs)==33
        rm = rank_mod(vs)
        if rm < 33:
            rq = rank_q(vs)
            assert rq == rm
            PAIR_BAD.append((e,f,rq))
        else:
            PAIR_GOOD.append((e,f))
assert PAIR_DISJOINT==7247
assert len(PAIR_BAD)==122
assert len(PAIR_GOOD)==7125
assert Counter(r for _,_,r in PAIR_BAD)==Counter({32:98,31:24})

PERMS=list(permutations(range(6)))
AUT=[]
rowsets=[set(x) for x in ROWS]
for pr in PERMS:
    for pc in PERMS:
        if all({pc[c] for c in rowsets[r]} ==
               {c for rr,c in E1SET if rr==pr[r]} for r in range(6)):
            AUT.append((pr,pc))
assert len(AUT)==8


def apply_cell(x,a):
    pr,pc=a; r,c=x
    return (pr[r],pc[c])


def canon_edge(e):
    return tuple(sorted(e))


def edge_orbit(e):
    return {canon_edge((apply_cell(e[0],a),apply_cell(e[1],a))) for a in AUT}

seen=set(); single_orbits=[]
goodset=set(GOOD)
for e in CAND:
    if e in seen: continue
    orb=edge_orbit(e); seen |= orb
    single_orbits.append((e,len(orb),e in goodset))
assert len(single_orbits)==31
assert sum(g for _,_,g in single_orbits)==23
assert sum(not g for _,_,g in single_orbits)==8


def canon_pair(p):
    return tuple(sorted((canon_edge(p[0]),canon_edge(p[1]))))


def pair_orbit(p):
    out=set()
    for a in AUT:
        e=canon_edge((apply_cell(p[0][0],a),apply_cell(p[0][1],a)))
        f=canon_edge((apply_cell(p[1][0],a),apply_cell(p[1][1],a)))
        out.add(canon_pair((e,f)))
    return out

pair_bad_set={canon_pair((e,f)) for e,f,_ in PAIR_BAD}
all_pairs=[canon_pair((e,f)) for e,f,_ in PAIR_BAD] + [canon_pair((e,f)) for e,f in PAIR_GOOD]
seen=set(); pair_orbits=[]
for p in all_pairs:
    if p in seen: continue
    orb=pair_orbit(p); seen |= orb
    pair_orbits.append((p,len(orb),p in pair_bad_set))
assert len(pair_orbits)==962
assert sum(b for _,_,b in pair_orbits)==21
assert sum(not b for _,_,b in pair_orbits)==941

print('TARGET_LAYERS=', TARGETS)
print('M6_E1=', len(E1), 'M6_FREE_CELLS=', len(FREE), 'C4_FREE=', c4_free())
print('M6_SINGLE_E2_TOTAL=', len(CAND))
print('M6_SINGLE_PRODUCT_RELATION_BAD=', len(BAD_SINGLE), 'rank_hist=', dict(sorted(Counter(r for _,r in BAD_SINGLE).items())))
print('M6_SINGLE_COMPATIBLE=', len(GOOD))
print('M6_DISJOINT_GOOD_PAIR_CASES=', PAIR_DISJOINT)
print('M6_PAIR_ADDITIONAL_PRODUCT_RELATION_BAD=', len(PAIR_BAD), 'rank_hist=', dict(sorted(Counter(r for _,_,r in PAIR_BAD).items())))
print('M6_PAIR_COMPATIBLE=', len(PAIR_GOOD))
print('M6_SKELETON_AUT_GROUP_ORDER=', len(AUT))
print('M6_SINGLE_ORBITS=', len(single_orbits), 'bad_orbits=', sum(not g for _,_,g in single_orbits), 'good_orbits=', sum(g for _,_,g in single_orbits))
print('M6_PAIR_ORBITS=', len(pair_orbits), 'bad_orbits=', sum(b for _,_,b in pair_orbits), 'good_orbits=', sum(not b for _,_,b in pair_orbits))
print('ALL_EXACT_CHECKS_PASS')
