#!/usr/bin/env python3
"""Independent exact/dyadic audit of adaptive Boolean root-KL nonreuse."""
import itertools
import math
import random

C0 = 2 / math.log(2)
TOL = 3e-12
TREE_CASES = NODE_CHECKS = 0
MAX_ENERGY_ERR = MAX_KL_SURPLUS = 0.0

def h2(t):
    if t <= 0 or t >= 1:
        return 0.0
    return -t*math.log2(t)-(1-t)*math.log2(1-t)

def root_kl(a,d):
    m=a*a+d*d
    if not m:
        return 0.0
    return m*(1-h2((1+2*a*d/m)/2))

def all_trees(remaining):
    if not remaining:
        return [None]
    out=[]
    for i in remaining:
        rem=tuple(j for j in remaining if j != i)
        sub=all_trees(rem)
        for left in sub:
            for right in sub:
                out.append((i,left,right))
    return out

def order_tree(order):
    if not order:
        return None
    child=order_tree(order[1:])
    return (order[0],child,child)

def random_tree(remaining,rng):
    if not remaining:
        return None
    i=rng.choice(remaining)
    rem=tuple(j for j in remaining if j != i)
    return (i,random_tree(rem,rng),random_tree(rem,rng))

def conditional_moments(table,n,prefix,i):
    vals=[]
    for x,y in enumerate(table):
        if all(((x>>j)&1)==e for j,e in prefix.items()):
            xi=1 if (x>>i)&1 else -1
            vals.append((y,xi))
    a=sum(y for y,_ in vals)/len(vals)
    d=sum(y*xi for y,xi in vals)/len(vals)
    return a,d

def audit(table,n,tree):
    global TREE_CASES,NODE_CHECKS,MAX_ENERGY_ERR,MAX_KL_SURPLUS
    TREE_CASES += 1
    energy=payment=0.0
    def rec(node,prefix,prob):
        nonlocal energy,payment
        global NODE_CHECKS,MAX_KL_SURPLUS
        if node is None:
            return
        i,left,right=node
        assert i not in prefix
        a,d=conditional_moments(table,n,prefix,i)
        k=root_kl(a,d)
        surplus=k-C0*d*d
        MAX_KL_SURPLUS=max(MAX_KL_SURPLUS,surplus)
        assert surplus <= TOL
        energy += prob*d*d
        payment += prob*k
        NODE_CHECKS += 1
        p0=dict(prefix); p0[i]=0
        p1=dict(prefix); p1[i]=1
        rec(left,p0,prob/2); rec(right,p1,prob/2)
    rec(tree,{},1.0)
    mean=sum(table)/len(table)
    var=1-mean*mean
    err=abs(energy-var)
    MAX_ENERGY_ERR=max(MAX_ENERGY_ERR,err)
    assert err <= TOL
    assert payment <= C0*energy+TOL <= C0*var+2*TOL

def table_from_mask(mask,N):
    return [1 if (mask>>x)&1 else -1 for x in range(N)]

def main():
    # Every Boolean function and every adaptive full read-once tree through n=3.
    for n in range(1,4):
        trees=all_trees(tuple(range(n)))
        for mask in range(1<<(1<<n)):
            table=table_from_mask(mask,1<<n)
            for tree in trees:
                audit(table,n,tree)

    # Every four-bit Boolean function under a complete physical order.
    tree=order_tree(tuple(range(4)))
    for mask in range(1<<16):
        audit(table_from_mask(mask,16),4,tree)

    # All 24 fixed orders on a deterministic 4096-function four-bit sample.
    for mask in range(0,1<<16,16):
        table=table_from_mask(mask,16)
        for order in itertools.permutations(range(4)):
            audit(table,4,order_tree(order))

    # Seeded adaptive stress in dimensions five and six.
    rng=random.Random(20261014)
    for n in (5,6):
        for _ in range(500):
            table=[rng.choice((-1,1)) for _ in range(1<<n)]
            audit(table,n,random_tree(tuple(range(n)),rng))

    print("claim=B07-A031-ADAPTIVE-ROOT-NONREUSE-v1")
    print("verdict=PROVED_PENDING_INDEPENDENT_REVIEW")
    print("tree_function_cases",TREE_CASES)
    print("node_checks",NODE_CHECKS)
    print("max_complete_tree_energy_error",f"{MAX_ENERGY_ERR:.3e}")
    print("max_root_kl_surplus",f"{MAX_KL_SURPLUS:.3e}")
    print("sharp_constant_2_over_ln2",f"{C0:.15g}")
    print("universal_GU=OPEN")

if __name__ == "__main__":
    main()

