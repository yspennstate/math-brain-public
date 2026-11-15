"""Reproducible FEIB22 computations. All writes go to this directory."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import ctypes as ct
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
LIB=ct.CDLL(str(ROOT/'engine.dylib'))
D=np.ctypeslib.ndpointer(dtype=np.float64,flags='C_CONTIGUOUS')
I=np.ctypeslib.ndpointer(dtype=np.int32,flags='C_CONTIGUOUS')
LIB.spectrum.argtypes=[ct.c_int,D]
LIB.transform.argtypes=[D,ct.c_int]
LIB.check_piv.argtypes=[ct.c_int,ct.c_int,ct.c_uint64]
LIB.optimal.argtypes=[D,ct.c_int,ct.c_int,ct.c_int,D,I,I]
LIB.blocks.argtypes=[ct.c_int,ct.c_int,I,ct.c_int,ct.c_int,ct.c_int,ct.c_uint64,D]
LIB.window.argtypes=[ct.c_int,ct.c_int,I,ct.c_int,ct.c_int,ct.c_int,ct.c_uint64,D]

def save(name,obj):
    p=ROOT/name
    p.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')

def phi(p,q):
    p,q=np.broadcast_arrays(np.maximum(p,0.),np.maximum(q,0.))
    with np.errstate(divide='ignore',invalid='ignore'):
        return np.where(p>0,p*np.log2(1+np.divide(q,p,out=np.zeros_like(p),where=p>0)),0)+np.where(q>0,q*np.log2(1+np.divide(p,q,out=np.zeros_like(q),where=q>0)),0)

def geometry(L,i=None,mode='radii'):
    if i is None:i=(L//2)*L+L//2
    r,c=divmod(i,L)
    dist=np.array([max(abs(a-r),abs(b-c),abs(a-r+b-c)) for a in range(L) for b in range(L)])
    order=sorted((k for k in range(L*L) if k!=i),key=lambda k:(dist[k],k))
    if mode=='radii':
        radii=[1,2,3,4,6,8,12,16,24,32,48,64,96]
        sizes=sorted(set(sum(dist[k]<=rad for k in order) for rad in radii))
        sizes=[s for s in sizes if s]
    elif mode=='original':
        from mc_chain_reference import Hex
        sizes=Hex(L).sizes
    else:sizes=list(range(1,L*L))
    shell=np.full(L*L,-1,dtype=np.int32)
    start=0
    for j,end in enumerate(sizes):
        shell[order[start:end]]=j;start=end
    return i,order,sizes,shell,dist

def spectrum(L):
    mu=np.empty(1<<(L*L),dtype=np.float64)
    LIB.spectrum(L,mu)
    return mu

def spectral_witness(mu,L,i,order,groups=None,rank=1):
    """Exact atom masses, without allocating a large S x n bit table."""
    n=L*L;N=1<<n
    if groups is None:groups=list(range(n-1))
    J=max(groups)+1
    # rank 1: first shell, rank 2: ordered first-two shell labels, J=none.
    p=np.zeros((J+1,J+1) if rank==2 else J+1)
    q=np.zeros_like(p)
    chunk=1<<18
    for start in range(0,N,chunk):
        S=np.arange(start,min(start+chunk,N),dtype=np.uint32)
        first=np.full(len(S),J,dtype=np.int32)
        second=first.copy()
        for k,g in zip(order,groups):
            hit=(S>>k)&1!=0
            take=hit&(first==J)
            if rank==2:second[hit&~take&(second==J)]=g
            first[take]=g
        has=(S>>i)&1!=0
        key=first*(J+1)+second if rank==2 else first
        p.flat[:]+=np.bincount(key[~has],weights=mu[start:start+len(S)][~has],minlength=p.size)
        q.flat[:]+=np.bincount(key[has],weights=mu[start:start+len(S)][has],minlength=q.size)
    return p,q

def exact(L,opt=True):
    t=time.time();mu=spectrum(L);n=L*L
    rows=[]
    for i in range(n):
        # Pair mu(T),mu(T+i) using a reshape; max temporary under 300 MiB.
        pair=mu.reshape(-1,2,1<<i)
        delta=float(pair[:,1,:].sum())
        entropy=float(phi(pair[:,0,:],pair[:,1,:]).sum())
        _,order,sizes,shell,dist=geometry(L,i)
        gr=[int(shell[k]) for k in order]
        p,q=spectral_witness(mu,L,i,order,gr,1)
        p2,q2=spectral_witness(mu,L,i,order,gr,2)
        f1=float(phi(p,q).sum()/delta);f2=float(phi(p2,q2).sum()/delta)
        row=dict(i=i,row=i//L,col=i%L,influence=delta,erasure_ratio=entropy/delta,ball_nested=f1,ball_two=f2,se=0)
        if opt:
            out=np.zeros(3);o1=np.zeros(n-1,np.int32);o2=o1.copy()
            LIB.optimal(mu,n,i,int(L<=4),out,o1,o2)
            row.update(best_nested=out[1],nested_order=o1.tolist())
            if L<=4:row.update(best_two=out[2],two_order=o2.tolist())
            # Independent regrouping verifies the reconstructed optimising order.
            a,b=spectral_witness(mu,L,i,o1,rank=1)
            assert abs(float(phi(a,b).sum()/delta)-out[1])<1e-9
            if L<=4:
                a,b=spectral_witness(mu,L,i,o2,rank=2)
                assert abs(float(phi(a,b).sum()/delta)-out[2])<1e-9
        rows.append(row)
        save(f'exact_L{L}.json',dict(L=L,rows=rows,parseval=float(mu.sum()),mean_squared=float(mu[0]),seconds=time.time()-t,complete=len(rows)==n))
        print('EXACT',L,i,delta,entropy/delta,f1,f2,row.get('best_nested'),row.get('best_two'),flush=True)
    return mu,rows

def block_run(L,r,G,each,seed):
    i,order,sizes,shell,dist=geometry(L)
    vs=np.array([i]+[k for k in order if dist[k]<=r],dtype=np.int32)
    m=len(vs);N=1<<m
    # G*2^19*8 = 64 MiB at G=16; no truth table is saved.
    acc=np.zeros((G,N),np.float64);t=time.time()
    for g in range(G):
        LIB.blocks(L,i,vs,m,1,each,seed+g*1000003,acc[g])
        print('BLOCK',L,r,g+1,G,'seconds',round(time.time()-t,2),flush=True)
    np.savez_compressed(ROOT/f'block_L{L}_r{r}_s{seed}.npz',acc=acc,each=each,vs=vs,seed=seed,seconds=time.time()-t)
    return block_summary(L,r,seed)

def block_summary(L,r,seed):
    z=np.load(ROOT/f'block_L{L}_r{r}_s{seed}.npz');acc=z['acc'];each=int(z['each']);G=len(acc)
    def vals(a):
        v=a/a.sum();p=v[::2];q=v[1::2];d=q.sum();return float(phi(p,q).sum()/d),float(d)
    split=[]
    for k in (1,2,4,8,16,32):
        if k>G or G%k:continue
        v=np.array([vals(acc[a:a+k].sum(axis=0)) for a in range(0,G,k)])
        split.append(dict(N=k*each,groups=len(v),plugin=float(v[:,0].mean()),plugin_se=float(v[:,0].std(ddof=1)/math.sqrt(len(v))) if len(v)>1 else None,influence=float(v[:,1].mean())))
    # Delete-group jackknife of the pooled plugin and influence.
    total=acc.sum(axis=0);base=np.array(vals(total));loo=np.array([vals(total-a) for a in acc]);pseudo=G*base-(G-1)*loo
    # First half chooses gradients, second half estimates their expectation.
    # Concavity + homogeneity gives Phi(p,q)<=p log2(1+q0/p0)+q log2(1+p0/q0).
    # A positive reference mass makes gradients finite even at pilot zeros.
    pilot=acc[:G//2].sum(axis=0);pilot/=pilot.sum();dp=pilot[1::2].sum()
    tangent=[]
    for alpha in (0.001,0.01,0.1):
        p0=(1-alpha)*pilot[::2]+alpha*(1-dp)/(len(pilot)//2)
        q0=(1-alpha)*pilot[1::2]+alpha*dp/(len(pilot)//2)
        wp=np.log2(1+q0/p0);wq=np.log2(1+p0/q0)
        hold=acc[G//2:]/each
        h=np.stack([hold[:,::2]@wp+hold[:,1::2]@wq,hold[:,1::2].sum(axis=1)],axis=1)
        mean=h.mean(axis=0);ratio=mean[0]/mean[1]
        infl=(h[:,0]-ratio*h[:,1])/mean[1]
        tangent.append(dict(alpha=alpha,ratio=float(ratio),se=float(infl.std(ddof=1)/math.sqrt(len(infl))),validation_N=each*len(hold)))
    result=dict(L=L,r=r,i=int(z['vs'][0]),block_size=len(z['vs'])-1,G=G,each=each,N=G*each,seed=seed,seconds=float(z['seconds']),split=split,plugin=float(base[0]),plugin_jackknife=float(pseudo[:,0].mean()),plugin_jackknife_se=float(pseudo[:,0].std(ddof=1)/math.sqrt(G)),influence=float(base[1]),influence_se=float(pseudo[:,1].std(ddof=1)/math.sqrt(G)),tangent=tangent)
    save(f'block_L{L}_r{r}_s{seed}.json',result)
    print(json.dumps(result,indent=2),flush=True)
    return result

def window_atoms(row,L,sizes,shell,endpoint=True):
    J=len(sizes);n=L*L;d=row[0]
    W=np.r_[d,row[2:2+J]].copy();C=np.r_[1-d,row[2+J:2+2*J]].copy()
    # Exact balance by Hex duality and monotonicity: fhat(empty)=0, fhat(i)=Inf_i.
    if endpoint:W[-1]=d*d;C[-1]=0.
    H=row[2+2*J:2+2*J+J*J].reshape(J,J)/4
    G=row[2+2*J+J*J:2+2*J+2*J*J].reshape(J,J)/4
    def cells(Z,F):
        out=np.zeros((J+1,J+1))
        out[J,J]=Z[-1]
        for a in range(J):
            out[a,J]=F[a,-1]
            out[a,a]=Z[a]-Z[a+1]-F[a,a]
            # A singleton shell cannot contain two distinct spectral points.
            # Enforce this exact zero rather than clipping its correlation noise.
            if sizes[a]-(sizes[a-1] if a else 0)==1:out[a,a]=0.
            for b in range(a+1,J):out[a,b]=F[a,b-1]-F[a,b]
        return out
    return cells(C,G),cells(W,H),C[:-1]-C[1:],W[:-1]-W[1:]

def window_summary(path):
    z=np.load(path);data=z['data']/int(z['each']);L=int(z['L']);each=int(z['each']);sizes=z['sizes'].tolist();shell=z['shell'];B=len(data);J=len(sizes);n=L*L
    def metrics(rows,endpoint=True,weights=None):
        row=rows.mean(axis=0).copy();off=2+2*J+2*J*J
        # Endpoint F(all) = sum of squared Fourier singleton coefficients.
        # Unbiased across independent batch means; this greatly reduces noise.
        for side in range(2):
            v=rows[:,off+side*n:off+(side+1)*n]/2
            sq=v.mean(axis=0)**2-v.var(axis=0,ddof=1)/len(v)
            for a in range(J):row[2+2*J+side*J*J+a*J+J-1]=4*sq[shell==a].sum()
        # Correct delta^2 just as for singleton derivative coefficients.
        d2=row[0]**2-rows[:,0].var(ddof=1)/len(rows)
        p,q,a,b=window_atoms(row,L,sizes,shell,endpoint)
        q[-1,-1]=d2
        # W(all) also enters the final nested and same-shell atom.
        b[-1]+=row[0]**2-d2
        if sizes[-1]-(sizes[-2] if J>1 else 0)>1:q[-2,-2]+=row[0]**2-d2
        d=row[0]
        nested=float(phi(a,b).sum())/d
        two=float(phi(p,q).sum()/d) if weights is None else float((p*weights[0]+q*weights[1]).sum()/d)
        negp=float(-np.minimum(p,0).sum());negq=float(-np.minimum(q,0).sum())
        ww=np.r_[d,row[2:2+J]].copy();ww[-1]=d2
        vv=np.r_[0,(1-d)-row[2+J:2+2*J]];vv[-1]=1-d
        prod=float(np.max(ww[:-1]*vv[1:]/d**2))
        return np.array([d,nested,two,negp,negq,prod]),(p,q)
    base,atoms=metrics(data);loo=np.array([metrics(np.delete(data,k,axis=0))[0] for k in range(B)]);pseudo=B*base-(B-1)*loo
    se=pseudo.std(axis=0,ddof=1)/math.sqrt(B)
    split=[]
    for k in (2,4,8,16,32,64):
        if k>B or B%k:continue
        v=np.array([metrics(data[a:a+k])[0] for a in range(0,B,k)])
        split.append(dict(N=k*each,repeats=len(v),nested=float(v[:,1].mean()),two=float(v[:,2].mean()),two_se=float(v[:,2].std(ddof=1)/math.sqrt(len(v))) if len(v)>1 else None,negative_q_mass=float(v[:,4].mean())))
    tangent=[]
    if B>=8:
        pp,pq=metrics(data[:B//2])[1]
        allowed=np.triu(np.ones_like(pp,dtype=bool));allowed[-1,-1]=False
        for a,sz in enumerate(np.diff([0]+sizes)):
            if sz==1:allowed[a,a]=False
        pp=np.maximum(pp,0);pq=np.maximum(pq,0)
        pp[-1,-1]=pq[-1,-1]=0
        for alpha in (0.001,0.01,0.1):
            p0=(1-alpha)*pp+alpha*pp.sum()*allowed/allowed.sum()
            q0=(1-alpha)*pq+alpha*pq.sum()*allowed/allowed.sum()
            wp=np.zeros_like(pp);wq=wp.copy();wp[allowed]=np.log2(1+q0[allowed]/p0[allowed]);wq[allowed]=np.log2(1+p0[allowed]/q0[allowed])
            hold=data[B//2:];v=metrics(hold,weights=(wp,wq))[0][2]
            lo=np.array([metrics(np.delete(hold,k,axis=0),weights=(wp,wq))[0][2] for k in range(len(hold))])
            pse=len(hold)*v-(len(hold)-1)*lo
            tangent.append(dict(alpha=alpha,ratio=float(v),se=float(pse.std(ddof=1)/math.sqrt(len(pse))),validation_N=len(hold)*each))
    gain_se=float((pseudo[:,1]-pseudo[:,2]).std(ddof=1)/math.sqrt(B))
    result=dict(L=L,i=int(z['i']),N=B*each,batches=B,each=each,seed=int(z['seed']),sizes=sizes,seconds=float(z['seconds']),influence=float(base[0]),influence_se=float(se[0]),nested=float(base[1]),nested_se=float(se[1]),two=float(base[2]),two_se=float(se[2]),two_jackknife=float(pseudo[:,2].mean()),nested_minus_two=float(base[1]-base[2]),nested_minus_two_se=gain_se,negative_p_mass=float(base[3]),negative_p_mass_se=float(se[3]),negative_q_mass=float(base[4]),negative_q_mass_se=float(se[4]),M=float(base[5]),M_se=float(se[5]),split=split,tangent=tangent,p=atoms[0].tolist(),q=atoms[1].tolist())
    save(Path(path).with_suffix('.json').name,result);print(json.dumps(result,indent=2),flush=True);return result

def window_run(L,B,each,seed,mode='radii'):
    i,order,sizes,shell,dist=geometry(L,mode=mode);J=len(sizes);n=L*L
    data=np.zeros((B,2+2*J+2*J*J+2*n));t=time.time()
    for b in range(B):
        LIB.window(L,i,shell,J,1,each,seed+b*1000003,data[b]);print('WINDOW',L,b+1,B,'seconds',round(time.time()-t,2),flush=True)
        np.savez_compressed(ROOT/f'window_L{L}_{mode}_s{seed}.npz',data=data[:b+1],L=L,i=i,each=each,seed=seed,sizes=sizes,shell=shell,seconds=time.time()-t)
    return window_summary(ROOT/f'window_L{L}_{mode}_s{seed}.npz')

def validate():
    import mc_chain_reference as mc_chain
    checks=[]
    for L in (2,3,4,8,12):
        bad=LIB.check_piv(L,128,123+L);assert bad==0
        checks.append(dict(L=L,pivotal_checks=128*L*L,mismatches=bad))
    for L in (2,3,4):
        mu=spectrum(L);fn=mc_chain.Hex(L);N=1<<(L*L);idx=np.arange(N,dtype=np.uint64)
        x=np.zeros((L*L,max(1,N//64)),dtype=np.uint64)
        # L=2 has only 16 configs; repeat to fill one word.
        ii=np.arange(max(64,N),dtype=np.uint64)%N
        for k in range(L*L):x[k]=np.packbits(((ii>>k)&1).astype(np.uint8)).view(np.uint64)
        truth=np.unpackbits(fn.eval(x).view(np.uint8))[:N]
        ref=mc_chain.wht(2.*truth.astype(float)-1)**2
        err=float(abs(mu-ref).max());assert err<1e-14
        checks.append(dict(L=L,spectrum_vs_mc_chain_max_error=err,parseval=float(mu.sum()),balance=float(mu[0])))
    # Exhaust all outside assignments on L=3 and compare the restriction mixture
    # to marginalising the full spectrum, using all radius-one variables.
    L=3;mu=spectrum(L);i,order,sizes,shell,dist=geometry(L);vs=np.array([i]+[k for k in order if dist[k]<=1],np.int32);m=len(vs)
    outside=[k for k in range(9) if k not in vs];mix=np.zeros(1<<m)
    for y in range(1<<len(outside)):
        a=np.empty(1<<m)
        for t in range(1<<m):
            bits=[0]*9
            for j,k in enumerate(vs):bits[k]=(t>>j)&1
            for j,k in enumerate(outside):bits[k]=(y>>j)&1
            a[t]=2*mc_chain.scalar_ref('hex:3',bits)-1
        LIB.transform(a,m);mix+=a*a/(1<<len(outside))
    marginal=np.zeros(1<<m)
    for s,v in enumerate(mu):marginal[sum(((s>>int(k))&1)<<j for j,k in enumerate(vs))]+=v
    err=float(abs(mix-marginal).max());assert err<1e-14
    checks.append(dict(block_mixture_exact_error=err))
    # Engine restricted graph: test random outside mixture against exhaustive mixture.
    block=block_run(3,1,16,256,314159)
    z=np.load(ROOT/'block_L3_r1_s314159.npz');est=z['acc'].sum(axis=0)/(16*256)
    err=float(abs(est-marginal).max());assert err<0.04
    checks.append(dict(block_mc_max_error=err,N=4096))
    # All first-two cell masses from second derivatives against the exact spectrum.
    win=window_run(4,16,2048,271828)
    i,order,sizes,shell,dist=geometry(4);p,q=spectral_witness(spectrum(4),4,i,order,[int(shell[k]) for k in order],2)
    ep=float(abs(np.array(win['p'])-p).max());eq=float(abs(np.array(win['q'])-q).max())
    assert max(ep,eq)<0.025
    checks.append(dict(window_L4_N=32768,max_p_atom_error=ep,max_q_atom_error=eq,exact_nested=float(phi(*spectral_witness(spectrum(4),4,i,order,[int(shell[k]) for k in order],1)).sum()/q.sum()),exact_two=float(phi(p,q).sum()/q.sum()),mc_two=win['two'],mc_two_se=win['two_se']))
    # Brute-force every ordering on the 2x2 board checks both path optimisations.
    mu=spectrum(2)
    for i in range(4):
        out=np.zeros(3);o1=np.zeros(3,np.int32);o2=o1.copy();LIB.optimal(mu,4,i,1,out,o1,o2)
        vals=[]
        for order in itertools.permutations([k for k in range(4) if k!=i]):
            a,b=spectral_witness(mu,2,i,order,rank=1);a2,b2=spectral_witness(mu,2,i,order,rank=2)
            vals.append((float(phi(a,b).sum()/b.sum()),float(phi(a2,b2).sum()/b.sum())))
        assert np.allclose(out[1:],np.min(vals,axis=0))
    checks.append(dict(optimal_paths_vs_all_L2_orders=True))
    save('validation.json',dict(checks=checks,passed=True))
    print('VALIDATION PASS',flush=True)

if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='validate':validate()
    elif cmd=='exact':exact(int(sys.argv[2]),len(sys.argv)<4 or sys.argv[3]!='noopt')
    elif cmd=='block':block_run(*map(int,sys.argv[2:]))
    elif cmd=='window':window_run(*map(int,sys.argv[2:6]),*sys.argv[6:])
    elif cmd=='block-summary':block_summary(*map(int,sys.argv[2:]))
    elif cmd=='window-summary':window_summary(sys.argv[2])
