from fractions import Fraction
from collections import Counter, defaultdict
from itertools import product
import hashlib, json, math

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
FIXED = {9:0, 10:0, 11:0, 12:1, 13:0, 14:1, 17:1, 20:0}
FREE = [0,1,2,3,4,5,6,7,8,15]

# -------- source-bound gate reconstruction --------
def parse_hex(h):
    out=[]
    for c in h:
        v=int(c,16)
        out.extend([(v>>j)&1 for j in range(4)])
    return out

def reconstruct_g10():
    base=[]
    for a,b in SLICES:
        base.append((parse_hex(a),parse_hex(b)))
    vals=[]
    for mask in range(1<<10):
        x=[0]*21
        for j,v in FIXED.items(): x[j]=v
        for j,var in enumerate(FREE): x[var]=(mask>>j)&1
        # The source generator selects a 256-bit slice by x[0:3], then one of a/b by x[3].
        idx=x[0]+2*x[1]+4*x[2]
        pair=base[idx]
        arr=pair[x[3]]
        # Remaining original coordinates 4..8 index the 32 chunks; 15 is the final bit.
        j=x[4]+2*x[5]+4*x[6]+8*x[7]+16*x[8]
        pos=2*j+x[15]
        vals.append(arr[pos])
    raw=bytes(vals)
    assert hashlib.sha256(raw).hexdigest()==EXPECTED_WITNESS_SHA
    return vals

# -------- exact Walsh / rational spectral data --------
def fwht(a):
    a=a[:]
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def restriction_truth(root,state):
    free=[i for i,s in enumerate(state) if s==2]
    vals=[]
    for mask in range(1<<len(free)):
        x=[0]*10
        for i,s in enumerate(state):
            if s!=2: x[i]=s
        for j,i in enumerate(free): x[i]=(mask>>j)&1
        idx=sum(x[i]<<i for i in range(10))
        vals.append(root[idx])
    return vals,free

def spectrum_stats(bits):
    m=(len(bits)).bit_length()-1
    signs=[1-2*b for b in bits]
    W=fwht(signs)
    N=1<<m
    den=N*N
    pnum=[w*w for w in W]
    assert sum(pnum)==den
    I_num=0
    for s,a in enumerate(pnum): I_num += s.bit_count()*a
    mean_num=W[0]
    var=Fraction(den-mean_num*mean_num,den)
    I=Fraction(I_num,den)
    return pnum,den,I,var,W

# -------- rigorous log2 intervals using atanh series --------
# For x>0 rational, write x=2^e*y with 1<=y<2 and compute ln(y)
# from z=(y-1)/(y+1), ln y=2 sum z^(2k+1)/(2k+1).
# Positive-tail bound: remainder <= 2 z^(2K+3)/((2K+3)(1-z^2)).
# ln2 is enclosed independently using z=1/3.
def ln_interval(x,K=26):
    assert x>0
    # exact dyadic exponent e=floor(log2 x)
    n,d=x.numerator,x.denominator
    e=n.bit_length()-d.bit_length()
    if e>=0:
        while Fraction(1<<e,1)>x: e-=1
        while Fraction(1<<(e+1),1)<=x: e+=1
    else:
        while Fraction(1,1<<(-e))>x: e-=1
        while Fraction(1,1<<(-(e+1)))<=x: e+=1
    y=x/Fraction(2**e if e>=0 else 1, 1 if e>=0 else 2**(-e))
    assert 1<=y<2
    z=(y-1)/(y+1)
    S=Fraction(0)
    zp=z
    for k in range(K+1):
        S += zp/Fraction(2*k+1)
        zp *= z*z
    lo=2*S
    rem=2*zp/Fraction((2*K+3),1)/(1-z*z) if z else Fraction(0)
    hi=lo+rem
    return lo,hi,e

def ln2_interval(K=40):
    z=Fraction(1,3); S=Fraction(0); zp=z
    for k in range(K+1):
        S+=zp/Fraction(2*k+1); zp*=z*z
    lo=2*S; hi=lo+2*zp/Fraction(2*K+3)/(1-z*z)
    return lo,hi

LN2_LO,LN2_HI=ln2_interval()

def log2_interval(x):
    lo,hi,e=ln_interval(x)
    # log2 x=e+ln(y)/ln2, all ln(y)>=0
    return Fraction(e)+lo/LN2_HI, Fraction(e)+hi/LN2_LO

def entropy_interval(pnum,den):
    # H=sum p log2(1/p). For dyadic rational p; use rigorous interval.
    lo=Fraction(0); hi=Fraction(0)
    for a in pnum:
        if not a: continue
        p=Fraction(a,den)
        # if p is reciprocal power of two, exact
        if p.numerator==1 and p.denominator & (p.denominator-1)==0:
            lg=Fraction(p.denominator.bit_length()-1)
            lo += p*lg; hi += p*lg; continue
        llo,lhi=log2_interval(Fraction(1,1)/p)
        lo+=p*llo; hi+=p*lhi
    return lo,hi

def floor_dec(q,n=15):
    z=(q.numerator*10**n)//q.denominator
    return f"{z//10**n}.{z%10**n:0{n}d}"
def ceil_dec(q,n=15):
    z=(q.numerator*10**n + q.denominator-1)//q.denominator
    return f"{z//10**n}.{z%10**n:0{n}d}"
def dec_lo(q,n=15): return floor_dec(q,n)
def dec_hi(q,n=15): return ceil_dec(q,n)


