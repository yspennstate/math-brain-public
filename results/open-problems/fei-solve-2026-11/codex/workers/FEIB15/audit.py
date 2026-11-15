#!/usr/bin/env python3
"""Independent dense Fourier checks and selector/record calculations."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'; os.environ['OMP_NUM_THREADS']='1'
import itertools,json,math,resource,time
import numpy as np

def fwht(f):
    a=np.asarray(f,dtype=np.int64).copy(); m=len(a)
    h=1
    while h<m:
        for k in range(0,m,2*h):
            x=a[k:k+h].copy(); y=a[k+h:k+2*h].copy()
            a[k:k+h]=x+y; a[k+h:k+2*h]=x-y
        h*=2
    return a

def metrics(f):
    a=fwht(f)/len(f); mu=a*a; n=len(f).bit_length()-1
    I=sum(s.bit_count()*p for s,p in enumerate(mu))
    H=sum(-p*math.log2(p) for p in mu if p)
    E=[]; D=[]; J=[]
    for i in range(n):
        ei=di=ji=0
        for s in range(len(f)):
            if s>>i&1: continue
            x=a[s]; y=a[s|(1<<i)]; p=x*x; q=y*y; z=p+q
            if not z: continue
            ei+=sum(v*math.log2(z/v) for v in [p,q] if v)
            eta=lambda t:-t*math.log2(t) if t else 0
            di+=eta(p)+eta(q)-(eta((x+y)**2)+eta((x-y)**2))/2
            u=(x+y)**2; v=(x-y)**2
            ji+=sum(t/2*math.log2(t/z) for t in [u,v] if t)
        E.append(ei); D.append(di); J.append(ji)
    return dict(I=I,H=H,erasure=sum(E),E=E,D=D,J=J,mean=float(a[0]))

def truth(n,t): return [1-2*((t>>x)&1) for x in range(1<<n)]

out={'niceness':os.getpriority(os.PRIO_PROCESS,0),'dense_transform_checks':[], 'selector_checks':[]}
start=time.monotonic()
for n in range(1,5):
    r=np.load(f'census_n{n}.npz'); W=r['weights']; m=1<<n; N=len(W)
    had=np.array([[(-1)**((s&x).bit_count()) for s in range(m)] for x in range(m)],dtype=np.int64)
    err=0
    for j in range(0,N,2048):
        tables=np.arange(j,min(j+2048,N),dtype=np.uint64)
        F=1-2*((tables[:,None]>>np.arange(m,dtype=np.uint64))&1).astype(np.int64)
        A=F@had; err=max(err,int(np.max(np.abs(A*A-W[j:j+len(tables)]))))
    assert err==0
    out['dense_transform_checks'].append(dict(n=n,functions=N,max_integer_weight_error=err))

examples=[]
for n,t in [(2,1),(3,1),(3,23),(3,27),(4,19),(4,980)]:
    f=truth(n,t); r=metrics(f); r.update(n=n,table=t)
    assert max(abs(d-e-j) for d,e,j in zip(r['D'],r['E'],r['J']))<1e-12
    examples.append(r)
    # g = selector ? f(x) : z; original bits low, selectors next, z last.
    for k in [1,2,3]:
        p=2.**-k; g=[]
        for x in range(1<<(n+k+1)):
            live=((x>>n)&((1<<k)-1))==((1<<k)-1)
            g.append(f[x&((1<<n)-1)] if live else 1-2*((x>>(n+k))&1))
        q=metrics(g)
        orig=sum(q['E'][:n]); expected=1-p+p*r['I']+k*p
        assert abs(orig-p*r['erasure'])<1e-12
        assert abs(q['I']-expected)<1e-12
        out['selector_checks'].append(dict(n=n,table=t,k=k,p=p,I=q['I'],I_formula=expected,original_erasure=orig,p_times_original_erasure=p*r['erasure'],variance=1-q['mean']**2))
out['examples']=examples

# Exact AND formula, avoiding truth tables for large n.
def eta(t): return -t*math.log2(t) if t>0 else 0
out['AND_small_I']=[]
for n in [3,4,8,12,20,40]:
    p=(1-2.**(1-n))**2; q=2.**(2-2*n)
    phi=eta(p)+eta(q)-eta(p+q)
    E=n*(phi+(2**(n-1)-1)*2*q); I=n*2.**(1-n)
    out['AND_small_I'].append(dict(n=n,I=I,erasure=E,erasure_over_I=E/I,erasure_over_I_squared=E/I**2))

# Record reconstruction from the explicit PM(K3,3)+nine-coins description.
n=18; x=np.arange(1<<n,dtype=np.uint32); core=x&511; v=np.zeros(len(x),bool)
for perm in itertools.permutations(range(3)):
    mask=sum(1<<(3*r+perm[r]) for r in range(3)); v|=(core&mask)==mask
for e in range(9):
    row,col=divmod(e,3); cross=sum(1<<j for j in range(9) if j//3==row or j%3==col)
    v|=((core==cross)|(core==(cross^(1<<e))))&(((x>>(9+e))&1)>0)
f=1-2*v.astype(np.int64); a=f.copy()
for i in range(n):
    b=a.reshape(-1,2,1<<i); c=b[:,0,:].copy(); d=b[:,1,:].copy(); b[:,0,:]=c+d; b[:,1,:]=c-d
w=a*a; denom=(1<<n)**2; deg=np.array([s.bit_count() for s in range(1<<n)])
It=sum(int(ww)*int(k) for ww,k in zip(w,deg)); I=It/denom
hist={int(ww):int(c) for ww,c in zip(*np.unique(w,return_counts=True))}
H=sum(c*(ww/denom)*math.log2(denom/ww) for ww,c in hist.items() if ww)
assert I==261/128 and a[0]==0
assert sum(int(ww) for ww in w)==denom
direct_counts=[int(np.count_nonzero(f!=f[x^(1<<i)])) for i in range(n)]
direct_I=sum(direct_counts)/(1<<n)
assert direct_I==I and int(v.sum())==(1<<(n-1))
out['record']=dict(n=n,I_numerator=It,I_denominator=denom,I=I,H_bits=H,amplified_ratio=H/(I-1),weight_histogram=hist,balanced=True)
out['record']['direct_pivotal_counts']=direct_counts
out['record']['direct_I']=direct_I
import mpmath as mp
mp.mp.dps=75
Hi=sum(mp.mpf(c)*ww/denom*mp.log(mp.mpf(denom)/ww,2) for ww,c in hist.items() if ww)
out['record']['H_bits_75dps']=str(Hi)
out['record']['ratio_75dps']=str(Hi/(mp.mpf(261)/128-1))
out['bounded_influence_large_degree_moment']=[dict(k=k,m=2**k,I=2+(k-1)/2**k,moment_lower_bound_bits=math.log2(2**k+1)) for k in [2,4,8,16,32]]
out['max_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
out['wall_seconds']=time.monotonic()-start
with open('audit.json','w') as h: json.dump(out,h,indent=2)
print(json.dumps(out,indent=2))
