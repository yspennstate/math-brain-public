"""PROVED: sequential exact replay; no solver, network or child workers."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import contextlib,resource,runpy,sys,time,json
from pathlib import Path
sys.dont_write_bytecode=True
root=Path(__file__).resolve().parent;os.chdir(root)
scripts=['verify_elementary.py','prior_four.py','prior_triangles.py','verify_boundary.py','verify_moments.py',
         'verify_polya_moments.py','prior_scale.py','verify_algebra.py','verify_cell_identities.py',
         'verify_small_ratio.py','verify_cells.py','verify_allN_cells.py','verify_allN_ratio.py',
         'zero_face.py','verify_boxes.py','residual_witness.py','verify_coverage.py']
results=[]
for script in scripts:
    start=time.monotonic()
    with open(script.replace('.py','.out'),'w')as output,contextlib.redirect_stdout(output):runpy.run_path(script,run_name='__main__')
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024 if sys.platform=='darwin' else 1024)
    assert peak<1024,'Exact replay exceeded its 1 GiB RSS guard'
    record=dict(script=script,seconds=time.monotonic()-start,peak_RSS_MiB=peak,resource_measurements='NUMERICAL')
    results.append(record)
    message='PROVED: %s PASS; NUMERICAL: %.2f seconds; peak RSS %.1f MiB'%(script,record['seconds'],peak)
    print(message,flush=True)
    with open('LOG.md','a')as log:log.write('\n'+message+'\n')
with open('replay_summary.json','w')as out:json.dump(dict(label='PROVED',results=results),out,indent=2)
print('PROVED: all exact certificates replayed. OPEN: the full 5+1 theorem is not closed.')
