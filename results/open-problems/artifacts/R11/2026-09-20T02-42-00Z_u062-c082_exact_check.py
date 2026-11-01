from fractions import Fraction
from math import comb
from itertools import product

ASSERTIONS = 0

def check(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def beta_int(i, j):
    from math import factorial
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def p_oriented_formula(i, j, x, th):
    return (
        x * (th + (1-th)*x)**i * ((1-th)*(1-x))**j
        + (1-x) * ((1-th)*x)**i * (th + (1-th)*(1-x))**j
    )

def p_oriented_bruteforce(i, j, x, th):
    m = i+j
    target = (1,)*i + (0,)*j
    ans = Fraction(0)
    for mask in product((0,1), repeat=m):
        r = sum(mask)
        pm = th**r * (1-th)**(m-r)
        unmarked = [a for a in range(m) if not mask[a]]
        for z in (0,1):
            pz = x if z else (1-x)
            for bits in product((0,1), repeat=len(unmarked)):
                pc = Fraction(1)
                colors = [None]*m
                for a in range(m):
                    if mask[a]:
                        colors[a] = z
                for a,b in zip(unmarked,bits):
                    colors[a] = b
                    pc *= x if b else (1-x)
                if tuple(colors) == target:
                    ans += pm*pz*pc
    return ans

def q_finite(N, i, j, th):
    ans = Fraction(0)
    for s in range(1,N):
        x = Fraction(s,N)
        lam = Fraction(N, 2*s*(N-s))
        ans += lam*(p_oriented_formula(i,j,x,th)+p_oriented_formula(j,i,x,th))
    return ans

def q_cont(i, j, th):
    a = 1-th
    s1 = sum(Fraction((-1)**r * comb(j,r), i+r) * a**(i+r) for r in range(j+1))
    s2 = sum(Fraction((-1)**r * comb(i,r), j+r) * a**(j+r) for r in range(i+1))
    return s1+s2

def delta_formula(i,j,th):
    s1 = sum(Fraction((-1)**a * comb(i-1,a), j+a+1)*th**(j+a+1) for a in range(i))
    s2 = sum(Fraction((-1)**a * comb(j-1,a), i+a+1)*th**(i+a+1) for a in range(j))
    return s1+s2

def D_sum(m, th):
    total = Fraction(0)
    for i in range(1,m):
        total += Fraction(comb(m,i),2)*delta_formula(i,m-i,th)
    return total

def D_closed(m, th):
    return sum(th**(a+1)/Fraction(a+1) for a in range(m)) - Fraction(1-(1-th)**m, m)

def theta_N(N):
    ceil_log2 = (N-1).bit_length()
    d = max(2, ceil_log2)
    return Fraction(1,d)

for m in range(2,6):
    for i in range(1,m):
        j=m-i
        for th in (Fraction(1,5), Fraction(1,3), Fraction(1,2)):
            for x in (Fraction(1,7), Fraction(1,4), Fraction(2,5), Fraction(3,4)):
                a=p_oriented_formula(i,j,x,th)
                b=p_oriented_bruteforce(i,j,x,th)
                check(a==b, ("oriented",m,i,th,x,a,b))
                check(0 <= a <= 1)

for m in range(2,10):
    for i in range(1,m):
        j=m-i
        for th in (Fraction(1,10),Fraction(1,4),Fraction(1,3),Fraction(1,2)):
            qc=q_cont(i,j,th)
            de=delta_formula(i,j,th)
            check(qc+de==beta_int(i,j), ("beta deficit",m,i,th,qc,de))
            check(de>=0)
            check(qc>=0)
            check(delta_formula(i,j,th)==delta_formula(j,i,th))

for m in range(2,15):
    for den in range(3,15):
        for num in range(1, den//2+1):
            th=Fraction(num,den)
            if th > Fraction(1,2):
                continue
            ds=D_sum(m,th)
            dc=D_closed(m,th)
            check(ds==dc, ("D identity",m,th,ds,dc))
            check(ds>=0)
            check(ds <= Fraction(m,2)*th*th/(1-th), ("D upper",m,th,ds))
check(D_closed(2,Fraction(1,3))==Fraction(1,9))

for N in range(3,20):
    total = sum(Fraction(N,2*s*(N-s)) for s in range(1,N))
    H = sum(Fraction(1,s) for s in range(1,N))
    check(total==H, ("proposal norm",N,total,H))
    for th in (Fraction(1,5),Fraction(1,3),Fraction(1,2)):
        q2=q_finite(N,1,1,th)
        target=Fraction(N-1,N)*(1-th*th)
        check(q2==target, ("pair rate",N,th,q2,target))

for N in range(3,9):
    for m in range(2,min(6,N+1)):
        for i in range(1,m):
            j=m-i
            for th in (Fraction(1,3),Fraction(1,2)):
                brute=Fraction(0)
                for s in range(1,N):
                    x=Fraction(s,N)
                    lam=Fraction(N,2*s*(N-s))
                    p1=p_oriented_bruteforce(i,j,x,th)
                    p2=p_oriented_bruteforce(j,i,x,th)
                    brute += lam*(p1+p2)
                form=q_finite(N,i,j,th)
                check(brute==form, ("finite brute",N,m,i,th,brute,form))
                check(form>=0)

check(theta_N(4)==Fraction(1,2))
for N in range(4,200):
    check(theta_N(N) <= Fraction(1,2))
for N in (16,32,64,128,256,1024,4096):
    check(theta_N(2*N) <= theta_N(N))

N=4
th=theta_N(N)
q13=q_finite(N,1,3,th)
q22=q_finite(N,2,2,th)
root=4*q13+3*q22
bal=3*q22/root
check(q13==Fraction(95,512), ("q13",q13))
check(q22==Fraction(49,512), ("q22",q22))
check(root==Fraction(527,512), ("root",root))
check(bal==Fraction(147,527), ("bal",bal))
check(bal != Fraction(3,11))
check(bal != Fraction(1,1))

for m in range(3,10):
    for i in range(1,m):
        j=m-i
        s=min(i,j)
        for th in (Fraction(1,100),Fraction(1,50),Fraction(1,20)):
            de=delta_formula(i,j,th)
            check(de >= 0)
            check(de / th**(s+1) >= 0)
        exponents=[]
        exponents += [j+a+1 for a in range(i)]
        exponents += [i+a+1 for a in range(j)]
        check(min(exponents)==s+1)

print("U062/C082 EXACT CHECK")
print("ASSERTIONS=", ASSERTIONS)
print("N4_THETA=", theta_N(4))
print("N4_Q_1|3=", q13)
print("N4_Q_2|2=", q22)
print("N4_ROOT_RATE=", root)
print("N4_BALANCED_ROOT_PROB=", bal)
print("CTCS4_BALANCED_ROOT_PROB=", Fraction(3,11))
print("CONT_PAIR_DEFICIT_THETA_1_3=", D_closed(2,Fraction(1,3)))
print("STATUS=ALL_EXACT_CHECKS_PASS")
