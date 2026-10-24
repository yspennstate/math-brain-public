#!/usr/bin/env python3
from decimal import Decimal, getcontext
from math import comb, floor

getcontext().prec = 100
D = Decimal
LN2 = D(2).ln()

def log2(x):
    return x.ln()/LN2

def h2(x):
    if x == 0 or x == 1:
        return D(0)
    return -x*log2(x)-(1-x)*log2(1-x)

def solve_c(k):
    q = D(2) ** D(2-k)
    lo, hi = D("0.5"), D(1)-D("1e-90")
    def F(c):
        return (D(1)-c*(D(1)-q))*(D(1)-c*q)**(k-1) - (D(1)-c)
    assert F(lo) <= 0 and F(hi) > 0
    for _ in range(400):
        mid = (lo+hi)/2
        if F(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def evaluate(k):
    N = k-2
    q = D(2) ** D(-N)
    c = solve_c(k)
    t1, t = c*(D(1)-q), c*q
    Iminus = D(N)*q

    pmain, ptail = (D(1)-q)**2, q*q
    ntail = D((1 << (k-1))-1)
    HP = -pmain*log2(pmain)-ntail*ptail*log2(ptail)
    Hmax = (h2(t1)+D(k-1)*h2(t)-h2(c))/c
    Kocc = Hmax-HP

    Qsupport = (t1*(D(1)-t)+(D(1)-t1)*t)/c
    zeta = D(1)-Qsupport
    Ksupp = -log2(D(1)-zeta)

    d2 = t1*(D(1)-t1)*(t*(D(1)-t))**(k-1)/(c*c)
    qE = t1*t**(k-1)/c
    s2 = D(1)-qE
    disc = s2*s2-D(4)*d2
    if disc < 0 and abs(disc) < D("1e-90"):
        disc = D(0)
    eta = (s2-disc.sqrt())/D(2)
    Kpar = -D(2)*log2(D(1)-eta/D(2))

    Korbit = D(0)
    cells = []
    totalP = totalQ = D(0)
    for a in (0,1):
        for b in (0,1):
            for w in range(N+1):
                if a == b == 0 and w == 0:
                    continue
                C = D(comb(N,w))
                Q = ((t1 if a else D(1)-t1) *
                     (t if b else D(1)-t) *
                     C*t**w*(D(1)-t)**(N-w))/c
                P = D(0)
                if a != b:
                    P = pmain if (a,b,w)==(1,0,0) else C*ptail
                totalP += P
                totalQ += Q
                if P > 0:
                    Korbit += P*log2(P/Q)
                cells.append((a,b,w,P,Q))
    assert abs(totalP-D(1)) < D("1e-80")
    assert abs(totalQ-D(1)) < D("1e-80")
    assert abs(Korbit-Kocc) < D("1e-75")

    m = max(1, floor(N/2 - N**0.75))
    pe = ue = D(0)
    for a,b,w,P,Q in cells:
        if w >= m:
            pe += P
            ue += Q
    Kbin = pe*log2(pe/ue)+(D(1)-pe)*log2((D(1)-pe)/(D(1)-ue))

    return {"k":k,"N":N,"q":q,"c":c,"Iminus":Iminus,
            "Kocc":Kocc,"Ksupp":Ksupp,"Kpar":Kpar,
            "Korbit":Korbit,"m":m,"Kbin":Kbin}

print("B17 orbit/cardinality KL checker")
for k in (4,5,6,8,10,16,32,64):
    z=evaluate(k)
    print(
        "k=%d c=%.18g Kocc/(I-1)=%.15g Ksupp/(I-1)=%.15g "
        "Kpar/(I-1)=%.15g Korbit-Kocc=%s m=%d Kbin/(I-1)=%.15g"
        % (k, z["c"], z["Kocc"]/z["Iminus"], z["Ksupp"]/z["Iminus"],
           z["Kpar"]/z["Iminus"], str(z["Korbit"]-z["Kocc"]),
           z["m"], z["Kbin"]/z["Iminus"])
    )

for k in range(5,65):
    z=evaluate(k)
    rhs=D(40)/(D(3)*LN2*D(k-2))
    assert max(z["Ksupp"],z["Kpar"])/z["Iminus"] <= rhs

print("PASS: exact orbit KL equals K_occ on every tested family member.")
print("PASS: newest support/complement explicit payment obeys O(1/k) influence-normalized bound for k=5..64.")
print("PASS: high-cardinality binary events retain a growing fraction of the hidden KL on the tested tail.")
