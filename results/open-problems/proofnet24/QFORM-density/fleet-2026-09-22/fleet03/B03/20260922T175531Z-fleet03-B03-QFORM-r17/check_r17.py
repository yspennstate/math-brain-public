import mpmath as mp

mp.mp.dps = 50


def Cagg(q, k):
    cq = 2*q/(mp.pi**2*mp.e**2)
    return (mp.sqrt(2/mp.pi)/(2*k)
            * mp.beta(mp.mpf(1)/(4*k), mp.mpf(1)/(4*q)-mp.mpf(1)/(4*k))
            * cq**(-mp.mpf(1)/4))


def Cprod(q, k):
    cq = 2*q/(mp.pi**2*mp.e**2)
    return (mp.sqrt(2/mp.pi)/2
            * mp.beta(mp.mpf(1)/4, mp.mpf(k)/(4*q)-mp.mpf(1)/4)
            * cq**(-mp.mpf(1)/4))


c12 = Cagg(1, 2)
c23 = Cagg(2, 3)
c2 = Cprod(1, 2)
cfam = c2*mp.sqrt(5/mp.sqrt(6))
Mconst = (mp.e*mp.sqrt(mp.pi)/(2*mp.sqrt(2))
          * mp.gamma(mp.mpf(1)/4)/mp.gamma(mp.mpf(3)/4))
cpeer = 2*mp.sqrt(Mconst)

assert abs(c12-mp.mpf('7.6737592903848577688991119917144518495794410900789')) < mp.mpf('1e-45')
assert abs(c23-mp.mpf('9.8406558649220185412255965812125468864414392294824')) < mp.mpf('1e-45')
assert abs(c2-mp.mpf('7.270461147134126112917892103140629650075565080081')) < mp.mpf('1e-45')

minsigma2 = mp.mpf(1)
min_e2 = mp.mpf(1)
for m in range(4, 201):
    p = m//2
    sigma2 = mp.mpf(p*(m-p))/(m*m)
    leverage = mp.mpf(1)/p
    e2 = sigma2**2
    assert sigma2 >= mp.mpf(6)/25
    assert leverage <= mp.mpf(1)/2
    assert e2 >= mp.mpf(36)/625
    minsigma2 = min(minsigma2, sigma2)
    min_e2 = min(min_e2, e2)

vals = []
for j in [2, 4, 8, 12, 16]:
    delta = mp.e**(-j)
    assert delta**2 < mp.mpf(1)/8
    lower = mp.sqrt(2)*mp.log(1/delta)+(2-mp.log(8))/mp.sqrt(2)
    integrated = (mp.log(1/(8*delta**2))+2)/mp.sqrt(2)
    assert abs(lower-integrated) < mp.mpf('1e-40')
    vals.append((j, lower))
assert all(vals[i+1][1] > vals[i][1] for i in range(len(vals)-1))

print('QFORM_B03_R17_CHECK_PASS')
print('C_agg(q=1,k=2) =', mp.nstr(c12, 18))
print('C_prod(q=1,k=2) =', mp.nstr(c2, 18))
print('C_agg(q=2,k=3) =', mp.nstr(c23, 18))
print('A_m uniform family constant <=', mp.nstr(cfam, 18))
print('peer B18 overlap constant =', mp.nstr(cpeer, 18))
print('min sigma^2 m=4..200 =', mp.nstr(minsigma2, 18))
print('min E2 m=4..200 =', mp.nstr(min_e2, 18))
for j, lower in vals:
    print(f'delta=e^-{j}: conditional lower bound =', mp.nstr(lower, 18))
