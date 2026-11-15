"""Independent exact-cube audit of FLOW 11. Run single-threaded, nice 10.
Integer sums, tie-free half-integer thresholds, integer Walsh numerators.
Only logarithms, square roots and evaluations in rho use float64.
No Monte Carlo estimation of any probability is used.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import numpy as np
import itertools, json, math, time, sys, resource
from fractions import Fraction
from pathlib import Path

OUT=Path('.')
RNG=np.random.default_rng(181110)
RHOS=np.unique(np.r_[np.linspace(0,1,33),1-2.**(-np.arange(1,17))])
COUNTS={}; BEST={}; ERRORS={}; START=time.time()
BOUNDS={'lemma_A':2,'lemma_B':16/3,'cross_stay':80,'M_positive':1019.13,'M_all':1019.13,'L_over_delta':1/math.log(2)+4+2*math.log2(1+2*1019.13)}

def dump():
    (OUT/'attack_summary.json').write_text(json.dumps({'counts':COUNTS,'best':BEST,'max_residuals':ERRORS,'bounds':BOUNDS,'rhos':RHOS.tolist(),'elapsed_seconds':time.time()-START,'actual_nice':os.getpriority(os.PRIO_PROCESS,0),'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2)+'\n')

def update(key,value,witness):
    if value>BEST.get(key,{'value':-1})['value']:
        BEST[key]={'value':float(value),'witness':witness}
    if key in BOUNDS and value>BOUNDS[key]+1e-8:
        dump()
        (OUT/'VIOLATION.json').write_text(json.dumps({'key':key,'value':value,'witness':witness},indent=2))
        raise RuntimeError('Proved bound exceeded: stop and independently recheck')

def residual(key,v): ERRORS[key]=max(ERRORS.get(key,0),float(abs(v)))

def walsh(v):
    a=np.array(v,dtype=np.int64,copy=True)
    h=1
    while h<len(a):
        q=a.reshape(-1,2,h); u=q[:,0,:].copy();v=q[:,1,:].copy()
        q[:,0,:]=u+v; q[:,1,:]=u-v; h*=2
    return a

def signsums(w):
    # Python integers allow exact rational geometric families beyond int64.
    s=[0]
    for a in w: s=[v+a for v in s]+[v-a for v in s]
    # Last-added variable is the most significant truth-table bit.
    return s

CACHE={}
def dimensions(m):
    if m not in CACHE:
        idx=np.arange(1<<m,dtype=np.int64)
        pc=np.zeros(1<<m,dtype=np.int64)
        for j in range(m):pc+=(idx>>j)&1
        CACHE[m]=(pc,RHOS[:,None]**np.arange(m+1)[None,:])
    return CACHE[m]

def phi(p,q):
    o=np.zeros_like(p,dtype=float); mask=(p>0)&(q>0)
    o[mask]=p[mask]*np.log2(1+q[mask]/p[mask])+q[mask]*np.log2(1+p[mask]/q[mask]);return o

ROWS=None
def cube(w,ths,kind):
    w=sorted([int(x) for x in w],reverse=True)
    a=w[0]; m=len(w)-1; sums=signsums(w[1:]); N=len(sums)
    huge=max([abs(x) for x in sums]+[a])>2**58
    v=np.array(sums,dtype=object if huge else np.int64)
    pc,powers=dimensions(m)
    for th2 in sorted(set(int(x) for x in ths)):
        assert th2%2, 'use odd doubled thresholds to remove all ties'
        z=2*v-th2
        slab=np.asarray(np.abs(z)<2*a,dtype=np.int64)
        up=np.asarray(z>2*a,dtype=np.int64)
        dn=np.asarray(z< -2*a,dtype=np.int64)
        delta=float(slab.sum()/N)
        COUNTS['cube_cases']=COUNTS.get('cube_cases',0)+1
        COUNTS[kind]=COUNTS.get(kind,0)+1
        if delta==0:
            assert up.sum()==N or dn.sum()==N
            COUNTS['constants']=COUNTS.get('constants',0)+1;continue
        f0=up-dn
        ah=walsh(f0);bh=walsh(slab);uh=walsh(up);dh=walsh(dn)
        # m<=15: squared integer numerators and their sums are exact in int64.
        anum=np.bincount(pc,weights=ah*ah,minlength=m+1)
        bnum=np.bincount(pc,weights=bh*bh,minlength=m+1)
        cnum=np.bincount(pc,weights=uh*dh,minlength=m+1)
        A=anum/(N*N);B=bnum/(N*N);Cl=cnum/(N*N)
        residual('parseval_A',A.sum()-(1-delta));residual('parseval_B',B.sum()-delta)
        residual('B0',B[0]-delta**2)
        At=np.cumsum(A[::-1])[::-1];Bh=np.cumsum(B)
        products=At*Bh/delta**2
        k=int(np.argmax(products)); kp=int(np.argmax(products[1:])+1) if m else 0
        stay=powers@B;cross=2*(powers@Cl);st0=powers@A
        residual('noise_identity',np.max(np.abs((1-delta-st0)-((delta-stay)+2*cross))))
        residual('independent_cross',cross[0]-2*float(up.mean())*float(dn.mean()))
        residual('independent_stay',stay[0]-delta**2)
        residual('rho1_cross',cross[-1]);residual('rho1_stay',stay[-1]-delta)
        R=cross*stay/delta**2;ri=int(np.argmax(R))
        # Search all numerically real stationary roots of the exact-coefficient
        # product polynomial, as well as the fixed rho mesh and endpoints.
        derivative=np.polynomial.polynomial.polyder(np.polynomial.polynomial.polymul(2*Cl,B))
        roots=np.polynomial.polynomial.polyroots(derivative) if np.any(derivative) else []
        candidates=[float(z.real) for z in roots if abs(z.imag)<1e-7 and 0<z.real<1]
        rbest=float(RHOS[ri]);vbest=float(R[ri])
        for r in candidates:
            value=float(np.polynomial.polynomial.polyval(r,2*Cl)*np.polynomial.polynomial.polyval(r,B)/delta**2)
            if value>vbest:rbest=r;vbest=value
        COUNTS['stationary_root_candidates']=COUNTS.get('stationary_root_candidates',0)+len(candidates)
        L=float(phi(A,B).sum()/delta)
        E=float(phi(ah*ah/(N*N),bh*bh/(N*N)).sum()/delta)
        assert E<=L+1e-10
        # Full-function entropy via coefficients a and b, without an extra transform.
        mu=np.r_[ah*ah,bh*bh]/(N*N);nz=mu>0
        H=float(-np.dot(mu[nz],np.log2(mu[nz])))
        I=float(np.dot(A,np.arange(m+1))+np.dot(B,np.arange(m+1)+1))
        row={'kind':kind,'n':len(w),'weights':w,'theta_twice':th2,'theta_sd':th2/(2*math.sqrt(sum(x*x for x in w))), 'delta':delta,'M_all':float(products[k]),'K_all':k,'M_positive':float(products[kp]) if m else 0,'K_positive':kp if m else None,'L_over_delta':L,'E_over_delta':E,'cross_stay':vbest,'rho':rbest,'H_over_I':H/I}
        ROWS.write(json.dumps(row)+'\n')
        for key in ('M_all','M_positive','L_over_delta','E_over_delta','cross_stay','H_over_I'):update(key,row[key],row)
        # Verify both level-noise bounds at all applicable K at the exact chosen rho.
        for K in range(1,m+1):
            rho=.5 if K==1 else 1-1/K
            pw=rho**np.arange(m+1)
            sb=float(pw@B); loss=float((1-pw)@A)
            assert Bh[K]<=rho**(-K)*sb+1e-10
            assert At[K]<=loss/(1-rho**K)+1e-10
        COUNTS['noise_rates']=COUNTS.get('noise_rates',0)+len(RHOS)
    if COUNTS.get('cube_cases',0)%100< len(ths):dump()


def thresholds(w,exhaustive=False):
    if exhaustive:
        # Every different truth table at a nonnegative threshold, incl. constant.
        ats=sorted(set(abs(x) for x in signsums(w)))
        return [1]+[2*x+1 for x in ats]
    sd=math.sqrt(sum(x*x for x in w))
    return [2*math.floor(t*sd)+1 for t in np.arange(0,4.00001,.25)]


def lemmas(w,kind):
    w=[int(x) for x in w];s=np.sort(np.array(signsums(w),dtype=np.int64))*32
    atoms=np.unique(s);mx=max(w);N=len(s)
    for a32 in sorted(set([32*mx,32*mx+8,40*mx,64*mx])):
        # All endpoint cells are integer; +/-1 samples both open sides exactly.
        breaks=np.r_[atoms+a32,atoms-a32,0]
        cc=np.unique(np.r_[breaks-1,breaks,breaks+1]);cc=cc[cc>=0]
        den=np.searchsorted(s,cc+a32,side='right')-np.searchsorted(s,cc-a32,side='left')
        minidx=np.zeros(len(cc),dtype=int);jj=0
        for j in range(len(cc)):
            if den[j]<den[jj]:jj=j
            minidx[j]=jj
        aa0=np.r_[atoms,atoms-a32,0]
        aa=np.unique(np.r_[aa0-1,aa0,aa0+1]);aa=aa[aa>=0]
        num=np.searchsorted(s,aa+a32,side='right')-np.searchsorted(s,aa,side='left')
        for al,numerator in zip(aa,num):
            if not numerator:continue
            j=minidx[np.searchsorted(cc,al,side='right')-1];d=int(den[j])
            value=float(numerator/d) if d else float('inf')
            update('lemma_A',value,{'weights':w,'a':a32/32,'alpha':int(al)/32,'c':int(cc[j])/32,'numerator_count':int(numerator),'denominator_count':d,'sign_patterns':N,'kind':kind})
        tail=N-np.searchsorted(s,cc+a32,side='right')
        fac=1+math.sqrt(sum(x*x for x in w))/(a32/32)
        for t,numerator,d in zip(cc,tail,den):
            if not numerator:continue
            value=float(numerator/(fac*d)) if d else float('inf')
            update('lemma_B',value,{'weights':w,'a':a32/32,'t':int(t)/32,'tail_count':int(numerator),'window_count':int(d),'sign_patterns':N,'kind':kind})
        COUNTS['lemma_window_scales']=COUNTS.get('lemma_window_scales',0)+1
    COUNTS['lemma_weight_sets']=COUNTS.get('lemma_weight_sets',0)+1


def run():
    global ROWS
    ROWS=open('cube_rows.jsonl','w',buffering=1)
    for n in range(1,17):
        grid=range(1,5) if n<=8 else range(1,4)
        for w in itertools.combinations_with_replacement(grid,n):
            cube(w,thresholds(w,True),'rational_grid_all_thresholds')
            if n<=6:lemmas(w,'rational_grid')
        print('grid dimension',n,COUNTS,flush=True);dump()
    for n in [1,2,3,4,6,8,10,12,14,16]:
        fams={'equal':[1]*n,'linear':list(range(1,n+1)),'one_heavy':[4*n]+[1]*(n-1),'two_heavy':[4*n]*min(n,2)+[1]*max(0,n-2),'zeros':[1]+[0]*(n-1)}
        for p,q in [(1001,1000),(101,100),(11,10),(3,2),(19,10),(199,100),(2,1),(201,100)]:
            fams['geometric_%d_%d'%(p,q)]=[p**j*q**(n-1-j) for j in range(n)]
        for rep in range(6):fams['integer_random_%d'%rep]=list(map(int,RNG.integers(1,33,n)))
        for kind,w in fams.items():
            cube(w,thresholds(w),kind)
            if kind in ('equal','linear','one_heavy','two_heavy'):
                lemmas(w,kind)
        print('families dimension',n,COUNTS,flush=True);dump()
    # Additional integer/rational small-step adversarial windows, exact <=16 bits.
    for rep in range(160):
        n=int(RNG.integers(1,17));w=list(map(int,RNG.integers(1,17,n)))
        lemmas(w,'random_integer')
        if rep%20==0:print('lemma random',rep,flush=True);dump()
    ROWS.close();dump();print(json.dumps({'counts':COUNTS,'best':{k:v['value'] for k,v in BEST.items()},'max_residuals':ERRORS,'elapsed_seconds':time.time()-START,'actual_nice':os.getpriority(os.PRIO_PROCESS,0),'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2),flush=True)

if __name__=='__main__':run()
