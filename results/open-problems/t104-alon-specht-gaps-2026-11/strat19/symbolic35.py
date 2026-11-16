"""Universal direct-matrix polynomial audits and path moment identities."""
from algebra35 import variables,blocks,numerator,TREES
from inherited18.inherited17.memory_guard import install

def main():
    install(850_000_000);rr,*_=variables();a,b=rr.gens[:2]
    W,R,D,L=blocks(rr,'path','star')[0]
    tr=sum(L[i][i] for i in range(3));ln=tr-D
    bn=sum(W[i]*W[j]*(int(i==j)*D-L[i][j])**2 for i in range(3) for j in range(3))
    hn=sum(W[i]**2*L[i][i] for i in range(3))
    yn=-2*sum(L[i][j]*(W[i]-W[j])**2*(2*D-L[i][i]-L[j][j]+2*L[i][j]) for i in range(3) for j in range(i+1,3))
    assert ln==3*a*b and D-3*ln==2*(a-b)**2
    assert 6*(D-ln)*bn==R*ln**2*(3*D-ln)
    assert 6*hn==R*(3*D+ln)
    assert yn==R*ln*(D-ln)+6*bn
    for corner in ('balanced','path'):
        for name in TREES:
            (U,R1,D1,L1),(V,R2,D2,L2)=blocks(rr,corner,name)
            R=R1*R2;D=D1*D2
            L=[[rr.zero for j in range(8)] for i in range(8)]
            P=[[rr.zero for j in range(8)] for i in range(8)]
            for i in range(3):
                for j in range(3):L[i][j]=D2*L1[i][j];P[i][j]=R2*U[i]*U[j]
            for i in range(5):
                for j in range(5):L[i+3][j+3]=D1*L2[i][j];P[i+3][j+3]=R1*V[i]*V[j]
            tr=sum(L[i][i] for i in range(8));sq=sum(p*p for row in L for p in row)
            B=sum(P[i][j]*(int(i==j)*D-L[i][j])**2 for i in range(8) for j in range(8))
            h=sum(P[i][i]*L[i][i] for i in range(8))
            Y=-2*sum(L[i][j]*(P[i][i]+P[j][j]-2*P[i][j])*(2*D-L[i][i]-L[j][j]+2*L[i][j]) for i in range(8) for j in range(i+1,8))
            for lower in (False,True):
                k=(8 if lower else 6)+rr.gens[-1];mass=tr+((k-7)*D if lower else 0)
                direct=2*R*k*k*(D*tr-sq)+2*k*(k+2)*B-k*k*Y
                direct+=(mass-2*D)/2*(2*(k+1)*(k-2)*R*D-2*k*R*mass+2*(k+2)*h)
                num,den=numerator(rr,corner,name,lower)
                assert num==direct and den==R*D*D*k*k
            print(corner,name,'both direct identities PASS',flush=True)
    print('PROVED (symbolic35.py): twelve direct 8x8 polynomial identities and the universal three-path moments.')

if __name__=='__main__':main()
