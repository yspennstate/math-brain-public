#!/usr/bin/env python3
"""Independent exact reconstruction of B05 reused-character claim.

Does not import or execute the producer checker. Entropic expressions are
stored as rational prime exponents, so identity and witness signs are exact.
"""
from fractions import Fraction
from math import gcd, log2
import itertools, random

def fwht(v):
    a=[Fraction(x) for x in v];h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                x,y=a[k],a[k+h];a[k],a[k+h]=x+y,x-y
        h*=2
    return [x/len(a) for x in a]

def caps(p):
    a=list(p);n=len(a).bit_length()-1
    for i in range(n):
        b=1<<i
        for s in range(len(a)):
            if not s&b:a[s]+=a[s|b]
    return a

def factor(n):
    out={};d=2
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out

def add_log(expr,weight,ratio):
    for p,e in factor(ratio.numerator).items():expr[p]=expr.get(p,Fraction())+weight*e
    for p,e in factor(ratio.denominator).items():expr[p]=expr.get(p,Fraction())-weight*e

def add(a,b,scale=Fraction(1)):
    o=dict(a)
    for p,e in b.items():o[p]=o.get(p,Fraction())+scale*e
    return {p:e for p,e in o.items() if e}

def scale(a,c):return {p:c*e for p,e in a.items() if c*e}

def Uexpr(v):
    p=[x*x for x in fwht(v)];c=caps(p);e={}
    for x,y in zip(p,c):
        if x:add_log(e,x,y/x)
    return e

def Bexpr(v):
    p=[x*x for x in fwht(v)];n=len(v).bit_length()-1;e={}
    for i in range(n):
        bit=1<<i
        for s in range(len(p)):
            if s&bit:continue
            t=p[s]+p[s|bit]
            if p[s]:add_log(e,p[s],t/p[s])
            if p[s|bit]:add_log(e,p[s|bit],t/p[s|bit])
    return e

def restrict(v,i,bit):
    n=len(v).bit_length()-1;o=[]
    for z in range(1<<(n-1)):
        lo=z&((1<<i)-1);hi=z>>i
        o.append(v[lo|(bit<<i)|(hi<<(i+1))])
    return tuple(o)

def Gexpr(v):
    n=len(v).bit_length()-1;u=Uexpr(v);e=scale(u,Fraction(n))
    for i in range(n):
        e=add(e,Uexpr(restrict(v,i,0)),Fraction(-1,2))
        e=add(e,Uexpr(restrict(v,i,1)),Fraction(-1,2))
    return e

def influence(v):
    p=[x*x for x in fwht(v)]
    return sum(Fraction(s.bit_count())*p[s] for s in range(len(p)))

def infcoord(v,x):
    p=[a*a for a in fwht(v)]
    return sum(p[s] for s in range(len(p)) if s&(1<<x))

def mult(v,x):return tuple(a*(1 if s&(1<<x) else -1) for s,a in enumerate(v))
def activate(v):return tuple(v)+tuple(1 for _ in v)

def W(v,x):return add(Uexpr(mult(v,x)),Uexpr(v),-1)
def drift(v,x):
    e=W(v,x);n=len(v).bit_length()-1
    for j in range(n):
        if j==x:continue
        xx=x-1 if j<x else x
        e=add(e,W(v,x))
        e=add(e,W(restrict(v,j,0),xx),Fraction(-1,2))
        e=add(e,W(restrict(v,j,1),xx),Fraction(-1,2))
    return e

def Lexpr(v,c=Fraction(7,4),eta=Fraction(1,4)):
    e=Gexpr(v);e=add(e,Bexpr(v),-1);e=add(e,Uexpr(v),1+eta)
    e[2]=e.get(2,Fraction())-c*influence(v)
    return {p:x for p,x in e.items() if x}

def lcm(a,b):return a//gcd(a,b)*b
def integer_exponents(e):
    d=1
    for x in e.values():d=lcm(d,x.denominator)
    return d,{p:int(x*d) for p,x in e.items()}
def exact_sign(e):
    d,z=integer_exponents(e);pos=neg=1
    for p,x in z.items():
        if x>0:pos*=p**x
        elif x<0:neg*=p**(-x)
    return (1 if pos>neg else -1 if pos<neg else 0),d,z,pos.bit_length(),neg.bit_length()
def value(e):return sum(float(x)*log2(p) for p,x in e.items())

def main():
    rng=random.Random(202610140644)
    cores=[]
    for n in range(1,4):
        cores.extend(tuple(v) for v in itertools.product((-1,1),repeat=1<<n))
    for n,count in ((4,2000),(5,200)):
        for _ in range(count):cores.append(tuple(1 if rng.getrandbits(1) else -1 for _ in range(1<<n)))
    coord=exact=0
    for q in cores:
        n=len(q).bit_length()-1
        for x in range(n):
            r=mult(q,x)
            assert mult(r,x)==q
            assert Bexpr(r)==Bexpr(q)
            assert influence(r)-influence(q)==1-2*infcoord(q,x)
            assert add(Gexpr(r),Gexpr(q),-1)==drift(q,x)
            F=activate(r)
            assert restrict(F,n,0)==r and set(restrict(F,n,1))=={1}
            coord+=1;exact+=3

    # New adversarial witness against the proposed cone-preserving repair.
    mask=10049
    q=tuple(1 if mask&(1<<i) else -1 for i in range(16));x=3
    out=activate(mult(q,x))
    lq=Lexpr(q);lo=Lexpr(out)
    sq=exact_sign(lq);so=exact_sign(lo)
    assert sq[0]<0 and so[0]>0
    print('status=PASS')
    print(f'boolean_cores_checked={len(cores)}')
    print(f'coordinate_checks={coord}')
    print(f'exact_signed_identity_checks={exact}')
    print('cone_witness_mask=10049')
    print('cone_witness_coordinate=3')
    print(f'L_q={value(lq):.15f}')
    print(f'L_output={value(lo):.15f}')
    print(f'L_q_integer_scale={sq[1]}')
    print(f'L_q_prime_exponents={sq[2]}')
    print(f'L_q_product_bits={sq[3]},{sq[4]}')
    print(f'L_output_integer_scale={so[1]}')
    print(f'L_output_prime_exponents={so[2]}')
    print(f'L_output_product_bits={so[3]},{so[4]}')
    print('seed=202610140644')

if __name__=='__main__':main()
