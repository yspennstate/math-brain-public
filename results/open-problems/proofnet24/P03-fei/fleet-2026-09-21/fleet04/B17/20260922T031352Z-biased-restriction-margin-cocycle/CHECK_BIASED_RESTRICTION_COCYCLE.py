#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from collections import Counter
import math

def h2(x):
    x=float(x)
    if x<=0.0 or x>=1.0: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def entropy(masses):
    return sum((-float(z)*math.log2(float(z))) for z in masses if z)

def bias_fr(ab):
    a,b=ab
    den=a*a+b*b
    return Fraction(a*a,den), Fraction(b*b,den), Fraction(a*b,den)

def coeffs(signs, abspec):
    n=len(abspec)
    ps=[bias_fr(z)[0] for z in abspec]
    qs=[bias_fr(z)[1] for z in abspec]
    out=[]
    for S in range(1<<n):
        c=Fraction(0)
        for x in range(1<<n):
            pr=Fraction(1)
            chi=Fraction(1)
            for i,(a,b) in enumerate(abspec):
                p,q,sr=bias_fr((a,b))
                bit=(x>>i)&1
                pr*= p if bit else q
                if (S>>i)&1:
                    chi*= Fraction(b,a) if bit else -Fraction(a,b)
            c += pr*signs[x]*chi
        out.append(c)
    return out

def restrict(signs,n,i,bit):
    others=[j for j in range(n) if j!=i]
    out=[]
    for y in range(1<<(n-1)):
        xbits=[0]*n
        xbits[i]=bit
        for k,j in enumerate(others):
            xbits[j]=(y>>k)&1
        x=sum(xbits[j]<<j for j in range(n))
        out.append(signs[x])
    return out, others

def remap_mask(mask_small, others):
    ans=0
    for k,j in enumerate(others):
        if (mask_small>>k)&1: ans |= 1<<j
    return ans

def influence_from_coeffs(cs,i):
    return sum(c*c for m,c in enumerate(cs) if (m>>i)&1)

def sensitivity(signs,n,i,abspec):
    s0,others=restrict(signs,n,i,0)
    s1,_=restrict(signs,n,i,1)
    prob=Fraction(0)
    for y in range(1<<(n-1)):
        if s0[y]!=s1[y]:
            pr=Fraction(1)
            for k,j in enumerate(others):
                p,q,_=bias_fr(abspec[j])
                pr*=p if ((y>>k)&1) else q
            prob+=pr
    return prob

def verify_gate(signs,abspec):
    n=len(abspec)
    cf=coeffs(signs,abspec)
    assert sum(c*c for c in cf)==1
    Hf=entropy([c*c for c in cf])
    for i in range(n):
        s0,others=restrict(signs,n,i,0)
        s1,_=restrict(signs,n,i,1)
        restspec=[abspec[j] for j in others]
        a=coeffs(s0,restspec); b=coeffs(s1,restspec)
        p,q,sr=bias_fr(abspec[i])
        P0=[z*z for z in a]; P1=[z*z for z in b]
        T=[q*u+p*v for u,v in zip(P0,P1)]
        d2=[p*q*(v-u)*(v-u) for u,v in zip(a,b)]
        # Exact 2x2 orthogonal pair identities.
        for sm,(u,v,t,dd) in enumerate(zip(a,b,T,d2)):
            fullm=remap_mask(sm,others)
            assert cf[fullm] == q*u+p*v
            assert cf[fullm | (1<<i)] == sr*(v-u)
            assert cf[fullm]*cf[fullm]+cf[fullm | (1<<i)]**2 == t
            assert cf[fullm | (1<<i)]**2 == dd
        It=sum(d2)
        delta=sensitivity(signs,n,i,abspec)
        assert It == 4*p*q*delta
        # Other-coordinate influence mixture identity.
        for kk,j in enumerate(others):
            Ifull=influence_from_coeffs(cf,j)
            I0=influence_from_coeffs(a,kk)
            I1=influence_from_coeffs(b,kk)
            assert Ifull == q*I0+p*I1
        # Entropy identity, numerical check after exact mass identities.
        H0=entropy(P0); H1=entropy(P1); HT=entropy(T)
        JS=HT-float(q)*H0-float(p)*H1
        VS=sum(float(t)*h2(float(dd/t)) for t,dd in zip(T,d2) if t)
        assert abs(Hf-(float(q)*H0+float(p)*H1+JS+VS)) < 2e-12
        credit=h2(float(p))-JS+h2(float(It))-VS
        assert credit > -2e-12
        assert abs(Hf-(float(q)*H0+float(p)*H1+h2(float(p))+h2(float(It))-credit)) < 2e-12

