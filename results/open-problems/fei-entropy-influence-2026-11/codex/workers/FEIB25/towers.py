"""Exact spectral recurrences (binary64 evaluation) for homogeneous block towers.

No truth tables of size 2^(9^depth) are materialized. Outer Fourier coefficients
are dyadic. At each level all singleton coefficients coincide by transitivity.
"""
import json, math
import numpy as np
from levels import ROOT, wht, pm33, profile, candidates

def compose(outer, W, A, mean, singleton, n):
    m=len(outer).bit_length()-1; c=wht(outer); size=1<<m
    # b_R = partial_R F evaluated with every argument equal to mean.
    b=c.copy()
    for j in range(m):
        for s in range(size):
            if not s>>j&1:b[s]+=mean*b[s|(1<<j)]
    degree=np.array([s.bit_count() for s in range(size)])
    P=W.copy();P[0]=0
    powers=[np.array([1.])]
    for r in range(1,m+1):powers.append(np.convolve(powers[-1],P))
    wn=np.zeros(m*n+1);an=np.zeros_like(wn);ainter=A.copy();ainter[1]=0
    q=singleton**2
    for r in range(m+1):
        indices=np.where(degree==r)[0];B=float(np.dot(b[indices],b[indices]))
        wn[:len(powers[r])]+=B*powers[r]
        if r==0:continue
        interior=np.convolve(ainter,powers[r-1])[:len(an)]
        an[:len(interior)]+=r*B*interior
        boundary=0.
        if q>0:
            for s in indices:
                if b[s]==0:continue
                for j in range(m):
                    if s>>j&1:boundary+=n*q*b[s]**2*math.log2(1+b[s^(1<<j)]**2/(b[s]**2*q))
        poly=powers[r-1]
        an[1:len(poly)+1]+=boundary*poly
    # A singleton of the composed function = inner singleton times b_{one}.
    assert np.max(np.abs(b[[1<<j for j in range(m)]]-b[1]))<1e-12
    return wn,an,float(b[0]),float(singleton*b[1]),m*n

def main():
    host=pm33();initial=profile(host);c=wht(host)
    W=np.array([0.,1.]);A=np.zeros(2);mean=0.;single=1.;n=1
    rows=[]
    for depth in range(1,5):
        W,A,mean,single,n=compose(host,W,A,mean,single,n)
        assert abs(W.sum()-1)<2e-10
        assert abs(W[0]-mean*mean)<1e-10
        assert abs(W[1]-n*single*single)<1e-10
        if depth==1:
            assert np.max(np.abs(W-initial['W']))<1e-13
            assert np.max(np.abs(A-initial['A']))<1e-13
        dd=np.arange(n+1);maxes={}
        for key,den in candidates(W).items():
            ratio=np.divide(A[2:],den[2:],out=np.zeros(n-1),where=den[2:]>1e-100)
            at=int(ratio.argmax()+2);maxes[key]=dict(d=at,ratio=float(ratio[at-2]))
        rows.append(dict(depth=depth,n=n,mean=mean,singleton=single,W=W.tolist(),A=A.tolist(),
                         dW=(dd*W).tolist(),prev_dW=np.r_[0,dd[:-1]*W[:-1]].tolist(),
                         I=float(np.dot(dd,W)),G=float(A.sum()),maxima=maxes))
        (ROOT/'towers.json').write_text(json.dumps(rows,indent=2))
        print(depth,n,'I',rows[-1]['I'],'G',rows[-1]['G'],'mass',W.sum(),flush=True)
    # Validate the recurrence against a full truth table for a small 3-input host
    # with nonzero mean, to exercise all boundary and interior terms at depth two.
    outer=np.array([1.,1.,1.,-1.,1.,-1.,-1.,-1.]);outer[0]=-1.
    h=profile(outer);coeff=wht(outer);W=np.array(h['W']);A=np.array(h['A'])
    w,a,me,si,nn=compose(outer,W,A,coeff[0],coeff[1],3)
    x=np.arange(512);slots=[]
    for j in range(3):slots.append((outer[(x>>(3*j))&7]<0).astype(np.int64))
    f=outer[slots[0]+2*slots[1]+4*slots[2]];direct=profile(f)
    discrepancy=max(np.max(np.abs(w-direct['W'])),np.max(np.abs(a-direct['A'])))
    assert discrepancy<1e-12
    (ROOT/'tower_audit.json').write_text(json.dumps(dict(full_table_n=9,max_absolute_discrepancy=float(discrepancy)),indent=2))
    print('audit',discrepancy)

if __name__=='__main__':main()
