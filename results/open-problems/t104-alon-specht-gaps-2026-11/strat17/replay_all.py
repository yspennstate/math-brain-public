"""Self-contained, sequential exact replay. No solver, network, or outside reads."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import hashlib
import json
import resource
import subprocess
import sys
import time
from pathlib import Path
from memory_guard import install,peak_bytes

HERE=Path(__file__).resolve().parent
INHERITED=['exact_audit.py','verify_rank_three_algebra.py','padding_monotonicity.py',
 'concavity_certificate.py','rank_two_certificate.py','tree_certificate.py',
 'disconnected_certificate.py','extreme_inventory.py','verify_sos.py',
 'prior_concavity4.py','prior_triangles.py','split34_trees.py','split34_boundary.py',
 'split34_audit.py','split34_reduction.py','prior_four.py','lower_components.py']
NEW=['lower_formula.py','split_endpoint_certificate.py','matrix_audit.py','double_increment.py','double_small_gap.py','double_small_gap_audit.py','split44_setup.py']


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    if sys.flags.optimize:raise RuntimeError('Assertions must be enabled')
    install();start=time.monotonic();records=[]
    sources=json.loads((HERE/'source_hashes.json').read_text())
    for name,rec in sources.items():assert digest(HERE/name)==rec['sha256'],name
    # Include every proof module/data file, provenance statement and ledger.
    names=set(sources)|{p.name for p in HERE.glob('*.py')}|{'source_hashes.json','RESULT.md'}
    hashes={name:digest(HERE/name)for name in sorted(names)}
    stages=[('inherited16/'+name,HERE/'inherited16')for name in INHERITED]+[(name,HERE)for name in NEW]
    for rel,cwd in stages:
        t=time.monotonic();print('Exact replay:',rel,flush=True)
        code="import sys,runpy;sys.path.insert(0,sys.argv[1]);from memory_guard import install;install();sys.path.insert(0,sys.argv[2]);runpy.run_path(sys.argv[3],run_name='__main__')"
        with (HERE/(rel.replace('/','_')+'.out')).open('w')as out:
            proc=subprocess.run([sys.executable,'-B','-c',code,str(HERE),str(cwd),str(HERE/rel)],cwd=cwd,stdout=out,stderr=subprocess.STDOUT)
        rec={'script':rel,'status':'PASS'if proc.returncode==0 else 'FAIL','seconds_NUMERICAL':time.monotonic()-t}
        records.append(rec)
        if proc.returncode:
            print(json.dumps(records,indent=2));raise RuntimeError(rel+' failed; inspect '+rel.replace('/','_')+'.out')
    assert hashes=={name:digest(HERE/name)for name in sorted(names)}
    child=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    if sys.platform!='darwin':child*=1024
    parent=peak_bytes();assert parent+child<1_500_000_000
    summary={'label':'PROVED (replay_all.py): split 2+5 and 3+4 allow arbitrary lower components; five-vertex double carrier allows arbitrary lowers; 4+4 fixed-vector setup only',
      'checks':records,'seconds_NUMERICAL':time.monotonic()-start,
      'child_peak_bytes_NUMERICAL':child,'parent_peak_bytes_NUMERICAL':parent,
      'aggregate_peak_upper_bound_bytes_NUMERICAL':child+parent,
      'compute_child_processes_at_once':1,'thread_limits':1,'memory_guard_child_bytes':1_000_000_000,
      'proof_hashes':hashes,'source_manifest':'source_hashes.json',
      'external_reads_required':False,'strat15_full_cover_replayed':False}
    (HERE/'replay_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    with (HERE/'LOG.md').open('a')as f:f.write('\nPROVED (replay_all.py): '+str(len(records))+' stages PASS. NUMERICAL seconds '+str(summary['seconds_NUMERICAL'])+', aggregate peak upper bound '+str(child+parent)+' bytes.\n')
    print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':main()
