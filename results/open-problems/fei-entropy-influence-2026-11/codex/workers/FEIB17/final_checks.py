import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,math,hashlib,time,resource
from pathlib import Path
import numpy as np
from audit import calc,h
out={}
# Full composed example at m=2,r=7, independently of the product formula.
m=2;r=7;n=m*r+1;ids=np.arange(1<<n);bits=((ids[:,None]>>np.arange(m*r))&1).reshape(-1,m,r);outer=bits.sum(2)>r//2;ip=np.logical_and(outer[:,0],outer[:,1]);f=1-2*ip.astype(float);point=~outer.any(1);z=1-2*((ids>>(n-1))&1);f=np.where(point,z,f);o=calc(f[None,:]);i=n-1
out['composed_truth_table']=dict(m=m,r=r,n=n,E_over_delta=float(o['E'][0,i]/o['Inf'][0,i]),D_over_delta=float(o['D'][0,i]/o['Inf'][0,i]),fresh_influence=float(o['Inf'][0,i]),maximum_block_influence=float(o['Inf'][0,:i].max()),unique_maximum=bool(np.all(o['Inf'][0,:i]<o['Inf'][0,i])))
p=q=.25;c=0;phi=(p+q)*float(h(p/(p+q)));out['steep_edge_counterexample']=dict(p=p,q=q,c=c,Phi=phi,claimed_rhs=(c+1)*q)
p=.03125;n=4;out['complex_singleton_budget']=dict(n=n,p=p,singleton_G_over_I=(1-p)**(n-1)*math.log2(1/p),real_Boolean_bound=2/(math.e*math.log(2)))
# Actual spectra check both claimed tribes witness quantities.
out['tribes_witness']=[]
for w,s in [(2,2),(3,2),(4,2)]:
    n=w*s;ids=np.arange(1<<n);bits=((ids[:,None]>>np.arange(n))&1).reshape(-1,s,w);f=np.where(bits.all(2).any(1),-1.,1.);o=calc(f[None,:]);mu=o['mu'][0];N=(1<<w)-2;i=0;A=sum(mu[j] for j in range(1<<n) if j&N);eta=sum(mu[j] for j in range(1<<n) if j&1 and not(j&N));d=o['Inf'][0,0];beta=2**(-w)
    out['tribes_witness'].append(dict(w=w,s=s,A=float(A),eta=float(eta),A_formula=float(2*(1-2*beta)*d),eta_formula=float(2*beta*d)))
# Validate receipts: finite JSON, identities/inequalities within rounding, exact signs in counterexamples.
paths=['audit_results.json','reductions.json','exact_families.json','vertex_lp.json','witnesses.json','extra_checks.json','records.json','edge_budget.json','singular_examples.json','path_census.json','record_precision.json']
for name in paths:
    obj=json.load(open(name));json.dumps(obj,allow_nan=False)
a=json.load(open('audit_results.json'))
for group in ['all4','sample6','sample7','sample8']:
    for key,val in a[group].items():
        if 'residual' in key or 'violation' in key:assert val<2e-12,(group,key,val)
pc=json.load(open('path_census.json'))
for group in pc.values():
    if 'H_residual' in group:assert group['H_residual']<1e-12 and group['I_residual']<1e-12
rr=json.load(open('reductions.json'));assert rr['nondegenerate_block_counterexample']['bad_rhs']<0
assert all(z['influence_residual']==0 and z['original_coordinate_erasure_residual']<1e-12 for z in rr['gated_switch'])
assert all(z['E_over_delta']>0 and (z['a_reference_singular'] if z['mode']=='a_zero' else z['u_reference_singular']) for z in json.load(open('singular_examples.json')))
assert out['composed_truth_table']['unique_maximum'];assert abs(out['composed_truth_table']['E_over_delta']-json.load(open('exact_families.json'))['bent_majorities'][0]['E_over_delta'])<1e-12
out['receipt_audit']='PASS';out['nice']=os.getpriority(os.PRIO_PROCESS,0);out['maxrss_bytes_macos']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
Path('final_checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
# Freeze read-only source provenance, without copying other workers' data.
sources=[Path('../../RULES.md'),Path('BRIEF.md'),Path('~/fei_solve_agent/FLOW.md'),Path('../FEIB10/PROOFS.md'),Path('../FEIB12/PROOFS.md'),Path('../FEIB11/npn5.txt')]
prov={str(p.resolve()):dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),mtime_epoch=p.stat().st_mtime) for p in sources}
Path('source_provenance.json').write_text(json.dumps(prov,indent=2))
