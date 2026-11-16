"""Replay every new PROVED claim sequentially, with exact arithmetic only."""
import os,sys,json,time,subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent
os.chdir(HERE)
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
SCRIPTS=['verify_provenance.py','verify_frame.py','verify_filters.py','verify_cone.py','verify_corner.py',
         'verify_examples.py','verify_rotation.py','verify_corner_faces.py','verify_overlay.py']

def main():
    results=[]
    with (HERE/'replay_all.out').open('w') as out:
        for script in SCRIPTS:
            start=time.monotonic()
            p=subprocess.run([sys.executable,'-B',script],capture_output=True,text=True)
            out.write(p.stdout+p.stderr);out.flush()
            result=dict(script=script,status='PASS' if p.returncode==0 else 'FAIL',
                        seconds=time.monotonic()-start,timing_label='NUMERICAL')
            results.append(result);print(result['status']+': '+script,flush=True)
            if p.returncode:
                print(p.stdout+p.stderr,flush=True)
                break
    failed=any(r['status']=='FAIL' for r in results) or len(results)!=len(SCRIPTS)
    summary=dict(label='OPEN: full region sign; '+('failed replay' if failed else 'PROVED: all new exact claims replayed'),checks=results)
    (HERE/'replay_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    if failed:raise SystemExit(1)
    print('PROVED: every new certificate replayed. OPEN: complement sign; see cover_summary.json.',flush=True)

if __name__=='__main__':main()
