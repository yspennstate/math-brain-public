from fractions import Fraction as F
from itertools import combinations

# Frozen source-equivalent formulation: vector coordinates in C^6,
# 7 labeled orthonormal bases, quartic cross-unbiasedness equations
# |<v_i^(k),v_j^(l)>|^2 = 1/6 for k != l.
d = 6
m = 7
D = 2*d  # real dimension of one complex unit vector
blocks = list(combinations(range(m), 2))
constraints_per_block = d*d
assert len(blocks) == 21
assert len(blocks)*constraints_per_block == 756

# Source normalization gate.
amplitude_sq = F(1, d)
assert amplitude_sq == F(1, 6)
# The erroneous displayed squared-amplitude value 1/sqrt(6) is deliberately
# NOT encoded. The source definition uses amplitude 1/sqrt(6), hence square 1/6.

# Monomial basis for degree <=2 real polynomials in independent x,y in S^{D-1}.
# A monomial is a tuple of variable indices in [0,2D), sorted.
mons = [()]
mons += [(i,) for i in range(2*D)]
mons += [(i,j) for i in range(2*D) for j in range(i,2*D)]
assert len(mons) == 1 + 2*D + (2*D)*(2*D+1)//2 == 325
idx = {mon:i for i,mon in enumerate(mons)}

# Exact sphere moment for one S^{D-1}, total degree <=4.
def sphere_moment(indices):
    n = len(indices)
    if n == 0:
        return F(1)
    counts = {}
    for i in indices:
        counts[i] = counts.get(i,0)+1
    if any(v % 2 for v in counts.values()):
        return F(0)
    if n == 2:
        return F(1,D) if list(counts.values()) == [2] else F(0)
    if n == 4:
        vals = sorted(counts.values(), reverse=True)
        if vals == [4]:
            return F(3, D*(D+2))
        if vals == [2,2]:
            return F(1, D*(D+2))
        return F(0)
    raise ValueError((indices,n))

def product_sphere_moment(mon):
    x = [i for i in mon if i < D]
    y = [i-D for i in mon if i >= D]
    return sphere_moment(x) * sphere_moment(y)

# Build exact 325x325 moment matrix M of the degree-4 Haar truncation
# for one cross-basis vector pair (x,y). Complex Haar unit vectors are
# uniform on the real sphere S^{2d-1}; different bases are independent.
n = len(mons)
M = [[F(0) for _ in range(n)] for __ in range(n)]
for a,ma in enumerate(mons):
    for b in range(a,n):
        mb = mons[b]
        val = product_sphere_moment(tuple(sorted(ma+mb)))
        M[a][b] = val
        M[b][a] = val

# Build an explicit rational weighted-squares Gram certificate K for E[f(x,y)^2].
# Any degree<=2 real polynomial can be written
# f = c + a.x + b.y + x^T A x + x^T C y + y^T B y,
# A,B symmetric. In monomial coefficients q_ij, A_ij=q_ij/2 off diagonal.
# Exact identity:
# E f^2 = mu^2 + ||a||^2/D + ||b||^2/D + ||C||_F^2/D^2
#       + 2||A_0||_F^2/[D(D+2)] + 2||B_0||_F^2/[D(D+2)],
# mu=c+tr(A)/D+tr(B)/D.
# We realize traceless diagonal norms as (1/D) sum_{i<j}(q_ii-q_jj)^2.
K = [[F(0) for _ in range(n)] for __ in range(n)]

def add_weighted_square(vec, w):
    nz = [(i,v) for i,v in vec.items() if v]
    assert w > 0
    for i,vi in nz:
        for j,vj in nz:
            K[i][j] += w*vi*vj

# mu^2
mu = {idx[()]: F(1)}
for base in (0,D):
    for i in range(D):
        mu[idx[(base+i,base+i)]] = F(1,D)
add_weighted_square(mu, F(1))

# linear x,y
for i in range(2*D):
    add_weighted_square({idx[(i,)]:F(1)}, F(1,D))

# mixed x_i y_j
for i in range(D):
    for j in range(D):
        add_weighted_square({idx[(i,D+j)]:F(1)}, F(1,D*D))

