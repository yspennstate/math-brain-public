from fractions import Fraction as F
Q=4870886400; S=202391574968484000000000; P=21471646
FH=89814898252348289024714956800000000000
FL=115562622066938801325250560000000000000
B0=151127280916349715999090892800000000000
FHr=57704102461588798433630822400000000000
J=811; K=3669
# inner reflected separator: u=3669 and equalize the two branches
d=F(FL-FH-40*Q*J*S,8*S*8640*Q)
b1=(F(K)-1728*d)/3840
a1=b1+d
u1=1728*a1+2112*b1
v1=2112*a1+1728*b1
assert u1==3669 and F(3633)<v1<F(3634) and 0<a1<b1<1
Hi=F(FH)+8*S*(8640*Q*a1-9600*P*b1)
Li=F(FL)+8*S*(8640*Q*b1-9600*P*b1)-40*Q*J*S
assert Hi==Li and Hi>F(B0)
# root: retain v=3029 and equalize with improved low continuation
ar=(Hi-F(FHr))/(8*S*19200*Q)
br=(F(3029)-2112*ar)/1728
ur=1728*ar+2112*br
vr=2112*ar+1728*br
assert vr==3029 and F(3175)<ur<F(3176) and 0<ar<br<1
Hr=F(FHr)+8*S*(8640*Q*ar-9600*P*br)
Lr=Hi+8*S*(-10560*Q*ar-9600*P*br)
assert Hr==Lr
T=8*S*(12480*Q+28800*P)
gap=Hr-T
assert gap>0
# Exact worst accumulated weight for the selected 416+612 continuation, from companion checker.
Mcont=F(97895,96)
Mstar=Mcont+b1+br
C=F(230400)+F(76800)*Mstar
eta=gap/(F(S)*C)
assert 0<eta<1
Pstar=F(P)+eta
U=F(9,10)-Pstar/F(Q)
W=U-F(19,30)
Uold=F(4716592387968856810867208985600000000000,5266434552595050168709499855395532216213)
assert U<Uold
print('I0130_P21471646_NESTED_EXACT_WEIGHT_ENDPOINT_PASS')
for k,v in [('inner_a',a1),('inner_b',b1),('inner_v',v1),('root_a',ar),('root_b',br),('root_u',ur),('root_gap',gap),('Mcont',Mcont),('Mstar',Mstar),('Cexact',C),('eta',eta),('Pstar',Pstar),('U_MIV',U),('W_MIV',W),('improvement',Uold-U)]:
    print(f'{k}={v.numerator}/{v.denominator}')
print('eta_decimal=%.18f'%float(eta))
print('U_decimal=%.18f'%float(U))
print('W_decimal=%.18f'%float(W))
print('improvement_decimal=%.18e'%float(Uold-U))
