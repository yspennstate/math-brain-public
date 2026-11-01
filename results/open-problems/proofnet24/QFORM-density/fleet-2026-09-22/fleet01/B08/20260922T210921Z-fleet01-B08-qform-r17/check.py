import math

s6=math.sqrt(6.0)
alpha=(7.0-s6)/14.0
eta=1.0/64.0
sigma=alpha-eta
c=2.0/5.0
q=5.0/4.0
gamma=c*sigma
term1=math.sqrt((1.0/7.0)/alpha)
term2=eta/gamma
ridge=(term1+term2)**2
theta=3.0/(1.0+c*c)
C=math.sqrt(math.e)/(math.sqrt(2.0*q)*gamma)*theta/(theta-2.0*q)
partner=(2.0**(4.0/3.0)+1.0)*math.sqrt(6.0)

assert sigma>0
assert theta>2*q
assert ridge<q/2
assert C<253
assert partner<8.622
# exact rational-envelope checks used in the report
assert 189000000 < 430*663**2
assert 175000 < 176022
assert 6241*8 < 10000*5

print(f"alpha={alpha:.15f}")
print(f"sigma={sigma:.15f}")
print(f"gamma={gamma:.15f}")
print(f"ridge_term1={term1:.15f}")
print(f"ridge_term2={term2:.15f}")
print(f"ridge_leverage_upper={ridge:.15f}")
print(f"q_over_2={q/2:.15f}")
print(f"theta_lower={theta:.15f}")
print(f"two_q={2*q:.15f}")
print(f"density_constant={C:.15f}")
print(f"partner_family_constant={partner:.15f}")
print("QFORM_B08_R17_CHECK_PASS")
