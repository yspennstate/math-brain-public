#!/usr/bin/env python3
from fractions import Fraction
from math import comb, log2

def conv(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            out[i+j]=out.get(i+j,Fraction(0))+x*y
    return out

def step(w):
    w3=conv(conv(w,w),w)
    out={}
    for k,v in w.items():
        out[k]=out.get(k,Fraction(0))+Fraction(3,4)*v
    for k,v in w3.items():
        out[k]=out.get(k,Fraction(0))+Fraction(1,4)*v
    return out

w={1:Fraction(1)}
H=Fraction(0)
print("PASS-PREAMBLE recursive-majority collision obstruction")
print("d n I H Ccoll Ccoll/(I-1) JensenLower ArchitectureCredit")
for d in range(1,8):
    w=step(w)
    H=Fraction(2)+Fraction(3,2)*H
    n=3**d
    I=sum(Fraction(k)*v for k,v in w.items())
    M2=sum(Fraction(k*k)*v for k,v in w.items())
    assert sum(w.values()) == 1
    assert I == Fraction(3,2)**d
    assert M2 == 2*I*I-I
    assert H == 4*(I-1)

    HK=0.0
    C=0.0
    for k,v in w.items():
        fv=float(v)
        if fv == 0.0:
            continue
        HK -= fv*(log2(v.numerator)-log2(v.denominator))
        C += fv*log2(comb(n,k))

    lower=float(I)*log2(n/(2*float(I)-1))
    assert C + 1e-10 >= lower
    architecture=HK+C-float(H)
    assert architecture >= -1e-10
    print(d, n,
          f"{float(I):.12f}", f"{float(H):.12f}",
          f"{C:.12f}", f"{C/(float(I)-1):.12f}",
          f"{lower:.12f}", f"{architecture:.12f}")

print("symbolic_checks")
print("I_d=(3/2)^d")
print("E[K_d^2]=2 I_d^2-I_d")
print("H(Maj3^d)=4(I_d-1)")
print("Ccoll >= I_d log2(n/(2 I_d-1)) > I_d(d-1)")
print("therefore Ccoll/(I_d-1)>d-1 and no universal collision-only constant exists")
print("PASS")
