from fractions import Fraction
from math import factorial, comb
from collections import defaultdict

checks = 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def beta_int(a,b):
    assert a>=1 and b>=1
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))

def rising(a,n):
    out=Fraction(1,1)
    for j in range(n):
        out *= a+j
    return out

def polya_assignment(r,s,d):
    return rising(Fraction(r),s)*rising(Fraction(1),d)/rising(Fraction(r+1),s+d)

# 1. Polya/Beta identity.
for r in range(1,21):
    for s in range(0,9):
        for d in range(0,9):
            lhs = polya_assignment(r,s,d)
            rhs = Fraction(r)*beta_int(r+s,d+1)
            ck(lhs == rhs, f"Polya identity r={r} s={s} d={d}")

# 2. Beta telescoping used by C012/C013.
for a in range(1,9):
    for c in range(1,9):
        for R in range(1,21):
            lhs = sum((beta_int(a+r-1,c+1) for r in range(1,R+1)), Fraction(0))
            rhs = beta_int(a,c)-beta_int(a+R,c)
            ck(lhs == rhs, f"telescoping a={a} c={c} R={R}")

def q0_direct(R,m,b,i):
    j=b-i
    Sa=sum((beta_int(r+i-1,j+1) for r in range(1,R+1)), Fraction(0))
    Sc=sum((beta_int(r+j-1,i+1) for r in range(1,R+1)), Fraction(0))
    Sh1=sum((beta_int(r+j,i+1) for r in range(1,R+1)), Fraction(0))
    Sh2=sum((beta_int(r+i,j+1) for r in range(1,R+1)), Fraction(0))
    return Fraction(i,m)*Sa + Fraction(j,m)*Sc + Fraction(m-b,m)*(Sh1+Sh2)

def q0_closed(R,m,b,i):
    j=b-i
    return (beta_int(i,j)
            - Fraction(i,m)*beta_int(i+R,j)
            - Fraction(j,m)*beta_int(j+R,i)
            - Fraction(m-b,m)*(beta_int(j+R+1,i)+beta_int(i+R+1,j)))

def qtheta(R,theta,m,b,i):
    j=b-i
    def wt(r):
        return Fraction(r,1)/(Fraction(r,1)+theta)
    Sa=sum((wt(r)*beta_int(r+i-1,j+1) for r in range(1,R+1)), Fraction(0))
    Sc=sum((wt(r)*beta_int(r+j-1,i+1) for r in range(1,R+1)), Fraction(0))
    Sh1=sum((wt(r)*beta_int(r+j,i+1) for r in range(1,R+1)), Fraction(0))
    Sh2=sum((wt(r)*beta_int(r+i,j+1) for r in range(1,R+1)), Fraction(0))
    return Fraction(i,m)*Sa + Fraction(j,m)*Sc + Fraction(m-b,m)*(Sh1+Sh2)

# 3. Hidden-size formulas and quantitative deformation bounds.
for R in range(1,13):
    theta=Fraction(1,R+3)
    for m in range(2,16):
        for b in range(2,m+1):
            for i in range(1,b):
                B=beta_int(i,b-i)
                q0=q0_direct(R,m,b,i)
                qc=q0_closed(R,m,b,i)
                qt=qtheta(R,theta,m,b,i)
                ck(q0 == qc, f"q0 direct/closed R={R},m={m},b={b},i={i}")
                ck(Fraction(0)<=qt<=q0<=B, f"ordering R={R},m={m},b={b},i={i}")
                ck(B-q0 <= Fraction(2,R+1), f"truncation R={R},m={m},b={b},i={i}")
                ck(q0-qt <= theta*q0, f"deformation R={R},m={m},b={b},i={i}")
                ck(B-qt <= Fraction(2,R+1)+theta*B,
                   f"combined bound R={R},m={m},b={b},i={i}")

# 4. Exact Feller/Ewens activation profile.
for N in range(2,101):
    theta=Fraction(1,N)
    R=N
    errs=[]
    total=Fraction(0)
    for r in range(1,R+1):
        p=theta/(theta+r)
        ratio=Fraction(r)*p/theta
        ck(ratio == Fraction(r,1)/(Fraction(r,1)+theta), f"profile N={N} r={r}")
        errs.append(abs(ratio-1))
        total += p
    e=max(errs)
    ck(e == theta/(1+theta), f"profile sup N={N}")
    H=sum((Fraction(1,r) for r in range(1,R+1)), Fraction(0))
    ck(total <= theta*H, f"activation mass N={N}")
    ck(Fraction(1,R+1) <= Fraction(1,N), f"R growth N={N}")
    ck(theta*H*H > 0, f"scale N={N}")

def peel_count_prob(r,n,d):
    return Fraction(comb(n,d))*rising(Fraction(r),n-d)*rising(Fraction(1),d)/rising(Fraction(r+1),n)

# 5. Exact N=3 C013 root witness: theta=1/3, R=3, increasing channel order.
N=3
theta=Fraction(1,N)
R=N
ps={r: theta/(theta+r) for r in range(1,R+1)}
states={(2, tuple()): Fraction(1)}
for r in range(1,R+1):
    p=ps[r]
    nxt=defaultdict(Fraction)
    for (n,children),prob in states.items():
        nxt[(n,children)] += prob*(1-p)
        for d in range(n+1):
            pd=peel_count_prob(r,n,d)
            if d==0:
                nxt[(n,children)] += prob*p*pd
            else:
                nxt[(n-d,children+(d,))] += prob*p*pd
    states=nxt

expected={
    (2, tuple()): Fraction(26,35),
    (1,(1,)): Fraction(39,280),
    (0,(2,)): Fraction(559,5040),
    (0,(1,1)): Fraction(1,144),
}
ck(sum(states.values(),Fraction(0))==1, "N3 state normalization")
ck(dict(states)==expected, f"N3 state law {states}")
p_no=states[(2,tuple())]
p_deg3=states[(0,(1,1))]
visible_deg3=p_deg3/(1-p_no)
ck(visible_deg3==Fraction(35,1296), f"N3 visible deg3={visible_deg3}")

# 6. Separation from retained finite witnesses.
prior = [
    Fraction(0,1),
    Fraction(1,10),
    Fraction(1,22),
    Fraction(1,6),
    Fraction(1,728),
    Fraction(1,7),
    Fraction(1,71),
    Fraction(2,105),
    Fraction(21521,4909716)
]
for x in prior:
    ck(visible_deg3 != x, f"witness separation from {x}")

print("R11 I0054 C013 Ewens-Feller logarithmic-channel exact self-check")
print(f"checks={checks}")
print("C013 parameters: R_N=N, theta_N=1/N, raw time theta_N")
print("N=3 activation probabilities:", ", ".join(f"p{r}={ps[r]}" for r in range(1,R+1)))
print("N=3 exact root state law:")
for k in sorted(states, key=str):
    print(f"  {k}: {states[k]}")
print(f"N=3 reduced first-visible root degree-3 probability = {visible_deg3}")
print("U003 concrete profile: sup_r |r p_r/theta - 1| = theta/(1+theta)")
print("uniform projected-rate error checked: B-q_theta <= 2/(R+1)+theta*B")
print("ALL_EXACT_CHECKS_PASS")
