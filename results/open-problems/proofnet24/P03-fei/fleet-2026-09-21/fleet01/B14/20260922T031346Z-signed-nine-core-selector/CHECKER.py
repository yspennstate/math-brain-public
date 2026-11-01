#!/usr/bin/env python3
"""Exact interval certificate for B14's signed nine-core physical-block selector.

Given the exact source-bound nine-host core, this proves that the physical
outer-core block has entropy/Poincare price < 6.528 for every balanced Boolean
source gadget, every distinguished physical coordinate, arbitrary signed
singleton coefficient b, and arbitrary influence q.  The proof intentionally
certifies the larger independent rectangle (b,q) in [-1,1] x [0,1].
It does not prove FEI.
"""
from fractions import Fraction as F
from collections import Counter

TOP='fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00'
BOT='fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
SLICES=[
(TOP,BOT),(TOP,'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000'),
(TOP,'fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000'),
('fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00','fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'),
(TOP,'fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000'),
(TOP,'fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000'),
('fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00',BOT),
('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00',BOT),
('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00',BOT),
('fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00',BOT)]

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

base=int(''.join(SLICES[0]),16)
masks=[int(''.join(r),16)^base for r in SLICES[1:]]
assert len(masks)==9 and all(m.bit_count()==2 for m in masks)
hosts=[[x for x in range(512) if (m>>x)&1] for m in masks]
a=[-1 if (base>>x)&1 else 1 for x in range(512)]
for h in hosts:
    for x in h:
        a[x]=0
A=fwht(a)
qsum=[0]*512
for lo,hi in hosts:
    q=[0]*512; q[lo]=1; q[hi]=-1
    w=fwht(q)
    qsum=[u+v for u,v in zip(qsum,w)]
pairs=Counter(zip(A,qsum))
assert len(pairs)==19
assert sum(pairs.values())==512

# Exact rational atanh enclosures for logarithms.
NTERMS=28
def p2(k):
    return F(1<<k,1) if k>=0 else F(1,1<<(-k))
def norm2(x):
    k=x.numerator.bit_length()-x.denominator.bit_length()
    while x<p2(k): k-=1
    while x>=p2(k+1): k+=1
    return k,x/p2(k)
def lnunit(y):
    if y==1:
        return F(0),F(0)
    z=(y-1)/(y+1); z2=z*z; t=z; s=F(0)
    for j in range(NTERMS):
        if j:
            t*=z2
        s+=t/F(2*j+1)
    lo=2*s
    rem=2*z**(2*NTERMS+1)/(F(2*NTERMS+1)*(1-z2))
    return lo,lo+rem
LN2L,LN2U=lnunit(F(2))
def log2b(x):
    k,y=norm2(x); lo,hi=lnunit(y)
    return F(k)+lo/LN2U,F(k)+hi/LN2L
def phib(p):
    if p==0:
        return F(0),F(0)
    lo,hi=log2b(1/p)
    return p*lo,p*hi

alpha=F(9,256)
B=F(257,256)
C=F(816,125)  # 6.528

def hcore_upper(l,u):
    out=F(0)
    for (ai,qi),mult in pairs.items():
        if ai==0 and qi==0:
            continue
        pmax=max((F(ai)+l*qi)**2,(F(ai)+u*qi)**2)/F(512*512)
        # Across b in [-1,1] every source mass remains in the increasing
        # part of phi(t)=-t log_2 t.
        assert pmax<F(1,16)
        out+=mult*phib(pmax)[1]
    return out

def min_abs_square(l,u):
    if l<=0<=u:
        return F(0)
    return min(l*l,u*u)

def min_phi_b2(l,u):
    # phi is concave in t, so over the t=b^2 image its minimum is at an
    # endpoint; if the b-cell crosses zero include t=0.
    vals=[phib(l*l)[0],phib(u*u)[0]]
    if l<=0<=u:
        vals.append(F(0))
    return min(vals)

def b_term_upper(l,u):
    # A_C(b)=K(b)-C[B+alpha(1-b^2)].
    return (hcore_upper(l,u)
            -alpha*min_phi_b2(l,u)
            +alpha*(F(16)-C)*(1-min_abs_square(l,u))
            -C*B)

def h2_upper(l,u):
    if l<=F(1,2)<=u:
        return F(1)
    z=u if u<F(1,2) else l
    return phib(z)[1]+phib(1-z)[1]

def tent_upper(l,u):
    if l<=F(1,2)<=u:
        return F(1,2)
    z=u if u<F(1,2) else l
    return min(z,1-z)

def q_term_upper(l,u):
    # F_C(q)=h_2(q)+(2/ln2)min(q,1-q)-Cq.
    # The last term is largest at the left endpoint.
    return h2_upper(l,u)+F(2)*tent_upper(l,u)/LN2L-C*l

MB=1024
MQ=8192
mx_b=None; arg_b=-1
for k in range(MB):
    l=F(-1)+F(2*k,MB)
    u=F(-1)+F(2*(k+1),MB)
    v=b_term_upper(l,u)
    if mx_b is None or v>mx_b:
        mx_b,arg_b=v,k

mx_q=None; arg_q=-1
for k in range(MQ):
    l=F(k,MQ); u=F(k+1,MQ)
    v=q_term_upper(l,u)
    if mx_q is None or v>mx_q:
        mx_q,arg_q=v,k

gap=mx_b+alpha*mx_q
assert gap<0

print("PASS")
print("b_cells",MB,"worst_b_cell",arg_b)
print("b_term_upper_float",float(mx_b))
print("q_cells",MQ,"worst_q_cell",arg_q)
print("q_term_upper_float",float(mx_q))
print("alpha_q_term_upper_float",float(alpha*mx_q))
print("combined_gap_upper_float",float(gap))
print("target_C",float(C))
print("domain","b in [-1,1], q in [0,1] independently")
print("full_FEI","OPEN_NOT_PROVED")
