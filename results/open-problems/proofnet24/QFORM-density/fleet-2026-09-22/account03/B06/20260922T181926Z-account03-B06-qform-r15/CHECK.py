import itertools, math

C0 = 4 + 2*math.sqrt(3)
r0 = 2/math.sqrt(3) - 1

def e2(xs):
    s = sum(xs)
    return (s*s - sum(x*x for x in xs))/2

def params(eps):
    lam = eps/C0
    F = lambda x: 0.0 if x == 0 else x/(lam+x)
    scalar_lb = F(1.0)+F(r0)
    theta0 = 2-eps
    q = 2*(1-eps)
    s = 2-eps
    beta0 = theta0/(2*q)
    bs = beta0*s
    A = (eps/2)**(-1/s)+1
    C = A*(2-eps)/(math.sqrt(2)*eps)*(C0*math.e/(eps*(1-eps)))**0.25
    assert scalar_lb >= theta0
    assert bs > 1
    return lam, scalar_lb, theta0, q, s, bs, C

def finite_grid(eps, denom=8, maxn=4):
    lam = eps/C0
    count = 0
    min_margin = float('inf')
    witness = None
    vals = [k/denom for k in range(denom+1)]
    for n in range(2,maxn+1):
        for xs in itertools.product(vals, repeat=n):
            if e2(xs) + 1e-15 >= 2/3:
                theta = sum(0 if x == 0 else x/(lam+x) for x in xs)
                margin = theta-(2-eps)
                if margin < min_margin:
                    min_margin, witness = margin, xs
                count += 1
    assert min_margin >= -1e-12
    return count, min_margin, witness

print('C0', repr(C0))
print('r0', repr(r0))
for eps in [1/6,1/8,1/16,1/32]:
    print('PARAM', eps, params(eps))
    print('GRID', eps, finite_grid(eps))
print('QFORM_B06_R15_CHECK_PASS')
