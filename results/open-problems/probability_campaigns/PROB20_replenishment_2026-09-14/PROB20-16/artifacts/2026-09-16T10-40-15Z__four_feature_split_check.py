from fractions import Fraction
import numpy as np
import sympy as sp

SEED=20260916
rng=np.random.default_rng(SEED)
I=sp.I

# Exact rational genuinely complex example from the report.
K=sp.Matrix([
    [sp.Rational(527,1000), sp.Rational(-67,1000)+sp.Rational(63,1000)*I,
     sp.Rational(-10,1000)+sp.Rational(77,1000)*I],
    [sp.Rational(-67,1000)-sp.Rational(63,1000)*I, sp.Rational(607,1000),
     sp.Rational(106,1000)-sp.Rational(112,1000)*I],
    [sp.Rational(-10,1000)-sp.Rational(77,1000)*I,
     sp.Rational(106,1000)+sp.Rational(112,1000)*I, sp.Rational(3,5)]
])

def leading_minors(M):
    return [sp.simplify(M[:k,:k].det()) for k in range(1,4)]

def atoms_exact(M):
    p=[]
    for mask in range(8):
        Q=M.copy()
        for i in range(3):
            if not ((mask>>i)&1):
                Q[i,i]-=1
        p.append(sp.simplify((-1)**(3-mask.bit_count())*Q.det()))
    return p

leadK=leading_minors(K)
leadI=leading_minors(sp.eye(3)-K)
assert all(x>0 for x in leadK+leadI)

p=atoms_exact(K)
assert sum(p)==1 and all(x>0 for x in p)
expected=[sp.Rational(x,200000000) for x in
          [11034023,15649977,25600177,27715823,24452177,27463823,33513623,34570377]]
assert p==expected

loop=sp.expand(K[0,1]*K[1,2]*K[2,0])
assert sp.im(loop)==-sp.Rational(69139,500000000)

Rt=sp.simplify(p[1]*p[2]*p[4]*p[7]/(p[0]*p[3]*p[5]*p[6]))  # exp(-tau)
R1=sp.simplify(p[3]*p[5]/(p[1]*p[7]))  # exp(c1+tau)
R2=sp.simplify(p[3]*p[6]/(p[2]*p[7]))
R3=sp.simplify(p[5]*p[6]/(p[4]*p[7]))
assert Rt>1 and R1>1 and R2>1 and R3>1
assert R1>=R2 and R1>=R3
easy_bound=sp.simplify((Rt-1)+sp.Rational(3,2)*(R1-1))
assert easy_bound<1

L=sp.simplify(K*(sp.eye(3)-K).inv())
assert sp.simplify(L[1,1]-2)>0
assert sp.simplify(L[1,1])==sp.Rational(25600177,11034023)

# Numeric helpers for independent curvature checks.
def adj3(A):
    return A@A-np.trace(A)*A+0.5*(np.trace(A)**2-np.trace(A@A))*np.eye(3,dtype=complex)

def atoms_num(Kn):
    out=np.zeros(8)
    for mask in range(8):
        Q=Kn.copy()
        for i in range(3):
            if not ((mask>>i)&1):
                Q[i,i]-=1
        out[mask]=(((-1)**(3-mask.bit_count()))*np.linalg.det(Q)).real
    return out

def atom_derivs(Kn,A):
    out=np.zeros(8)
    for mask in range(8):
        Q=Kn.copy()
        for i in range(3):
            if not ((mask>>i)&1):
                Q[i,i]-=1
        sg=(-1)**(3-mask.bit_count())
        out[mask]=(sg*np.linalg.det(Q)*np.trace(np.linalg.solve(Q,A))).real
    return out

def coeffs(Kn,pn):
    c=np.array([
        np.log(pn[2]*pn[4]/(pn[0]*pn[6])),
        np.log(pn[1]*pn[4]/(pn[0]*pn[5])),
        np.log(pn[1]*pn[2]/(pn[0]*pn[3]))
    ])
    tau=np.log(pn[0]*pn[3]*pn[5]*pn[6]/(pn[1]*pn[2]*pn[4]*pn[7]))
    return c,tau,np.diag(c)+tau*Kn

def occupation_cov(Kn):
    a=np.real(np.diag(Kn))
    S=np.diag(a*(1-a))
    for i,j in [(0,1),(0,2),(1,2)]:
        S[i,j]=S[j,i]=-abs(Kn[i,j])**2
    return S

def Rmat(a):
    return np.array([[0,a[2],a[1]],[a[2],0,a[0]],[a[1],a[0],0.]],float)

