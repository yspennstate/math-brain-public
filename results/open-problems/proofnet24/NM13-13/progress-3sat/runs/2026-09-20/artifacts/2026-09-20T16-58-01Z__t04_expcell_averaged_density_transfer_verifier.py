from fractions import Fraction as F
from decimal import Decimal, getcontext, ROUND_CEILING
import math

getcontext().prec = 120

# Archived outward-interval values from NM13-06's 4.38885876 certificate.
base_A_upper_hi = Decimal('0.000000159854506579460996066850425030078009689111404669756519673471239716127351522936880471012639394118231878192')
corr_lower_lo = Decimal('0.000000161064281210006386476641093901052807137141261927461668334192905537408297126151940536184721632610205475564')
old_A_upper_hi = Decimal('-0.0000000012097746305453904097906688709747974480298572577051486607216658212809456032150600651720822384919735973715')

K = 2300
R = 11
h = F(5,10**6)
N = K + 2*R + 1

base_centers = [
'0.10811434877041591547197332520229392481333811647909509658066325131739346177722031',
'0.38961179433949103180935168130769110476075892251509127722205349682222078469488787',
'0.85302815455684441825894440315507826468710197003218042883300620638164339796885793',
'1.5119803451375556786014789860579987654304266751392532521241821390094546699078513',
'2.3775412673697419072807377974951765316939608008841864226598943438319679235359591',
'3.4718031374428377697474403581744441193193995221031368344417466847956425223872879',
'4.8273085501311171722752344538559720987468493099499172037697259702885065062329339',
'6.4951967385949401030992584945005508803889755669985057656501843057253621640875252',
'8.5533446620142581089650546391336420351601118097037908429385336533121173291915833',
'11.154004044320008822388762833852666608277622814441372286069054520846004895936782',
'14.691646845338102885031685000732982545933957606637073818366948166487519471668833']
tau_centers = [
'0.86397294947911821346911520415749922672046726384574218996895963447287793020577349',
'6.9369437416031674176432126947052890027564081798420640256511109181401958048285061',
'15.704055446327097514316042091997184245469176286312034946225319888611583247031691',
'20.458368694345474673903928232710450230798065015507329864387747125874955899694237']
eps = Decimal('1e-24')

base_ceil_dec = [Decimal(x) for x in [
'0.108115','0.389612','0.853029','1.511981','2.377542','3.471804',
'4.827309','6.495197','8.553345','11.154005','14.691647']]
tau_last_ceil_dec = Decimal('20.458369')
assert all(Decimal(c)+eps < u for c,u in zip(base_centers,base_ceil_dec))
assert Decimal(tau_centers[-1])+eps < tau_last_ceil_dec

def dec_to_frac(d):
    s = format(d, 'f')
    if '.' in s:
        a,b = s.split('.')
        return F(int(a+b), 10**len(b))
    return F(int(s),1)

x0 = F(1,50)
alt5 = sum(((-1)**j * x0**j / F(math.factorial(j),1) for j in range(6)), F(0,1))
u = F(98019867,10**8)
assert alt5 > u

base_y_ceil = [dec_to_frac(d) for d in base_ceil_dec]
base_x_lower = [F(1,1)-yy/F(1000,1) for yy in base_y_ceil]
tau_z_lower = F(1,1)-dec_to_frac(tau_last_ceil_dec)/F(1000,1)

def odds(y):
    return y/(1-y)

D_lower = F(N,1) + 2*sum((odds(x*u) for x in base_x_lower), F(0,1)) + odds(tau_z_lower*u)
assert D_lower > 3244

x = D_lower*h
cell_factor = F(1,1)
for n in range(1,7):
    cell_factor += x**n / F(math.factorial(n+1),1)
assert cell_factor > F(1008155,1000000)

facD = Decimal(cell_factor.numerator)/Decimal(cell_factor.denominator)
new_A0_upper = base_A_upper_hi - facD*corr_lower_lo
assert new_A0_upper < old_A_upper_hi

vals=[F(7,200000),F(651,100000),F(789,10000),F(1,2),F(9211,10000),F(99349,100000),F(199993,200000)]
w=[F(147,100000),F(2717,50000),F(3669,20000),F(13037,25000),F(3669,20000),F(2717,50000),F(147,100000)]
assert sum(w,F(0,1)) == 1
assert sum((wi*ri for wi,ri in zip(w,vals)),F(0,1)) == F(1,2)

