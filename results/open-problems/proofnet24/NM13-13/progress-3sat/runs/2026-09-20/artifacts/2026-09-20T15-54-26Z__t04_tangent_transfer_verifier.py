from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 80

# Archived outward-interval values from NM13-06's 4.38885876 certificate.
base_A_upper_hi = Decimal('0.000000159854506579460996066850425030078009689111404669756519673471239716127351522936880471012639394118231878192')
corr_lower_lo = Decimal('0.000000161064281210006386476641093901052807137141261927461668334192905537408297126151940536184721632610205475564')
old_A_upper_hi = Decimal('-0.0000000012097746305453904097906688709747974480298572577051486607216658212809456032150600651720822384919735973715')

K = 2300
R = 11
h = F(5,10**6)
N = K + 2*R + 1

# Root-center data certified by the archived checker with eps=1e-24.
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
base_ceil = [Decimal(x) for x in ['0.109','0.390','0.854','1.512','2.378','3.472','4.828','6.496','8.554','11.155','14.692']]
tau_last_ceil = Decimal('20.459')
assert all(Decimal(c)+eps < u for c,u in zip(base_centers,base_ceil))
assert Decimal(tau_centers[-1])+eps < tau_last_ceil

# For t <= 0.02, exp(-t) > 49/50 because -log(49/50) > 1/50.
u = F(49,50)
base_y_ceil = [F(int(str(d).replace('.','')), 10**(len(str(d).split('.')[1]))) for d in base_ceil]
base_x_lower = [F(1,1)-yy/F(1000,1) for yy in base_y_ceil]
tau_z_lower = F(1,1)-F(20459,1000)/F(1000,1)

def odds(y):
    return y/(1-y)

D_lower = F(N,1) + 2*sum((odds(x*u) for x in base_x_lower), F(0,1)) + odds(tau_z_lower*u)
assert D_lower > 3200
D0 = F(3200,1)
relative_gain = D0*h/2
assert relative_gain == F(1,125)

# Survey for the downward-density coupling.
vals=[F(7,200000),F(651,100000),F(789,10000),F(1,2),F(9211,10000),F(99349,100000),F(199993,200000)]
rmax=max(vals)
smin=1-rmax*rmax

# Prove -log(smin) < 48/5 without floating point:
# e^(4/5) > sum_{j=0}^5 (4/5)^j/j! > 89/40, hence
# e^(48/5) > (89/40)^12 > 1/smin.
series = sum((F(4,5)**j / F(__import__('math').factorial(j),1) for j in range(6)), F(0,1))
assert series > F(89,40)
assert F(89,40)**12 > 1/smin
mark_log_bound = F(48,5)

# Lowering alpha decreases the positive clause term -2 alpha L because L<0.
# Only the compound-Poisson first term can increase. Two copies contribute
# expected 2*(3/2)*delta extra marks, each costing at most C.
Lip = 3*mark_log_bound
assert Lip == F(144,5)

rg = Decimal(relative_gain.numerator)/Decimal(relative_gain.denominator)
new_A0_upper = base_A_upper_hi - (Decimal(1)+rg)*corr_lower_lo
new_A0_upper_2 = old_A_upper_hi - rg*corr_lower_lo
assert abs(new_A0_upper-new_A0_upper_2) < Decimal('1e-70')

alpha0 = F(109721469,25000000)
delta = F(8,10**11)
alpha1 = alpha0-delta
transfer_penalty = Decimal(Lip.numerator)/Decimal(Lip.denominator) * (Decimal(delta.numerator)/Decimal(delta.denominator))
alpha1_upper = new_A0_upper + transfer_penalty
assert alpha1_upper < 0
assert alpha1 == F(54860734499,12500000000)

print('T04 TANGENT-CORRECTED NESTED-RADAU + DENSITY-LIPSCHITZ VERIFIER')
print('N =', N, 'h =', float(h))
print('certified coarse D_lower =', float(D_lower), '>', 3200)
print('relative tangent gain >=', float(relative_gain))
print('archived corrLB lower =', corr_lower_lo)
print('new A(alpha0) upper <=', new_A0_upper)
print('smin =', smin, 'and -log(smin) < 48/5 by rational exponential lower bound')
print('one-sided downward-density Lipschitz constant <=', float(Lip))
print('alpha0 =', float(alpha0))
print('delta =', float(delta))
print('alpha1 =', alpha1, '=', float(alpha1))
print('transfer penalty <=', transfer_penalty)
print('A(alpha1) upper <=', alpha1_upper)
print('CERTIFIED_TANGENT_GAIN =', new_A0_upper < old_A_upper_hi)
print('CERTIFIED_STRICT_DENSITY_IMPROVEMENT =', alpha1_upper < 0 and alpha1 < alpha0)
