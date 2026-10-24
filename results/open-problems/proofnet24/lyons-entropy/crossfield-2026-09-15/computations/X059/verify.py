"""Exact finite verification of X059's conditional replacement calculus."""
import itertools
import json
from pathlib import Path
import sympy as S

R = S.Rational
states = list(itertools.product((0, 1), repeat=3))
n = len(states)
checks = 0

def check(v):
    global checks
    if isinstance(v, S.MatrixBase):
        assert all(S.simplify(x) == 0 for x in v), v
    else:
        assert bool(v), v
    checks += 1

def atoms(K):
    out = []
    for x in states:
        J = [i for i in range(3) if x[i]]
        O = [i for i in range(3) if not x[i]]
        z = 0
        for r in range(len(O)+1):
            for B in itertools.combinations(O, r):
                T = J + list(B)
                z += (-1)**r * (K.extract(T,T).det() if T else 1)
        out.append(S.expand(z))
    return S.Matrix(out)

def bath(mu, i):
    T = S.zeros(n)
    for yidx, y in enumerate(states):
        inds = [j for j,x in enumerate(states) if all(x[k] == y[k] for k in range(3) if k != i)]
        mass = sum(mu[j] for j in inds)
        for xidx in inds:
            T[xidx,yidx] = mu[xidx] / mass
    return T

def conditional_values(p, values, i):
    out = []
    for x in states:
        inds = [j for j,y in enumerate(states) if all(x[k] == y[k] for k in range(3) if k != i)]
        out.append(sum(p[j]*values[j] for j in inds)/sum(p[j] for j in inds))
    return S.Matrix(out)

def logbounds(x, N=120):
    """Rational enclosure from the convergent atanh power series."""
    z = (x-1)/(x+1)
    if z < 0:
        lo, hi = logbounds(1/x, N)
        return -hi, -lo
    lo = sum(2*z**(2*k+1)/R(2*k+1) for k in range(N))
    tail = 2*z**(2*N+1)/(R(2*N+1)*(1-z*z))
    return lo, lo+tail

def workbounds(coeff, p):
    check(sum(coeff) == 0)
    lo = hi = 0
    for c, x in zip(coeff, p):
        l, h = logbounds(x/p[0])
        lo += c*(l if c >= 0 else h)
        hi += c*(h if c >= 0 else l)
    return lo, hi

def divlogs(p, q):
    """Exact coefficients of log(prime) in a rational KL divergence."""
    result = {}
    for a, b in zip(p,q):
        num, den = (a/b).as_numer_denom()
        for sign, integer in ((1,num),(-1,den)):
            for prime, power in S.factorint(integer).items():
                result[prime] = result.get(prime,0)+sign*a*power
    return result

def combine(*terms):
    result = {}
    for scale, term in terms:
        for prime, coeff in term.items():
            result[prime] = result.get(prime,0)+scale*coeff
    return {p:c for p,c in result.items() if c != 0}

K = S.Matrix([[R(2,5),R(1,10),R(1,12)],
              [R(1,10),R(1,2),S.I*R(1,15)],
              [R(1,12),-S.I*R(1,15),R(3,5)]])
M = S.Matrix([[R(1,2),R(1,4),0],[R(1,4),R(1,2),0],[0,0,R(1,2)]])
p, mu = atoms(K), atoms(M)
check(all(x > 0 for x in p)); check(all(x > 0 for x in mu))
for B in (K,S.eye(3)-K,M,S.eye(3)-M):
    for r in range(1,4):
        for inds in itertools.combinations(range(3),r):
            check(B.extract(inds,inds).det() > 0)
T, U = bath(mu,0), bath(mu,1)
for B in (T,U):
    check(S.ones(1,n)*B-S.ones(1,n))
    check(B*B-B)
    check(B*mu-mu)
    check(B*S.diag(*mu)-S.diag(*mu)*B.T)
