from mpmath import mp

mp.dps = 60


def sinc(x):
    return mp.one if x == 0 else mp.sin(x) / x


def Ck(k):
    f = lambda t: mp.e**(-t*t/2) * sinc(mp.sqrt(3)*t/mp.sqrt(k))**k
    # Gaussian factor makes this absolutely integrable; split at moderate points.
    val = mp.quad(f, [-mp.inf, -12, -6, 0, 6, 12, mp.inf])
    return 6 * val / mp.sqrt(2*mp.pi)


C1_exact = mp.sqrt(6*mp.pi) * mp.erf(mp.sqrt(mp.mpf(3)/2))
C2_exact = 2*mp.sqrt(3*mp.pi)*mp.erf(mp.sqrt(3)) - 2 + 2*mp.e**(-3)
barrier = 3*mp.sqrt(2)

v1 = Ck(1)
v2 = Ck(2)
assert abs(v1-C1_exact) < mp.mpf('1e-35')
assert abs(v2-C2_exact) < mp.mpf('1e-35')

print('PASS exact k=1 formula')
print(mp.nstr(v1, 30))
print('PASS exact k=2 partner formula')
print(mp.nstr(v2, 30))
print('barrier', mp.nstr(barrier, 30))

for k in [1,2,3,4,5,10,20,50,100]:
    v = Ck(k)
    print(k, mp.nstr(v, 30), 'gap=', mp.nstr(barrier-v, 20))

# Check the two-term asymptotic numerically at increasing k.
for k in [20, 50, 100, 200]:
    v = Ck(k)
    approx = barrier * (1-mp.mpf(3)/(80*k)-mp.mpf(173)/(17920*k*k))
    scaled = (v-approx) * k**3
    print('asymptotic', k, 'k^3 residual=', mp.nstr(scaled, 20))

# Exact equimeasurability identity behind the negative-output shell rearrangement.
# For K(z)=1/2 exp(-(a^2 z^2-r^2)/2) 1_{|z|>=r/a},
# a superlevel shell [z0,z0+d] U [-z0-d,-z0] has measure 2d,
# and the rearranged value at |u|=d is 1/2 exp(-a*r*d-a^2*d^2/2).
for a in [mp.mpf('0.7'), mp.mpf('1.3'), mp.mpf('2.2')]:
    for r in [mp.mpf('0.2'), mp.mpf('1.1')]:
        for d in [mp.mpf('0.1'), mp.mpf('0.6'), mp.mpf('1.4')]:
            z0 = r/a
            shell_value = mp.mpf('0.5')*mp.e**(-(a*a*(z0+d)**2-r*r)/2)
            rearranged = mp.mpf('0.5')*mp.e**(-a*r*d-a*a*d*d/2)
            assert abs(shell_value-rearranged) < mp.mpf('1e-45')
print('PASS shell rearrangement identity')
