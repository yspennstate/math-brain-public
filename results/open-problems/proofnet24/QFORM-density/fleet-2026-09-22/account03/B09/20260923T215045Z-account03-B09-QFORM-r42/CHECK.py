import math


def K_p(p):
    return (4*math.pi)**(1/p) * 2**(0.5-1/(2*p)) * math.sqrt(p/(p-2))


def H_p(p):
    return math.pi*math.sqrt(2)*K_p(p)*(2*(p-1))**((p-1)/p)


def C_p(p):
    return (p+1)/math.pi*(H_p(p)/(2*p))**(p/(p+1))


def bound(eps,p):
    Delta=eps
    a=1/eps
    return C_p(p)*Delta**(-p/(2*(p+1)))*a**(-1/(p+1))


c4=C_p(4.0)
c4_old=5*6**(3/5)/2**(9/10)
print('C4',repr(c4))
print('C4_old',repr(c4_old))
print('C4_ratio',repr(c4/c4_old))
assert abs(c4/c4_old-1)<1e-12

for e in [1e-1,1e-2,1e-3,1e-4,1e-5]:
    p=2+e
    print('endpoint',e,'Cp',C_p(p),'Cp*eps^(1/3)',C_p(p)*e**(1/3))
print('3sqrt2',3*math.sqrt(2))
print('asymptotic_log_coefficient',3*math.sqrt(2)*(math.e/6)**(1/3))

coarse=4*2**(17/16)*math.pi**(1/8)*math.exp(1/(18*math.e))
print('coarse_Cp_eps13',coarse)
print('coarse_log_coefficient',coarse*(math.e/6)**(1/3))
assert coarse < 9.839
assert coarse*(math.e/6)**(1/3) < 7.557

for eps in [1e-2,1e-4,1e-6,1e-12]:
    R=eps**(-3)
    p=2+min(1,6/math.log(R))
    print('stress',eps,'R',R,'p',p,'adaptive',bound(eps,p),'p4',bound(eps,4))
    assert bound(eps,p) < bound(eps,4)

for eps in [0.5,0.1,1e-3]:
    star=math.sqrt(1+eps**-2)
    lp=(1+math.sqrt(1+4*eps*eps))/2
    lm=(1-math.sqrt(1+4*eps*eps))/2
    spectrum=[-star,lm,0.0,lp,star]
    large=sum(abs(x)>=1-1e-12 for x in spectrum)
    print('spectrum',eps,spectrum,'large',large)
    assert large>=3
    Delta=eps
    a=1/eps
    V=Delta**2*a**2
    R=a*a/Delta
    assert abs(V-1)<1e-12
    assert abs(R-eps**-3)/R<1e-12

partner=3*2**(-1/3)
print('partner_bound',partner)
assert partner < 2.382
print('PASS')
