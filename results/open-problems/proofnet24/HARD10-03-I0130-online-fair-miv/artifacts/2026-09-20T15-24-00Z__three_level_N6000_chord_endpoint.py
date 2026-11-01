from fractions import Fraction as F
from decimal import Decimal, getcontext

Q=4870886400
S=202391574968484000000000
P0=21476383
N=6000
V0={
7015:57719977623155054880651571200000000000,
4483:89757393707928277928706048000000000000,
6141:67864014914209824195763200000000000000,
382:159557404200594447305155247280000000000,
}
VN={
7015:57718589902403197490037964800000000000,
4483:89753663226418458831618048000000000000,
6141:67855807854888222182169600000000000000,
382:159531099558230723173198624080000000000,
}
D={j:VN[j]-V0[j] for j in V0}
def chord(j,t): return F(V0[j])+t*D[j]

def data(t):
    P=F(P0)+N*t
    J2=2824
    FH2=chord(6141,t); FL2=chord(382,t)
    d2=(FL2-FH2-40*Q*J2*S)/(8*S*8640*Q)
    b2=(F(3206)-2112*d2)/3840
    a2=b2+d2
    u2=1728*a2+2112*b2
    v2=2112*a2+1728*b2
    H2=FH2+8*S*(8640*Q*a2-9600*P*b2)
    L2=FL2+8*S*(8640*Q*b2-9600*P*b2)-40*Q*J2*S
    assert H2==L2

    J1=812
    FH1=chord(4483,t)
    d1=(H2-FH1-40*Q*J1*S)/(8*S*8640*Q)
    b1=(F(3671)-1728*d1)/3840
    a1=b1+d1
    u1=1728*a1+2112*b1
    v1=2112*a1+1728*b1
    H1=FH1+8*S*(8640*Q*a1-9600*P*b1)
    L1=H2+8*S*(8640*Q*b1-9600*P*b1)-40*Q*J1*S
    assert H1==L1

    FHr=chord(7015,t)
    a0=(H1-FHr)/(8*S*19200*Q)
    b0=(F(3028)-2112*a0)/1728
    u0=1728*a0+2112*b0
    v0=2112*a0+1728*b0
    H0=FHr+8*S*(8640*Q*a0-9600*P*b0)
    L0=H1+8*S*(-10560*Q*a0-9600*P*b0)
    assert H0==L0
    T=8*S*(12480*Q+28800*P)
    return a2,b2,u2,v2,a1,b1,u1,v1,a0,b0,u0,v0,H0-T

lo=F(924066078,10**9)
hi=F(924066079,10**9)
z=data(lo)
zh=data(hi)
assert z[-1]>0 and zh[-1]<0

a2,b2,u2,v2,a1,b1,u1,v1,a0,b0,u0,v0,g=z
assert 0<a2<b2<1 and F(3316)<u2<F(3317) and v2==3206
assert 0<a1<b1<1 and u1==3671 and F(3635)<v1<F(3636)
assert 0<a0<b0<1 and F(3174)<u0<F(3175) and v0==3028

U=F(9,10)-(F(P0)+N*lo)/Q
W=U-F(19,30)
Uprev=F(2181160688204325047,2435443200000000000)
assert U<Uprev
print('I0130_THREE_LEVEL_N6000_CHORD_PASS')
print(f't_bracket={lo.numerator}/{lo.denominator},{hi.numerator}/{hi.denominator}')
print(f'P_effective={(F(P0)+N*lo).numerator}/{(F(P0)+N*lo).denominator}')
print(f'U_explicit={U.numerator}/{U.denominator}')
print(f'W_explicit={W.numerator}/{W.denominator}')
print(f'exact_improvement_vs_previous_explicit={(Uprev-U).numerator}/{(Uprev-U).denominator}')
print(f'positive_gap={g.numerator}/{g.denominator}')
print(f'a2={a2.numerator}/{a2.denominator}')
print(f'b2={b2.numerator}/{b2.denominator}')
print(f'u2={u2.numerator}/{u2.denominator}')
print(f'v2={v2.numerator}/{v2.denominator}')
print(f'a1={a1.numerator}/{a1.denominator}')
print(f'b1={b1.numerator}/{b1.denominator}')
print(f'u1={u1.numerator}/{u1.denominator}')
print(f'v1={v1.numerator}/{v1.denominator}')
print(f'a0={a0.numerator}/{a0.denominator}')
print(f'b0={b0.numerator}/{b0.denominator}')
print(f'u0={u0.numerator}/{u0.denominator}')
print(f'v0={v0.numerator}/{v0.denominator}')
getcontext().prec=50
print('U_decimal=',Decimal(U.numerator)/Decimal(U.denominator))
print('improvement_decimal=',Decimal((Uprev-U).numerator)/Decimal((Uprev-U).denominator))
print('gap_normalized=',Decimal(g.numerator)/Decimal(g.denominator)/Decimal(S*Q))
