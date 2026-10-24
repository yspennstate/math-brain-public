from fractions import Fraction

# Exact Gaussian-rational arithmetic. This is a self-check for the finite core of
# P01-P74, not a substitute for the operator-K-theory proof in the run report.
class G:
    def __init__(self, re=0, im=0):
        self.re = Fraction(re)
        self.im = Fraction(im)
    def __add__(self, other):
        other = other if isinstance(other, G) else G(other)
        return G(self.re + other.re, self.im + other.im)
    def __sub__(self, other):
        other = other if isinstance(other, G) else G(other)
        return G(self.re - other.re, self.im - other.im)
    def __mul__(self, other):
        other = other if isinstance(other, G) else G(other)
        return G(self.re*other.re - self.im*other.im,
                 self.re*other.im + self.im*other.re)
    def conj(self):
        return G(self.re, -self.im)
    def norm2(self):
        return self.re*self.re + self.im*self.im
    def __eq__(self, other):
        other = other if isinstance(other, G) else G(other)
        return self.re == other.re and self.im == other.im
    def __repr__(self):
        return f"({self.re}+{self.im}i)"

# r=(1-e)+ie for e=(1+a)/2 in C[C2], a^2=1.
c0 = G(Fraction(1, 2), Fraction(1, 2))
c1 = G(Fraction(-1, 2), Fraction(1, 2))
id_coeff = c0.conj()*c0 + c1.conj()*c1
a_coeff = c0.conj()*c1 + c1.conj()*c0
assert id_coeff == 1
assert a_coeff == 0
assert c0.norm2() == Fraction(1, 2)
assert c1.norm2() == Fraction(1, 2)

# For U=R(r u_s1) diag(u_s1^2,u_s2^-1), the two upper-right terms have
# quotient exponent vector (1,-1), and the two lower-left terms have (1,0).
weights = [
    (c0.norm2(), (1, -1)),
    (c1.norm2(), (1, -1)),
    (c0.norm2(), (1, 0)),
    (c1.norm2(), (1, 0)),
]
k1 = sum(w*e[0] for w, e in weights)
k2 = sum(w*e[1] for w, e in weights)
assert k1 == 2
assert k2 == -1

# Exact abstract matrix check for R(v)=[[0,v],[v*,0]] and D=diag(x,y).
# Free-group words are tuples of signed generator numbers.
def reduce_word(word):
    st = []
    for a in word:
        if st and st[-1] == -a:
            st.pop()
        else:
            st.append(a)
    return tuple(st)

def inv_word(word):
    return tuple(-a for a in reversed(word))

def gr_add(A, B):
    C = dict(A)
    for w, c in B.items():
        C[w] = C.get(w, 0) + c
        if C[w] == 0:
            del C[w]
    return C

def gr_mul(A, B):
    C = {}
    for w, a in A.items():
        for z, b in B.items():
            rz = reduce_word(w + z)
            C[rz] = C.get(rz, 0) + a*b
    return {w: c for w, c in C.items() if c}

def gr_star(A):
    return {inv_word(w): c for w, c in A.items()}

ZERO = {}
ONE = {(): 1}
def atom(i):
    return {(i,): 1}

def sum_gr(lst):
    out = {}
    for A in lst:
        out = gr_add(out, A)
    return out

def mat_mul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    return [[sum_gr([gr_mul(A[i][r], B[r][j]) for r in range(k)])
             for j in range(m)] for i in range(n)]

def mat_star(A):
    n, m = len(A), len(A[0])
    return [[gr_star(A[j][i]) for j in range(n)] for i in range(m)]

def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]

v = atom(1)
V = gr_star(v)
x = atom(2)
y = atom(3)
R = [[ZERO, v], [V, ZERO]]
D = [[x, ZERO], [ZERO, y]]
assert mat_star(R) == R
assert mat_mul(R, R) == eye(2)
assert mat_mul(mat_star(D), D) == eye(2)
U = mat_mul(R, D)
assert mat_mul(mat_star(U), U) == eye(2)
assert mat_mul(U, mat_star(U)) == eye(2)

print("P01 P74 exact self-check")
print("r*r coefficients in C[C2]: identity =", id_coeff, ", a =", a_coeff)
print("|c0|^2 =", c0.norm2(), "; |c1|^2 =", c1.norm2())
print("explicit matrix-unitary coordinate =", (k1, k2))
print("abstract R*=R, R^2=I, D*=D^{-1}, U*=U^{-1}: PASS")
print("ALL ASSERTIONS PASSED")
