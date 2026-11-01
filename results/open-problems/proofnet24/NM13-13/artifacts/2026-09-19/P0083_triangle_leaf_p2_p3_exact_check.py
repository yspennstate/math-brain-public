from fractions import Fraction as F

# Exact polynomial arithmetic; coefficients are stored in ascending order.
def add(a,b):
    n=max(len(a),len(b)); out=[F(0) for _ in range(n)]
    for i,v in enumerate(a): out[i]+=v
    for i,v in enumerate(b): out[i]+=v
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def scale(a,c): return [c*v for v in a]
def mul(a,b):
    out=[F(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def power(a,n):
    out=[F(1)]
    for _ in range(n): out=mul(out,a)
    return out

def shift_poly(a,c):
    out=[F(0)]
    base=[c,F(1)]
    pw=[F(1)]
    for coeff in a:
        out=add(out,scale(pw,coeff))
        pw=mul(pw,base)
    return out

def assert_eq(a,b,label):
    if a!=b:
        raise AssertionError(f"{label}: {a} != {b}")

def assert_positive(a,label):
    if not all(v>0 for v in a):
        raise AssertionError(f"{label}: nonpositive coefficient in {a}")

# 1) Exact constant used in the uniform 2<=p<=3 ratio bound.
assert F(343,576) < 1

# 2) Symmetry contradiction core:
# (2x-1)(x+4/3)^3-(x+1)^4 > 0 for x>4/3.
x=[F(0),F(1)]
one=[F(1)]
poly_sym = add(
    mul(add(scale(x,F(2)),[F(-1)]), power(add(x,[F(4,3)]),3)),
    scale(power(add(x,[F(1)]),4),F(-1))
)
expected_sym=[F(-91,27),F(-124,27),F(2,3),F(3),F(1)]
assert_eq(poly_sym,expected_sym,"symmetry polynomial identity")
shifted_sym=shift_poly(poly_sym,F(4,3))
expected_shifted_sym=[F(53,27),F(68,3),F(70,3),F(25,3),F(1)]
assert_eq(shifted_sym,expected_shifted_sym,"symmetry shifted coefficients")
assert_positive(shifted_sym,"symmetry positivity")

# 3) Uniform Rayleigh lower-bound core for 2<=p<=3.
# With t=2x/(1+x),
# S=x(1+x)(1+t+t^4+t^-4)-4(1+x^2).
# After multiplying by 16*x^3*(1+x)^3, the numerator is (x-1)P(x).
x3=power(x,3); x4=power(x,4); x5=power(x,5); x8=power(x,8)
onepx=add(one,x)
left=[F(0)]
left=add(left, scale(mul(x4,power(onepx,4)),F(16)))
left=add(left, scale(mul(x5,power(onepx,3)),F(32)))
left=add(left, scale(x8,F(256)))
left=add(left, power(onepx,8))
left=add(left, scale(mul(mul(x3,power(onepx,3)),add(one,power(x,2))),F(-64)))
P=[F(-1),F(-9),F(-37),F(-29),F(77),F(181),F(217),F(241)]
right=mul([F(-1),F(1)],P)
assert_eq(left,right,"Rayleigh cleared factorization")

shifted_P=shift_poly(P,F(4,3))
expected_shifted_P=[
    F(8492737,2187),
    F(13335799,729),
    F(2962423,81),
    F(3284195,81),
    F(730739,27),
    F(32743,3),
    F(7399,3),
    F(241),
]
assert_eq(shifted_P,expected_shifted_P,"Rayleigh shifted coefficients")
assert_positive(shifted_P,"Rayleigh positivity")

print("EXACT_SELF_CHECK_PASS")
print("ratio_bound_343_over_576=", F(343,576))
print("symmetry_shift_coeffs=", shifted_sym)
print("rayleigh_shift_coeffs=", shifted_P)
