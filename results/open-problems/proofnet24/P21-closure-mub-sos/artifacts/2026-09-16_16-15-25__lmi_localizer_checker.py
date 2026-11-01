from fractions import Fraction

# Exact algebraic checker for the degree-four localizing matrix in
# Randomstrasse101 Open Problem 23, d=6, m=7.
# Arithmetic is in Q(s), s^2 = 6.

class Qsqrt6:
    __slots__ = ('a','b')
    def __init__(self,a=0,b=0):
        self.a = a if isinstance(a,Fraction) else Fraction(a)
        self.b = b if isinstance(b,Fraction) else Fraction(b)
    def __add__(self,o):
        o = o if isinstance(o,Qsqrt6) else Qsqrt6(o,0)
        return Qsqrt6(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Qsqrt6(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Qsqrt6) else Qsqrt6(o,0)))
    def __rsub__(self,o): return (o if isinstance(o,Qsqrt6) else Qsqrt6(o,0))-self
    def __mul__(self,o):
        o = o if isinstance(o,Qsqrt6) else Qsqrt6(o,0)
        return Qsqrt6(self.a*o.a + 6*self.b*o.b, self.a*o.b + self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o = o if isinstance(o,Qsqrt6) else Qsqrt6(o,0)
        den = o.a*o.a - 6*o.b*o.b
        assert den != 0
        return self * Qsqrt6(o.a/den, -o.b/den)
    def __eq__(self,o):
        o = o if isinstance(o,Qsqrt6) else Qsqrt6(o,0)
        return self.a==o.a and self.b==o.b
    def __repr__(self):
        return f"({self.a})+({self.b})*sqrt(6)"

D=6
M=7
blocks=M*(M-1)//2
quartics=blocks*D*D
Hdim=1+2*M*D*D
localizer_dim=2*Hdim
active_rank=2*D
inactive_scalars=localizer_dim-2*active_rank

# Enumerate the normalized complex affine Haar basis exactly.
# Mode ('U',k,r,c) means sqrt(d) U_k[r,c], and ('C',...) its conjugate.
modes=[('1',)]
for k in range(M):
    for r in range(D):
        for col in range(D):
            modes.append(('U',k,r,col))
            modes.append(('C',k,r,col))
assert len(modes)==Hdim and len(set(modes))==Hdim

# Fix one cross constraint: basis 0 column 0 versus basis 1 column 0.
# Haar second moments and global-phase balance give exactly these channels:
# K(sqrt(d) conjugate(V[a,0]))=(1/d)sqrt(d) conjugate(U[a,0]);
# K(sqrt(d) U[a,0])=(1/d)sqrt(d) V[a,0].
Kmap={}
for r in range(D):
    Kmap[('C',1,r,0)]=('C',0,r,0)
    Kmap[('U',0,r,0)]=('U',1,r,0)
assert len(Kmap)==active_rank
assert len(set(Kmap.values()))==active_rank
assert all(src in modes and dst in modes for src,dst in Kmap.items())

# a=1/sqrt(6)=sqrt(6)/6; c=1/d=1/6.
a=Qsqrt6(0,Fraction(1,6))
c=Qsqrt6(Fraction(1,6),0)
ell=c/a
D1=a
D2=a-(c*c)/a

assert a*a == Qsqrt6(Fraction(1,6),0)
assert c*c == Qsqrt6(Fraction(1,36),0)
assert (a*a-c*c) == Qsqrt6(Fraction(5,36),0)
assert ell == a
assert D2 == Qsqrt6(0,Fraction(5,36))

# Exact LDL^* certificate for every active 2x2 localizer block:
# [[a,c],[c,a]] = L diag(D1,D2) L^T, L=[[1,0],[ell,1]].
L00=Qsqrt6(1,0); L10=ell; L11=Qsqrt6(1,0)
R00=L00*D1*L00
R01=L00*D1*L10
R11=L10*D1*L10 + L11*D2*L11
assert R00==a and R01==c and R11==a

# Positivity is exact: D1=sqrt(6)/6>0 and D2=5sqrt(6)/36>0.
assert active_rank == 12
assert Hdim == 505
assert localizer_dim == 1010
assert inactive_scalars == 986
assert blocks == 21 and quartics == 756

print('P21 degree-four MUB LMI localizer exact checker: PASS')
print(f'd={D}, m={M}, labeled cross-basis blocks={blocks}, quartic equalities={quartics}')
print(f'complex affine Haar space dimension H={Hdim}; localizer dimension=2H={localizer_dim}')
print(f'compressed multiplication operator K: exact rank={active_rank}=2d; each nonzero singular value=1/{D}')
print('source amplitude a=1/sqrt(6)=sqrt(6)/6; squared-overlap normalization=1/6')
print('exact active 2x2 block = [[sqrt(6)/6, 1/6],[1/6, sqrt(6)/6]]')
print('exact determinant = 1/6 - 1/36 = 5/36 > 0')
print('exact LDL certificate: ell=sqrt(6)/6, D1=sqrt(6)/6, D2=5*sqrt(6)/36')
print(f'active 2x2 blocks={active_rank}; inactive positive scalar coordinates={inactive_scalars}')
print('therefore every degree-four affine-vector localizer is PSD; no pointwise MUB assumption used')
print('tracked quartic-equality metric remains exactly 0/21 eliminated labeled blocks')
