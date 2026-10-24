#!/usr/bin/env python3
"""New follow-on checks: arbitrary signs on subcube support and approximate support.
Exact Walsh/influence/row tests and rational entropy certificates are distinguished
from diagnostics. This does not prove unrestricted FEI.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,math
import numpy as np
from check_peeling import walsh,spectral,subcube,entropy_interval_W


def run():
    count=maximum=certified=0
    # All three-bit functions and a seeded, explicitly nonexhaustive four-bit set.
    rng=np.random.default_rng(20260921200609)
    for n,codes in [(3,range(256)),(4,rng.integers(0,65536,size=4096))]:
        N=1<<n
        for code in codes:
            f=np.array([1-2*((int(code)>>x)&1) for x in range(N)],np.int64)
            W,I,H=spectral(f)
            for i in range(n):
                rest=[j for j in range(n) if j!=i]
                loc=[sum(((s>>k)&1)<<j for k,j in enumerate(rest)) for s in range(1<<(n-1))]
                row=(f[loc]-f[np.array(loc)|(1<<i)])//2
                Q=subcube(row!=0,n-1)
                if Q is None:continue
                fixed,a=Q;r=len(fixed)
                if r==0:continue
                controls=[rest[k] for k in fixed];free=[j for j in rest if j not in controls]
                q=F(1,1<<r);q0=1-q
                B=sum(F(int(I[j]),N*N)-q for j in controls)
                assert B>=0
                payload=None;children=[]
                for z in range(1<<r):
                    zz=sum(((z>>k)&1)<<j for k,j in enumerate(controls))
                    anchor=sum(((a>>k)&1)<<rest[k] for k in fixed)
                    vals=[]
                    for w in range(1<<len(free)):
                        y=zz|sum(((w>>k)&1)<<j for k,j in enumerate(free))
                        if zz==anchor:assert f[y]==-f[y|(1<<i)]
                        else:assert f[y]==f[y|(1<<i)]
                        vals.append(f[y])
                    if zz==anchor:payload=np.array(vals,np.int64)
                    else:children.append(np.array(vals,np.int64))
                assert payload is not None
                Ig=F(int(sum(spectral(payload)[1])),len(payload)**2)
                Ic=sum((F(int(sum(spectral(h)[1])),len(h)**2) for h in children),F(0))/len(children)
                assert F(int(sum(I)),N*N)==q*(r+1)+B+q*Ig+q0*Ic
                if I[i]==max(I):
                    maximum+=1;assert B==0
                    assert all(np.array_equal(h,children[0]) for h in children)
                hf=entropy_interval_W(W)[1]
                hg=entropy_interval_W(walsh(payload))[0]
                hh=sum((entropy_interval_W(walsh(h))[0] for h in children),F(0))/len(children)
                assert hf<=q*hg+q0*hh+4*(r+1)*(q+B)
                certified+=1
                count+=1
    records=[]
    for r in range(1,6):
        N=1<<r; target=16*r*(N-1);m=(target-1).bit_length();M=1<<m
        # f=(-1)^x if z=0 OR w=0, and +1 otherwise.
        a=np.arange(2*N*M,dtype=np.int64);z=(a>>1)&(N-1);w=a>>(r+1)
        vals=np.where((z==0)|(w==0),1-2*(a&1),1).astype(np.int64)
        W,I,H=spectral(vals);den=len(vals)**2;q=F(1,N);t=F(1,M);E=(1-q)*t
        pivot=q+(1-q)*t
        IZ=r*q*(1-t)
        assert E<=q/F(16*r)
        assert F(int(I[0]),den)==pivot
        assert all(I[0]>v for v in I[1:])
        assert sum(F(int(I[k]),den) for k in range(1,r+1))==IZ
        # Child at z=0 is a dictator. All other children coincide.
        child=np.where(np.arange(2*M)>>1==0,1-2*(np.arange(2*M)&1),1).astype(np.int64)
        hlo,hhi=entropy_interval_W(W);clo,chi=entropy_interval_W(walsh(child))
        lower_margin=12*IZ-(hhi-(1-q)*clo)
        assert lower_margin>0
        rounded=F((lower_margin*(1<<40)).numerator//(lower_margin*(1<<40)).denominator,1<<40)
        records.append({'r':r,'m':m,'dimension':r+m+1,'truth_table_size':len(vals),
                        'pivot_influence':str(pivot),'support_error':str(E),
                        'allowed_error':str(q/F(16*r)),'I_control':str(IZ),
                        'certified_margin_12I_minus_Delta_lower':str(rounded)})
    # Arbitrary sign cannot be discarded without keeping the payload entropy.
    # r=1, g is a six-bit bent sign, h=+1: H=5, old unsigned/no-payload RHS=4.
    vals=[]
    for x in range(256):
        pivot=x&1;z=(x>>1)&1;w=x>>2
        exponent=sum(((w>>(2*k))&1)*((w>>(2*k+1))&1) for k in range(3))
        vals.append((-1)**(pivot+exponent) if z==0 else 1)
    W,I,H=spectral(np.array(vals,np.int64))
    assert H==5
    assert all(abs(int(v)) in (0,16,128) for v in W)
    return {'status':'PASS','seed':20260921200609,
            'exact_support_rows':count,'maximum_rows':maximum,
            'rational_arbitrary_sign_peeling_certificates':certified,
            'coverage':'all 256 three-bit truth tables plus 4096 seeded four-bit samples, repeats possible; not exhaustive four-bit',
            'approximate_support_examples':records,
            'unsigned_payload_omission_counterexample':{'dimension':8,'H_exact':5,'invalid_rhs':4,
                                                       'correct_payload_entropy_term':'3'},
            'full_FEI':'OPEN_NOT_PROVED'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);a=ap.parse_args()
    text=json.dumps(run(),indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(text)
    print(text)
