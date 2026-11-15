"""Check saved source text integrity and independently recompute key data totals."""
import csv
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path

if os.getpriority(os.PRIO_PROCESS,0)<10:
    os.setpriority(os.PRIO_PROCESS,0,10)
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'


def read(name):
    with (DATA/name).open() as f:return list(csv.DictReader(f))


def main():
    report=(ROOT/'REPORT.md').read_text()
    assert report.splitlines()[0] in ('PROVED','COUNTEREXAMPLE','PARTIAL','NO_PROGRESS','RESOLVED_IN_LITERATURE')
    assert 'being finalized' not in report
    for p in ROOT.rglob('*'):
        if not p.is_file():continue
        assert p.suffix.lower()!='.pdf',p
        with p.open('rb') as f:assert f.read(4)!=b'%PDF',p
    entries=[]
    for p in sorted((ROOT/'sources').glob('*.metadata.txt')):
        meta=json.loads(p.read_text())
        source=p.with_name(p.name.replace('.metadata.txt','.txt'))
        content=source.read_text()
        assert hashlib.sha256(content.encode()).hexdigest()==meta['text_sha256'],p
        pages=len(content.split('\f'))-int(content.endswith('\f'))
        assert pages==meta['pages'],p
        entries.append(f"{source.name}\n  URL: {meta['url']}\n  PDF pages: {pages}\n"
                       f"  source SHA256 (retrieval): {meta['source_sha256']}\n"
                       f"  saved text SHA256 (verified): {meta['text_sha256']}\n")
    (ROOT/'sources'/'index.txt').write_text('\n'.join(entries))
    paths=read('paths.csv');params=read('parameters.csv');summaries=read('speed_summary.csv')
    assert len(params)==9
    assert len(paths)==9*24*5
    assert len(summaries)==9*5
    for p in params:
        cfg=p['config']
        # Independent decimal/Fraction check of the parameter calculation.
        if cfg.startswith('horizontal_k'):
            k=Fraction(cfg.split('_k')[1])
            expected=[3*k/8,k/8,k/8,k/8]
            observed=[Fraction(p[x]) for x in ('a_plus_x','a_plus_y','a_minus_x','a_minus_y')]
            assert all(abs(float(x-y))<1e-14 for x,y in zip(expected,observed))
            assert abs(float(k)-float(p['kappa']))<1e-14
        group=[r for r in paths if r['config']==cfg]
        assert len({r['seed'] for r in group})==24
        for rep in range(24):
            g=[r for r in group if int(r['rep'])==rep]
            assert sorted(int(r['n']) for r in g)==[1000,10000,100000,1000000,2000000]
            assert len({r['seed'] for r in g})==1
    for s in summaries:
        group=[r for r in paths if r['config']==s['config'] and r['n']==s['n']]
        xs=[int(r['x']) for r in group];N=int(s['n']);count=len(xs)
        exact_mean=Fraction(sum(xs),count*N)
        exact_variance=(sum(Fraction(x*x) for x in xs)-Fraction(sum(xs)**2,count))/(count*(count-1)*N*N)
        assert abs(float(exact_mean)-float(s['mean_vx']))<1e-15
        assert abs(math.sqrt(float(exact_variance))-float(s['se_vx']))<1e-15
    episodes=read('episodes.csv')
    for p in params:
        for rep in range(24):
            group=sorted([r for r in episodes if r['config']==p['config'] and int(r['rep'])==rep],
                         key=lambda r:int(r['threshold']))
            counts=[int(r['completed_runs_ge_threshold']) for r in group]
            assert len(counts)==8 and counts==sorted(counts,reverse=True)
    traps=read('traps.csv');assert len(traps)==9*17
    for p in params:
        group=sorted([r for r in traps if r['config']==p['config']],key=lambda r:int(r['threshold']))
        counts=[int(r['exceedances']) for r in group]
        assert counts==sorted(counts,reverse=True)
        assert all(int(r['samples'])==1000000 for r in group)
    result=dict(source_texts_verified=len(entries),independent_trajectories=9*24,
        steps_per_trajectory=2000000,total_walk_steps=9*24*2000000,
        independent_pair_samples=9*1000000,checkpoint_rows=len(paths),
        trap_tail_rows=len(traps),summary_arithmetic='integer/Fraction recomputation passed',
        no_saved_pdfs=True,nice=os.getpriority(os.PRIO_PROCESS,0))
    (DATA/'artifact_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
