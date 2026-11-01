from fractions import Fraction

p=256717
q=800000
d=q-p
a=int('1995237757733917147310102692686664915858011319606812684127301')
b=4_220_452_010_631_561_279
M=5_000_000_000_000_000_000
alpha=a % b
h=707_440_146_652_911_839
vstar=h+b
assert (alpha*h) % b == 1
assert vstar <= M < 2*b
S=q**6*d
c=[q**(6-k)*d*p**k for k in range(7)] + [p**7]
c7=c[7]
assert c7 == min(c)
D_floor=a//vstar
D_rem=a%vstar
assert D_rem != 0
D_star=Fraction(a,vstar)
D_new=D_floor + 1500*c7 + 1
assert Fraction(D_new,1) > D_star

# Non-tight rows.  The companion exact semigroup checker proves that in the
# only extremal residue case s=1,V=vstar, T=B s is > 5000*c7.
assert Fraction(2*a,M) > D_new
assert Fraction(a,h) > D_new
extremal_defect_floor = D_star + Fraction(b*5000*c7,vstar)
assert extremal_defect_floor > D_new

# Tight rows.  The companion exact four-band checker proves no admissible
# congruent relaxed T <= D_new-1, hence every actual tight row has T>=D_new.
R=Fraction(a,b)
t=Fraction(p,q)
scale=t*t/S
base=4*t*t
beta_old=R-Fraction(1,2*b*vstar)
beta_new=R-Fraction(D_new,2*a*b)
assert beta_new < beta_old
assert beta_new*beta_new > R*R-Fraction(D_new,b*b)
lambda_old=scale*beta_old
lambda_new=scale*beta_new
assert 0 < base < 1
assert 0 < lambda_new < lambda_old < 1

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
Nlo,Nhi=neglog_bounds(lambda_new)
Olo,Ohi=neglog_bounds(lambda_old)
U_new_upper=Ahi/Nlo
U_old_lower=Alo/Ohi
Q=Fraction(
    82627594276228262501510658153729663282346199619319002388080618331256294443029952,
    10**80,
)
assert U_new_upper < Q < U_old_lower
L=Fraction(99083249,125000000)
assert L < U_new_upper

print('P02 T02 matched 1500-c7 two-step defect endpoint checker')
print('alpha=' + str(alpha))
print('h=' + str(h))
print('vstar=' + str(vstar))
print('c7=' + str(c7))
print('D_star_num=' + str(D_star.numerator))
print('D_star_den=' + str(D_star.denominator))
print('D_new=' + str(D_new))
print('D_new_over_D_star=' + str(Fraction(D_new,1)/D_star))
print('extremal_defect_floor_minus_Dnew=' + str(extremal_defect_floor-Fraction(D_new,1)))
print('beta_new_num=' + str(beta_new.numerator))
print('beta_new_den=' + str(beta_new.denominator))
print('lambda_new_num=' + str(lambda_new.numerator))
print('lambda_new_den=' + str(lambda_new.denominator))
print('separator_Q_num=' + str(Q.numerator))
print('separator_Q_den=' + str(Q.denominator))
print('NON_TIGHT_BRANCH_COMPARISONS=PASS')
print('D_NEW_STRICTLY_BEATS_D_STAR=PASS')
print('TWO_STEP_SPECTRAL_MAJORANT_STRICTLY_IMPROVES=PASS')
print('EXACT_LOG_SEPARATOR_PASS')
print('SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS')
print('ALL_EXACT_CHECKS_PASS')
