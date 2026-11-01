from fractions import Fraction
from math import factorial

checks = 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def B(a,b):
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))

def H(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

# ------------------------------------------------------------------
# 1. Move #2: a flat/uniform-frequency excursion law has the wrong
#    4-leaf shape ratio, so the singular endpoint occupation matters.
# ------------------------------------------------------------------
flat13 = 2*B(2,4)   # 2 B(i+1,j+1), i=1,j=3
flat22 = 2*B(3,3)
ctcs13 = B(1,3)
ctcs22 = B(2,2)
ck(flat13/flat22 == Fraction(3,2), "flat ratio")
ck(ctcs13/ctcs22 == 2, "CTCS ratio")
ck(flat13/flat22 != ctcs13/ctcs22, "flat model must fail")

# ------------------------------------------------------------------
# 2. Exact Green occupation for the neutral lazy Moran chain.
#    Internal transition p_i^+=p_i^-=i(N-i)/N^2.
#    Candidate G_N(i,r) is expected pre-absorption number of visits
#    to state r, starting from i.
# ------------------------------------------------------------------
def moran_green(N,i,r):
    if i in (0,N):
        return Fraction(0)
    return Fraction(N * min(i,r) * (N-max(i,r)), r*(N-r))

for N in range(2,31):
    for r in range(1,N):
        ck(moran_green(N,0,r)==0 and moran_green(N,N,r)==0,
           f"Green boundary N={N}, r={r}")
        for i in range(1,N):
            p = Fraction(i*(N-i), N*N)
            lhs = moran_green(N,i,r)
            rhs = ((Fraction(1) if i==r else Fraction(0))
                   + p*moran_green(N,i+1,r)
                   + p*moran_green(N,i-1,r)
                   + (1-2*p)*moran_green(N,i,r))
            ck(lhs == rhs, f"Green equation N={N}, i={i}, r={r}")
        ck(moran_green(N,1,r) == Fraction(N,r),
           f"singleton occupation N={N}, r={r}")
    ck(sum((moran_green(N,1,r) for r in range(1,N)), Fraction(0))
       == N*H(N-1), f"absorption mean N={N}")

# ------------------------------------------------------------------
# 3. Embedded simple random walk absorption moments, and a rigorous
#    N^5 second-moment envelope for lazy Moran absorption time tau.
# ------------------------------------------------------------------
def m_emb(N,i):
    return i*(N-i)

def u_emb(N,i):
    if i in (0,N):
        return 0
    return Fraction(i**4 - 2*N*i**3 + 2*i**2 + (N**3-2*N)*i, 3)

for N in range(2,101):
    for i in range(1,N):
        ck(2*m_emb(N,i) - m_emb(N,i-1) - m_emb(N,i+1) == 2,
           f"embedded mean recurrence N={N}, i={i}")
        ck(2*u_emb(N,i) - u_emb(N,i-1) - u_emb(N,i+1)
           == 4*m_emb(N,i)-2,
           f"embedded second recurrence N={N}, i={i}")
    ck(m_emb(N,1)==N-1, f"embedded ES N={N}")
    ck(u_emb(N,1)==Fraction(N**3-4*N+3,3),
       f"embedded ES2 N={N}")
    # Every internal Moran move probability q_i=2i(N-i)/N^2 >= 1/N.
    for i in range(1,N):
        q = Fraction(2*i*(N-i), N*N)
        ck(q >= Fraction(1,N), f"move lower bound N={N}, i={i}")
    upper_tau2 = N*N*(Fraction(m_emb(N,1)) + u_emb(N,1))
    ck(upper_tau2 <= N**5, f"tau2 envelope N={N}")

# ------------------------------------------------------------------
# 4. First-order split rate from the Moran occupation spectrum.
# ------------------------------------------------------------------
def qN(N,i,j):
    total = Fraction(0)
    for k in range(1,N):
        x = Fraction(k,N)
        total += Fraction(1,N)*(x**(i-1)*(1-x)**j
                                + x**(j-1)*(1-x)**i)
    return total

def qH(N,i,j):
    # C001 harmonic-grid particular-split rate.
    return sum((Fraction(1,N)*Fraction(k,N)**(i-1)
                *(1-Fraction(k,N))**(j-1)
                for k in range(1,N)), Fraction(0))

for b in range(2,13):
    for i in range(1,b):
        j=b-i
        # Limiting beta identity:
        ck(B(i,j+1)+B(j,i+1)==B(i,j),
           f"beta limit identity b={b}, i={i}")
        # Exact rates are positive and symmetric at finite N.
        for N in (3,4,5,8,16,32):
            if N >= 2:
                q=qN(N,i,j)
                ck(q>=0, f"qN positivity N={N}, b={b}, i={i}")
                ck(q==qN(N,j,i), f"qN symmetry N={N}, b={b}, i={i}")
                ck(q==qH(N,i,j), f"Moran/HGPF exact generator identity N={N}, b={b}, i={i}")
        # A simple exact convergence sanity check: error decreases from N=8 to 32
        # for these polynomial Riemann sums (not used as the proof).
        e8=abs(qN(8,i,j)-B(i,j))
        e32=abs(qN(32,i,j)-B(i,j))
        ck(e32 <= e8, f"Riemann convergence sanity b={b}, i={i}")

# Total first-order exit rate converges to H_{b-1}.
# Sum over PARTICULAR unordered partitions, represented by the side containing label 1.
for b in range(2,11):
    target=H(b-1)
    for N in (8,16,32,64):
        import math
        tot=sum((math.comb(b-1,i-1)*qN(N,i,b-i)
                 for i in range(1,b)), Fraction(0))
        ck(tot>0, f"total exit positive N={N}, b={b}")
    tot_target=sum((Fraction(__import__('math').comb(b-1,i-1))*B(i,b-i)
                    for i in range(1,b)), Fraction(0))
    ck(tot_target==target, f"CTCS total rate b={b}")

# ------------------------------------------------------------------
# 5. Chosen rare-gate scale a_N=delta_N/N, delta_N=N^-4.
#    Expected gates per excursion = delta_N H_{N-1}.
#    P(>=2 gates) <= a_N^2 E[tau^2]/2 <= delta_N^2 N^3/2.
# ------------------------------------------------------------------
for N in range(2,101):
    delta=Fraction(1,N**4)
    a=delta/N
    expected_gates=a*(N*H(N-1))
    ck(expected_gates==delta*H(N-1), f"gate mean N={N}")
    upper_tau2=N*N*(Fraction(m_emb(N,1))+u_emb(N,1))
    multi_bound=Fraction(1,2)*a*a*upper_tau2
    ck(multi_bound <= Fraction(1,2)*delta*delta*N**3,
       f"multi-gate bound N={N}")
    ck(delta*N**3==Fraction(1,N), f"accumulated scale N={N}")

# ------------------------------------------------------------------
# 6. Exact N=3 finite branching witness from an independent linear solve.
# ------------------------------------------------------------------
def solve_linear(A,b):
    n=len(b)
    M=[list(map(Fraction,A[r]))+[Fraction(b[r])] for r in range(n)]
    for c in range(n):
        piv=next(r for r in range(c,n) if M[r][c])
        M[c],M[piv]=M[piv],M[c]
        z=M[c][c]
        for j in range(c,n+1):
            M[c][j]/=z
        for r in range(n):
            if r!=c and M[r][c]:
                z=M[r][c]
                for j in range(c,n+1):
                    M[r][j]-=z*M[c][j]
    return [M[r][-1] for r in range(n)]

N=3
delta=Fraction(1,N**4)
a=delta/N
# Moran: from 1 or 2, absorption in one direction with h=2/9,
# switch to the other internal state with 2/9, hold with 5/9.
h=Fraction(2,9)
sw=Fraction(2,9)
st=Fraction(5,9)
q=a*Fraction(2,3)  # a gate visibly splits a 3-block
r=a*Fraction(4,9)  # a gate splits the remaining 2-block in a binary partition

# Triple absorption probability. Unknown order:
# (x=1,shape0),(x=2,shape0),(x=1,shape1),(x=2,shape1)
A=[[Fraction(0) for _ in range(4)] for __ in range(4)]
bb=[Fraction(0) for _ in range(4)]
for xidx in (0,1):
    row=xidx
    A[row][row]=1
    other=1-xidx
    A[row][row]-=(1-q)*st
    A[row][other]-=(1-q)*sw
    A[row][2+xidx]-=q*st
    A[row][2+other]-=q*sw
    row=2+xidx
    A[row][row]=1
    bb[row]=r
    A[row][row]-=(1-r)*st
    A[row][2+other]-=(1-r)*sw
triple=solve_linear(A,bb)[0]

# No-visible-split probability: solve only shape0; a visible gate kills this event.
A0=[[Fraction(0),Fraction(0)],[Fraction(0),Fraction(0)]]
b0=[Fraction(0),Fraction(0)]
for xidx in (0,1):
    other=1-xidx
    A0[xidx][xidx]=1-(1-q)*st
    A0[xidx][other]=-(1-q)*sw
    b0[xidx]=(1-q)*h
none=solve_linear(A0,b0)[0]
reduced=triple/(1-none)
ck(triple==Fraction(63,809968), "N=3 raw triple witness")
ck(none==Fraction(727,736), "N=3 no-visible witness")
ck(reduced==Fraction(14,2201), "N=3 reduced degree-3 witness")

old=[
    Fraction(0), Fraction(1,10), Fraction(1,22), Fraction(1,6),
    Fraction(1,728), Fraction(1,7), Fraction(1,71),
    Fraction(2,105), Fraction(21521,4909716), Fraction(35,1296)
]
for z in old:
    ck(reduced != z, f"new witness collides with {z}")

print("R11 I0054 C014 neutral-Moran-excursion exact checker")
print("flat-frequency 4-leaf rate ratio =", flat13/flat22,
      "; CTCS =", ctcs13/ctcs22)
print("Moran Green identity: E_1 L_k = N/k verified exactly for N<=30")
print("Embedded absorption moments and E[tau^2] <= N^5 verified exactly for N<=100")
print("Moran-occupation split beta identity verified on finite exact grid")
print("Moran occupation generator equals C001 harmonic-grid generator exactly on checked grid")
print("chosen scale delta_N=N^-4 gives delta_N*N^3=1/N")
print("N=3 raw degree-3 probability =", triple)
print("N=3 no-visible probability =", none)
print("N=3 reduced first-visible root degree-3 probability =", reduced)
print("exact checks =", checks)
print("ALL_EXACT_CHECKS_PASS")
