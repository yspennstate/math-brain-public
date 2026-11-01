#!/usr/bin/env python3
"""Certified interval core for P20 / I0081 six-mode counterexample.

Input logarithmic density:
    h(y)=5/196 for |y|<=10,
         4/196 for 10<|y|<=20,
         1/196 for 20<|y|<=28,
         0 otherwise.
For rho=mu boxtimes mu, certify the physical-boundary derivative signs
    g'(8)>0, g'(18)<0, g'(29)>0, g'(37)<0, g'(46)>0, g'(50)<0.

Exact rational admissibility is checked by Fraction.
The analytic root boxes are certified by a Krawczyk/contraction argument
using mpmath interval arithmetic with outward rounding.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 120
mp.iv.dps = 80
iv = mp.iv

# Exact finite core for the input law.
inner = Fraction(5, 196)
middle = Fraction(4, 196)
outer = Fraction(1, 196)
assert 20*inner + 20*middle + 16*outer == 1
assert inner >= middle >= outer > 0
# Indicator decomposition:
# h=(1/196)1[-10,10] + (3/196)1[-20,20] + (1/196)1[-28,28].
assert inner - middle == Fraction(1,196)
assert middle - outer == Fraction(3,196)

DATA = {
    8: {
        "qre": "0.001302728302429206909179921731633517855466599605871706910829826242872389469077711801007631372890387898",
        "qim": "0.01468684106613733684441936185578147636218584982857701977288560411082090948887535199216658921151773255",
        "cre": "2.002147353313873347542582073247931804168054442014442562264930422687036481790824691672525637938538733",
        "cim": "23.12036441755470706995792630896572411202926377156284864140331179696419853884077913281571167769713299",
        "sign": 1,
    },
    18: {
        "qre": "0.000007530314504238990433202026339280582274742255792971023746655014667835681516835026429683808031382554278",
        "qim": "0.00007268685196002723099462162458598537218741465044153992230687907666880349984408644334647964440909155283",
        "cre": "264.405951568747001094603685485098993461992505783264858950477749550776131952154075900310688122774368",
        "cim": "2546.099276816666236430207799712434805773528584135402770086405944005834220779496729818159976739873968",
        "sign": -1,
    },
    29: {
        "qre": "0.0000000296407229606564995474221796167448219338396526615870072893330362259228572036009692182651929964923601",
        "qim": "0.0000001996975891418734876585859798200605734770289622027304179854075041610135233668340746549077372142974359",
        "cre": "55440.98551977604224340519540061372983724080131006439496461533375597773105363041969783552872182558477",
        "cim": "429181.6258438517415302830480651693133728795817594185072686742411757013943418417080732077702167758149",
        "sign": 1,
    },
    37: {
        "qre": "0.0000000005379678736498936738958552599402939389228582202114911111627161755869728944024811244070603143603873706",
        "qim": "0.00000000204484840068811507906933912829877604461982318069914329414467988086761373274963166973493744590500508",
        "cre": "4329697.310313682492225341548893741170313487254784354200743799100474569847776304436473618644810079849",
        "cim": "14235640.07241279915971088989278669015115100038887474766221132889539261651957141761380102642824713101",
        "sign": -1,
    },
    46: {
        "qre": "0.0000000000038028128677478097424897887269762277136214209253415759258504750477643721421513620503115739737198265",
        "qim": "0.00000000001325949751621314483102358986840854744541339259730823058384924692653757797108344863129249346298851233",
        "cre": "151277946.0085925493474299317125383629257699219117173381430401017729650605225131250091082176163265919",
        "cim": "735897283.6999105091344963168349548933034631957813725072149064896922208279694799352930322656560523782",
        "sign": 1,
    },
    50: {
        "qre": "0.0000000000008180931737256100029575682713029913062219033071800389837261516532408010998563988461374907089534233631",
        "qim": "0.000000000001023741217417438364835438129787377193448335920769495545570856159739888417650823866500231330465265832",
        "cre": "1448434472.592766230673550243633510909640145408992757943380289993238573004211863995721897574154302838",
        "cim": "4089293726.128465915792748075232447217806154257899579102114125157127943742412898601156955308053067318",
        "sign": -1,
    },
}
RADIUS = iv.mpf("1e-29")

def positive(x): return x.a > 0
def negative(x): return x.b < 0
def less_than(x,c): return x.b < iv.mpf(str(c))
def strict_contains(outer, inner):
    return (outer.real.a < inner.real.a and inner.real.b < outer.real.b
            and outer.imag.a < inner.imag.a and inner.imag.b < outer.imag.b)
def abs2(z): return z.real**2 + z.imag**2

def F(X,z):
    X=iv.mpf(X); ep=iv.exp(X); em=iv.exp(-X)
    return 2*X - iv.log(1-z*ep) + iv.log(1-z*em)
def Fp(X,z):
    X=iv.mpf(X); ep=iv.exp(X); em=iv.exp(-X)
    return ep/(1-z*ep)-em/(1-z*em)
def M(z):
    return (F(10,z)+3*F(20,z)+F(28,z))/196
def Mp(z):
    return (Fp(10,z)+3*Fp(20,z)+Fp(28,z))/196
def eta(z):
    mz=M(z); return 1-1/mz
def etap(z):
    mz=M(z); return Mp(z)/mz**2
def H(z):
    ez=eta(z); return z**2/ez
def Hp(z):
    ez=eta(z); ep=etap(z)
    return 2*z/ez-z**2*ep/ez**2
def density_and_derivative(y,z):
    s=iv.exp(-iv.mpf(y))
    w=eta(z)
    qy=-s/Hp(z)
    wy=etap(z)*qy
    g=iv.im(1/(1-w))/iv.pi
    gp=iv.im(wy/(1-w)**2)/iv.pi
    return g,gp,w

print("P20 I0081 three-level A=10 B=20 C=28 levels 5:4:1 six-mode interval core")
print("mpmath version:",mp.__version__)
print("interval dps:",mp.iv.dps)
print("exact normalization:",20*inner+20*middle+16*outer)
print("exact monotone levels:",inner,middle,outer)
print("indicator coefficients:",inner-middle,middle-outer,outer)
print("root-box radius:",RADIUS)

all_ok=True
for y in (8,18,29,37,46,50):
    d=DATA[y]
    r0=iv.mpf(d["qre"]); i0=iv.mpf(d["qim"])
    q0=iv.mpc(r0,i0)
    C=iv.mpc(iv.mpf(d["cre"]),iv.mpf(d["cim"]))
    X=iv.mpc([r0.a-RADIUS.b,r0.b+RADIUS.b],
             [i0.a-RADIUS.b,i0.b+RADIUS.b])
    s=iv.exp(-iv.mpf(y))
    branch_ok=True
    for R in (10,20,28):
        ep=iv.exp(iv.mpf(R)); em=iv.exp(-iv.mpf(R))
        branch_ok &= negative((1-X*ep).imag)
        branch_ok &= negative((1-X*em).imag)
    mz=M(X); ez=eta(X); hp=Hp(X)
    denominator_ok=positive(abs2(mz)) and positive(abs2(ez)) and positive(abs2(hp))
    f0=H(q0)-s
    contraction_factor=1-C*hp
    K=q0-C*f0+contraction_factor*(X-q0)
    inclusion=strict_contains(X,K)
    contraction_sq=abs2(contraction_factor)
    contraction_ok=less_than(contraction_sq,1)
    g,gp,w=density_and_derivative(y,X)
    one_minus_w_ok=positive(abs2(1-w))
    w_inside_unit=less_than(abs2(w),1)
    density_positive=positive(g)
    derivative_sign=positive(gp) if d["sign"]>0 else negative(gp)
    upper_half_plane=positive(X.imag)
    ok=all([branch_ok,denominator_ok,inclusion,contraction_ok,upper_half_plane,
            one_minus_w_ok,w_inside_unit,density_positive,derivative_sign])
    all_ok &= ok
    print("\ny =",y)
    print("X.real =",X.real)
    print("X.imag =",X.imag)
    print("principal-log branch safe:",branch_ok)
    print("denominators nonzero:",denominator_ok)
    print("K.rawczyk.real =",K.real)
    print("K.rawczyk.imag =",K.imag)
    print("K(X) subset int(X):",inclusion)
    print("|1-C Hprime(X)|^2 =",contraction_sq," <1:",contraction_ok)
    print("Im X > 0:",upper_half_plane)
    print("|w|^2 =",abs2(w)," <1:",w_inside_unit)
    print("|1-w|^2 =",abs2(1-w)," nonzero:",one_minus_w_ok)
    print("g(y) =",g," positive:",density_positive)
    print("gprime(y) =",gp," expected sign:",d["sign"]," PASS:",derivative_sign)
    print("H(q0)-exp(-y) =",f0)
    print("POINT CERTIFICATE PASS:",ok)

assert all_ok
print("\nALL_INTERVAL_CHECKS_PASS")
print("Certified sign pattern: gprime(8)>0, gprime(18)<0, gprime(29)>0, gprime(37)<0, gprime(46)>0, gprime(50)<0.")