def eta_exact_matrix(Kn):
    pn=atoms_num(Kn); c,tau,M=coeffs(Kn,pn); S=occupation_cov(Kn)
    ew,U=np.linalg.eigh(S); Sh=(U*np.sqrt(ew))@U.T
    if tau>=0:
        aa=c; pe=pn[7]; tt=tau
    else:
        aa=c+tau; pe=pn[0]; tt=-tau
    lam=np.linalg.eigvalsh(Sh@Rmat(aa)@Sh)[-1]
    easy=tt*(1-pe)+1.5*np.max(aa)
    return tt*(1-pe)+lam,easy,tau,pn,c,M,S

def frozen(Kn,M,A):
    return float((-2*np.trace(M@adj3(A))).real)

def curvature(Kn,A):
    pn=atoms_num(Kn); c,tau,M=coeffs(Kn,pn)
    q=atom_derivs(Kn,A)
    FI=float(np.sum(q*q/pn))
    return FI+frozen(Kn,M,A)

Kn=np.array(K.evalf(30),dtype=complex)
eta,easy,tau,pn,c,M,S=eta_exact_matrix(Kn)
assert eta<1 and easy<1 and tau<0

# Check the theorem's explicit lower bound for many directions at K*.
min_gap=1e100
min_curv=1e100
for _ in range(2000):
    X=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    A=(X+X.conj().T)/2
    curv=curvature(Kn,A)
    p0=pn[0]; cb=c+tau; theta=(-tau)*(1-p0)
    ew,U=np.linalg.eigh(np.eye(3)-Kn)
    ih=(U*(1/np.sqrt(ew)))@U.conj().T
    B=ih@A@ih
    d=np.real(np.diag(A))
    off=2*(cb[0]*abs(A[1,2])**2+cb[1]*abs(A[0,2])**2+cb[2]*abs(A[0,1])**2)
    lower=p0*(-tau)*np.linalg.norm(B,'fro')**2+off+d@((1-theta)*np.linalg.inv(S)-Rmat(cb))@d
    min_gap=min(min_gap,curv-lower)
    min_curv=min(min_curv,curv)
assert min_gap>-1e-8 and min_curv>0

# Broad diagnostic bank: theorem-certified points must have nonnegative direct curvature matrix.
BASIS=[]
for i in range(3):
    A=np.zeros((3,3),complex); A[i,i]=1; BASIS.append(A)
for i,j in [(0,1),(0,2),(1,2)]:
    A=np.zeros((3,3),complex); A[i,j]=A[j,i]=1; BASIS.append(A)
    A=np.zeros((3,3),complex); A[i,j]=1j; A[j,i]=-1j; BASIS.append(A)

def hessian_curvature_matrix(Kn):
    vals=[curvature(Kn,E) for E in BASIS]
    H=np.empty((9,9))
    for i in range(9):
        H[i,i]=vals[i]
        for j in range(i):
            v=(curvature(Kn,BASIS[i]+BASIS[j])-vals[i]-vals[j])/2
            H[i,j]=H[j,i]=v
    return H

accepted=0
certified=0
min_certified_eig=1e100
max_eta_cert=-1e100
for _ in range(3000):
    Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    U,_=np.linalg.qr(Z)
    ev=1/(1+np.exp(-rng.uniform(-6,6,3)))
    Q=U@np.diag(ev)@U.conj().T
    pp=atoms_num(Q)
    if pp.min()<1e-9:
        continue
    accepted+=1
    et,ez,*_=eta_exact_matrix(Q)
    if et<=1:
        certified+=1
        mine=np.linalg.eigvalsh(hessian_curvature_matrix(Q))[0]
        min_certified_eig=min(min_certified_eig,mine)
        max_eta_cert=max(max_eta_cert,et)
assert certified>0 and min_certified_eig>-1e-7

print('status=PASS')
print('seed=',SEED)
print('exact_leading_minors_K=',leadK)
print('exact_leading_minors_I_minus_K=',leadI)
print('exact_atoms=',p)
print('exact_loop_product=',loop)
print('exp_minus_tau_ratio=',Rt)
print('exp_cbar_ratios=',R1,R2,R3)
print('easy_scalar_upper_bound=',easy_bound)
print('easy_scalar_slack=',sp.simplify(1-easy_bound))
print('odds_L22=',L[1,1])
print('numeric_eta_matrix_example=',repr(float(eta)))
print('numeric_easy_scalar_example=',repr(float(easy)))
print('direction_checks=2000')
print('min_direct_curvature_minus_theorem_lower_bound=',repr(float(min_gap)))
print('min_direct_curvature_at_example=',repr(float(min_curv)))
print('broad_random_accepted=',accepted)
print('broad_random_certified_by_eta=',certified)
print('min_curvature_eigenvalue_among_certified=',repr(float(min_certified_eig)))
print('max_eta_among_certified=',repr(float(max_eta_cert)))
print('random_bank_is_diagnostic_only=True')
print('unrestricted_three_site_proved=False')