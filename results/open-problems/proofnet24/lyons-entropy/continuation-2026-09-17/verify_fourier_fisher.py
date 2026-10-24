"""Exact identities and sample checks for the unproved count-Fisher route."""
from fractions import Fraction as F
from math import comb
from itertools import permutations
from pathlib import Path
import json
import verify_fourier_extension as core
from verify_fourier_barriers import count
from verify_shuffle_obstruction import log_bounds,scale,enclose_decimal


def det(M):
    n=len(M);ans=F(0)
    for p in permutations(range(n)):
        term=F((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
        for i,j in enumerate(p):term*=M[i][j]
        ans+=term
    return ans


def inverse(M):
    n=len(M);B=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        k=next(i for i in range(j,n) if B[i][j]);B[j],B[k]=B[k],B[j]
        pivot=B[j][j];B[j]=[v/pivot for v in B[j]]
        for i in range(n):
            if i!=j:
                c=B[i][j];B[i]=[x-c*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B]


def main():
    core.NN=4;variables=[]
    for i in range(4):
        k=[0]*4;k[i]=1;variables.append(core.Poly({tuple(k):1}))
    a,b,A,B=variables;C=A-B;E=a*B-b*A;D=C*C+4*(a-b)*E
    kap=[4*a*E+A*C,-2*E,-C,2*(a-b)]
    core.identity('influence derivative in a',2*kap[0]+4*b*kap[1]+2*B*kap[2],2*D)
    core.identity('influence derivative in b',2*kap[0]+4*a*kap[1]+2*A*kap[2],0)
    core.identity('influence derivative in A',kap[1]+2*b*kap[2]+B*kap[3],0)
    core.identity('influence derivative in B',kap[1]+2*a*kap[2]+A*kap[3],0)
    U=[1-2*a+A,2*a-2*A,A];V=[1-2*b+B,2*b-2*B,B]
    ff=[sum(U[i]*V[k-i] for i in range(3) if 0<=k-i<3) for k in range(5)]
    Z=[sum(kap[j-1]*comb(k,j) for j in range(1,min(4,k)+1)) for k in range(5)]
    EZ=sum(ff[k]*Z[k] for k in range(5));EN=sum(k*ff[k] for k in range(5))
    VA=2*a+2*A-4*a*a;VB=2*b+2*B-4*b*b
    core.identity('influence covariance with count',sum(k*ff[k]*Z[k] for k in range(5))-EZ*EN,D*VA)
    # Separate polynomial variables are now interpreted as a,b,x,y.
    aa,bb,xx,yy=variables;AA=aa*aa-xx*xx;BB=bb*bb-yy*yy
    resultant=(AA-BB)**2+4*(aa-bb)*(aa*BB-bb*AA)
    roots=[aa+xx,aa-xx];other=[bb+yy,bb-yy];cross=core.Poly(1)
    for p in roots:
        for q in other:cross*=p-q
    core.identity('pair resultant',resultant,cross)

    W=[[1,0,1,0],[0,1,0,1],[1,0,-1,0],[0,1,0,-1]]
    bases=[('4/5','1/5','1/10','1/20'),('1/2','1/1000','1/100','1/2000'),('1/5','9/10','1/10','1/20'),('83/100','9/100','1/20','3/100'),('3/5','1/5','1/10','1/20')]
    rows=[]
    for base in bases:
        av,bv,xv,yv=map(F,base);lam=[av+xv,bv+yv,av-xv,bv-yv]
        assert len(set(lam))==4 and all(0<p<1 for p in lam)
        f=count(lam);G=[[F(0) for _ in range(4)] for k in range(4)]
        for i in range(4):
            deleted=count([lam[j] for j in range(4) if j!=i])
            for k in range(4):
                for j in range(4):G[k][j]+=W[i][j]*deleted[k]
        df=[[((G[k-1][j] if k else 0)-(G[k][j] if k<4 else 0)) for j in range(4)] for k in range(5)]
        FI=[[sum(df[k][i]*df[k][j]/f[k] for k in range(5)) for j in range(4)] for i in range(4)]
        INV=inverse(FI)
        values=[av,bv,av*av-xv*xv,bv*bv-yv*yv];Dv=D.at(values);VAv=VA.at(values);VBv=VB.at(values)
        zv=[core.aspoly(p).at(values) for p in Z];mean=sum(p*z for p,z in zip(f,zv));var=sum(p*z*z for p,z in zip(f,zv))-mean*mean
        tau=var/(4*Dv*Dv)-VAv/4
        assert tau>=0
        assert INV[0][0]==VAv/4+tau and INV[1][1]==VBv/4+tau and INV[0][1]==-tau
        O=(av*(1-av)+xv*xv)*(bv*(1-bv)+yv*yv)
        P=(f[2]-2*O)/4;assert 0<O<P
        ell=log_bounds(O/P);assert ell[1]<0
        theta=F(2,5);adj_ab=-det([[FI[i][j] for j in range(4) if j!=0] for i in range(4) if i!=1]);minor=det([[FI[i][j] for j in [2,3]] for i in [2,3]])
        enclosure=[theta**4*det(FI)]*2
        for coeff,interval in [(4*theta**3*adj_ab,ell),(-4*theta**2*minor,(ell[1]**2,ell[0]**2))]:
            lo,hi=scale(coeff,interval);enclosure[0]+=lo;enclosure[1]+=hi
        assert enclosure[0]>0
        rows.append(dict(base=list(base),V_A=str(VAv),V_B=str(VBv),tau=str(tau),candidate_matrix_determinant_interval=enclose_decimal(enclosure),status='positive definite at this rational sample only'))
    out=dict(status='PASS: scalar-reduction identities and finite candidate checks; global Fisher inequality UNPROVED',polynomial_identity_count=len(core.checks),polynomial_identities=core.checks,rational_candidate_cases=rows)
    Path(__file__).with_name('fourier_fisher_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status=out['status'],polynomial_identity_count=len(core.checks),rational_candidate_case_count=len(rows)),indent=2))


if __name__=='__main__':main()
