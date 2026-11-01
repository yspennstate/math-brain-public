from itertools import permutations
import sympy as sp

# Exact Gaussian-integer vertex check for the 2+2 exposed-face witness.
def gsub(z,w):
    return (z[0]-w[0], z[1]-w[1])

def gmul(z,w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])

x=[(-3,0),(-2,0),(1,-3),(1,-2)]  # x=-a
b=[(-1,0),(0,0),(1,0),(1,1)]
support=[]
off=[]
for p in permutations(range(4)):
    z=(1,0)
    for i,j in enumerate(p):
        z=gmul(z,gsub(b[j],x[i]))
    if set(p[:2])=={0,1}:
        support.append((p,z))
    else:
        off.append((p,z))

print('support =', support)
print('off_imag_unique =', sorted({z[1] for _,z in off}))
print('all_off_imag_negative =', all(z[1] < 0 for _,z in off))
print('support_sum =', (sum(z[0] for _,z in support), sum(z[1] for _,z in support)))

# Exact second variation in every off-block skew-Hermitian tangent.
I=sp.I
A=sp.diag(3,2,-1+3*I,-1+2*I)
B1=sp.Matrix([[-sp.Rational(1,2), sp.Rational(1,2)],
              [ sp.Rational(1,2),-sp.Rational(1,2)]])
B2=sp.Matrix([[1+I/2, I/2],[I/2,1+I/2]])
B0=sp.diag(1,1,1,1)
B0[:2,:2]=B1
B0[2:,2:]=B2
M0=A+B0
D0=sp.factor(M0.det())

u=sp.symbols('u0:8', real=True)
C=sp.Matrix([[u[0]+I*u[1],u[2]+I*u[3]],
             [u[4]+I*u[5],u[6]+I*u[7]]])
Z=sp.zeros(2)
K=sp.Matrix.vstack(sp.Matrix.hstack(Z,C),
                   sp.Matrix.hstack(-C.conjugate().T,Z))
Bp=K*B0-B0*K
Bpp=K*Bp-Bp*K
N=M0.inv()
D2=sp.expand(D0*(sp.trace(N*Bpp)-sp.trace((N*Bp)*(N*Bp))))
q=sp.expand(sp.im(D2))
realvars=[u[0],u[2],u[4],u[6]]
M=sp.hessian(q,realvars)/2
P=-M
minors=[sp.factor(P[:k,:k].det()) for k in range(1,5)]

print('D0 =', D0)
print('Im_D2 =', sp.factor(q))
print('one_copy_matrix =', M.tolist())
print('negative_definite_check_principal_minors_of_minus_M =', minors)
assert D0 == -sp.Rational(119,4)
assert all(z[1] < 0 for _,z in off)
assert minors == [59,4660,263136,19107648]
