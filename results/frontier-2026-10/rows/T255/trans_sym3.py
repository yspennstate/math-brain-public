# joint regularity at the corner: L = [[1,0,0],[w1, s t1, 0],[w2, s t2, s t3]]; Phi_S = tr(Schur)/V11 = s^2 |T|^2.
# limit s->0 of drift(log Phi_S)/|W|^2 as a function of w; check it is a rational function regular at w=0 equal to mu_perp there.
import sympy as sp
g2,s=sp.symbols('g2 s',positive=True); w1,w2,t1,t2,t3=sp.symbols('w1 w2 t1 t2 t3',real=True)
m=3; P=sp.eye(m)-sp.ones(m,m)/m
L=sp.Matrix([[1,0,0],[w1,s*t1,0],[w2,s*t2,s*t3]]); V=L*L.T
W=P*V*P; trW=W.trace(); D=sp.Matrix([W[i,i]-trW/m for i in range(m)]); v=sp.Matrix([V[i,i] for i in range(m)])
nW2=sum(W[i,j]**2 for i in range(m) for j in range(m))
b=g2*(V*nW2/m**2+(v*(V*D).T+(V*D)*v.T)/(2*m)); k=g2/m
def phiS(V): return (V[1,1]+V[2,2])-(V[1,0]**2+V[2,0]**2)/V[0,0]   # tr of Schur complement (V11 here = V[0,0])
# first and second derivatives of F(V)=log(phiS(V)/V00) wrt the 6 entries via sympy on a symbolic symmetric matrix
X=sp.Matrix(3,3,lambda i,j: sp.Symbol('x%d%d'%(min(i,j),max(i,j))))
F=sp.log(phiS(X)/X[0,0]); xs=sorted(F.free_symbols,key=str)
grad={x:sp.diff(F,x) for x in xs}
sub={sp.Symbol('x%d%d'%(i,j)):V[i,j] for i in range(3) for j in range(i,3)}
def dmat(Mt):  # directional derivative coefficients: dF = sum_x grad_x * dX_x, with x_ij symmetric entry
    return sum(grad.get(sp.Symbol('x%d%d'%(i,j)),0)*Mt[i,j] for i in range(3) for j in range(i,3))
drift=dmat(b); ito=0
for i in range(m):
    for j in range(m):
        N=sp.zeros(m,m); N[i,j]=1; Xn=L*N*L.T*P*V; E=k*(Xn+Xn.T)
        lin=dmat(E)
        # second-order term: sum_xy d2F/dxdy E_x E_y
        q=sum(sp.diff(F,x,y)*E[int(str(x)[1]),int(str(x)[2])]*E[int(str(y)[1]),int(str(y)[2])] for x in xs for y in xs)
        ito+=q
d=(drift+ito/2).subs(sub)
expr=sp.together(d/nW2)
lim=sp.limit(expr.subs({t1:1,t2:sp.Rational(1,3),t3:sp.Rational(1,2)}),s,0)
lim=sp.simplify(lim)
print("limit at s->0 (T fixed):",lim)
print("at w=0:",sp.factor(lim.subs({w1:0,w2:0})))
print("denominator vanishes at w=0?",sp.denom(sp.together(lim)).subs({w1:0,w2:0}))
