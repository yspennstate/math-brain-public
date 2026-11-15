"""Sparse exact algebra for the optional split 3+4 extension."""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ


def variables():return ring('x,y,z,a,b,h',QQ)


def tree_data(rr,edges,fluxes,n):
    sizes=[sum(t for e,t in zip(edges,fluxes)if i in e)for i in range(n)]
    signs=[None]*n;signs[0]=1
    while None in signs:
        for i,j in edges:
            if signs[i]is not None:signs[j]=-signs[i]
            elif signs[j]is not None:signs[i]=-signs[j]
    U=[v*sg for v,sg in zip(sizes,signs)];R=sum(v*v for v in U)
    ds=[sizes[i]+sizes[j]for i,j in edges];D=rr.one
    for a in ds:D*=a
    L=[[rr.zero for j in range(n)]for i in range(n)]
    for e,((i,j),t)in enumerate(zip(edges,fluxes)):
        w=t
        for f,q in enumerate(ds):
            if e!=f:w*=q
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    assert sum(U)==0
    assert all(sum(L[i][j]*U[j]for j in range(n))==D*U[i]for i in range(n))
    return U,R,D,L


def triangle(rr,corner):
    a,b=rr.gens[3:5]
    if corner=='path':return tree_data(rr,[(0,1),(1,2)],(a,b),3)
    U=[rr.one,-rr.one,rr.zero];R=rr(2);D=rr(3)
    return U,R,D,[[rr(3*int(i==j)-1)for j in range(3)]for i in range(3)]


def numerator(rr,block1,block2):
    U,R1,D1,L1=block1;V,R2,D2,L2=block2;n=len(U);m=len(V);R=R1*R2;D=D1*D2;k=5+rr.gens[-1]
    L=[[rr.zero for j in range(n+m)]for i in range(n+m)]
    P=[[rr.zero for j in range(n+m)]for i in range(n+m)]
    for i in range(n):
        for j in range(n):L[i][j]=D2*L1[i][j];P[i][j]=R2*U[i]*U[j]
    for i in range(m):
        for j in range(m):L[n+i][n+j]=D1*L2[i][j];P[n+i][n+j]=R1*V[i]*V[j]
    N=n+m;tr=sum(L[i][i]for i in range(N));tr2=sum(L[i][j]**2 for i in range(N)for j in range(N))
    B=sum(P[i][j]*(int(i==j)*D-L[i][j])**2 for i in range(N)for j in range(N))
    hn=sum(P[i][i]*L[i][i]for i in range(N))
    Y=-2*sum(L[i][j]*(P[i][i]+P[j][j]-2*P[i][j])*(2*D-L[i][i]-L[j][j]+2*L[i][j])for i in range(N)for j in range(i+1,N))
    num=2*R*k*k*(D*tr-tr2)+2*k*(k+2)*B-k*k*Y
    num+=(tr-2*D)/2*(2*(k+1)*(k-2)*R*D-2*k*R*tr+2*(k+2)*hn)
    return num,R*D*D*k*k
