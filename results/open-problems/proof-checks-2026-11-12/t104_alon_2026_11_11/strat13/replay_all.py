"""Replay STRAT12 and STRAT13, plus every original cover leaf and its premises.

Inherited programs run in a temporary byte-identical copy. Their operational
outputs may change there; the supplied STRAT10--12 trees remain untouched.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[k]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,time,subprocess,tempfile,shutil,hashlib,resource
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'STRAT12'

def source_hashes():
    return {str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(SOURCE.rglob('*'))if p.is_file()}

# These are the premises actually used by cover_face.necessary/prove_box.
# The optional pressure-family, numerical samples, and all-N-only extensions
# are not needed to close the canonical N=6 face root.
COVER_PREMISES=['verify_provenance.py','verify_elementary.py','verify_moments.py',
               'verify_polya_moments.py','prior_scale.py','verify_algebra.py',
               'verify_cell_identities.py','verify_cells.py','zero_face.py',
               'verify_domain.py','axis_bernstein.py','verify_cubic_moment.py',
               'verify_cubic_sos.py','verify_cubic_identities.py','verify_extensions.py',
               'verify_cover.py']

def main():
    started=time.monotonic();records=[]
    hashes=json.loads((HERE/'source_hashes.json').read_text())
    assert source_hashes()==hashes
    # The original cover independently replayed below is precisely the cover
    # STRAT11 overlaid, including every mathematical helper it imports.
    a=SOURCE/'STRAT10';b=SOURCE/'STRAT11/STRAT10'
    for p in a.iterdir():
        if p.is_file() and (b/p.name).exists():assert p.read_bytes()==(b/p.name).read_bytes(),p.name
    with (HERE/'replay_all.out').open('w')as out, tempfile.TemporaryDirectory(prefix='strat13-replay-')as temp:
        clone=Path(temp)/'STRAT12';shutil.copytree(SOURCE,clone)
        def run(name,args,cwd):
            start=time.monotonic();print('OPEN: exact replay running',name,flush=True)
            out.write('\n'+name+'\n');out.flush()
            p=subprocess.run([sys.executable,'-B',*args],cwd=cwd,stdout=out,stderr=subprocess.STDOUT)
            rec=dict(check=name,status='PASS'if p.returncode==0 else 'FAIL',seconds_NUMERICAL=time.monotonic()-start)
            records.append(rec);out.flush();print(rec['status']+': '+name,flush=True)
            if p.returncode:raise RuntimeError('Exact replay failed: '+name)
        run('STRAT12 full replay',['replay_all.py'],clone)
        # Preserve detailed inherited output before its temporary copy is removed.
        for name in ('replay_all.out','replay_summary.json','verification_summary.json'):
            shutil.copy2(clone/name,HERE/('strat12_'+name))
        for script in COVER_PREMISES:run('original-cover premise '+script,[script],clone/'STRAT10')
        # The full-cover replay must have strictly positive margins, as opposed
        # to merely nonnegative Bernstein margins.
        old=json.loads((clone/'STRAT10/global_cover.json').read_text())
        from fractions import Fraction as F
        assert all(F(n['lower'])>0 for n in old['nodes']if n['kind']=='positive')
        summary=json.loads((clone/'STRAT10/cover_verification.json').read_text())
        assert summary['counts']==old['counts']
        shutil.copy2(clone/'STRAT10/cover_verification.json',HERE/'original_cover_verification.json')
        run('STRAT13 local theorems and collar partition',['verify_collars.py'],HERE)
    assert source_hashes()==hashes
    result=dict(label='PROVED (replay_all.py): region (11), N=6, closed; zero OPEN leaves',
                checks=records,elapsed_seconds_NUMERICAL=time.monotonic()-started,
                inherited_files_unchanged=len(hashes),
                parent_peak_rss_bytes_NUMERICAL=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    (HERE/'replay_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    with (HERE/'LOG.md').open('a')as f:f.write('\n'+result['label']+'. NUMERICAL total replay elapsed '+str(result['elapsed_seconds_NUMERICAL'])+' seconds. All inherited fingerprints unchanged.\n')
    print(result['label'],flush=True)

if __name__=='__main__':main()
