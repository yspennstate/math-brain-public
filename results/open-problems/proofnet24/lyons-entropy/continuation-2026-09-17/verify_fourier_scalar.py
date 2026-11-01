"""Coefficientwise rational self-checks for FOURIER_ONE_SCALAR.md."""
from itertools import combinations,permutations
from pathlib import Path
import json
import verify_fourier_extension as core


def det(M):
    ans=core.Poly()
    for p in permutations(range(len(M))):
        term=core.Poly((-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p))))
        for i,j in enumerate(p):term*=M[i][j]
        ans+=term
    return ans


def prod(items):
    p=core.Poly(1)
    for item in items:p*=item
    return p


def main():
    core.NN=11
    variables=[]
    for i in range(11):
        k=[0]*11;k[i]=1;variables.append(core.Poly({tuple(k):1}))
    q0,q1,q2,q3=variables[:4]
    X=q0+q2;Y=q1+q3;U=q0*q2;V=q1*q3;C=X*Y+2*U+2*V
    core.identity('strict endpoint odds ratio numerator',(X+Y)**2-2*C,(q0-q2)**2+(q1-q3)**2)
    core.identity('strict middle odds ratio numerator',C*X*Y-2*(X+Y)*(U*Y+V*X),((X*X-4*U)*Y*Y+(Y*Y-4*V)*X*X)/2)

    a,b,x,y,c,d,u,v=variables[:8]
    lam=[a+x,b+y,a-x,b-y];slope=[c+u,d+v,c-u,d-v]
    f0=prod([1-p for p in lam]);deleted=[prod([1-lam[j] for j in range(4) if j!=i]) for i in range(4)]
    g0=sum(slope[i]*deleted[i] for i in range(4))
    h0=sum(2*slope[i]*slope[j]*prod([1-lam[k] for k in range(4) if k not in [i,j]]) for i,j in combinations(range(4),2))
    core.identity('empty-event coercivity identity',h0*f0,g0*g0-sum(slope[i]**2*deleted[i]**2 for i in range(4)))

    # A generic symmetric matrix: this checks the determinant update as a
    # polynomial identity in all ten independent entries and ell.
    R=[[None]*4 for _ in range(4)];n=0
    for i in range(4):
        for j in range(i,4):R[i][j]=R[j][i]=variables[n];n+=1
    ell=variables[10];Q=[row[:] for row in R]
    Q[0][1]+=2*ell;Q[1][0]+=2*ell
    adj_ab=-det([[R[i][j] for j in range(4) if j!=0] for i in range(4) if i!=1])
    minor_xy=det([[R[i][j] for j in [2,3]] for i in [2,3]])
    core.identity('generic symmetric determinant update',det(Q),det(R)+4*ell*adj_ab-4*ell*ell*minor_xy)
    out=dict(status='PASS: exact polynomial self-checks; global Phi_F sign remains unproved',polynomial_identity_count=len(core.checks),polynomial_identities=core.checks)
    Path(__file__).with_name('fourier_scalar_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
