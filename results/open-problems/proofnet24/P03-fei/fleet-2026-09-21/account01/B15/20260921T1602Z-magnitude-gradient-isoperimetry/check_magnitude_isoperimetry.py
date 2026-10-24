"""Exact/sanity checker for the B15 magnitude-gradient isoperimetric bridge.

The report's universal inequalities are analytic. This script:
  * exhausts every Boolean function through n=4 and checks L_i <= min(J_i, alpha_i/2 log2(1/alpha_i));
  * constructs the canonical bent-one-flip family and compares direct integer Walsh values with the closed formulas.
"""
from __future__ import annotations
import math
import numpy as np

def fwht(a):
    a=np.asarray(a,dtype=np.int64).copy()
    h=1
    while h<a.size:
        b=a.reshape(-1,2*h)
        x=b[:,:h].copy(); y=b[:,h:].copy()
        b[:,:h]=x+y; b[:,h:]=x-y
        a=b.reshape(-1); h*=2
    return a

def coord_stats(table,i):
    N=len(table); n=N.bit_length()-1
    c=fwht(table).astype(np.float64)/N
    bit=1<<i
    L=alpha=J=0.0
    for S in range(N):
        if S & bit:
            v=abs(c[S]); u=abs(c[S^bit]); p=v*v
            alpha += p
            J += (S.bit_count()-1)*p
            if v>0 and u>v:
                L += p*math.log2(u/v)
    entropy_cap=0.0 if alpha in (0.0,1.0) else 0.5*alpha*math.log2(1.0/alpha)
    return alpha,L,J,entropy_cap

def bent(r,x):
    q=0
    for j in range(r):
        q ^= ((x>>(2*j))&1) & ((x>>(2*j+1))&1)
    return -1 if q else 1

def bent_one_flip(r):
    m=2*r; N=1<<m
    a=np.array([bent(r,x) for x in range(N)],dtype=np.int64)
    b=a.copy(); b[0]*=-1
    return np.concatenate([a,b])

def formulas(r):
    q=2.0**(-r)
    alpha_t=q*q
    R_t=r+0.5*((1+q)*math.log2(1-q)+(1-q)*math.log2(1+q))
    J_t=alpha_t*r
    M=(4**(r-1)-2**(r-1))/2
    A=q-q*q; B=q+q*q
    L_j=0.0 if M==0 else M*A*A*math.log2(B/A)
    alpha_j=0.5+q*q
    return alpha_t,R_t,J_t,L_j,alpha_j

def exhaustive_small():
    worst=0.0
    for n in range(1,5):
        N=1<<n
        for mask in range(1<<N):
            table=np.array([1 if ((mask>>x)&1) else -1 for x in range(N)],dtype=np.int64)
            for i in range(n):
                alpha,L,J,cap=coord_stats(table,i)
                if alpha==0:
                    continue
                assert L <= cap+2e-12, (n,mask,i,"cap",L,cap)
                assert L <= J+2e-12, (n,mask,i,"J",L,J)
                if J>0: worst=max(worst,L/J)
    return worst

def main():
    worst=exhaustive_small()
    print("exhaustive_n_le_4 PASS worst_L_over_J",repr(worst))
    for r in range(1,8):
        table=bent_one_flip(r); m=2*r
        at,Lt,Jt,cap=coord_stats(table,m)
        at0,Rt0,Jt0,Lj0,aj0=formulas(r)
        assert abs(at-at0)<1e-12
        assert abs(Lt/at-Rt0)<2e-11
        assert abs(Jt-Jt0)<1e-12
        aj,Lj,Jj,capj=coord_stats(table,0)
        assert abs(aj-aj0)<1e-12
        assert abs(Lj-Lj0)<2e-11
        assert Lt <= Jt+2e-12 and Lj <= Jj+2e-12
        print("r",r,
              "selector_alpha",repr(at),
              "selector_L_over_Inf",repr(Lt/at),
              "selector_L_over_J",repr(Lt/Jt if Jt else 0.0),
              "inner_alpha",repr(aj),
              "inner_L_over_Inf",repr(Lj/aj))
    print("PASS")

if __name__=="__main__":
    main()
