#!/usr/bin/env python3
"""
Exact/self-check for PROB10-01 root pivotal and square-pivotal stopping-tree identities.

All tree/influence/curvature checks use fractions/integers.  No entropy
floating point is used.  These checks support, but do not replace, the
all-dimensional proofs in the accompanying report.
"""
from fractions import Fraction
from itertools import combinations
import random, json

SEED = 20260920

class Node:
    __slots__=("coord","one","zero")
    def __init__(self, coord=None, one=None, zero=None):
        self.coord=coord
        self.one=one
        self.zero=zero
    @property
    def leaf(self):
        return self.coord is None

def random_tree(n, rng, free=None, depth=0, max_depth=None, stop_p=Fraction(1,3)):
    if free is None:
        free=tuple(range(n))
    if max_depth is None:
        max_depth=n
    if depth>=max_depth or not free or (depth>0 and rng.randrange(stop_p.denominator) < stop_p.numerator):
        return Node()
    i=rng.choice(list(free))
    rest=tuple(k for k in free if k != i)
    return Node(
        i,
        random_tree(n,rng,rest,depth+1,max_depth,stop_p),
        random_tree(n,rng,rest,depth+1,max_depth,stop_p),
    )

def cylinder_points(n, assign):
    for x in range(1<<n):
        if all(((x>>i)&1)==b for i,b in assign.items()):
            yield x

def inf_coord(vals,n,i,assign):
    pts=list(cylinder_points(n,assign))
    bad=sum(vals[x] != vals[x^(1<<i)] for x in pts)
    return Fraction(bad,len(pts))

def total_inf(vals,n,assign):
    return sum((inf_coord(vals,n,i,assign) for i in range(n) if i not in assign), Fraction())

def square_prob(vals,n,i,k,assign):
    pts=list(cylinder_points(n,assign))
    bad=0
    for x in pts:
        prod=vals[x]*vals[x^(1<<i)]*vals[x^(1<<k)]*vals[x^(1<<i)^(1<<k)]
        bad += (prod == -1)
    return Fraction(bad,len(pts))

def tree_resource_sums(vals,n,root):
    # Q: queried influence. C: consumed square curvature.
    # IL: average residual leaf influence.
    # D: descendant influence sum from NM13-02 equation (3.3).
    Q=C=IL=D=Fraction()
    leaf_C2=Fraction()
    def rec(node,assign,w):
        nonlocal Q,C,IL,D,leaf_C2
        if node.leaf:
            IL += w*total_inf(vals,n,assign)
            free=[i for i in range(n) if i not in assign]
            leaf_C2 += w*sum((square_prob(vals,n,i,k,assign) for i,k in combinations(free,2)), Fraction())
            return
        i=node.coord
        Q += w*inf_coord(vals,n,i,assign)
        C += w*sum((square_prob(vals,n,i,k,assign)
                    for k in range(n) if k not in assign and k != i), Fraction())
        for b,ch in ((1,node.one),(0,node.zero)):
            aa=dict(assign); aa[i]=b
            ww=w*Fraction(1,2)
            D += ww*total_inf(vals,n,aa)
            rec(ch,aa,ww)
    rec(root,{},Fraction(1))
    return Q,C,IL,D,leaf_C2

def path_queries(root,x):
    node=root
    out=[]
    while not node.leaf:
        i=node.coord
        out.append(i)
        node=node.one if ((x>>i)&1) else node.zero
    return out

def root_event_sums(vals,n,root):
    N=1<<n
    Q=C=IL=D=Fraction()
    for x in range(N):
        order=path_queries(root,x)
        qset=set(order)
        pos={i:r+1 for r,i in enumerate(order)}
        depth=len(order)
        for i in range(n):
            piv=(vals[x] != vals[x^(1<<i)])
            if not piv:
                continue
            if i in qset:
                Q += Fraction(1,N)
                ell=pos[i]-1
            else:
                IL += Fraction(1,N)
                ell=depth
            D += Fraction(ell,N)
        for i,k in combinations(range(n),2):
            sq=(vals[x]*vals[x^(1<<i)]*vals[x^(1<<k)]*vals[x^(1<<i)^(1<<k)] == -1)
            if sq and (i in qset or k in qset):
                C += Fraction(1,N)
    return Q,C,IL,D

def root_C2(vals,n):
    return sum((square_prob(vals,n,i,k,{}) for i,k in combinations(range(n),2)), Fraction())

def all_truth_tables(n):
    N=1<<n
    for mask in range(1<<N):
        yield [(-1 if ((mask>>x)&1) else 1) for x in range(N)]

