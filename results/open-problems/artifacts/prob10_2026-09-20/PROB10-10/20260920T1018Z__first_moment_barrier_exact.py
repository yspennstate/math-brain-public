from fractions import Fraction

# P04 width-7/length-4 rigorous axis upper cap consumed by PROB10-10.
c = Fraction(1035580351964689, 2000000000000000)

# For 0<c<1, write z=(1-c)/(1+c), so
# log(c) = -2 * atanh(z)
#        = -2 * sum_{k>=0} z^(2k+1)/(2k+1).
# For the positive tail after k=N,
# sum_{k=N+1}^infinity z^(2k+1)/(2k+1)
# <= z^(2N+3)/((2N+3)(1-z^2)).
# Therefore the expression below is a rigorous LOWER bound on log(c).
N = 8
z = (1 - c) / (1 + c)
partial = sum(z**(2*k+1) / Fraction(2*k+1) for k in range(N+1))
tail_upper = z**(2*N+3) / (Fraction(2*N+3) * (1-z*z))
logc_lower = -2 * (partial + tail_upper)

# J(c)<log 4 is algebraically equivalent to
# log(c) > c/2 - 1.
threshold = c/Fraction(2) - 1
margin = logc_lower - threshold

# Hence log 4 - J(c)
# = 2*(log(c) - c/2 + 1)
# is rigorously at least eta below.
eta = 2 * margin

print("PROB10-10 exact first-moment barrier certificate")
print("c_num =", c.numerator)
print("c_den =", c.denominator)
print("c_float =", float(c))
print("N =", N)
print("z_num =", z.numerator)
print("z_den =", z.denominator)
print("logc_lower_num =", logc_lower.numerator)
print("logc_lower_den =", logc_lower.denominator)
print("logc_lower_float =", float(logc_lower))
print("threshold_num =", threshold.numerator)
print("threshold_den =", threshold.denominator)
print("threshold_float =", float(threshold))
print("margin_num =", margin.numerator)
print("margin_den =", margin.denominator)
print("margin_float =", float(margin))
print("eta_num =", eta.numerator)
print("eta_den =", eta.denominator)
print("eta_float =", float(eta))
assert 0 < c < 1
assert 0 < z < 1
assert margin > 0
assert eta > 0
print("CERTIFIED: log(c) > c/2 - 1")
print("CERTIFIED: J(c)=c-2-2log(c/2) < log(4)")
print("CERTIFIED: log(4)-J(c) > eta > 0")
print("ALL_EXACT_CHECKS_PASS = True")
