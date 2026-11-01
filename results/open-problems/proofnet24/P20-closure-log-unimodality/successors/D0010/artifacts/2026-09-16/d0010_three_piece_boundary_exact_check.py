from fractions import Fraction as Q

# Exact finite algebra for the D0010 three-piece boundary family.
# Family:
#   f_c = 15c-3       on [0,1/6)
#         9-21c       on [1/6,1/3)
#         3c/2        on [1/3,1]
# with c in [1/4,2/5].

def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mul(q,x): return (q*x[0], q*x[1])
def sub(x,y): return (x[0]-y[0], x[1]-y[1])
def val(x,c): return x[0]+x[1]*c

h1=(Q(-3),Q(15))
h2=(Q(9),Q(-21))
h3=(Q(0),Q(3,2))

# Integral and first moment as affine functions of c.
norm = add(add(mul(Q(1,6),h1), mul(Q(1,6),h2)), mul(Q(2,3),h3))
mean = add(add(mul(Q(1,72),h1), mul(Q(1,24),h2)), mul(Q(4,9),h3))
assert norm == (Q(1),Q(0))
assert mean == (Q(1,3),Q(0))

left=(Q(1,4),Q(1,3))
right=(Q(1,3),Q(2,5))

# On [1/4,1/3], middle plateau is the mode.
for c in left:
    assert val(h1,c) >= 0 and val(h2,c) >= 0 and val(h3,c) >= 0
    assert val(sub(h2,h1),c) >= 0
    assert val(sub(h2,h3),c) >= 0

# On [1/3,2/5], the density is monotone decreasing.
for c in right:
    assert val(h1,c) >= 0 and val(h2,c) >= 0 and val(h3,c) >= 0
    assert val(sub(h1,h2),c) >= 0
    assert val(sub(h2,h3),c) >= 0

# Tail mass above 1/3 is exactly c (the endpoint has zero mass).
tail = mul(Q(2,3),h3)
assert tail == (Q(0),Q(1))

# Exact transition identities.
assert val(sub(h2,h1), Q(1,3)) == 0
assert val(sub(h2,h3), Q(2,5)) == 0
assert val(h1,Q(1,4)) == Q(3,4)

print("D0010 three-piece exact algebra: PASS")
print("normalization affine pair =", norm)
print("mean affine pair =", mean)
print("tail P(X>1/3) affine pair =", tail)
print("c interval =", (Q(1,4),Q(2,5)))
print("non-CM side = [1/4,1/3)")
print("CM side = [1/3,2/5]")
print("transition h2-h1 at c=1/3 =", val(sub(h2,h1),Q(1,3)))
print("right endpoint h2-h3 at c=2/5 =", val(sub(h2,h3),Q(2,5)))
print("ALL_EXACT_CHECKS_PASS")
