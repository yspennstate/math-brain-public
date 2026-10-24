import math


def det3(M):
    return (
        M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    )


def inv2_apply(B, C):
    a,b=B[0]
    c,d=B[1]
    det=a*d-b*c
    return ((d*C[0]-b*C[1])/det, (-c*C[0]+a*C[1])/det)

# Fixed nondegenerate regression point.
a,b,c,d = 0.6, 0.8, -0.8, 0.6
lam,nu = 1.7, 1.3
Delta=a*d-b*c
M=[
    [lam*a*a, nu*c, lam*a*b],
    [nu*c, 0.0, nu*d],
    [lam*a*b, nu*d, lam*b*b],
]
Bc=[[lam*a*a,nu*c],[nu*c,0.0]]
C=[lam*a*b,nu*d]
u=inv2_apply(Bc,C)
schur=lam*b*b-(C[0]*u[0]+C[1]*u[1])
assert abs(det3(M)-(-lam*nu*nu*Delta*Delta)) < 1e-12
assert abs(schur-lam*Delta*Delta/(c*c)) < 1e-12
assert abs(u[0]-d/c) < 1e-12
assert abs(u[1]-lam*a*(b*c-a*d)/(nu*c*c)) < 1e-12

k0=(math.sqrt(3.0)-1.0)/2.0
C_phase=8.0*2.0**0.25*k0**(-0.25)
pbank=(math.sqrt(3.0)-1.0)/32.0
C_bank=8.0*2.0**0.25*pbank**(-0.25)
C0=3.0*2.0**(2.0/3.0)
delta_star=(C0/C_phase)**6

assert C_phase < 12.232
assert C_bank < 24.463
assert 0.00348 < delta_star < 0.00349

# Partner packet: ell=(1,1,-1,-1)/2, v=(1,1,1,1)/2.
ell=[0.5,0.5,-0.5,-0.5]
v=[0.5,0.5,0.5,0.5]
lel=sum(x*x for x in ell)
lvv=sum(x*x for x in v)
lv=sum(x*y for x,y in zip(ell,v))
G=lel*lvv-lv*lv
leverages=[x*x+y*y for x,y in zip(ell,v)]
partner_bound=12.0*(G*1.0)**(-1.0/3.0)
assert abs(lel-1.0)<1e-15 and abs(lvv-1.0)<1e-15 and abs(lv)<1e-15
assert all(abs(q-0.5)<1e-15 for q in leverages)
assert abs(G-1.0)<1e-15
assert abs(partner_bound-12.0)<1e-15

print('det_identity=', det3(M))
print('schur_identity=', schur)
print('k0=', k0)
print('C_phase=', C_phase)
print('pbank=', pbank)
print('C_bank=', C_bank)
print('C0=', C0)
print('delta_star=', delta_star)
print('partner_G=', G)
print('partner_leverages=', leverages)
print('partner_bound=', partner_bound)
print('STATUS=PASS')
