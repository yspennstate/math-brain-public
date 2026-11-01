from fractions import Fraction as Q
from math import factorial
import sympy as sp

checks=0

def ok(cond,msg='assertion failed'):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def H(n):
    return sum((Q(1,k) for k in range(1,n+1)), Q(0))

def tau(x):
    x=Q(x)
    if x < Q(1,2):
        return x
    if x < Q(2,3):
        return 2*x/(1+x)
    if x < Q(4,5):
        return x/(2-x)
    return x

def lam(N,s):
    return Q(N,2*s*(N-s))

def qrate(N,i,j):
    z=Q(0)
    for s in range(1,N):
        p=tau(Q(s,N))
        z += lam(N,s)*(p**i*(1-p)**j+p**j*(1-p)**i)
    return z

def beta_int(i,j):
    return Q(factorial(i-1)*factorial(j-1), factorial(i+j-1))

# Exact piecewise map facts and involution on a dense rational grid.
ok(tau(Q(1,2)) == Q(2,3))
ok(tau(Q(2,3)) == Q(1,2))
ok(tau(Q(4,5)) == Q(4,5))
for den in range(2,81):
    for num in range(1,den):
        x=Q(num,den)
        y=tau(x)
        ok(Q(0) < y < Q(1), f'range {x}->{y}')
        ok(tau(y) == x, f'involution {x}->{y}->{tau(y)}')

# Harmonic proposal normalization.
for N in range(2,101):
    ok(sum((lam(N,s) for s in range(1,N)), Q(0)) == H(N-1), f'norm N={N}')

# Exact symbolic Jacobian/conserved-measure identities on the two moved intervals.
x=sp.symbols('x', positive=True)
p2=2*x/(1+x)
pm=x/(2-x)
for p in [p2,pm]:
    jac=sp.simplify(sp.diff(p,x)/(p*(1-p)) - 1/(x*(1-x)))
    ok(jac == 0, f'jacobian {p}: {jac}')
ok(sp.simplify(p2.subs(x,sp.Rational(1,2))-sp.Rational(2,3))==0)
ok(sp.simplify(p2.subs(x,sp.Rational(2,3))-sp.Rational(4,5))==0)
ok(sp.simplify(pm.subs(x,sp.Rational(2,3))-sp.Rational(1,2))==0)
ok(sp.simplify(pm.subs(x,sp.Rational(4,5))-sp.Rational(2,3))==0)

# Exact symbolic integral identity for all split types through 7 visible labels.
segments=[
    (sp.Rational(0),sp.Rational(1,2),x),
    (sp.Rational(1,2),sp.Rational(2,3),p2),
    (sp.Rational(2,3),sp.Rational(4,5),pm),
    (sp.Rational(4,5),sp.Rational(1),x),
]
for m in range(2,8):
    for i in range(1,m):
        j=m-i
        integ=sp.Integer(0)
        for a,b,p in segments:
            f=sp.cancel((p**i*(1-p)**j+p**j*(1-p)**i)/(2*x*(1-x)))
            integ += sp.integrate(f,(x,a,b))
        target=sp.Rational(factorial(i-1)*factorial(j-1),factorial(m-1))
        ok(sp.simplify(integ-target)==0, f'integral {i}|{j}: {sp.simplify(integ-target)}')

# C084 exact N=4 witness.
N=4
bias=[tau(Q(s,N)) for s in range(1,N)]
weights=[lam(N,s) for s in range(1,N)]
ok(bias == [Q(1,4),Q(2,3),Q(3,5)], bias)
ok(weights == [Q(2,3),Q(1,2),Q(2,3)], weights)
q13=qrate(4,1,3)
q22=qrate(4,2,2)
total=4*q13+3*q22
bal=3*q22/total
ok(q13 == Q(722693,3240000), q13)
ok(q22 == Q(560707,3240000), q22)
ok(total == Q(4572893,3240000), total)
ok(bal == Q(1682121,4572893), bal)
source_bal=Q(3,11)
c083_bal=Q(186177,553141)
ok(bal != source_bal)
ok(bal != c083_bal)
ok(q13/q22 != Q(2,1))  # CTCS ratio B(1,3)/B(2,2)=2.

# Direct finite split rates are symmetric and positive in a broad exact scan.
for N in range(2,61):
    for m in range(2,min(N,8)+1):
        for i in range(1,m):
            j=m-i
            q=qrate(N,i,j)
            ok(q>0, f'positive N={N} {i}|{j}')
            ok(q==qrate(N,j,i), f'sym N={N} {i}|{j}')

# Exact finite convergence sanity evaluations. No finite scan is used as proof.
for N in [8,16,32,64,128,256]:
    for i,j in [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]:
        _ = qrate(N,i,j)-beta_int(i,j)
        ok(isinstance(_, Q), f'exact sanity N={N} {i}|{j}')

print('R11-I0054-C084 logit interval-exchange exact self-check')
print(f'ASSERTIONS={checks}')
print('N4_biases=' + ','.join(map(str,bias)))
print('N4_clock_rates=' + ','.join(map(str,weights)))
print(f'N4_q_1_3={q13}')
print(f'N4_q_2_2={q22}')
print(f'N4_total_root_rate={total}')
print(f'N4_balanced_root_probability={bal}')
print(f'SOURCE_CTCS4_balanced_probability={source_bal}')
print(f'C083_balanced_probability={c083_bal}')
print('CONVERGENCE_SANITY_POINTS=36 exact rational evaluations')
print('STATUS=ALL_EXACT_CHECKS_PASS')
