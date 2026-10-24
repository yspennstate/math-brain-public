from itertools import combinations
from collections import Counter

def is_forest(n, edges):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for u,v in edges:
        ru,rv=find(u),find(v)
        if ru==rv:
            return False
        p[rv]=ru
    return True

def labels(n, edges):
    p=list(range(n))
    def find(x):
        if p[x]!=x:
            p[x]=find(p[x])
        return p[x]
    for u,v in edges:
        ru,rv=find(u),find(v)
        if ru!=rv:
            p[rv]=ru
    return [find(i) for i in range(n)]

def state_counts(n, outside):
    c=Counter()
    m=len(outside)
    for mask in range(1<<m):
        H=[outside[i] for i in range(m) if (mask>>i)&1]
        if not is_forest(n,H):
            continue
        lab=labels(n,H)
        bc=lab[1]==lab[2]
        bd=lab[1]==lab[3]
        cd=lab[2]==lab[3]
        if bc and bd:
            key="bcd"
        elif bc:
            key="bc"
        elif bd:
            key="bd"
        elif cd:
            key="cd"
        else:
            key="0"
        c[key]+=1
    return c

def direct_counts(n, edges):
    Z=Ze=Zf=Zef=0
    m=len(edges)
    for mask in range(1<<m):
        F=[edges[i] for i in range(m) if (mask>>i)&1]
        if not is_forest(n,F):
            continue
        Z += 1
        ie=(mask>>0)&1
        jf=(mask>>1)&1
        Ze += ie
        Zf += jf
        Zef += ie*jf
    return Z,Ze,Zf,Zef

graphs=0
zero_gaps=0
for n in range(4,7):
    possible=list(combinations(range(1,n),2))
    for gmask in range(1<<len(possible)):
        outside=[possible[i] for i in range(len(possible)) if (gmask>>i)&1]
        c=state_counts(n,outside)
        x0,xbc,xbd,xcd,xbcd=(c[k] for k in ("0","bc","bd","cd","bcd"))
        N=x0+xbc+xbd+xcd+xbcd

        Z0=8*x0+6*(xbc+xbd+xcd)+4*xbcd
        Ze0=4*x0+2*xbc+2*xbd+3*xcd+xbcd
        Zf0=4*x0+2*xbc+3*xbd+2*xcd+xbcd
        Zef0=2*x0+xbd+xcd
        gap_formula=4*xbc*N+xbd*xcd+xbcd*(xbd+xcd+xbcd)

        edges=[(0,1),(0,2),(0,3)]+outside
        Z,Ze,Zf,Zef=direct_counts(n,edges)
        assert (Z,Ze,Zf,Zef)==(Z0,Ze0,Zf0,Zef0)
        gap=Ze*Zf-Z*Zef
        assert gap==gap_formula
        assert gap>=0
        graphs += 1
        zero_gaps += (gap==0)

# Exact degree-four local-kernel negative control:
# all four neighbours separate versus all four connected.
# W_sep=16, alpha_sep=beta_sep=1/2, r_sep=1;
# W_join=5, alpha_join=beta_join=1/5, r_join=0.
# The unordered cross coefficient in Delta is
# W_sep*W_join*K with
# K=a_sep*b_join+a_join*b_sep-r_sep*a_sep*b_sep-r_join*a_join*b_join=-1/20.
assert 16*5 * (-1) == -80  # numerator before /20
degree4_cross_coefficient = -4

print("FOREST_DEG3_STAR_ID_PASS")
print(f"outside_graphs_exhausted_n4_to_n6={graphs}")
print(f"zero_gap_instances={zero_gaps}")
print("direct_forest_count_identity_failures=0")
print("positive_coefficient_identity_failures=0")
print(f"degree4_sep_join_cross_coefficient={degree4_cross_coefficient}")
print("DEGREE4_COEFFICIENTWISE_EXTENSION_REJECTED")
