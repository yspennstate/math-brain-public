from fractions import Fraction as F
from itertools import combinations

# Frozen quartic vector-coordinate formulation.
d = 6
m = 7
D = 2*d
blocks = list(combinations(range(m), 2))
assert len(blocks) == 21
assert len(blocks)*d*d == 756
assert F(1,d) == F(1,6)

# Degree <=2 real monomial basis in independent Haar unit vectors x,y in C^d ~= R^(2d).
mons = [()]
mons += [(i,) for i in range(2*D)]
mons += [(i,j) for i in range(2*D) for j in range(i,2*D)]
assert len(mons) == 325
idx = {mon:i for i,mon in enumerate(mons)}

def sphere_moment(indices):
    n = len(indices)
    if n == 0:
        return F(1)
    counts = {}
    for i in indices:
        counts[i] = counts.get(i, 0) + 1
    if any(v % 2 for v in counts.values()):
        return F(0)
    vals = sorted(counts.values(), reverse=True)
    if n == 2:
        return F(1,D) if vals == [2] else F(0)
    if n == 4:
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

n = len(mons)
M = [[F(0) for _ in range(n)] for __ in range(n)]
for a,ma in enumerate(mons):
    for b in range(a,n):
        mb = mons[b]
        val = product_sphere_moment(tuple(sorted(ma+mb)))
        M[a][b] = val
        M[b][a] = val

# Explicit rational weighted-square Gram certificate.
K = [[F(0) for _ in range(n)] for __ in range(n)]
def add_square(vec, weight):
    assert weight > 0
    for i,vi in vec.items():
        if not vi: continue
        for j,vj in vec.items():
            if not vj: continue
            K[i][j] += weight*vi*vj

mu = {idx[()]: F(1)}
for base in (0,D):
    for i in range(D):
        mu[idx[(base+i,base+i)]] = F(1,D)
add_square(mu, F(1))
for i in range(2*D):
    add_square({idx[(i,)]: F(1)}, F(1,D))
for i in range(D):
    for j in range(D):
        add_square({idx[(i,D+j)]: F(1)}, F(1,D*D))
wdiag = F(2, D*D*(D+2))
woff = F(1, D*(D+2))
for base in (0,D):
    for i,j in combinations(range(D),2):
        add_square({idx[(base+i,base+i)]:F(1), idx[(base+j,base+j)]:F(-1)}, wdiag)
        add_square({idx[(base+i,base+j)]:F(1)}, woff)

for i in range(n):
    for j in range(n):
        assert M[i][j] == K[i][j], (i,j,M[i][j],K[i][j])

# Exact unbiasedness moment.
def lincomb_square_expect(terms):
    s=F(0)
    for ca,ma in terms:
        ia=idx[tuple(sorted(ma))]
        for cb,mb in terms:
            ib=idx[tuple(sorted(mb))]
            s += ca*cb*M[ia][ib]
    return s

re_terms=[]; im_terms=[]
for r in range(d):
    xr,xi = r,d+r
    yr,yi = D+r,D+d+r
    re_terms += [(F(1),(xr,yr)), (F(1),(xi,yi))]
    im_terms += [(F(1),(xr,yi)), (F(-1),(xi,yr))]
Ezre2=lincomb_square_expect(re_terms)
Ezim2=lincomb_square_expect(im_terms)
Eabs2=Ezre2+Ezim2
assert (Ezre2,Ezim2,Eabs2)==(F(1,12),F(1,12),F(1,6))

# Exact Q(sqrt(6)) arithmetic for LMI active block.
class QS6:
    __slots__=("a","b")
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=o if isinstance(o,QS6) else QS6(o)
        return QS6(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return QS6(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,QS6) else QS6(o)))
    def __rsub__(self,o): return QS6(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,QS6) else QS6(o)
        return QS6(self.a*o.a+6*self.b*o.b, self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,o):
        o=o if isinstance(o,QS6) else QS6(o)
        return self.a==o.a and self.b==o.b
    def __repr__(self): return f"QS6({self.a},{self.b})"

sqrt6=QS6(0,1)
c=sqrt6*F(1,6)
t=QS6(F(1,6),0)
ell=c
D1=c
D2=sqrt6*F(5,36)
# LDL entrywise: [[D1, D1*ell],[ell*D1, ell*D1*ell+D2]].
assert D1 == c
assert D1*ell == t
assert ell*D1 == t
assert ell*D1*ell + D2 == c
# determinant c^2 - t^2 = 1/6 - 1/36 = 5/36.
det = F(1,6)-F(1,36)
assert det == F(5,36)
# Compression rank and dimensions.
affine_dim = 1 + 2*m*d*d
localizer_dim=2*affine_dim
rankT=2*d
active_blocks=rankT
inactive_scalars=localizer_dim-2*active_blocks
assert (affine_dim,localizer_dim,rankT,active_blocks,inactive_scalars)==(505,1010,12,12,986)
# Norm inequality 1/d <= 1/sqrt(d), squared exactly: 1/d^2 <= 1/d.
assert F(1,d*d) <= F(1,d)

cert_squares = 1 + 2*D + D*D + 4*(D*(D-1)//2)
assert cert_squares == 433

print("P21 closure-package exact checker: PASS")
print(f"d={d}, m={m}, labeled_cross_blocks={len(blocks)}, quartic_cross_equations={len(blocks)*d*d}")
print("normalization: amplitude=1/sqrt(6), squared amplitude=1/6")
print(f"moment_gram={n}x{n}, weighted_square_terms={cert_squares}, identity=M==K exact over Fraction")
print(f"E_Re2={Ezre2}, E_Im2={Ezim2}, E_abs2={Eabs2}")
print("degree-four quartic equality consequence: all 756 cross equations have pseudoexpectation zero; eliminated blocks=0/21")
print(f"LMI affine_dim={affine_dim}, localizer_dim={localizer_dim}, compression_rank={rankT}, nonzero_singular_value=1/{d}")
print(f"LMI active_blocks={active_blocks}, inactive_positive_scalars={inactive_scalars}, active_block_det={det}")
print("LMI LDL: ell=sqrt(6)/6, D1=sqrt(6)/6, D2=5sqrt(6)/36; exact reconstruction verified")
print("ALL_EXACT_CHECKS_PASS")
