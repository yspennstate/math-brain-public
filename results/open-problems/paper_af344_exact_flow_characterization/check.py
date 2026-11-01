#!/usr/bin/env python3
"""
Exact-arithmetic checks for the Aldous--Fill Open Problem 3.44 package.

This is the package copy of artifacts/R01/i0024_exact_flow_checker.py.
It checks finite examples and normalization; the universal theorem is proved in
main.tex and is not inferred from these examples.
"""
import sympy as sp

Q = sp.Rational

def laplacian_data(P, pi):
    n = P.rows
    Pi = sp.diag(*pi)
    edges, conductances = [], []
    for i in range(n):
        for j in range(i+1, n):
            c = sp.simplify(pi[i] * P[i,j])
            if c != 0:
                assert c > 0
                assert sp.simplify(c - pi[j]*P[j,i]) == 0
                edges.append((i,j))
                conductances.append(c)
    B = sp.zeros(n, len(edges))
    for k,(i,j) in enumerate(edges):
        B[i,k] = 1
        B[j,k] = -1
    C = sp.diag(*conductances)
    L = sp.simplify(B*C*B.T)
    assert L == sp.simplify(Pi*(sp.eye(n)-P))
    J = sp.ones(n,n)
    Lplus = sp.simplify((L + J/Q(n)).inv() - J/Q(n))
    assert sp.simplify(L*Lplus - (sp.eye(n)-J/Q(n))) == sp.zeros(n,n)
    return Pi, edges, B, C, L, Lplus

def zero_pi_basis(pi):
    n = len(pi)
    H = sp.zeros(n,n-1)
    for i in range(n-1):
        H[i,i] = 1
        H[n-1,i] = -pi[i]/pi[n-1]
    assert (sp.Matrix([pi])*H) == sp.zeros(1,n-1)
    return H

def check_exact_flow_formula(P, pi, expected_tau, expected_cost_spectrum):
    n=P.rows
    Pi, edges, B, C, L, Lplus = laplacian_data(P,pi)
    H = zero_pi_basis(pi)

    pair_flow = {}
    for x in range(n):
        for y in range(n):
            if x==y:
                pair_flow[(x,y)] = sp.zeros(len(edges),1)
                continue
            d = sp.zeros(n,1)
            d[x]=1; d[y]=-1
            f = sp.simplify(C*B.T*Lplus*d)
            assert sp.simplify(B*f-d)==sp.zeros(n,1)
            pair_flow[(x,y)] = f
            assert sp.simplify(pair_flow[(y,x)] + f)==sp.zeros(len(edges),1) if (y,x) in pair_flow else True

    T = sp.zeros(len(edges),n-1)
    for x in range(n):
        for y in range(n):
            coeff = H[x,:]-H[y,:]
            T += Q(1,2)*pi[x]*pi[y]*pair_flow[(x,y)]*coeff

    assert sp.simplify(B*T-Pi*H)==sp.zeros(n,n-1)
    Tstar = sp.simplify(C*B.T*Lplus*Pi*H)
    assert sp.simplify(T-Tstar)==sp.zeros(len(edges),n-1)

    E = sp.simplify(T.T*C.inv()*T)
    E2 = sp.simplify(H.T*Pi*Lplus*Pi*H)
    assert E==E2

    G = sp.simplify(H.T*Pi*H)
    A = sp.simplify(G.inv()*E)
    got = A.eigenvals()
    assert got == expected_cost_spectrum
    maxcost = max(got.keys(), key=lambda z: float(z))
    assert sp.simplify(maxcost-expected_tau)==0

    ev=[]
    for z,mult in P.eigenvals().items():
        ev += [z]*mult
    ev=sorted(ev,key=lambda z:float(z),reverse=True)
    tau=sp.simplify(1/(1-ev[1]))
    assert sp.simplify(tau-expected_tau)==0
    return maxcost

P4 = sp.Matrix([
    [0,1,0,0],
    [Q(1,2),0,Q(1,2),0],
    [0,Q(1,2),0,Q(1,2)],
    [0,0,1,0],
])
pi4=[Q(1,6),Q(1,3),Q(1,3),Q(1,6)]
assert P4.charpoly().as_expr().factor() == (sp.Symbol('lambda') - 1)*(sp.Symbol('lambda') + 1)*(2*sp.Symbol('lambda') - 1)*(2*sp.Symbol('lambda') + 1)/4
tau4=Q(2)

dist = [
    [0,1,2,3],
    [1,0,1,2],
    [2,1,0,1],
    [3,2,1,0],
]
load=Q(0)
for x in (0,1):
    for y in (2,3):
        load += pi4[x]*pi4[y]*dist[x][y]
path_congestion = 6*load
assert load == Q(5,12)
assert path_congestion == Q(5,2)
assert path_congestion/tau4 == Q(5,4)
print("COUNTEREXAMPLE A PASS: P4 random-path congestion inf = 5/2, tau2 = 2, ratio = 5/4")

K3 = sp.Matrix([
    [0,Q(1,2),Q(1,2)],
    [Q(1,2),0,Q(1,2)],
    [Q(1,2),Q(1,2),0],
])
pi3=[Q(1,3)]*3
Pi3,_,_,_,L3,Lp3=laplacian_data(K3,pi3)
avg=Q(0)
for x in range(3):
    for y in range(3):
        d=sp.zeros(3,1); d[x]=1; d[y]-=1
        resistance=sp.simplify((d.T*Lp3*d)[0])
        avg += Q(1,2)*pi3[x]*pi3[y]*resistance
assert avg == Q(4,3)
assert K3.eigenvals()=={1:1,Q(-1,2):2}
tau3=Q(2,3)
assert avg/tau3==2
print("COUNTEREXAMPLE B PASS: K3 average pair Thomson energy = 4/3, tau2 = 2/3, ratio = 2")

c4 = check_exact_flow_formula(
    P4, pi4, Q(2),
    {Q(2):1,Q(2,3):1,Q(1,2):1}
)
assert c4==2
print("EXACT FLOW FORMULA PASS: P4 electrical all-pairs routing cost = tau2 = 2")

Pnu = sp.Matrix([
    [Q(1,4),Q(1,4),Q(1,2)],
    [Q(1,6),Q(1,3),Q(1,2)],
    [Q(1,5),Q(3,10),Q(1,2)],
])
pinu=[Q(1,5),Q(3,10),Q(1,2)]
assert sp.Matrix([pinu])*Pnu == sp.Matrix([pinu])
cnu=check_exact_flow_formula(
    Pnu,pinu,Q(12,11),
    {Q(12,11):1,Q(1):1}
)
assert cnu==Q(12,11)
print("EXACT FLOW FORMULA PASS: non-uniform 3-state chain cost = tau2 = 12/11")

ck3=check_exact_flow_formula(
    K3,pi3,Q(2,3),
    {Q(2,3):2}
)
assert ck3==Q(2,3)
print("EXACT FLOW FORMULA PASS: K3 electrical all-pairs routing cost = tau2 = 2/3")

print("ALL EXACT CHECKS PASS")
