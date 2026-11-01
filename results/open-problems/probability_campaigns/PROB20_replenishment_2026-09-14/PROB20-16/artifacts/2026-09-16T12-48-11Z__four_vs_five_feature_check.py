from fractions import Fraction as F
import math
import sympy as sp
import numpy as np

I=sp.I

# Exact rational Hermitian witness.  The theorem is applied to J=I-K because tau(J)>0.
K=sp.Matrix([
    [sp.Rational(3898,10000), sp.Rational(-2921,10000)-sp.Rational(1627,10000)*I,
     sp.Rational(521,10000)-sp.Rational(3138,10000)*I],
    [sp.Rational(-2921,10000)+sp.Rational(1627,10000)*I, sp.Rational(4515,10000),
     sp.Rational(-975,10000)+sp.Rational(809,10000)*I],
    [sp.Rational(521,10000)+sp.Rational(3138,10000)*I,
     sp.Rational(-975,10000)-sp.Rational(809,10000)*I, sp.Rational(6657,10000)]
])
J=sp.eye(3)-K

def leading_minors(M):
    return [sp.factor(M[:k,:k].det()) for k in range(1,4)]

leadK=leading_minors(K)
leadJ=leading_minors(J)
expectedK=[sp.Rational(1949,5000),sp.Rational(64201,1000000),
           sp.Rational(11028757,10**12)]
expectedJ=[sp.Rational(3051,5000),sp.Rational(222901,1000000),
           sp.Rational(7471243,10**12)]
assert leadK==expectedK and leadJ==expectedJ
assert all(x>0 for x in leadK+leadJ)  # Sylvester: 0<K<I.

def atoms_exact(M):
    out=[]
    for mask in range(8):
        Q=M.copy()
        for i in range(3):
            if not ((mask>>i)&1):
                Q[i,i]-=1
        out.append(sp.factor((-1)**(3-mask.bit_count())*Q.det()))
    return out

p=atoms_exact(J)
expected_atoms=[sp.Rational(n,10**12) for n in [
    11028757,284501461243,158293981243,222893528757,
    64189971243,102797538757,167305018757,7471243]]
assert p==expected_atoms and sum(p)==1 and all(x>0 for x in p)

loop=sp.expand(K[0,1]*K[1,2]*K[2,0])
assert sp.im(loop)==sp.Rational(316565551,25000000000) != 0

# exp(c_i) and exp(tau) for J, with complementary-pair indexing.
R1=sp.factor(p[2]*p[4]/(p[0]*p[6]))
R2=sp.factor(p[1]*p[4]/(p[0]*p[5]))
R3=sp.factor(p[1]*p[2]/(p[0]*p[3]))
Rt=sp.factor(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
assert min(R1,R2,R3,Rt)>1

# ---------- exact rational real/complex interval arithmetic ----------
class IV:
    __slots__=("lo","hi")
    def __init__(self,lo,hi=None):
        lo=F(lo); hi=lo if hi is None else F(hi)
        if lo>hi: raise ValueError((lo,hi))
        self.lo,self.hi=lo,hi
    def __add__(self,o):
        o=toiv(o); return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-toiv(o))
    def __rsub__(self,o): return toiv(o)-self
    def __mul__(self,o):
        o=toiv(o)
        z=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return IV(min(z),max(z))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError
        return IV(1/self.hi,1/self.lo)
    def __truediv__(self,o): return self*toiv(o).inv()
    def __rtruediv__(self,o): return toiv(o)/self
    def __pow__(self,n):
        if n<0: return self.inv()**(-n)
        r=IV(1); b=self
        while n:
            if n&1: r=r*b
            b=b*b; n//=2
        return r
    def width(self): return self.hi-self.lo

def toiv(x): return x if isinstance(x,IV) else IV(x)

class CIV:
    __slots__=("re","im")
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
        return CIV(self.re*o.re-self.im*o.im,
                   self.re*o.im+self.im*o.re)
    __rmul__=__mul__
    def conj(self): return CIV(self.re,-self.im)

def tociv(x):
    if isinstance(x,CIV): return x
    if isinstance(x,IV): return CIV(x,0)
    return CIV(x,0)

def sf(q):
    q=sp.Rational(q)
    return F(int(q.p),int(q.q))

def cpoint(z):
    z=sp.simplify(z)
    return CIV(sf(sp.re(z)),sf(sp.im(z)))

