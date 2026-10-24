from fractions import Fraction
from collections import Counter
from itertools import combinations

ASSERTIONS = 0
def ck(cond, msg=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def de_bruijn(q, k):
    # FKM algorithm, returns a cyclic de Bruijn word B(q,k)
    a = [0] * (q * k + 1)
    seq = []
    def db(t, p):
        if t > k:
            if k % p == 0:
                seq.extend(a[1:p+1])
        else:
            a[t] = a[t-p]
            db(t+1, p)
            for j in range(a[t-p] + 1, q):
                a[t] = j
                db(t+1, t)
    db(1, 1)
    return seq

def cyclic_block(word, s, r):
    L = len(word)
    return tuple(word[(s+t) % L] for t in range(r))

def threshold_bits(word, s, r, u):
    return tuple(1 if x < u else 0 for x in cyclic_block(word,s,r))

def rate_a(q,u):
    x = Fraction(u,q)
    return Fraction(1, 2*(q-1)) / (x*(1-x))

def split_rate_direct(word, q, u, A, B):
    # unordered split A|B on named positions, averaged over a uniform cyclic shift
    L = len(word)
    hits = 0
    m = max(A|B)
    for s in range(L):
        bits = [1 if word[(s+t)%L] < u else 0 for t in range(m+1)]
        orient1 = all(bits[a]==1 for a in A) and all(bits[b]==0 for b in B)
        orient2 = all(bits[a]==0 for a in A) and all(bits[b]==1 for b in B)
        if orient1 or orient2:
            hits += 1
    return rate_a(q,u) * Fraction(hits,L)

def total_rate(q):
    return sum((rate_a(q,u) for u in range(1,q)), Fraction(0,1))

def mesh_delta(q):
    return Fraction(1, q**3)

def G(q,i,j):
    tot = Fraction(0,1)
    for u in range(1,q):
        x = Fraction(u,q)
        tot += x**(i-1) * (1-x)**(j-1)
    return tot / (q-1)

# de Bruijn existence/property checks
for q in range(2,6):
    for K in range(2,5):
        w = de_bruijn(q,K)
        ck(len(w)==q**K, (q,K,len(w)))
        Kblocks = [cyclic_block(w,s,K) for s in range(len(w))]
        ck(len(set(Kblocks))==q**K, f"unique K blocks {q},{K}")
        for r in range(1,K+1):
            c = Counter(cyclic_block(w,s,r) for s in range(len(w)))
            ck(len(c)==q**r, (q,K,r,len(c)))
            target = q**(K-r)
            for v in c.values():
                ck(v==target, (q,K,r,v,target))
            # threshold cylinder exactness
            for u in range(1,q):
                cb = Counter(threshold_bits(w,s,r,u) for s in range(len(w)))
                for m in range(2**r):
                    bits = tuple((m>>t)&1 for t in range(r))
                    ones = sum(bits)
                    expected = q**(K-r) * (u**ones) * ((q-u)**(r-ones))
                    ck(cb[bits]==expected, (q,K,r,u,bits,cb[bits],expected))

# generator identity from direct cyclic shifts whenever k<=K
for q in range(2,7):
    K = 5
    w = de_bruijn(q,K)
    for i in range(1,4):
        for j in range(1,4):
            k=i+j
            if k>K:
                continue
            A=set(range(i))
            B=set(range(i,k))
            direct=sum((split_rate_direct(w,q,u,A,B) for u in range(1,q)), Fraction(0,1))
            ck(direct==G(q,i,j), (q,i,j,direct,G(q,i,j)))

# discrete microstep validity and vanishing simultaneous-jump scale
for q in range(2,101):
    A = total_rate(q)
    d = mesh_delta(q)
    ck(d*A <= 1, ("activation",q,d*A))
    ck(d*A*A < Fraction(1,1), ("double_jump",q,d*A*A))

# pair normalization is exact in the eventual local-iid regime
for q in range(2,40):
    ck(G(q,1,1)==1, ("pair",q,G(q,1,1)))

# Exact N=4 natural small-case support witness: q=K=2, canonical FKM cycle.
# This is deliberately outside the eventual K>=4 regime and is used only to
# distinguish the finite class under relabeling/global-time-rescaling.
w = de_bruijn(2,2)
ck(w==[0,0,1,1], ("B22",w))

def n4_rate(A):
    A=set(A); B=set(range(4))-A
    return sum((split_rate_direct(w,2,u,A,B) for u in range(1,2)), Fraction(0,1))

pair_rates=[]
for A in combinations(range(4),1):
    for b in range(A[0]+1,4):
        # all six named 1|1 restrictions, evaluated only on those two coordinates
        r=sum((split_rate_direct(w,2,u,{A[0]},{b}) for u in range(1,2)), Fraction(0,1))
        pair_rates.append(r)
triple_rates=[n4_rate({a}) for a in range(4)]
balanced_rates=[n4_rate(A) for A in ({0,1},{0,2},{0,3})]
ck(sorted(pair_rates)==[Fraction(1),Fraction(1),Fraction(1),Fraction(1),Fraction(2),Fraction(2)], pair_rates)
ck(triple_rates==[Fraction(0)]*4, triple_rates)
ck(sorted(balanced_rates)==[Fraction(0),Fraction(1),Fraction(1)], balanced_rates)

# exact rational convergence sample against beta values
def beta_int(i,j):
    from math import factorial
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

samples=[]
for q in [2,3,4,5,8,16,32,64]:
    vals=[]
    for i,j in [(1,2),(2,2),(1,3),(2,3),(3,3)]:
        vals.append((i,j,G(q,i,j),beta_int(i,j),abs(G(q,i,j)-beta_int(i,j))))
    samples.append((q,vals))
    if q==64:
        for i,j,g,b,e in vals:
            ck(e < Fraction(1,20), (i,j,g,b,e))

print("R11-I0054-U039-C060 exact self-check")
print("ASSERTIONS", ASSERTIONS)
print("B(2,2) word", ''.join(map(str,w)))
print("N4_pair_rate_multiset", ','.join(map(str,sorted(pair_rates))))
print("N4_1v3_rate_multiset", ','.join(map(str,sorted(triple_rates))))
print("N4_2v2_rate_multiset", ','.join(map(str,sorted(balanced_rates))))
print("q2_total_rate", total_rate(2), "delta", mesh_delta(2), "delta_A", mesh_delta(2)*total_rate(2), "delta_A2", mesh_delta(2)*total_rate(2)**2)
print("q64_total_rate", total_rate(64), "delta_A2", mesh_delta(64)*total_rate(64)**2)
for q,vals in samples:
    line = ["q="+str(q)]
    for i,j,g,b,e in vals:
        line.append(f"G({i},{j})={g};err={e}")
    print(" | ".join(line))
print("ALL_EXACT_CHECKS_PASS")
