#!/usr/bin/env python3
"""Exact packet/free-energy profiler for public FEI record seeds from teorth/optimizationproblems PR #94.

Uses only integer Walsh transforms and Fraction arithmetic for packet masses, valuations,
normalizers and influences. Logs are reported in binary64 only for descriptive entropy/D values.
Canonical PR encoding: bit x of truth_table_true_hex is 1 iff f(x)=-1.
"""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from math import log2

SEEDS = {
    "g10": {
        "n": 10,
        "hex": "fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc88eeaacc00fefefefef0f0f000feaafeaaf000f000fcfcccccf0f0c0000000000000000000fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc88eeaacc00fefefefef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000",
        "sha256": "2ec326a08661bdae8a2f830906bacd1cfa68cd17e767afd736848cbc6e4edf9f",
        "I": Fraction(257,128),
    },
    "g12": {
        "n": 12,
        "hex": "fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc88eeaacc00fefefefef0f0f000feaafeaaf0a0f000fefeccccf0f0c0000000000000000000fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc88eeaacc00fefefefef0f0f000faaafaaaf0a0f000fcfcccccf0f0c0000000000000000000fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00fefefefef0f0f000feaafeaaf0a0f000fcfcccccf0f0c0000000000000000000fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00fefefefef0f0f000faaafaaaf0a0f000fcfcccccf0f0c0000000000000000000fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc88eeaacc00fefefefef0f0f000feaafeaaf000f000fefeccccf0f0c0000000000000000000fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc88eeaacc00fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00fefefefef0f0f000feaafeaaf000f000fcfcccccf0f0c0000000000000000000fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000",
        "sha256": "ff94bc3b5fc2ea3a8fd3e6620588dda972ac7b6366e8c7597936535cd0543adb",
        "I": Fraction(259,128),
    },
    "g12*": {
        "n": 12,
        "hex": "fefefefefefefe00feaafeaafeaafe00fefeccccfefecc00feaacc88feaacc00fefefefef0f0f000feaafeaaf000f000fcfcccccf0f0c0000000000000000000fefefefefefefe00feaafeaafeaafe00fefeccccfefecc00feaacc88feaacc00fefefefef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000fefefefefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc88eeaacc00fefefefef0f0f000feaafeaaf000f000fcfcccccf0f0c0000000000000000000fefefefefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc88eeaacc00fefefefef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00feaacc88feaacc00fefefefef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000fefefefefefafe00feaafeaafeaafe00fefeccccfefacc00feaacc88feaacc00fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00fefefefef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000",
        "sha256": "35438a105857623fbd9fdcbee353b9e34b7de683d1132be37f3b1a40346cf714",
        "I": Fraction(259,128),
    },
    "g14": {
        "n": 14,
        "hex": "fefefefefefefe00feaafeaafeaafe00fefeccccfefecc00feaacc00feaacc00fefefefef0f0f000feaafeaaf0a0f000fefeccccf0f0c0000000000000000000fefefefefefefe00feaafeaafeaafe00fefeccccfefecc00feaacc00feaacc00fefefefef0f0f000faaafaaaf0a0f000fefeccccf0f0c0000000000000000000fefefefefefefe00feaafeaafeaafe00fefeccccfefecc00eeaacc00eeaacc00fefefefef0f0f000feaafeaaf0a0f000fefeccccf0f0c0000000000000000000fefefefefefefe00feaafeaafeaafe00fefeccccfefecc00eeaacc00eeaacc00fefefefef0f0f000faaafaaaf0a0f000fefeccccf0f0c0000000000000000000fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00feaacc00feaacc00fefefeeef0f0f000feaafeaaf0a0f000fefeccccf0f0c0000000000000000000fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00feaacc00feaacc00fefefeeef0f0f000faaafaaaf0a0f000fefeccccf0f0c0000000000000000000fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00fefefeeef0f0f000feaafeaaf000f000fefeccccf0f0c0000000000000000000fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00fefefeeef0f0f000faaafaaaf000f000fefeccccf0f0c0000000000000000000fefefefefefefc00feaafeaafeaafc00fefeccccfefecc00feaacc00feaacc00fefefefef0f0f000feaafeaaf0a0f000fefeccccf0f0c0000000000000000000fefefefefefefc00feaafeaafeaafc00fefeccccfefecc00feaacc00feaacc00fefefefef0f0f000faaafaaaf0a0f000fefeccccf0f0c0000000000000000000fefefefefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00fefefefef0f0f000feaafeaaf0a0f000fefeccccf0f0c0000000000000000000fefefefefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00fefefefef0f0f000faaafaaaf0a0f000fefeccccf0f000000000000000000000fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00fefefeeef0f0f000feaafeaaf0a0f000fefeccccf0f0c0000000000000000000fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00fefefeeef0f0f000faaafaaaf0a0f000fefeccccf0f0c0000000000000000000fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00fefefeeef0f0f000feaafeaaf000f000fefeccccf0f0c0000000000000000000fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000fefefefefefefe00feaafeaafeaafe00fefeccccfefecc00feaacc00feaacc00fefefefef0f0f000feaafeaaf0a0f000fcfcccccf0f0c0000000000000000000fefefefefefefe00feaafeaafeaafe00fefeccccfefecc00feaacc00feaacc00fefefefef0f0f000faaafaaaf0a0f000fcfcccccf0f0c0000000000000000000fefefefefefefe00feaafeaafeaafe00fefeccccfefecc00eeaacc00eeaacc00fefefefef0f0f000feaafeaaf000f000fcfcccccf0f0c0000000000000000000fefefefefefefe00feaafeaafeaafe00fefeccccfefecc00eeaacc00eeaacc00fefefefef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00feaacc00feaacc00fefefeeef0f0f000feaafeaaf0a0f000fcfcccccf0f0c0000000000000000000fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00feaacc00feaacc00fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f0c0000000000000000000fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f0c0000000000000000000fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000fefefefefefefc00feaafeaafeaafc00fefeccccfefecc00feaacc00feaacc00fefefefef0f0f000feaafeaaf0a0f000fcfcccccf0f0c0000000000000000000fefefefefefefc00feaafeaafeaafc00fefeccccfefecc00feaacc00feaacc00fefefefef0f0f000faaafaaaf0a0f000fcfcccccf0f0c0000000000000000000fefefefefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00fefefefef0f0f000feaafeaaf000f000fcfcccccf0f0c0000000000000000000fefefefefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00fefefeeef0f0f000feaafeaaf0a0f000fcfcccccf0f0c0000000000000000000fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f0c0000000000000000000fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f0c0000000000000000000fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000",
        "sha256": "80929c1b10f4941ba56f13dd355ebaa4c2fabb602df9125a68755c116859d527",
        "I": Fraction(521,256),
    },
}

