#!/usr/bin/env python3
"""
Outward-rounded certificate for the remaining two-equal KS kernel regions
for P10/F0119.

Let p(a)=((1+2a)/3,(1-a)/3,(1-a)/3), a in [-1/2,1], and at
lambda_*=1/sqrt(2) let
  F(a)=Psi(p(a)),
  E(a)=F(a)/2-F(a/sqrt(2)),
  J(a,b)=K_*(p(a),p(b))-F(a/sqrt(2))-F(b/sqrt(2)).
Then H(a,b)=E(a)+E(b)-J(a,b).

This certificate covers positive-positive [0,1]^2 and mixed-sign
[-1/2,0]x[0,1]. The negative-negative quadrant is covered by the
separate prior certificate.

Mathematical inputs used here:
(1) E(a)>=0 and E is decreasing on [-1/2,0], increasing on [0,1].
    This follows from the global quartic edge theorem and its third-
    derivative ray proof; see report.
(2) Exact factorization
    J(a,b)=a^2 b^2 * jhat(a,b),
    jhat = JP(a,b) - ghat(ab),
    where JP is the rational Q(sqrt(2)) function below and
    ghat(t)=g(t)/t^2,
    g(t)=[(1+t)log(1+t)+2(1-t/2)log(1-t/2)]/3.
(3) Near axes, exact convergent series are used with explicit tails.
"""
from fractions import Fraction
import mpmath as mp
mp.mp.dps=80
iv=mp.iv
SQ2=iv.sqrt(2)

COEFFS=[(8, 4, 4, 1, 0, 1), (7, 4, 0, 1, -6, 1), (7, 3, -12, 1, 0, 1), (6, 3, 0, 1, 18, 1), (6, 2, -12, 1, 0, 1), (5, 5, 14, 1, 0, 1), (5, 4, 0, 1, -21, 1), (5, 3, 10, 1, 0, 1), (5, 2, 0, 1, 12, 1), (5, 1, 64, 1, 0, 1), (4, 8, 4, 1, 0, 1), (4, 7, 0, 1, -6, 1), (4, 5, 0, 1, -21, 1), (4, 4, 121, 1, 0, 1), (4, 3, 0, 1, -77, 1), (4, 2, 18, 1, 0, 1), (4, 1, 0, 1, -108, 1), (4, 0, 96, 1, 0, 1), (3, 7, -12, 1, 0, 1), (3, 6, 0, 1, 18, 1), (3, 5, 10, 1, 0, 1), (3, 4, 0, 1, -77, 1), (3, 3, 134, 1, 0, 1), (3, 1, 60, 1, 0, 1), (3, 0, 0, 1, -168, 1), (2, 6, -12, 1, 0, 1), (2, 5, 0, 1, 12, 1), (2, 4, 18, 1, 0, 1), (2, 2, -100, 1, 0, 1), (2, 1, 0, 1, 84, 1), (2, 0, 16, 1, 0, 1), (1, 5, 64, 1, 0, 1), (1, 4, 0, 1, -108, 1), (1, 3, 60, 1, 0, 1), (1, 2, 0, 1, 84, 1), (1, 1, -296, 1, 0, 1), (1, 0, 0, 1, 208, 1), (0, 4, 96, 1, 0, 1), (0, 3, 0, 1, -168, 1), (0, 2, 16, 1, 0, 1), (0, 1, 0, 1, 208, 1), (0, 0, -160, 1, 0, 1)]

def I(q):
    if isinstance(q, Fraction):
        return iv.mpf(q.numerator)/q.denominator
    if isinstance(q, int):
        return iv.mpf(q)
    raise TypeError(q)

def eval_num(A,B):
    out=iv.mpf(0)
    for ia,ib,p0,q0,p1,q1 in COEFFS:
        out += (iv.mpf(p0)/q0 + iv.mpf(p1)/q1*SQ2)*(A**ia)*(B**ib)
    return out

def jpolyhat(A,B):
    t=A*B
    den=72*(t-2)**3*(t+1)**3
    return eval_num(A,B)/den

def cn(n):
    return iv.mpf(((-1)**n)*(2**(n-1))+1)/((2**(n-1))*3*n*(n-1))

def ghat(T, N=60):
    l=float(T.a); u=float(T.b)
    crosses=(l <= 0 <= u)
    R=abs(T).b
    r=float(R)
    if crosses or r <= 0.15:
        if r >= 1:
            raise RuntimeError("series box reached radius 1")
        out=iv.mpf(0)
        for n in range(2,N+1):
            out += cn(n)*T**(n-2)
        tail=(R**(N-1))/(2*N*(N+1)*(1-R))
        return out + iv.mpf([-1,1])*tail
    one=iv.mpf(1)
    g=(one+T)*iv.log(one+T)/3 + 2*(one-T/2)*iv.log(one-T/2)/3
    return g/(T**2)

def jhat(A,B):
    return jpolyhat(A,B)-ghat(A*B)

