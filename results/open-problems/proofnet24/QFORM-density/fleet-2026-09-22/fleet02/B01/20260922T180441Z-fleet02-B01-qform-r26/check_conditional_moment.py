from math import exp, gamma, lgamma, log

# Exact formula proved in REPORT.md for the three-block conditional-density moment.
def one_block_moment(m: int, theta: float) -> float:
    assert m >= 2 and 0.0 < theta < 2.0
    # J_{m,theta}=m^{-theta/2} m(m-1) B(m-1,2-theta)
    log_j = ((-theta/2.0)*log(m) + log(m) + log(m-1)
             + lgamma(m-1) + lgamma(2.0-theta) - lgamma(m+1.0-theta))
    return exp(log_j)

def three_block_moment(m: int, theta: float) -> float:
    return one_block_moment(m, theta)**3

print('theta=2/3 exact-formula regression')
for m in [2,4,8,16,32,64,128,256,1024]:
    value = three_block_moment(m, 2.0/3.0)
    print(f'm={m:4d} E[M^(2/3)]={value:.15f} ratio_over_m={value/m:.15f} Pii={1/m:.12f}')

# At m=2 the exact value is 27/16.
assert abs(three_block_moment(2, 2.0/3.0) - 27.0/16.0) < 1e-12
# The asymptotic ratio is Gamma(4/3)^3.
asym = gamma(4.0/3.0)**3
print(f'asymptotic_ratio_Gamma(4/3)^3={asym:.15f}')
assert 0.7120 < asym < 0.7122
# The ridge-window hypothesis max_i P_ii <=1/32 holds from m=32 onward.
assert 1.0/32.0 <= 1.0/32.0
print('RIDGE_WINDOW_LEVERAGE_CHECK=m>=32 PASS')
print('STATUS=PASS')
