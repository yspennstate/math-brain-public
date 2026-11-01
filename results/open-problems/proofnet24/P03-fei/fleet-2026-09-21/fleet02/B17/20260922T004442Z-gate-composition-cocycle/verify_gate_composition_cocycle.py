#!/usr/bin/env python3
"""Finite sanity checks for the gate-composition cocycle used in fleet02/B17.

This script is NOT a proof of FEI.  It checks:
  * exact p-biased squared Fourier masses for small Boolean gates;
  * exact Poincare-defect cocycle M(K)=M(F)+sum b_j M(G_j);
  * high-precision Shannon-slack cocycle D(K)=D(F)+sum b_j D(G_j)
    for Gamma=0;
  * the induced convex averaging of c=-D/M when all terms are defined;
  * the balanced uniform composition identities with integer Walsh transforms.

Definitions match the gate reformulation:
  V_p=4p(1-p), It_i=sum_{S contains i} pbiased_hat_G(S)^2,
  b_i=It_i/V_p, Ht_G=entropy of the p-biased spectral law,
  D_G=sum_i b_i (Gamma(p_i)+h2(V_pi))-Gamma(pout)-Ht_G,
  M_G=I_t(G)/4-pout(1-pout).
"""

from fractions import Fraction
import itertools, json
import mpmath as mp
mp.mp.dps = 80

def gate_val(mask,n,bits):
    idx=sum((1<<i) for i,b in enumerate(bits) if b==-1)
    return -1 if (mask>>idx)&1 else 1

def pbiased_spectrum(mask,n,ps):
    probs={}
    for Smask in range(1<<n):
        S=[i for i in range(n) if (Smask>>i)&1]
        T=[i for i in range(n) if not (Smask>>i)&1]
        avg=Fraction(0)
        for tm in range(1<<len(T)):
            fixed={}
            wt=Fraction(1)
            for k,i in enumerate(T):
                neg=(tm>>k)&1
                fixed[i]=-1 if neg else 1
                wt*=ps[i] if neg else (1-ps[i])
            delta=0
            for sm in range(1<<len(S)):
                bits=[None]*n
                for i in T: bits[i]=fixed[i]
                parity=0
                for k,i in enumerate(S):
                    neg=(sm>>k)&1
                    bits[i]=-1 if neg else 1
                    parity ^= neg
                delta += (-1 if parity else 1)*gate_val(mask,n,bits)
            avg += wt*delta
        factor=Fraction(1)
        for i in S:
            factor*=ps[i]*(1-ps[i])
        probs[Smask]=factor*avg*avg
    assert sum(probs.values(),Fraction(0))==1
    return probs

def entropy(probs):
    ans=mp.mpf("0")
    for q in probs:
        if q:
            x=mp.mpf(q.numerator)/q.denominator
            ans -= x*mp.log(x,2)
    return ans

def h2(q):
    if q==0 or q==1: return mp.mpf("0")
    x=mp.mpf(q.numerator)/q.denominator
    return -x*mp.log(x,2)-(1-x)*mp.log(1-x,2)

def stats(mask,n,ps):
    sp=pbiased_spectrum(mask,n,ps)
    mean=Fraction(0)
    for xm in range(1<<n):
        bits=[]; wt=Fraction(1)
        for i in range(n):
            neg=(xm>>i)&1
            bits.append(-1 if neg else 1)
            wt*=ps[i] if neg else (1-ps[i])
        mean += wt*gate_val(mask,n,bits)
    pout=(1-mean)/2
    infl=[sum(q for S,q in sp.items() if (S>>i)&1) for i in range(n)]
    return sp,pout,infl,entropy(sp.values())

def D_M(mask,n,ps):
    sp,pout,infl,H=stats(mask,n,ps)
    D=-H  # Gamma=0
    for i,p in enumerate(ps):
        V=4*p*(1-p)
        if V:
            b=infl[i]/V
            D += (mp.mpf(b.numerator)/b.denominator)*h2(V)
    M=sum(infl,Fraction(0))/4-pout*(1-pout)
    return D,M,pout,infl,H

def compose(Fmask,Gmasks,ns):
    m=len(Gmasks); N=sum(ns)
    offsets=[]; z=0
    for n in ns:
        offsets.append(z); z+=n
    K=0
    for x in range(1<<N):
        outer=[]
        for gm,n,off in zip(Gmasks,ns,offsets):
            idx=(x>>off)&((1<<n)-1)
            outer.append(-1 if (gm>>idx)&1 else 1)
        if gate_val(Fmask,m,outer)==-1:
            K|=1<<x
    return K,N

