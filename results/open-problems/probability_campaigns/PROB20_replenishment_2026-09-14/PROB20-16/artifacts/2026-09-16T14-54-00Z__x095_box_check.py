from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F

P = 80
EPS_DEC = Decimal('1e-9')
EPS_RAT = F(1, 10**9)

# Directed Decimal interval arithmetic.
def _down(fn):
    with localcontext() as c:
        c.prec = P
        c.rounding = ROUND_FLOOR
        return +fn()

def _up(fn):
    with localcontext() as c:
        c.prec = P
        c.rounding = ROUND_CEILING
        return +fn()

class IV:
    __slots__ = ('lo','hi')
    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo, Decimal) else Decimal(str(lo))
        self.hi = self.lo if hi is None else (hi if isinstance(hi, Decimal) else Decimal(str(hi)))
        if self.lo > self.hi:
            raise ValueError((self.lo,self.hi))
    def __add__(self, other):
        o=toiv(other)
        return IV(_down(lambda:self.lo+o.lo), _up(lambda:self.hi+o.hi))
    __radd__=__add__
    def __neg__(self):
        return IV(-self.hi,-self.lo)
    def __sub__(self, other):
        return self + (-toiv(other))
    def __rsub__(self, other):
        return toiv(other)-self
    def __mul__(self, other):
        o=toiv(other)
        pairs=((self.lo,o.lo),(self.lo,o.hi),(self.hi,o.lo),(self.hi,o.hi))
        lows=[_down(lambda a=a,b=b:a*b) for a,b in pairs]
        highs=[_up(lambda a=a,b=b:a*b) for a,b in pairs]
        return IV(min(lows),max(highs))
    __rmul__=__mul__
    def inv(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError((self.lo,self.hi))
        vals_lo=[_down(lambda x=x:Decimal(1)/x) for x in (self.lo,self.hi)]
        vals_hi=[_up(lambda x=x:Decimal(1)/x) for x in (self.lo,self.hi)]
        return IV(min(vals_lo),max(vals_hi))
    def __truediv__(self, other):
        return self*toiv(other).inv()
    def __rtruediv__(self, other):
        return toiv(other)/self
    def contains_zero(self):
        return self.lo <= 0 <= self.hi
    def __repr__(self):
        return f'[{self.lo},{self.hi}]'

def toiv(x):
    return x if isinstance(x,IV) else IV(x)

class CIV:
    __slots__=('re','im')
    def __init__(self,re=0,im=0):
        self.re=toiv(re); self.im=toiv(im)
    def __add__(self,o):
        o=tociv(o); return CIV(self.re+o.re,self.im+o.im)
    __radd__=__add__
    def __neg__(self): return CIV(-self.re,-self.im)
    def __sub__(self,o): return self+(-tociv(o))
    def __rsub__(self,o): return tociv(o)-self
    def __mul__(self,o):
        o=tociv(o)
        return CIV(self.re*o.re-self.im*o.im, self.re*o.im+self.im*o.re)
    __rmul__=__mul__
    def conj(self): return CIV(self.re,-self.im)

def tociv(x):
    if isinstance(x,CIV): return x
    if isinstance(x,IV): return CIV(x,0)
    return CIV(x,0)

def det_dp(A):
    n=len(A)
    zero = CIV() if isinstance(A[0][0], CIV) else IV(0)
    one = CIV(1,0) if isinstance(A[0][0], CIV) else IV(1)
    dp={0:one}
    for i in range(n):
        nd={}
        for mask,val in dp.items():
            for j in range(n):
                if (mask>>j)&1: continue
                inv = (mask >> (j+1)).bit_count()
                term = val*A[i][j]
                if inv & 1: term = -term
                nm=mask|(1<<j)
                nd[nm] = nd.get(nm,zero) + term
        dp=nd
    return dp[(1<<n)-1]

def matmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    iscomplex=isinstance(A[0][0],CIV) or isinstance(B[0][0],CIV)
    z=CIV() if iscomplex else IV(0)
    return [[sum((A[i][r]*B[r][j] for r in range(k)), z) for j in range(m)] for i in range(n)]

def trace(A):
    z=CIV() if isinstance(A[0][0],CIV) else IV(0)
    return sum((A[i][i] for i in range(len(A))), z)

def minor2_det(A, rows, cols):
    return A[rows[0]][cols[0]]*A[rows[1]][cols[1]] - A[rows[0]][cols[1]]*A[rows[1]][cols[0]]

def adj3(A):
    out=[[CIV() for _ in range(3)] for __ in range(3)]
    for i in range(3):
        for j in range(3):
            rows=[r for r in range(3) if r!=j]
            cols=[c for c in range(3) if c!=i]
            cof=minor2_det(A,rows,cols)
            if (i+j)&1: cof=-cof
            out[i][j]=cof
    return out

def ln_bound(x, lower):
    # Decimal.ln is correctly rounded. Evaluate at P+30 digits, add a much
    # larger 1e-(P+10) outward guard, then round outward to P digits.
    with localcontext() as c:
        c.prec=P+30
        y=x.ln()
        guard=Decimal(1).scaleb(-(P+10))
        y=y-guard if lower else y+guard
    with localcontext() as c:
        c.prec=P
        c.rounding=ROUND_FLOOR if lower else ROUND_CEILING
        return +y

def log_iv(x):
    x=toiv(x)
    if x.lo<=0: raise ValueError(('log domain',x))
    return IV(ln_bound(x.lo,True),ln_bound(x.hi,False))

def D(q):
    return Decimal(q.numerator)/Decimal(q.denominator)

def box(q):
    qd=D(q)
    return IV(_down(lambda:qd-EPS_DEC),_up(lambda:qd+EPS_DEC))

# Center J=I-K from the prior exact rational witness.
Jrat=[
    [(F(6102,10000),F(0)), (F(2921,10000),F(1627,10000)), (F(-521,10000),F(3138,10000))],
    [(F(2921,10000),F(-1627,10000)), (F(5485,10000),F(0)), (F(975,10000),F(-809,10000))],
    [(F(-521,10000),F(-3138,10000)), (F(975,10000),F(809,10000)), (F(3343,10000),F(0))],
]

# Exact central strictness via Sylvester plus lambda_min >= 4 det/(tr)^2.
leadJ=[F(3051,5000),F(222901,10**6),F(7471243,10**12)]
leadK=[F(1949,5000),F(64201,10**6),F(11028757,10**12)]
assert all(x>0 for x in leadJ+leadK)
detJ=leadJ[-1]; trJ=F(14930,10000)
detK=leadK[-1]; trK=F(15070,10000)
center_lower_J=4*detJ/(trJ*trJ)
center_lower_K=4*detK/(trK*trK)
assert center_lower_J > F(1,100000)
assert center_lower_K > F(1,100000)
# For 9 independent Hermitian coordinates, ||Delta||_F^2 <= 15 eps^2,
# hence ||Delta||_op < 4 eps.
assert F(1,100000)-4*EPS_RAT > 0

J=[[None]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        re,im=Jrat[i][j]
        if i==j:
            J[i][j]=CIV(box(re),IV(0))
        elif i<j:
            J[i][j]=CIV(box(re),box(im))
        else:
            J[i][j]=J[j][i].conj()

for i,j in ((0,1),(0,2),(1,2)):
    assert not (J[i][j].re.contains_zero() and J[i][j].im.contains_zero())

def shifted(mask):
    Q=[[CIV(J[i][j].re,J[i][j].im) for j in range(3)] for i in range(3)]
    for i in range(3):
        if not ((mask>>i)&1):
            Q[i][i]=Q[i][i]-1
    return Q

atoms=[]; Qs=[]
for mask in range(8):
    Q=shifted(mask); Qs.append(Q)
    z=det_dp(Q)
    if (3-mask.bit_count())&1: z=-z
    assert z.im.contains_zero()
    atoms.append(z.re)

min_atom_lower=min(x.lo for x in atoms)
assert min_atom_lower>0
p=atoms
c1=log_iv(p[2]*p[4]/(p[0]*p[6]))
c2=log_iv(p[1]*p[4]/(p[0]*p[5]))
c3=log_iv(p[1]*p[2]/(p[0]*p[3]))
tau=log_iv(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
c=[c1,c2,c3]

M=[[CIV() for _ in range(3)] for __ in range(3)]
for i in range(3):
    for j in range(3):
        M[i][j]=J[i][j]*tau
    M[i][i]=M[i][i]+c[i]
dz=det_dp(M)
assert dz.im.contains_zero()
d=dz.re
assert d.lo>0

Es=[]
for mask in range(1,8):
    E=adj3(Qs[mask])
    if (3-mask.bit_count())&1:
        E=[[-x for x in row] for row in E]
    Es.append(E)

pp=p[1:]
V=[[None]*7 for _ in range(7)]
for i in range(7):
    for j in range(7):
        V[i][j]=(pp[i] if i==j else IV(0))-pp[i]*pp[j]

ME=[matmul(M,E) for E in Es]
v=[]
for a in range(7):
    z=trace(ME[a]); assert z.im.contains_zero(); v.append(z.re)
T=[[None]*7 for _ in range(7)]
for a in range(7):
    for b in range(7):
        z=trace(matmul(ME[a],ME[b])); assert z.im.contains_zero(); T[a][b]=z.re
C=[[T[i][j]+d*V[i][j] for j in range(7)] for i in range(7)]

detC=det_dp(C)
assert detC.lo>0
Aug=[[None]*8 for _ in range(8)]
for i in range(7):
    for j in range(7): Aug[i][j]=C[i][j]
    Aug[i][7]=v[i]
for j in range(7): Aug[7][j]=v[j]
Aug[7][7]=IV(2)
detAug=det_dp(Aug)
Phi=-detAug
assert Phi.lo>0

print('status=PASS')
print('box_center=J=I-K from PROB20-16 2026-09-16T12-48-11Z witness')
print('independent_coordinates=9 real Hermitian coordinates')
print('coordinate_radius_eps=',EPS_DEC)
print('exact_leading_minors_J=',leadJ)
print('exact_leading_minors_I_minus_J=',leadK)
print('center_lambda_lower_J_exact=',center_lower_J,'approx=',float(center_lower_J))
print('center_lambda_lower_I_minus_J_exact=',center_lower_K,'approx=',float(center_lower_K))
print('uniform_box_spectral_margin_gt=',float(F(1,100000)-4*EPS_RAT))
print('min_atom_lower=',min_atom_lower)
print('c1_interval=',c1)
print('c2_interval=',c2)
print('c3_interval=',c3)
print('tau_interval=',tau)
print('detM_interval=',d)
print('detC_interval=',detC)
print('Phi_interval=',Phi)
print('CERTIFIED_PHI_LOWER_ON_BOX=',Phi.lo)
print('global_Phi_lower_bound=UNMEASURED')
