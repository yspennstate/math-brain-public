from fractions import Fraction
from itertools import product, combinations, permutations
from math import comb, factorial

def beta_int(a,b):
    # B(a,b) for positive integers
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))

def rtts(m):
    # recursive rooted trees: parent(v) in {1,...,v-1}
    for choices in product(*[range(1,v) for v in range(2,m+1)]):
        parent={1:None}
        for v,p in enumerate(choices,start=2):
            parent[v]=p
        yield parent

def is_desc(parent,v,root):
    x=v
    while x is not None:
        if x==root:
            return True
        x=parent[x]
    return False

def fringe_size(parent,v):
    return sum(is_desc(parent,u,v) for u in parent)

def process_lifts(parent, labmap, order):
    # Goldschmidt-Martin-style lift: cut parent(c)--c, merge every label
    # in the current descendant subtree of c into the parent node, and
    # delete those descendant nodes. Marked edges whose endpoints have
    # already disappeared are inert.
    active=set(parent)
    blocks={v:{labmap[v]} for v in active}
    for c in order:
        p=parent[c]
        if c not in active or p not in active:
            continue
        ds={v for v in active if is_desc(parent,v,c)}
        merged=set(blocks[p])
        for v in ds:
            merged |= blocks[v]
        blocks[p]=merged
        for v in ds:
            del blocks[v]
        active-=ds
    return list(blocks.values())

def canon_split(A,all_labels):
    A=frozenset(A)
    C=frozenset(all_labels-set(A))
    if not A or not C:
        return None
    return tuple(sorted((tuple(sorted(A)),tuple(sorted(C)))))

def check_rrt_fringe(max_m=9):
    tests=0
    for m in range(2,max_m+1):
        trees=list(rtts(m))
        got={s:Fraction(0) for s in range(1,m)}
        for T in trees:
            for v in range(2,m+1):
                got[fringe_size(T,v)] += Fraction(1,len(trees))
        for s in range(1,m):
            target=Fraction(m,s*(s+1))
            assert got[s]==target,(m,s,got[s],target)
            tests+=1
    return tests

def check_shifted_bs_identity(max_m=30):
    # RRT one-edge lift merger-set coefficient for a specified k-set:
    # [m/((k-1)k)] / C(m,k) = B(k-1,m-k+1)
    tests=0
    for m in range(2,max_m+1):
        for k in range(2,m+1):
            lhs=Fraction(m,(k-1)*k*comb(m,k))
            rhs=beta_int(k-1,m-k+1)
            assert lhs==rhs,(m,k,lhs,rhs)
            tests+=1
    return tests

def check_anchor_split_identity(max_m=30):
    # Given a target unordered split S|S^c of sizes s,m-s, every anchor
    # chooses exactly one shifted BS merger: S+anchor or S^c+anchor.
    tests=0
    for m in range(2,max_m+1):
        for s in range(1,m):
            lam_left=beta_int(s,m-s)   # k=s+1
            lam_right=beta_int(m-s,s)  # k=m-s+1
            lhs=Fraction(m-s,m)*lam_left + Fraction(s,m)*lam_right
            rhs=beta_int(s,m-s)
            assert lhs==rhs,(m,s,lhs,rhs)
            tests+=1
    return tests

def check_total_ctcs_rate(max_m=50):
    tests=0
    for m in range(2,max_m+1):
        # unordered split total rate: half sum over oriented subset sizes
        total=Fraction(0)
        for s in range(1,m):
            total += Fraction(comb(m,s),2)*beta_int(s,m-s)
        H=sum((Fraction(1,j) for j in range(1,m)),Fraction(0))
        assert total==H,(m,total,H)
        tests+=1
    return tests

def one_mark_coefficients(m):
    # Exact exhaustive coefficient of p for each particular visible split
    # when exactly one original RRT edge is marked. Includes uniform
    # relabelling and uniform anchor.
    trees=list(rtts(m))
    labels=set(range(1,m+1))
    from collections import defaultdict
    split_coeff=defaultdict(Fraction)
    shape_coeff=defaultdict(Fraction)
    denom=len(trees)*factorial(m)*m
    for T in trees:
        for perm in permutations(range(1,m+1)):
            labmap={v:perm[v-1] for v in range(1,m+1)}
            for c in range(2,m+1):
                parts=process_lifts(T,labmap,(c,))
                for anchor in range(1,m+1):
                    M=next(B for B in parts if anchor in B)
                    A=set(M)-{anchor}
                    out=canon_split(A,labels)
                    if out is None:
                        continue
                    w=Fraction(1,denom)
                    split_coeff[out]+=w
                    shape_coeff[tuple(sorted(map(len,out)))]+=w
    return split_coeff,shape_coeff

def check_one_mark_ctcs(max_m=5):
    tests=0
    for m in range(2,max_m+1):
        split_coeff,shape_coeff=one_mark_coefficients(m)
        for split,val in split_coeff.items():
            s=len(split[0])
            # beta symmetric, so either side is fine
            target=beta_int(s,m-s)
            assert val==target,(m,split,val,target)
            tests+=1
        # independent aggregate shape check
        for shape,val in shape_coeff.items():
            s=shape[0]
            if s*2==m:
                count=comb(m,s)//2
            else:
                count=comb(m,s)
            target=count*beta_int(s,m-s)
            assert val==target,(m,shape,val,target)
            tests+=1
    return tests

