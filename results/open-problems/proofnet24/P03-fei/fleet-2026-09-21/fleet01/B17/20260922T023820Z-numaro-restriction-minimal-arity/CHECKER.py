from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import hashlib, json

CORE_HEX = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
HOSTS = [(78,79),(113,121),(228,484),(170,186),(149,151),(338,466),(284,316),(291,295),(393,457)]
EXPECTED_SOURCE_SHA256 = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
CAP = F(64559,10000)
LOG_TERMS = 40

BASE = int(CORE_HEX,16)
OWNER = {x:j for j,h in enumerate(HOSTS) for x in h}
CORE = [-1 if (BASE>>x)&1 else 1 for x in range(512)]
assert all(CORE[x] == 1 for h in HOSTS for x in h)

def fwht(a):
    a=list(map(int,a)); n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def source_digest():
    vals=[]
    for y in range(512):
        for x in range(512):
            j=OWNER.get(x)
            vals.append(CORE[x] if j is None else (1 if ((y>>j)&1)==0 else -1))
    return hashlib.sha256(",".join(map(str,vals)).encode()).hexdigest()

def ln_unit_interval(m):
    assert F(1) <= m <= F(2)
    z=(m-1)/(m+1); z2=z*z; p=z; s=F(0)
    for j in range(LOG_TERMS):
        s += p/F(2*j+1)
        p *= z2
    lo=2*s
    rem=F(0) if z==0 else 2*p/(F(2*LOG_TERMS+1)*(1-z2))
    return lo,lo+rem

LN2 = ln_unit_interval(F(2))

@lru_cache(None)
def log2_interval(q):
    q=F(q); assert q>0
    e=q.numerator.bit_length()-q.denominator.bit_length()
    pow2=F(2**e) if e>=0 else F(1,2**(-e))
    if q < pow2:
        e-=1; pow2/=2
    m=q/pow2
    nlo,nhi=ln_unit_interval(m)
    dlo,dhi=LN2
    return F(e)+nlo/dhi, F(e)+nhi/dlo

def entropy_interval(W):
    n=len(W); den=n*n; lo=F(0); hi=F(0)
    hist=Counter(w*w for w in W if w)
    for s,mult in hist.items():
        p=F(s,den); a,b=log2_interval(F(den,s))
        lo += mult*p*a
        hi += mult*p*b
    return lo,hi,hist

def restriction_table(core_status, active, aux_status):
    free_core=[i for i,s in enumerate(core_status) if s==-1]
    m=len(free_core)
    fixed=sum((1<<i) for i,s in enumerate(core_status) if s==1)
    xs=[]
    for z in range(1<<m):
        x=fixed
        for t,i in enumerate(free_core):
            if (z>>t)&1: x |= 1<<i
        xs.append(x)
    free_aux=[active[t] for t,s in enumerate(aux_status) if s==-1]
    fixed_aux={active[t]:s for t,s in enumerate(aux_status) if s!=-1}
    apos={j:t for t,j in enumerate(free_aux)}
    vals=[]
    for u in range(1<<len(free_aux)):
        for x in xs:
            j=OWNER.get(x)
            if j is None: v=CORE[x]
            elif j in apos: v=1 if ((u>>apos[j])&1)==0 else -1
            else: v=1 if fixed_aux[j]==0 else -1
            vals.append(v)
    return vals

def dec(q, digits=55):
    from decimal import Decimal, localcontext
    with localcontext() as c:
        c.prec=digits
        return str(Decimal(q.numerator)/Decimal(q.denominator))

def main():
    assert source_digest()==EXPECTED_SOURCE_SHA256
    stats={k:{"balanced":0,"violating":0,"ambiguous":0,"max_lo":F(-1),"max_hi":F(-1),
              "max_I":None,"max_hist":None,"max_core_status":None,"max_aux_status":None}
           for k in range(11)}
    normalized=0
    for cs in product((-1,0,1),repeat=9):
        free=[i for i,s in enumerate(cs) if s==-1]; m=len(free)
        fixed=sum((1<<i) for i,s in enumerate(cs) if s==1)
        xs=[]
        for z in range(1<<m):
            x=fixed
            for t,i in enumerate(free):
                if (z>>t)&1: x|=1<<i
            xs.append(x)
        active=tuple(sorted({OWNER[x] for x in xs if x in OWNER}))
        for ast in product((-1,0,1),repeat=len(active)):
            nominal=m+sum(s==-1 for s in ast)
            if nominal>10: continue
            normalized += 1
            vals=restriction_table(cs,active,ast)
            if sum(vals)!=0: continue
            W=fwht(vals); N=len(W); den=N*N
            infnums=[sum(W[s]*W[s] for s in range(N) if (s>>j)&1) for j in range(nominal)]
            essential=sum(x>0 for x in infnums)
            I=F(sum(s.bit_count()*W[s]*W[s] for s in range(N)),den)
            hlo,hhi,hist=entropy_interval(W)
            if I==1:
                rlo=rhi=F(0)
            else:
                rlo,rhi=hlo/(I-1),hhi/(I-1)
            d=stats[essential]; d["balanced"]+=1
            if rlo>CAP: d["violating"]+=1
            elif rhi>CAP: d["ambiguous"]+=1
            if rhi>d["max_hi"]:
                d.update(max_lo=rlo,max_hi=rhi,max_I=I,max_hist=dict(sorted(hist.items())),
                         max_core_status=cs,max_aux_status=ast)
    active_stats={}
    for k,d in stats.items():
        if not d["balanced"]: continue
        active_stats[str(k)]={
            "balanced_normalized_restrictions":d["balanced"],
            "violating_cap_6.4559":d["violating"],
            "ambiguous_at_cap":d["ambiguous"],
            "max_ratio_interval":[dec(d["max_lo"]),dec(d["max_hi"])],
            "max_I_exact":str(d["max_I"]),
            "max_square_histogram":d["max_hist"],
            "max_core_status":list(d["max_core_status"]),
            "max_aux_status":list(d["max_aux_status"]),
        }
    assert normalized==44266
    assert {k:stats[k]["balanced"] for k in range(11) if stats[k]["balanced"]} == {1:3492,4:288,6:324,8:72,10:630}
    assert all(stats[k]["violating"]==0 and stats[k]["ambiguous"]==0 for k in range(10))
    assert stats[10]["violating"]==621 and stats[10]["ambiguous"]==0
    assert stats[8]["max_hi"] < CAP
    assert stats[10]["max_lo"] > CAP
    assert stats[4]["max_I"]==F(3,2)
    assert stats[6]["max_I"]==F(13,8)
    assert stats[8]["max_I"]==F(53,32)
    assert stats[10]["max_I"]==F(257,128)
    out={
      "status":"PASS",
      "source_sha256":EXPECTED_SOURCE_SHA256,
      "normalized_restrictions_nominal_arity_at_most_10":normalized,
      "coverage":"Every physical restriction with at most 10 essential variables has an equivalent representative here: free inactive/dummy auxiliary variables can be fixed without changing the function.",
      "cap_tested_exact":str(CAP),
      "effective_arity_stats":active_stats,
      "conclusion":"Within all physical restrictions of the recovered Numaro n=18 seed, no balanced restriction with <=9 essential variables violates 6.4559; balanced 10-essential-variable restrictions do, and the maximal observed interval is the peer-certified G10 value.",
      "full_FEI_status":"OPEN"
    }
    print(json.dumps(out,indent=2))

if __name__=="__main__": main()
