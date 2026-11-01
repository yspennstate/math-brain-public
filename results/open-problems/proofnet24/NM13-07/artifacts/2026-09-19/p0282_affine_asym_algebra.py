from fractions import Fraction as F

# Exact positive-coefficient numerator after the shift x=j-114.
COEFF = [
    30831805661390923879179,
    22360544718475629526016121,
    6887341703432624550016227600,
    1165587363898525774979509177420,
    116733611163842880528276299643760,
    6891390444932332115787218755067376,
    220754325194042945064078386485357184,
    2932446498311666301890219904268631360,
]

def poly(coeff, x):
    z = 0
    for c in coeff:
        z = z*x + c
    return z

def direct(j):
    s = j-1
    K = F(3129*j, 2000) + 1
    L = F(s,5) + 8
    U = 1/K + F(s,1)/(K*K*(K-L))
    y = K*U
    B = F(j+1,j) * ((K-y)/((K-1)*y))**2
    return B*(1-F(1,700*j))-1

def denom(j):
    return 6853448700 * j**4 * (8539041*j*j - 33096400*j - 31200000)**2

assert all(c > 0 for c in COEFF)
# The cleared numerator has degree at most 7 from the displayed rational expression.
# Eight exact values therefore certify the hard-coded polynomial identity.
for j in range(114, 122):
    x = j-114
    assert direct(j) == F(poly(COEFF, x), denom(j))
# Extra exact spot checks away from the interpolation block.
for j in (122, 137, 251, 1000):
    x = j-114
    assert direct(j) == F(poly(COEFF, x), denom(j))
    assert direct(j) > 0
print('P0282 affine asymptotic algebra certificate')
print('boundary_K=(3129/2000)j+1 cutoff_content<s/5+8')
print('identity= B(j)*(1-1/(700j))-1 = H(j-114)/D(j)')
print('H_degree=7 all_8_coefficients_strictly_positive=True')
print('D(j)=6853448700*j^4*(8539041*j^2-33096400*j-31200000)^2')
print('identity_exact_checks_j114_121_plus_122_137_251_1000=PASS')
print('ALL_EXACT_CHECKS_PASS')
