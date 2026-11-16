"""Sparse exact five/five block algebra over QQ."""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from inherited20.inherited19.inherited18.inherited17.inherited16.split34_algebra import tree_data
FIVE={'star':[(0,1),(0,2),(0,3),(0,4)],'path':[(0,1),(1,2),(2,3),(3,4)],'fork':[(0,1),(0,2),(0,3),(3,4)]}
def variables():return ring('a,b,c,d,x,y,v,w,z',QQ)
def blocks(rr,left,right):return tree_data(rr,FIVE[left],rr.gens[:4],5),tree_data(rr,FIVE[right],rr.gens[4:8],5)
def numerator(rr,left,right,lower=False):
    (U,R1,D1,L1),(V,R2,D2,L2)=blocks(rr,left,right)
    R=R1*R2;D=D1*D2;k=(10 if lower else 8)+rr.gens[-1]
    tr=sum(L1[i][i]for i in range(5))*D2+sum(L2[i][i]for i in range(5))*D1
    square=sum(p*p for row in L1 for p in row)*D2**2+sum(p*p for row in L2 for p in row)*D1**2
    B=rr.zero;hn=rr.zero;Y=rr.zero
    for W,Rother,Dother,L in ((U,R2,D2,L1),(V,R1,D1,L2)):
        dd=D//Dother
        B+=Rother*Dother**2*sum(W[i]*W[j]*(int(i==j)*dd-L[i][j])**2 for i in range(5)for j in range(5))
        hn+=Rother*Dother*sum(W[i]**2*L[i][i]for i in range(5))
        Y+=-2*Rother*Dother**2*sum(L[i][j]*(W[i]-W[j])**2*(2*dd-L[i][i]-L[j][j]+2*L[i][j])for i in range(5)for j in range(i+1,5))
    mass=tr+((k-9)*D if lower else 0)
    return assemble(k,R,D,tr,square,B,hn,Y,mass),R*D*D*k*k

def block(rr,kind,ep=1):
    if kind in FIVE:
        U,R,D,L=tree_data(rr,FIVE[kind],rr.gens[:4],5);K=[[u]for u in U]
    else:
        gaps=rr.gens[:4]
        V=[sum((5-j if i<j else -j)*gaps[j-1]for j in range(1,5))for i in range(5)]
        R=sum(v*v for v in V);D=5*(-V[0]*V[4]) if ep else rr.one
        K=[[rr.zero for j in range(3)]for i in range(5)]
        for col,j in enumerate((1,2,3)):
            K[0][col]=V[4]-V[j];K[j][col]=V[0]-V[4];K[4][col]=V[j]-V[0]
        L=[[(int(i==j)-QQ(1,5))*D-(V[i]*V[j]if ep else 0)for j in range(5)]for i in range(5)]
    d=len(K[0]);Q=[[sum(K[i][a]*K[i][b]for i in range(5))for b in range(d)]for a in range(d)]
    B=[[sum(K[i][a]*K[j][b]*(int(i==j)*D-L[i][j])**2 for i in range(5)for j in range(5))for b in range(d)]for a in range(d)]
    H=[[sum(K[i][a]*K[i][b]*L[i][i]for i in range(5))for b in range(d)]for a in range(d)]
    Y=[[-2*sum(L[i][j]*(K[i][a]-K[j][a])*(K[i][b]-K[j][b])*(2*D-L[i][i]-L[j][j]+2*L[i][j])for i in range(5)for j in range(i+1,5))for b in range(d)]for a in range(d)]
    tr=sum(L[i][i]for i in range(5));square=sum(p*p for row in L for p in row)
    return D,tr,square,Q,B,H,Y,K,L


def assemble(k,R,D,tr,square,B,hn,Y,mass):
    out=2*R*k*k*(D*tr-square)+2*k*(k+2)*B-k*k*Y
    out+=(mass-2*D)/2*(2*(k+1)*(k-2)*R*D-2*k*R*mass+2*(k+2)*hn)
    return out
