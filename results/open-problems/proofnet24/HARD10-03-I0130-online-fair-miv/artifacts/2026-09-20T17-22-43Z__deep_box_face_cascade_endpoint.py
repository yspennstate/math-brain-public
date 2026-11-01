from fractions import Fraction as F
from decimal import Decimal,getcontext
Q=4870886400; S=202391574968484000000000; P0=21487480; N=20000
raw='''7015 57716764100348914229089094420742144000 57490832477771103508134631645446144000
6624 62101964736745630658961408000000000000 61870121152453901200614969600000000000
7269 54993360448068548123897856000000000000 54774758130943293204781255645446144000
1188 143939792693719849122607104000000000000 143711901649610295927339225600000000000
6184 67425464314579923945964195200000000000 67218999131947660495621776000000000000
6101 68490028839221486448795648000000000000 68274016052182722399604126045446144000
7552 52059472620558701068873728000000000000 51859751852066811788212329600000000000
1582 136680784680031044513691852800000000000 136458806114067784071284822400000000000
7175 55974440402082790770253824000000000000 55738429668607059252613793245446144000
1048 146626009207077958561522339200000000000 146408251256730079593456412800000000000
3534 104196619651224298314643660800000000000 103981583231552663807603062936338432000
9926 31110712746977495328620544000000000000 30887423209307542796756820445446144000
4666 87138550699726331822248099220742144000 86906065520590657060902220800000000000
4683 86934134835698188396548096000000000000 86718499606397680410392294400000000000
2541 120164789732268039927939072000000000000 119990679317954941551061334400000000000'''
V0={};V1={}
for line in raw.splitlines():j,a,b=map(int,line.split());V0[j]=a;V1[j]=b
D={j:V1[j]-V0[j] for j in V0}
def C(j,x): return F(V0[j])+x*D[j]
def nr(FH,FL,P,vwall):
 a=(FL-FH)/(8*S*19200*Q); b=(F(vwall)-2112*a)/1728
 u=1728*a+2112*b; v=2112*a+1728*b
 H=FH+8*S*(8640*Q*a-9600*P*b); L=FL+8*S*(-10560*Q*a-9600*P*b); assert H==L
 return H,a,b,u,v
def rv(FH,FL,P,J,vwall):
 d=(FL-FH-40*Q*J*S)/(8*S*8640*Q); b=(F(vwall)-2112*d)/3840; a=b+d
 u=1728*a+2112*b;v=2112*a+1728*b
 H=FH+8*S*(8640*Q*a-9600*P*b);L=FL+8*S*(8640*Q*b-9600*P*b)-40*Q*J*S;assert H==L
 return H,a,b,u,v
def ru(FH,FL,P,J,uwall):
 d=(FL-FH-40*Q*J*S)/(8*S*8640*Q); b=(F(uwall)-1728*d)/3840;a=b+d
 u=1728*a+2112*b;v=2112*a+1728*b
 H=FH+8*S*(8640*Q*a-9600*P*b);L=FL+8*S*(8640*Q*b-9600*P*b)-40*Q*J*S;assert H==L
 return H,a,b,u,v
def sat3(FL,FH_avail,P):
 J=382; vwall=F(3751); b=F(1); d=(vwall-3840)/2112; a=b+d
 FH_req=FL-40*Q*J*S-8*S*8640*Q*d
 assert FH_avail>=FH_req
 u=1728*a+2112*b;v=2112*a+1728*b
 H=FH_req+8*S*(8640*Q*a-9600*P*b);L=FL+8*S*(8640*Q*b-9600*P*b)-40*Q*J*S;assert H==L
 return H,a,b,u,v,FH_req,FH_avail-FH_req

