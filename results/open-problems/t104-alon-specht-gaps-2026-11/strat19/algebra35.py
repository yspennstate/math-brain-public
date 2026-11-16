"""Sparse exact block construction for the two triangle corners and five-trees."""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from inherited18.inherited17.inherited16.split34_algebra import tree_data

TREES = {
    'star': [(0,1),(0,2),(0,3),(0,4)],
    'path': [(0,1),(1,2),(2,3),(3,4)],
    'fork': [(0,1),(0,2),(0,3),(3,4)],
}

def variables():
    return ring('a,b,x,y,v,w,z', QQ)

def blocks(rr, corner, name):
    a,b,*_ = rr.gens
    if corner == 'path':
        left = tree_data(rr, [(0,1),(1,2)], (a,b), 3)
    else:
        left = ([rr.one,-rr.one,rr.zero],rr(2),rr(3),
                [[rr(3*int(i==j)-1) for j in range(3)] for i in range(3)])
    return left,tree_data(rr,TREES[name],rr.gens[2:6],5)

def numerator(rr, corner, name, lower=False):
    left,right=blocks(rr,corner,name)
    U,R1,D1,L1=left;V,R2,D2,L2=right
    R=R1*R2;D=D1*D2;k=(8 if lower else 6)+rr.gens[-1]
    tr=sum(L1[i][i] for i in range(3))*D2+sum(L2[i][i] for i in range(5))*D1
    square=sum(p*p for row in L1 for p in row)*D2**2+sum(p*p for row in L2 for p in row)*D1**2
    B=rr.zero;hn=rr.zero;Y=rr.zero
    for W,Rother,Dother,L in ((U,R2,D2,L1),(V,R1,D1,L2)):
        dd=D//Dother;n=len(W)
        B+=Rother*Dother**2*sum(W[i]*W[j]*(int(i==j)*dd-L[i][j])**2 for i in range(n) for j in range(n))
        hn+=Rother*Dother*sum(W[i]**2*L[i][i] for i in range(n))
        Y+=-2*Rother*Dother**2*sum(L[i][j]*(W[i]-W[j])**2*(2*dd-L[i][i]-L[j][j]+2*L[i][j]) for i in range(n) for j in range(i+1,n))
    massnum=tr+((k-7)*D if lower else 0)
    out=2*R*k*k*(D*tr-square)+2*k*(k+2)*B-k*k*Y
    out+=(massnum-2*D)/2*(2*(k+1)*(k-2)*R*D-2*k*R*massnum+2*(k+2)*hn)
    return out,R*D*D*k*k

def padding_coefficients(rr,p):
    return [rr.from_dict({e[:-1]+(0,):c for e,c in p.items() if e[-1]==j}) for j in (0,1,2)]
