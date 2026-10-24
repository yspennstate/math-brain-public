from fractions import Fraction as F
from decimal import Decimal, getcontext

def fd(s):
    a,b=s.split(".")
    return F(int(a+b),10**len(b))

def dec(x, digits=70):
    getcontext().prec = digits + 10
    return format(Decimal(x.numerator)/Decimal(x.denominator), f".{digits}f")

# Certified exact-rational enclosure endpoints copied from the immutable
# account03/B18 shared-graft extension report/checker.
R3_LO=fd("6.5218509158557171794336583919648574196767563718341573")
R3_HI=fd("6.5218509158557171794342597335463471829453334335276482")
R4_LO=fd("6.5218509485644448965490881329959858569477358114202361")
R4_HI=fd("6.5218509485644448965496895824490791318643557898359042")

I3=F(
7293635508681408439604535567475568379907630049888658770829188246173012479808017893097,
1942668892225729070919461906823518906642406839052139521251812409738904285205208498176)
alpha=F(9,256)
a=F(133,128)
B=F(257,256)
source_I=F(261,128)

# Exact next influence and source recurrence.
I4=source_I+alpha*(I3**4-1)
assert F(8) < I4 < F(9)
D3=I4-1

# Exact relaxation identity:
# R_{t+1}-R_t = [K(c_t^4)-a R_t]/D_t,
# hence T(c_t):=K(c_t^4)/a = R_t + D_t/a*(R_{t+1}-R_t).
T3_LO=R3_LO+F(128,133)*D3*(R4_LO-R3_HI)
T3_HI=R3_HI+F(128,133)*D3*(R4_HI-R3_LO)

# Singleton contraction c_{t+1}=57/256+c_t^4/256.
c1=F(14593,65536)
def nxt(c):
    return F(57,256)+c**4/F(256)
c2=nxt(c1); c3=nxt(c2); c4=nxt(c3)
assert F(0) < c4 < c3 < c2 < c1 < F(1,4)
assert c1-c2 < F(1,100000)

# On [0,1/4], F'(c)=c^3/64 <= 1/4096.
# Therefore |c3-c_*| <= L^2 |c1-c2|/(1-L).
L=F(1,4096)
c_tail=L**2*(c1-c2)/(1-L)

# The report proves |T'(c)|<10/3 on [0,1/4].
T_drift=F(10,3)*c_tail
T_MIN=T3_LO-T_drift
T_MAX=T3_HI+T_drift

# For t=4, D4=B+alpha I4^4 and lambda4=a/D4.
# I4<9 and I4>8 give lower/upper bounds without floating point.
lam4_LO=a/(B+alpha*F(9)**4)
lam4_HI=a/(B+alpha*F(8)**4)

# I5=1+D4 > 1+B+alpha*8^4.
I5_LO=F(1)+B+alpha*F(8)**4
assert I5_LO > F(146)

# For t>=5, I_{t+1}>I_t^2, so
# sum_{t>=5} lambda_t < (a/alpha) q/(1-q), q=I5_LO^{-4}.
q=I5_LO**-4
tail_lambda=(a/alpha)*q/(1-q)
SUM_LAMBDA=lam4_HI+tail_lambda
assert SUM_LAMBDA < F(72,10000)  # <0.0072

# Bootstrap: all future thresholds lie in [T_MIN,T_MAX].
# The total possible rise from R4 is too small to reach T_MIN,
# hence every future increment is strictly positive.
max_future_rise=SUM_LAMBDA*(T_MAX-R4_LO)
headroom=T_MIN-R4_HI-max_future_rise
assert headroom > F(217,1_000_000_000)  # >2.17e-7

# Rigorous F5 gain and new FEI lower floor.
gain5_LO=lam4_LO*(T_MIN-R4_HI)
R5_LO=R4_LO+gain5_LO
assert gain5_LO > F(981,1_000_000_000_000) # >9.81e-10
assert R5_LO > fd("6.5218509495457")

print("PASS")
print("I4=" + dec(I4,60))
print("T3_LO=" + dec(T3_LO,60))
print("T3_HI=" + dec(T3_HI,60))
print("c_tail_bound=" + dec(c_tail,70))
print("T_drift_bound=" + dec(T_drift,70))
print("T_MIN=" + dec(T_MIN,60))
print("T_MAX=" + dec(T_MAX,60))
print("lambda4_LO=" + dec(lam4_LO,60))
print("lambda4_HI=" + dec(lam4_HI,60))
print("tail_lambda_upper=" + dec(tail_lambda,70))
print("all_future_lambda_upper=" + dec(SUM_LAMBDA,60))
print("bootstrap_headroom=" + dec(headroom,60))
print("gain5_LO=" + dec(gain5_LO,70))
print("R5_LO=" + dec(R5_LO,70))
print("future_gain_sign=STRICTLY_POSITIVE_FOR_ALL_ROUNDS_t>=4")
print("full_FEI_status=OPEN")
