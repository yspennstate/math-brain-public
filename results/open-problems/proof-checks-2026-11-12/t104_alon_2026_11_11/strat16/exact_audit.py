"""Exact independent matrix audits; finite fixtures do not replace universal proofs."""
import sympy as s
from algebra import functional,quadratic,spanning,laplacian
from rank_three_target import construct


def original(L,U,N):
    full=s.zeros(N);full[:5,:5]=L
    full[5:7,5:7]=s.Matrix([[1,-1],[-1,1]])/2
    mass=s.trace(full)/2;lam=1/mass;full/=mass
    P=s.zeros(N);P[:5,:5]=U*U.T/U.dot(U)
    P[5:7,5:7]=s.Matrix([[1,-1],[-1,1]])/2
    H=s.eye(N)-s.ones(N)/N;G=lam*H-full
    assert full*P==lam*P and P*s.ones(N,1)==s.zeros(N,1)
    X1=2*(lam*s.trace(G)-s.trace(G*G))
    X2=2*s.Rational(N,N-2)*sum(P[i,j]*G[i,j]**2 for i in range(N)for j in range(N))
    X3=(1-lam)/(N-2)*(2*s.trace(G)-2*s.Rational(N,N-2)*sum(P[i,i]*G[i,i]for i in range(N)))
    Y=-2*sum(full[i,j]*(P[i,i]+P[j,j]-2*P[i,j])*(G[i,i]+G[j,j]-2*G[i,j])for i in range(N)for j in range(i+1,N))
    return s.factor(mass**2*(X1+X2+X3-Y))


def main():
    k,t=s.symbols('k t');U=s.Matrix([5,2,0,-3,-4]);K=spanning(U)
    assert K.rank()==3 and K.T*s.ones(5,1)==s.zeros(3,1) and K.T*U==s.zeros(3,1)
    E=K*s.Matrix([[2,1,-1],[1,3,2],[-1,2,-2]])*K.T/100
    H=s.eye(5)-s.ones(5)/5
    L=H-(H-U*U.T/U.dot(U))/10
    expr=s.Poly(s.expand(functional(L+t*E,U,k)),t)
    assert s.factor(expr.coeff_monomial(t*t)-quadratic(E,U,k))==0
    for N in (7,8,13):assert original(L,U,N)==functional(L,U,s.Integer(N-2))
    rr,V,R,mats,controls,gs,bounds=construct()
    for point in ((2,-s.Rational(1,2),s.Rational(1,3),0,-s.Rational(2,3),s.Rational(1,2)),
                  (1,-1,1,0,-1,0),(3,0,-s.Rational(1,2),-1,1,1)):
        sub=dict(zip(rr.symbols,point))
        def ev(p):return s.sympify(p.as_expr()).subs(sub)
        VV=s.Matrix([[ev(a)for a in row]for row in V]);SS=VV*VV.T/(5*point[0]);LL=H-SS
        us=s.Matrix.hstack(s.ones(5,1),VV).T.nullspace()
        assert len(us)>=2
        for uu in us:
            for kk in (5,7,11):
                z=s.Rational(1,kk)
                MM=s.Matrix([[ev(mats[0][i][j]+z*mats[1][i][j]+z*z*mats[2][i][j])for j in range(4)]for i in range(4)])
                # u=K0*u[:4], because u has zero sum.
                val=(uu[:4,0].T*MM*uu[:4,0])[0]/(50*point[0]**2*uu.dot(uu))
                assert s.factor(val-functional(LL,uu,s.Integer(kk)))==0
                assert original(LL,uu,kk+2)==val
    # General compactification identity, independently of the graph chart.
    a,b,c,z=s.symbols('a b c z');q=5*z
    F=a+b*z+c*z*z;B0=a;B1=a+b/10;B2=a+b/5+c/25
    assert s.expand(F-((1-q)**2*B0+2*q*(1-q)*B1+q*q*B2))==0
    print('PROVED (exact_audit.py): padding, variation quadratic and rank-three matrix targets match the original selected-projector definitions at exact fixtures; compactification identity exact.')

if __name__=='__main__':main()
