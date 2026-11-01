from fractions import Fraction as F
from decimal import Decimal, getcontext

Q = 4_870_886_400
P0 = 21_454_950
S = 202_391_574_968_484_000_000_000
FH0 = 57_721_999_839_463_163_025_285_120_000_000_000_000
FL0 = 151_136_423_727_392_343_150_259_200_000_000_000_000
FH1 = 57_721_999_155_541_552_891_783_987_200_000_000_000
FL1 = 151_136_423_214_451_135_550_133_350_400_000_000_000
KH = 3176
q = 3029

def add(x,y):
    n=max(len(x),len(y)); return [(x[i] if i<len(x) else F(0))+(y[i] if i<len(y) else F(0)) for i in range(n)]
def scale(x,c): return [c*z for z in x]
def mul(x,y):
    z=[F(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y): z[i+j]+=a*b
    return z

def ev(p,t):
    s=F(0)
    for c in reversed(p): s=s*t+c
    return s

FH=[F(FH0),F(FH1-FH0)]
FL=[F(FL0),F(FL1-FL0)]
a=scale(add(FL,scale(FH,-1)), F(1,8*S*19200*Q))
b=scale(add([F(q)],scale(a,-2112)), F(1,1728))
u=add(scale(a,1728),scale(b,2112))
v=add(scale(a,2112),scale(b,1728))
P=[F(P0),F(1)]
H=add(FH, scale(add(scale(a,8640*Q), scale(mul(P,b),-9600)), 8*S))
T=scale(add([F(12480*Q)],scale(P,28800)),8*S)
gap=add(H,scale(T,-1))

assert a == [F(66_107_841_150,107_159_500_800), F(121,107_159_500_800)]
assert b == [F(87_578_772_450,87_675_955_200), F(-121,87_675_955_200)]
assert u == [F(398_794_164_990,125_577_540), F(-121,125_577_540)]
assert v == [F(3029),F(0)]

A=1331
B=41_489_323_036_260
C=34_382_775_109_500
fac=F(1_402_166_902_000_000_000,87)
assert gap == [fac*C, -fac*B, fac*A]
assert ev(gap,F(0)) == F(16_070_129_752_483_441_923_000_000_000_000,29)

for tt in (F(0),F(1)):
    aa,bb,uu,vv=ev(a,tt),ev(b,tt),ev(u,tt),ev(v,tt)
    assert F(0)<aa<bb<F(1)
    assert F(3175)<uu<F(3176)
    assert vv==F(3029)

def qpoly(tt): return A*tt*tt-B*tt+C
lo=F(828_713,1_000_000)
hi=F(414_357,500_000)
assert qpoly(lo)>0
assert qpoly(hi)<0
assert 2*A-B<0

glo=ev(gap,lo)
assert glo>0
alpha_lo=F(9,10)-F(P0, Q)-lo/F(Q)
width_lo=alpha_lo-F(19,30)

getcontext().prec=70
DD=Decimal(B)*Decimal(B)-Decimal(4*A*C)
tau=(Decimal(B)-DD.sqrt())/Decimal(2*A)
U=Decimal(145_411_427)/Decimal(162_362_880)-tau/Decimal(Q)
W=U-Decimal(19)/Decimal(30)
print('I0130_LARGE_WALL_CHORD_ENDPOINT_PASS')
print('FH0=',FH0); print('FL0=',FL0); print('FH1=',FH1); print('FL1=',FL1)
print('a(t)=(66107841150+121 t)/107159500800')
print('b(t)=(87578772450-121 t)/87675955200')
print('v(t)=3029')
print('u(t)=(398794164990-121 t)/125577540 in (3175,3176) for 0<=t<=1')
print('gap(t)=(1402166902000000000/87)*(1331 t^2-41489323036260 t+34382775109500)')
print('q(828713/1000000)=',qpoly(lo))
print('q(414357/500000)=',qpoly(hi))
print('tau=',tau)
print('U_MIV_algebraic=',U)
print('W_MIV_algebraic=',W)
print('strict_rational_t=',lo,'strict_gap=',glo)
print('strict_rational_U=',alpha_lo,'strict_rational_W=',width_lo)
