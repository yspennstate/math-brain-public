#!/usr/bin/env python3
"""Exact/finite checks for B16 shared-product coherent composition identity.

Self-check only: exhaustive Boolean pairs through n=3 plus one explicit n=4
obstruction. Exact rational arithmetic is used for all mass, influence, and
support identities; logarithms are binary64 only for the reported entropies.
"""
from fractions import Fraction
import json, math

def fwht_int(vals):
    a=list(map(int, vals)); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def spectrum_probs(vals):
    N=len(vals); w=fwht_int(vals)
    return [Fraction(x*x,N*N) for x in w]

def xor_conv(pa,pb):
    N=len(pa); q=[Fraction(0) for _ in range(N)]
    for s in range(N):
        q[s]=sum(pa[t]*pb[s^t] for t in range(N))
    return q

def H(p):
    return -sum(float(x)*math.log2(float(x)) for x in p if x)

def I_spectral(p):
    return sum(Fraction(s.bit_count())*p[s] for s in range(len(p)))

def infs_physical(vals):
    N=len(vals); n=N.bit_length()-1
    return [Fraction(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N)
            for i in range(n)]

def simultaneous(vals_a, vals_b):
    N=len(vals_a); n=N.bit_length()-1
    total=Fraction(0)
    for i in range(n):
        e=1<<i
        total += Fraction(sum((vals_a[x]!=vals_a[x^e]) and
                              (vals_b[x]!=vals_b[x^e]) for x in range(N)),N)
    return total

def analyze(a,b):
    pa,pb=spectrum_probs(a),spectrum_probs(b)
    prod=[x*y for x,y in zip(a,b)]
    p=spectrum_probs(prod); q=xor_conv(pa,pb)
    assert sum(pa)==sum(pb)==sum(p)==sum(q)==1
    Ia,Ib,Ip,Iq=map(I_spectral,(pa,pb,p,q))
    ia,ib=infs_physical(a),infs_physical(b)
    assert Ia==sum(ia) and Ib==sum(ib)
    R=simultaneous(a,b)
    assert Ip==Ia+Ib-2*R
    Omega=sum(x*y for x,y in zip(ia,ib))
    assert Iq==Ia+Ib-2*Omega
    Delta=[p[s]-q[s] for s in range(len(p))]
    assert sum(Delta)==0
    Ha,Hb,Hp,Hq=map(H,(pa,pb,p,q))
    M=Ha+Hb-Hq
    D=sum(float(p[s])*math.log2(float(p[s]/q[s]))
          for s in range(len(p)) if p[s])
    Coh=sum(float(Delta[s])*math.log2(1/float(q[s]))
            for s in range(len(p)) if q[s])
    err=abs(Hp-(Ha+Hb-M-D+Coh))
    tri_err=abs((Ha+Hb-Hp)-(M+D-Coh))
    return {"pa":pa,"pb":pb,"p":p,"q":q,
            "Ha":Ha,"Hb":Hb,"Hp":Hp,"Hq":Hq,
            "M":M,"D":D,"Coh":Coh,
            "Ia":Ia,"Ib":Ib,"Ip":Ip,"Iq":Iq,
            "R":R,"Omega":Omega,
            "entropy_error":err,"triangle_error":tri_err}

def truth_table(n,bits):
    return [1 if (bits>>x)&1 else -1 for x in range(1<<n)]

def one_point(n):
    v=[1]*(1<<n); v[0]=-1; return v

def bent4():
    out=[]
    for x in range(16):
        bit=(((x>>0)&1)*((x>>1)&1)) ^ (((x>>2)&1)*((x>>3)&1))
        out.append(-1 if bit else 1)
    return out

def main():
    maxerr=0.0; count=0
    funcs=[truth_table(3,b) for b in range(256)]
    for a in funcs:
        for b in funcs:
            m=analyze(a,b)
            maxerr=max(maxerr,m["entropy_error"],m["triangle_error"])
            count+=1
    assert count==65536
    assert maxerr < 2e-12

    b=one_point(4)
    f=bent4()
    a=[f[x]*b[x] for x in range(16)]
    m=analyze(a,b)
    qcounts={}
    for x in m["q"]:
        key=f"{x.numerator}/{x.denominator}"
        qcounts[key]=qcounts.get(key,0)+1
    assert qcounts=={"31/256":6,"7/256":10}
    assert all(x==Fraction(1,16) for x in m["p"])
    assert m["Ia"]==Fraction(5,2)
    assert m["Ib"]==Fraction(1,2)
    assert m["Ip"]==Fraction(2)
    assert m["Iq"]==Fraction(19,8)
    assert m["R"]==Fraction(1,2)
    assert m["Omega"]==Fraction(5,16)
    lift=m["Hp"]-m["Hq"]
    assert lift > 0.36

    out={
      "status":"PASS",
      "scope":"self_check_not_FEI_closure",
      "exhaustive_n3_ordered_pairs":count,
      "max_float_entropy_identity_error":maxerr,
      "n4_obstruction":{
        "definition":"b=-1 only at 0000; f=(-1)^(x1*x2+x3*x4); a=f*b, so a*b=f",
        "p_product":"uniform 1/16 on 16 labels",
        "q_incoherent_counts":qcounts,
        "H_a":m["Ha"],"H_b":m["Hb"],"H_product":m["Hp"],"H_q":m["Hq"],
        "coherent_entropy_lift_Hp_minus_Hq":lift,
        "multiplicity_refund_M":m["M"],
        "KL_refund_D_p_q":m["D"],
        "signed_cross_entropy_Coh":m["Coh"],
        "I_a":str(m["Ia"]),"I_b":str(m["Ib"]),
        "I_product":str(m["Ip"]),"I_q":str(m["Iq"]),
        "simultaneous_physical_flip_R":str(m["R"]),
        "spectral_marginal_overlap_Omega":str(m["Omega"]),
        "coherent_influence_shift_Ip_minus_Iq":str(m["Ip"]-m["Iq"])
      }}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
