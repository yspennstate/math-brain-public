"""Self-contained exact replay: one guarded compute child at a time."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import hashlib,json,resource,shutil,subprocess,sys,tempfile,time
from pathlib import Path
from inherited20.inherited19.inherited18.inherited17.memory_guard import install,peak_bytes
HERE=Path(__file__).resolve().parent
OLD16=['exact_audit.py','verify_rank_three_algebra.py','padding_monotonicity.py','concavity_certificate.py','rank_two_certificate.py','tree_certificate.py','disconnected_certificate.py','extreme_inventory.py','verify_sos.py','prior_concavity4.py','prior_triangles.py','split34_trees.py','split34_boundary.py','split34_audit.py','split34_reduction.py','prior_four.py','lower_components.py']
OLD17=['lower_formula.py','split_endpoint_certificate.py','matrix_audit.py','double_increment.py','double_small_gap.py','double_small_gap_audit.py','split44_setup.py']
OLD18=['tree44.py','boundary44.py','padding44.py','lower44.py','symbolic44.py','audit44.py','symmetric44.py','setup35.py']
OLD19=['transfer35.py','tree35.py','lower35.py','symbolic35.py','audit35.py','symmetric35.py','setup45.py']
OLD20=['symmetric45.py','transfer45.py','tree45.py','lower45.py','symbolic45.py','audit45.py','setup55.py']
NEW=['symmetric55.py','transfer55.py','tree55.py','rank3_certificate55.py','rank3_pair55.py','lower55.py','symbolic55.py','audit55.py']
MODULES=['algebra55.py','rank3_target55.py','replay_all.py']
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    if sys.flags.optimize:raise RuntimeError('Assertions must be enabled')
    install(200_000_000);start=time.monotonic();records=[]
    sources=json.loads((HERE/'source_hashes.json').read_text())
    for name,rec in sources.items():assert digest(HERE/name)==rec['sha256'],name
    names=set(sources)|set(NEW)|set(MODULES)|{'rank3_sos55.json','source_hashes.json','RESULT.md'}
    hashes={name:digest(HERE/name)for name in sorted(names)}
    output=HERE/'replay_outputs';output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='replay_work_',dir=HERE)as tmp:
        w20=Path(tmp)/'inherited20';shutil.copytree(HERE/'inherited20',w20)
        w19=w20/'inherited19';w18=w19/'inherited18';w17=w18/'inherited17';w16=w17/'inherited16'
        stages=[]
        for prefix,cwd,ns in [('inherited20/inherited19/inherited18/inherited17/inherited16/',w16,OLD16),('inherited20/inherited19/inherited18/inherited17/',w17,OLD17),('inherited20/inherited19/inherited18/',w18,OLD18),('inherited20/inherited19/',w19,OLD19),('inherited20/',w20,OLD20),('',HERE,NEW)]:
            stages.extend((prefix+name,cwd,cwd/name)for name in ns)
        for rel,cwd,path in stages:
            t=time.monotonic();print('Exact replay:',rel,flush=True)
            code="import sys,runpy;sys.path.insert(0,sys.argv[1]);from inherited20.inherited19.inherited18.inherited17.memory_guard import install;install(850_000_000);sys.path.insert(0,sys.argv[2]);runpy.run_path(sys.argv[3],run_name='__main__')"
            outpath=output/(rel.replace('/','_')+'.out')
            with outpath.open('w')as out:
                proc=subprocess.run([sys.executable,'-B','-c',code,str(HERE),str(cwd),str(path)],cwd=cwd,stdout=out,stderr=subprocess.STDOUT)
            records.append(dict(script=rel,status='PASS'if proc.returncode==0 else 'FAIL',seconds_NUMERICAL=time.monotonic()-t))
            if proc.returncode:
                print(outpath.read_text());raise RuntimeError(rel+' failed')
    assert hashes=={name:digest(HERE/name)for name in sorted(names)}
    child=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    if sys.platform!='darwin':child*=1024
    parent=peak_bytes();assert child+parent<1_500_000_000
    total_bytes=sum(p.stat().st_size for p in HERE.rglob('*')if p.is_file());assert total_bytes<500_000_000
    receipts={p.name:digest(p)for p in HERE.glob('*55_checks.json')}
    receipts['lower55_controls.json']=digest(HERE/'lower55_controls.json')
    discovery={p.name:digest(p)for name in ('discover_rank3.py','rationalize_rank3.py','rank3_discovery_meta.json','rank3_discovery.npz','rank3_discovery.out')if(p:=HERE/name).exists()}
    summary=dict(label='PROVED (replay_all.py): split 5+5 with isolates or arbitrary lower components for every N>=10 and fixed-graph infinity; closes disconnected D=2 with all components at most five, under the inherited STRAT15 theorem premise',checks=records,seconds_NUMERICAL=time.monotonic()-start,child_peak_bytes_NUMERICAL=child,parent_peak_bytes_NUMERICAL=parent,aggregate_peak_upper_bound_bytes_NUMERICAL=child+parent,workspace_bytes_NUMERICAL=total_bytes,compute_children_at_once=1,threads_per_library=1,child_memory_guard_bytes=850_000_000,parent_memory_guard_bytes=200_000_000,proof_input_hashes=hashes,generated_certificate_receipt_hashes=receipts,discovery_artifact_hashes=discovery,external_proof_reads_required=False,solver_required_for_replay=False,strat15_full_cover_replayed=False,inherited_scripts_replayed=46,new_scripts_replayed=len(NEW))
    (HERE/'replay_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    with(HERE/'LOG.md').open('a')as f:
        f.write('\nPROVED (replay_all.py): '+str(len(records))+' stages PASS. NUMERICAL elapsed '+str(summary['seconds_NUMERICAL'])+' seconds; aggregate peak upper bound '+str(child+parent)+' bytes; workspace '+str(total_bytes)+' bytes.\n')
    print(json.dumps({k:v for k,v in summary.items()if k not in ('proof_input_hashes','generated_certificate_receipt_hashes','discovery_artifact_hashes')},indent=2),flush=True)
if __name__=='__main__':main()
