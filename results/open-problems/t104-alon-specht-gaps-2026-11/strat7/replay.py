"""Run every exact certificate, sequentially, with one thread and RSS reporting."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import contextlib
import resource
import runpy
import sys
import time

scripts=['four_vertex_certificate.py','triangle_certificate.py','concavity_certificate.py','split_boundary_certificate.py','tree_certificate.py','scale_certificate.py','exact_audit.py']
for script in scripts:
    started=time.monotonic()
    with open(script.replace('.py','.out'),'w') as out,contextlib.redirect_stdout(out):
        runpy.run_path(script,run_name='__main__')
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform=='darwin':peak/=1024*1024
    else:peak/=1024
    assert peak<900, 'Replay exceeded the 900 MiB memory guard'
    print('PROVED:',script,'PASS; %.2f seconds; cumulative peak RSS %.1f MiB'%(time.monotonic()-started,peak),flush=True)
print('PROVED: all exact certificates replay successfully. This does not close the unresolved 5+1 region.')
