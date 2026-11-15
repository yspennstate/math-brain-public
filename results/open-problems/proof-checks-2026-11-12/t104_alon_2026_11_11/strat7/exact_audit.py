"""Exact independent checks against the original matrix definitions.

These finite identity checks audit implementation; the universal proofs are
the written derivations and coefficient certificates, not these examples.
"""
import sympy as s
from tree_certificate import functional

def original(W,P,N):
    w=s.zeros(N);p=s.zeros(N)
    w[:W.rows,:W.cols]=W;p[:P.rows,:P.cols]=P
    mass=sum(w)/2;w/=mass
    L=s.diag(*list(w*s.ones(N,1)))-w;lm=1/mass
    G=lm*(s.eye(N)-s.ones(N)/N)-L
    c=s.Rational(2*N,N-2);beta=(1-lm)/(N-2)
    X1=2*(lm*s.trace(G)-s.trace(G*G))
    X2=c*sum(p[i,j]*G[i,j]**2 for i in range(N) for j in range(N))
    X3=beta*(2*s.trace(G)-c*sum(p[i,i]*G[i,i] for i in range(N)))
    Y=2*sum(w[i,j]*(p[i,i]+p[j,j]-2*p[i,j])*(G[i,i]+G[j,j]-2*G[i,j]) for i in range(N) for j in range(i+1,N))
    return s.factor((X1+X2+X3-Y)*mass**2)

def check(W,P):
    assert P*P==P and P*s.ones(P.rows,1)==s.zeros(P.rows,1) and s.trace(P)==2
    L=s.diag(*list(W*s.ones(W.rows,1)))-W
    assert L*P==P
    assert all(v>=0 for v in W)
    for N in [6,7,10]:
        assert s.factor(original(W,P,N)-functional(W,P,s.Integer(N-2)))==0