leaf_ps=[Fraction(1,4),Fraction(1,3),Fraction(2,5),Fraction(3,7)]
checks=0; convex_checks=0; max_D_error=mp.mpf("0")
for F in range(16):
    for G0 in range(16):
        for G1 in range(16):
            ps0=leaf_ps[:2]; ps1=leaf_ps[2:]
            _,q0,_,_=stats(G0,2,ps0)
            _,q1,_,_=stats(G1,2,ps1)
            # Degenerate inner output has V_q=0; the displayed b=It/V form is
            # singular, so this finite checker skips those cases.
            if q0 in (0,1) or q1 in (0,1):
                continue
            DF,MF,_,IF,_=D_M(F,2,[q0,q1])
            D0,M0,*_=D_M(G0,2,ps0)
            D1,M1,*_=D_M(G1,2,ps1)
            b0=IF[0]/(4*q0*(1-q0))
            b1=IF[1]/(4*q1*(1-q1))
            K,N=compose(F,[G0,G1],[2,2])
            DK,MK,*_=D_M(K,N,leaf_ps)
            assert MK==MF+b0*M0+b1*M1
            rhs=DF+(mp.mpf(b0.numerator)/b0.denominator)*D0+(mp.mpf(b1.numerator)/b1.denominator)*D1
            err=abs(DK-rhs); max_D_error=max(max_D_error,err)
            assert err < mp.mpf("1e-60")
            checks+=1

            # If zero-M pieces carry no nonzero D, c is a literal weighted average.
            pieces=[(DF,MF,Fraction(1)),(D0,M0,b0),(D1,M1,b1)]
            if MK>0 and all(M>=0 for _,M,_ in pieces) and all(M>0 or abs(D)<mp.mpf("1e-60") for D,M,_ in pieces):
                cK=-DK/(mp.mpf(MK.numerator)/MK.denominator)
                num=mp.mpf("0")
                for D,M,b in pieces:
                    if M>0:
                        bm=mp.mpf(b.numerator)/b.denominator
                        mm=mp.mpf(M.numerator)/M.denominator
                        num += bm*mm*(-D/mm)
                assert abs(cK-num/(mp.mpf(MK.numerator)/MK.denominator)) < mp.mpf("1e-60")
                convex_checks+=1

# Exact balanced-uniform composition check on every balanced 2-bit outer/inner gate.
def fwht(a):
    a=list(map(int,a)); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def uniform_HI(mask,n):
    vals=[-1 if (mask>>x)&1 else 1 for x in range(1<<n)]
    W=fwht(vals); den=(1<<n)**2
    weights=[Fraction(w*w,den) for w in W if w]
    H=entropy(weights)
    I=sum(Fraction(W[s]*W[s],den)*s.bit_count() for s in range(1<<n))
    return H,I

balanced=[m for m in range(16) if m.bit_count()==2]
balanced_checks=0
for F in balanced:
    HF,IF=uniform_HI(F,2)
    for G0 in balanced:
        for G1 in balanced:
            H0,I0=uniform_HI(G0,2); H1,I1=uniform_HI(G1,2)
            K,N=compose(F,[G0,G1],[2,2])
            HK,IK=uniform_HI(K,N)
            # Outer coordinate influences are p-biased spectral memberships at p=1/2.
            _,_,a,_=stats(F,2,[Fraction(1,2),Fraction(1,2)])
            assert IK==a[0]*I0+a[1]*I1
            assert abs(HK-(HF+(mp.mpf(a[0].numerator)/a[0].denominator)*H0+
                              (mp.mpf(a[1].numerator)/a[1].denominator)*H1)) < mp.mpf("1e-60")
            balanced_checks+=1

out={
  "status":"PASS",
  "biased_gate_compositions_checked":checks,
  "convex_margin_checks":convex_checks,
  "balanced_uniform_compositions_checked":balanced_checks,
  "max_abs_D_cocycle_error_80dps":mp.nstr(max_D_error,8),
  "exact_checks":"p-biased spectral mass normalization and M cocycle use Fraction; balanced I identity exact",
  "scope":"2-bit outer gates with two 2-bit inner gates on one fixed rational-bias vector; all balanced 2-bit compositions",
  "full_FEI_status":"OPEN; finite checks only"
}
print(json.dumps(out,indent=2))
