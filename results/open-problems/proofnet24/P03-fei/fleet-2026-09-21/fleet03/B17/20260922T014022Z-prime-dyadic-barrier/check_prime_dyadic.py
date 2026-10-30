"""Exact checker for fleet03/B17 explicit prime-gate / dyadic-restriction barrier.

Reconstructs the source-exact 10-input balanced monotone witness from the
Numaro 18-input seed. Proves:
  (i) the 10-input witness is composition-prime under arbitrary disjoint
      Boolean block composition, via a row-state criterion;
  (ii) the root gate violates the read-once quadratic-correction threshold
       c=0.01 at uniform bias;
  (iii) every proper physical restriction whose uniform output measure is
        dyadic (min(q,1-q)=2^{-k}) has nonpositive correction margin for the
        exact dyadic read-once fixed-point value Gamma(2^{-k}); equality cases
        are literal AND/OR subcubes with dummies.
No floating-point comparison decides a theorem statement.
"""
from fractions import Fraction
from collections import Counter, defaultdict
import hashlib
import itertools

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
FIXED = {9:0, 10:0, 11:0, 12:1, 13:1, 14:0, 15:1, 16:1}
FREE = [0,1,2,3,4,5,6,7,8,17]
C0 = Fraction(16137,2500)  # 6.4548
LOG_TERMS = 70

def reconstruct_parent():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    seen = base
    hosts = []
    for mask in masks:
        assert mask.bit_count() == 2
        assert not (seen & mask)
        seen |= mask
        hosts.append([x for x in range(512) if (mask >> x) & 1])
    core = [-1 if (base >> x) & 1 else 1 for x in range(512)]
    table = []
    for y in range(512):
        row = core.copy()
        for j,cells in enumerate(hosts):
            if (y >> j) & 1:
                for x in cells:
                    row[x] = -1
        table.extend(row)
    assert hashlib.sha256(",".join(map(str,table)).encode()).hexdigest() == EXPECTED_PARENT_SHA
    return table

def restrict_parent(parent):
    base = sum(v << i for i,v in FIXED.items())
    out = []
    for z in range(1 << len(FREE)):
        idx = base
        for j,i in enumerate(FREE):
            idx |= ((z >> j) & 1) << i
        out.append(parent[idx])
    assert hashlib.sha256(",".join(map(str,out)).encode()).hexdigest() == EXPECTED_WITNESS_SHA
    return out

