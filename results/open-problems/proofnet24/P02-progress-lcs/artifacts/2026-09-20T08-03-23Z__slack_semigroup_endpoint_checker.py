from fractions import Fraction

p=256717
q=800000
d=q-p
M=5_000_000_000_000_000_000
a=int('1995237757733917147310102692686664915858011319606812684127301')
b=4_220_452_010_631_561_279
S=q**6*d
c=[q**(6-k)*d*p**k for k in range(7)] + [p**7]
D_R=c[0]+c[3]+c[6]+c[7]
H=2200
D_new=D_R+H*c[7]+1
assert D_new*M <= a

R=Fraction(a,b)
t=Fraction(p,q)
scale=t*t/S
base=4*t*t
beta_R=R-Fraction(D_R,2*a*b)
beta_new=R-Fraction(D_new,2*a*b)
lambda_R=scale*beta_R
lambda_new=scale*beta_new
assert 0 < base < 1
assert 0 < lambda_new < lambda_R < 1
# The exact two-step theorem is rho(B)^2 <= (a^2-D_new)/b^2.
# beta_new is a strict rational majorant of that square root.
assert beta_new*beta_new > R*R-Fraction(D_new,b*b)

# Exact positive atanh-series enclosure for -log(z).
def neglog_bounds(z,K=220):
    assert 0 < z < 1
    u=(1-z)/(1+z)
    u2=u*u
    pw=u
    s=Fraction(0,1)
    for k in range(K):
        s += 2*pw/Fraction(2*k+1,1)
        pw *= u2
    tail = 2*pw/Fraction(2*K+1,1)/(1-u2)
    return s,s+tail

Alo,Ahi=neglog_bounds(base)
Nlo,Nhi=neglog_bounds(lambda_new)
Rlo,Rhi=neglog_bounds(lambda_R)
U_new_upper=Ahi/Nlo
U_R_lower=Alo/Rhi
Q=Fraction(
    82627594276228262501510658153729663282346199619319002388080618331256294443029954,
    10**80,
)
assert U_new_upper < Q < U_R_lower
L=Fraction(99083249,125000000)
assert L < U_new_upper

print('P02 T02 successor-slack semigroup endpoint checker')
print('D_R=' + str(D_R))
print('D_new=' + str(D_new))
print('D_new_over_D_R=' + str(Fraction(D_new,D_R)))
print('beta_R_num=' + str(beta_R.numerator))
print('beta_R_den=' + str(beta_R.denominator))
print('beta_new_num=' + str(beta_new.numerator))
print('beta_new_den=' + str(beta_new.denominator))
print('lambda_new_num=' + str(lambda_new.numerator))
print('lambda_new_den=' + str(lambda_new.denominator))
print('Q_num=' + str(Q.numerator))
print('Q_den=' + str(Q.denominator))
print('D_NEW_STRICTLY_BEATS_D_R=PASS')
print('TWO_STEP_SPECTRAL_MAJORANT_STRICTLY_IMPROVES=PASS')
print('EXACT_LOG_SEPARATOR_PASS')
print('SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS')
print('ALL_EXACT_CHECKS_PASS')