def fwht(a):
    a = list(map(int,a))
    h = 1
    while h < len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return a

def v2(z):
    z=abs(int(z))
    assert z
    return (z & -z).bit_length()-1

def analyze(rec):
    n=rec["n"]; N=1<<n
    mask=int(rec["hex"],16)
    assert len(rec["hex"]) == N//4
    f=[-1 if ((mask>>x)&1) else 1 for x in range(N)]
    digest=sha256(",".join(map(str,f)).encode()).hexdigest()
    assert digest == rec["sha256"], (digest,rec["sha256"])
    assert sum(f)==0
    W=fwht(f)
    groups=defaultdict(list)
    for s,w in enumerate(W):
        if w:
            groups[abs(w)].append((s,1 if w>0 else -1))
    prof={}
    for mag,entries in groups.items():
        spec=[0]*N
        for s,sgn in entries:
            spec[s]=sgn
        V=fwht(spec)
        r=min(v2(z) for z in V if z)
        count=len(entries)
        p=Fraction(count*mag*mag,N*N)
        b=Fraction(mag*(1<<r),N)
        prof[mag]=(count,r,p,b)
    assert sum(x[2] for x in prof.values()) == 1
    I=sum(Fraction(w*w,N*N)*s.bit_count() for s,w in enumerate(W))
    assert I == rec["I"], (I,rec["I"])
    R=sum(p*r for count,r,p,b in prof.values())
    D=sum(float(p)*log2(1/float(b)) for count,r,p,b in prof.values())
    H=sum(float(Fraction(w*w,N*N))*log2(1/float(Fraction(w*w,N*N))) for w in W if w)
    assert abs(H-(2*float(R)+2*D)) < 1e-12
    Nnorm=sum(p/(b*b) for count,r,p,b in prof.values())
    K=log2(float(Nnorm))-2*D
    bands={}
    for r in sorted(set(x[1] for x in prof.values())):
        xs=[x for x in prof.values() if x[1]==r]
        mass=sum(x[2] for x in xs)
        db=sum(float(x[2])*log2(1/float(x[3])) for x in xs)
        nrm=sum(x[2]/(x[3]*x[3]) for x in xs)
        bands[r]=(mass,db,nrm,sum(x[0] for x in xs),len(xs))
    return dict(W=W,prof=prof,I=I,R=R,D=D,H=H,N=Nnorm,K=K,bands=bands)

def main():
    out={k:analyze(v) for k,v in SEEDS.items()}
    print("seed  nz  packets  I  H  L=H/(I-1)  R  D  N  KL")
    for k in ("g10","g12","g12*","g14"):
        a=out[k]
        L=a["H"]/float(a["I"]-1)
        print(k,sum(w!=0 for w in a["W"]),len(a["prof"]),a["I"],
              f"{a['H']:.15f}",f"{L:.15f}",a["R"],f"{a['D']:.15f}",a["N"],f"{a['K']:.15f}")
        for r,(mass,db,nrm,ncoeff,npkt) in a["bands"].items():
            print(" band",r,"mass",mass,"D",f"{db:.15f}","N",nrm,"coeff",ncoeff,"packets",npkt)
    A=out["g12*"]; B=out["g14"]
    LR_A=2*A["R"]/(A["I"]-1)
    LR_B=2*B["R"]/(B["I"]-1)
    L_A=A["H"]/float(A["I"]-1); L_B=B["H"]/float(B["I"]-1)
    print("g12*_to_g14")
    print("delta_R_exact",B["R"]-A["R"])
    print("delta_D",f"{B['D']-A['D']:.15f}")
    print("delta_L",f"{L_B-L_A:.15f}")
    print("delta_LR_exact",LR_B-LR_A,"=",f"{float(LR_B-LR_A):.15f}")
    print("delta_LD",f"{(L_B-L_A)-float(LR_B-LR_A):.15f}")
    assert B["D"] < A["D"]
    assert L_B > L_A
    assert LR_B > LR_A
    print("PASS")

if __name__=="__main__":
    main()
