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
FIX = {9:0,10:0,11:0,12:1,13:1,14:0,15:1,16:1}
FREE = [0,1,2,3,4,5,6,7,8,17]
C0 = Fraction(64548,10000)
AND_MARGIN = Fraction(43974201,10_000_000_000)
AND_RATIO_THRESHOLD = C0 + AND_MARGIN/4

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
    return table

def restrict_g10(table):
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

def hyperplane_restriction(g,a,b,n=10):
    # Restrict a dot x = b. The least nonzero bit of a is solved for;
    # the remaining n-1 bits are free coordinates on the hyperplane.
    assert 0<a<(1<<n) and b in (0,1)
    pivot=(a & -a).bit_length()-1
    free=[i for i in range(n) if i!=pivot]
    out=[]
    for z in range(1<<(n-1)):
        x=0
        for t,i in enumerate(free):
            if (z>>t)&1: x |= 1<<i
        parity=(a & x).bit_count() & 1
        if parity ^ b: x |= 1<<pivot
        assert ((a & x).bit_count() & 1)==b
        out.append(g[x])
    return out

def add_independent(basis,v):
    x=v
    for p in sorted(basis,reverse=True):
        if (x>>p)&1: x ^= basis[p]
    if not x: return False
    basis[x.bit_length()-1]=x
    return True

def minimum_basis_influence(h):
    # For displacement a in F_2^m, q(a)=Pr[h(x)!=h(x+a)].
    # Under an invertible linear reparameterization, total influence is the
    # sum of q(a_j) over a basis {a_j}. Minimum-weight basis in this vector
    # matroid is therefore obtained exactly by greedy sorting.
    N=len(h); m=N.bit_length()-1
    W=fwht(h)
    w2=[w*w for w in W]
    corr_num=fwht(w2)
    candidates=[]
    for a in range(1,N):
        diff=N*N-corr_num[a]
        assert diff%2==0
        candidates.append((diff//2,a))
    candidates.sort()
    basis={}; chosen=[]; total=0
    for num,a in candidates:
        if add_independent(basis,a):
            chosen.append((a,num)); total += num
            if len(chosen)==m: break
    assert len(chosen)==m
    return Fraction(total,N*N), chosen, W

def ln_interval(q,N=30):
    assert Fraction(1)<=q<=Fraction(2)
    z=(q-1)/(q+1)
    s=Fraction()
    for n in range(N):
        s += 2*z**(2*n+1)/(2*n+1)
    if not z: return s,s
    rem=2*z**(2*N+1)/((2*N+1)*(1-z*z))
    return s,s+rem

LN2_LO,LN2_HI=ln_interval(Fraction(2),30)
LOG_CACHE={}
def log2_int_interval(x):
    if x in LOG_CACHE: return LOG_CACHE[x]
    k=x.bit_length()-1
    y=Fraction(x,1<<k)
    lo,hi=ln_interval(y,30)
    ans=(Fraction(k)+lo/LN2_HI, Fraction(k)+hi/LN2_LO)
    LOG_CACHE[x]=ans
    return ans

def entropy_interval(W):
    N=len(W); expo=2*(N.bit_length()-1); NN=N*N
    hist=Counter(w*w for w in W if w)
    hlo=Fraction(); hhi=Fraction()
    for x,c in hist.items():
        llo,lhi=log2_int_interval(x)
        mass=Fraction(c*x,NN)
        hlo += mass*(expo-lhi)
        hhi += mass*(expo-llo)
    return hlo,hhi,hist

def dec(f,digits=18):
    # display only; every decision below uses exact Fraction comparisons
    return format(float(f),f".{digits}g")

def main():
    g10=restrict_g10(reconstruct())
    total=0; balanced=0; eligible=0
    records=[]
    for a in range(1,1<<10):
        for b in (0,1):
            total += 1
            h=hyperplane_restriction(g10,a,b)
            if sum(h)!=0: continue
            balanced += 1
            Imin,chosen,W=minimum_basis_influence(h)
            if Imin<=1: continue
            eligible += 1
            hlo,hhi,hist=entropy_interval(W)
            rlo=hlo/(Imin-1); rhi=hhi/(Imin-1)
            # Stronger than merely staying below the positive AND margin:
            # every balanced affine hyperplane remains below C0 itself.
            assert rhi < C0
            assert rhi < AND_RATIO_THRESHOLD
            records.append((a,b,Imin,chosen,hlo,hhi,rlo,rhi,hist))
    assert total==2046
    assert balanced==570 and eligible==570

    # Exact maximum certification. Candidate class is identified by exact
    # influence and exact Walsh-square histogram; equal data imply equal ratio.
    best=max(records,key=lambda r:r[7])
    best_hist=best[8]; best_I=best[2]
    ties=[r for r in records if r[2]==best_I and r[8]==best_hist]
    assert len(ties)==256
    rep=min(ties,key=lambda r:(r[0],r[1]))
    non_tie_upper=max(r[7] for r in records if not (r[2]==best_I and r[8]==best_hist))
    assert non_tie_upper < rep[6]
    assert rep[0]==576 and rep[1]==1
    assert rep[2]==Fraction(257,128)

    a,b,Imin,chosen,hlo,hhi,rlo,rhi,hist=rep
    c_lo=4*(rlo-C0); c_hi=4*(rhi-C0)
    assert c_hi < 0
    report={
      "PASS":True,
      "source_sha256":EXPECTED_SHA,
      "g10_source_peer":"account04/B13/20260922T0055Z-arity10-prime-falsifier",
      "affine_hyperplanes_total":total,
      "balanced_affine_hyperplanes":balanced,
      "balanced_with_Imin_gt_1":eligible,
      "linear_reparameterization_optimization":"exact minimum-weight basis in F2^9 vector matroid",
      "global_maximizer_tie_count":len(ties),
      "representative_normal_decimal":a,
      "representative_normal_bits":[i for i in range(10) if (a>>i)&1],
      "representative_rhs":b,
      "representative_relation":"local coordinate 6 XOR local coordinate 9 = 1 (x6 XOR y8 = 1)",
      "Imin_exact":str(Imin),
      "chosen_basis_cost_numerators":[[v,num] for v,num in chosen],
      "entropy_lower_approx":dec(hlo),
      "entropy_upper_approx":dec(hhi),
      "entropy_interval_width_upper":dec(hhi-hlo),
      "ratio_lower_approx":dec(rlo),
      "ratio_upper_approx":dec(rhi),
      "next_best_nontie_ratio_upper_approx":dec(non_tie_upper),
      "C0_exact":str(C0),
      "AND_ratio_threshold_exact":str(AND_RATIO_THRESHOLD),
      "gap_below_C0_lower_bound":dec(C0-rhi),
      "gap_below_AND_ratio_threshold":dec(AND_RATIO_THRESHOLD-rhi),
      "cG_at_C0_lower_approx":dec(c_lo),
      "cG_at_C0_upper_approx":dec(c_hi),
      "walsh_abs_histogram":dict(sorted(Counter(abs(w) for w in fwht(hyperplane_restriction(g10,a,b)) if w).items())),
      "claim":"No balanced codimension-one affine restriction of G10, under any affine F2^9 parametrization, beats even C0 at uniform bias."
    }
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
