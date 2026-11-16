"""PROVED: sequential replay of every retained exact certificate.
OPEN: successful replay does not prove the full remaining continuous region.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import contextlib,resource,runpy,sys,time,json
from pathlib import Path
sys.dont_write_bytecode=True
root=Path(__file__).resolve().parent;os.chdir(root)
SCRIPTS=['verify_provenance.py','verify_elementary.py','prior_four.py','prior_triangles.py','verify_boundary.py','verify_moments.py','verify_polya_moments.py','prior_scale.py','verify_algebra.py','verify_cell_identities.py','verify_small_ratio.py','verify_cells.py','verify_allN_cells.py','verify_allN_ratio.py','zero_face.py','verify_boxes.py','residual_witness.py','verify_coverage.py','verify_domain.py','axis_bernstein.py','verify_cubic_moment.py','verify_cubic_sos.py','verify_cubic_identities.py','verify_analytic.py','verify_extensions.py','verify_samples.py','verify_new_boxes.py','verify_family.py','verify_baseline.py','verify_cover.py','verify_new_residual.py','verify_summary.py']

def main():
    records=[];start_all=time.monotonic();failures=[]
    for script in SCRIPTS:
        start=time.monotonic();status='PASS';failure=None
        try:
            with open(script.replace('.py','.out'),'w')as output,contextlib.redirect_stdout(output):runpy.run_path(script,run_name='__main__')
            peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024 if sys.platform=='darwin'else 1024)
            assert peak<1024,'Exact replay exceeded 1 GiB RSS guard'
        except Exception as error:
            import traceback
            status='FAIL';failure=type(error).__name__+': '+str(error);failures.append(dict(script=script,error=failure))
            with open(script.replace('.py','.out'),'a')as output:traceback.print_exc(file=output)
            peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024 if sys.platform=='darwin'else 1024)
        rec=dict(script=script,status=status,seconds=time.monotonic()-start,peak_RSS_MiB=peak,resource_label='NUMERICAL')
        if failure:rec['error']=failure
        records.append(rec)
        msg=f'{status}: {script}. NUMERICAL: {rec["seconds"]:.3f} seconds, peak RSS {peak:.2f} MiB.'
        if failure:msg+=' OPEN: '+failure
        print(msg,flush=True)
        with open('LOG.md','a')as f:f.write('\n'+('PROVED: 'if status=='PASS'else 'OPEN: ')+msg+'\n')
    result=dict(label='PROVED exact certificate replay; OPEN full remaining sign'if not failures else 'OPEN replay failures',checks=records,failures=failures,total_seconds=time.monotonic()-start_all,resource_measurements='NUMERICAL')
    Path('replay_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    if failures:
        print('FAIL: '+str(len(failures))+' scripts; see replay_summary.json.',flush=True);sys.exit(1)
    print('PASS: all retained exact certificates replayed sequentially. OPEN: full residual sign remains unproved.',flush=True)
if __name__=='__main__':main()