def main():
    rootbits=reconstruct_g10()
    states=list(product(range(3), repeat=10)) # 0,1 fixed; 2 free
    data={}
    byess=defaultdict(lambda:{"states":0,"equality":0,"min_slack_lo":None})
    strict_min=None; strict_state=None
    for state in states:
        bits,free=restriction_truth(rootbits,state)
        pnum,N2,I,var,W=spectrum_stats(bits)
        Hlo,Hhi=entropy_interval(pnum,N2)
        den=I-var
        slack_lo=8*den-Hhi
        slack_hi=8*den-Hlo
        # essential arity by exact restriction influence / Walsh support dependence
        ess=0
        for j in range(len(free)):
            active=any(((s>>j)&1) and a for s,a in enumerate(pnum))
            ess+=bool(active)
        assert slack_lo>=0, (state,slack_lo)
        eq=(slack_lo==0 and slack_hi==0)
        r=byess[ess]; r["states"]+=1; r["equality"]+=eq
        if r["min_slack_lo"] is None or slack_lo<r["min_slack_lo"]: r["min_slack_lo"]=slack_lo
        if ess>=3 and (strict_min is None or slack_lo<strict_min): strict_min=slack_lo; strict_state=state
        data[state]=(Hlo,Hhi,den,ess,slack_lo,slack_hi)

    assert sum(r["states"] for r in byess.values())==3**10
    assert sum(r["equality"] for r in byess.values())==22962+9054+9888

    root=(2,)*10
    Hlo,Hhi,den,ess,slo,shi=data[root]
    assert den==Fraction(129,128)
    assert ess==10
    assert slo>Fraction(3,2)

    # Exact child-continuation test. Some individual one-step residuals are negative.
    # GS8 only asks that every nonaffine state have at least one good essential coordinate,
    # so certify that adaptive statement across the complete restriction lattice.
    neg_edges=0
    edge_count=0
    min_L_hi=None; min_L_state=None
    worst_ratio_lo=None; worst_ratio_state=None
    all_bad_states=0
    min_best_resid_lo=None; min_best_state=None; min_best_coord=None
    for state,(Hlo,Hhi,den,ess,slo,shi) in data.items():
        best_resid_lo=None; best_coord=None
        for i,s in enumerate(state):
            if s!=2: continue
            edge_count+=1
            a=list(state); a[i]=0; s0=tuple(a)
            a=list(state); a[i]=1; s1=tuple(a)
            H0lo,H0hi,d0,*_=data[s0]
            H1lo,H1hi,d1,*_=data[s1]
            currency=den-(d0+d1)/2
            assert currency>=0
            Delta_lo=Hlo-(H0hi+H1hi)/2
            Delta_hi=Hhi-(H0lo+H1lo)/2
            R_lo=8*currency-Delta_hi
            R_hi=8*currency-Delta_lo
            if R_hi<0:
                neg_edges+=1
                if min_L_hi is None or R_hi<min_L_hi:
                    min_L_hi=R_hi; min_L_state=(state,i,R_lo,R_hi,currency,Delta_lo,Delta_hi)
            if currency>0:
                if best_resid_lo is None or R_lo>best_resid_lo:
                    best_resid_lo=R_lo; best_coord=i
                ratio_lo=Delta_lo/currency
                if worst_ratio_lo is None or ratio_lo>worst_ratio_lo:
                    worst_ratio_lo=ratio_lo
                    worst_ratio_state=(state,i,ratio_lo,Delta_lo,Delta_hi,currency)
        if ess>=2:
            assert best_resid_lo is not None
            if best_resid_lo<0:
                all_bad_states+=1
            assert best_resid_lo>=0
            if ess>=3 and (min_best_resid_lo is None or best_resid_lo<min_best_resid_lo):
                min_best_resid_lo=best_resid_lo
                min_best_state=state
                min_best_coord=best_coord
    assert edge_count==10*3**9
    assert neg_edges==31
    assert all_bad_states==0
    assert min_best_resid_lo>Fraction(12,100)
    assert worst_ratio_lo>Fraction(921,100)

    out={
      "status":"PASS",
      "witness_sha256":EXPECTED_WITNESS_SHA,
      "states_checked":3**10,
      "split_edges_checked":edge_count,
      "by_essential_arity":{},
      "strict_min_slack_lower":dec_lo(strict_min,15),
      "strict_min_state":"".join(map(str,strict_state)),
      "root_den_I_minus_var":str(data[root][2]),
      "root_slack_lower":dec_lo(data[root][4],15),
      "negative_one_step_edges":neg_edges,
      "all_bad_states":all_bad_states,
      "min_best_residual_lower_essential_arity_ge_3":dec_lo(min_best_resid_lo,15),
      "min_best_residual_state":"".join(map(str,min_best_state)),
      "min_best_residual_coordinate":min_best_coord,
      "most_negative_one_step_L_upper":dec_hi(min_L_hi,15),
      "worst_local_ratio_lower":dec_lo(worst_ratio_lo,15),
      "worst_local_state":"".join(map(str,worst_ratio_state[0])),
      "worst_local_split_coordinate":worst_ratio_state[1],
      "interpretation":"Every nonaffine uniform-bias coordinate restriction of G10 has a GS8-good physical continuation, although 31 individual split edges are rigorously bad."
    }
    for ess in sorted(byess):
        r=byess[ess]
        out["by_essential_arity"][str(ess)]={
           "states":r["states"],"equality_states":r["equality"],
           "min_slack_lower":dec_lo(r["min_slack_lo"],15)
        }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