L, N = T-S.eye(n), U-S.eye(n)
c = (U*T-T*U)*p
v = (L+N)*p
b = (N*L+L*N)*p
check(c != S.zeros(n,1))
fi = sum(vx*vx/px for vx,px in zip(v,p))
commutator_coefficient = sum(cx*cx/px for cx,px in zip(c,p))/8
check(commutator_coefficient > 0)

# The complete finite, positive entropy-dissipation identity at t=1/3.
tau = R(1,3)
Ci, Cj = S.eye(n)+tau*L, S.eye(n)+tau*N
cip, cjp = Ci*p, Cj*p
pjfinite, pifinite = Cj*cip, Ci*cjp
avgfinite = (pjfinite+pifinite)/2
for B, C in ((T,Ci),(U,Cj)):
    bp, cp = B*p, C*p
    check(combine((1,divlogs(p,mu)),(-1,divlogs(bp,mu)),(-1,divlogs(p,bp))) == {})
    check(combine((1,divlogs(p,mu)),(-1,divlogs(cp,mu)),
        (-tau,divlogs(p,bp)),(-(1-tau),divlogs(p,cp)),(-tau,divlogs(bp,cp))) == {})
check(combine((1,divlogs(p,mu)),(-1,divlogs(avgfinite,mu)),
    (-R(1,2),divlogs(p,mu)),(R(1,2),divlogs(cip,mu)),
    (-R(1,2),divlogs(cip,mu)),(R(1,2),divlogs(pjfinite,mu)),
    (-R(1,2),divlogs(p,mu)),(R(1,2),divlogs(cjp,mu)),
    (-R(1,2),divlogs(cjp,mu)),(R(1,2),divlogs(pifinite,mu)),
    (-R(1,2),divlogs(pjfinite,avgfinite)),(-R(1,2),divlogs(pifinite,avgfinite))) == {})

# A seven-coordinate Hermitian chart is locally surjective at this K.
q = S.symbols('q0:7', real=True)
Achart = S.Matrix([[q[0],q[3],q[4]],
                   [q[3],q[1],q[5]+S.I*q[6]],
                   [q[4],q[5]-S.I*q[6],q[2]]])
t = S.symbols('t', real=True)
chart_atoms = atoms(K+t*Achart)
dp = chart_atoms.diff(t).subs(t,0)
J = dp.jacobian(q)
check(J.rank() == 7)
solution = S.linsolve((J,v),q)
check(len(solution) == 1)
sol = dict(zip(q,next(iter(solution))))
A = Achart.subs(sol)
pt = atoms(K+t*A)
check(pt.subs(t,0)-p)
check(pt.diff(t).subs(t,0)-v)
a = pt.diff(t,2).subs(t,0)
d = a-b
check(A.det() != 0)
check(K*A-A*K != S.zeros(3))
for j in range(3):
    check(sum(states[k][j]*a[k] for k in range(n)) == 0)

# The exact ordered polynomials, their common first jet and their difference.
pj = (S.eye(n)+t*N)*(S.eye(n)+t*L)*p
pi = (S.eye(n)+t*L)*(S.eye(n)+t*N)*p
bar = (pj+pi)/2
check(pj-pi-t*t*c)
check(bar.diff(t).subs(t,0)-v)
check(bar.diff(t,2).subs(t,0)-b)
check(sum(d) == 0)
check(sum(states[k][0]*b[k] for k in range(n)) != 0)

# Scalar fourth-derivative formula for h=-x log x gives JS''''/24.
def entropy_fourth(vel, acc):
    return sum(-2*vel[k]**4/p[k]**3+6*vel[k]**2*acc[k]/p[k]**2
               -3*acc[k]**2/p[k] for k in range(n))
aj = pj.diff(t,2).subs(t,0)
ai = pi.diff(t,2).subs(t,0)
js4 = (entropy_fourth(v,b)-(entropy_fourth(v,aj)+entropy_fourth(v,ai))/2)/24
check(S.simplify(js4-commutator_coefficient) == 0)

