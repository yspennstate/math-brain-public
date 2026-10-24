#!/usr/bin/env python3
"""Independent high-precision sanity check of the differentiated margin."""
from decimal import Decimal as D, getcontext
getcontext().prec=110
Z,O,TWO,FOUR=D(0),D(1),D(2),D(4)

def h(x):
    if x==Z or x==O:return Z
    return -x*x.ln()-(O-x)*(O-x).ln()

def margin(p,q):
    s=FOUR*q*(O-q); c=FOUR*q*q; b=O-s*p
    a=c*p*(O-p)/b
    return b*h(a)+s*p*h(p)-h(s*p)+p*h(s)+p/TWO*((O-p)/p).ln()

def derivative(p,q):
    s=FOUR*q*(O-q); c=FOUR*q*q; b=O-s*p
    a=c*p*(O-p)/b
    R=(O-TWO*p)*b+s*p*(O-p)
    m=b-c*p*(O-p)
    T=Z if c==Z else c*R/b*(m.ln()-c.ln()-p.ln()-(O-p).ln())
    shpa=Z if a==Z or a==O else -s*h(a)
    sp=s*p
    mixed=Z if s==Z else -s*(O-sp).ln()+s*s.ln()+s*p.ln()
    return (shpa+T+s*h(p)+s*p*((O-p).ln()-p.ln())+mixed+h(s)
            +(D('0.5'))*((O-p).ln()-p.ln())-O/(TWO*(O-p)))

def main():
    step=D('1e-25'); worst=Z; cases=0
    for ps in ('0.4901','0.493','0.497','0.499','0.4999'):
        p=D(ps)
        for qs in ('0.000001','0.0001','0.001','0.004','0.009','0.01'):
            q=D(qs)
            fd=(margin(p+step,q)-margin(p-step,q))/(TWO*step)
            err=abs(fd-derivative(p,q)); worst=max(worst,err); cases+=1
    assert worst < D('1e-40')
    print('B17/A084 derivative formula reconstruction: PASS')
    print('cases=',cases,sep='')
    print('maximum_centered_difference_error=',worst,sep='')
    print('finite_difference_used_as_proof=no')

if __name__=='__main__':main()
