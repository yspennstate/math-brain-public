import sympy as s

# Exact self-check for the new P11 adjugate-feature identity.
# All variables are algebraically independent reals; Hermitian off-diagonals
# are represented by x+I y and their conjugates.
I=s.I
c1,c2,c3,tau=s.symbols('c1 c2 c3 tau', real=True)
a1,a2,a3=s.symbols('a1 a2 a3', real=True)
x12,y12,x13,y13,x23,y23=s.symbols('x12 y12 x13 y13 x23 y23', real=True)
z12=x12+I*y12; z13=x13+I*y13; z23=x23+I*y23
K=s.Matrix([[a1,z12,z13],[s.conjugate(z12),a2,z23],[s.conjugate(z13),s.conjugate(z23),a3]])
D=s.diag(c1,c2,c3)
M=D+tau*K

def pair_grad(i,j):
    G=s.zeros(3)
    G[i,i]=K[j,j]
    G[j,j]=K[i,i]
    G[i,j]=-K[i,j]
    G[j,i]=-K[j,i]
    return G

G23=pair_grad(1,2)
G13=pair_grad(0,2)
G12=pair_grad(0,1)
R=s.diag(c2*c3,c1*c3,c1*c2) + tau*(c1*G23+c2*G13+c3*G12) + tau**2*K.adjugate()
assert all(s.simplify(M.adjugate()[i,j]-R[i,j])==0 for i in range(3) for j in range(3))

# Exact determinant polynomial behind the identity.
det_formula=(c1*c2*c3
             +tau*(c2*c3*a1+c1*c3*a2+c1*c2*a3)
             +tau**2*(c1*K.extract([1,2],[1,2]).det()
                      +c2*K.extract([0,2],[0,2]).det()
                      +c3*K.extract([0,1],[0,1]).det())
             +tau**3*K.det())
assert s.simplify(M.det()-det_formula)==0

print('PASS')
print('claim=P11-LYONS-ADJUGATE-FEATURE-01')
print('checked=adj(D+tau*K) expansion and det(D+tau*K) expansion for generic Hermitian 3x3 K')
