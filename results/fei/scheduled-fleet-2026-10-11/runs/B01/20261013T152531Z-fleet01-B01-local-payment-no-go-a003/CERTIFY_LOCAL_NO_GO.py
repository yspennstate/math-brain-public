#!/usr/bin/env python3
"""Exact certificate refuting Delta_i U <= B_i + (4/3) Inf_i.

Every logarithmic term has an integer exponent after multiplication by
3*N^2.  The final sign check is therefore a comparison of two integers.
"""
from collections import defaultdict
from decimal import Decimal, getcontext

N = 32
TRUTH_MASK = 1382935834
COORD = 1
vals = [1 if (TRUTH_MASK >> x) & 1 else -1 for x in range(N)]

def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def factorint(x):
    out={};d=2
    while d*d<=x:
        while x%d==0:out[d]=out.get(d,0)+1;x//=d
        d+=1
    if x>1:out[x]=out.get(x,0)+1
    return out

def add_ratio(exps,num,den,weight):
    for p,e in factorint(num).items():exps[p]+=weight*e
    for p,e in factorint(den).items():exps[p]-=weight*e

def u_terms(v):
    w=fwht(v);n=len(v).bit_length()-1;sq=[z*z for z in w];cap=sq[:]
    for j in range(n):
        for s in range(len(v)):
            if not((s>>j)&1):cap[s]+=cap[s|(1<<j)]
    return [(a,cap[s],a) for s,a in enumerate(sq) if a]

children=[[vals[x] for x in range(N) if ((x>>COORD)&1)==b] for b in (0,1)]
parent_w=fwht(vals);parent_sq=[z*z for z in parent_w]

# Scale by 3*N^2. Parent U weights are 3a; the average child U weights
# are -6a because each child denominator is N^2/4.
exps=defaultdict(int)
for a,num,den in u_terms(vals):add_ratio(exps,num,den,3*a)
for child in children:
    for a,num,den in u_terms(child):add_ratio(exps,num,den,-6*a)

# Subtract B_i. Paired parent Walsh squares have total m.
for s in range(N):
    if (s>>COORD)&1:continue
    a=parent_sq[s];b=parent_sq[s|(1<<COORD)];m=a+b
    if a:add_ratio(exps,m,a,-3*a)
    if b:add_ratio(exps,m,b,-3*b)

# Subtract (4/3) Inf_i.  Inf_i=changes/N, so after scaling by 3*N^2
# this is 4*changes*N whole bits.
changes=sum(vals[x]!=vals[x^(1<<COORD)] for x in range(N))
assert changes==14
exps[2]-=4*changes*N
exps={p:e for p,e in exps.items() if e}

num=1;den=1
for p,e in exps.items():
    if e>0:num*=p**e
    else:den*=p**(-e)
assert num>den

getcontext().prec=80
ln2=Decimal(2).ln()
scaled=sum(Decimal(e)*Decimal(p).ln()/ln2 for p,e in exps.items())
margin=scaled/Decimal(3*N*N)

# Independently evaluate the three displayed quantities from the same exact
# log terms at high precision.
def eval_u(v):
    d=Decimal(len(v)*len(v));z=Decimal(0)
    for a,num0,den0 in u_terms(v):
        z += Decimal(a)/d * (Decimal(num0)/Decimal(den0)).ln()/ln2
    return z
U_parent=eval_u(vals)
U_children=(eval_u(children[0])+eval_u(children[1]))/2
Delta=U_parent-U_children
B=Decimal(0)
for s in range(N):
    if (s>>COORD)&1:continue
    a=parent_sq[s];b=parent_sq[s|(1<<COORD)];m=a+b
    if a:B+=Decimal(a)/(N*N)*(Decimal(m)/Decimal(a)).ln()/ln2
    if b:B+=Decimal(b)/(N*N)*(Decimal(m)/Decimal(b)).ln()/ln2
Inf=Decimal(changes)/N
assert abs((Delta-B-Decimal(4)*Inf/3)-margin) < Decimal('1e-70')

def eval_h(v):
    w=fwht(v);d=Decimal(len(v)*len(v));z=Decimal(0)
    for a in (q*q for q in w):
        if a:
            p=Decimal(a)/d;z-=p*p.ln()/ln2
    return z

H=eval_h(vals);I=Decimal(0);G=Decimal(0)
for j in range(5):
    cs=[[vals[x] for x in range(N) if ((x>>j)&1)==b] for b in (0,1)]
    ch=sum(vals[x]!=vals[x^(1<<j)] for x in range(N))
    I+=Decimal(ch)/N
    G+=U_parent-(eval_u(cs[0])+eval_u(cs[1]))/2

print(f"dimension=5")
print(f"truth_mask={TRUTH_MASK}")
print(f"coordinate={COORD}")
print(f"influence={Inf}")
print(f"Delta_U={Delta}")
print(f"B_i={B}")
print(f"Delta_U_minus_B_i={Delta-B}")
print(f"coefficient_ratio={(Delta-B)/Inf}")
print(f"margin_over_4_over_3={margin}")
print(f"H={H}")
print(f"U={U_parent}")
print(f"I={I}")
print(f"G={G}")
print(f"H_plus_I_minus_G={H+I-G}")
print(f"prime_exponents={dict(sorted(exps.items()))}")
print(f"exact_numerator_bits={num.bit_length()}")
print(f"exact_denominator_bits={den.bit_length()}")
print(f"exact_integer_difference_sign={1 if num-den>0 else 0}")
print("PASS")
