from fractions import Fraction

m = 8  # 2d in d=4
Q = Fraction(1,4)
R = Fraction(1,4)
alpha = [Q] + [Fraction(0)]*(m-1)
beta  = [R] + [Fraction(0)]*(m-1)

mean_a = sum(alpha, Fraction(0))/m
mean_b = sum(beta, Fraction(0))/m
mean_ab = sum((a*b for a,b in zip(alpha,beta)), Fraction(0))/m
cov = mean_ab - mean_a*mean_b
pair = sum((alpha[i]-alpha[j])*(beta[i]-beta[j]) for i in range(m) for j in range(m)) / (2*m*m)

assert cov == Fraction(7,1024)
assert pair == cov
assert all(Fraction(0) <= a <= Q for a in alpha)
assert all(Fraction(0) <= b <= R for b in beta)
assert max([Q]*m)-min([Q]*m) == 0
assert max([R]*m)-min([R]*m) == 0
factor = Fraction(1,1) + cov / ((1-mean_a)*(1-mean_b))
assert factor == Fraction(968,961)

print(f"m={m}")
print(f"mean_alpha={mean_a}")
print(f"mean_beta={mean_b}")
print(f"covariance={cov}")
print(f"pairwise_identity={pair}")
print("envelope_oscillation_alpha=0")
print("envelope_oscillation_beta=0")
print(f"normalized_factor={factor}")
print("ALL EXACT ASSERTIONS PASSED")
