"""Exact inherited and new replays. An OPEN result is not a global theorem."""
import os,sys,json,time,subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'

def main():
    inherited=['verify_provenance.py','verify_frame.py','verify_filters.py','verify_cone.py',
               'verify_corner.py','verify_examples.py','verify_rotation.py','verify_corner_faces.py','verify_overlay.py']
    jobs=[['verify_sources.py']]+[['inherited_replay.py',s] for s in inherited]
    jobs += [[s] for s in ('verify_formulation.py','verify_obstruction.py','verify_samples.py',
                           'verify_certificates.py','verify_sources.py')]
    results=[];started=time.monotonic()
    with (HERE/'replay_all.out').open('w') as out:
        for args in jobs:
            start=time.monotonic();name=' '.join(args)
            print('OPEN: running exact check',name,flush=True)
            p=subprocess.run([sys.executable,'-B',*args],cwd=HERE,stdout=out,stderr=subprocess.STDOUT)
            result=dict(check=name,status='PASS' if p.returncode==0 else 'FAIL',
                        seconds_NUMERICAL=time.monotonic()-start)
            results.append(result);out.flush();print(result['status']+': '+name,flush=True)
            if p.returncode:break
    passed=len(results)==len(jobs) and all(x['status']=='PASS' for x in results)
    summary=dict(label=('PROVED: all exact partial claims replayed; OPEN: global sign'
                        if passed else 'OPEN: exact replay failed'),
                 checks=results,elapsed_seconds_NUMERICAL=time.monotonic()-started,
                 inherited_provenance_operational_omissions=['STRAT9/codex.pid','STRAT10/codex.pid'])
    (HERE/'replay_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    with (HERE/'LOG.md').open('a') as f:
        f.write('\n'+summary['label']+'. NUMERICAL full replay elapsed '+str(summary['elapsed_seconds_NUMERICAL'])+' seconds.\n')
    if not passed:raise SystemExit(1)
    print(summary['label'],flush=True)

if __name__=='__main__':main()