def xlog3_point(x):
    if x == 0:
        return iv.mpf(0)
    X=I(x)
    return X*iv.log(3*X)

def Ppoint(a):
    A=I(a)
    return A**3/3 - 2*A**4/9

def Fpoint(a):
    p1=(1+2*a)/3
    p2=(1-a)/3
    return xlog3_point(p1)+2*xlog3_point(p2)+Ppoint(a)

def Epoint(a):
    A=I(a)
    p1=(1+2*A/SQ2)/3
    p2=(1-A/SQ2)/3
    Fs=p1*iv.log(3*p1)+2*p2*iv.log(3*p2)+(A/SQ2)**3/3-2*(A/SQ2)**4/9
    return Fpoint(a)/2-Fs

def Elower(a0,a1):
    if a0 >= 0:
        return Epoint(a0).a
    if a1 <= 0:
        return Epoint(a1).a
    return iv.mpf(0).a

def ehat_series(A, r, N=20):
    out=iv.mpf(0)
    for n in range(4,N+1):
        if n==4:
            fn=iv.mpf(5)/18
        else:
            fn=iv.mpf(((-1)**n)*(2**n)+2)/(3*n*(n-1))
        out += fn*(iv.mpf(1)/2-SQ2**(-n))*A**(n-4)
    R=I(r)
    tail=4*(2*R)**(N-3)/(N*(N+1)*(1-2*R))
    return out+iv.mpf([-1,1])*tail

def cauchy_local(a0,a1,b0,b1):
    A=iv.mpf([I(a0).a, I(a1).b])
    B=iv.mpf([I(b0).a, I(b1).b])
    ra=max(abs(a0),abs(a1)); rb=max(abs(b0),abs(b1))
    ea=ehat_series(A,ra)
    eb=ehat_series(B,rb)
    jj=jhat(A,B)
    if jj.b <= 0:
        return True, float('inf')
    if ea.a <= 0 or eb.a <= 0:
        return False, -1.0
    rhs=2*iv.sqrt(ea.a*eb.a)
    margin=rhs.a-jj.b
    return margin >= 0, float(margin.a)

def maxsq(a0,a1):
    return max(a0*a0,a1*a1)

def box_ok(a0,a1,b0,b1):
    local=Fraction(1,20)
    if max(abs(a0),abs(a1),abs(b0),abs(b1)) <= local:
        return cauchy_local(a0,a1,b0,b1)
    A=iv.mpf([I(a0).a,I(a1).b])
    B=iv.mpf([I(b0).a,I(b1).b])
    jh=jhat(A,B)
    ju=max(iv.mpf(0).b,jh.b)
    Jup=I(maxsq(a0,a1))*I(maxsq(b0,b1))*ju
    Elow=Elower(a0,a1)+Elower(b0,b1)
    margin=Elow-Jup
    return margin >= 0, float(margin.a)

def split_box(box):
    a0,a1,b0,b1,d=box
    if (a1-a0) >= (b1-b0):
        m=(a0+a1)/2
        return [(a0,m,b0,b1,d+1),(m,a1,b0,b1,d+1)]
    m=(b0+b1)/2
    return [(a0,a1,b0,m,d+1),(a0,a1,m,b1,d+1)]

def certify(domain, parts=4, maxdepth=18, maxnodes=200000):
    al,au,bl,bu=domain
    stack=[]
    for i in range(parts):
        a0=al+(au-al)*Fraction(i,parts)
        a1=al+(au-al)*Fraction(i+1,parts)
        for j in range(parts):
            b0=bl+(bu-bl)*Fraction(j,parts)
            b1=bl+(bu-bl)*Fraction(j+1,parts)
            stack.append((a0,a1,b0,b1,0))
    nodes=accepted=0; md=0; minmargin=float('inf')
    while stack:
        box=stack.pop(); nodes+=1
        if nodes>maxnodes:
            return False,("NODE_LIMIT",nodes,accepted,md,minmargin,box)
        a0,a1,b0,b1,d=box
        ok,margin=box_ok(a0,a1,b0,b1)
        if ok:
            accepted+=1
            if margin < minmargin: minmargin=margin
            continue
        if d>=maxdepth:
            return False,("DEPTH_FAIL",nodes,accepted,md,minmargin,box,margin)
        md=max(md,d+1)
        stack.extend(split_box(box))
    return True,(nodes,accepted,md,minmargin)

if __name__=="__main__":
    PP=(Fraction(0),Fraction(1),Fraction(0),Fraction(1))
    MP=(Fraction(-1,2),Fraction(0),Fraction(0),Fraction(1))
    ok1,s1=certify(PP)
    print("POSITIVE_POSITIVE_PASS" if ok1 else "POSITIVE_POSITIVE_FAIL")
    print("pp_stats",s1)
    ok2,s2=certify(MP)
    print("MIXED_SIGN_PASS" if ok2 else "MIXED_SIGN_FAIL")
    print("mixed_stats",s2)
    print("OVERALL_PASS" if ok1 and ok2 else "OVERALL_FAIL")
