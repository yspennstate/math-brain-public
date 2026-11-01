from fractions import Fraction
from itertools import combinations


def is_forest(n, edge_list, mask):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb:
            return False
        parent[rb]=ra
        return True
    for i,(u,v) in enumerate(edge_list):
        if (mask>>i)&1:
            if not union(u,v):
                return False
    return True


def forest_counts(n, edges):
    m=len(edges)
    Z=0
    Zi=[0]*m
    Zij=[[0]*m for _ in range(m)]
    forests=[]
    for mask in range(1<<m):
        if is_forest(n, edges, mask):
            forests.append(mask)
            Z += 1
            present=[i for i in range(m) if (mask>>i)&1]
            for i in present:
                Zi[i]+=1
            for a in range(len(present)):
                i=present[a]
                for b in range(a+1,len(present)):
                    j=present[b]
                    Zij[i][j]+=1
                    Zij[j][i]+=1
    return Z,Zi,Zij,forests


def rho_sq(Z,Zi,Zij,i,j):
    num=Z*Zij[i][j]-Zi[i]*Zi[j]
    den=Zi[i]*(Z-Zi[i])*Zi[j]*(Z-Zi[j])
    return Fraction(num*num,den)


def conditional_cov_numerator(forests,i,j,g,gval):
    # numerator N*count(ij)-count(i)count(j); sign matches conditional covariance.
    sub=[mask for mask in forests if ((mask>>g)&1)==gval]
    N=len(sub)
    ci=sum((mask>>i)&1 for mask in sub)
    cj=sum((mask>>j)&1 for mask in sub)
    cij=sum(((mask>>i)&1) and ((mask>>j)&1) for mask in sub)
    return N*cij-ci*cj


def total_cov_identity_scaled(Z,Zi,Zij,forests,i,j,g):
    # Check Cov(i,j)=E Cov(i,j|g)+Cov(i,g)Cov(j,g)/Var(g) exactly.
    # Work directly with Fractions.
    def p1(a): return Fraction(Zi[a],Z)
    def p2(a,b): return Fraction(Zij[a][b],Z)
    covij=p2(i,j)-p1(i)*p1(j)
    covig=p2(i,g)-p1(i)*p1(g)
    covjg=p2(j,g)-p1(j)*p1(g)
    pg=p1(g)
    vg=pg*(1-pg)
    cond=Fraction(0,1)
    for gv in (0,1):
        sub=[mask for mask in forests if ((mask>>g)&1)==gv]
        N=len(sub)
        w=Fraction(N,Z)
        pi=Fraction(sum((mask>>i)&1 for mask in sub),N)
        pj=Fraction(sum((mask>>j)&1 for mask in sub),N)
        pij=Fraction(sum((((mask>>i)&1) and ((mask>>j)&1)) for mask in sub),N)
        cond += w*(pij-pi*pj)
    return covij == cond + covig*covjg/vg


def main():
    graph_count=0
    edge_row_count=0
    triple_identity_count=0
    p_half_fail=0
    row_budget_fail=0
    identity_fail=0
    max_ratio=Fraction(0,1)
    max_ratio_witness=None
    min_slack=None
    min_slack_witness=None
    for n in range(2,6):
        complete=list(combinations(range(n),2))
        for gmask in range(1<<len(complete)):
            edges=[e for k,e in enumerate(complete) if (gmask>>k)&1]
            graph_count+=1
            if not edges:
                continue
            Z,Zi,Zij,forests=forest_counts(n,edges)
            m=len(edges)
            for i in range(m):
                edge_row_count += 1
                p=Fraction(Zi[i],Z)
                if p > Fraction(1,2):
                    p_half_fail += 1
                lhs=Fraction(0,1)
                for j in range(m):
                    if i==j: continue
                    pj=Fraction(Zi[j],Z)
                    lhs += (1-pj)*rho_sq(Z,Zi,Zij,i,j)
                slack=p-lhs
                if slack < 0:
                    row_budget_fail += 1
                if p>0:
                    ratio=lhs/p
                    if ratio>max_ratio:
                        max_ratio=ratio
                        max_ratio_witness=(n,tuple(edges),i,Z,Zi[:],lhs,p)
                if min_slack is None or slack<min_slack:
                    min_slack=slack
                    min_slack_witness=(n,tuple(edges),i,slack,p,lhs)
            if m>=3:
                for i,j,g in combinations(range(m),3):
                    for a,b,c in ((i,j,g),(i,g,j),(j,g,i)):
                        triple_identity_count += 1
                        if not total_cov_identity_scaled(Z,Zi,Zij,forests,a,b,c):
                            identity_fail += 1
    print(f"GRAPHS_CHECKED={graph_count}")
    print(f"EDGE_ROWS_CHECKED={edge_row_count}")
    print(f"TOTAL_COVARIANCE_TRIPLES_CHECKED={triple_identity_count}")
    print(f"P_HALF_FAILURES={p_half_fail}")
    print(f"ROW_BUDGET_FAILURES={row_budget_fail}")
    print(f"TOTAL_COVARIANCE_IDENTITY_FAILURES={identity_fail}")
    print(f"MAX_EXACT_ROW_RATIO={max_ratio.numerator}/{max_ratio.denominator}")
    if max_ratio_witness:
        n,edges,i,Z,zis,lhs,p=max_ratio_witness
        print(f"MAX_RATIO_WITNESS_n={n}_m={len(edges)}_edge_index={i}_Z={Z}_lhs={lhs.numerator}/{lhs.denominator}_p={p.numerator}/{p.denominator}")
    print(f"MIN_EXACT_ROW_SLACK={min_slack.numerator}/{min_slack.denominator}")
    if min_slack_witness:
        n,edges,i,slack,p,lhs=min_slack_witness
        print(f"MIN_SLACK_WITNESS_n={n}_m={len(edges)}_edge_index={i}_p={p.numerator}/{p.denominator}_lhs={lhs.numerator}/{lhs.denominator}")
    assert p_half_fail==0 and row_budget_fail==0 and identity_fail==0
    print("ALL_EXACT_CHECKS_PASS")

if __name__ == '__main__':
    main()
