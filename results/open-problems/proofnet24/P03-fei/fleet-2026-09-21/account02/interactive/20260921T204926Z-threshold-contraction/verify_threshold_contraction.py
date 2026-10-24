#!/usr/bin/env python3
"""Exact Boolean/code checks and separately labelled floating kernel checks.
No finite experiment here proves unrestricted FEI. See REPORT.md for proofs.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
from math import comb, pi, log, sqrt
from pathlib import Path
import argparse, json, math
import numpy as np
import mpmath as mp


def walsh(v: np.ndarray) -> np.ndarray:
    a=np.array(v,dtype=np.int64,copy=True)
    size=a.shape[-1]
    if size<1 or size&(size-1):raise ValueError('power-of-two length required')
    h=1
    while h<size:
        b=a.reshape(*a.shape[:-1],-1,2,h)
        x=b[...,0,:].copy();y=b[...,1,:].copy()
        b[...,0,:]=x+y;b[...,1,:]=x-y;h*=2
    return a


def rm_values(dimension: int, degree: int) -> np.ndarray:
    N=1<<dimension
    masks=[i for i in range(N) if i.bit_count()<=degree]
    if len(masks)>16:raise ValueError('this verifier limits code dimension to 16')
    xs=np.arange(N,dtype=np.int64)
    code=np.zeros((1<<len(masks),N),np.int8)
    ids=np.arange(len(code),dtype=np.int64)
    for j,mask in enumerate(masks):
        code ^= (((ids>>j)&1)[:,None] & ((xs&mask)==mask)[None,:]).astype(np.int8)
    return 1-2*code


def moment_rademacher(N: int, k: int) -> int:
    return sum(comb(N,j)*(N-2*j)**k for j in range(N+1))//(1<<N)


def kraw(N: int, k: int, negatives: int) -> int:
    return sum((-1)**a*comb(negatives,a)*comb(N-negatives,k-a)
               for a in range(max(0,k-(N-negatives)),min(k,negatives)+1))


def exact_christoffel() -> dict:
    comparisons=orthogonal=0
    for N in (8,16,32,64,128,256):
        for m in range(1,min(32,N//2)+1):
            terms=[F(comb(N//2,j)**2,comb(N,2*j)) for j in range(m+1)]
            cs=[F(comb(2*j,j),4**j) for j in range(m+1)]
            assert all(a>=b for a,b in zip(terms,cs))
            assert sum(cs)==(2*m+1)*cs[-1]
            assert 4*m*cs[-1]**2>=1
            comparisons+=1
        for m in range(1,min(4,N//4)+1):
            K=sum(F(comb(N//2,j)**2,comb(N,2*j)) for j in range(m+1))
            ep=ep2=F(0)
            for a in range(N+1):
                p=sum(F((-1)**j*comb(N//2,j)*kraw(N,2*j,a),comb(N,2*j))
                      for j in range(m+1))/K
                if a==N//2:assert p==1
                probability=F(comb(N,a),1<<N)
                ep+=probability*p;ep2+=probability*p*p
            assert ep==1/K and ep2==1/K
            orthogonal+=1
    m=4096
    c=F(comb(2*m,m),4**m)
    assert 4*m*c*c>=1
    assert (2*m+1)*c>64
    return {'status':'PASS','exact_central_term_comparisons':comparisons,
            'exact_reproducing_polynomial_norm_checks':orthogonal,
            'large_m_exact_central_binomial_check':m,
            'large_m_bound':'K > 64, hence zero-atom probability < 1/64',
            'warning':'large-dimensional RM laws are handled by the analytic independence proof, not enumerated'}


def exact_code_examples() -> dict:
    summaries=[];moment_checks=0;syndrome_checks=0
    for D,d in ((3,2),(4,2),(4,3),(5,2)):
        N=1<<D
        # Four points: old adjacent two-point defect, with last coordinate dummy.
        base=(1<<(D-1))-1
        direction=6 if D>=5 else 2
        pts=[(base ^ (direction if a else 0)) | (b<<(D-1)) for a in (0,1) for b in (0,1)]
        assert len(set(pts))==4
        ids=np.arange(16,dtype=np.int64)
        h=np.ones((16,N),np.int64)
        for j,x in enumerate(pts):h[:,x]=1-2*((ids>>j)&1)
        f=h[-1]
        # Exact active q-flip basis: all and only these four singleton duals.
        active=[]
        for v in range(1,N):
            if v.bit_count()<2:continue
            e=v&-v
            if int(f[0]*f[e]*f[v]*f[v^e])<0:active.append(v)
        if D>=4:
            assert set(active)==set(pts)
            syndrome_checks+=1
        # D=3 has an affine target (codimension one); retained as a negative control.
        codes=rm_values(D,d).astype(np.int64);L=len(codes)
        W0=walsh(h)
        W1=h@codes.T
        assert np.all((W1%2)==0)
        assert np.all(np.sum(W0*W0,axis=1)==N*N)
        assert np.all(np.sum(W1*W1,axis=1)==L*N)
        z0=[F(int(np.count_nonzero(w==0)),N) for w in W0]
        z1=[F(int(np.count_nonzero(w==0)),L) for w in W1]
        if D>=4:
            for S in range(16):
                k=S.bit_count()
                expected=(F(1)-F(1,N) if k==0 else F(0) if k%2 else F(1,2) if k==2 else F(3,4))
                assert z0[S]==expected
        beta=[a-b for a,b in zip(z0,z1)]
        beta3=[]
        for R in range(16):
            if R.bit_count()!=3:continue
            b0=sum(beta[S]*(-1)**((S&R).bit_count()) for S in range(16))/16
            a0=sum(z0[S]*(-1)**((S&R).bit_count()) for S in range(16))/16
            if D>=4:assert a0==F(1,64)-F(1,16*N)
            beta3.append(str(b0))
        if (D,d)==(4,3):
            for row in W1:
                counts={int(a):int(np.count_nonzero(row==a)) for a in np.unique(row)}
                for k in range(0,13):
                    actual=sum(count*a**k for a,count in counts.items())
                    expected=moment_rademacher(N,k)*L
                    assert actual==expected
                    moment_checks+=1
        # Build exact rational zero-frequency Walsh coefficients independently via histogram.
        a=np.arange(0,N+1,2,dtype=np.int64)
        h0=np.array([[np.count_nonzero(np.abs(w)==j) for j in a] for w in W0],dtype=np.int64)
        h1=np.array([[np.count_nonzero(np.abs(w)==j) for j in a] for w in W1],dtype=np.int64)
        numer=h0*(L//N)-h1
        assert np.all(numer.sum(axis=1)==0)
        assert np.all((numer*(a*a)).sum(axis=1)==0)
        bhat_num=walsh(numer.T).T
        for R in range(16):
            if R.bit_count()==3:
                b0=F(int(bhat_num[R,0]),16*L)
                assert str(b0)==beta3[[r for r in range(16) if r.bit_count()==3].index(R)]
        # Brownian phase-switch energy for the actual uniform active syndrome law.
        # h_(S xor 15) = f*h_S exactly.
        threshold_energy=F(0)
        for S in range(16):
            signed=numer[S^15]-numer[S]
            cumulative=0;en=0
            for j in range(len(a)-1,0,-1):
                cumulative+=int(signed[j])
                en+=int(a[j]**2-a[j-1]**2)*cumulative*cumulative
            threshold_energy+=F(en,L*L*16)
        # This quantity already equals N^2 E Q_M, since threshold lengths are delta(a^2)/N^2.
        inf=[F(int(np.count_nonzero(f!=f[np.arange(N)^(1<<j)])),N) for j in range(D)]
        I=sum(inf)
        assert I==F(8*(D-1 if direction.bit_count()>1 else D-2),N)
        # Exact entropy <4I for the subcube-defect class is analytic in the report;
        # numerical value here is only a diagnostic.
        p=(W0[-1].astype(float)/N)**2
        H=float(-np.sum(p*np.log2(np.where(p>0,p,1))))
        summaries.append({'D':D,'d':d,'truth_values_per_function':N,
            'enumerated_codewords':L,'phase_states':16,'active_qflip_count':len(active),'difference_direction_weight':direction.bit_count(),
            'triple_zero_frequency_coefficients_exact':beta3,
            'N2_mean_Brownian_exact':str(threshold_energy),
            'I_exact':str(I),'H_float':H,
            'analytic_large_D_counterexample_hypothesis':False})
    return {'status':'PASS','exact_code_coset_moment_checks':moment_checks,
            'exact_four_active_generator_checks':syndrome_checks,
            'examples':summaries,
            'scope':'low-dimensional identity checks, not extrapolation to the analytic D>=27 counterfamily'}


def phi(z: float) -> tuple[float,float,float]:
    # high precision avoids cancellation at large logarithmic scale separation
    v=mp.mpf(z)
    cs=2*mp.cosh(v)*mp.log(2*mp.cosh(v))-2*v*mp.sinh(v)
    q=mp.sech(v)
    # 0 log 0 at q=1
    D=((1+q)*mp.log(1+q)+(1-q)*mp.log(1-q))/2 if q<1 else mp.log(2)
    cp=2*mp.cosh(v)*D
    return float(cs),float(cp),float(cs+cp)


def kernel_checks() -> dict:
    mp.mp.dps=75
    constants=[pi,pi*pi/2-pi,pi*pi/2]
    results=[]
    for width,num in ((2,21),(6,49),(12,81),(20,121)):
        z=np.linspace(-width,width,num)
        M=np.exp(-np.abs(z[:,None]-z[None,:]))
        vals=[phi(float(x)) for x in np.unique(np.round(np.abs(z[:,None]-z[None,:]),12))]
        cache=dict(zip(np.unique(np.round(np.abs(z[:,None]-z[None,:]),12)),vals))
        matrices=[np.array([[cache[round(abs(x-y),12)][k] for y in z] for x in z]) for k in range(3)]
        L=np.linalg.cholesky(M)
        row=[]
        for C,K in zip(constants,matrices):
            whitened=np.linalg.solve(L,np.linalg.solve(L,K).T).T
            whitened=(whitened+whitened.T)/2
            eig=np.linalg.eigvalsh(whitened)
            margin=float(np.linalg.eigvalsh(C*M-K)[0])
            assert eig[0]>-1e-9 and eig[-1]<C+1e-8
            row.append({'max_generalized_eigenvalue_float':float(eig[-1]),'optimal_constant_float':C,'min_Loewner_margin_float':margin})
        results.append({'half_log_width':width,'points':num,'S_P_G':row})
    # Independent scalar identities: mixed derivative and convolution mass integrals.
    pairs=[(mp.mpf(1)/7,mp.mpf(2)/3),(mp.mpf(1)/100,mp.mpf(4)),(mp.mpf(2),mp.mpf(3))]
    worst=mp.mpf(0)
    def S(X,Y):return (X+Y)*mp.log(X+Y)-X*mp.log(X)-Y*mp.log(Y)
    def G(X,Y):
        x=mp.sqrt(X);y=mp.sqrt(Y)
        def FF(a):return a*a*mp.log(abs(a)) if a else mp.mpf(0)
        return FF(x-y)+FF(x+y)-2*FF(x)-2*FF(y)
    for X,Y in pairs:
        sxy=mp.diff(lambda xx:mp.diff(lambda yy:S(xx,yy),Y),X)
        gxy=mp.diff(lambda xx:mp.diff(lambda yy:G(xx,yy),Y),X)
        target=mp.log((mp.sqrt(X)+mp.sqrt(Y))/abs(mp.sqrt(X)-mp.sqrt(Y)))/(2*mp.sqrt(X*Y))
        worst=max(worst,abs(sxy-1/(X+Y)),abs(gxy-target))
    mass_s=mp.quad(lambda t:1/(2*mp.cosh(t/2)),[-mp.inf,0,mp.inf])
    mass_g=mp.quad(lambda t:mp.log(mp.coth(t/4)),[0,1,mp.inf])
    assert abs(mass_s-mp.pi)<mp.mpf('1e-60')
    assert abs(mass_g-mp.pi**2/2)<mp.mpf('1e-60')
    return {'status':'PASS','arithmetic':'floating numerical diagnostics only; theorem proved analytically',
        'log_grid_generalized_eigenvalue_checks':results,
        'mixed_derivative_max_error':str(worst),
        'Carleman_mass_error':str(abs(mass_s-mp.pi)),
        'combined_mass_error':str(abs(mass_g-mp.pi**2/2))}


def finite_window_checks() -> dict:
    mp.mp.dps=65
    X=[mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(3)/4]
    c=[mp.mpf(1),mp.mpf(-2),mp.mpf(1)]
    assert sum(c)==0 and sum(a*b for a,b in zip(c,X))==0
    direct=lambda s:4*sum(a*mp.sin(s*mp.sqrt(x)/2)**2 for a,x in zip(c,X))
    def by_tail(s):
        endpoints=[mp.mpf(0)]+X
        out=mp.mpf(0)
        for a,b in zip(endpoints[:-1],endpoints[1:]):
            tail=sum(cc for cc,xx in zip(c,X) if xx>=b)
            # integrate tail sin(s sqrt(u))/sqrt(u) in u independently
            out+=tail*mp.quad(lambda y:2*mp.sin(s*y),[mp.sqrt(a),mp.sqrt(b)])
        return s*out
    maxerror=max(abs(direct(s)-by_tail(s)) for s in [mp.mpf(1)/7,mp.mpf(1),mp.mpf(9)/2])
    E1=mp.quad(lambda s:direct(s)**2/s**3,[mp.mpf(1)/5,1,4])
    E2=mp.quad(lambda s:by_tail(s)**2/s**3,[mp.mpf(1)/5,1,4])
    assert maxerror<mp.mpf('1e-55') and abs(E1-E2)<mp.mpf('1e-55')
    return {'status':'PASS','arithmetic':'high precision diagnostic, not an interval certificate',
            'phase_transform_max_error':str(maxerror),'energy_difference':str(abs(E1-E2)),
            'finite_window_energy':str(E1)}


def current_formula_checks() -> dict:
    mp.mp.dps=60
    records=[];maxerror=mp.mpf(0)
    for D in range(5,13):
        N=1<<D;base=(1<<(D-1))-1;pts=[base,base|(1<<(D-1)),base^6,(base^6)|(1<<(D-1))]
        h=np.ones((16,N),np.int64)
        for j,x in enumerate(pts):h[:,x]=1-2*((np.arange(16)>>j)&1)
        W=walsh(h)
        signs=np.array([(-1)**((S&7).bit_count()) for S in range(16)],np.int64)
        counts=np.array([np.count_nonzero(w==0) for w in W])
        zero=F(int(np.dot(signs,counts)),16*N)
        assert zero==F(1,64)-F(1,16*N)
        # For terminal degree >=D-2, f belongs to the code: its odd code term is zero.
        # Compare the true affine-coset spectrum with the analytic trigonometric formula.
        for ss in [mp.mpf(3)/10,mp.mpf(10),mp.mpf(N)/7]:
            a=sum(mp.mpf(int(signs[S]))*sum(mp.cos(ss*mp.mpf(int(w))/N) for w in W[S]) for S in range(16))/(16*N)
            t=ss/N
            b=mp.sin(t)**3*mp.cos(t)*(mp.sin(ss-4*t)/N-(mp.mpf(1)/4-mp.mpf(1)/N)*mp.sin(4*t))
            maxerror=max(maxerror,abs(a-b))
        n=D-1
        event=F(n-2,n)*(F(1,2)-F(2,1<<n))
        assert event>=F(1,8)
        records.append({'D':D,'N':N,'triple_affine_zero_coefficient_exact':str(zero),
                        'random_anchor_order_event_lower_bound_exact':str(event),
                        'J_exact':str(F(8*n,N)),
                        'all_original_coordinates_relevant':True})
    assert maxerror<mp.mpf('1e-50')
    # Constants used for the late-cut live-window lower bound.
    for D in range(10,101):
        N=1<<D;n=D-1
        T=1/math.sqrt(2*n)
        assert T<math.pi/8 and N>=8+8/T and N*T/2>=40
    # Closed late-cut full-line current, using only eight rational cosine weights.
    assert 3**63*5**25 > 2**16*7**49
    limit=(-16*mp.log(2)+63*mp.log(3)+25*mp.log(5)-49*mp.log(7))/144
    large=[]
    for DD in (5,10,20,30,40,60):
        NN=1<<DD
        bb={0:F(1,64),1:F(-1,32),3:F(1,32),4:F(-1,64)}
        bb={k:v*(1-F(4,NN)) for k,v in bb.items()}
        for k,v in ((NN//2-3,F(1,8*NN)),(NN//2-1,F(-1,8*NN)),(NN//2-4,F(-1,16*NN)),(NN//2,F(1,16*NN))):
            bb[k]=bb.get(k,F(0))+v
        assert sum(bb.values())==0
        assert sum(v*k*k for k,v in bb.items())==0
        assert sum(v*k**4 for k,v in bb.items())==0
        integ=mp.mpf(0)
        for i,aa in bb.items():
            for j,cc in bb.items():
                for k in (abs(i-j),i+j):
                    if k:integ+=mp.mpf(aa.numerator*cc.numerator)/(aa.denominator*cc.denominator)*k*k*mp.log(k)
        energy=64*integ/9
        large.append({'D':DD,'full_line_current_float':mp.nstr(energy,20),
                      'ratio_to_J_float':mp.nstr(energy/(mp.mpf(8)*(DD-1)/NN),20),
                      'representation':'succinct exact rational cosine weights with high-precision logarithms, NOT truth-table enumeration'})
    return {'status':'PASS','exact_spectrum_and_event_checks':records,
            'late_cut_limit_exact':'(-16 ln 2+63 ln 3+25 ln 5-49 ln 7)/144',
            'late_cut_limit_float':mp.nstr(limit,30),'late_cut_limit_positive_integer_certificate':True,
            'succinct_late_cut_values':large,
            'analytic_trig_identity_max_error':str(maxerror),
            'live_window_elementary_constant_checks':91,
            'warning':'late-cut formula uses f in RM(d,D); it is not asserted at every smaller d. The D>=27 half-band full-line theorem uses the separate analytic moment lemma.'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--part',choices=['all','exact','kernels','window'],default='all');parser.add_argument('--output',type=Path)
    args=parser.parse_args();out={'full_FEI':'OPEN_NOT_PROVED','schema_version':1,'checks':{}}
    if args.part in ('all','exact'):
        out['checks']['Christoffel']=exact_christoffel();out['checks']['Boolean_codes']=exact_code_examples();out['checks']['current_formula']=current_formula_checks()
    if args.part in ('all','kernels'):out['checks']['kernels']=kernel_checks()
    if args.part in ('all','window'):out['checks']['finite_window']=finite_window_checks()
    text=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(text,encoding='utf-8')
    print(text)
if __name__=='__main__':main()
