#!/usr/bin/env python3
"""Self-check new signed-subcube peeling and balanced influence dilution.

Combinatorial, Walsh, Gram and influence equalities use integers/Fractions.
Entropy comparisons are separately labeled floating diagnostics. The universal
inequalities are proved analytically in REPORT.md; these tests do not prove FEI.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse
import json
import math
from functools import lru_cache
import numpy as np


def walsh(v):
    v=np.asarray(v,dtype=np.int64).copy()
    N=v.shape[-1]
    if N<1 or N & (N-1): raise ValueError('power-of-two dimension required')
    h=1
    while h<N:
        a=v.reshape(*v.shape[:-1],-1,2,h)
        l,r=a[...,0,:].copy(),a[...,1,:].copy()
        a[...,0,:],a[...,1,:]=l+r,l-r
        h*=2
    return v


def entropy(p):
    p=np.asarray(p,dtype=float)
    return float(-sum(x*math.log2(x) for x in p.ravel() if x>0))



@lru_cache(maxsize=None)
def ln_interval(y):
    """Natural log enclosure for rational y in [1,2], 40 exact terms."""
    y=F(y)
    if not F(1)<=y<=F(2):raise ValueError('range reduction needed')
    z=(y-1)/(y+1)
    total=sum((2*z**(2*j+1)/F(2*j+1) for j in range(40)),F(0))
    tail=2*z**81/(81*(1-z*z))
    return total,total+tail


@lru_cache(maxsize=None)
def log2_integer_interval(k):
    if k<1:raise ValueError('positive integer required')
    e=k.bit_length()-1;y=F(k,1<<e)
    lo,hi=ln_interval(y);l2,h2v=ln_interval(F(2))
    return e+lo/h2v,e+hi/l2


def entropy_interval_W(W):
    """Exact rational enclosure, assuming integer Walsh vector of Boolean row."""
    N=len(W);n=N.bit_length()-1
    counts={int(k):int(c) for k,c in zip(*np.unique(np.abs(W),return_counts=True)) if k}
    lo=hi=F(2*n)
    for a,c in counts.items():
        l,u=log2_integer_interval(a*a)
        lo-=F(a*a*c,N*N)*u;hi-=F(a*a*c,N*N)*l
    return lo,hi


def h2(x):
    return entropy([x,1-x])


def spectral(v):
    N=len(v); W=walsh(v); n=N.bit_length()-1
    degrees=np.array([s.bit_count() for s in range(N)],np.int64)
    masses=W*W
    I=np.array([int(sum(masses[s] for s in range(N) if s>>i&1)) for i in range(n)],np.int64)
    direct=np.array([N*int(np.sum(v!=v[np.arange(N)^(1<<i)])) for i in range(n)],np.int64)
    assert np.array_equal(I,direct)
    assert int(sum(masses))==N*N
    return W,I,entropy(masses/(N*N))


def subcube(support,n):
    inds=np.flatnonzero(support).tolist()
    if not inds: return None
    fixed=[]; a=0
    for i in range(n):
        b=(inds[0]>>i)&1
        if all(((t>>i)&1)==b for t in inds):
            fixed.append(i);a|=b<<i
    mask=sum(1<<i for i in fixed)
    if len(inds)!=(1<<(n-len(fixed))):return None
    if not all(((t&mask)==a)==bool(support[t]) for t in range(1<<n)):return None
    return fixed,a


def cube_family(h,r,sign=1,anchor=0):
    h=np.asarray(h,np.int64);N=1<<r
    if h.ndim!=2 or h.shape[0]!=N-1:raise ValueError('wrong branch array')
    M=h.shape[1]
    if M<1 or M&(M-1):raise ValueError('branch length not power of two')
    full=np.ones((M,N,2),np.int64)
    for z in range(N):
        if z==anchor:full[:,z,0],full[:,z,1]=sign,-sign
        else:full[:,z,:]=h[z if z<anchor else z-1,:,None]
    return full.ravel()


def exact_family_checks(h,r):
    h=np.asarray(h,np.int64);N=1<<r;M=h.shape[1]
    q=F(1,N);q0=1-q
    f=cube_family(h,r);W,I,H=spectral(f);den=len(f)**2
    hp=walsh(h); children_H=[entropy(a*a/(M*M)) for a in hp]
    child_I=[]
    for row in h:
        child_I.append(sum(F(int(np.sum(row!=row[np.arange(M)^(1<<k)])),M) for k in range(M.bit_length()-1)))
    B=sum(F(int(I[1+k]),den)-q for k in range(r))
    assert B>=0
    assert F(int(sum(I)),den)==q*(r+1)+B+q0*sum(child_I,F(0))/(N-1)
    boundary=0
    for z in range(1,N):
        for k in range(r):
            zz=z^(1<<k)
            if zz!=0 and z<zz:boundary+=int(np.sum(h[z-1]!=h[zz-1]))
    assert B==F(2*boundary,N*M)
    v=F((N-1)**2*M-int(np.sum(np.sum(h,axis=0)**2)),(N-1)**2*M)
    assert v>=0
    assert v<=2*B/q0
    # x-frequency-one branch is exactly q with uniform control Fourier labels.
    assert F(int(np.sum(W[1::2]**2)),den)==q
    for t in range(N):
        assert W[1+2*t]==len(f)//N
    assert np.all(W[2*N+1::2]==0)
    # x-frequency-zero branch control-frequency-zero mass is q0^2(1-v).
    assert F(int(np.sum(W[::2*N]**2)),den)==q0*q0*(1-v)
    # Gram trace and purity of branch vectors are exact.
    gram=hp@hp.T
    assert np.all(np.diag(gram)==M*M)
    assert np.array_equal(gram,M*(h@h.T))
    # Eigenvalue and entropy comparisons below are diagnostics only.
    rho=gram.astype(float)/((N-1)*M*M)
    ev=np.linalg.eigvalsh(rho)
    ev=np.maximum(ev,0);ev=ev/sum(ev)
    S=entropy(ev)
    mixture=np.mean(hp.astype(float)**2/(M*M),axis=0)
    holevo_excess=entropy(mixture)-sum(children_H)/(N-1)-S
    assert holevo_excess<2e-10
    vf=float(v)
    if r>=2 and vf<=.5:
        assert S<=h2(vf)+vf*math.log2(N-2)+2e-10
        s=float(q+q0*v)
        bound=float(q0)*sum(children_H)/(N-1)+h2(float(q))+float(q)*r
        bound+=float(q0)*(h2(vf)+vf*math.log2(N-2)+h2(s)+s*math.log2(N-1))
        assert H<=bound+2e-10
    eps=B/q
    certified_margin=None
    if eps<=F(1,8):
        peeled=float(q0)*sum(children_H)/(N-1)+float((4+8*eps)*q*(r+1))
        assert H<=peeled+2e-10
        _,upper_H=entropy_interval_W(W)
        lower_children=sum((entropy_interval_W(a)[0] for a in hp),F(0))/(N-1)
        margin=q0*lower_children+(4+8*eps)*q*(r+1)-upper_H
        assert margin>=0
        certified_margin=str(F((margin*(1<<40)).numerator//(margin*(1<<40)).denominator,1<<40))
    if B==0:
        assert all(np.array_equal(row,h[0]) for row in h)
        K=entropy([float(q0*q0)])+2*float(q)*r*(2-float(q))
        assert abs(H-(float(q0)*children_H[0]+K))<2e-10
    return {'r':r,'m':M.bit_length()-1,'B':str(B),'epsilon':str(eps),'v':str(v),
            'H_float':H,'I_exact':str(F(int(sum(I)),den)),
            'max_pivot':bool(all(I[0]>=p for p in I)),
            'low_surplus':bool(eps<=F(1,8)),
            'rational_peeling_margin_lower':certified_margin,
            'Holevo_excess_float':holevo_excess}


def exhaustive():
    counts={'functions':0,'signed_subcube_rows':0,'positive_codimension_rows':0,
            'maximum_rows':0,'zero_surplus_rows':0,'low_surplus_rows':0}
    max_exact_excess=0.0
    for n in range(1,5):
        N=1<<n
        for code in range(1<<N):
            f=np.array([1-2*((code>>x)&1) for x in range(N)],np.int64)
            W,I,H=spectral(f)
            counts['functions']+=1
            for i in range(n):
                rest=[k for k in range(n) if k!=i]
                base=[sum(((y>>j)&1)<<k for j,k in enumerate(rest)) for y in range(1<<(n-1))]
                g=(f[base]-f[np.array(base)|(1<<i)])//2
                if not np.any(g):continue
                sig=int(g[np.flatnonzero(g)[0]])
                if not np.all((g==0)|(g==sig)):continue
                parsed=subcube(g!=0,n-1)
                if parsed is None:continue
                counts['signed_subcube_rows']+=1
                fixed,a=parsed;r=len(fixed)
                if not r:
                    assert np.sum(W!=0)==1
                    continue
                counts['positive_codimension_rows']+=1
                controls=[rest[k] for k in fixed]
                free=[k for k in rest if k not in controls]
                q=F(1,1<<r);q0=1-q
                B=sum(F(int(I[k]),N*N)-q for k in controls)
                assert B>=0
                children=[]
                for z in range(1<<r):
                    mapped=sum(((z>>j)&1)<<k for j,k in enumerate(controls))
                    anchor=sum(((a>>k)&1)<<rest[k] for k in fixed)
                    if mapped==anchor:continue
                    values=[]
                    for w in range(1<<len(free)):
                        x=mapped|sum(((w>>j)&1)<<k for j,k in enumerate(free))
                        assert f[x]==f[x|(1<<i)]
                        values.append(f[x])
                    children.append(np.array(values,np.int64))
                if B==0:
                    counts['zero_surplus_rows']+=1
                    assert all(np.array_equal(h,children[0]) for h in children)
                    Hc=spectral(children[0])[2]
                    K=entropy([float(q0*q0)])+2*float(q)*r*(2-float(q))
                    max_exact_excess=max(max_exact_excess,abs(H-(float(q0)*Hc+K)))
                    assert max_exact_excess<1e-10
                if I[i]==max(I):
                    counts['maximum_rows']+=1
                    assert B==0
                if B/q<=F(1,8):
                    counts['low_surplus_rows']+=1
                    ch=sum(spectral(h)[2] for h in children)/len(children)
                    assert H<=float(q0)*ch+float((4+8*B/q)*q*(r+1))+1e-10
    return {'status':'PASS','exact_counts':counts,
            'entropy_diagnostics_only_max_identity_gap':max_exact_excess}


def seeded():
    rng=np.random.default_rng(20260921192650)
    records=[]
    # Generic independent branches: no low-surplus hypothesis assumed.
    for r in range(1,6):
        for m in range(0,5):
            for _ in range(5):
                h=rng.choice(np.array([-1,1],np.int64),((1<<r)-1,1<<m))
                records.append(exact_family_checks(h,r))
    # Same branch except rare modifications, giving genuinely positive small B/q.
    for r in range(2,7):
        m=8;N=1<<r
        base=rng.choice(np.array([-1,1],np.int64),1<<m)
        for flipped_vertices in (1,2,3):
            h=np.tile(base,(N-1,1))
            for z in range(1,1+flipped_vertices):h[z-1,0]*=-1
            records.append(exact_family_checks(h,r))
        records.append(exact_family_checks(np.tile(base,(N-1,1)),r))
    return {'status':'PASS','seed':20260921192650,'cases':len(records),
            'rational_interval_peeling_certificates':sum(x['low_surplus'] for x in records),
            'minimum_rational_margin_lower':str(min(F(x['rational_peeling_margin_lower']) for x in records if x['low_surplus'])),
            'positive_low_surplus_cases':sum(x['low_surplus'] and F(x['B'])>0 for x in records),
            'max_Holevo_excess_float':max(x['Holevo_excess_float'] for x in records),
            'record_columns':list(records[0]),
            'record_rows':[[row[k] for k in records[0]] for row in records]}


def majority3(x):return 1 if sum(x)>0 else -1


def substitution():
    cases=0;maxgap=0.
    # All three-bit outer functions, each pivot left intact, other bits replaced
    # by disjoint three-bit majorities. The result has seven physical bits.
    for code in range(256):
        f=np.array([1-2*((code>>x)&1) for x in range(8)],np.int64)
        _,Ii,H=spectral(f)
        for i in range(3):
            other=[j for j in range(3) if j!=i]
            vals=[]
            for x in range(128):
                y=((x&1)<<i)
                for b,j in enumerate(other):
                    signs=[1-2*((x>>(1+3*b+k))&1) for k in range(3)]
                    y|=(majority3(signs)<0)<<j
                vals.append(f[y])
            Fv=np.array(vals,np.int64);_,If,HF=spectral(Fv)
            # exact leaf influence and entropy composition (latter diagnostic)
            den=128**2
            assert F(int(If[0]),den)==F(int(Ii[i]),64)
            for b,j in enumerate(other):
                for k in range(3):assert F(int(If[1+3*b+k]),den)==F(int(Ii[j]),128)
            expected=H+2*sum(float(F(int(Ii[j]),64)) for j in other)
            assert abs(HF-expected)<2e-10
            Hchild=[];Houterchild=[]
            for bit in (0,1):
                Hchild.append(spectral(Fv[bit::2])[2])
                outerchild=np.array([f[sum(((y>>b)&1)<<j for b,j in enumerate(other))|(bit<<i)] for y in range(4)],np.int64)
                Houterchild.append(spectral(outerchild)[2])
            gap=abs((HF-sum(Hchild)/2)-(H-sum(Houterchild)/2))
            maxgap=max(maxgap,gap);assert gap<2e-10
            cases+=1
    # Exact compact formulas for the unbounded genuine Boolean family.
    rec=[]
    for m in (2,4,6,10,20):
        N=1<<m;d=m+2;p=F(1,2*N);A=F(3,2)**d
        oldI=F(m+2,2);oldH=F(4+3*m,2)
        newI=p+(oldI-p)*A
        newH=oldH+(oldI-p)*4*(A-1)
        assert newH-4*newI==oldH-4*oldI<0
        assert F(1,1<<d)<p
        rec.append({'m':m,'depth':d,'formal_dimension':1+(m+N)*(3**d),
                    'pivot_influence':str(p),'all_other_leaf_influences_upper':str(F(1,1<<d)),
                    'greedy_ratio_strict_lower_bound':m,
                    'H_minus_4I_exact':str(newH-4*newI),
                    'not_truth_table_enumerated':True})
    return {'status':'PASS','direct_composition_cases':cases,
            'entropy_diagnostic_max_decrement_gap':maxgap,'analytic_family_evaluations':rec}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--part',choices=('all','exhaustive','seeded','substitution'),default='all');ap.add_argument('--output',type=Path)
    args=ap.parse_args();funcs={'exhaustive':exhaustive,'seeded':seeded,'substitution':substitution}
    checks=funcs if args.part=='all' else {args.part:funcs[args.part]}
    out={'full_FEI':'OPEN_NOT_PROVED','check_scope':'self-checks; exact algebra separated from floating entropy diagnostics',
         'checks':{k:fn() for k,fn in checks.items()}}
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(text)
    print(text)
if __name__=='__main__':main()
