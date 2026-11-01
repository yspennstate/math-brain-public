from fractions import Fraction
from math import gcd, log
from hashlib import sha256
from itertools import combinations

checks = 0

def ck(cond, msg='check failed'):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def least_prime_ge(n):
    p = n
    while not is_prime(p):
        p += 1
    return p

def lcm(a,b):
    return a // gcd(a,b) * b

def harmonic(n):
    return sum((Fraction(1,j) for j in range(1,n+1)), Fraction(0,1))

def d_of_p(p):
    return min(p-1, max(2, int(log(p,2))))

def yscore(a,t,p,d):
    y = 0
    tp = t % p
    ap = 1
    for _ in range(d):
        y = (y + ap*tp) % p
        ap = (ap*a) % p
        tp = (tp*t) % p
    return y

def redset(N,p,d,s,t):
    return tuple(a for a in range(N) if yscore(a,t,p,d) < s)

def w(p,s):
    return Fraction(p, 2*s*(p-s))

def rotor_data(N):
    p = least_prime_ge(N)
    d = d_of_p(p)
    tau = Fraction(1,p*p)
    delta = tau / Fraction(p*(p-1),1)
    D = 1
    for s in range(1,p):
        D = lcm(D, 2*s*(p-s))
    rho = delta / D
    rows = []
    for s in range(1,p):
        c = Fraction(p-1,1)*w(p,s)
        M = c*D
        ck(M.denominator == 1, (N,p,s,D,c,M))
        M = int(M)
        h = M*rho
        a = 1 - (1-rho)**M
        ck(h == delta*c)
        ck(Fraction(0) < a <= h < 1)
        lower = h - Fraction(M*(M-1),2)*rho*rho
        ck(lower <= a <= h)
        ck(h-a <= h*h/Fraction(2,1))
        rows.append((s,M,h,a))
    return p,d,tau,delta,D,rho,rows

for N in range(3,14):
    p,d,tau,delta,D,rho,rows = rotor_data(N)
    ck(N <= p < 2*N,(N,p))
    ck(2 <= d < p,(N,p,d))
    ck(rho > 0)
    ck(sum((w(p,s) for s in range(1,p)),Fraction(0,1)) == harmonic(p-1))
    hmax = max(h for _,_,h,_ in rows)
    ck(hmax == tau/Fraction(2*(p-1),1),(N,p,hmax))
    err_bound = Fraction(p*(p-1),1)*hmax*hmax/Fraction(2,1)
    target_bound = tau*tau*Fraction(p,8*(p-1))
    ck(err_bound == target_bound,(N,p,err_bound,target_bound))
    ck(err_bound/tau <= Fraction(1,4*p*p))

for p in [17,19,23,29,31,37,41,43,47,53,59]:
    tau=Fraction(1,p*p)
    hmax=tau/Fraction(2*(p-1),1)
    err_bound=Fraction(p*(p-1),1)*hmax*hmax/Fraction(2,1)
    ck(err_bound == tau*tau*Fraction(p,8*(p-1)))
    ck(err_bound/tau <= Fraction(1,4*p*p))

for den in [17,31,101,216,1009]:
    rho = Fraction(1,den)
    for m in [1,2,5,11]:
        for n in [1,3,7]:
            lhs = (1-rho)**(m+n) / (1-rho)**m
            rhs = (1-rho)**n
            ck(lhs == rhs,(den,m,n,lhs,rhs))

for N in range(3,26):
    p = least_prime_ge(N); d = d_of_p(p)
    for a,b in combinations(range(N),2):
        found = False
        for t in range(p):
            ya,yb = yscore(a,t,p,d),yscore(b,t,p,d)
            if ya != yb:
                lo,hi = sorted((ya,yb))
                if lo < hi and lo < p-1:
                    found = True
                    break
        ck(found,(N,p,d,a,b))

N=3
p,d,tau,delta,D,rho,rows = rotor_data(N)
ck((p,d,tau,delta,D,rho) == (3,2,Fraction(1,9),Fraction(1,54),4,Fraction(1,216)))
row1 = [x for x in rows if x[0] == 1][0]
_,M1,h1,a1 = row1
ck(M1 == 6)
ck(h1 == Fraction(1,36))
ck(a1 == 1 - Fraction(215,216)**6)
ck(a1 == Fraction(2788659027791,101559956668416))
ck(a1 < h1)
ck(redset(3,p,d,1,0) == (0,1,2))
ck(set(redset(3,p,d,1,1)) == {2})

N=5
p,d,tau,delta,D,rho,rows = rotor_data(N)
ck((p,d,tau,delta,D,rho)==(5,2,Fraction(1,25),Fraction(1,500),24,Fraction(1,12000)))
visible = tuple(range(4))
rowmap = {s:(M,h,a) for s,M,h,a in rows}
entries=[]
for s in range(1,p):
    M,h,a = rowmap[s]
    for t in range(p):
        entries.append((a,set(redset(4,p,d,s,t)),s,t,M))

def canon_support(S):
    S=frozenset(S); C=frozenset(visible)-S
    x=tuple(sorted(S)); y=tuple(sorted(C))
    return min(x,y),max(x,y)

def one_cycle_split_mass(target):
    target=canon_support(target)
    surv=Fraction(1,1)
    mass=Fraction(0,1)
    for a,R,s,t,M in entries:
        RR=R & set(visible)
        if 0 < len(RR) < len(visible):
            if canon_support(RR)==target:
                mass += surv*a
            surv *= (1-a)
    return mass,surv

m13,surv13=one_cycle_split_mass({0})
m22,surv22=one_cycle_split_mass({0,1})
ck(surv13==surv22)
ck(m13>0 and m22>0)
R=m13/m22
R032=Fraction(7703418956282489179517201,3464343821016000000000000)
ck(Fraction(11,5) < R < R032,(R,R032))

prior=[
    Fraction(2,1), Fraction(7,5), Fraction(2699,1365), Fraction(2273,1153),
    Fraction(61381,43765), Fraction(166094447739,85563797248),
    Fraction(33,17), Fraction(5,3), Fraction(597,359), Fraction(18,11),
    Fraction(9,5), Fraction(5,4), Fraction(459,224)
]
for q0 in prior:
    ck(q0 < Fraction(11,5) < R,(q0,R))

ratio_text=f'{R.numerator}/{R.denominator}'
ratio_sha=sha256(ratio_text.encode()).hexdigest()

print('C033_GEOMETRIC_BUDGET_ROTOR_EXACT_SELF_CHECK')
print(f'checks={checks}')
print('N3_p=3')
print('N3_tau=1/9')
print('N3_delta=1/54')
print('N3_D=4')
print('N3_rho=1/216')
print('N3_first_nonmono_tick_weight=6')
print('N3_C032_linear_activation=1/36')
print(f'N3_C033_budget_activation={a1}')
print(f'N3_strict_gap={h1-a1}')
print('N5_p=5')
print('N5_tau=1/25')
print('N5_delta=1/500')
print('N5_D=24')
print('N5_rho=1/12000')
print(f'N5_root_ratio_float={float(R):.15f}')
print('N5_exact_bracket=11/5 < R_C033 < R_C032')
print(f'N5_root_ratio_num_digits={len(str(R.numerator))}')
print(f'N5_root_ratio_den_digits={len(str(R.denominator))}')
print(f'N5_root_ratio_sha256={ratio_sha}')
print('R_C032=7703418956282489179517201/3464343821016000000000000')
print('ALL_EXACT_CHECKS_PASS')
