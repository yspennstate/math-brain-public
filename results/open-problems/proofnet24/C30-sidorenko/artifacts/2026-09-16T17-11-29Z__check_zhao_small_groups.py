#!/usr/bin/env python3
from itertools import product, permutations
from math import gcd

# Frozen H = K_{5,5} \ C_10, with right vertex i adjacent to left i,i+1,i+2 mod 5.
E = [(i, (i+j)%5) for i in range(5) for j in (0,1,2)]
assert len(E)==15

def make_group(elements, mul):
    idx={g:i for i,g in enumerate(elements)}
    n=len(elements)
    table=[[idx[mul(a,b)] for b in elements] for a in elements]
    e=None
    for i in range(n):
        if all(table[i][j]==j and table[j][i]==j for j in range(n)):
            e=i; break
    assert e is not None
    inv=[None]*n
    for i in range(n):
        for j in range(n):
            if table[i][j]==e and table[j][i]==e:
                inv[i]=j; break
        assert inv[i] is not None
    conj=[[None]*n for _ in range(n)]
    for h in range(n):
        for x in range(n):
            conj[h][x]=table[table[h][x]][inv[h]]
    return table, inv, conj

def compose(p,q):
    # (p*q)(i)=p(q(i))
    return tuple(p[q[i]] for i in range(len(p)))

S3=list(permutations(range(3)))
S3_table,S3_inv,S3_conj=make_group(S3, compose)

D4=[(r,s) for r in range(4) for s in range(2)]
def d4mul(a,b):
    r,s=a; q,t=b
    return ((r + (q if s==0 else -q))%4, (s+t)%2)
D4_table,D4_inv,D4_conj=make_group(D4,d4mul)

def raw_hom_cayley(a, table, inv):
    """Unnormalized sum over all 10 vertex maps of product of edge weights.
    K[x][y] = a[x^{-1} y]. Exact integer arithmetic.
    Uses the 5-right-vertex common-neighbor contraction.
    """
    g=len(a)
    K=[[a[table[inv[x]][y]] for y in range(g)] for x in range(g)]
    C=[[[0]*g for _ in range(g)] for __ in range(g)]
    for x in range(g):
        for y in range(g):
            for z in range(g):
                C[x][y][z]=sum(K[x][u]*K[y][u]*K[z][u] for u in range(g))
    total=0
    for xs in product(range(g), repeat=5):
        prodv=1
        for i in range(5):
            prodv *= C[xs[i]][xs[(i+1)%5]][xs[(i+2)%5]]
            if prodv==0:
                break
        total += prodv
    return total

def raw_hom_direct(a, table, inv):
    # Independent direct five-left-variable contraction for tiny cross-checks.
    g=len(a)
    total=0
    for left in product(range(g), repeat=5):
        prodv=1
        for i in range(5):
            s=0
            for u in range(g):
                q=1
                for j in (0,1,2):
                    x=left[(i+j)%5]
                    q *= a[table[inv[x]][u]]
                s += q
            prodv *= s
        total += prodv
    return total

def class_sum(a, conj):
    g=len(a)
    # b(x) = sum_h a(h x h^{-1}) = g * a_cl(x)
    return [sum(a[conj[h][x]] for h in range(g)) for x in range(g)]

def exhaustive(name, table, inv, conj, alphabet):
    g=len(table)
    total_cases=0
    bad=[]
    equality=0
    min_positive_slack=None
    min_positive_witness=None
    min_ratio_pair=None
    tests=[(0,)*g,(1,)*g,tuple(range(g))]
    for a in tests:
        f=raw_hom_cayley(a,table,inv)
        d=raw_hom_direct(a,table,inv)
        assert f==d, (name,a,f,d)
    direct_pass=len(tests)

    for a in product(alphabet, repeat=g):
        total_cases += 1
        rawa=raw_hom_cayley(a,table,inv)
        b=class_sum(a,conj)
        rawb=raw_hom_cayley(b,table,inv)
        lhs=(g**15)*rawa
        rhs=rawb
        slack=lhs-rhs
        if slack<0:
            bad.append((a,lhs,rhs,slack))
            break
        if slack==0:
            equality += 1
        elif min_positive_slack is None or slack<min_positive_slack:
            min_positive_slack=slack
            min_positive_witness=a
        if rhs>0:
            if min_ratio_pair is None:
                min_ratio_pair=(lhs,rhs,a)
            else:
                n0,d0,_=min_ratio_pair
                if lhs*d0 < n0*rhs:
                    min_ratio_pair=(lhs,rhs,a)
    assert not bad, bad[:1]
    return {
        'name':name,
        'group_order':g,
        'alphabet':tuple(alphabet),
        'cases':total_cases,
        'equalities':equality,
        'min_positive_slack':min_positive_slack,
        'min_positive_witness':min_positive_witness,
        'min_ratio_pair':min_ratio_pair,
        'direct_cross_checks':direct_pass,
    }

def fmt(res):
    lines=[]
    lines.append(f"{res['name']} alphabet={res['alphabet']} group_order={res['group_order']} cases={res['cases']} violations=0 PASS")
    lines.append(f"{res['name']} direct_vs_contraction_checks={res['direct_cross_checks']} PASS")
    lines.append(f"{res['name']} equalities={res['equalities']}")
    lines.append(f"{res['name']} min_positive_slack={res['min_positive_slack']} witness={res['min_positive_witness']}")
    if res['min_ratio_pair']:
        n,d,a=res['min_ratio_pair']
        gg=gcd(n,d)
        lines.append(f"{res['name']} min_nonzero_ratio_exact={n//gg}/{d//gg} witness={a}")
    return '\n'.join(lines)

def main():
    print('C30 Zhao conjugacy-averaging exact small-group search')
    print('H=K_{5,5}\\C_10; right i adjacent to left i,i+1,i+2 mod5; e(H)=15')
    print('comparison_exact: |Gamma|^15 Raw(a) >= Raw(sum_h a(h x h^-1))')
    print('arithmetic=integer_exact; floating_point_decisions=NONE')
    runs=[
        exhaustive('S3-binary',S3_table,S3_inv,S3_conj,(0,1)),
        exhaustive('S3-ternary',S3_table,S3_inv,S3_conj,(0,1,2)),
        exhaustive('D4-binary',D4_table,D4_inv,D4_conj,(0,1)),
    ]
    for r in runs:
        print(fmt(r))
    print(f"total_exhaustive_cases={sum(r['cases'] for r in runs)}")
    print('ALL_EXACT_CHECKS_PASS')

if __name__=='__main__':
    main()
