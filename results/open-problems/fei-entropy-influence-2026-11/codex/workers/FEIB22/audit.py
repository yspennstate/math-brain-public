"""Final independent audit and machine-readable consolidated tables."""
import study as s
import csv
import gc
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np

t=time.time();checks=[]
# Full independent L=5 truth table through the provided bit-sliced evaluator.
import mc_chain_reference as mc_chain
L=5;n=25;N=1<<n;words=N//64
wordids=np.arange(words,dtype=np.uint64)
X=np.empty((n,words),dtype=np.uint64)
for j in range(n):
    if j<6:
        pattern=np.packbits(((np.arange(64,dtype=np.uint64)>>j)&1).astype(np.uint8)).view(np.uint64)[0]
        X[j]=pattern
    else:X[j]=np.where(((wordids>>(j-6))&1)!=0,np.uint64(2**64-1),np.uint64(0))
truth=np.unpackbits(mc_chain.Hex(5).eval(X).view(np.uint8));del X,wordids
assert truth.mean()==0.5
ref=mc_chain.wht(2.*truth.astype(float)-1);ref*=ref
mu=s.spectrum(5)
err=float(abs(mu-ref).max());assert err==0
checks.append(dict(check='independent_full_L5_spectrum',entries=N,maximum_absolute_error=err,parseval=float(mu.sum())))
del ref;gc.collect()
exact=json.loads(Path('exact_L5.json').read_text())
inferr=0.;enterr=0.
for i in range(n):
    pair=truth.reshape(-1,2,1<<i)
    delta=float(np.mean(pair[:,0,:]!=pair[:,1,:]))
    inferr=max(inferr,abs(delta-exact['rows'][i]['influence']))
    ent=0.
    for a in range(0,1<<(n-1),1<<18):
        tt=np.arange(a,min(a+(1<<18),1<<(n-1)),dtype=np.uint32)
        ss=(tt&((1<<i)-1))|((tt>>i)<<(i+1));p=mu[ss];q=mu[ss|(1<<i)]
        qp=np.divide(q,p,out=np.zeros_like(p),where=p>0);pq=np.divide(p,q,out=np.zeros_like(q),where=q>0)
        ent+=float((p*np.log1p(qp)+q*np.log1p(pq)).sum()/np.log(2))
    enterr=max(enterr,abs(ent/delta-exact['rows'][i]['erasure_ratio']))
assert inferr==0
checks.append(dict(check='all_L5_influences_direct_flips',sites=n,maximum_absolute_error=inferr))
assert enterr<1e-10
checks.append(dict(check='all_L5_erasure_ratios_stable_log1p',sites=n,maximum_absolute_error=enterr))
del truth,mu;gc.collect()

# Recompute window summaries from saved batch counts with the final estimator.
for L in (() if '--no-windows' in sys.argv else (8,12,16,24)):
    path=Path(f'window_L{L}_original_s{L*1000+7}.npz')
    if path.exists():s.window_summary(path)

small=[];allrows=[]
opt=json.loads(Path('optimal_L5.json').read_text());assert opt['complete']
omap={k:r for r in opt['rows'] for k in r['orbit']}
for L in (3,4,5):
    a=json.loads(Path(f'exact_L{L}.json').read_text());assert a['complete'];mu=s.spectrum(L)
    for r in a['rows']:
        r=dict(r)
        if L==5:
            r.update(best_nested=omap[r['i']]['best_nested'],best_two=omap[r['i']]['best_two'])
        assert r['erasure_ratio']<=r['best_two']+1e-10<=r['best_nested']+1e-10
        allrows.append(dict(L=L,i=r['i'],row=r['row'],col=r['col'],influence=r['influence'],erasure_ratio=r['erasure_ratio'],best_nested=r['best_nested'],best_two=r['best_two'],ball_nested=r['ball_nested'],ball_two=r['ball_two'],se=0))
    i,order,sizes,shell,dist=s.geometry(L,mode='original')
    gr=[int(shell[k]) for k in order]
    p,q=s.spectral_witness(mu,L,i,order,gr,1)
    p2,q2=s.spectral_witness(mu,L,i,order,gr,2)
    pv,qv=s.spectral_witness(mu,L,i,order,rank=2)
    d=float(q.sum());rr=dict(L=L,i=i,influence=d,influence_se=0,nested=float(s.phi(p,q).sum()/d),nested_se=0,two=float(s.phi(p2,q2).sum()/d),two_se=0,vertex_two=float(s.phi(pv,qv).sum()/d),erasure_ratio=a['rows'][i]['erasure_ratio'],block={})
    assert rr['erasure_ratio']<=rr['vertex_two']+1e-10<=rr['two']+1e-10<=rr['nested']+1e-10
    for rad in (1,2):
        vs=[i]+[k for k in order if dist[k]<=rad];m=len(vs);marg=np.zeros(1<<m)
        for start in range(0,len(mu),1<<18):
            idx=np.arange(start,min(start+(1<<18),len(mu)),dtype=np.uint32);key=np.zeros_like(idx)
            for j,k in enumerate(vs):key|=((idx>>k)&1)<<j
            marg+=np.bincount(key,weights=mu[start:start+len(idx)],minlength=len(marg))
        val=float(s.phi(marg[::2],marg[1::2]).sum()/d)
        assert rr['erasure_ratio']<=val+1e-10
        rr['block'][str(rad)]=dict(size=m-1,ratio=val,se=0,q_empty_over_delta=float(marg[1]/d))
    small.append(rr);del mu;gc.collect()
s.save('small_centre_table.json',small)
with Path('exact_all_sites.csv').open('w') as f:
    wr=csv.DictWriter(f,fieldnames=list(allrows[0]));wr.writeheader();wr.writerows(allrows)

blocks=[]
for L in (8,12,16,24):
    for rad in (1,2):
        seed=L*1000+rad;a=json.loads(Path(f'block_L{L}_r{rad}_s{seed}.json').read_text())
        z=np.load(f'block_L{L}_r{rad}_s{seed}.npz');acc=z['acc'];each=int(z['each']);G=len(acc)
        masses=acc.sum(axis=0)/(G*each);d=masses[1::2].sum();ratio=masses[1]/d
        total=acc.sum(axis=0)
        lo=[]
        for b in acc:
            v=total-b;lo.append(v[1]/v[1::2].sum())
        pseudo=G*ratio-(G-1)*np.array(lo)
        a['q_empty_over_delta']=float(ratio);a['q_empty_over_delta_se']=float(pseudo.std(ddof=1)/np.sqrt(G))
        s.save(f'block_L{L}_r{rad}_s{seed}.json',a)
        blocks.append(a)
s.save('block_table.json',blocks)

checks.append(dict(check='all_exact_witness_inequalities',passed=True,sites=len(allrows)))
checks.append(dict(check='optimal_L5_symmetries',results=opt['symmetry_checks']))
checks.append(dict(check='folder_size_bytes',value=sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file())))
assert checks[-1]['value']<200_000_000
s.save('audit.json',dict(passed=True,checks=checks,seconds=time.time()-t,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
print('AUDIT PASS',time.time()-t,flush=True)
