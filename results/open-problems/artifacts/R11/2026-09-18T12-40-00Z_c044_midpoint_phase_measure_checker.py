from fractions import Fraction
from collections import defaultdict

checks = 0

def chk(cond, msg=""):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg or f"failed check #{checks}")

def xmid(N,r):
    return Fraction(2*r-1, 2*N)

def wmid(N,r):
    x=xmid(N,r)
    return Fraction(1,2*N)/(x*(1-x))

def q_direct(N,i,j):
    ans=Fraction(0)
    for r in range(1,N+1):
        x=xmid(N,r)
        w=wmid(N,r)
        ans += w*(x**i*(1-x)**j + x**j*(1-x)**i)
    return ans

def q_mid(N,i,j):
    return sum((xmid(N,r)**(i-1)*(1-xmid(N,r))**(j-1)
                for r in range(1,N+1)), Fraction(0))/N

def rho(N):
    d=defaultdict(Fraction)
    for r in range(1,N+1):
        x=xmid(N,r)
        mass=wmid(N,r)*x*(1-x)
        d[x] += mass
        d[1-x] += mass
    return dict(d)

def exit_rate(N,m):
    return sum((wmid(N,r)*(1-xmid(N,r)**m-(1-xmid(N,r))**m)
                for r in range(1,N+1)), Fraction(0))

# Exact transformed phase measure and generator identities.
for N in range(2,81):
    rw=rho(N)
    chk(len(rw)==N, f"rho support N={N}")
    for r in range(1,N+1):
        chk(rw[xmid(N,r)] == Fraction(1,N), f"rho mass N={N},r={r}")
    chk(sum(rw.values(), Fraction(0)) == 1, f"rho total N={N}")
    for i in range(1,7):
        for j in range(1,7):
            chk(q_direct(N,i,j)==q_mid(N,i,j), f"generator identity N={N},i={i},j={j}")

# Closed moment identities.
for N in range(2,201):
    chk(q_direct(N,1,1)==1, f"q11 N={N}")
    chk(q_direct(N,2,1)==Fraction(1,2), f"q21 N={N}")
    chk(q_direct(N,2,2)==Fraction(2*N*N+1,12*N*N), f"q22 N={N}")
    chk(q_direct(N,1,3)==Fraction(4*N*N-1,12*N*N), f"q13 N={N}")
    chk(q_direct(N,1,3)/q_direct(N,2,2)==Fraction(4*N*N-1,2*N*N+1), f"root ratio N={N}")

# Uniform finite-restriction rate control.
for N in range(2,101):
    for m in range(2,11):
        er=exit_rate(N,m)
        chk(er > 0, f"positive exit N={N},m={m}")
        chk(er <= m, f"exit bound N={N},m={m}: {er}")

# Exact C044 finite witness at N=4.
N=4
q11=q_direct(N,1,1)
q13=q_direct(N,1,3)
q22=q_direct(N,2,2)
ratio=q13/q22
chk(q11==1)
chk(q13==Fraction(21,64))
chk(q22==Fraction(11,64))
chk(ratio==Fraction(21,11))

# Nearest harmonic-grid independent-block model at N=4:
# q_h(i,j)=(1/N) sum_{s=1}^{N-1}(s/N)^(i-1)(1-s/N)^(j-1).
qh11=Fraction(N-1,N)
qh22=sum((Fraction(s,N)*(1-Fraction(s,N)) for s in range(1,N)), Fraction(0))/N
chk(qh11==Fraction(3,4))
chk(qh22==Fraction(5,32))
chk(qh22/qh11==Fraction(5,24))
chk(q22/q11==Fraction(11,64))
chk(q22/q11 != qh22/qh11)

# Archived exact binary root-ratio witnesses through C029.
old = [
    Fraction(2,1), Fraction(7,5), Fraction(2699,1365),
    Fraction(2273,1153), Fraction(61381,43765),
    Fraction(166094447739,85563797248), Fraction(33,17),
    Fraction(5,3), Fraction(597,359), Fraction(18,11),
    Fraction(9,5), Fraction(5,4), Fraction(459,224)
]
for z in old:
    chk(ratio != z, f"collision with archived ratio {z}")

# Later archived brackets used in C033.
chk(ratio < 2)          # separates C030, whose witness is >2
chk(ratio < Fraction(11,5))  # separates C032/C033, whose witnesses are >11/5

print(f"ASSERTIONS={checks}")
print("C044_N4_q11=", q11)
print("C044_N4_q13=", q13)
print("C044_N4_q22=", q22)
print("C044_N4_root_ratio=", ratio)
print("C044_N4_q22_over_q11=", q22/q11)
print("HARMONIC_N4_q22_over_q11=", qh22/qh11)
print("ALL_EXACT_CHECKS_PASS")
