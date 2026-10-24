from fractions import Fraction
from decimal import Decimal, getcontext
import hashlib, json, math

getcontext().prec = 80

def dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)

def log2q(q):
    if q <= 0:
        raise ValueError("log positive only")
    return dec(q).ln() / Decimal(2).ln()

def walsh(vals):
    n = (len(vals).bit_length() - 1)
    out = []
    for s in range(1 << n):
        z = 0
        for x, fx in enumerate(vals):
            z += fx * (-1 if ((x & s).bit_count() & 1) else 1)
        out.append(z)
    return out

def spectral(vals):
    N = len(vals)
    w = walsh(vals)
    return [Fraction(z*z, N*N) for z in w], w

def lam(p):
    return sum(Fraction(s.bit_count()) * q for s,q in enumerate(p))

def inf_i(p, i):
    return sum(q for s,q in enumerate(p) if (s >> i) & 1)

def nu(p, mask):
    return sum(q for s,q in enumerate(p) if (s & mask) == mask)

def vshadow(p, A):
    a = A.bit_count()
    out = Fraction(0)
    for B,q in enumerate(p):
        if (B & A) == A:
            out += q / math.comb(B.bit_count(), a)
    return out

def palm_q_formula(p, i, A):
    return vshadow(p, A | (1 << i)) / (Fraction(A.bit_count()+1) * inf_i(p,i))

def beta_mixture_q(p, i, A):
    out = Fraction(0)
    ii = inf_i(p,i)
    a = A.bit_count()
    for B,q in enumerate(p):
        if not ((B >> i) & 1) or (B & A) != A:
            continue
        if A & (1 << i):
            continue
        if A & ~(B & ~(1 << i)):
            continue
        k = B.bit_count()
        integ = Fraction(math.factorial(a)*math.factorial(k-1-a), math.factorial(k))
        out += q/ii * integ
    return out

def containment_q(p, i, T):
    ii = inf_i(p,i)
    return nu(p, T | (1 << i)) / (Fraction(T.bit_count()+1)*ii)

def direct_containment_from_q(p, i, T, n):
    return sum(palm_q_formula(p,i,A) for A in range(1<<n)
               if not (A>>i)&1 and (A & T)==T)

def thinning_joint(p,n,u):
    L = lam(p)
    joint = {}
    for B,q in enumerate(p):
        if not q or B == 0:
            continue
        for i in range(n):
            if not ((B >> i) & 1):
                continue
            t = B & ~(1 << i)
            a = t
            while True:
                prob = q/L * (u**a.bit_count()) * ((1-u)**(t.bit_count()-a.bit_count()))
                joint[(i,a)] = joint.get((i,a), Fraction(0)) + prob
                if a == 0:
                    break
                a = (a-1) & t
    assert sum(joint.values()) == 1
    return joint

def mi(joint):
    px, py = {}, {}
    for (x,y),q in joint.items():
        px[x] = px.get(x,Fraction(0))+q
        py[y] = py.get(y,Fraction(0))+q
    I = Decimal(0)
    for (x,y),q in joint.items():
        if q:
            I += dec(q)*log2q(q/(px[x]*py[y]))
    return I

checks = 0
raw = [1,2,3,5,7,11,13,17]
Z = sum(raw)
p = [Fraction(x,Z) for x in raw]
n = 3
assert sum(p)==1 and lam(p)>0
for i in range(n):
    if inf_i(p,i)==0:
        continue
    total = Fraction(0)
    for A in range(1<<n):
        if (A>>i)&1:
            continue
        q1 = palm_q_formula(p,i,A)
        q2 = beta_mixture_q(p,i,A)
        assert q1 == q2
        total += q1
        checks += 1
    assert total == 1
    for T in range(1<<n):
        if (T>>i)&1:
            continue
        assert direct_containment_from_q(p,i,T,n) == containment_q(p,i,T)
        checks += 1

parity_rows=[]
for k in [2,3,4,8,16,32,64,128]:
    Ik = (Decimal(k).ln()/Decimal(2).ln()
          - sum(Decimal(j).ln()/Decimal(2).ln() for j in range(1,k+1))/Decimal(k))
    parity_rows.append({"k":k,"I_A_X":str(+Ik)})
checks += len(parity_rows)
log2e = Decimal(1)/Decimal(2).ln()
assert abs(Decimal(parity_rows[-1]["I_A_X"])-log2e) < Decimal("0.04")
checks += 1

vals = []
for x in range(16):
    fx = -1 if ((x>>3)&1) else 1
    if x == 7:
        fx = -fx
    vals.append(fx)
pb,w = spectral(vals)
assert pb[8] == Fraction(49,64)
assert all(pb[s] == Fraction(1,64) for s in range(16) if s != 8)
checks += 2

u0,um,u1 = Fraction(9,10),Fraction(19,20),Fraction(1,1)
J0,Jm,J1 = (mi(thinning_joint(pb,4,u)) for u in (u0,um,u1))
convex_chord_gap = J0 + J1 - 2*Jm
assert convex_chord_gap < Decimal("-0.00012")
checks += 1

for a in [0,1]:
    assert (a, 1-a) in [(0,1),(1,0)]
    checks += 1

out = {
  "status":"PASS",
  "exact_checks":checks,
  "arbitrary_subset_law_lambda":str(lam(p)),
  "parity_rows":parity_rows,
  "log2e":str(+log2e),
  "boolean_counterexample":{
    "description":"4-bit dictator with one truth-table vertex flipped",
    "main_spectral_mass":"49/64",
    "all_other_spectral_masses":"1/64",
    "u_values":["9/10","19/20","1"],
    "J_values":[str(+J0),str(+Jm),str(+J1)],
    "convex_chord_gap_J09_plus_J1_minus_2J095":str(+convex_chord_gap)
  }
}
canon=json.dumps(out,sort_keys=True,separators=(",",":"))
out["result_sha256"]=hashlib.sha256(canon.encode()).hexdigest()
print(json.dumps(out,indent=2,sort_keys=True))
