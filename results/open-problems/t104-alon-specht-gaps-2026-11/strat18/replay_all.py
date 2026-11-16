"""Sequential self-contained exact replay; inherited files remain immutable."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import hashlib,json,resource,shutil,subprocess,sys,tempfile,time
from pathlib import Path
from inherited17.memory_guard import install,peak_bytes

HERE=Path(__file__).resolve().parent
OLD16=['exact_audit.py','verify_rank_three_algebra.py','padding_monotonicity.py',
 'concavity_certificate.py','rank_two_certificate.py','tree_certificate.py',
 'disconnected_certificate.py','extreme_inventory.py','verify_sos.py',
 'prior_concavity4.py','prior_triangles.py','split34_trees.py','split34_boundary.py',
 'split34_audit.py','split34_reduction.py','prior_four.py','lower_components.py']
OLD17=['lower_formula.py','split_endpoint_certificate.py','matrix_audit.py','double_increment.py',
 'double_small_gap.py','double_small_gap_audit.py','split44_setup.py']
NEW=['tree44.py','boundary44.py','padding44.py','lower44.py','symbolic44.py','audit44.py','symmetric44.py','setup35.py']

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    if sys.flags.optimize:raise RuntimeError('Run with assertions enabled')
    install(200_000_000);start=time.monotonic();records=[]
    source=json.loads((HERE/'source_hashes.json').read_text())
    for name,rec in source.items():assert digest(HERE/name)==rec['sha256'],name
    names=set(source)|{p.name for p in HERE.glob('*.py')}|{'source_hashes.json','RESULT.md'}
    hashes={name:digest(HERE/name)for name in sorted(names)}
    output=HERE/'replay_outputs';output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='replay_work_',dir=HERE)as tmp:
        work=Path(tmp)/'inherited17';shutil.copytree(HERE/'inherited17',work)
        stages=[('inherited17/inherited16/'+name,work/'inherited16',work/'inherited16'/name)for name in OLD16]
        stages += [('inherited17/'+name,work,work/name)for name in OLD17]
        stages += [(name,HERE,HERE/name)for name in NEW]
        for rel,cwd,path in stages:
            t=time.monotonic();print('Exact replay:',rel,flush=True)
            code="import sys,runpy;sys.path.insert(0,sys.argv[1]);from inherited17.memory_guard import install;install(850_000_000);sys.path.insert(0,sys.argv[2]);runpy.run_path(sys.argv[3],run_name='__main__')"
            outpath=output/(rel.replace('/','_')+'.out')
            with outpath.open('w')as out:
                proc=subprocess.run([sys.executable,'-B','-c',code,str(HERE),str(cwd),str(path)],cwd=cwd,stdout=out,stderr=subprocess.STDOUT)
            records.append({'script':rel,'status':'PASS'if proc.returncode==0 else'FAIL','seconds_NUMERICAL':time.monotonic()-t})
            if proc.returncode:
                print(outpath.read_text());raise RuntimeError(rel+' failed')
    assert hashes=={name:digest(HERE/name)for name in sorted(names)}
    child=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    if sys.platform!='darwin':child*=1024
    parent=peak_bytes();assert child+parent<1_500_000_000
    generated={p.name:digest(p)for p in HERE.glob('*_checks.json')}
    generated['lower44_controls.json']=digest(HERE/'lower44_controls.json')
    summary={'label':'PROVED (replay_all.py): complete split 4+4 with arbitrary lower components, all N>=8 and infinity; 3+5 setup only',
      'checks':records,'seconds_NUMERICAL':time.monotonic()-start,
      'child_peak_bytes_NUMERICAL':child,'parent_peak_bytes_NUMERICAL':parent,
      'aggregate_peak_upper_bound_bytes_NUMERICAL':child+parent,
      'compute_children_at_once':1,'threads_per_library':1,'child_memory_guard_bytes':850_000_000,
      'proof_input_hashes':hashes,'generated_certificate_receipt_hashes':generated,
      'external_proof_reads_required':False,'strat15_full_cover_replayed':False,
      'inherited_scripts_replayed':len(OLD16)+len(OLD17),'new_scripts_replayed':len(NEW)}
    (HERE/'replay_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    with (HERE/'LOG.md').open('a')as f:f.write('\nPROVED (replay_all.py): '+str(len(records))+' stages PASS. NUMERICAL runtime '+str(summary['seconds_NUMERICAL'])+' seconds; peak aggregate upper bound '+str(child+parent)+' bytes.\n')
    print(json.dumps({k:v for k,v in summary.items()if k not in ('proof_input_hashes','generated_certificate_receipt_hashes')},indent=2),flush=True)

if __name__=='__main__':main()
