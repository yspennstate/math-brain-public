from fractions import Fraction


def tanh_from_exp2x(r: Fraction) -> Fraction:
    return (r - 1) / (r + 1)

# Choose h=(1/2)log 2 and J=(1/2)log(4/3).
# Then exp(2(h+2J))=32/9, exp(2h)=2, exp(2(h-2J))=9/8.
t_pp = tanh_from_exp2x(Fraction(32, 9))
t_0 = tanh_from_exp2x(Fraction(2, 1))
t_mm = tanh_from_exp2x(Fraction(9, 8))

# Walsh coefficient of x1*x3 in tanh(h+J x1+J x3).
d = (t_pp - 2*t_0 + t_mm) / 4

tanh_J = tanh_from_exp2x(Fraction(4, 3))
dobrushin_row_sum_bound = 2 * tanh_J

assert t_pp == Fraction(23, 41)
assert t_0 == Fraction(1, 3)
assert t_mm == Fraction(1, 17)
assert d == Fraction(-49, 4182)
assert d != 0
assert tanh_J == Fraction(1, 7)
assert dobrushin_row_sum_bound == Fraction(2, 7)
assert dobrushin_row_sum_bound < 1

print(f"tanh(h+2J)={t_pp}")
print(f"tanh(h)={t_0}")
print(f"tanh(h-2J)={t_mm}")
print(f"degree_2_Walsh_coefficient={d}")
print(f"tanh(J)={tanh_J}")
print(f"Dobrushin_row_sum_bound={dobrushin_row_sum_bound}")
print("EXACT_PAIRWISE_ISING_BLOCK_PASS")