# Moving physical reference: verify each conditional kernel's full two-jet.
s = S.Matrix([v[k]/p[k] for k in range(n)])
u = S.Matrix([a[k]/p[k] for k in range(n)])
T0s, T1s, T2s = [], [], []
for i in (0,1):
    Bt = bath(pt,i)
    B0 = Bt.subs(t,0)
    B1 = Bt.diff(t).subs(t,0)
    B2 = Bt.diff(t,2).subs(t,0)
    si = conditional_values(p,s,i)
    ui = conditional_values(p,u,i)
    alpha = s-si
    beta = u-ui-2*S.matrix_multiply_elementwise(si,alpha)
    check(B1-S.diag(*alpha)*B0)
    check(B2-S.diag(*beta)*B0)
    check(B0*v+B1*p-v)
    check(B0*a+2*B1*v+B2*p-a)
    T0s.append(B0); T1s.append(B1); T2s.append(B2)
full_second = (T0s[1]*T0s[0]*a
    +2*(T1s[1]*T0s[0]+T0s[1]*T1s[0])*v
    +(T2s[1]*T0s[0]+2*T1s[1]*T1s[0]+T0s[1]*T2s[0])*p)
check(full_second-a)

def interval_dec(pair):
    return [str(S.N(pair[0],25)),str(S.N(pair[1],25))]

lb, ub = workbounds(d,p)
la, ua = workbounds(a,p)
lc, uc = workbounds(c,p)
lbb, ubb = workbounds(b,p)

# A reference approaching the current physical law from either side.
# mu_e=P_(K+e I) has a strictly physical two-sided interval about e=0.
vb = atoms(K+t*S.eye(3)).diff(t).subs(t,0)
P0 = S.eye(n)-bath(p,0)
P1 = S.eye(n)-bath(p,1)
velocity_first = (P0+P1)*vb
sol_first = dict(zip(q,next(iter(S.linsolve((J,velocity_first),q)))))
Afirst = Achart.subs(sol_first)
defect_first = (P0*P1+P1*P0)*vb
commutator_first = (P0*P1-P1*P0)*vb
check(J*S.Matrix([sol_first[z] for z in q])-velocity_first)
check(Afirst.det() != 0)
check(K*Afirst-Afirst*K != S.zeros(3))
check(commutator_first != S.zeros(n,1))
ld, ud = workbounds(defect_first,p)
check(ld > -R(20385,10**6))
check(ud < -R(20384,10**6))
check(ud-ld < R(1,10**60))
check(lb > R(103427,10**6))
check(ub < R(103429,10**6))
data = {
    'exact_assertions':checks,
    'K':str(K), 'reference_K':str(M),'A':str(A),'det_A':str(A.det()),
    'p':[str(x) for x in p],
    'commutator':[str(x) for x in c],
    'physical_acceleration':[str(x) for x in a],
    'bath_acceleration':[str(x) for x in b],
    'bath_marginal_accelerations':[str(sum(states[k][j]*b[k] for k in range(n))) for j in range(3)],
    'quartic_JS_coefficient':str(commutator_coefficient),
    'quartic_JS_coefficient_decimal':str(S.N(commutator_coefficient,20)),
    'physical_correction_interval':interval_dec((lb,ub)),
    'physical_minus_Hsecond_interval':interval_dec((fi+la,fi+ua)),
    'bath_minus_Hsecond_interval':interval_dec((fi+lbb,fi+ubb)),
    'order_Hsecond_difference_interval':interval_dec((-2*uc,-2*lc)),
    'near_reference_Afirst':str(Afirst),
    'near_reference_det_Afirst':str(Afirst.det()),
    'near_reference_defect_work_derivative_interval':interval_dec((ld,ud)),
    'near_reference_defect_first':[str(x) for x in defect_first],
}
Path(__file__).with_name('results.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
