import sympy as sp

d,e,k,a,b,H,s,h,u=sp.symbols('d e k a b H s h u')
L2=4*d*e-3*k
L1=2*a*e+2*b*d-k*(s-6*h)
C0=a*b-H*k

aT=a+2*d
bT=b+2*e
HT=H+s+2
sT=s+6
L2T=4*d*e-3*k
L1T=2*aT*e+2*bT*d-k*(sT-6*h)
C0T=aT*bT-HT*k
assert sp.expand(L2T-L2)==0
assert sp.expand(L1T-(L1+2*L2))==0
assert sp.expand(C0T-(C0+L1+L2+k*(1-6*h)))==0
lo=sp.Rational(43,360); hi=sp.Rational(1,8)
assert 1-6*hi==sp.Rational(1,4)
assert 1-6*lo>0
print('TRIANGLE_SEED_LIFT_IDENTITIES_PASS')
print('L2_TRI = L2')
print('L1_TRI = L1 + 2*L2')
print('C0_TRI = C0 + L1 + L2 + k*(1-6*h)')
print('STRIP',lo,hi,'MIN_EXTRA_K_FACTOR',1-6*hi)
print('ALL_EXACT_CHECKS_PASS')