def exp_lower(q, n=50):
    term=F(1,1)
    s=term
    for k in range(1,n+1):
        term = term*q/F(k,1)
        s += term
    return s

scale=10**8
M_upper=F(0,1)
max_log_bound_degree=0
max_log_ceiling=F(0,1)
for i,ri in enumerate(vals):
    for j,rj in enumerate(vals):
        p=ri*rj
        pd = Decimal(p.numerator)/Decimal(p.denominator)
        target = -(Decimal(1)-pd).ln()
        qint = int((target*Decimal(scale)).to_integral_value(rounding=ROUND_CEILING))
        C=F(qint,scale)
        degree=20
        while exp_lower(C,degree) <= 1/(1-p):
            degree += 5
            if degree > 80:
                C += F(1,scale)
                degree=20
        max_log_bound_degree=max(max_log_bound_degree,degree)
        max_log_ceiling=max(max_log_ceiling,C)
        M_upper += w[i]*w[j]*C

J_lower=F(0,1)
MCLAUSE=50
for m in range(1,MCLAUSE+1):
    rm=sum((wi*(ri**m) for wi,ri in zip(w,vals)),F(0,1))
    J_lower += rm**3/F(m,1)

Lip = 3*M_upper - 2*J_lower
assert Lip > 0
assert Lip < F(82,100)

alpha0=F(109721469,25000000)
delta=F(3078,10**12)
alpha1=alpha0-delta
prev_alpha=F(54860734499,12500000000)
assert alpha1 < prev_alpha < alpha0

LipD=Decimal(Lip.numerator)/Decimal(Lip.denominator)
deltaD=Decimal(delta.numerator)/Decimal(delta.denominator)
transfer_penalty=LipD*deltaD
alpha1_upper=new_A0_upper+transfer_penalty
assert alpha1_upper < 0

print('T04 EXPONENTIAL-CELL + SURVEY-AVERAGED DENSITY-TRANSFER VERIFIER')
print('N =', N, 'h =', float(h))
print('certified exp(-0.02) lower rational =', float(u))
print('certified D_lower =', Decimal(D_lower.numerator)/Decimal(D_lower.denominator))
print('certified exponential cell factor >=', facD)
print('archived correction lower =', corr_lower_lo)
print('old tangent-corrected A(alpha0) upper <=', Decimal('-2.49828888022544150160e-9'))
print('new exponential-cell A(alpha0) upper <=', new_A0_upper)
print('survey-averaged M=E[-log(1-R1R2)] upper <=', Decimal(M_upper.numerator)/Decimal(M_upper.denominator))
print('clause J=E[-log(1-R1R2R3)] lower >=', Decimal(J_lower.numerator)/Decimal(J_lower.denominator))
print('density one-sided Lipschitz constant <=', LipD)
print('max exact exp Taylor degree used for pair-log ceilings =', max_log_bound_degree)
print('max pair log ceiling =', Decimal(max_log_ceiling.numerator)/Decimal(max_log_ceiling.denominator))
print('alpha0 =', Decimal(alpha0.numerator)/Decimal(alpha0.denominator))
print('delta =', deltaD)
print('alpha1 =', alpha1, '=', Decimal(alpha1.numerator)/Decimal(alpha1.denominator))
print('previous project alpha =', Decimal(prev_alpha.numerator)/Decimal(prev_alpha.denominator))
print('strict project-endpoint gain =', Decimal((prev_alpha-alpha1).numerator)/Decimal((prev_alpha-alpha1).denominator))
print('transfer penalty <=', transfer_penalty)
print('A(alpha1) upper <=', alpha1_upper)
print('CERTIFIED_EXPONENTIAL_CELL_GAIN =', new_A0_upper < Decimal('-2.49828888022544150160e-9'))
print('CERTIFIED_AVERAGED_LIPSCHITZ =', Lip < F(82,100))
print('CERTIFIED_STRICT_DENSITY_IMPROVEMENT =', alpha1_upper < 0 and alpha1 < prev_alpha)
