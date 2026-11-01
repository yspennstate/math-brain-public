from fractions import Fraction as F
from decimal import Decimal,getcontext
Q=4870886400
S=202391574968484000000000
P0=21486645
N=5000
V0={
7015:57717451925852225832575119992010752000,
4483:89751013341052650666319872000000000000,
6141:67853672097701403630615552000000000000,
4150:94625640757741190105710080000000000000,
245:162214607164298029501897011600000000000,
6624:62102457937488574658755584000000000000,
}
VN={
7015:57713333210263533596131853098186752000,
4483:89746803174454639021031737498186752000,
6141:67847612371198092087934820400000000000,
4150:94624785855728523229294080000000000000,
245:162205629484928021991564434996373504000,
6624:62097972393311700752412108000000000000,
}
D={j:VN[j]-V0[j] for j in V0}
def chord(j,t): return F(V0[j])+t*D[j]

def data(t):
    P=F(P0)+N*t
    # J4=3369: non-reflected continuous refinement, b4=1.
    FH4=chord(6624,t); FL4=chord(245,t)
    a4=(FL4-FH4)/(8*S*19200*Q); b4=F(1)
    u4=1728*a4+2112*b4; v4=2112*a4+1728*b4
    H4=FH4+8*S*(8640*Q*a4-9600*P*b4)
    L4=FL4+8*S*(-10560*Q*a4-9600*P*b4)
    assert H4==L4

    # J3=382: active-wall continuation v3=3751, high child 4150, low child 3369.
    J3=382
    FH3=chord(4150,t); FL3=H4
    d3=(FL3-FH3-40*Q*J3*S)/(8*S*8640*Q)
    b3=(F(3751)-2112*d3)/3840; a3=b3+d3
    u3=1728*a3+2112*b3; v3=2112*a3+1728*b3
    H3=FH3+8*S*(8640*Q*a3-9600*P*b3)
    L3=FL3+8*S*(8640*Q*b3-9600*P*b3)-40*Q*J3*S
    assert H3==L3

    # J2=2824: reflected low wall v2=3206.
    J2=2824
    FH2=chord(6141,t); FL2=H3
    d2=(FL2-FH2-40*Q*J2*S)/(8*S*8640*Q)
    b2=(F(3206)-2112*d2)/3840; a2=b2+d2
    u2=1728*a2+2112*b2; v2=2112*a2+1728*b2
    H2=FH2+8*S*(8640*Q*a2-9600*P*b2)
    L2=FL2+8*S*(8640*Q*b2-9600*P*b2)-40*Q*J2*S
    assert H2==L2

    # J1=812: reflected active wall v1=3636.
    J1=812
    FH1=chord(4483,t); FL1=H2
    d1=(FL1-FH1-40*Q*J1*S)/(8*S*8640*Q)
    b1=(F(3636)-2112*d1)/3840; a1=b1+d1
    u1=1728*a1+2112*b1; v1=2112*a1+1728*b1
    H1=FH1+8*S*(8640*Q*a1-9600*P*b1)
    L1=FL1+8*S*(8640*Q*b1-9600*P*b1)-40*Q*J1*S
    assert H1==L1

    # Source root v0=3028.
    FHr=chord(7015,t)
    a0=(H1-FHr)/(8*S*19200*Q)
    b0=(F(3028)-2112*a0)/1728
    u0=1728*a0+2112*b0; v0=2112*a0+1728*b0
    H0=FHr+8*S*(8640*Q*a0-9600*P*b0)
    L0=H1+8*S*(-10560*Q*a0-9600*P*b0)
    assert H0==L0
    T=8*S*(12480*Q+28800*P)
    return a4,b4,u4,v4,a3,b3,u3,v3,a2,b2,u2,v2,a1,b1,u1,v1,a0,b0,u0,v0,H0-T

lo=F(166907998,10**9)
hi=F(166907999,10**9)
z=data(lo); zh=data(hi)
assert z[-1]>0 and zh[-1]<0
(a4,b4,u4,v4,a3,b3,u3,v3,a2,b2,u2,v2,a1,b1,u1,v1,a0,b0,u0,v0,g)=z
assert 0<a4<b4<=1 and F(3254)<u4<F(3255) and F(3124)<v4<F(3125)
assert 0<a3<b3<=1 and F(3767)<u3<F(3768) and v3==3751
assert 0<a2<b2<1 and F(3316)<u2<F(3317) and v2==3206
assert 0<a1<b1<1 and F(3670)<u1<F(3671) and v1==3636
assert 0<a0<b0<1 and F(3174)<u0<F(3175) and v0==3028
P_eff=F(P0)+N*lo
U=F(9,10)-P_eff/Q
W=U-F(19,30)
Uprev=F(1090578958150883,1217721600000000)
assert U<Uprev
print('I0130_FIVE_LEVEL_ACTIVE_WALL_PASS')
print(f't_bracket={lo.numerator}/{lo.denominator},{hi.numerator}/{hi.denominator}')
print(f'P_effective={P_eff.numerator}/{P_eff.denominator}')
print(f'U_explicit={U.numerator}/{U.denominator}')
print(f'W_explicit={W.numerator}/{W.denominator}')
print(f'improvement_vs_previous={(Uprev-U).numerator}/{(Uprev-U).denominator}')
print(f'positive_gap={g.numerator}/{g.denominator}')
for nm,x in [('a4',a4),('b4',b4),('u4',u4),('v4',v4),('a3',a3),('b3',b3),('u3',u3),('v3',v3),('a2',a2),('b2',b2),('u2',u2),('v2',v2),('a1',a1),('b1',b1),('u1',u1),('v1',v1),('a0',a0),('b0',b0),('u0',u0),('v0',v0)]:
    print(f'{nm}={x.numerator}/{x.denominator}')
getcontext().prec=50
print('U_decimal=',Decimal(U.numerator)/Decimal(U.denominator))
print('W_decimal=',Decimal(W.numerator)/Decimal(W.denominator))
print('improvement_decimal=',Decimal((Uprev-U).numerator)/Decimal((Uprev-U).denominator))
print('gap_normalized=',Decimal(g.numerator)/Decimal(g.denominator)/Decimal(S*Q))
