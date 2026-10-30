#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter
import hashlib, itertools, json, math

EXPECTED_SOURCE_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
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
FIX18 = {9:0,10:0,11:0,12:1,13:1,14:0,15:1,16:1}
FREE18 = [0,1,2,3,4,5,6,7,8,17]

def reconstruct18():
    base = int("".join(SLICES[0]),16)
    masks = [int("".join(row),16)^base for row in SLICES[1:]]
    assert all((m & base)==0 and m.bit_count()==2 for m in masks)
    seen=base; hosts=[]
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
                for x in cells:
                    row[x]=-1
        table.extend(row)
    digest=hashlib.sha256(",".join(map(str,table)).encode()).hexdigest()
    assert digest==EXPECTED_SOURCE_SHA and sum(table)==0
    return table

def g10_from_source(table):
    out=[]
    for z in range(1<<10):
        idx=sum(((z>>loc)&1)<<j for loc,j in enumerate(FREE18))
        idx += sum(v<<j for j,v in FIX18.items())
        out.append(table[idx])
    assert len(out)==1024 and sum(out)==0
    return out

def restrict_table(g,n,fixed):
    free=[j for j in range(n) if j not in fixed]
    out=[]
    for z in range(1<<len(free)):
        idx=sum(((z>>loc)&1)<<j for loc,j in enumerate(free))
        idx += sum(v<<j for j,v in fixed.items())
        out.append(g[idx])
    return out,free

def fwht(a):
    a=list(map(int,a)); n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return a

def ln_interval(q, terms=40):
    q=Fraction(q)
    assert Fraction(1)<=q<=Fraction(2)
    z=(q-1)/(q+1)
    s=Fraction()
    for n in range(terms):
        s += 2*z**(2*n+1)/(2*n+1)
    if not z:
        return s,s
    rem=2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return s,s+rem

LN2_LO,LN2_HI=ln_interval(Fraction(2))

def log2_int_interval(x):
    k=x.bit_length()-1
    q=Fraction(x,1<<k)
    lo,hi=ln_interval(q)
    return Fraction(k)+lo/LN2_HI, Fraction(k)+hi/LN2_LO

def spectral_interval(g):
    W=fwht(g); N=len(g); n=N.bit_length()-1
    assert sum(w*w for w in W)==N*N
    I=Fraction(sum(s.bit_count()*w*w for s,w in enumerate(W)),N*N)
    hist=Counter(w*w for w in W if w)
    hlo=Fraction(); hhi=Fraction()
    for x,c in hist.items():
        llo,lhi=log2_int_interval(x)
        mass=Fraction(c*x,N*N)
        hlo += mass*(2*n-lhi)
        hhi += mass*(2*n-llo)
    return W,I,hlo,hhi,hist

def prime_certificate(g):
    n=len(g).bit_length()-1
    full=(1<<n)-1
    checked=0; mind=1<<30
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
                idx=abase+sum(((bvec>>t)&1)<<i for t,i in enumerate(B))
                row.append(g[idx])
            seen.add(tuple(row))
            if len(seen)>=3:
                break
        mind=min(mind,len(seen))
        if len(seen)<=2:
            return False,checked,mind
    return True,checked,mind

