from fractions import Fraction as F

N = 1024

# Coefficient in the six-mass l1 perturbation after division by m|s|.
l1_coeff = F(4,1) + F(8,N) + F(1,56) + F(4, N*224*224)
assert l1_coeff < 5

# Near-center entropy derivative bound used to upgrade |Gamma'|<66 to |B'|<67.
center_hprime = F(76,512)
assert center_hprime < 1

# Smooth selector-perturbation debit, divided by m.
smooth = F(67,N) + F(164, N*224)

# Fannes debit, divided by m, after log2(e)<3/2 and m log2(1/m)<=1.
entropy = F(5,2) * F(29,2) / N

total = smooth + entropy
remaining = F(13,100) - total

assert total == F(5823,57344)
assert total < F(51,500)          # < 0.102
assert remaining == F(40793,1433600)
assert remaining > F(7,250)

print('PASS=True')
print('N=', N)
print('l1_coeff_upper=', l1_coeff, float(l1_coeff))
print('center_hprime_upper=', center_hprime, float(center_hprime))
print('smooth_ratio_upper=', smooth, float(smooth))
print('entropy_ratio_upper=', entropy, float(entropy))
print('total_ratio_upper=', total, float(total))
print('remaining_ratio_lower=', remaining, float(remaining))
print('claimed_final_floor=', F(7,250), float(F(7,250)))
