"""Independent exact matrix audits and feasible negative-increment fixtures."""
import sympy as s
from lower_formula import x3


def H(n):return s.eye(n)-s.ones(n)/n

def direction(n):
    u=s.Matrix([1,-1]+[0]*(n-2))
    return u*u.T/2


def data(L,P):
    n=L.rows;A=s.eye(n)-L
    M=s.trace(L)/2
    h=sum(P[i,i]*L[i,i] for i in range(n))
    B=sum(P[i,j]*A[i,j]**2 for i in range(n) for j in range(n))
    Y=-2*sum(L[i,j]*(P[i,i]+P[j,j]-2*P[i,j])*
              (2-L[i,i]-L[j,j]+2*L[i,j]) for i in range(n) for j in range(i+1,n))
    return M,h,B,Y


def formula(L,P):
    k=s.Integer(L.rows-2);M,h,B,Y=data(L,P)
    return s.factor(2*(s.trace(L)-s.trace(L*L))+2*(k+2)*B/k+x3(k,M,h)-Y)


def original(L,P):
    n=L.rows;k=s.Integer(n-2);M=s.trace(L)/2;lam=1/M;W=L/M
    G=lam*H(n)-W
    X1=2*(lam*s.trace(G)-s.trace(G*G))
    X2=2*s.Rational(n,n-2)*sum(P[i,j]*G[i,j]**2 for i in range(n) for j in range(n))
    X3=(1-lam)/k*(2*s.trace(G)-2*s.Rational(n,n-2)*sum(P[i,i]*G[i,i] for i in range(n)))
    Y=-2*sum(W[i,j]*(P[i,i]+P[j,j]-2*P[i,j])*
              (G[i,i]+G[j,j]-2*G[i,j]) for i in range(n) for j in range(i+1,n))
    return s.factor(M*M*(X1+X2+X3-Y))


def lap(n,edges):
    out=s.zeros(n)
    for i,j,w in edges:
        out[i,i]+=w;out[j,j]+=w;out[i,j]-=w;out[j,i]-=w
    return out


def main():
    eps=s.Rational(1,100);P2=direction(2)
    cases=[('2+5',s.diag(P2,H(5)-eps*(H(5)-direction(5))),s.diag(P2,direction(5))),
           ('3+4',s.diag(*[H(n)-eps*(H(n)-direction(n)) for n in (3,4)]),s.diag(direction(3),direction(4))),
           ('double5',H(5)-eps*(H(5)-s.diag(H(3),s.zeros(2))),s.diag(H(3),s.zeros(2)))]
    lows=[('edge',s.Rational(99,100)*P2),
          ('path3',lap(3,[(0,1,s.Rational(1,10)),(1,2,s.Rational(1,10))])),
          ('star4',lap(4,[(0,j,s.Rational(1,10))for j in (1,2,3)])),
          ('triangle',H(3)/3),('clique5',H(5)/5)]
    count=0
    for name,C,Pc in cases:
        assert Pc*Pc==Pc and s.trace(Pc)==2 and C*Pc==Pc
        assert C*s.ones(C.rows,1)==s.zeros(C.rows,1)
        # Exact spectral construction: C acts by 1 and 99/100 on the two
        # complementary orthogonal subspaces of 1-perpendicular.
        HH=H(5) if name=='double5' else s.diag(H(2),H(5)) if name=='2+5' else s.diag(H(3),H(4))
        assert (C-Pc)==(1-eps)*(HH-Pc)
        for lname,D in lows:
            n=C.rows+D.rows;L=s.diag(C,D);P=s.diag(Pc,s.zeros(D.rows));L0=s.diag(C,s.zeros(D.rows))
            # Edge spectrum is {0,99/100}; the other lower PSD Laplacians
            # have trace<=1, or are the explicit scaled clique projectors.
            assert all(D[i,j]<=0 for i in range(D.rows)for j in range(i+1,D.rows))
            if lname not in ('edge','triangle','clique5'):assert s.trace(D)<1
            for extra in (0,2):
                LL=s.diag(L,s.zeros(extra));PP=s.diag(P,s.zeros(extra))
                assert formula(LL,PP)==original(LL,PP);assert formula(LL,PP)>0;count+=1
            m0,h0,b0,y0=data(L0,P);m1,h1,b1,y1=data(L,P)
            assert h1==h0 and b1==b0 and y1==y0 and m1-m0==s.trace(D)/2
            tt=s.trace(D);kk=s.Integer(n-2)
            increment=2*(s.trace(D)-s.trace(D*D))+x3(kk,m0+tt/2,h0)-x3(kk,m0,h0)
            assert s.factor(formula(L,P)-formula(L0,P)-increment)==0
            if lname=='edge':
                assert increment<0
                print(name,'negative increment',s.factor(increment),'positive T*',formula(L,P))
        if name=='2+5':
            A=s.eye(5)-C[2:7,2:7];S=A-s.ones(5)/5;pp=Pc[2:7,2:7]
            cc=s.Rational(13,10)
        elif name=='3+4':
            S=s.diag(H(3)-C[:3,:3],H(4)-C[3:7,3:7]);pp=Pc;cc=s.Rational(17,12)
        else:continue
        dd=sum(pp[i,i]*S[i,i] for i in range(S.rows));tau=s.trace(S)
        mm,hh,bb,yy=data(C,Pc)
        assert mm==(5-tau)/2 and hh==cc-dd and 0<=bb<=dd<=cc-1
    print('PROVED (matrix_audit.py):',count,'original-formula audits; exact lower increments and gap moments; actual rational negative increments have positive full T.')

if __name__=='__main__':main()
