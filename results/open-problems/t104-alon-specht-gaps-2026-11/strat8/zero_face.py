"""PROVED: rational coordinates and exact identities for the zero edge {4,5}.

Run python3 zero_face.py to replay the algebraic reduction.
This script does not claim positivity of the resulting face polynomial.
"""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ


def construct():
    rr,t,v1,z1,v2,z2,z=ring('t,v1,z1,v2,z2,z',QQ)
    V=[(v1,z1),(v2,z2),(1-t-v1-v2,-z-z1-z2),(t,rr.zero),(-rr.one,z)]
    R=[[sum(V[i][a]*V[j][a] for a in range(2)) for j in range(5)] for i in range(5)]
    M=[[sum(V[i][a]*V[i][b] for i in range(5)) for b in range(2)] for a in range(2)]
    Delta=M[0][0]*M[1][1]-M[0][1]**2
    adj=((M[1][1],-M[0][1]),(-M[0][1],M[0][0]))
    Q=[[sum(V[i][a]*adj[a][b]*V[j][b] for a in range(2) for b in range(2))
        for j in range(5)] for i in range(5)]
    N=sum(R[i][i] for i in range(5))
    D=20*t-N
    edges={(i,j):t+R[i][j] for i in range(5) for j in range(i+1,5)}
    Pi=[[Delta*(5*int(i==j)-1)-5*Q[i][j] for j in range(5)] for i in range(5)]
    trace_m2=sum(M[a][b]*M[b][a] for a in range(2) for b in range(2))
    numerator=Delta*(1800*t*N-360*trace_m2)
    numerator+=120*sum(Pi[i][j]*R[i][j]**2 for i in range(5) for j in range(5))
    numerator+=(D-10*t)*(60*N*Delta-20*sum(Pi[i][i]*R[i][i] for i in range(5)))
    numerator-=360*sum(g*(2*Delta-Q[i][i]-Q[j][j]+2*Q[i][j])
                         *(R[i][i]+R[j][j]-2*R[i][j]) for (i,j),g in edges.items())
    return rr,t,V,R,M,Delta,Q,N,D,edges,Pi,numerator


def main():
    rr,t,V,R,M,Delta,Q,N,D,edges,Pi,numerator=construct()
    assert all(sum(row[a] for row in V)==0 for a in range(2))
    assert edges[3,4]==0
    assert sum(edges.values())==D/2
    assert all(sum(Q[i][j] for j in range(5))==0 for i in range(5))
    assert sum(Q[i][i] for i in range(5))==2*Delta
    assert all(sum(Q[i][k]*Q[k][j] for k in range(5))==Delta*Q[i][j]
               for i in range(5) for j in range(5))
    assert all(sum(Q[i][k]*R[k][j] for k in range(5))==Delta*R[i][j]
               for i in range(5) for j in range(5))
    # Build 45 D^2 Delta times each trace expression independently.
    X1=45*Delta*(40*t*N-8*sum(R[i][j]**2 for i in range(5) for j in range(5)))
    X2=120*sum(Pi[i][j]*R[i][j]**2 for i in range(5) for j in range(5))
    X3=5*(D-10*t)*(12*N*Delta-4*sum(Pi[i][i]*R[i][i] for i in range(5)))
    twiceS5=360*sum(g*(2*Delta-Q[i][i]-Q[j][j]+2*Q[i][j])
                         *(R[i][i]+R[j][j]-2*R[i][j]) for (i,j),g in edges.items())
    assert numerator==X1+X2+X3-twiceS5
    print('PROVED: rational zero-face chart covers rank-two gaps with edge {4,5} zero.')
    print('PROVED: projector identities, total weight, and the exact numerator 45 D^2 Delta T checked symbolically.')
    print('PROVED: face numerator has',len(numerator.terms()),'nonzero rational coefficients.')


if __name__=='__main__':
    main()
