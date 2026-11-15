"""Assert saved checks, resources and proof witnesses; record a compact manifest."""
import json,hashlib,os,platform,sys,datetime
from pathlib import Path
from numerics import *
import scipy,mpmath

def read(p):return json.loads(Path(p).read_text(),parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
def main():
    check=[read('check_all4.json'),read('check_sample6.json')]
    for r in check:
        assert all(np.isfinite(v) and v<1e-9 for k,v in r.items() if ('max_error' in k or 'max_violation' in k) and k!='slope_finite_difference_max_error')
        assert r['slope_finite_difference_max_error']<1e-7
        assert r['median_claim_max_failure']>0
    ca=read('census_audit.json');assert [r['classes'] for r in ca]==[2,4,14,222,616126]
    for n,r in enumerate(ca,1):assert Path(f'npn{n}.bin').stat().st_size==4*r['classes']
    assert max(r['max_census_disagreement'] for r in ca)<1e-12
    for p in ['classes_all4.json','classes_sample6.json','families_audit.json']:
        rr=read(p);assert max(v for k,v in rr.items() if 'max_' in k or k.endswith('failures') or k.endswith('mismatches'))<1e-9
    lpa=read('induction_audit.json');assert max(r['rechecked_max_violation'] for r in lpa['primal_replay'])<1e-9
    assert max(r['dual_constraint_max_violation'] for r in lpa['dual_replay'])<1e-9
    assert lpa['recursion_explicit_J_max_error']<1e-12
    assert lpa['influence_recursion_max_error']<1e-12
    assert all(r['violating_rows']>0 and r['max_violation']>1e-4 for r in lpa['held_out'])
    lg=read('large_audit.json');assert max(r['binary64_max_error'] for r in lg)<1e-11
    c=read('census5.json');assert c['nice']>=10 and c['threads']==1 and c['maxrss_bytes']<3*1024**3
    runs=[json.loads(x) for x in Path('runs.jsonl').read_text().splitlines()];assert all(r['nice']>=10 and r['exit_code']==0 and r['child_maxrss_bytes']<3*1024**3 for r in runs)
    # Re-derive the numerical values used in the short class arguments.
    maj=1-2*(pc(5)>2);d=data(maj,True);trip=[s for s in range(32) if s.bit_count()==3]
    assert np.all(d['alpha'][0,trip]==3/8) and np.all(abs(d['hat'][0,trip])==1/8)
    assert abs(d['gamma'][0]-(10/64)*np.log2(3))<1e-14
    f=np.ones(4);f[0]=-1;da=data(f,True);assert da['gamma'][0]==.25
    proof_witnesses=dict(AND2_gamma_bits=float(da['gamma'][0]),majority5_gamma_bits=float(d['gamma'][0]),majority5_triple_alpha=3/8,majority5_triple_hat_magnitude=1/8,majority5_triples=len(trip),Gamma_one_sign_coefficient=1/(2*np.log(2)))
    Path('proof_witnesses.json').write_text(json.dumps(proof_witnesses,indent=2))
    for p in Path('.').glob('*.json'):read(p.name)
    size=sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file());assert size<10**9
    sums={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('.').glob('*') if p.is_file() and p.suffix in ['.py','.c','.bin']}
    out=dict(status='PASS',timestamp=datetime.datetime.now().astimezone().isoformat(),python=sys.version,numpy=np.__version__,scipy=scipy.__version__,mpmath=mpmath.__version__,nice=os.getpriority(os.PRIO_PROCESS,0),folder_bytes_at_audit=size,max_recorded_process_rss_bytes=max(r['child_maxrss_bytes'] for r in runs),census5_cpu_seconds=c['cpu_seconds'],census5_maxrss_bytes=c['maxrss_bytes'],max_census_disagreement=max(r['max_census_disagreement'] for r in ca),max_large_example_error=max(r['binary64_max_error'] for r in lg),max_finite_difference_slope_error=max(r['slope_finite_difference_max_error'] for r in check),local_recursion_J_error=lpa['recursion_explicit_J_max_error'],local_influence_recursion_error=lpa['influence_recursion_max_error'],proof_witnesses=proof_witnesses,source_and_census_sha256=sums)
    Path('final_audit.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='source_and_census_sha256'},indent=2))
if __name__=='__main__':main()
