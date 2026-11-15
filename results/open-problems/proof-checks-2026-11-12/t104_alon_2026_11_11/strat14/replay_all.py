"""Replay STRAT8 in a byte-identical temporary copy, then STRAT14 and priors.

Only exact arithmetic decides mathematical signs. Runtime and RSS are metadata.
All subprocesses run sequentially; the new partition uses two exact workers.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,time,subprocess,tempfile,shutil,hashlib,resource
from pathlib import Path

HERE=Path(__file__).resolve().parent

def check_hashes(path):
    hashes=json.loads(path.read_text())
    for name,value in hashes.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==value,name
    return len(hashes)

def main():
    started=time.monotonic();checks=[]
    source_count=check_hashes(HERE/'source_hashes.json')
    prior_count=check_hashes(HERE/'prior_hashes.json')
    proof_count=check_hashes(HERE/'proof_hashes.json')
    with (HERE/'replay_all.out').open('w')as out,tempfile.TemporaryDirectory(prefix='strat14-replay-')as temp:
        root=Path(temp)
        def run(name,args,cwd):
            start=time.monotonic();print('OPEN: exact replay running:',name,flush=True)
            out.write('\n'+name+'\n');out.flush()
            p=subprocess.run([sys.executable,'-B',*args],cwd=cwd,stdout=out,stderr=subprocess.STDOUT)
            record=dict(check=name,status='PASS'if p.returncode==0 else 'FAIL',seconds_NUMERICAL=time.monotonic()-start)
            checks.append(record);out.flush();print(record,flush=True)
            if p.returncode:raise RuntimeError('Exact replay failed: '+name)
        source=HERE/'STRAT8';clone=root/'STRAT8';shutil.copytree(source,clone)
        for p in source.rglob('*'):
            if p.is_file():assert p.read_bytes()==(clone/p.relative_to(source)).read_bytes()
        run('unchanged STRAT8 replay',['replay_all.py'],clone)
        for name in ('verification.json','cover_verification.json'):
            shutil.copy2(clone/name,HERE/('strat8_'+name))
        for script in ('verify_targets.py','verify_local.py','verify_limits.py','verify_radial.py','verify_disconnected.py','verify_jets.py','verify_partition.py'):
            run(script,[script],HERE)
        # These extra replays support the full five-vertex theorem, including
        # the scale and ratio premises used by the STRAT8 exclusions.
        shutil.copytree(HERE/'prior',root/'prior')
        stages=[('STRAT4',['exact_audit.py']),('STRAT4',['isolated_certificate.py']),
                ('STRAT4',['rank_one_certificate.py']),('STRAT4',['recheck_matrices.py']),
                ('STRAT5',['verify_moments.py']),
                ('STRAT5',['verify_quartic_certificate.py','quartic_ratio_matrices_3_25.json']),
                ('STRAT5',['weight_moment_audit.py']),('STRAT5',['verify_cells.py']),
                ('STRAT6',['replay_all.py'])]
        for folder,args in stages:run('prior '+folder+' '+args[0],args,root/'prior'/folder)
    assert check_hashes(HERE/'source_hashes.json')==source_count
    assert check_hashes(HERE/'prior_hashes.json')==prior_count
    assert check_hashes(HERE/'proof_hashes.json')==proof_count
    partition=json.loads((HERE/'partition_verification.json').read_text())
    assert partition['open_leaves']==0,'Unresolved leaves; global theorem remains OPEN'
    parent=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    child=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    conservative=parent+max(child,partition['conservative_peak_bytes_NUMERICAL'])+128000000
    assert conservative<2500000000
    result=dict(label='PROVED (replay_all.py): connected five-vertex D=2 residual closed; zero OPEN leaves',
                checks=checks,seconds_NUMERICAL=time.monotonic()-started,
                source_files_unchanged=source_count,prior_files_unchanged=prior_count,
                parent_peak_bytes_NUMERICAL=parent,child_peak_bytes_NUMERICAL=child,
                conservative_peak_bytes_NUMERICAL=conservative,
                combined_partition=partition['combined_counts'],chart_volume='1152')
    (HERE/'replay_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    with (HERE/'LOG.md').open('a')as f:f.write('\n'+result['label']+'. NUMERICAL total seconds '+str(result['seconds_NUMERICAL'])+'; conservative process-memory bound '+str(conservative)+' bytes. All source fingerprints unchanged.\n')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
