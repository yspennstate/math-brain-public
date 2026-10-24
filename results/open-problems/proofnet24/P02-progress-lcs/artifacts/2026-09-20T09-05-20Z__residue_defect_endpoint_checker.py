from fractions import Fraction

p=256717
q=800000
d=q-p
a=int('1995237757733917147310102692686664915858011319606812684127301')
b=4_220_452_010_631_561_279
alpha=a % b
h=707_440_146_652_911_839
M=5_000_000_000_000_000_000
vstar=h+b
assert (alpha*h) % b == 1
assert vstar <= M < 2*b
assert a % vstar != 0
S=q**6*d
c=[q**(6-k)*d*p**k for k in range(7)] + [p**7]
D_R=c[0]+c[3]+c[6]+c[7]
D_C=D_R+2200*c[7]+1
D_star=Fraction(a,vstar)
assert D_star > D_C

R=Fraction(a,b)
t=Fraction(p,q)
scale=t*t/S
base=4*t*t
beta_C=R-Fraction(D_C,2*a*b)
beta_star=R-Fraction(1,2*b*vstar)
lambda_C=scale*beta_C
lambda_star=scale*beta_star
assert 0 < base < 1
assert 0 < lambda_star < lambda_C < 1
assert beta_star*beta_star > R*R-D_star/Fraction(b*b,1)

# Rigorous positive atanh-series bounds for -log z.
def neglog_bounds(z,K=260):
    assert 0 < z < 1
    u=(1-z)/(1+z)
    u2=u*u
    pw=u
    s=Fraction(0,1)
    for k in range(K):
        s += 2*pw/Fraction(2*k+1,1)
        pw *= u2
    tail=2*pw/Fraction(2*K+1,1)/(1-u2)
    return s,s+tail

Alo,Ahi=neglog_bounds(base)
Nlo,Nhi=neglog_bounds(lambda_star)
Clo,Chi=neglog_bounds(lambda_C)
U_star_upper=Ahi/Nlo
U_C_lower=Alo/Chi
Q=Fraction(
    82627594276228262501510658153729663282346199619319002388080618331256294443029953,
    10**80,
)
assert U_star_upper < Q < U_C_lower
L=Fraction(99083249,125000000)
assert L < U_star_upper

print('P02 T02 residue-optimal defect endpoint checker')
print('alpha=a_mod_b=' + str(alpha))
print('h=alpha_inverse_mod_b=' + str(h))
print('vstar=h+b=' + str(vstar))
print('D_C=' + str(D_C))
print('D_star_num=' + str(D_star.numerator))
print('D_star_den=' + str(D_star.denominator))
print('D_star_over_D_C=' + str(D_star/Fraction(D_C,1)))
print('beta_star_num=' + str(beta_star.numerator))
print('beta_star_den=' + str(beta_star.denominator))
print('lambda_star_num=' + str(lambda_star.numerator))
print('lambda_star_den=' + str(lambda_star.denominator))
print('Q_num=' + str(Q.numerator))
print('Q_den=' + str(Q.denominator))
print('RESIDUE_INVERSE_CHECK=PASS')
print('D_STAR_STRICTLY_BEATS_D_C=PASS')
print('TWO_STEP_SPECTRAL_MAJORANT_STRICTLY_IMPROVES=PASS')
print('EXACT_LOG_SEPARATOR_PASS')
print('SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS')
print('ALL_EXACT_CHECKS_PASS')
