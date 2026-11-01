from fractions import Fraction
import hashlib
from collections import Counter

C0 = Fraction(16137,2500)
CSTAR = Fraction(4076157,625000)
DELTA = CSTAR-C0
A = 4*DELTA

EXPECTED_PARENT_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
EXPECTED_WITNESS_SHA = "3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
    (TOP, BOT),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
    ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00",
     "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
    ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
    ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]
FIXED={9:0,10:0,11:0,12:1,13:1,14:0,15:1,16:1}
FREE=[0,1,2,3,4,5,6,7,8,17]

def reconstruct_parent():
    base = int("".join(SLICES[0]),16)
    masks=[int("".join(row),16)^base for row in SLICES[1:]]
    seen=base; hosts=[]
    for mask in masks:
        assert mask.bit_count()==2 and not(seen&mask)
        seen |= mask
        hosts.append([x for x in range(512) if (mask>>x)&1])
    core=[-1 if (base>>x)&1 else 1 for x in range(512)]
    table=[]
    for y in range(512):
        row=core.copy()
        for j,cells in enumerate(hosts):
            if (y>>j)&1:
                for x in cells: row[x]=-1
        table.extend(row)
    assert hashlib.sha256(",".join(map(str,table)).encode()).hexdigest()==EXPECTED_PARENT_SHA
    return table

def restrict_parent(parent):
    base=sum(v<<i for i,v in FIXED.items())
    out=[]
    for z in range(1<<len(FREE)):
        idx=base
        for j,i in enumerate(FREE):
            idx |= ((z>>j)&1)<<i
        out.append(parent[idx])
    assert hashlib.sha256(",".join(map(str,out)).encode()).hexdigest()==EXPECTED_WITNESS_SHA
    return out

def face_type(vals):
    neg=sum(v==-1 for v in vals)
    if neg in (0,4): return "constant"
    if neg==2:
        if vals[0]==vals[3] and vals[1]==vals[2] and vals[0]!=vals[1]:
            return "xor"
        return "unary"
    return "and"

def d2sq(vals):
    d=Fraction(vals[0]-vals[1]-vals[2]+vals[3],4)
    return d*d

def direct_face_defect(ft):
    if ft in ("constant","unary"): return Fraction(0)
    if ft=="and": return A/Fraction(16)
    if ft=="xor": return CSTAR
    raise AssertionError

for mask in range(16):
    vals=[-1 if (mask>>k)&1 else 1 for k in range(4)]
    ft=face_type(vals)
    x=Fraction(1 if ft=="xor" else 0)
    rhs=DELTA*d2sq(vals)+C0*x
    assert direct_face_defect(ft)==rhs

w=restrict_parent(reconstruct_parent())
n=10
counts=Counter()
sum_d2=Fraction(0)
sum_x=Fraction(0)
for i in range(n):
    for j in range(i+1,n):
        outside=[k for k in range(n) if k not in (i,j)]
        for z in range(1<<len(outside)):
            base=0
            for t,k in enumerate(outside):
                base |= ((z>>t)&1)<<k
            vals=[]
            for bj in (0,1):
                for bi in (0,1):
                    idx=base | (bi<<i) | (bj<<j)
                    vals.append(w[idx])
            ft=face_type(vals)
            counts[ft]+=1
            sum_d2 += d2sq(vals)
            if ft=="xor": sum_x += 1

assert counts == Counter({"constant":6894,"unary":2882,"and":1744})
assert sum_x==0
factorial_moment = sum_d2/Fraction(1<<(n-2))
assert factorial_moment == Fraction(109,64)
pairs=Fraction(n*(n-1),2)
T2 = DELTA*factorial_moment/pairs + C0*(sum_x/Fraction(1<<(n-2)))/pairs
assert T2 == Fraction(1522621,600000000)

print("PASS")
print("C0", float(C0), "Cstar", float(CSTAR), "delta", float(DELTA))
print("two_bit_truth_tables_checked", 16)
print("G10_face_counts", dict(counts))
print("G10_total_faces", sum(counts.values()))
print("G10_sum_pair_mixed_energy", str(factorial_moment))
print("G10_average_terminal_reserve_exact", str(T2))
print("G10_average_terminal_reserve_decimal", f"{float(T2):.15f}")
print("G10_xor_face_probability_sum", str(sum_x))
print("full_FEI", "OPEN_NOT_PROVED")
