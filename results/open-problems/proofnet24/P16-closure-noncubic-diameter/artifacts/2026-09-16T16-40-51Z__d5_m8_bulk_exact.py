#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations
from math import gcd

N=8
ALL={tuple(e) for e in combinations(range(N),2)}
CYCLE_TYPES={
    '8': ((0,1,2,3,4,5,6,7),),
    '5+3': ((0,1,2,3,4),(5,6,7)),
    '4+4': ((0,1,2,3),(4,5,6,7)),
}

def cycle_edges(cycles):
    out=set()
    for cyc in cycles:
        for i,u in enumerate(cyc):
            v=cyc[(i+1)%len(cyc)]
            out.add(tuple(sorted((u,v))))
    return out

def present_edges(cycles):
    return sorted(ALL-cycle_edges(cycles))

def invert_fraction_matrix(A):
    n=len(A)
    M=[[Fraction(A[i][j]) for j in range(n)]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv=next(r for r in range(col,n) if M[r][col])
        M[col],M[piv]=M[piv],M[col]
        q=M[col][col]
        M[col]=[x/q for x in M[col]]
        for r in range(n):
            if r==col: continue
            q=M[r][col]
            if q:
                M[r]=[M[r][j]-q*M[col][j] for j in range(2*n)]
    return [row[n:] for row in M]

def mat_quad(inv,b):
    return sum(Fraction(b[i])*inv[i][j]*Fraction(b[j]) for i in range(len(b)) for j in range(len(b)))

def lift_voltage_gcd(E,colors):
    # canonical orientation u<v. Voltage is cell(v)-cell(u).
    adj=[[] for _ in range(N)]
    for u,v in E:
        cu,cv=colors[u],colors[v]
        w=0
        if {cu,cv}=={0,2}:
            # Layer-2 in cell j is joined to layer-0 in cell j+1.
            # Hence from a layer-2 endpoint to layer-0 endpoint the voltage is +1.
            w=1 if (cu==2 and cv==0) else -1
        adj[u].append((v,w)); adj[v].append((u,-w))
    pot=[None]*N
    pot[0]=0
    stack=[0]
    g=0
    while stack:
        u=stack.pop()
        for v,w in adj[u]:
            if pot[v] is None:
                pot[v]=pot[u]+w
                stack.append(v)
            else:
                g=gcd(g,abs(pot[u]+w-pot[v]))
    assert all(x is not None for x in pot) # K8 minus a 2-factor is connected.
    return g

def laplacian_inverse(E):
    L=[[0]*N for _ in range(N)]
    for u,v in E:
        L[u][u]+=1;L[v][v]+=1
        L[u][v]-=1;L[v][u]-=1
    # Ground vertex 7. Since every b below sums to zero, b^T L^+ b is obtained from this inverse.
    return invert_fraction_matrix([row[:N-1] for row in L[:N-1]])

def coefficient(E,inv,colors):
    b=[0]*N
    c=0
    for u,v in E:
        cu,cv=colors[u],colors[v]
        if {cu,cv}=={0,2}:
            c+=1
            # Term (h_2-h_0-1)^2. b is the signed incidence sum of unit-voltage edges.
            if cu==2:
                b[u]+=1;b[v]-=1
            else:
                b[v]+=1;b[u]-=1
    assert sum(b)==0
    G=Fraction(c)-mat_quad(inv,b[:N-1])
    # M=8 vertices per translational period. Bulk coefficient C=M*G.
    return Fraction(N)*G

print('MODEL three-layer Z-periodic 5-regular bulk templates with M=8')
print('CONVERSE_ENCODING K8 minus a 2-regular omitted-edge graph')
print('TWO_REGULAR_ISOMORPHISM_TYPES 8 5+3 4+4')

global_best=None
global_rec=None
for name,cycles in CYCLE_TYPES.items():
    E=present_edges(cycles)
    assert len(E)==20
    assert all(sum(1 for e in E if v in e)==5 for v in range(N))
    inv=laplacian_inverse(E)
    eligible=0
    best=None
    best_example=None
    for colors in product(range(3), repeat=N):
        if set(colors)!={0,1,2}:
            continue
        # Connected infinite voltage lift iff cycle voltages generate Z, i.e. gcd=1.
        if lift_voltage_gcd(E,colors)!=1:
            continue
        eligible+=1
        C=coefficient(E,inv,colors)
        if best is None or C<best:
            best=C;best_example=colors
    print('TYPE',name,'CONNECTED_SURJECTIVE_COLORINGS',eligible,
          'MIN_BULK_C',f'{best.numerator}/{best.denominator}',
          'EXAMPLE_COLORS',''.join(map(str,best_example)))
    if global_best is None or best<global_best:
        global_best=best
        global_rec=(name,best_example)

assert global_best==Fraction(263,51), global_best
assert global_best>4
print('GLOBAL_MIN_BULK_C',f'{global_best.numerator}/{global_best.denominator}')
print('SOURCE_D5_REFERENCE_BULK_C 4')
print('EXACT_GAP',f'{(global_best-4).numerator}/{(global_best-4).denominator}')
print('GLOBAL_MIN_TYPE',global_rec[0])
print('GLOBAL_MIN_EXAMPLE_COLORS',''.join(map(str,global_rec[1])))
print('CLAIM P16-D5-M8-THREELAYER-BULK-01 PASS')
print('ALL_EXACT_CHECKS_PASSED')
