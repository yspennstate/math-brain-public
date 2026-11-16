"""Sparse rational block algebra; all denominators are retained explicitly."""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from inherited17.inherited16.split34_algebra import tree_data

TREES={'star':[(0,1),(0,2),(0,3)],'path':[(0,1),(1,2),(2,3)]}

def variables():return ring('x,y,z,a,b,c,h',QQ)

def tree(rr,name,offset):
    return tree_data(rr,TREES[name],rr.gens[offset:offset+3],4)

def numerator(rr,block1,block2,lower=False):
    U,R1,D1,L1=block1;V,R2,D2,L2=block2
    R=R1*R2;D=D1*D2;k=(8 if lower else 6)+rr.gens[-1]
    tr1=sum(L1[i][i]for i in range(4));tr2=sum(L2[i][i]for i in range(4))
    tr=tr1*D2+tr2*D1
    square=sum(L1[i][j]**2 for i in range(4)for j in range(4))*D2**2
    square+=sum(L2[i][j]**2 for i in range(4)for j in range(4))*D1**2
    B=rr.zero;hn=rr.zero;Y=rr.zero
    for W,Rother,Dother,L in ((U,R2,D2,L1),(V,R1,D1,L2)):
        dd=D//Dother
        B+=Rother*Dother**2*sum(W[i]*W[j]*(int(i==j)*dd-L[i][j])**2 for i in range(4)for j in range(4))
        hn+=Rother*Dother*sum(W[i]**2*L[i][i]for i in range(4))
        Y+=-2*Rother*Dother**2*sum(L[i][j]*(W[i]-W[j])**2*(2*dd-L[i][i]-L[j][j]+2*L[i][j])for i in range(4)for j in range(i+1,4))
    massnum=tr+((k-7)*D if lower else 0)
    num=2*R*k*k*(D*tr-square)+2*k*(k+2)*B-k*k*Y
    num+=(massnum-2*D)/2*(2*(k+1)*(k-2)*R*D-2*k*R*massnum+2*(k+2)*hn)
    return num,R*D*D*k*k

def rank_data(rr,offset,endpoint):
    x,y,z=rr.gens[offset:offset+3]
    V=[3*x+2*y+z,-x+2*y+z,-x-2*y+z,-x-2*y-3*z]
    R=sum(v*v for v in V);p=-V[0]*V[3]
    G,H=(rr.zero,rr.one)if endpoint==0 else(R,4*p)
    K=[[rr.zero for j in range(2)]for i in range(4)]
    for col,j in enumerate((1,2)):
        K[0][col]=V[3]-V[j];K[j][col]=V[0]-V[3];K[3][col]=V[j]-V[0]
    return V,R,G,H,K

def block(rr,kind,offset,endpoint=1):
    if kind in TREES:
        U,R,D,L=tree(rr,kind,offset);K=[[u]for u in U]
    else:
        V,R,G,H,K=rank_data(rr,offset,endpoint)
        D=H
        # G=R at the nonzero endpoint: cancel R BEFORE expansion.
        L=[[(int(i==j)-QQ(1,4))*D-(V[i]*V[j]if endpoint else 0)for j in range(4)]for i in range(4)]
    d=len(K[0]);Q=[[sum(K[i][a]*K[i][b]for i in range(4))for b in range(d)]for a in range(d)]
    B=[[sum(K[i][a]*K[j][b]*(int(i==j)*D-L[i][j])**2 for i in range(4)for j in range(4))for b in range(d)]for a in range(d)]
    Hm=[[sum(K[i][a]*K[i][b]*L[i][i]for i in range(4))for b in range(d)]for a in range(d)]
    Ym=[[-2*sum(L[i][j]*(K[i][a]-K[j][a])*(K[i][b]-K[j][b])*(2*D-L[i][i]-L[j][j]+2*L[i][j])for i in range(4)for j in range(i+1,4))for b in range(d)]for a in range(d)]
    tr=sum(L[i][i]for i in range(4));square=sum(L[i][j]**2 for i in range(4)for j in range(4))
    return D,tr,square,Q,B,Hm,Ym,K,L

def pair(rr,left,right,ep1=1,ep2=1,lower=False,margin=0):
    D1,t1,v1,Q1,B1,H1,Y1,*_=block(rr,left,0,ep1)
    D2,t2,v2,Q2,B2,H2,Y2,*_=block(rr,right,3,ep2)
    D=D1*D2;k=(8 if lower else 6)+rr.gens[-1]
    tr=t1*D2+t2*D1;square=v1*D2**2+v2*D1**2
    mass=tr+((k-7)*D if lower else 0)
    const=2*k*k*(D*tr-square)+(mass-2*D)/2*(2*(k+1)*(k-2)*D-2*k*mass)-margin*k*k*D*D
    ids=[(i,j)for i in range(len(Q1))for j in range(len(Q2))]
    M=[]
    for a,b in ids:
        row=[]
        for c,d in ids:
            value=const*Q1[a][c]*Q2[b][d]
            value+=2*k*(k+2)*(D2**2*B1[a][c]*Q2[b][d]+D1**2*Q1[a][c]*B2[b][d])
            value-=k*k*(D2**2*Y1[a][c]*Q2[b][d]+D1**2*Q1[a][c]*Y2[b][d])
            value+=(mass-2*D)*(k+2)*(D2*H1[a][c]*Q2[b][d]+D1*Q1[a][c]*H2[b][d])
            row.append(value)
        M.append(row)
    return M,k*k*D*D,Q1,Q2