def main():
    from four_vertex_certificate import T as T4,g,t,k,q,m
    from triangle_certificate import T as T3,g as g3,h as h3,k as k3,p as p3,q as q3
    for U in [s.Matrix([3,-1,-1,-1]),s.Matrix([3,1,-1,-3]),s.Matrix([4,2,-1,-5])]:
        R=U.dot(U);Q=U*U.T/R;gap=s.Rational(1,5)
        for tt in [s.Integer(0),s.Rational(1,3),s.Integer(1)]:
            W=s.zeros(6);P=s.zeros(6)
            for i in range(4):
                for j in range(4):
                    if i!=j:W[i,j]=s.Rational(1,4)+gap*Q[i,j]
            W[4,5]=W[5,4]=tt/2
            P[:4,:4]=s.eye(4)-s.ones(4)/4-Q
            check(W,P)
            qq=sum(v**4 for v in U)/R**2;mm=sum(v**3 for v in U)**2/R**3
            for N in [6,9]:assert s.factor(original(W,P,N)-T4.subs({g:gap,t:tt,k:N-2,q:qq,m:mm}))==0
    for U in [s.Matrix([1,1,-2]),s.Matrix([1,2,-3])]:
        W=s.zeros(6);P=s.zeros(6);pp=-max(U)*min(U)/U.dot(U)
        for at,gap in [(0,s.Rational(1,5)),(3,s.Rational(2,5))]:
            Q=U*U.T/U.dot(U)
            for i in range(3):
                for j in range(3):
                    if i!=j:W[at+i,at+j]=s.Rational(1,3)+gap*Q[i,j]
            P[at:at+3,at:at+3]=s.eye(3)-s.ones(3)/3-Q
        check(W,P)
        for N in [6,8]:assert s.factor(original(W,P,N)-T3.subs({g3:s.Rational(1,5),h3:s.Rational(2,5),k3:N-2,p3:pp,q3:pp}))==0
    # Trees: verify the rational top eigenvectors directly.
    for v,edges in [(s.Matrix([-6,1,2,3]),[(0,1,s.Rational(1,7)),(0,2,s.Rational(1,4)),(0,3,s.Rational(1,3))]),(s.Matrix([1,-3,5,-3]),[(0,1,s.Rational(1,4)),(1,2,s.Rational(1,4)),(2,3,s.Rational(3,8))])]:
        W=s.zeros(6);P=s.zeros(6)
        for i,j,w in edges:W[i,j]=W[j,i]=w
        W[4,5]=W[5,4]=s.Rational(1,2)
        P[:4,:4]=v*v.T/v.dot(v);P[4:6,4:6]=s.Matrix([[1,-1],[-1,1]])/2
        check(W,P)
    # Five-vertex carrier: check the padding identity and the full moments.
    U=s.Matrix([3,1,-1,-3,0]);V=s.Matrix([1,-1,-1,1,0])
    Ru=U.dot(U);Rv=V.dot(V);assert U.dot(V)==0
    Q1=U*U.T/Ru;Q2=V*V.T/Rv
    W=s.zeros(6);P=s.zeros(6);ga=s.Rational(1,3);gb=s.Rational(1,5)
    for i in range(5):
        for j in range(5):
            if i!=j:W[i,j]=s.Rational(1,5)+ga*Q1[i,j]+gb*Q2[i,j]
    P[:5,:5]=s.eye(5)-s.ones(5)/5-Q1-Q2
    check(W,P)
    mass=(4-ga-gb)/2;a=ga/mass;b=gb/mass;ss=a+b;lm=1/mass
    AA=sum(v**4 for v in U)/Ru**2;BB=sum(v**4 for v in V)/Rv**2
    CC=sum(U[i]**2*V[i]**2 for i in range(5))/(Ru*Rv)
    du=sum(v**3 for v in U);hv=sum(v**3 for v in V)
    eu=sum(U[i]**2*V[i] for i in range(5));fv=sum(U[i]*V[i]**2 for i in range(5))
    d2=du**2/Ru**3;h2=hv**2/Rv**3;e2=eu**2/(Ru**2*Rv);f2=fv**2/(Ru*Rv**2)
    df=du*fv/(Ru**2*Rv);he=hv*eu/(Ru*Rv**2)
    F=a*(AA+CC)+b*(BB+CC);k2=a*a+b*b
    cubic=s.Rational(8,3)*(a*a*d2+b*b*h2)+s.Rational(2,3)*a*(a+5*b)*e2+s.Rational(2,3)*b*(b+5*a)*f2+2*ss*(a*df+b*he)
    T5=(14+2*ss)/9*(F-ss/5)+s.Rational(4,3)*k2-s.Rational(14,3)*(a*a*AA+b*b*BB)-4*(k2+a*b/3)*CC+cubic
    KS=a*a*AA+b*b*BB+2*a*b*CC-k2/5-a*a*(d2+e2)-2*a*b*(e2+f2)-b*b*(f2+h2)
    T6=T5-KS/3+(1-lm)*(162+169*ss-260*F)/720
    assert s.factor(original(W,P,6)/mass**2-T6)==0
    # Boundary matrix (6), checked against the original selected-projector functional.
    from split_boundary_certificate import matrix
    from concavity_certificate import cone
    xyz,Z,K=cone();subs=dict(zip(xyz,[1,2,3]));Z=Z.subs(subs);K=K.subs(subs)
    av=K*s.Matrix([2,-1]);R=Z.dot(Z);gg=s.Rational(1,7)
    W=s.zeros(6);P=s.zeros(6)
    for i in range(4):
        for j in range(4):
            if i!=j:W[i,j]=s.Rational(1,4)+gg*Z[i]*Z[j]/R
    W[4,5]=W[5,4]=s.Rational(1,2)
    P[:4,:4]=av*av.T/av.dot(av);P[4:6,4:6]=s.Matrix([[1,-1],[-1,1]])/2
    check(W,P)
    for N in [6,8]:
        assert s.factor(original(W,P,N)-(av.T*matrix(s.Integer(N-2),gg,Z)*av)[0]/av.dot(av))==0
    # Independently check the quadratic part (5) against the complete functional.
    PP=Z*Z.T/R;HH=s.eye(4)-s.ones(4)/4
    Lbase=HH-s.Rational(1,10)*(HH-PP)
    EE=K*s.Matrix([[2,1],[1,-1]])*K.T
    theta=s.symbols('theta');LL=Lbase+theta*EE
    W=s.zeros(6);P=s.zeros(6)
    for i in range(4):
        for j in range(4):
            if i!=j:W[i,j]=-LL[i,j]
    W[4,5]=W[5,4]=s.Rational(1,2);P[:4,:4]=PP
    P[4:6,4:6]=s.Matrix([[1,-1],[-1,1]])/2
    pv=PP.diagonal().T;ed=EE.diagonal().T;em=s.trace(EE)/2
    BE=sum(PP[i,j]*EE[i,j]**2 for i in range(4) for j in range(4))
    for kval in [s.Integer(4),s.Integer(7)]:
        Q=-2*s.trace(EE*EE)+(2*(kval+2)/kval-4)*BE+4*sum(PP[i,i]*(EE*EE)[i,i] for i in range(4))-2*(pv.T*EE*ed)[0]
        Q+=em/kval**2*(-4*kval*em+2*(kval+2)*pv.dot(ed))
        assert s.expand(functional(W,P,kval)).coeff(theta,2)==Q
    print('PROVED: exact matrix-definition audits pass for all rational fixtures and padding sizes.')
if __name__=='__main__':main()
