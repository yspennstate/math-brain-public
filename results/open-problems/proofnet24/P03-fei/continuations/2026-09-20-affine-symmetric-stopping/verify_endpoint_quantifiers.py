#!/usr/bin/env python3
"""Exact certificates for the every-coordinate endpoint obstruction.
No exponential-dimensional truth table is constructed for the large witness.
The large certificate uses the proved analytic bounds in ENDPOINT_QUANTIFIERS.md.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import numpy as np
from verify_affine_symmetry import fwht,entropy_form,linadd,interval,leq


def ln2_interval(terms=48):
    z=F(1,3);power=z;ans=F(0)
    for j in range(terms):
        ans+=2*power/(2*j+1);power*=z*z
    return ans,ans+2*power/((2*terms+1)*(1-z*z))


def bent(m):
    assert m>=2 and m%2==0
    x=np.arange(1<<m);phase=np.zeros(1<<m,dtype=np.int64)
    for j in range(0,m,2):phase^=((x>>j)&1)*((x>>(j+1))&1)
    return 1-2*phase


def decimal_bounds(lo,hi,places=12):
    unit=10**places
    a=(lo.numerator*unit)//lo.denominator
    b=-((-hi.numerator*unit)//hi.denominator)
    def show(z):
        return ('-' if z<0 else '')+str(abs(z)//unit)+'.'+str(abs(z)%unit).zfill(places)
    return [show(a),show(b)]


def run_bases():
    cases=fibres=0;dims=[];records=[]
    for m in range(2,13,2):
        N=1<<m;g=bent(m);h=g.copy();h[0]*=-1
        f=np.empty(2*N,dtype=np.int64);f[::2]=g;f[1::2]=h
        G=fwht(g);H=fwht(h);W=fwht(f)
        assert np.all(G*G==N) and np.array_equal(H,G-2)
        assert np.array_equal(W[::2],G+H)
        assert np.array_equal(W[1::2],G-H)
        assert np.all(W[1::2]==2)
        assert sum(int(v)**2 for v in W)==4*N*N
        delta=F(1,N)
        assert F(np.count_nonzero(f!=f[np.arange(2*N)^1]),2*N)==delta
        # Parent u=(G-1)/N and v=1/N. Verify u^2/v^2 >= N/4.
        assert np.all(4*(G-1)**2>=N)
        ef=entropy_form(W,np.ones(2*N,dtype=int),2*N)
        eg=entropy_form(G,np.ones(N,dtype=int),N)
        eh=entropy_form(H,np.ones(N,dtype=int),N)
        D=linadd(linadd(ef,eg,F(-1,2)),eh,F(-1,2))
        leq({p:-c for p,c in D.items()},-delta*(m-2))
        # A separate exact rational/log expression for B_t.
        B={}
        for u,v in zip(W[::2],W[1::2]):
            a,b=int(u)**2,int(v)**2;den=4*N*N
            # (a+b)log(a+b)-a log(a)-b log(b), all divided by den.
            from verify_affine_symmetry import factors
            for val,sgn in ((a+b,1),(a,-1),(b,-1)):
                if val:
                    for p,pow in factors(val):B[p]=B.get(p,F(0))+F(sgn*val*pow,den)
        B={p:c for p,c in B.items() if c}
        leq(B,interval(D)[0]) # B <= Delta; strict for this family.
        leq({p:-c for p,c in B.items()},-delta*(m-2))
        cases+=1;fibres+=N;dims.append(m+1)
        lo,hi=interval(D)
        records.append({'bent_dimension':m,'parent_dimension':m+1,
                        'query_influence':str(delta),
                        'proved_entropy_decrement_ratio_lower':m-2,
                        'finite_entropy_decrement_ratio_outward_decimal_interval':decimal_bounds(lo/delta,hi/delta)})
    return {'base_cases':cases,'fourier_fibres':fibres,'parent_dimensions':dims,'records':records}


def relevant_products():
    cases=coords=0;maxn=0
    for m in (4,6,8):
        g=bent(m);h=g.copy();h[0]*=-1
        f=np.empty(2*len(g),dtype=np.int64);f[::2]=g;f[1::2]=h
        for k in range(2,9):
            w=np.ones(1<<k,dtype=np.int64);w[0]=-1
            product=np.outer(w,f).ravel();n=m+k+1;N=len(product);x=np.arange(N)
            for i in range(n):
                num=int(np.count_nonzero(product!=product[x^(1<<i)]))
                assert num>0
                if i==0:assert F(num,N)==F(1,1<<m)
                coords+=1
            W=fwht(product);Wf=fwht(f);Ww=fwht(w)
            assert np.array_equal(W,np.outer(Ww,Wf).ravel())
            assert entropy_form(W,np.ones(N,dtype=int),N)==linadd(
                entropy_form(Wf,np.ones(len(f),dtype=int),len(f)),
                entropy_form(Ww,np.ones(len(w),dtype=int),len(w)))
            cases+=1;maxn=max(maxn,n)
    return {'all_relevant_product_cases':cases,'positive_coordinate_influence_checks':coords,
            'max_constructed_dimension':maxn,'spectral_tensor_identity':'exact'}


def giant_analytic_certificate():
    m=16;k=1<<24;n=m+k+1
    lo,hi=ln2_interval()
    # Taylor remainder after division by j_t is <= ln(2)^2,
    # because m^2 2^m/(n-1)<=1.
    assert m*m*(1<<m)<=n-1
    # Padding remainder <=16(n-1)2^(m-k)<2^-100.
    # Prove this by bit lengths, never constructing 2^k.
    assert (16*(n-1)).bit_length()+m-k <= -100
    certified=7*lo-hi*hi-F(1,1<<100)
    assert certified>F(437,100)>4
    return {'bent_dimension':m,'rare_factor_dimension':k,'total_dimension':n,
            'all_variables_relevant':'proved analytically; finite small instances checked separately',
            'query_influence':'1/65536',
            'endpoint_charge_over_query_influence_strict_lower':'4.37',
            'exact_rational_lower':str(certified),
            'large_truth_table_constructed':False,
            'certificate_basis':'proved Taylor and rare-factor remainder bounds, with rational ln(2) interval',
            'refutes':'every-coordinate coefficient four, not an existential coordinate selector'}


def main():
    out={'status':'PASS','date':'2026-09-20','full_FEI_proved':False,
         'existential_endpoint_selector_refuted':False,'independent_audit':False,
         'proof_assistant_used':False,'base_checks':run_bases(),
         'relevant_products':relevant_products(),'large_witness':giant_analytic_certificate()}
    out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    dep=Path(__file__).with_name('verify_affine_symmetry.py')
    out['dependency_sha256']=hashlib.sha256(dep.read_bytes()).hexdigest()
    text=json.dumps(out,indent=2)+'\n';Path(__file__).with_name('endpoint_verification.json').write_text(text);print(text,end='')
if __name__=='__main__':main()
