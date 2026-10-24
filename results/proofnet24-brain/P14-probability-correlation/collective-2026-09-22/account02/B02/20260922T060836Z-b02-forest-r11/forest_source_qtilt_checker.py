#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from collections import defaultdict

def is_forest(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a,b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
    return True

def connected(n, edges, s, t):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a,b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    return find(s) == find(t)

def components(vertices, edges):
    parent = {v:v for v in vertices}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a,b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    for a,b in edges:
        if a in parent and b in parent:
            union(a,b)
    groups = defaultdict(list)
    for v in vertices:
        groups[find(v)].append(v)
    return list(groups.values())

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def neg_hess_from_exponents(exps):
    Z = len(exps)
    d = len(exps[0])
    means = [sum(Fraction(v[j], Z) for v in exps) for j in range(d)]
    cov = [[sum(Fraction((v[i]-means[i])*(v[j]-means[j]), Z)
                for v in exps) for j in range(d)] for i in range(d)]
    return [[(means[i] if i==j else 0)-cov[i][j]
             for j in range(d)] for i in range(d)]

def k3_homogenization_check():
    inds = [(),(0,),(1,),(2,),(0,1),(0,2),(1,2)]
    rank_exp = [[2-len(S), int(0 in S), int(1 in S)] for S in inds]
    ground_exp = [[3-len(S), int(0 in S), int(1 in S)] for S in inds]
    Mr = neg_hess_from_exponents(rank_exp)
    Mg = neg_hess_from_exponents(ground_exp)
    dr, dg = det3(Mr), det3(Mg)
    assert dr == Fraction(-1,2401)
    assert dg == Fraction(76,2401)
    return Mr, Mg, dr, dg

def phi_theta(n, E, u, v, T):
    W = [x for x in range(n) if x not in (u,v)]
    cs = components(W,T)
    data=[]
    phi=1
    for C in cs:
        a=sum(tuple(sorted((u,w))) in E for w in C)
        b=sum(tuple(sorted((v,w))) in E for w in C)
        data.append((C,a,b))
        phi *= 1+a+b
    theta=0
    for i,(_,a,b) in enumerate(data):
        if a*b:
            term=a*b
            for j,(_,aa,bb) in enumerate(data):
                if i!=j:
                    term *= 1+aa+bb
            theta += term
    q=Fraction(theta,phi)
    return phi,theta,q,data

def exhaustive_extension_identity(max_n=5):
    graphs=tri_edges=base_forests=0
    for n in range(3,max_n+1):
        allE=list(combinations(range(n),2))
        for gmask in range(1<<len(allE)):
            E={allE[i] for i in range(len(allE)) if gmask>>i&1}
            graphs += 1
            for u,v in sorted(E):
                if not any(tuple(sorted((u,w))) in E and tuple(sorted((v,w))) in E
                           for w in range(n) if w not in (u,v)):
                    continue
                tri_edges += 1
                W=set(range(n))-{u,v}
                base=[e for e in E if e[0] in W and e[1] in W]
                inc=[e for e in E if e != (u,v) and (u in e or v in e)]
                for tmask in range(1<<len(base)):
                    T=[base[i] for i in range(len(base)) if tmask>>i&1]
                    if not is_forest(n,T):
                        continue
                    base_forests += 1
                    phi,theta,q,data = phi_theta(n,E,u,v,T)
                    total=disc=conn=0
                    for imask in range(1<<len(inc)):
                        A=[inc[i] for i in range(len(inc)) if imask>>i&1]
                        U=T+A
                        if not is_forest(n,U):
                            continue
                        total += 1
                        if connected(n,U,u,v):
                            conn += 1
                        else:
                            disc += 1
                    assert disc == phi, (n,E,(u,v),T,disc,phi)
                    assert conn == theta, (n,E,(u,v),T,conn,theta)
                    assert total == phi+theta
                    assert q == Fraction(theta,phi)
    return graphs,tri_edges,base_forests

def qtilt_counterexample():
    n=5
    E={(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)}
    u,v=1,2
    base=[(0,3),(0,4)]
    states=[]
    for mask in range(4):
        T=[base[i] for i in range(2) if mask>>i&1]
        phi,theta,q,data=phi_theta(n,E,u,v,T)
        states.append((mask,phi,theta,q))
    Znu=sum(phi for _,phi,_,_ in states)
    Zmu=sum(phi+theta for _,phi,theta,_ in states)
    assert [x[1] for x in states] == [12,8,8,5]
    assert [x[2] for x in states] == [4,4,4,3]
    def Enu(func):
        return sum(Fraction(phi,Znu)*func(mask,q) for mask,phi,theta,q in states)
    def Emu(func):
        return sum(Fraction(phi+theta,Zmu)*func(mask,q) for mask,phi,theta,q in states)
    X=lambda mask,q: (mask>>0)&1
    Y=lambda mask,q: (mask>>1)&1
    Q=lambda mask,q: q
    EX,EY,EQ=Enu(X),Enu(Y),Enu(Q)
    EXY=Enu(lambda m,q:X(m,q)*Y(m,q))
    covnu=EXY-EX*EY
    EmX,EmY=Emu(X),Emu(Y)
    covmu=Emu(lambda m,q:X(m,q)*Y(m,q))-EmX*EmY
    ux=Enu(lambda m,q:X(m,q)*Q(m,q))-EX*EQ
    uy=Enu(lambda m,q:Y(m,q)*Q(m,q))-EY*EQ
    kappa=Enu(lambda m,q:(X(m,q)-EX)*(Y(m,q)-EY)*(Q(m,q)-EQ))
    s=1+EQ
    correction=kappa/s-ux*uy/(s*s)
    assert covmu == covnu+correction
    assert covnu == Fraction(-4,1089)
    assert covmu == Fraction(-1,144)
    assert EQ == Fraction(5,11)
    assert ux == uy == Fraction(4,121)
    assert kappa == Fraction(-16,3993)
    curvature=s*kappa-ux*uy
    assert curvature == Fraction(-304,43923)
    assert curvature < 0 and covnu < 0 and covmu < 0
    return states,Znu,Zmu,covnu,covmu,EQ,ux,uy,kappa,curvature,correction

if __name__ == "__main__":
    Mr,Mg,dr,dg=k3_homogenization_check()
    print("K3_RANK_NEG_HESS=",Mr)
    print("K3_RANK_PRINCIPAL_DET=",dr)
    print("K3_GROUND_NEG_HESS=",Mg)
    print("K3_GROUND_PRINCIPAL_DET=",dg)
    g,t,b=exhaustive_extension_identity(5)
    print(f"EXTENSION_IDENTITY_PASS graphs={g} triangle_edge_instances={t} base_forest_instances={b}")
    result=qtilt_counterexample()
    states,Znu,Zmu,covnu,covmu,EQ,ux,uy,kappa,curvature,correction=result
    print("QTILT_PHI=", [x[1] for x in states])
    print("QTILT_THETA=", [x[2] for x in states])
    print("QTILT_ZNU=",Znu,"ZMU=",Zmu)
    print("QTILT_COV_NU=",covnu,"COV_MU=",covmu)
    print("QTILT_EQ=",EQ,"COV_XQ=",ux,"COV_YQ=",uy,"KAPPA=",kappa)
    print("QTILT_CORRECTION=",correction)
    print("QTILT_CURVATURE_S_KAPPA_MINUS_UV=",curvature)
    print("STATUS=ALL_EXACT_CHECKS_PASS_AND_CURVATURE_CANDIDATE_REFUTED")