def data(x):
 P=F(P0)+N*x
 B14,a14,b14,u14,v14=nr(C(9926,x),C(4666,x),P,2509)
 B15,a15,b15,u15,v15=rv(C(4683,x),C(2541,x),P,1048,3589)
 B13,a13,b13,u13,v13=nr(B14,B15,P,2987)
 B8,a8,b8,u8,v8=rv(B13,C(3534,x),P,245,3779)
 B4,a4,b4,u4,v4=nr(C(6624,x),B8,P,F(3124999999,1000000))
 B6,a6,b6,u6,v6=nr(C(7269,x),C(1188,x),P,2962)
 B3,a3,b3,u3,v3,cap3,slack3=sat3(B4,B6,P)
 B7,a7,b7,u7,v7=nr(C(6184,x),C(6101,x),P,40)
 B2,a2,b2,u2,v2=rv(B7,B3,P,2824,3206)
 B10,a10,b10,u10,v10=nr(C(7552,x),C(1582,x),P,2901)
 B1,a1,b1,u1,v1=ru(B10,B2,P,812,3671)
 Br,a0,b0,u0,v0=nr(C(7015,x),B1,P,3028)
 T=8*S*(12480*Q+28800*P)
 return locals()

def verify(d):
 def oo(x,a,b): return F(a)<x<F(b)
 for i in [14,15,13,8,4,6,3,7,2,10,1,0]: assert 0<d['a'+str(i)]<d['b'+str(i)]<=1
 assert oo(d['u14'],2750,2751) and d['v14']==2509
 assert oo(d['u15'],3634,3635) and d['v15']==3589
 assert oo(d['u13'],3139,3140) and d['v13']==2987
 assert oo(d['u8'],3789,3790) and d['v8']==3779
 assert oo(d['u4'],3254,3255) and oo(d['v4'],3124,3125)
 assert oo(d['u6'],3118,3119) and d['v6']==2962
 assert oo(d['u3'],3767,3768) and d['v3']==3751 and d['b3']==1 and d['slack3']>0
 assert oo(d['u7'],42,43) and d['v7']==40
 assert oo(d['u2'],3316,3317) and d['v2']==3206
 assert oo(d['u10'],3068,3069) and d['v10']==2901
 assert d['u1']==3671 and oo(d['v1'],3635,3636)
 assert oo(d['u0'],3174,3175) and d['v0']==3028
 return True

lo=F(105166525,10**9)
hi=F(105166526,10**9)
dl=data(lo); dh=data(hi)
verify(dl); verify(dh)
assert dl['Br']>dl['T'] and dh['Br']<dh['T']
P_eff=dl['P']
U=F(9,10)-P_eff/Q
W=U-F(19,30)
Uold=F(436231028046001,487088640000000)
assert P_eff==F(42979166661,2000)
assert U==F(2908205451113,3247257600000)
assert W==F(851608971113,3247257600000)
assert Uold-U==F(210379051,487088640000000)
print('I0130_DEEP_BOX_FACE_CASCADE_PASS')
print(f'x_bracket={lo.numerator}/{lo.denominator},{hi.numerator}/{hi.denominator}')
print(f'P_effective={P_eff.numerator}/{P_eff.denominator}')
print(f'U_explicit={U.numerator}/{U.denominator}')
print(f'W_explicit={W.numerator}/{W.denominator}')
print(f'improvement_vs_previous={(Uold-U).numerator}/{(Uold-U).denominator}')
print(f'positive_gap={(dl["Br"]-dl["T"]).numerator}/{(dl["Br"]-dl["T"]).denominator}')
print(f'cap3_slack={dl["slack3"].numerator}/{dl["slack3"].denominator}')
getcontext().prec=50
print('U_decimal=',Decimal(U.numerator)/Decimal(U.denominator))
print('W_decimal=',Decimal(W.numerator)/Decimal(W.denominator))
print('improvement_decimal=',Decimal((Uold-U).numerator)/Decimal((Uold-U).denominator))
print('gap_normalized=',Decimal((dl['Br']-dl['T']).numerator)/Decimal((dl['Br']-dl['T']).denominator)/Decimal(S*Q))
print('cap3_slack_normalized=',Decimal(dl['slack3'].numerator)/Decimal(dl['slack3'].denominator)/Decimal(S*Q))
