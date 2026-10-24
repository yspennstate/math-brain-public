import mpmath as mp
mp.mp.dps = 50

def H(k,q):
    q=mp.mpf(q)
    return (mp.sqrt(mp.e)/(mp.mpf(k)*2**(mp.mpf(3)/4)*q**(mp.mpf(1)/4))
            * mp.beta(mp.mpf(1)/(4*k), mp.mpf(1)/(4*q)-mp.mpf(1)/(4*k)))

def partner_case(mu,tau,q):
    mu,tau,q=map(mp.mpf,(mu,tau,q))
    lev=2*mu/(1-tau)
    generic=H(2,q)*mp.sqrt(2)*(1-tau*tau)**(-mp.mpf(1)/4)
    exact_heavy=generic*mp.sqrt(2)
    return lev,generic,exact_heavy

for name,k,q in [('k2q1',2,1),('k2q1.6',2,mp.mpf(8)/5),
                 ('k2q1.801',2,mp.mpf(1801)/1000),('k3q2',3,2)]:
    print(name, mp.nstr(H(k,q),30))

for name,mu,tau,q in [
    ('mu<1/8',mp.mpf(1)/8,mp.mpf(1)/2,1),
    ('mu<=1/6',mp.mpf(1)/6,mp.mpf(58)/100,mp.mpf(8)/5),
    ('mu<=0.18',mp.mpf(18)/100,mp.mpf(6001)/10000,mp.mpf(1801)/1000),
]:
    lev,generic,exact_heavy=partner_case(mu,tau,q)
    print(name)
    print('sqrt2mu', mp.nstr(mp.sqrt(2*mu),20), 'tau', mp.nstr(tau,20))
    print('lev', mp.nstr(lev,20), 'q/2', mp.nstr(q/2,20))
    print('generic', mp.nstr(generic,30), 'exact_heavy', mp.nstr(exact_heavy,30))
