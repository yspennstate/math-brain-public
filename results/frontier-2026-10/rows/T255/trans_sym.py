# exact (sympy) transverse exponent at lam e1 e1^T, attention noise only, leading order in the transverse size s
import sympy as sp
g2,s=sp.symbols('g2 s',positive=True)
def expo(m):
    P=sp.eye(m)-sp.ones(m,m)/m
    L=sp.diag(*([1]+[s]*(m-1))); V=L*L.T
    W=P*V*P; trW=W.trace(); D=sp.Matrix([W[i,i]-trW/m for i in range(m)]); v=sp.Matrix([V[i,i] for i in range(m)])
    VD=V*D; nW2=sum(W[i,j]**2 for i in range(m) for j in range(m))
    b=g2*(V*nW2/m**2+(v*VD.T+VD*v.T)/(2*m)); k=g2/m
    bl=b.trace()-b[0,0]; ba=b[0,0]; ql=0; qa=0
    for i in range(m):
        for j in range(m):
            N=sp.zeros(m,m); N[i,j]=1; X=L*N*L.T*P*V; E=k*(X+X.T)
            ql+=(E.trace()-E[0,0])**2; qa+=E[0,0]**2
    l=(m-1)*s**2; a=1
    d=bl/l-ba/a-ql/(2*l**2)+qa/(2*a**2)
    return sp.simplify(sp.limit(sp.simplify(d/nW2),s,0))
for m in range(3,9):
    e=sp.factor(expo(m)); guess=sp.factor(2*g2/m**2*(g2-sp.Rational(m*(m-2),2*(m-1))))
    print(m,e,"| matches 2g2/m^2 (g2 - m(m-2)/(2(m-1))):",sp.simplify(e-guess)==0,flush=True)
