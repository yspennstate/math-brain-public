from mpmath import mp

mp.dps = 80
ALPHAS = [mp.mpf('3.52'), mp.mpf('3.6'), mp.mpf('4.0'), mp.mpf('4.39539'), mp.mpf('4.4898')]


def q_majority(alpha):
    mu = mp.mpf(3)*alpha/2
    x = 2*mu
    return (1-mp.e**(-x)*(mp.besseli(0,x)+mp.besseli(1,x)))/2


def safe_batch(alpha, K=80):
    mu = mp.mpf(3)*alpha/2
    q = q_majority(alpha)
    pmf = [mp.e**(-mu)]
    for k in range(K):
        pmf.append(pmf[-1]*mu/(k+1))
    p_use = mp.mpf('0')
    ED_use = mp.mpf('0')
    for p in range(K+1):
        for n in range(K+1):
            pr = pmf[p]*pmf[n]
            z = min(p,n)
            m = max(p,n)
            D = z+m
            useful = (1-q*q)**m * (1-(1-q*q)**z)
            p_use += pr*useful
            ED_use += pr*D*useful
    meanD = ED_use/p_use
    c_safe = p_use/(1+2*meanD)
    unsat = alpha*q**3
    return q,p_use,meanD,c_safe,unsat,c_safe/unsat


print('T04 conflict-free useful zero-break batch diagnostic')
print('mp.dps =', mp.dps)
for alpha in ALPHAS:
    q,p,md,c,u,frac = safe_batch(alpha)
    print()
    print('alpha =', mp.nstr(alpha,20))
    print('q =', mp.nstr(q,30))
    print('useful zero-break variable density p_use =', mp.nstr(p,30))
    print('mean total degree among useful candidates =', mp.nstr(md,30))
    print('Caro-Wei safe-batch density lower diagnostic c_safe =', mp.nstr(c,30))
    print('initial unsatisfied-clause density per variable alpha*q^3 =', mp.nstr(u,30))
    print('c_safe/(alpha*q^3) =', mp.nstr(frac,30))
