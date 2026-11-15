"""Sparse exact four-tree/five-tree block algebra."""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from inherited19.inherited18.inherited17.inherited16.split34_algebra import tree_data
FOUR={'star':[(0,1),(0,2),(0,3)],'path':[(0,1),(1,2),(2,3)]}
FIVE={'star':[(0,1),(0,2),(0,3),(0,4)],'path':[(0,1),(1,2),(2,3),(3,4)],'fork':[(0,1),(0,2),(0,3),(3,4)]}
def variables():return ring('a,b,c,x,y,v,w,z',QQ)
def blocks(rr,left,right):return tree_data(rr,FOUR[left],rr.gens[:3],4),tree_data(rr,FIVE[right],rr.gens[3:7],5)
def numerator(rr,left,right,lower=False):
    (U,R1,D1,L1),(V,R2,D2,L2)=blocks(rr,left,right)
    R=R1*R2;D=D1*D2;k=(9 if lower else 7)+rr.gens[-1]
    tr=sum(L1[i][i]for i in range(4))*D2+sum(L2[i][i]for i in range(5))*D1
    square=sum(p*p for row in L1 for p in row)*D2**2+sum(p*p for row in L2 for p in row)*D1**2
    B=rr.zero;hn=rr.zero;Y=rr.zero
    for W,Rother,Dother,L in ((U,R2,D2,L1),(V,R1,D1,L2)):
        dd=D//Dother;n=len(W)
        B+=Rother*Dother**2*sum(W[i]*W[j]*(int(i==j)*dd-L[i][j])**2 for i in range(n)for j in range(n))
        hn+=Rother*Dother*sum(W[i]**2*L[i][i]for i in range(n))
        Y+=-2*Rother*Dother**2*sum(L[i][j]*(W[i]-W[j])**2*(2*dd-L[i][i]-L[j][j]+2*L[i][j])for i in range(n)for j in range(i+1,n))
    mass=tr+((k-8)*D if lower else 0)
    out=2*R*k*k*(D*tr-square)+2*k*(k+2)*B-k*k*Y
    out+=(mass-2*D)/2*(2*(k+1)*(k-2)*R*D-2*k*R*mass+2*(k+2)*hn)
    return out,R*D*D*k*k

def padding_coefficients(rr,p):return [rr.from_dict({e[:-1]+(0,):c for e,c in p.items()if e[-1]==j})for j in (0,1,2)]