def main():
    g10=g10_from_source(reconstruct18())
    W,I,hlo,hhi,hist=spectral_interval(g10)
    assert I==Fraction(257,128)
    root_ratio_lo=hlo/(I-1)
    root_ratio_hi=hhi/(I-1)
    assert root_ratio_lo > Fraction(64559,10000)

    prime,prime_blocks,min_cofactors=prime_certificate(g10)
    assert prime and prime_blocks==1012 and min_cofactors>=3

    canonical_g,_=restrict_table(g10,10,{0:0,3:1,6:0})
    assert sum(canonical_g)==0
    Wm,Im,Hmlo,Hmhi,histm=spectral_interval(canonical_g)
    assert Im==Fraction(13,8)
    canonical_norm_hist=Counter(Fraction(w*w,len(canonical_g)**2) for w in Wm if w)
    expected_norm_hist=Counter({
        Fraction(1,256):32,
        Fraction(1,64):4,
        Fraction(1,16):4,
        Fraction(9,64):4,
    })
    assert canonical_norm_hist==expected_norm_hist
    canonical_ratio_lo=Hmlo/(Im-1)
    canonical_ratio_hi=Hmhi/(Im-1)

    counts=Counter()
    max_by_dim={}
    all_balanced=0
    all_proper=0
    global_max_hi=Fraction(-1)
    global_max_data=None
    max_tie_count=0
    threshold=Fraction(32,5)

    for rfix in range(1,10):
        for coords in itertools.combinations(range(10),rfix):
            for vals in itertools.product((0,1), repeat=rfix):
                all_proper += 1
                fixed=dict(zip(coords,vals))
                g,free=restrict_table(g10,10,fixed)
                if sum(g)!=0:
                    continue
                all_balanced += 1
                d=10-rfix
                counts[d]+=1
                Wc,Ic,hclo,hchi,histc=spectral_interval(g)
                if Ic==1:
                    rlo=rhi=Fraction(0)
                else:
                    rlo=hclo/(Ic-1); rhi=hchi/(Ic-1)
                assert rhi < threshold
                norm_hist=Counter(Fraction(w*w,len(g)**2) for w in Wc if w)
                if Ic==Im and norm_hist==canonical_norm_hist:
                    max_tie_count += 1
                else:
                    assert rhi < canonical_ratio_lo
                if d not in max_by_dim or rhi > max_by_dim[d]["ratio_hi"]:
                    max_by_dim[d]={
                        "ratio_lo":rlo,"ratio_hi":rhi,"H_lo":hclo,"H_hi":hchi,
                        "I":Ic,"fixed":fixed,"hist":histc
                    }
                if rhi > global_max_hi:
                    global_max_hi=rhi
                    global_max_data=(d,fixed,Ic,histc,hclo,hchi)

    d,fixed,Imax,histmax,hmaxlo,hmaxhi=global_max_data
    assert Imax==Fraction(13,8)
    assert float(global_max_hi) < 6.348
    assert global_max_hi < Fraction(635,100)
    assert Fraction(64559,10000) < root_ratio_lo

    out={
      "source_truth_table_sha256": EXPECTED_SOURCE_SHA,
      "g10_balanced": True,
      "g10_I_exact": str(I),
      "g10_ratio_lower": format(float(root_ratio_lo),".15f"),
      "g10_ratio_upper": format(float(root_ratio_hi),".15f"),
      "g10_composition_prime": prime,
      "g10_prime_blocks_checked": prime_blocks,
      "g10_min_cofactors": min_cofactors,
      "proper_restrictions_checked": all_proper,
      "balanced_proper_restrictions": all_balanced,
      "balanced_counts_by_remaining_dimension": {str(k):counts[k] for k in sorted(counts)},
      "balanced_dimension_8_or_9_count": counts[8]+counts[9],
      "proper_balanced_ratio_upper_lt": "6.35",
      "proper_balanced_global_max_ratio_numeric_lower": format(float(canonical_ratio_lo),".15f"),
      "proper_balanced_global_max_ratio_numeric_upper": format(float(canonical_ratio_hi),".15f"),
      "proper_balanced_global_max_tie_count": max_tie_count,
      "proper_balanced_global_max_remaining_dimension_example": d,
      "proper_balanced_global_max_I_exact": str(Imax),
      "proper_balanced_global_max_fixed_local_coordinates": {str(k):v for k,v in fixed.items()},
      "proper_balanced_global_max_histogram": {str(k):v for k,v in sorted(histmax.items())},
      "exact_max_formula": "46/5 - (9/5)*log2(3)",
      "status": "PASS"
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