def cubic_star(r):
    # x0 plus y1,...,y_{2r}; (-1)^{x0 sum y_{2s-1}y_{2s}}
    n=2*r+1
    vals=[]
    for x in range(1<<n):
        p=0
        x0=(x>>0)&1
        if x0:
            for s in range(r):
                y1=(x>>(1+2*s))&1
                y2=(x>>(2+2*s))&1
                p ^= (y1 & y2)
        vals.append(-1 if p else 1)
    return vals,n

rng=random.Random(SEED)
tree_cases=0
identity_failures=0
max_denominator=1

# Exhaust every Boolean function through dimension 3, with several adaptive trees.
for n in range(1,4):
    for vals in all_truth_tables(n):
        for _ in range(5):
            T=random_tree(n,rng,max_depth=n,stop_p=Fraction(1,3))
            lhs=tree_resource_sums(vals,n,T)
            rhs=root_event_sums(vals,n,T)
            if lhs[:4] != rhs:
                identity_failures += 1
                raise AssertionError((n,lhs,rhs))
            if lhs[1] + lhs[4] != root_C2(vals,n):
                identity_failures += 1
                raise AssertionError(("C2 telescope",n,lhs,root_C2(vals,n)))
            tree_cases += 1
            for q in lhs:
                max_denominator=max(max_denominator,q.denominator)

# Larger deterministic random stress.
random_function_tree_cases=0
for n in (4,5):
    for _ in range(300):
        vals=[rng.choice((-1,1)) for _ in range(1<<n)]
        T=random_tree(n,rng,max_depth=n,stop_p=Fraction(2,5))
        lhs=tree_resource_sums(vals,n,T)
        rhs=root_event_sums(vals,n,T)
        assert lhs[:4] == rhs
        assert lhs[1] + lhs[4] == root_C2(vals,n)
        random_function_tree_cases += 1

# Cubic-star central-query exact check: C_T=2 I_L, while C_T/Q_T diverges.
star=[]
for r in range(1,7):
    vals,n=cubic_star(r)
    T=Node(0,Node(),Node())
    Q,C,IL,D,leafC=tree_resource_sums(vals,n,T)
    assert C == 2*IL
    # known formulas: alpha=(1-2^-r)/2; IL=r/2; C=r
    alpha=Fraction((1<<r)-1,1<<(r+1))
    assert Q == alpha
    assert IL == Fraction(r,2)
    assert C == r
    star.append({
        "r":r,
        "Q":f"{Q.numerator}/{Q.denominator}",
        "I_L":f"{IL.numerator}/{IL.denominator}",
        "C":f"{C.numerator}/{C.denominator}",
        "C_over_Q":float(C/Q),
        "two_account_KL_exact":2
    })

# Closed-form obstruction/calibration values quoted in report.
one_point_full_order = []
for n in range(2,13):
    # root-folded one-point defect has all j_i=2^(1-n);
    # fixed full order lifetime / J = (n-1)/2.
    one_point_full_order.append([n, Fraction(n-1,2).numerator, Fraction(n-1,2).denominator])

addressing_natural = []
for s in range(1,13):
    # m=2^s data variables. Natural tree queries s address bits.
    # J=s/2+1. Descendant pivotal lifetime:
    # address pivots: (1/2) sum_{r=1}^s (r-1)=s(s-1)/4
    # data pivots: total root influence 1, each survives s address queries => s.
    L=Fraction(s*(s-1),4)+s
    J=Fraction(s,2)+1
    addressing_natural.append([s, float(L/J), f"{L.numerator}/{L.denominator}", f"{J.numerator}/{J.denominator}"])

out={
    "status":"PASS" if identity_failures==0 else "FAIL",
    "seed":SEED,
    "exact_boolean_adaptive_tree_cases_n_le_3":tree_cases,
    "random_boolean_adaptive_tree_cases_n_4_5":random_function_tree_cases,
    "identity_failures":identity_failures,
    "checked_exact_identities":[
        "Q_T = sum_i E[piv_i * 1{i queried}]",
        "I_L = sum_i E[piv_i * 1{i survives}]",
        "C_T = sum_{i<k} E[square_piv_{ik} * 1{i or k queried}]",
        "descendant_influence_sum = sum_i E[piv_i * lifetime_i]",
        "C_2(root) = C_T + average_leaf_C_2"
    ],
    "cubic_star_central_query":star,
    "one_point_full_order_lifetime_over_J":one_point_full_order,
    "addressing_natural_address_tree_lifetime_over_J":addressing_natural,
    "note":"Exact Fraction checks validate identities on finite cases only; all-dimensional claims rely on proofs in the report. No independent audit or Lean verification."
}
print(json.dumps(out,indent=2))