def fwht_int(a):
    a = list(a)
    h = 1
    while h < len(a):
        for start in range(0,len(a),2*h):
            for j in range(start,start+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return a

def pow2(k):
    return Fraction(1<<k,1) if k >= 0 else Fraction(1,1<<(-k))

def normalize_pow2(x):
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    while x < pow2(k): k -= 1
    while x >= pow2(k+1): k += 1
    y = x / pow2(k)
    return k,y

def ln_interval_unit(y):
    assert 1 <= y <= 2
    z = (y-1)/(y+1)
    if z == 0:
        return Fraction(0),Fraction(0)
    z2 = z*z
    zp = z
    s = Fraction(0)
    for j in range(LOG_TERMS):
        if j:
            zp *= z2
        s += zp/(2*j+1)
    lo = 2*s
    rem = 2*z**(2*LOG_TERMS+1)/((2*LOG_TERMS+1)*(1-z2))
    return lo,lo+rem

LN2_LO,LN2_HI = ln_interval_unit(Fraction(2))

def log2_interval(x):
    k,y = normalize_pow2(x)
    lo,hi = ln_interval_unit(y)
    return Fraction(k)+lo/LN2_HI, Fraction(k)+hi/LN2_LO

def entropy_interval(table):
    N = len(table)
    W = fwht_int(table)
    assert sum(x*x for x in W) == N*N
    hist = Counter(abs(x) for x in W if x)
    lo = hi = Fraction(0)
    for a,count in hist.items():
        p = Fraction(a*a,N*N)
        llo,lhi = log2_interval(1/p)
        lo += count*p*llo
        hi += count*p*lhi
    return lo,hi,tuple(sorted(hist.items()))

def influence(table):
    N = len(table)
    n = N.bit_length()-1
    edges = 0
    for i in range(n):
        bit = 1<<i
        edges += sum(table[x] != table[x|bit] for x in range(N) if not (x&bit))
    return Fraction(edges,N//2)

def subtable(table,state):
    free = [i for i,s in enumerate(state) if s == -1]
    base = sum(s<<i for i,s in enumerate(state) if s != -1)
    out = []
    for z in range(1<<len(free)):
        x = base
        for j,i in enumerate(free):
            x |= ((z>>j)&1)<<i
        out.append(table[x])
    return out

def row_state_count(table,Bmask):
    n = len(table).bit_length()-1
    B=[i for i in range(n) if (Bmask>>i)&1]
    C=[i for i in range(n) if not ((Bmask>>i)&1)]
    rows=set()
    for aa in range(1<<len(B)):
        row=[]
        for cc in range(1<<len(C)):
            x=0
            for j,i in enumerate(B): x |= ((aa>>j)&1)<<i
            for j,i in enumerate(C): x |= ((cc>>j)&1)<<i
            row.append(table[x])
        rows.add(tuple(row))
    return len(rows)

def rare_sign_is_subcube(table):
    N=len(table); m=N.bit_length()-1
    neg=sum(v==-1 for v in table)
    if neg <= N//2:
        target=-1; r=neg
    else:
        target=+1; r=N-neg
    pts=[x for x,v in enumerate(table) if v==target]
    if not pts: return False,None
    fixed={}
    free=[]
    for i in range(m):
        bits={(x>>i)&1 for x in pts}
        if len(bits)==1: fixed[i]=next(iter(bits))
        else: free.append(i)
    expected=1<<len(free)
    if len(pts)!=expected: return False,None
    base=sum(v<<i for i,v in fixed.items())
    generated=set()
    for z in range(1<<len(free)):
        x=base
        for j,i in enumerate(free):
            x |= ((z>>j)&1)<<i
        generated.add(x)
    return set(pts)==generated, len(fixed)

def and_entropy_interval(k):
    table=[1]*(1<<k)
    table[-1]=-1
    return entropy_interval(table)[:2]

def main():
    witness=restrict_parent(reconstruct_parent())
    assert sum(witness)==0
    Iroot=influence(witness)
    assert Iroot==Fraction(257,128)
    Hroot_lo,Hroot_hi,_=entropy_interval(witness)
    root_threshold=(Iroot-1)*(C0+Fraction(1,400))
    assert Hroot_lo > root_threshold

    profile=defaultdict(Counter)
    min_by_size={}
    for mask in range(1,(1<<10)-1):
        s=mask.bit_count()
        if s<2: continue
        c=row_state_count(witness,mask)
        profile[s][c]+=1
        min_by_size[s]=min(min_by_size.get(s,c),c)
        assert c>=3
    assert min_by_size=={2:3,3:5,4:8,5:9,6:7,7:6,8:4,9:3}

    counts=Counter()
    signatures=set()
    strict_gaps=[]
    for state in itertools.product((-1,0,1),repeat=10):
        if all(s==-1 for s in state):
            continue
        t=subtable(witness,state)
        N=len(t)
        neg=sum(v==-1 for v in t)
        r=min(neg,N-neg)
        if r==0:
            continue
        ratio=N//r
        if r*ratio != N or ratio&(ratio-1):
            continue
        k=ratio.bit_length()-1
        if k<1:
            continue
        I=influence(t)
        V=Fraction(4*r*(N-r),N*N)
        if I==V:
            continue
        Hlo,Hhi,hist=entropy_interval(t)
        HAk_lo,HAk_hi=and_entropy_interval(k)
        IAk=Fraction(k,1<<(k-1))
        Dlo=C0*(I-IAk)+HAk_lo-Hhi

        signatures.add((len(t).bit_length()-1,neg,I,hist))
        if Dlo>0:
            counts[(k,"strict")]+=1
            strict_gaps.append(Dlo)
        else:
            ok,codim=rare_sign_is_subcube(t)
            assert ok and codim==k
            assert I==IAk
            counts[(k,"equality")]+=1

    expected=Counter({
        (1,"strict"):460,
        (2,"strict"):264,
        (2,"equality"):9888,
        (3,"equality"):2928,
        (4,"equality"):102,
        (5,"equality"):6,
    })
    assert counts==expected
    assert len(signatures)==51
    assert strict_gaps
    min_gap=min(strict_gaps)
    assert min_gap > Fraction(1,30)

    print("PASS")
    print("witness_sha256",EXPECTED_WITNESS_SHA)
    print("root_I",Iroot)
    print("root_H_lower_gt_6_509836127588151479", Hroot_lo > Fraction(6509836127588151479,10**18))
    print("composition_prime",True)
    print("row_state_min_by_block_size",dict(sorted(min_by_size.items())))
    print("dyadic_proper_restrictions_positive_denominator",sum(counts.values()))
    print("dyadic_counts",sorted((k,kind,v) for (k,kind),v in counts.items()))
    print("unique_dyadic_signatures",len(signatures))
    print("strict_defect_min_gt_1_over_30",min_gap > Fraction(1,30))
    print("interpretation","all dyadic proper descendants have c<=0; equality iff literal AND/OR subcube with dummies")
    print("full_FEI","OPEN_NOT_PROVED")

if __name__=="__main__":
    main()
