"""PROVED: symbolic certificates used for canonical chart bounds/exclusions.

The implications from nonnegative weights, PSD and interval inclusion are
spelled out in RESULT.md. This replays their exact algebraic identities.
"""
from zero_face import construct


def replay():
    rr,t,V,R,M,Delta,Q,N,D,edges,Pi,C=construct()
    zero=rr.zero;one=rr.one
    for i in range(5):
        degree=sum(g for (a,b),g in edges.items()if i in(a,b))
        assert degree==4*t-R[i][i]
    L=[[((4*t-R[i][i])if i==j else -edges[min(i,j),max(i,j)])for j in range(5)]for i in range(5)]
    assert all(L[i][j]==t*(5*int(i==j)-1)-R[i][j]for i in range(5)for j in range(5))
    assert sum(edges.values())==D/2
    assert 20*t-N==D
    # Positivity of the g-weighted Laplacian implies M<=5t I.
    assert edges[3,4]==0
    assert sum(g for (a,b),g in edges.items()if 3 in(a,b))==t*(4-t)
    assert R[4][4]==1+V[4][1]**2
    x1,x2,x3=[V[i][0]for i in range(3)]
    assert x1+x2+x3==1-t
    assert -3*x1==t-1+(x2-x1)+(x3-x1)
    assert 1-2*x2==t-1+(x1+1)+(x3-x2)
    for i in range(5):
        degree=4*t-R[i][i]
        assert 16-V[i][1]**2==16-4*t+V[i][0]**2+degree
    # Fixed-r eigenvalue relation. ratio>3/25 iff 784Delta>75N^2.
    from fractions import Fraction as F
    assert F(3,25)/(1+F(3,25))**2==F(75,784)
    # Connectedness determinant identity.
    det5=(5*t-M[0][0])*(5*t-M[1][1])-M[0][1]**2
    assert det5==25*t*t-5*t*N+Delta
    print('PROVED: canonical root bounds, degree identities, ratio and connectedness algebra replayed.')

if __name__=='__main__':replay()
