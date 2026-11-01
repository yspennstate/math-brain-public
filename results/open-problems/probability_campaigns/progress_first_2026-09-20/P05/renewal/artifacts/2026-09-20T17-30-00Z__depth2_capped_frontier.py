#!/usr/bin/env python3
"""Exact depth-two Pareto-renewal upper certificates for the one-sided capped
binary LCS constants a_2 and a_3.

No simulation is used.  The right iid source is enumerated exactly through a
four-run cutoff L, and the omitted geometric tail is bounded pathwise by at
most four frontier children.  Rational Collatz witnesses certify the full
infinite-source two-character macro operator.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product

WORDS = ("00","01","10","11")
L = 24
LOG_N = 40

def capped_probs(M):
    return [(k, Fraction(1,2**k)) for k in range(1,M)] + [(M, Fraction(1,2**(M-1)))]

def left_grouped(M,a,startbit=0):
    """Distribution of the joint greedy endpoints of all 2-bit words,
    starting immediately after a capped-source character of age a.
    Quotient by global bit-complement symmetry, so startbit=0 is enough.
    Returns {(endpoint_tuple,end_age_tuple): probability}.
    """
    full = capped_probs(M)
    first = []
    if a == M:
        for l,p in full:
            first.append((1-startbit,l,0,p))
    else:
        d=M-a
        # Current run stops now.
        for l,p in full:
            first.append((1-startbit,l,0,Fraction(1,2)*p))
        # Current run continues for exactly r further characters.
        for r in range(1,d):
            first.append((startbit,r,a,Fraction(1,2**(r+1))))
        first.append((startbit,d,a,Fraction(1,2**d)))

    out=defaultdict(Fraction)
    for B,l1,offset,p1 in first:
      for l2,p2 in full:
       for l3,p3 in full:
        for l4,p4 in full:
          chars=[]; ages=[]
          bit=B
          for j,runlen in enumerate((l1,l2,l3,l4)):
            off=offset if j==0 else 0
            for t in range(1,runlen+1):
                chars.append(str(bit)); ages.append(off+t)
            bit ^= 1
          ep=[]; ea=[]
          for w in WORDS:
            pos=-1
            for c in w:
                pos=next(i for i in range(pos+1,len(chars)) if chars[i]==c)
            ep.append(pos+1); ea.append(ages[pos])
          out[(tuple(ep),tuple(ea))] += p1*p2*p3*p4
    assert sum(out.values()) == 1
    return out

def endpoint_tuple(B,l1,l2,l3,l4):
    chars = str(B)*l1 + str(1-B)*l2 + str(B)*l3 + str(1-B)*l4
    ans=[]
    for w in WORDS:
        pos=-1
        for c in w:
            pos=chars.find(c,pos+1)
            assert pos >= 0
        ans.append(pos+1)
    return tuple(ans)

def right_grouped_int(L):
    """Exact iid-right joint endpoint distribution on the event that its
    first four runs all have length <= L.  Common denominator is 2^(1+4L).
    """
    den = 1 << (1+4*L)
    g=defaultdict(int)
    for B in (0,1):
      for l1 in range(1,L+1):
       for l2 in range(1,L+1):
        for l3 in range(1,L+1):
          base=4*L-l1-l2-l3
          for l4 in range(1,L+1):
            g[endpoint_tuple(B,l1,l2,l3,l4)] += 1 << (base-l4)
    num=sum(g.values())
    expected = (Fraction((1<<L)-1,1<<L))**4
    assert Fraction(num,den) == expected
    return g,num,den

def frontier_indices(tx,ty):
    keep=[]
    for i in range(4):
        dominated=False
        for j in range(4):
            if i==j:
                continue
            if tx[j] <= tx[i] and ty[j] <= ty[i]:
                if tx[j] < tx[i] or ty[j] < ty[i] or j < i:
                    dominated=True
                    break
        if not dominated:
            keep.append(i)
    assert 1 <= len(keep) <= 4
    return keep

RIGHT, RIGHT_NUM, RIGHT_DEN = right_grouped_int(L)
TAIL = 1-Fraction(RIGHT_NUM,RIGHT_DEN)
assert TAIL == 1-(1-Fraction(1,2**L))**4

def exact_truncated_K(M,zx,zy):
    K=[[Fraction(0) for _ in range(M)] for __ in range(M)]
    for a in range(1,M+1):
        LG=left_grouped(M,a)
        for (tx,ea),pl in LG.items():
            for ty,num in RIGHT.items():
                pr=Fraction(num,RIGHT_DEN)
                for i in frontier_indices(tx,ty):
                    K[a-1][ea[i]-1] += pl*pr*(zx**tx[i])*(zy**ty[i])
    return K

def log_interval_ge1(x,N=LOG_N):
    """Rigorous rational interval for log(x), x>=1, using
    log y = 2 atanh((y-1)/(y+1)) after dyadic scaling.
    """
    x=Fraction(x)
    assert x>=1
    k=0
    y=x
    while y>=2:
        y/=2
        k+=1
    def core(y):
        t=(y-1)/(y+1)
        s=Fraction(0)
        tp=t
        for j in range(N):
            s += tp/Fraction(2*j+1)
            tp *= t*t
        lo=2*s
        rem=2*tp/(Fraction(2*N+1)*(1-t*t))
        return lo,lo+rem
    l2,u2=core(Fraction(2))
    ly,uy=core(y)
    return k*l2+ly,k*u2+uy

def certify(case):
    M=case["M"]; zx=case["zx"]; zy=case["zy"]; lam=case["lam"]
    h=case["h"]; q=case["q"]
    K=exact_truncated_K(M,zx,zy)
    hmax=max(h)
    slacks=[]
    for a in range(M):
        lhs=sum(K[a][e]*h[e] for e in range(M)) + 4*TAIL*hmax
        rhs=lam*h[a]
        slack=rhs-lhs
        assert slack>0
        slacks.append(slack)

    mu=Fraction(2)-Fraction(1,2**(M-1))
    lx=log_interval_ge1(1/zx)
    ly=log_interval_ge1(1/zy)
    ld=log_interval_ge1(1/lam)
    A_lo=mu*lx[0]+2*ly[0]
    A_hi=mu*lx[1]+2*ly[1]
    D_lo,D_hi=ld
    assert A_hi < q*D_lo

    print("M =",M)
    print("z_x =",zx)
    print("z_y =",zy)
    print("lambda =",lam)
    print("witness_h =",h)
    print("right_run_cutoff =",L)
    print("omitted_right_probability =",TAIL)
    print("omitted_right_probability_decimal =",format(float(TAIL),".18g"))
    for i,row in enumerate(K,1):
        print("K_trunc_row_%d ="%i, " ; ".join(str(x) for x in row))
    for i,s in enumerate(slacks,1):
        print("collatz_slack_row_%d ="%i,s)
        print("collatz_slack_row_%d_decimal ="%i,format(float(s),".18g"))
    print("certified_a_M_upper <",q)
    print("certified_a_M_upper_decimal <",format(float(q),".12f"))
    print("log_margin_exact =",q*D_lo-A_hi)
    print("log_margin_decimal =",format(float(q*D_lo-A_hi),".18g"))
    if M==2:
        u1=4*(q-Fraction(1,2))
        print("therefore_u_1 <",u1)
        print("therefore_u_1_decimal <",format(float(u1),".12f"))
        print("one_sided_cap_internal_gamma_upper <",q+Fraction(1,4))
    if M==3:
        print("one_sided_cap_internal_gamma_upper <",q+Fraction(1,8))
    print("CASE_PASS")
    print()

CASES=[
    dict(M=2,zx=Fraction(49,500),zy=Fraction(73,125),
         lam=Fraction(887,500000),h=[10043,10000],
         q=Fraction(14397,20000)),
    dict(M=3,zx=Fraction(21,100),zy=Fraction(4,9),
         lam=Fraction(861,200000),h=[10119,10220,10000],
         q=Fraction(7991,10000)),
]
for c in CASES:
    certify(c)
print("EXACT_DEPTH2_CAPPED_RENEWAL_FRONTIER_PASS")
