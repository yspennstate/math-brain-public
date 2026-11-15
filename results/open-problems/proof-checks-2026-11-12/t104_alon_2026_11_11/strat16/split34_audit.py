"""Exact independent checks of the optional 3+4 reduction and certificates."""
import sympy as s
from split34_algebra import variables,tree_data,triangle,numerator
from split34_boundary import construct


def value(L,P,k):
    n=L.rows;A=s.eye(n)-L;mass=s.trace(L)/2
    B=sum(P[i,j]*A[i,j]**2 for i in range(n)for j in range(n))
    h=sum(P[i,i]*L[i,i]for i in range(n))
    Y=-2*sum(L[i,j]*(P[i,i]+P[j,j]-2*P[i,j])*(2-L[i,i]-L[j,j]+2*L[i,j])for i in range(n)for j in range(i+1,n))
    return (2*(s.trace(L)-s.trace(L*L))+2*(k+2)*B/k
            +(mass-1)/k**2*(2*(k+1)*(k-2)-4*k*mass+2*(k+2)*h)-Y)


def original(L,P,N):
    X=s.zeros(N);Q=s.zeros(N);X[:7,:7]=L;Q[:7,:7]=P
    mass=s.trace(X)/2;lam=1/mass;X/=mass
    assert Q*Q==Q and s.trace(Q)==2 and X*Q==lam*Q
    G=lam*(s.eye(N)-s.ones(N)/N)-X
    x1=2*(lam*s.trace(G)-s.trace(G*G))
    x2=2*s.Rational(N,N-2)*sum(Q[i,j]*G[i,j]**2 for i in range(N)for j in range(N))
    x3=(1-lam)/(N-2)*(2*s.trace(G)-2*s.Rational(N,N-2)*sum(Q[i,i]*G[i,i]for i in range(N)))
    y=-2*sum(X[i,j]*(Q[i,i]+Q[j,j]-2*Q[i,j])*(G[i,i]+G[j,j]-2*G[i,j])for i in range(N)for j in range(i+1,N))
    return s.factor(mass**2*(x1+x2+x3-y))


def main():
    rr,x,y,z,a,b,h=variables();point=(1,2,3,2,3,0);sub=dict(zip(rr.symbols,point))
    def ev(p):return s.sympify(p.as_expr()).subs(sub)
    for corner in ('balanced','path'):
        tu,tr,td,tl=triangle(rr,corner);U3=s.Matrix([ev(p)for p in tu]);R3=ev(tr);D3=ev(td);L3=s.Matrix([[ev(p)/D3 for p in row]for row in tl]);P3=U3*U3.T/R3
        for ep in (0,1):
            rb,M=construct(corner,ep)
            V=s.Matrix([10,6,-2,-14]);Rv=V.dot(V);p=-V[0]*V[3];g=0 if ep==0 else Rv/(4*p)
            L4=s.eye(4)-s.ones(4)/4-g*V*V.T/Rv
            K=s.zeros(4,2)
            for c,j in enumerate((1,2)):
                K[0,c]=V[3]-V[j];K[j,c]=V[0]-V[3];K[3,c]=V[j]-V[0]
            c=s.Matrix([1,2]);U4=K*c;R4=U4.dot(U4)
            L=s.diag(L4,L3);P=s.diag(U4*U4.T/R4,P3)
            for kk in (5,7,13):
                sub[rr.symbols[-1]]=kk-5
                MM=s.Matrix([[ev(p)for p in row]for row in M]);H=1 if ep==0 else 4*p
                val=(c.T*MM*c)[0]/(Rv**2*kk**2*D3**2*R3*H**2*R4)
                assert s.factor(val-value(L,P,s.Integer(kk)))==0
                assert original(L,P,kk+2)==val
        for edges in ([(0,1),(0,2),(0,3)],[(0,1),(1,2),(2,3)]):
            block=tree_data(rr,edges,(x,y,z),4);num,den=numerator(rr,block,triangle(rr,corner))
            uu,r,d,l=block;uu=s.Matrix([ev(p)for p in uu]);r=ev(r);d=ev(d);LL=s.Matrix([[ev(p)/d for p in row]for row in l]);PP=uu*uu.T/r
            L=s.diag(LL,L3);P=s.diag(PP,P3)
            for kk in (5,8):
                sub[rr.symbols[-1]]=kk-5
                assert s.factor(ev(num)/ev(den)-value(L,P,s.Integer(kk)))==0
                assert original(L,P,kk+2)==ev(num)/ev(den)
    print('PROVED (split34_audit.py): tree and boundary polynomials independently match the original selected-projector definitions at exact rational fixtures.')

if __name__=='__main__':main()
