"""Check tangent targets against known spectra and the finite-block lower bound."""
import study as s
import json
import numpy as np
from pathlib import Path

checks=[]
L=3;mu=s.spectrum(L);i,order,sizes,shell,dist=s.geometry(L)
vs=[i]+[k for k in order if dist[k]<=1];M=1<<len(vs);v=np.zeros(M)
for S,w in enumerate(mu):v[sum(((S>>k)&1)<<j for j,k in enumerate(vs))]+=w
z=np.load('block_L3_r1_s314159.npz');pilot=z['acc'][:8].sum(axis=0);pilot/=pilot.sum();d=pilot[1::2].sum();alpha=.001
p0=(1-alpha)*pilot[::2]+alpha*(1-d)/(M//2)
q0=(1-alpha)*pilot[1::2]+alpha*d/(M//2)
actual=float(s.phi(v[::2],v[1::2]).sum()/v[1::2].sum())
target=float((v[::2]@np.log2(1+q0/p0)+v[1::2]@np.log2(1+p0/q0))/v[1::2].sum())
assert target>=actual-1e-12
checks.append(dict(check='block_tangent_on_exact_L3_distribution',actual=actual,target=target,slack=target-actual,se=0))

L=4;i,order,sizes,shell,dist=s.geometry(L);J=len(sizes)
p,q=s.spectral_witness(s.spectrum(L),L,i,order,[int(shell[k]) for k in order],2)
pilot=json.loads(Path('window_L4_radii_s271828.json').read_text());pp=np.maximum(pilot['p'],0);pq=np.maximum(pilot['q'],0);pp[-1,-1]=pq[-1,-1]=0
allowed=np.triu(np.ones_like(pp,dtype=bool));allowed[-1,-1]=False;alpha=.1
for a,sz in enumerate(np.diff([0]+sizes)):
    if sz==1:allowed[a,a]=False
p0=(1-alpha)*pp+alpha*pp.sum()*allowed/allowed.sum();q0=(1-alpha)*pq+alpha*pq.sum()*allowed/allowed.sum()
wp=np.zeros_like(pp);wq=wp.copy();wp[allowed]=np.log2(1+q0[allowed]/p0[allowed]);wq[allowed]=np.log2(1+p0[allowed]/q0[allowed])
actual=float(s.phi(p,q).sum()/q.sum());target=float((p*wp+q*wq).sum()/q.sum())
assert target>=actual-1e-12
checks.append(dict(check='window_tangent_on_exact_L4_distribution',actual=actual,target=target,slack=target-actual,se=0))

small=json.loads(Path('small_centre_table.json').read_text())
for r in small:
    for a in r['block'].values():assert a['q_empty_over_delta']>=2.**(-a['size'])-1e-12
count=0
for L in (8,12,16,24):
    for rad in (1,2):
        path=f'block_L{L}_r{rad}_s{L*1000+rad}.npz';z=np.load(path);a=z['acc'];b=len(z['vs'])-1
        # The inequality holds for each restricted table and hence each batch.
        assert np.all(a[:,1]>=2.**(-b)*a[:,1::2].sum(axis=1)-1e-12)
        assert np.max(abs(a.sum(axis=1)-int(z['each'])))<1e-10
        count+=len(a)
checks.append(dict(check='finite_block_lower_bound_and_parseval',large_board_batches=count,passed=True))
s.save('audit_estimators.json',dict(passed=True,checks=checks))
print('ESTIMATOR AUDIT PASS')
