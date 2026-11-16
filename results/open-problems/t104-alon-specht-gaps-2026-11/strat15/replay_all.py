"""Replay byte-identical STRAT14 and STRAT13 copies, then the new proof.

Pool sizes alone are capped at two by a pinned runtime shim. Source programs
and mathematical inputs are unchanged. All mathematical signs are exact.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,time,tempfile,shutil,subprocess,hashlib,resource
from pathlib import Path
HERE=Path(__file__).resolve().parent

def hashes_check():
    pinned=json.loads((HERE/'source_hashes.json').read_text())
    actual={str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest()for p in sorted((HERE/'STRAT14').rglob('*'))if p.is_file()}
    assert actual==pinned,'Supplied STRAT14 source changed'
    return actual

def main():
    start=time.monotonic();hashes=hashes_check();records=[]
    resume='--resume'in sys.argv;previous_elapsed=0;archive=None
    if resume:
        previous=json.loads((HERE/'replay_progress.json').read_text())
        pins=json.loads((HERE/'proof_hashes.json').read_text())
        assert hashlib.sha256((HERE/'source_hashes.json').read_bytes()).hexdigest()==pins['source_hashes.json']
        expected=['unchanged STRAT14 full replay','unchanged STRAT13 full replay',
                  'all-N premise verify_allN_ratio.py','all-N premise verify_allN_cells.py',
                  'all-N premise verify_analytic.py','all-N premise verify_summary.py']
        records=previous['checks'][:6]
        assert [r['check']for r in records]==expected and all(r['status']=='PASS'for r in records)
        for name in ('strat14_replay_summary.json','strat13_replay_summary.json'):
            receipt=json.loads((HERE/name).read_text());assert all(r['status']=='PASS'for r in receipt['checks'])
        previous_elapsed=previous['elapsed_seconds_NUMERICAL']
        number=1+len(list(HERE.glob('failed_replay_*.json')))
        archive='failed_replay_'+str(number)+'.json'
        shutil.copy2(HERE/'replay_progress.json',HERE/archive)
        shutil.copy2(HERE/'replay_all.out',HERE/('failed_replay_'+str(number)+'.out'))
    env=os.environ.copy();env['STRAT15_POOL_CAP']='2';env['PYTHONPATH']=str(HERE/'replay_runtime')
    with (HERE/'replay_all.out').open('a'if resume else 'w')as out,tempfile.TemporaryDirectory(prefix='strat15-replay-')as temp:
        root=Path(temp);clone=root/'STRAT14'
        if resume:out.write('\nRESUME: inherited PASS receipts retained after checking the unchanged source manifest.\n');out.flush()
        else:
            shutil.copytree(HERE/'STRAT14',clone)
            for name,h in hashes.items():
                p=root/name;assert hashlib.sha256(p.read_bytes()).hexdigest()==h,name
        def run(name,args,cwd):
            tick=time.monotonic();print('OPEN: replay running '+name,flush=True)
            out.write('\n'+name+'\n');out.flush()
            proc=subprocess.run([sys.executable,'-B',*args],cwd=cwd,env=env,stdout=out,stderr=subprocess.STDOUT)
            rec=dict(check=name,status='PASS'if proc.returncode==0 else 'FAIL',seconds_NUMERICAL=time.monotonic()-tick)
            records.append(rec);print(rec,flush=True);out.flush()
            (HERE/'replay_progress.json').write_text(json.dumps(dict(checks=records,elapsed_seconds_NUMERICAL=previous_elapsed+time.monotonic()-start),indent=2)+'\n')
            if proc.returncode:raise RuntimeError(name+' failed')
        if not resume:
            run('unchanged STRAT14 full replay',['replay_all.py'],clone)
            for n in ('replay_all.out','replay_summary.json'):shutil.copy2(clone/n,HERE/('strat14_'+n))
            run('unchanged STRAT13 full replay',['replay_all.py'],clone/'STRAT13')
            for n in ('replay_all.out','replay_summary.json'):shutil.copy2(clone/'STRAT13'/n,HERE/('strat13_'+n))
            for script in ('verify_allN_ratio.py','verify_allN_cells.py','verify_analytic.py','verify_summary.py'):
                run('all-N premise '+script,[script],clone/'STRAT13/STRAT12/STRAT10')
        for script in ('verify_target.py','verify_padding.py','check_spawn.py','verify_new.py'):
            run(script,[script],HERE)
    assert hashes_check()==hashes
    result=dict(label='PROVED (replay_all.py): all required exact replays passed',checks=records,
                seconds_NUMERICAL=previous_elapsed+time.monotonic()-start,source_files_unchanged=len(hashes),
                resumed=resume,previous_attempt_seconds_NUMERICAL=previous_elapsed,
                retry_seconds_NUMERICAL=time.monotonic()-start,previous_attempt_archive=archive,
                pool_cap=2,parent_peak_bytes_NUMERICAL=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                child_peak_bytes_NUMERICAL=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
    (HERE/'replay_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    with(HERE/'LOG.md').open('a')as f:f.write('\n'+result['label']+'. NUMERICAL seconds '+str(result['seconds_NUMERICAL'])+'.\n')
    print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