def mat_from_sym(M):
    return [[cpoint(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),CIV())
             for j in range(len(B[0]))] for i in range(len(A))]

def traceM(A):
    return sum((A[i][i] for i in range(len(A))),CIV())

def detM(A):
    n=len(A)
    if n==1: return A[0][0]
    out=CIV()
    for j in range(n):
        sub=[row[:j]+row[j+1:] for row in A[1:]]
        out += (1 if j%2==0 else -1)*A[0][j]*detM(sub)
    return out

def log_interval_pos(r,N=30):
    """Exact enclosure of log(r), r a positive Fraction."""
    r=F(r)
    if r<=0: raise ValueError
    s=r; m=0
    while s>=2:
        s/=2; m+=1
    while s<1:
        s*=2; m-=1
    z=(s-1)/(s+1)  # 0<=z<1/3
    part=sum((2*z**(2*k+1)/F(2*k+1) for k in range(N+1)),F(0))
    tail=2*z**(2*N+3)/(F(2*N+3)*(1-z*z))
    z2=F(1,3)
    p2=sum((2*z2**(2*k+1)/F(2*k+1) for k in range(N+1)),F(0))
    t2=2*z2**(2*N+3)/(F(2*N+3)*(1-z2*z2))
    if m>=0:
        return IV(part+m*p2,part+tail+m*(p2+t2))
    return IV(part+m*(p2+t2),part+tail+m*p2)

c=[log_interval_pos(sf(r)) for r in (R1,R2,R3)]
tau=log_interval_pos(sf(Rt))
assert tau.lo>0
assert max(x.width() for x in c+[tau]) < F(1,10**25)

