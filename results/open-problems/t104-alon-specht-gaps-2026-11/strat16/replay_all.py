"""Replay all STRAT16 proof certificates exactly, sequentially.

Discovery programs and floating solvers are not invoked by this program.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json
import time
import subprocess
import resource
import sys
import hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
SCRIPTS=['exact_audit.py','verify_rank_three_algebra.py','padding_monotonicity.py',
         'concavity_certificate.py','rank_two_certificate.py','tree_certificate.py',
         'disconnected_certificate.py','extreme_inventory.py','verify_sos.py',
         'prior_concavity4.py','prior_triangles.py','split34_trees.py',
         'split34_boundary.py','split34_audit.py','split34_reduction.py',
         'prior_four.py','lower_components.py']


def main():
    if sys.flags.optimize:raise RuntimeError('Exact replay requires Python assertions; do not use -O.')
    tick=time.monotonic();records=[]
    inputs=[*SCRIPTS,'algebra.py','rank_three_target.py','rational_sos_2.json','split34_algebra.py']
    assert (HERE/'prior_concavity4.py').read_bytes()==(HERE/'STRAT7/concavity_certificate.py').read_bytes()
    assert (HERE/'prior_triangles.py').read_bytes()==(HERE/'STRAT7/triangle_certificate.py').read_bytes()
    assert (HERE/'prior_four.py').read_bytes()==(HERE/'STRAT7/four_vertex_certificate.py').read_bytes()
    hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()for name in inputs}
    for script in SCRIPTS:
        start=time.monotonic();print('Exact replay:',script,flush=True)
        with (HERE/(script[:-3]+'.replay.out')).open('w')as out:
            result=subprocess.run([sys.executable,'-B',script],cwd=HERE,stdout=out,stderr=subprocess.STDOUT)
        records.append(dict(script=script,status='PASS'if result.returncode==0 else 'FAIL',seconds_NUMERICAL=time.monotonic()-start))
        if result.returncode:raise RuntimeError(script+' failed; see its .replay.out')
    assert hashes=={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()for name in inputs}
    elapsed=time.monotonic()-tick
    peak=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    if sys.platform!='darwin':peak*=1024
    assert peak<2_500_000_000
    summary=dict(label='PROVED (replay_all.py): split 2+5 and 3+4 with isolates; smaller carrier classes with arbitrary lowers; every real k>=5 and infinity',
        checks=records,seconds_NUMERICAL=elapsed,child_peak_bytes_NUMERICAL=peak,
        parent_peak_bytes_NUMERICAL=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        proof_hashes=hashes,worker_processes=1,
        discovery_limit_breach_recorded_in='RESULT.md')
    (HERE/'replay_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    with(HERE/'LOG.md').open('a')as f:f.write('\nPROVED (replay_all.py): all '+str(len(records))+' exact stages passed. NUMERICAL seconds '+str(elapsed)+', child peak bytes '+str(peak)+'.\n')
    print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':main()
