import sympy as sp


def cof(M):
    return sp.Matrix([[M[1,1], -M[1,0]], [-M[0,1], M[0,0]]])


def delta(A,B):
    return sp.Rational(1,2)*((A+B).det()-A.det()-B.det())


def frob(A,B):
    return sum(A[i,j]*B[i,j] for i in range(2) for j in range(2))


def Phi(A,B,K,X):
    return K*delta(A,B)+sp.Rational(1,4)*X*frob(A,B)


def f(B,K,X):
    return K*B.det()+sp.Rational(1,4)*X*frob(B,B)


def setblk(M,i,j,B):
    M[2*i:2*i+2,2*j:2*j+2]=B


A=sp.Matrix([[1,2],[3,5]])
G=sp.Matrix([[2,-1],[4,3]])
H=sp.Matrix([[-2,1],[1,4]])
Z=sp.Matrix([[1,3],[-2,2]])
Y=sp.Matrix([[2,-1],[5,1]])
Ka,Kg,Kh=sp.Rational(3,2),sp.Rational(-2,3),sp.Rational(5,4)
Xa,Xg,Xh=sp.Rational(7,3),sp.Rational(-4,5),sp.Rational(2,7)

stack=A.col_join(G).col_join(H)
L1=sp.zeros(6); L2=sp.zeros(6)
setblk(L1,0,1,Z); setblk(L1,1,0,-Z.T)
setblk(L2,0,2,Y); setblk(L2,2,0,-Y.T)
t,s=sp.symbols('t s')
X=t*L1+s*L2
E3=sp.eye(6)+X+sp.Rational(1,2)*X**2+sp.Rational(1,6)*X**3
rows=sp.expand(E3*stack)
At,Gt,Ht=rows[0:2,:],rows[2:4,:],rows[4:6,:]
expr=sp.expand(f(At,Ka,Xa)+f(Gt,Kg,Xg)+f(Ht,Kh,Xh))

h_direct=sp.expand(expr).coeff(t,1).coeff(s,1)
h_formula=2*Phi(Z*G,Y*H,Ka,Xa)-Phi(G,Z.T*Y*H,Kg,Xg)-Phi(H,Y.T*Z*G,Kh,Xh)

chi=2*Xa-Xg-Xh
P=Ka*cof(G)*H.T
Q=-sp.Rational(1,2)*Kg*cof(G)*H.T-sp.Rational(1,2)*Kh*G*cof(H).T+sp.Rational(1,4)*chi*G*H.T
Cmat=cof(Z)*P+Z*Q
h_matrix=frob(Y,Cmat)

beta_direct=2*sp.expand(expr).coeff(t,2).coeff(s,1)
S=Z*Z.T
beta_formula=2*(sp.Rational(1,3)*(-Phi(A,S*Y*H,Ka,Xa)+Phi(H,Y.T*S*A,Kh,Xh))
                -Phi(Y*H,S*A,Ka,Xa)+Phi(Z.T*A,Z.T*Y*H,Kg,Xg))
nu=3*Xg+Xh-4*Xa
Bmat=(-sp.Rational(1,3)*Ka*S*cof(A)*H.T
      +sp.Rational(1,3)*Kh*S*A*cof(H).T
      -Ka*cof(S*A)*H.T
      +Kg*Z.det()*cof(A)*H.T
      +sp.Rational(1,6)*nu*S*A*H.T)
beta_matrix=frob(Y,Bmat)

assert sp.simplify(h_direct-h_formula)==0
assert sp.simplify(h_direct-h_matrix)==0
assert sp.simplify(beta_direct-beta_formula)==0
assert sp.simplify(beta_direct-beta_matrix)==0

# Synthetic exact kernel-normalization check for the algebraic consequences.
Zk=sp.Matrix([[3,0],[0,1]])
Tk=sp.Rational(5,2); Ck=sp.Rational(3,2)
Qk=sp.Matrix([[2,1],[1,3]])
Sk=Zk.T*Zk
dk=Zk.det()
Pk=-(Sk*Qk)/dk
assert dk==2*Ck
assert frob(Zk,Zk)==4*Tk
assert cof(Zk)*Pk+Zk*Qk==sp.zeros(2)
assert Pk.det()==Qk.det()
assert Pk*Qk.adjugate()==(Pk*Qk.adjugate()).T
assert 2*Tk*Qk.det()+Ck*sp.trace(Pk*Qk.adjugate())==0
assert sp.trace(Pk*Qk.inv())==-2*Tk/Ck
assert (Pk*Qk.inv()).det()==1

print('PASS')
print('mixed_second =', h_direct)
print('mixed_cubic  =', beta_direct)
print('cross_hessian_matrix =', Cmat.tolist())
print('cross_cubic_matrix   =', Bmat.tolist())
print('synthetic detP=detQ =', Pk.det())
print('synthetic trace(P Q^-1) =', sp.trace(Pk*Qk.inv()))
print('synthetic -C P Q^-1 =', (-Ck*Pk*Qk.inv()).tolist())