Jiv=mat_from_sym(J)
M=[[CIV() for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        M[i][j]=tociv(tau)*Jiv[i][j]
    M[i][i]=M[i][i]+tociv(c[i])
delta=detM(M).re
assert delta.lo>0

# Feature covectors.  For p_empty(J)=det(I-J), derivative is -adj(I-J).
E=[]
for i in range(3):
    H=sp.zeros(3); H[i,i]=1; E.append(H)
H7=J.adjugate()
H0=-K.adjugate()

# Exact feature independence.
def col(H): return sp.Matrix(H).reshape(9,1)
assert sp.Matrix.hstack(*[col(H) for H in E+[H7]]).rank()==4
assert sp.Matrix.hstack(*[col(H) for H in E+[H0,H7]]).rank()==5

def lorentz_gram(Hs):
    Hiv=[mat_from_sym(H) for H in Hs]
    MH=[matmul(M,H) for H in Hiv]
    t=[traceM(X) for X in MH]
    n=len(Hs); C=[[IV(0) for _ in range(n)] for __ in range(n)]
    for a in range(n):
        for b in range(n):
            z=traceM(matmul(MH[a],MH[b]))-tociv(F(1,2))*t[a]*t[b]
            assert z.im.lo<=0<=z.im.hi
            C[a][b]=z.re
    return C

def feature4(mask):
    return tuple([(mask>>i)&1 for i in range(3)]+[mask==7])

def feature5(mask):
    return tuple([(mask>>i)&1 for i in range(3)]+[mask==0,mask==7])

def covariance(feat):
    vals=[feat(m) for m in range(8)]
    probs=[sf(x) for x in p]
    n=len(vals[0])
    mu=[sum((probs[m]*F(vals[m][i]) for m in range(8)),F(0)) for i in range(n)]
    return [[sum((probs[m]*F(vals[m][i])*F(vals[m][j]) for m in range(8)),F(0))
             -mu[i]*mu[j] for j in range(n)] for i in range(n)]

C4=lorentz_gram(E+[H7])
C5=lorentz_gram(E+[H0,H7])
S4=covariance(feature4)
S5=covariance(feature5)

def ratmat(S):
    return sp.Matrix([[sp.Rational(x.numerator,x.denominator) for x in row] for row in S])
assert ratmat(S4).det()>0 and ratmat(S5).det()>0

def det_real_iv(A):
    z=detM([[CIV(x,0) for x in row] for row in A])
    assert z.im.lo==0 and z.im.hi==0
    return z.re

detC4=det_real_iv(C4)
detC5=det_real_iv(C5)
assert detC4.hi<0 and detC5.hi<0  # matches inherited Lorentz inertia.

def plus_delta_sigma(C,S):
    return [[C[i][j]+delta*S[i][j] for j in range(len(C))] for i in range(len(C))]

D4=det_real_iv(plus_delta_sigma(C4,S4))
D5=det_real_iv(plus_delta_sigma(C5,S5))

# Large exact margins: universal four-feature candidate fails here,
# while the five-feature lower certificate succeeds.
assert D4.lo > F(10_000_000)
assert D5.hi < -F(1_000_000_000)

# ---------- floating-point diagnostics only ----------
def npmat(M): return np.array(M.evalf(30),dtype=complex)
Jn=npmat(J)
pn=np.array([float(x) for x in p])
cn=np.array([math.log(float(R1)),math.log(float(R2)),math.log(float(R3))])
tn=math.log(float(Rt))
Mn=np.diag(cn)+tn*Jn

def adj3(A):
    return A@A-np.trace(A)*A+0.5*(np.trace(A)**2-np.trace(A@A))*np.eye(3,dtype=complex)

def atom_grads(M):
    out=[]
    for mask in range(8):
        Q=M.copy()
        for i in range(3):
            if not ((mask>>i)&1): Q[i,i]-=1
        out.append(((-1)**(3-mask.bit_count()))*adj3(Q))
    return out
gr=atom_grads(Jn)

B=[]
for i in range(3):
    A=np.zeros((3,3),complex); A[i,i]=1; B.append(A)
s2=math.sqrt(2)
for i,j in ((0,1),(0,2),(1,2)):
    A=np.zeros((3,3),complex); A[i,j]=A[j,i]=1/s2; B.append(A)
    A=np.zeros((3,3),complex); A[i,j]=1j/s2; A[j,i]=-1j/s2; B.append(A)

def frozen(A): return float((-2*np.trace(Mn@adj3(A))).real)
def fullq(A):
    q=np.array([np.trace(G@A).real for G in gr])
    return float(np.sum(q*q/pn)+frozen(A))

def qmatrix(qfun):
    q=[qfun(A) for A in B]
    H=np.zeros((9,9))
    for i in range(9):
        H[i,i]=q[i]
        for j in range(i):
            H[i,j]=H[j,i]=(qfun(B[i]+B[j])-q[i]-q[j])/2
    return H

S4n=np.array([[float(x) for x in row] for row in S4])
S5n=np.array([[float(x) for x in row] for row in S5])
H4n=[npmat(H) for H in E+[H7]]
H5n=[npmat(H) for H in E+[H0,H7]]

def projq(A,Hs,S):
    z=np.array([np.trace(H@A).real for H in Hs])
    return float(z@np.linalg.solve(S,z)+frozen(A))

eig4=np.linalg.eigvalsh(qmatrix(lambda A:projq(A,H4n,S4n)))
eig5=np.linalg.eigvalsh(qmatrix(lambda A:projq(A,H5n,S5n)))
eigfull=np.linalg.eigvalsh(qmatrix(fullq))
assert eig4[0] < -0.9
assert eig5[0] > 3.9
assert eigfull[0] > 3.9

print("status=PASS")
print("exact_leading_minors_K=",leadK)
print("exact_leading_minors_I_minus_K=",leadJ)
print("exact_atoms_J=",p)
print("exact_cycle_product_K=",loop)
print("exp_c_ratios=",R1,R2,R3)
print("exp_tau_ratio=",Rt)
print("max_log_interval_width_lt_1e-25=True")
print("delta_interval_approx=",(float(delta.lo),float(delta.hi)))
print("rank_four_features=4")
print("rank_five_features=5")
print("det_C4_interval_approx=",(float(detC4.lo),float(detC4.hi)))
print("det_C5_interval_approx=",(float(detC5.lo),float(detC5.hi)))
print("det_C4_plus_deltaSigma4_interval_approx=",(float(D4.lo),float(D4.hi)))
print("det_C5_plus_deltaSigma5_interval_approx=",(float(D5.lo),float(D5.hi)))
print("EXACT_ASSERT_det4_gt_10000000=True")
print("EXACT_ASSERT_det5_lt_minus1000000000=True")
print("four_feature_certificate_min_eigenvalue_diagnostic=",float(eig4[0]))
print("five_feature_certificate_min_eigenvalue_diagnostic=",float(eig5[0]))
print("full_curvature_min_eigenvalue_diagnostic=",float(eigfull[0]))
print("four_feature_universal_candidate_refuted=True")
print("five_feature_universal_candidate_proved=False")
print("unrestricted_three_site_proved=False")
