#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter
import hashlib, json

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
 (TOP, BOT),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
 ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00", "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
 ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
 ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]
# Original variables 0..8 are core x_0..x_8; 9..17 are auxiliary y_0..y_8.
# Fix y_0..y_7 to 00011011, leave y_8 free.
FIX = {9:0,10:0,11:0,12:1,13:1,14:0,15:1,16:1}
FREE = [0,1,2,3,4,5,6,7,8,17]

def reconstruct():
    base = int("".join(SLICES[0]),16)
    masks = [int("".join(row),16)^base for row in SLICES[1:]]
    assert all((m & base)==0 and m.bit_count()==2 for m in masks)
    seen=base
    hosts=[]
    for m in masks:
        assert not (seen & m)
        seen |= m
        hosts.append([x for x in range(512) if (m>>x)&1])
    core=[-1 if (base>>x)&1 else 1 for x in range(512)]
    table=[]
    for y in range(1<<9):
        row=core.copy()
        for j,cells in enumerate(hosts):
            if (y>>j)&1:
                for x in cells: row[x]=-1
        table.extend(row)
    digest=hashlib.sha256(",".join(map(str,table)).encode()).hexdigest()
    assert digest==EXPECTED_SHA
    assert sum(table)==0
    return table,hosts

def restrict(table):
    out=[]
    for z in range(1<<len(FREE)):
        idx=sum(((z>>loc)&1)<<j for loc,j in enumerate(FREE))
        idx += sum(v<<j for j,v in FIX.items())
        out.append(table[idx])
    assert len(out)==1024 and sum(out)==0
    return out

def fwht(a):
    a=list(map(int,a)); n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return a

def ln_interval(q, N=20):
    assert Fraction(1)<=q<=Fraction(2)
    z=(q-1)/(q+1)
    s=Fraction()
    for n in range(N):
        s += 2*z**(2*n+1)/(2*n+1)
    if not z: return s,s
    rem = 2*z**(2*N+1)/((2*N+1)*(1-z*z))
    return s,s+rem

LN2_LO,LN2_HI=ln_interval(Fraction(2),20)

def log2_int_interval(x):
    k=x.bit_length()-1
    y=Fraction(x,1<<k)
    lo,hi=ln_interval(y,20)
    return Fraction(k)+lo/LN2_HI, Fraction(k)+hi/LN2_LO

def entropy_interval(hist):
    hlo=Fraction(); hhi=Fraction()
    for x,c in hist.items():
        llo,lhi=log2_int_interval(x)
        mass=Fraction(c*x,1<<20)
        hlo += mass*(20-lhi)
        hhi += mass*(20-llo)
    return hlo,hhi

def composition_prime_certificate(g):
    n=10
    checked=0
    min_distinct=1<<30
    full=(1<<n)-1
    for A_mask in range(1,full):
        r=A_mask.bit_count()
        if r<2 or r>n-1:
            continue
        checked += 1
        A=[i for i in range(n) if (A_mask>>i)&1]
        B=[i for i in range(n) if not ((A_mask>>i)&1)]
        seen=set()
        for avec in range(1<<len(A)):
            abase=sum(((avec>>t)&1)<<i for t,i in enumerate(A))
            row=[]
            for bvec in range(1<<len(B)):
                idx=abase + sum(((bvec>>t)&1)<<i for t,i in enumerate(B))
                row.append(g[idx])
            seen.add(tuple(row))
            if len(seen)>=3:
                break
        min_distinct=min(min_distinct,len(seen))
        assert len(seen)>=3, (A_mask,len(seen))
    assert checked==1012
    return checked,min_distinct

def minmax_certificate(g):
    n=10; full=(1<<n)-1
    mins=[]
    maxclauses=[]
    for z,v in enumerate(g):
        if v==-1:
            if all(((z>>j)&1)==0 or g[z & ~(1<<j)]==1 for j in range(n)):
                mins.append(z)
        else:
            if all(((z>>j)&1)==1 or g[z | (1<<j)]==-1 for j in range(n)):
                maxclauses.append(full^z)
    m=84; c=566
    assert m in mins and c in maxclauses and (m&c).bit_count()==2
    return mins,maxclauses,m,c

def main():
    table,hosts=reconstruct()
    g=restrict(table)
    W=fwht(g)
    N=len(g)
    assert sum(w*w for w in W)==N*N
    hist=Counter(w*w for w in W if w)
    expected={16:337,144:108,64:48,1296:36,1024:34,576:32,256:28,
              1600:24,784:18,6400:16,7056:12,53824:8,9216:8,5184:8,
              3136:8,2304:8,12544:4,38416:1}
    assert dict(hist)==expected
    infl_num=sum(s.bit_count()*w*w for s,w in enumerate(W))
    I=Fraction(infl_num,N*N)
    assert I==Fraction(257,128)
    indiv=[]
    for j,orig in enumerate(FREE):
        num=sum(w*w for s,w in enumerate(W) if (s>>j)&1)
        indiv.append((orig,Fraction(num,N*N)))
    assert all(v>0 for _,v in indiv)
    hlo,hhi=entropy_interval(hist)
    support_deficit=I-1
    rlo=hlo/support_deficit
    rhi=hhi/support_deficit
    C0=Fraction(64548,10000)
    clo=4*(rlo-C0)
    chi=4*(rhi-C0)
    candidate_cap=Fraction(64559,10000) # 6.4559
    and_floor=Fraction(43974201,10_000_000_000) # 0.0043974201 quoted live
    assert rlo > candidate_cap
    assert clo > and_floor
    blocks_checked,min_cofactors=composition_prime_certificate(g)
    mins,maxclauses,m,c=minmax_certificate(g)
    report={
      "source_sha256":EXPECTED_SHA,
      "restriction_fix":FIX,
      "free_original_variables":FREE,
      "balanced":sum(g)==0,
      "essential_influences":[[orig,str(v)] for orig,v in indiv],
      "I_exact":str(I),
      "I_minus_1_exact":str(support_deficit),
      "nonzero_fourier_coefficients":sum(hist.values()),
      "walsh_square_histogram":dict(sorted(hist.items())),
      "entropy_lower":format(float(hlo),".16f"),
      "entropy_upper":format(float(hhi),".16f"),
      "entropy_interval_width_upper":float(hhi-hlo),
      "support_deficit_ratio_lower":format(float(rlo),".16f"),
      "support_deficit_ratio_upper":format(float(rhi),".16f"),
      "readonce_candidate_cap_6_4559_beaten":True,
      "cG_at_C0_lower":format(float(clo),".16f"),
      "cG_at_C0_upper":format(float(chi),".16f"),
      "quoted_AND_margin_0_0043974201_beaten":True,
      "minterm_local_mask":m,
      "maxterm_clause_local_mask":c,
      "minterm_original_variables":[FREE[j] for j in range(10) if (m>>j)&1],
      "maxterm_original_variables":[FREE[j] for j in range(10) if (c>>j)&1],
      "minterm_maxterm_intersection_size":(m&c).bit_count(),
      "read_once_AND_OR_refuted_by_Gurvich_criterion":True,
      "composition_prime":True,
      "composition_blocks_checked":blocks_checked,
      "minimum_distinct_cofactors_observed":min_cofactors
    }
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
