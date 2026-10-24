from fractions import Fraction as F


def K(D):
    return F(2*D*D*(D-1), (D+1)**2*(2*D+1)**2)


def P12(x):
    return 11*x**3 - 153*x**2 + 312*x - 144


def P12p(x):
    return 33*x**2 - 306*x + 312


def cert(D,L,p0):
    h=D-1
    k=K(D)
    t=(1+L)/(D+L)
    Theta=p0*t/(1-p0+p0*t)
    A=L/(1-L)
    Bmin=A-p0*k
    C=Bmin*(1-2*Theta)-1
    monotone=C*t-k/F(4)
    delta=1+h*Theta-h*Bmin*Theta*(1-Theta)
    denom=1+h*Theta+L
    margin=2*delta/(denom*denom)
    static_slack=D*(1-L)-(1+L)
    return dict(K=k,t=t,Theta=Theta,A=A,Bmin=Bmin,C=C,monotone=monotone,
                delta=delta,margin=margin,static_slack=static_slack)


def show(name,D,L,p0,clean_den=None):
    c=cert(D,L,p0)
    print(name)
    print(' D,L,p0 =',D,L,p0)
    for key in ['K','t','Theta','static_slack','C','monotone','delta','margin']:
        print(' ',key,'=',c[key], '~', float(c[key]))
    assert c['static_slack'] >= 0
    assert c['C'] > 0
    assert c['monotone'] > 0
    assert c['delta'] > 0
    assert c['margin'] > 0
    if clean_den:
        clean=F(1,clean_den)
        print(' margin - 1/%d ='%clean_den, c['margin']-clean)
        assert c['margin'] > clean
    print()
    return c


L12=F(670001,1000000)
assert P12p(L12)>0
assert P12(L12)<0
print('P12(L12)=',P12(L12))
print("P12'(L12)=",P12p(L12))
print()

assert P12p(F(2,3))>0
assert P12(F(2,3))<0
print('P12(2/3)=',P12(F(2,3)))
print("P12'(2/3)=",P12p(F(2,3)))
print()

show('HEADLINE {1,12}, p<=1/2',12,L12,F(1,2),1100000)
show('BREADTH {1,48}, p<=2/5',48,F(2,3),F(2,5),2300)
show('BREADTH {1,230}, p<=19/50',230,F(2,3),F(19,50),55000)

f12_fail=cert(12,F(67001,100000),F(1,2))['delta']
f49_fail=cert(49,F(2,3),F(2,5))['delta']
f231_fail=cert(231,F(2,3),F(19,50))['delta']
print('METHOD_BOUNDARY delta D=12,L=0.67001 =',f12_fail,'~',float(f12_fail))
print('METHOD_BOUNDARY delta D=49,L=2/3,p0=2/5 =',f49_fail,'~',float(f49_fail))
print('METHOD_BOUNDARY delta D=231,L=2/3,p0=19/50 =',f231_fail,'~',float(f231_fail))
assert f12_fail < 0
assert f49_fail < 0
assert f231_fail < 0

print('ALL_EXACT_CHECKS_PASS')
