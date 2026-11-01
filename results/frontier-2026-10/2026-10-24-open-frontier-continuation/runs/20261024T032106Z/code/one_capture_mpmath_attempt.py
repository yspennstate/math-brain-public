"""Deterministic limit identities, not a finite-width random-network simulation."""
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 60
rho = F(1, 2)
C_exact = ((F(1), F(1)), (F(1), F(3)))
Q_exact = ((F(2), F(3, 2)), (F(3, 2), F(4)))
det = Q_exact[0][0]*Q_exact[1][1]-Q_exact[0][1]**2
ell_coeff = ((Q_exact[1][1]-rho*Q_exact[0][1])/det,
             (-Q_exact[0][1]+rho*Q_exact[0][0])/det)
assert ell_coeff == (F(13, 23), F(-2, 23))
assert ell_coeff[0] + 10*ell_coeff[1] == -F(7, 23)
f_active = Q_exact[0][1] + (Q_exact[1][1]-Q_exact[0][0])*rho-Q_exact[0][1]*rho**2
f_face = C_exact[0][1]+(C_exact[1][1]+1-rho**2-C_exact[0][0])*rho-C_exact[0][1]*rho**2
assert f_active == f_face == F(17, 8)
print('Exact ell coefficients:', tuple(map(str, ell_coeff)))
print('Exact active/face ratio field at rho:', f_active)

C = mp.matrix([[1, 1], [1, 3]])
G = mp.matrix([[1, mp.mpf('.5')], [mp.mpf('.5'), 1]])
Q = C+G
Qs = C+mp.matrix([[0, 0], [0, mp.mpf('.75')]])
Id = mp.eye(2)

def active(t, R):
    E = mp.expm(-t*Q)
    r = E*R
    I = Q**-1*(Id-E)*R
    return r, I, G*I

def bisect(fun, lo, hi):
    assert fun(lo)>0 and fun(hi)<0
    for _ in range(210):
        mid=(lo+hi)/2
        if fun(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

R=mp.matrix([1, 10])
tau=bisect(lambda t: active(t,R)[0][0], mp.mpf(0), mp.mpf(10))
sigma=bisect(lambda t: active(t,R)[2][0], tau, mp.mpf(20))
rs, Is, Bs=active(sigma,R)
assert sigma>tau>0 and -rs[0]/rs[1]>mp.mpf('.5')
max_error=mp.mpf(0)
for dt in [0, .01, .1, 1, 5, 20]:
    dt=mp.mpf(str(dt))
    E=mp.expm(-dt*Qs)
    r=E*rs
    J=Qs**-1*(Id-E)*rs
    I=Is+J
    B=mp.matrix([0, Bs[1]+mp.mpf('.75')*J[1]])
    err=mp.norm(r-(R-C*I-B))
    max_error=max(max_error,err)
    assert r[0]<0<r[1] and -r[0]/r[1]>mp.mpf('.5')
    assert B[1]>0 and err<mp.mpf('1e-50')
print('Strict-capture tau:', mp.nstr(tau, 25))
print('Strict-capture sigma:', mp.nstr(sigma, 25))
print('Inherited B at residual-axis crossing:', [mp.nstr(x,25) for x in active(tau,R)[2]])
print('Ratio at capture:', mp.nstr(-rs[0]/rs[1],25))
print('Maximum post-face Volterra identity error:', mp.nstr(max_error,8))

for name, RR in [('positive-limit',[1,2]), ('zero-limit',[2,13])]:
    RR=mp.matrix(RR)
    ell=(G*Q**-1*RR)[0]
    for t in ['.001','.1','1','5','10','30']:
        B=active(mp.mpf(t),RR)[2]
        assert B[0]>0 and B[1]>0
    print(name, 'ell_b=',mp.nstr(ell,25),'B_b(30)=',mp.nstr(active(mp.mpf(30),RR)[2][0],15))

kappa_plus=(2+mp.sqrt(13))/3
R=mp.matrix([1,kappa_plus])
for t in ['.01','1','10']:
    r,I,B=active(mp.mpf(t),R)
    assert r[0]>0 and r[1]>0 and B[0]>0 and B[1]>0
print('No-axis-exit eigenray checked at three finite times.')
print('PASS: exact identities and 60-digit deterministic-limit checks; no random-network simulation.')