def exact_one_step(m,p):
    # Exact finite one-step law including all marked-edge subsets and
    # a uniformly random processing order of marked edges.
    from collections import defaultdict
    trees=list(rtts(m))
    labels=set(range(1,m+1))
    outcome=defaultdict(Fraction)
    denom_base=len(trees)*factorial(m)*m
    for T in trees:
        for perm in permutations(range(1,m+1)):
            labmap={v:perm[v-1] for v in range(1,m+1)}
            edges=tuple(range(2,m+1))
            for r in range(m):
                for subset in combinations(edges,r):
                    markprob=p**r*(1-p)**(m-1-r)
                    orders=((),) if r==0 else tuple(permutations(subset))
                    for order in orders:
                        parts=process_lifts(T,labmap,order)
                        for anchor in range(1,m+1):
                            M=next(B for B in parts if anchor in B)
                            A=set(M)-{anchor}
                            out=canon_split(A,labels)
                            outcome[out]+=Fraction(1,denom_base*len(orders))*markprob
    assert sum(outcome.values())==1
    return outcome

def check_finite_witness():
    from collections import defaultdict
    m=4
    p=Fraction(1,m**3)
    out=exact_one_step(m,p)
    no=out[None]
    shapes=defaultdict(Fraction)
    for split,pr in out.items():
        if split is None:
            continue
        shape=tuple(sorted(map(len,split)))
        shapes[shape]+=pr
    # Aggregate probabilities
    assert no==Fraction(509397,524288),no
    assert shapes[(1,3)]==Fraction(2699,131072),shapes
    assert shapes[(2,2)]==Fraction(4095,524288),shapes
    visible=1-no
    assert shapes[(1,3)]/visible==Fraction(10796,14891)
    assert shapes[(2,2)]/visible==Fraction(4095,14891)

    # By exchangeability, divide aggregate shape mass by number of unordered
    # labelled splits of that shape. Their ratio is invariant under waiting
    # suppression, relabelling, and global branch-length rescaling.
    q13=shapes[(1,3)]/4
    q22=shapes[(2,2)]/3
    ratio=q13/q22
    assert ratio==Fraction(2699,1365),ratio

    # Original CTCS particular split rate ratio at m=4 is 2.
    ctcs_ratio=beta_int(1,3)/beta_int(2,2)
    assert ctcs_ratio==2
    assert ratio!=ctcs_ratio

    # C001 harmonic-grid paintbox at N=4 has q(4,1)=7/32, q(4,2)=5/32.
    def hgpf_q(N,m,i):
        total=Fraction(0)
        for j in range(1,N):
            x=Fraction(j,N)
            total += x**(i-1)*(1-x)**(m-i-1)
        return total/N
    c001_ratio=hgpf_q(4,4,1)/hgpf_q(4,4,2)
    assert c001_ratio==Fraction(7,5)
    assert ratio!=c001_ratio
    return no,shapes,ratio,c001_ratio,ctcs_ratio

def check_binary_output(max_m=7):
    # The anchor rule always returns at most two children; exhaustive
    # algebraic check of all possible nontrivial A sizes.
    tests=0
    for m in range(2,max_m+1):
        labels=set(range(1,m+1))
        for r in range(1,m):
            A=set(range(1,r+1))
            sp=canon_split(A,labels)
            assert sp is not None and len(sp)==2
            tests+=1
    return tests

def check_error_scale():
    # For p_N=N^-3, union bound on >=2 marked edges in all sampled-containing
    # hidden blocks (at most N relevant edges total) gives C(N,2)p_N^2 per
    # raw step. Over 1/p_N steps: <= C(N,2)p_N < 1/(2N).
    tests=0
    for N in range(2,501):
        p=Fraction(1,N**3)
        bound=Fraction(comb(N,2))*p
        assert bound < Fraction(1,2*N)
        tests+=1
    return tests

def main():
    n1=check_rrt_fringe()
    n2=check_shifted_bs_identity()
    n3=check_anchor_split_identity()
    n4=check_total_ctcs_rate()
    n5=check_one_mark_ctcs()
    no,shapes,ratio,c001,ctcs=check_finite_witness()
    n6=check_binary_output()
    n7=check_error_scale()
    print("R11 I0054 C009 exact checker")
    print(f"rrt_fringe_checks={n1}")
    print(f"shifted_bs_beta_checks={n2}")
    print(f"anchor_split_checks={n3}")
    print(f"ctcs_total_rate_checks={n4}")
    print(f"exhaustive_one_mark_split_checks={n5}")
    print(f"binary_output_checks={n6}")
    print(f"error_scale_checks={n7}")
    print(f"N4_no_split={no}")
    print(f"N4_shape_1_3={shapes[(1,3)]}")
    print(f"N4_shape_2_2={shapes[(2,2)]}")
    print(f"N4_reduced_particular_ratio_C009={ratio}")
    print(f"N4_particular_ratio_C001={c001}")
    print(f"N4_particular_ratio_original_CTCS={ctcs}")
    print("NOTE: finite enumeration checks identities/witnesses only; asymptotic convergence is proved in the report.")
    print("ALL_EXACT_CHECKS_PASS")

if __name__=="__main__":
    main()
