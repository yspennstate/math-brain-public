#!/usr/bin/env python3
"""Integer/rational checks for FEI remainder isolation and drift obstructions.
Run with Python >=3.10 and NumPy. This is not a full FEI proof or a proof assistant.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import hashlib, json, random
import numpy as np

ROOT=Path(__file__).resolve().parent
SEED=202609201531

def fwht(a):
    a=np.asarray(a,dtype=np.int64).copy(); one=a.ndim==1
    if one:a=a[None,:]
    N=a.shape[1]; assert N>0 and not (N&(N-1))
    for j in range(N.bit_length()-1):
        v=a.reshape(len(a),-1,2<<j)
        l=v[:,:,:1<<j].copy();r=v[:,:,1<<j:].copy()
        v[:,:,:1<<j]=l+r;v[:,:,1<<j:]=l-r
    return a[0] if one else a

def v2(x):
    x=abs(int(x));assert x
    return (x&-x).bit_length()-1

def val(values,default):
    return min((v2(x) for x in values if x),default=default)

def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(c,a):return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])

@lru_cache(None)
def ln_range(q):
    q=F(q);assert 1<=q<=2
    z=(q-1)/(q+1);zz=z*z;power=z;out=F(0);M=48
    for j in range(M):
        out+=2*power/(2*j+1);power*=zz
    return out,out+2*power/((2*M+1)*(1-zz))

@lru_cache(None)
def log2(q):
    q=F(q);assert q>0
    k=q.numerator.bit_length()-q.denominator.bit_length();t=q/F(2)**k
    if t<1:k-=1;t*=2
    if t>=2:k+=1;t/=2
    a,b=ln_range(t);c,d=ln_range(F(2))
    return F(k)+a/d,F(k)+b/c

@lru_cache(None)
def h(q):
    q=F(q);return scale(q,log2(1/q)) if q else (F(0),F(0))
def h2(q):return add(h(q),h(1-q))

def entropy_hist(den,hist):
    ans=F(0),F(0)
    for m,count in hist.items():
        if m and count:ans=add(ans,scale(F(count),h(F(m*m,den*den))))
    return ans

def str_interval(a):
    # Preserve an outward rational enclosure without serializing huge exact denominators.
    grid=1<<96
    lo=a[0].numerator*grid//a[0].denominator
    hi=-((-a[1].numerator*grid)//a[1].denominator)
    return [str(F(lo,grid)),str(F(hi,grid))]

def primitive(f):
    f=np.asarray(f,dtype=np.int64);N=len(f);n=N.bit_length()-1
    assert np.all(abs(f)==1)
    W=fwht(f);assert int(np.sum(W*W))==N*N
    hist=Counter(map(int,abs(W)));R=F(0);bands=[]
    for m in sorted(set(hist)-{0}):
        mask=np.where(abs(W)==m,np.sign(W),0);V=fwht(mask);r=val(V,n+1)
        b=F(m*(1<<r),N);assert 0<b<=1 and r<=n
        p=F(hist[m]*m*m,N*N);R+=p*r
        bands.append(dict(amplitude=str(F(m,N)),multiplicity=hist[m],valuation=r,mesh=str(b)))
    H=entropy_hist(N,hist);D=add(scale(F(1,2),H),(-R,-R))
    I=F(sum(int(a)**2*s.bit_count() for s,a in enumerate(W)),N*N)
    return dict(W=W,R=R,H=H,D=D,I=I,bands=bands)

@lru_cache(None)
def selector(n):
    N=1<<n
    counts=list(range(1,N))+[N*N-N*(N-1)//2]
    assert len(set(counts))==N and min(counts)>0 and sum(counts)==N*N
    labels=np.repeat(np.arange(N),counts)
    G=np.array([1-2*((int(s)&x).bit_count()%2) for s in labels for x in range(N)],dtype=np.int64)
    WG=fwht(G);assert list(map(int,WG[:N]))==[N*c for c in counts]
    IG=F(sum(int(a)**2*s.bit_count() for s,a in enumerate(WG)),len(G)**2)
    return G,WG,IG

def isolated(f,t,direct):
    f=np.asarray(f,dtype=np.int64);N=len(f);n=N.bit_length()-1
    assert t>=n+3
    M=1<<t;delta=F(1,M);G,WG,IG=selector(n);B=len(G);dim=3*n+t;den=M*B
    ext=np.tile(f,N*N);WF=fwht(ext);diff=[int(a-b) for a,b in zip(WG,WF)]
    top=[M*int(a)+b for a,b in zip(WF,diff)]
    ha=Counter(map(abs,top));hb=Counter(map(abs,diff));hist=ha.copy()
    for k,c in hb.items():hist[k]+=(M-1)*c
    assert sum(m*m*c for m,c in hist.items())==den*den
    original=primitive(f);dom=[j for j in range(N) if original['W'][j]]
    assert len({abs(top[j]) for j in dom})==len(dom)
    for j in dom:
        m=abs(top[j]);assert m>2*B and hist[m]==1 and hb[m]==0
    outside=F(den*den-sum(top[j]**2 for j in dom),den*den)
    assert 0<=outside<=4*delta
    R=F(0)
    for m,c in hist.items():
        if not m:continue
        A=np.array([0 if abs(z)!=m else (1 if z>0 else -1) for z in top],dtype=np.int64)
        C=np.array([0 if abs(z)!=m else (1 if z>0 else -1) for z in diff],dtype=np.int64)
        WA,WC=fwht(A),fwht(C)
        r=min(val(WA-WC,dim+1),t+val(WC,dim+1))
        assert 0<=r<=dim and F(m*(1<<r),den)<=1
        R+=F(c*m*m,den*den)*r
    assert R<=4*delta*dim
    inum=sum(j.bit_count()*(top[j]**2+(M-1)*diff[j]**2) for j in range(B))
    inum+=t*(M//2)*sum(x*x for x in diff)
    I=F(inum,den*den);corr=F(int(np.dot(ext,G)),B)
    assert I==(1-delta)*original['I']+delta*IG+t*delta*(1-corr)
    assert I<=original['I']+delta*(3*n+2*t)
    tv=F(0)
    for j in dom:tv+=abs(F(top[j]**2,den*den)-F(int(original['W'][j])**2,N*N))
    tv=(tv+outside)/2;assert tv<=4*delta
    H=entropy_hist(den,hist);D=add(scale(F(1,2),H),(-R,-R))
    error=add(h2(4*delta),(4*delta*dim,4*delta*dim))
    assert H[0]-original['H'][1]>=-error[1] and H[1]-original['H'][0]<=error[1]
    if direct:
        full=np.tile(ext,M);full[:B]=G;Wfull=fwht(full)
        expect=np.concatenate([np.array(top,dtype=np.int64),np.tile(np.array(diff,dtype=np.int64),M-1)])
        assert np.array_equal(Wfull,expect)
        obs=primitive(full);assert obs['R']==R and obs['I']==I
    return dict(original_dimension=n,flag_bits=t,total_dimension=dim,direct_walsh=direct,
                influence=str(I),R=str(R),outside_mass=str(outside),entropy_interval=str_interval(H),D_interval=str_interval(D))

def isolation_checks():
    rows=[];rng=random.Random(SEED)
    for n in (1,2):
        N=1<<n
        for code in range(1<<N):
            f=[1-2*((code>>x)&1) for x in range(N)]
            rows.append(isolated(f,n+3,True))
    for n in (3,4):
        for _ in range(4):rows.append(isolated([rng.choice([-1,1]) for _ in range(1<<n)],n+3,n==3))
    bent=[1,1,1,-1];seq=[isolated(bent,t,False) for t in (5,8,16,32,64)]
    rows+=seq
    assert primitive(bent)['D']==(F(0),F(0))
    return dict(cases=len(rows),direct_full_walsh=sum(r['direct_walsh'] for r in rows),
                largest_direct_dimension=max(r['total_dimension'] for r in rows if r['direct_walsh']),
                largest_symbolic_dimension=max(r['total_dimension'] for r in rows),bent_convergence=seq)

def tribes_truth(k,m):
    n=k*m;x=np.arange(1<<n);alive=np.ones(len(x),dtype=bool)
    for j in range(m):alive&=((x>>(k*j))&((1<<k)-1))!=0
    return 2*alive.astype(np.int64)-1

def tribes_checks():
    root=tribes_truth(2,3);base=primitive(root);assert base['R']==0
    x=np.arange(len(root));splits=[]
    for i in range(6):
        a=primitive(root[(x&(1<<i))==0]);b=primitive(root[(x&(1<<i))!=0])
        alpha=base['I']-(a['I']+b['I'])/2;assert alpha>0
        loss=add(base['D'],scale(F(-1,2),add(a['D'],b['D'])))
        ratio=scale(1/alpha,loss);assert ratio[0]>F(5477,1000)
        splits.append(str_interval(ratio))
    params=[];rootbands=childvals=0
    for k in range(4,11):
        N=1<<k;m=N-1;q=F(N-1,N)
        assert all(comb(m,b)%2 for b in range(m+1));rootbands+=m+1
        M=N-2
        for z in range(M+1):assert v2(N*z-M)==1
        childvals+=M+1
        p1=F(4*M,N)*q**(2*N-5);alpha=F(2,N)*q**(N-2)
        lower=p1/(2*alpha);assert lower==(N-2)*q**(N-3) and lower>F(N-2,3)
        params.append(dict(k=k,N=N,dimension=k*(N-1),ratio_lower=str(lower),simple_lower=str(F(N-2,3))))
    return dict(actual_six_variable_splits=len(splits),six_variable_ratio_intervals=splits,
                symbolic_cases=len(params),root_parity_checks=rootbands,child_mask_checks=childvals,rows=params)

def bounded_tree_checks():
    rows=[];cases=0
    # Exact all-ones branch certificates prove the tree-uniform payment;
    # no exponentially large physical truth table is represented here.
    for d in range(1,9):
        k=max(4,(16*(d+1)-1).bit_length());N=1<<k;q=F(N-1,N)
        assert N>=16*(d+1)
        for touched in range(1,d+1):
            M=N-1-touched;b=touched&-touched
            assert b<=d and comb(M,b)%2==0
            p=4*F(comb(M,b),N**b)*q**(2*M-b)
            c=F(1,4*(4**d)*__import__('math').factorial(d))
            assert p/F(2**d)>=c
            Qupper=F(d*(1<<d),N)
            assert c/Qupper==F(N,4*d*__import__('math').factorial(d)*(8**d))
            cases+=1
        rows.append(dict(depth=d,N=N,drop_lower=str(c),query_budget_upper=str(Qupper),ratio_lower=str(c/Qupper)))
    return dict(exact_branch_parameter_checks=cases,depths_checked=8,rows=rows,
                scope='The analytical proof quantifies over every nontrivial adaptive tree of the fixed depth; finite checks verify its scalar certificates.')

# Exact polynomial recurrences for the explicit balanced four-input gate.
def padd(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    while len(c)>1 and not c[-1]:c.pop()
    return c

def pneg(a):return [-x for x in a]
def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[i+j]+=x*y
    while len(c)>1 and not c[-1]:c.pop()
    return c

def shift(a,j,c=1):return [0]*j+[c*x for x in a]
def mask_gate(A,B,C,D):
    left=shift(padd(C,D),1)
    right=padd(pmul(padd(A,B),padd([1],pneg(pmul(C,D)))),pmul(padd(A,pneg(B)),padd(C,pneg(D))))
    return padd(left,shift(right,2))

def gate(a,b,c,d):return (c+d)//2+((1+c)*(1-d)*a+(1-c)*(1+d)*b)//4

def counts(depth):
    C=[1]
    for _ in range(depth):
        C=padd(shift(C,1,2),shift(pmul(C,pmul(padd([1],C),padd([1],C))),2,2))
    return C

def evaluate(bits,depth):
    if depth==0:return [1-2*bits[0]]
    L=4**(depth-1)
    return mask_gate(*(evaluate(bits[j*L:(j+1)*L],depth-1) for j in range(4)))

def generate_certificates():
    rng=random.Random(2026092016);search=[];final_inputs=[]
    def sample(depth):
        if depth==0:
            sign=rng.choice([-1,1]);return [sign],[int(sign<0)]
        if depth==1:
            degree=rng.choice([1,2]);sign=rng.choice([-1,1])
            bits=[0,0,int(sign<0),int(sign<0)] if degree==1 else [int(sign<0),0,0,1]
            P=[0]*degree+[sign*(1<<degree)]
            assert evaluate(bits,1)==P
            return P,bits
        results=[sample(depth-1) for _ in range(4)]
        return mask_gate(*(v[0] for v in results)),sum((v[1] for v in results),[])
    for d in range(1,6):
        C=counts(d);r=[None]*len(C);witness={}
        for _ in range(1000):
            P,bits=sample(d)
            assert sum(F(v,1<<i) for i,v in enumerate(P)) in (-1,1)
            for j,c in enumerate(C):
                if not c:continue
                value=P[j] if j<len(P) else 0
                if value and (r[j] is None or v2(value)<r[j]):
                    r[j]=v2(value);witness[j]=hex(sum(int(b)<<i for i,b in enumerate(bits)))
        Rupper=sum(F(c,4**j)*(r[j] if r[j] is not None else 4**d) for j,c in enumerate(C) if c)
        H=6*(F(3,2)**d-1);I=F(3,2)**d;lower=H/2-Rupper
        search.append(dict(depth=d,entropy=str(H),influence=str(I),R_upper=str(Rupper),D_lower=str(lower),D_I_lower=str(lower/I),selected_inputs=len(set(witness.values()))))
        if d==5:final_inputs=sorted(set(witness.values()))
    out=dict(seed=2026092016,depth=5,dimension=1024,samples_per_depth=1000,
             physical_inputs_hex=final_inputs,search=search,
             scope='Inputs are actual Boolean assignments; observing a valuation bounds the true minimum from above, never from below.')
    (ROOT/'recursive_gate_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
    return out

def recursive_checks():
    f=np.array([gate(*(1-2*((x>>j)&1) for j in range(4))) for x in range(16)],dtype=np.int64)
    base=primitive(f);assert base['H']==(F(3),F(3)) and base['I']==F(3,2) and base['R']==F(3,2)
    x=np.arange(1<<16);inner=[f[(x>>(4*j))&15] for j in range(4)]
    d2=gate(*inner);actual=primitive(d2)
    assert actual['H']==(F(15,2),F(15,2)) and actual['I']==F(9,4) and actual['R']==2
    for d in range(1,8):
        C=counts(d)
        assert sum(F(c,4**j) for j,c in enumerate(C))==1
        assert sum(F(2*j*c,4**j) for j,c in enumerate(C))==6*(F(3,2)**d-1)
    path=ROOT/'recursive_gate_certificates.json'
    cert=json.loads(path.read_text()) if path.exists() else generate_certificates()
    assert cert['depth']==5 and cert['dimension']==1024
    C=counts(5);r=[1024]*len(C)
    for encoded in cert['physical_inputs_hex']:
        integer=int(encoded,16);assert integer.bit_length()<=1024
        P=evaluate([(integer>>j)&1 for j in range(1024)],5)
        assert sum(F(v,1<<j) for j,v in enumerate(P)) in (-1,1)
        for j,c in enumerate(C):
            if c and j<len(P) and P[j]:r[j]=min(r[j],v2(P[j]))
    Rupper=sum(F(c*r[j],4**j) for j,c in enumerate(C));H=F(633,16);I=F(243,32)
    lower=H/2-Rupper;assert lower>F(218,100)*I
    return dict(actual_truth_table_dimensions=[4,16],coefficient_count_depths=list(range(1,8)),
        certificate_dimension=1024,physical_inputs_checked=len(cert['physical_inputs_hex']),
        entropy=str(H),influence=str(I),R_upper=str(Rupper),D_lower=str(lower),D_I_lower=str(lower/I),
        finite_claim='D/I > 2.18',full_truth_table_at_dimension_1024_generated=False)

ANF=[0,1,2,6,7,8,9,10,13,17,18,19,20,21,22,25,26,33,34,37,38,40,41,56,64,66,67,68,72,73,76,80,84,88,96,130,133,134,145,146,152,168,192,196,208,224,257,261,262,264,268,272,274,280,288,290,292,320,322,385,386,388,400,416,448]
def two_band_check():
    x=np.arange(512);p=np.zeros(512,dtype=np.int64)
    for a in ANF:p^=((x&a)==a).astype(np.int64)
    f=1-2*p;data=primitive(f)
    assert data['H']==(F(121,16),F(121,16)) and data['I']==F(71,16)
    assert len(data['bands'])==2 and all(b['mesh']=='1/4' for b in data['bands'])
    assert [(b['amplitude'],b['multiplicity'],b['valuation']) for b in data['bands']]==[('1/16',200,2),('1/8',14,1)]
    out=dict(dimension=9,ANF_monomial_masks=ANF,walsh_integers=data['W'].tolist(),bands=data['bands'],
             entropy=str(data['H'][0]),influence=str(data['I']),
             refuted_claim='Two distinct Fourier magnitudes force half-integer-valued magnitude projections.',
             is_FEI_counterexample=False)
    (ROOT/'two_band_witness.json').write_text(json.dumps(out,indent=2)+'\n')
    return {k:v for k,v in out.items() if k not in ('ANF_monomial_masks','walsh_integers')}

def band_label_checks():
    rows=[]
    for j in range(1,9):
        t=(1<<j)-1
        assert all(comb(t,b)%2 for b in range(t+1))
        mass=[F(comb(t,b)*3**b,4**t) for b in range(t+1)]
        assert sum(mass)==1 and sum(p*b for b,p in enumerate(mass))==F(3*t,4)
        assert sum(mass[b]*(t+b-b) for b in range(t+1))==t
        H=F(7*t,2);R=F(3*t,4);assert H/2-R==t
        rows.append(dict(t=t,bands=t+1,R=str(R),D=t,entropy=str(H),influence=str(F(15*t,8)),band_label_entropy_upper=j))
    return dict(symbolic_parameter_cases=len(rows),rows=rows,
                conclusion='No universal D <= C * entropy(magnitude label). This is not an FEI counterexample.')

def main():
    result=dict(status='PASS',full_FEI_proved=False,independent_review=False,proof_assistant_used=False,
        isolation=isolation_checks(),transitive_drift=tribes_checks(),bounded_depth=bounded_tree_checks(),
        recursive_power_spectra=recursive_checks(),two_band=two_band_check(),band_label=band_label_checks())
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['gate_certificate_sha256']=hashlib.sha256((ROOT/'recursive_gate_certificates.json').read_bytes()).hexdigest()
    (ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('isolation','transitive_drift')},indent=2))
if __name__=='__main__':main()
