import sympy as sp

# Exact symbolic diagnostic for the two polynomial identities in REPORT.md.
a0,d,b1,b2,c11,c12,c22,q1,q2,g11,g12,g22,nu=sp.symbols(
    "a0 d b1 b2 c11 c12 c22 q1 q2 g11 g12 g22 nu"
)
a=a0+d
b=sp.Matrix([b1,b2])
C=sp.Matrix([[c11,c12],[c12,c22]])
q=sp.Matrix([[q1,q2]])
G2=sp.Matrix([[g11,g12],[g12,g22]])
B=sp.Matrix([[a0,b1,b2],[b1,c11,c12],[b2,c12,c22]])
D=sp.det(B)
K=sp.det(C)
c=C.adjugate()*b
theta=sp.expand(K+(q*c)[0])
W=sp.det(G2)
H=sp.expand(nu*(c.T*G2.adjugate()*c)[0])

S=C-b*b.T/a
uvec=d*b/a
T=S+uvec*q
uperp=sp.Matrix([uvec[1],-uvec[0]])
detNN=sp.expand(sp.det(T)**2*W + nu*(uperp.T*S*G2*S.T*uperp)[0])
identity1=sp.factor(a**2*detNN-(W*(D+d*theta)**2+d**2*H))

qcol=sp.Matrix([q1,q2])
cross=q*G2
G=sp.Matrix([
    [(q*G2*qcol)[0]+nu,cross[0,0],cross[0,1]],
    [cross[0,0],g11,g12],
    [cross[0,1],g12,g22],
])
t=sp.Matrix([K,-c[0],-c[1]])
identity2=sp.factor((t.T*G.adjugate()*t)[0]-(W*theta**2+H))

print("compensated_cross_identity =", identity1)
print("adjugate_split_identity =", identity2)
assert identity1 == 0
assert identity2 == 0
print("QFORM_B06_COMPENSATION_CHECK_PASS")
