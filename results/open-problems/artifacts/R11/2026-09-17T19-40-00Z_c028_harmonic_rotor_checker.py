from fractions import Fraction as F
from math import factorial

CHECKS = 0
def ck(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def beta_int(i,j):
    return F(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def w(N,s):
    return F(N, 2*s*(N-s))

def c(N,s):
    return (N-1)*w(N,s)

def x(N,s):
    return F(s,N)

def f_support(N,s,i,j):
    z=x(N,s)
    return z**i*(1-z)**j + z**j*(1-z)**i

def p_nonmono(N,s,b):
    z=x(N,s)
    return 1-z**b-(1-z)**b

def q_cycle(N,i,j):
    return sum(w(N,s)*f_support(N,s,i,j) for s in range(1,N))

# 1. Exact harmonic identities and uniform exit-rate bound.
for N in range(3, 201):
    lhs=sum(w(N,s) for s in range(1,N))
    rhs=sum(F(1,r) for r in range(1,N))
    ck(lhs==rhs, f'harmonic normalization N={N}: {lhs} vs {rhs}')
    for b in range(2,9):
        for s in range(1,N):
            val=c(N,s)*p_nonmono(N,s,b)
            ck(val <= b, f'exit bound N={N} b={b} s={s}: {val}')
            ck(val >= 0, f'negative exit N={N} b={b} s={s}')

# 2. Exact averaged-generator identity.
for N in range(3,101):
    for i in range(1,6):
        for j in range(1,6):
            if i+j > 9:
                continue
            lhs=q_cycle(N,i,j)
            rhs=sum(x(N,s)**(i-1)*(1-x(N,s))**(j-1) for s in range(1,N))/N
            ck(lhs==rhs, f'quadrature identity N={N} i={i} j={j}: {lhs} vs {rhs}')

# 3. Riemann convergence finite self-check along an increasing grid sequence.
for i in range(1,6):
    for j in range(1,6):
        B=beta_int(i,j)
        vals=[]
        for N in (20,40,80,160,320):
            vals.append(abs(q_cycle(N,i,j)-B))
        ck(vals[-1] < F(1,100), f'quadrature error large i={i} j={j}: {vals[-1]}')
        ck(vals[-1] <= vals[0], f'quadrature failed to improve i={i} j={j}: {vals}')

# 4. Critical scales and activation probabilities Delta*c_s <= 1.
for N in range(3,1001):
    Delta=F(1,N**3)
    tau=(N-1)*Delta
    ck(tau > 0, f'tau positive N={N}')
    ck(tau <= F(1,N**2), f'tau scale N={N}: {tau}')
    for s in (1, N//2, N-1):
        if 1 <= s <= N-1:
            a=Delta*c(N,s)
            ck(0 <= a <= 1, f'activation invalid N={N} s={s}: {a}')

# 5. Deterministic rotor discrepancy: phase visit counts differ by at most one.
for N in range(3,30):
    m=N-1
    for t in range(0,5*m+1):
        counts=[]
        for s in range(1,N):
            q,r=divmod(t,m)
            counts.append(q + (1 if s <= r else 0))
        ck(max(counts)-min(counts) <= 1, f'rotor discrepancy N={N} t={t}')

# 6. N=3 exact first-visible-root support ratio.
N=3; Delta=F(1,N**3); b=4
phase=[]
for s in (1,2):
    a=Delta*c(N,s)
    p13=a*f_support(N,s,1,3)
    p22=a*f_support(N,s,2,2)
    psplit=a*p_nonmono(N,s,b)
    phase.append((a,p13,p22,psplit))
ck(phase[0]==phase[1], f'mirror phases differ: {phase}')
a,p13,p22,psplit=phase[0]
ck(a==F(1,18), f'a={a}')
ck(p13==F(5,729), f'p13={p13}')
ck(p22==F(4,729), f'p22={p22}')
ck(psplit==F(32,729), f'psplit={psplit}')
ratio=p13/p22
ck(ratio==F(5,4), f'ratio={ratio}')
surv=1-psplit
cycle13=p13 + surv*p13
cycle22=p22 + surv*p22
ck(cycle13/cycle22==ratio, 'cycle root ratio mismatch')

# 7. Separation from every retained binary finite witness through C027.
prior_binary = [
    F(2,1), F(7,5), F(2699,1365), F(2273,1153), F(61381,43765),
    F(166094447739,85563797248), F(33,17), F(5,3), F(597,359),
    F(18,11), F(9,5)
]
for q in prior_binary:
    ck(ratio != q, f'collision with prior binary witness {q}')

print('R11 C028 deterministic harmonic-rotor exact self-check')
print(f'CHECKS={CHECKS}')
print('Cyclic model: Delta_N=N^-3, phases s=1,...,N-1, x_s=s/N,')
print('  w_s=N/[2s(N-s)], c_s=(N-1)w_s, activation a_s=Delta_N c_s.')
print('Exact averaged specified-support rate:')
print('  q_N(i,j)=sum_s w_s[x_s^i(1-x_s)^j+x_s^j(1-x_s)^i]')
print('          =(1/N)sum_s x_s^(i-1)(1-x_s)^(j-1) -> B(i,j).')
print('N=3, b=4 exact finite root witness:')
print(f'  per-phase activation={a}')
print(f'  per-phase particular p(1|3)={p13}')
print(f'  per-phase particular p(2|2)={p22}')
print(f'  per-phase any visible split={psplit}')
print(f'  first-visible particular-support ratio={ratio} = {float(ratio):.12f}')
print(f'  difference from C001 7/5 = {ratio-F(7,5)}')
print('Rotor prefix visit-count discrepancy <= 1 checked on finite grid.')
print('ALL_EXACT_CHECKS_PASS')
