import math

# Deterministic checks for REPORT.md.

def matvec(M, x):
    return [sum(a*b for a,b in zip(row,x)) for row in M]

def max_abs(v):
    return max(abs(x) for x in v)

def residual(M, x, lam):
    y = matvec(M, x)
    return max_abs([yy-lam*xx for yy,xx in zip(y,x)])

for q in [63/64, 0.99, 1.0]:
    kappa = 1.7
    c = -2.3
    sq = math.sqrt(q)
    sp = math.sqrt(1-q)
    rt2 = math.sqrt(2)
    M = [
        [0.0, 0.0, kappa*sq, 0.0],
        [0.0, 0.0, kappa*sp, 0.0],
        [kappa*sq, kappa*sp, 0.0, 0.0],
        [0.0, 0.0, 0.0, c],
    ]
    eplus  = [sq/rt2, sp/rt2,  1/rt2, 0.0]
    eminus = [sq/rt2, sp/rt2, -1/rt2, 0.0]
    ezero  = [-sp, sq, 0.0, 0.0]
    ec     = [0.0, 0.0, 0.0, 1.0]
    assert residual(M, eplus,  kappa) < 1e-12
    assert residual(M, eminus, -kappa) < 1e-12
    assert residual(M, ezero,   0.0) < 1e-12
    assert residual(M, ec,         c) < 1e-12

# Constants in (4.6)-(4.7).
C_q1 = 2 * 12**(1/3)
C_near = C_q1 * (64/63)**(1/3)
assert abs(C_q1 - 4.5788569702133275) < 1e-12
assert abs(C_near - 4.602956661318305) < 1e-12
assert math.pi*math.sqrt(2) < C_near

# The square L^{3/2} estimate is sharp for a symmetric cap-L interval.
# For f=L on [-1/(2L),1/(2L)], h=2L on [0,1/(2L)].
for L in [0.5, 1.0, 3.0]:
    a = 2.7
    int_p_32 = 2*math.sqrt(2)*L/math.sqrt(a)
    norm_p_32 = int_p_32**(2/3)
    claimed = 2*(L**(2/3))*(a**(-1/3))
    assert abs(norm_p_32-claimed) < 1e-12

# Homogeneity check: m=3 is the unique solution of 1-1/m=2/3.
m = 3
assert abs((1-1/m) - 2/3) < 1e-15
assert abs((1/m) - 1/3) < 1e-15

print('C_q1 =', C_q1)
print('C_q>=63/64 =', C_near)
print('pi*sqrt(2) =', math.pi*math.sqrt(2))
print('QFORM_B11_L3_SQUARE_COMPILER_CHECK_PASS')
