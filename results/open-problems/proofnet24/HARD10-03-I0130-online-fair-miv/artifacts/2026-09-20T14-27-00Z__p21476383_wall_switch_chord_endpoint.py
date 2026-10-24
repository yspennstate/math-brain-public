from fractions import Fraction as F
from decimal import Decimal, getcontext

Q=4870886400
S=202391574968484000000000
P0=21476383
V0={7015:57719977623155054880651571200000000000,812:151086287291137698427224853680000000000,4483:89757393707928277928706048000000000000,2824:115550511421873896362731622400000000000}
V1={7015:57719977421087306432117145600000000000,812:151086286762215470511301347840000000000,4483:89757393086181359625523200000000000000,2824:115550510940020034677764915200000000000}
D={j:V1[j]-V0[j] for j in V0}
def chord(j,t): return F(V0[j])+t*D[j]
def data(t):
    P=F(P0)+t
    FH=chord(4483,t); FL=chord(2824,t); FHr=chord(7015,t); B0=chord(812,t)
    J=812; K=3671
    d=(FL-FH-40*Q*J*S)/(8*S*8640*Q)
    b1=(F(K)-1728*d)/3840; a1=b1+d
    u1=1728*a1+2112*b1; v1=2112*a1+1728*b1
    Hi=FH+8*S*(8640*Q*a1-9600*P*b1)
    Li=FL+8*S*(8640*Q*b1-9600*P*b1)-40*Q*J*S
    assert Hi==Li
    a0=(Hi-FHr)/(8*S*19200*Q)
    b0=(F(3028)-2112*a0)/1728
    u0=1728*a0+2112*b0; v0=2112*a0+1728*b0
    H0=FHr+8*S*(8640*Q*a0-9600*P*b0)
    L0=Hi+8*S*(-10560*Q*a0-9600*P*b0)
    assert H0==L0
    T=8*S*(12480*Q+28800*P)
    return a1,b1,u1,v1,Hi-B0,a0,b0,u0,v0,H0-T
def q(t):
    return 121*t**3-F(2579349451371)*t**2-F(28627069331302871763093)*t+F(16928614787078554696327)
C=F(54772144609375,3678534)
for x in (F(0),F(1)): assert data(x)[-1] == C*q(x)
assert q(0)>0 and q(1)<0
# q'(t)=363t^2-5158698902742t-28627069331302871763093 is strictly negative on [0,1].
assert F(363)-F(28627069331302871763093)<0
lo=F(591349906,10**9); hi=F(591349907,10**9)
assert q(lo)>0 and q(hi)<0
for x in (F(0),F(1)):
    a1,b1,u1,v1,ig,a0,b0,u0,v0,g=data(x)
    assert 0<a1<b1<1 and u1==3671 and F(3635)<v1<F(3636) and ig>0
    assert 0<a0<b0<1 and F(3174)<u0<F(3175) and v0==3028
assert data(lo)[-1]>0
Uexp=F(9,10)-(F(P0)+lo)/Q
Wexp=Uexp-F(19,30)
Uinherit=F(2155622931638898223608000,2406925605048556309219721)
assert Uexp<Uinherit
print('I0130_P21476383_WALL_SWITCH_CHORD_PASS')
print('q(t)=121*t^3-2579349451371*t^2-28627069331302871763093*t+16928614787078554696327')
print('tau_bracket=591349906/1000000000,591349907/1000000000')
print(f'explicit_t={lo.numerator}/{lo.denominator}')
print(f'U_explicit={Uexp.numerator}/{Uexp.denominator}')
print(f'W_explicit={Wexp.numerator}/{Wexp.denominator}')
print(f'exact_improvement={(Uinherit-Uexp).numerator}/{(Uinherit-Uexp).denominator}')
getcontext().prec=50
print('U_explicit_decimal=',Decimal(Uexp.numerator)/Decimal(Uexp.denominator))
print('improvement_decimal=',Decimal((Uinherit-Uexp).numerator)/Decimal((Uinherit-Uexp).denominator))
