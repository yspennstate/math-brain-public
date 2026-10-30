#!/usr/bin/env python3
"""Exact spectrum/influence checks for the fixed-relative row counterfamily.
Floating entropy comparisons are diagnostics; the all-r lower bound is analytic.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, json, math
import numpy as np
from check_peeling import walsh, entropy


def fast_spectral(v):
    v=np.asarray(v,np.int64);N=len(v); n=N.bit_length()-1
    W=walsh(v);ii=np.arange(N,dtype=np.int64);sq=W*W
    assert int(sq.sum())==N*N
    infs=[]
    for k in range(n):
        mass=int(sq[(ii>>k)&1==1].sum())
        assert mass==N*int(np.count_nonzero(v!=v[ii^(1<<k)]))
        infs.append(F(mass,N*N))
    return W,infs,entropy(sq.astype(float)/(N*N))


def outer_values(r,s=4):
    M=r+s;N=1<<(1+r+M);ii=np.arange(N,dtype=np.int64)
    x=ii&1;z=(ii>>1)&((1<<r)-1);w=ii>>(r+1)
    out=np.ones(N,np.int64)
    for k in range(r):
        a=w==(1<<k)
        out[a]=1-2*((z[a]>>k)&1)
    mask=(z==0)|(w==0)
    out[mask]=1-2*x[mask]
    return out


def run():
    records=[]
    for r in range(2,8):
        s=4;M=r+s;Nz=1<<r;Nw=1<<M
        q=F(1,Nz);delta=F(1,Nw);p=q+(1-q)*delta
        f=outer_values(r,s);W,I,H=fast_spectral(f);N=len(f)
        assert I[0]==p
        assert all(I[k+1]==q+delta-3*q*delta for k in range(r))
        assert all(I[1+r+k]==delta*(r-q) for k in range(r))
        assert all(I[1+r+k]==delta*(r+1-q) for k in range(r,M))
        # Every nonzero residual frequency has the displayed singleton formula.
        for k in range(r):
            for w in range(1,Nw):
                actual=F(int(W[(w<<(r+1))|(2<<k)]),N)
                expected=delta*((-1)**((w>>k)&1)+q)
                assert actual==expected
        # True support error and exact control influence.
        idx=np.arange(N//2,dtype=np.int64)
        eta=f[0::2]!=f[1::2]; z=idx&(Nz-1)
        E=F(int(np.count_nonzero(eta!=(z==0))),N//2)
        assert E==(1-q)*delta<=q/16
        IZ=sum(I[1:r+1],F(0))
        assert IZ==r*(q+delta-3*q*delta)<r*p
        childH=[]
        for z in range(Nz):
            loc=((np.arange(2*Nw,dtype=np.int64)>>1)<<(r+1))|(z<<1)|(np.arange(2*Nw)&1)
            childH.append(fast_spectral(f[loc])[2])
        Delta=H-sum(childH)/Nz
        P=(W.astype(float)**2/N**2).reshape(Nw,Nz,2)
        B=H-entropy(P.sum(axis=1))
        lower=float(r*delta*(1-delta)*(1-q)**2)*(math.log2(r)+2*math.log2(float((1-q)/(1+q))))
        assert B+1e-11>=lower
        assert Delta+1e-11>=B
        records.append({'r':r,'s':s,'raw_dimension':1+r+M,'raw_truth_table_size':N,
          'support_error_exact':str(E),'relative_error_exact':str(E/q),
          'pivot_influence_exact':str(p),'each_control_influence_exact':str(I[1]),
          'I_controls_exact':str(IZ),'raw_pivot_is_unique_max':all(p>t for t in I[1:]),
          'spectral_erasure_float':B,'decrement_float':Delta,'analytic_lower_bound_float':lower,
          'diluted_folded_drift_exact':str(IZ+q),
          'entropy_values_are_diagnostics':True})
    # Confirm the all-r numerical-free constants used for r>=4.
    assert F(255*225,256*256*21)>F(1,25)
    assert F(15,17)**2>F(1,2)
    assert 2*(1+F(17,32))*(3+F(11,32))<11
    # Direct block-preserving balanced substitution: r=2,s=1; each three-bit w
    # coordinate replaced by majority of three, leaving x and both z bits.
    r,s=2,1;M=r+s;raw=outer_values(r,s);N=1<<(1+r+3*M)
    ii=np.arange(N,dtype=np.int64);mapped=ii&7
    for j in range(M):
        bits=np.zeros(N,np.int64)
        for k in range(3):bits+=(ii>>(1+r+3*j+k))&1
        mapped|=(bits>=2).astype(np.int64)<<(1+r+j)
    sub=raw[mapped];_,I0,H0=fast_spectral(raw);_,I1,H1=fast_spectral(sub)
    vals=[]
    for f,nw in [(raw,M),(sub,3*M)]:
        h=[]
        for z in range(4):
            loc=((np.arange(1<<(nw+1),dtype=np.int64)>>1)<<3)|(z<<1)|(np.arange(1<<(nw+1))&1)
            h.append(fast_spectral(f[loc])[2])
        vals.append(fast_spectral(f)[2]-sum(h)/4)
    assert abs(vals[0]-vals[1])<1e-10
    assert I0[:3]==I1[:3]
    return {'status':'PASS','full_FEI':'OPEN_NOT_PROVED',
      'scope':'counterexample to fixed-relative near-support selected-block payment, not FEI',
      'raw_family_checks':records,
      'direct_block_substitution':{'raw_dimension':6,'new_dimension':12,
          'decrement_diagnostic_gap':abs(vals[0]-vals[1]),'retained_influences_exact_equal':True},
      'large_r_constant_comparisons':'exact rational PASS; no large-dimension truth table extrapolation'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);a=ap.parse_args()
    text=json.dumps(run(),indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(text)
    print(text)
