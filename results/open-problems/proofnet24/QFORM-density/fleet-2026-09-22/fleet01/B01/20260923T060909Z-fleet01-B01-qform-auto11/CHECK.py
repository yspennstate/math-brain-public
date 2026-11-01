import math
import sympy as sp

# Exact compound-Schur / adjugate identities.
a,b=sp.symbols('a b', nonzero=True, real=True)
c=b**2/a
uk,ul,vk,vl=sp.symbols('uk ul vk vl', real=True)
adj=sp.Matrix([[c,-b],[-b,a]])
mk=sp.Matrix([uk,vk]); ml=sp.Matrix([ul,vl])
zk=vk-b*uk/a; zl=vl-b*ul/a
assert sp.simplify((mk.T*adj*ml)[0]-a*zk*zl)==0

aa,bb,cc,p,q,r,s,dd=sp.symbols('aa bb cc p q r s dd')
M3=sp.Matrix([[aa,bb,p],[bb,cc,q],[r,s,dd]])
B=sp.Matrix([[aa,bb],[bb,cc]])
adjB=sp.Matrix([[cc,-bb],[-bb,aa]])
rhs=B.det()*dd-(sp.Matrix([[r,s]])*adjB*sp.Matrix([p,q]))[0]
assert sp.simplify(M3.det()-rhs)==0

C_hub=2**(11/4)
print('C_hub=',repr(C_hub))

# Stress family: U,V of size m, W of size N=m^3,
# A=uu^T + L(vw^T+wv^T), L=m^(3/2).
for m in [2,3,4,10]:
    N=m**3
    L=m**1.5
    a0=1/m
    zentry=L/(math.sqrt(m)*math.sqrt(N))
    znorm=math.sqrt(N*zentry*zentry)
    W2=N*(N-1)*(a0*zentry*zentry)**2
    direct=C_hub*(a0**-0.5)*(znorm**-0.5)
    aggregate=8*((1/m)**-0.25)*(W2**-0.125)
    assert abs(znorm-m)<1e-10
    assert abs(W2-(m*m-1/m))<1e-10
    assert abs(direct-C_hub)<1e-10
    print('m=',m,'zentry=',zentry,'znorm=',znorm,'W2=',W2,
          'direct=',direct,'aggregate=',aggregate,'F_residual_lower=',2*znorm**2)
print('STATUS=PASS')