def sign_from_mask(mask,n):
    return [(-1 if (mask>>x)&1 else 1) for x in range(1<<n)]

def b0_signs():
    A={0,1,2,3,4,5,8,10}
    return [(-1 if x in A else 1) for x in range(16)]

def b0_credit(i):
    signs=b0_signs(); n=4; abspec=[(1,1)]*4
    s0,others=restrict(signs,n,i,0); s1,_=restrict(signs,n,i,1)
    a=coeffs(s0,[(1,1)]*3); b=coeffs(s1,[(1,1)]*3)
    P0=[z*z for z in a]; P1=[z*z for z in b]
    p=q=Fraction(1,2)
    T=[(u+v)/2 for u,v in zip(P0,P1)]
    d2=[Fraction(1,4)*(v-u)*(v-u) for u,v in zip(a,b)]
    It=sum(d2)
    JS=entropy(T)-.5*entropy(P0)-.5*entropy(P1)
    VS=sum(float(t)*h2(float(dd/t)) for t,dd in zip(T,d2) if t)
    C=1-JS+h2(float(It))-VS
    return Counter(P0), Counter(P1), Counter(T), Counter(d2), It, JS, VS, C


def output_bias(signs,abspec):
    n=len(abspec); r=Fraction(0)
    for x in range(1<<n):
        if signs[x] == -1:
            pr=Fraction(1)
            for i,ab in enumerate(abspec):
                p,q,_=bias_fr(ab)
                pr*=p if ((x>>i)&1) else q
            r+=pr
    return r

def gamma_test(u):
    u=float(u); z=u*(1-u)
    return 3.0*z+2.0*z*z

def gate_defect(signs,abspec):
    n=len(abspec); cs=coeffs(signs,abspec)
    H=entropy([z*z for z in cs])
    rhs=0.0
    for i,ab in enumerate(abspec):
        p,q,_=bias_fr(ab); V=4*p*q
        It=influence_from_coeffs(cs,i)
        rhs += float(It/V)*(gamma_test(p)+h2(float(V)))
    r=output_bias(signs,abspec)
    return rhs-gamma_test(r)-H

def gate_W(signs,abspec):
    cs=coeffs(signs,abspec)
    I=sum(influence_from_coeffs(cs,i) for i in range(len(abspec)))
    r=output_bias(signs,abspec)
    return I/Fraction(4)-r*(1-r)

def local_credit_data(signs,abspec,i):
    n=len(abspec)
    s0,others=restrict(signs,n,i,0); s1,_=restrict(signs,n,i,1)
    rest=[abspec[j] for j in others]
    a=coeffs(s0,rest); b=coeffs(s1,rest)
    P0=[z*z for z in a]; P1=[z*z for z in b]
    p,q,_=bias_fr(abspec[i])
    T=[q*u+p*v for u,v in zip(P0,P1)]
    d2=[p*q*(v-u)*(v-u) for u,v in zip(a,b)]
    It=sum(d2)
    JS=entropy(T)-float(q)*entropy(P0)-float(p)*entropy(P1)
    VS=sum(float(t)*h2(float(dd/t)) for t,dd in zip(T,d2) if t)
    C=h2(float(p))-JS+h2(float(It))-VS
    r0=output_bias(s0,rest); r1=output_bias(s1,rest); r=q*r0+p*r1
    delta=sensitivity(signs,n,i,abspec)
    V=4*p*q
    L=(float(q)*gamma_test(r0)+float(p)*gamma_test(r1)-gamma_test(r)
       +float(delta)*(gamma_test(p)+h2(float(V)))
       -h2(float(p))-h2(float(It))+C)
    w=p*q*(delta-(r1-r0)*(r1-r0))
    return L,w,s0,s1,rest


