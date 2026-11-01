import math


def Kbeta(beta):
    return 2*math.exp(beta/2)*(4*math.pi)**beta/(beta*(1-2*beta))


def cbeta(beta):
    # coefficient multiplying D^(beta-1/2) kappa^(-beta) W2^(-beta/2) r^(2 beta)
    return 2*Kbeta(beta)/math.pi


def Mbeta(beta):
    a=2*math.sqrt(2)
    return ((2*beta+1)/(2*beta)
            *a**(2*beta/(2*beta+1))
            *(2*beta*cbeta(beta))**(1/(2*beta+1)))

print('M_1/4=',repr(Mbeta(0.25)))
assert Mbeta(0.25) < 20.814

for beta in (0.25,0.30,0.40,0.45,0.49):
    eD=(beta-0.5)/(2*beta+1)
    ek=-beta/(2*beta+1)
    eW=-beta/(2*(2*beta+1))
    total=2*eD+ek+6*eW
    print('beta',beta,'M',Mbeta(beta),'scale_exponent',total)
    assert abs(total+1) < 1e-12

mx=0.0
arg=None
for j in range(1,100000):
    eps=0.25*j/100000
    beta=0.5-eps
    val=Mbeta(beta)*math.sqrt(eps)
    if val>mx:
        mx=val; arg=beta
print('grid max M_beta*sqrt(epsilon)=',mx,'at beta=',arg)
assert mx < 25

for eps in (0.5,0.1,0.01):
    D=eps**2
    kappa=eps
    Delta=eps**-6
    F=4*eps**-6
    W2=D**2*F
    Rstar=kappa**0.25*W2**0.125/D**0.5
    partner=16*Delta**(-1/8)*(D*kappa)**(-1/4)
    expected_R=4**0.125/eps
    print('eps',eps,'W2',W2,'Rstar',Rstar,'partner',partner)
    assert abs(W2-4*eps**-2) <= 1e-10*max(1,W2)
    assert abs(Rstar-expected_R) <= 1e-12*max(1,Rstar)
    assert abs(partner-16) < 1e-12

print('STATUS=PASS')
