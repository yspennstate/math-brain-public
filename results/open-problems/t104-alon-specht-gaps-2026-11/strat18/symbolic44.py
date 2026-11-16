"""Universal sparse identity auditing the tensor certificate numerator."""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from algebra44 import block,pair
from padding44 import JOBS
from inherited17.memory_guard import install

def main():
    install(850_000_000)
    rr,*gs=ring('x,y,z,a,b,c,p,q,r,s,h',QQ)
    for left,right,ep1,ep2 in JOBS:
        d1,*_,K1,L1=block(rr,left,0,ep1)
        d2,*_,K2,L2=block(rr,right,3,ep2)
        c1=gs[6:6+len(K1[0])];c2=gs[8:8+len(K2[0])]
        U=[sum(a*b for a,b in zip(row,c1))for row in K1]
        V=[sum(a*b for a,b in zip(row,c2))for row in K2]
        R1=sum(u*u for u in U);R2=sum(v*v for v in V);R=R1*R2;D=d1*d2
        # Direct 8x8, selected-projector construction. No operator formula.
        L=[[rr.zero for j in range(8)]for i in range(8)]
        P=[[rr.zero for j in range(8)]for i in range(8)]
        for i in range(4):
            for j in range(4):
                L[i][j]=d2*L1[i][j];L[i+4][j+4]=d1*L2[i][j]
                P[i][j]=R2*U[i]*U[j];P[i+4][j+4]=R1*V[i]*V[j]
        tr=sum(L[i][i]for i in range(8));sq=sum(L[i][j]**2 for i in range(8)for j in range(8))
        B=sum(P[i][j]*(int(i==j)*D-L[i][j])**2 for i in range(8)for j in range(8))
        hn=sum(P[i][i]*L[i][i]for i in range(8))
        Y=-2*sum(L[i][j]*(P[i][i]+P[j][j]-2*P[i][j])*(2*D-L[i][i]-L[j][j]+2*L[i][j])for i in range(8)for j in range(i+1,8))
        for lower in (False,True):
            k=(8 if lower else 6)+gs[-1];mass=tr+((k-7)*D if lower else 0)
            direct=2*R*k*k*(D*tr-sq)+2*k*(k+2)*B-k*k*Y
            direct+=(mass-2*D)/2*(2*(k+1)*(k-2)*R*D-2*k*R*mass+2*(k+2)*hn)
            M,den,*_=pair(rr,left,right,ep1,ep2,lower)
            cc=[u*v for u in c1 for v in c2]
            contracted=sum(cc[i]*M[i][j]*cc[j]for i in range(len(cc))for j in range(len(cc)))
            assert contracted==direct,(left,right,ep1,ep2,lower)
            assert den==k*k*D*D
        print(left,right,ep1,ep2,'universal identities PASS',flush=True)
    print('PROVED (symbolic44.py): all twenty isolate/lower tensor numerators equal the direct 8x8 matrix functional as polynomial identities.')

if __name__=='__main__':main()