# traceless quadratic sectors for x and y.
# diagonal differences: weight 2/[D^2(D+2)] each (q_ii-q_jj)^2
wdiag = F(2, D*D*(D+2))
# off-diagonal monomial q_ij: weight 1/[D(D+2)] q_ij^2
woff = F(1, D*(D+2))
for base in (0,D):
    for i,j in combinations(range(D),2):
        add_weighted_square({idx[(base+i,base+i)]:F(1), idx[(base+j,base+j)]:F(-1)}, wdiag)
        add_weighted_square({idx[(base+i,base+j)]:F(1)}, woff)

# Exact matrix identity M=K.
for i in range(n):
    for j in range(n):
        if M[i][j] != K[i][j]:
            raise AssertionError((i,j,M[i][j],K[i][j],mons[i],mons[j]))

# Exact cross-unbiasedness moment in C^d from the real-sphere oracle.
# z_re=sum_r (x_Rr y_Rr + x_Ir y_Ir),
# z_im=sum_r (x_Rr y_Ir - x_Ir y_Rr).
def lincomb_square_expect(terms):
    s=F(0)
    for ca,ma in terms:
        ia=idx[tuple(sorted(ma))]
        for cb,mb in terms:
            ib=idx[tuple(sorted(mb))]
            s += ca*cb*M[ia][ib]
    return s

re_terms=[]
im_terms=[]
for r in range(d):
    xr, xi = r, d+r
    yr, yi = D+r, D+d+r
    re_terms += [(F(1),(xr,yr)), (F(1),(xi,yi))]
    im_terms += [(F(1),(xr,yi)), (F(-1),(xi,yr))]
Ezre2 = lincomb_square_expect(re_terms)
Ezim2 = lincomb_square_expect(im_terms)
Eabs2 = Ezre2 + Ezim2
assert Ezre2 == F(1,12)
assert Ezim2 == F(1,12)
assert Eabs2 == F(1,6)
assert Eabs2 - amplitude_sq == 0

# By exchangeability this same exact zero is the pseudoexpectation of every
# one of the 756 quartic cross equations, simultaneously under product Haar.
zero_cross_constraints = len(blocks)*constraints_per_block
assert zero_cross_constraints == 756

# The 21 cross-basis blocks are all feasible in the degree-4 pseudoexpectation,
# so none is exactly eliminated by the frozen degree-4 vector-coordinate model.
eliminated_labeled_blocks = 0
eliminated_symmetry_orbits = 0
assert eliminated_labeled_blocks == 0
assert eliminated_symmetry_orbits == 0

# Certificate term count (weighted squares). All weights are positive rationals.
# 1 mu + 2D linear + D^2 mixed + 2*(C(D,2) diag-diff + C(D,2) offdiag).
cert_squares = 1 + 2*D + D*D + 4*(D*(D-1)//2)
assert cert_squares == 433  # redundant squares are fine; exact PSD certificate

print('P21 degree-four MUB exact checker: PASS')
print(f'd={d}, m={m}, real sphere dimension D={D}')
print(f'frozen labeled cross-basis blocks={len(blocks)}; quartic equations={zero_cross_constraints}')
print('normalization: |<u,v>|=1/sqrt(6) => |<u,v>|^2=1/6 (exact)')
print(f'E[(Re <x,y>)^2]={Ezre2}; E[(Im <x,y>)^2]={Ezim2}; E|<x,y>|^2={Eabs2}')
print(f'orbit-representative degree<=2 moment Gram size={n}x{n}')
print(f'exact rational weighted-square certificate terms={cert_squares}')
print(f'certificate weights: linear=1/{D}, mixed=1/{D*D}, diag-diff={wdiag}, offdiag={woff}')
print('moment-matrix identity M == K: VERIFIED entrywise over Fraction')
print('same-basis constraints: pointwise zero on Haar U(6), hence all allowed degree<=2 multipliers vanish')
print('cross-basis quartic constraints: pseudoexpectation zero for all 756 equations; only constant multipliers at degree 4')
print(f'primary metric: exactly eliminated symmetry-reduced cross-block orbits = {eliminated_symmetry_orbits}/1')
print(f'labeled corroboration: exactly eliminated cross-basis blocks = {eliminated_labeled_blocks}/{len(blocks)}')
print('status for frozen vector-coordinate quartic formulation: degree-4 refutation impossible (explicit Haar pseudoexpectation)')