def tree_totals(signs,abspec):
    if not abspec:
        # Boundary-normalized Gamma_test has Gamma(0)=Gamma(1)=0, so constant defect and W vanish.
        return 0.0, Fraction(0)
    L,w,s0,s1,rest=local_credit_data(signs,abspec,0)
    p,q,_=bias_fr(abspec[0])
    D0,W0=tree_totals(s0,rest)
    D1,W1=tree_totals(s1,rest)
    return L+float(q)*D0+float(p)*D1, w+q*W0+p*W1

def verify_tree(signs,abspec):
    Dt,Wt=tree_totals(signs,abspec)
    assert abs(Dt-gate_defect(signs,abspec))<1e-11
    assert Wt==gate_W(signs,abspec)

def verify_defect_recursion(signs,abspec):
    n=len(abspec)
    D=gate_defect(signs,abspec); W=gate_W(signs,abspec)
    for i in range(n):
        L,w,s0,s1,rest=local_credit_data(signs,abspec,i)
        p,q,_=bias_fr(abspec[i])
        rhs=float(q)*gate_defect(s0,rest)+float(p)*gate_defect(s1,rest)+L
        assert abs(D-rhs)<5e-12
        wrhs=q*gate_W(s0,rest)+p*gate_W(s1,rest)+w
        assert W==wrhs
        assert w>=0

def main():
    # Exhaust all 3-bit Boolean truth tables at three exact square-odds
    # product-bias vectors.  Global complements are retained deliberately.
    specs=[
        [(1,1),(1,2),(2,3)],
        [(1,2),(2,1),(3,2)],
        [(2,3),(3,1),(1,3)],
    ]
    tested=0
    for mask in range(256):
        signs=sign_from_mask(mask,3)
        for sp in specs:
            verify_gate(signs,sp); verify_defect_recursion(signs,sp); verify_tree(signs,sp); tested+=1

    # Exact B0 uniform data from the quarter-equality factorization handoff.
    signs=b0_signs()
    verify_gate(signs,[(1,1)]*4)
    full=coeffs(signs,[(1,1)]*4)
    assert Counter(c*c for c in full)==Counter({Fraction(1,16):8,Fraction(1,4):2,Fraction(0):6})
    # The two pivot orbits have exact influence 1/4 and 1/2.
    for i in (0,1):
        dat=b0_credit(i); assert dat[4]==Fraction(1,4)
    for i in (2,3):
        dat=b0_credit(i); assert dat[4]==Fraction(1,2)
        assert abs(dat[5]-.5)<1e-12 and abs(dat[6]-.5)<1e-12 and abs(dat[7]-1.0)<1e-12

    # Unary identity: the credit-free local all-gate remainder equals -h2(p)
    # for every interior p, while the branch-uncertainty credit is +h2(p).
    # We exact-check the spectral pair at several square-odds biases.
    for ab in [(1,1),(1,2),(2,3),(3,1)]:
        p,q,sr=bias_fr(ab)
        signs=[1,-1]
        c=coeffs(signs,[ab])
        assert c[0]==q-p
        assert c[1]==-2*sr
        It=c[1]*c[1]
        assert It==4*p*q
        # Restrictions have identical spectral laws delta_empty, hence JS=0.
        # Vertical split is exactly h2(It), so total credit is h2(p).
        H=entropy([z*z for z in c])
        assert abs(H-h2(float(It)))<1e-12

    print("PASS exact biased restriction pair identities")
    print("exhaustive_3bit_gate_bias_cases =", tested)
    print("PASS exact influence-mixture and pivot It=V_p*delta identities")
    print("PASS all-gate defect restriction cocycle for symmetric test Gamma")
    print("PASS exact Poincare-currency restriction cocycle")
    print("PASS complete restriction-tree telescoping of defect and currency")
    print("PASS entropy/KL-credit cocycle numerical layer after exact mass identities")
    for i in range(4):
        P0,P1,T,D,It,JS,VS,C=b0_credit(i)
        print("B0 pivot",i,"It=",It,"JS=%.15f"%JS,"vertical=%.15f"%VS,"credit=%.15f"%C)
    print("B0 pivot orbit {2,3}: exact JS=1/2, vertical=1/2, total_credit=1")
    print("PASS unary identity adversary: credit-free local remainder = -h2(p), exact credit = +h2(p)")

if __name__=="__main__":
    main()
