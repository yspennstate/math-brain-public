"""Check final artifact integrity and independently recheck key numerical summaries."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
import csv,hashlib,json,resource
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
assert os.getpriority(os.PRIO_PROCESS,0)>=10
report=(ROOT/'REPORT.md').read_text()
assert report.splitlines()[0]=='COUNTEREXAMPLE'
assert not any(ord(c)<32 and c not in '\n\t' for c in report)
assert '**Conjecture 5.** After scaling, T_n converges to the random operator' in report
assert r'\beta' in report
assert 'Theorem 4' in report and 'arXiv:2304.09236v2' in report
manifest=json.loads((ROOT/'sources/manifest.json').read_text())
for name,entry in manifest.items():
    text=(ROOT/'sources'/f'{name}.txt').read_bytes()
    assert hashlib.sha256(text).hexdigest()==entry['text_sha256'],name
    text.decode('utf-8')
    assert text.count(b'\f')==entry['pages']
for path in ROOT.rglob('*'):
    if path.is_file():
        assert path.suffix.lower()!='.pdf',str(path)
        with path.open('rb') as f: assert f.read(5)!=b'%PDF-',str(path)
for path in (ROOT/'sources').iterdir():
    if path.is_file():path.read_text(encoding='utf-8')
expected={'artificial_eigenvalues.csv':1152,'quartic_eigenvalues.csv':2880,
          'quartic_banded_eigenvalues.csv':7200,'rayleigh_tail.csv':117,
          'finite_unitary_cdf.csv':45}
for file,count in expected.items():
    rows=list(csv.DictReader((ROOT/'data'/file).open()))
    assert len(rows)==count,(file,len(rows))
    for row in rows:
        for key,value in row.items():
            if key not in ['model']:assert np.isfinite(float(value)),(file,key,value)
diag=json.loads((ROOT/'data/quartic_banded_diagnostics.json').read_text())
assert len(diag)==9
for row in diag:
    assert row['diagnostics']['split_rhat']<1.05
    for chain in row['chains']:
        assert chain['divergences']==0 and chain['hessian_shift']==0
raw=list(csv.DictReader((ROOT/'data/quartic_banded_eigenvalues.csv').open()))
for row in diag:
    vals=[float(r['cv_scaled_top0']) for r in raw if int(r['n'])==row['n'] and int(r['beta'])==row['beta']]
    assert abs(np.mean(vals)-row['mean_cv'])<1e-12
samples=list((ROOT/'data').glob('quartic_banded_sample_*.npz'))
assert len(samples)==18
for file in samples:
    sample=np.load(file);assert len(sample['a'])==len(sample['b'])+1
    assert (sample['b']>0).all() and np.isfinite(sample['a']).all()
tail=list(csv.DictReader((ROOT/'data/rayleigh_tail.csv').open()))
tail_powers=[]
for k in [0,1,2]:
    rows=[r for r in tail if int(r['k'])==k and int(r['beta'])==2]
    slope=np.log(float(rows[-1]['log_probability'])/float(rows[-2]['log_probability']))/np.log(2)
    target=(4*k+3)/(4*k+2)
    assert abs(slope-target)<.01
    tail_powers.append(dict(k=k,measured_loglog_slope=float(slope),formula=target))
out=dict(status='pass',source_texts_verified=len(manifest),csv_rows=expected,
         sampled_matrices_verified=len(samples),no_pdfs=True,no_report_control_characters=True,
         tail_power_checks=tail_powers,nice=os.getpriority(os.PRIO_PROCESS,0),
         maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         proof_audit='Manual: equilibrium transform, Gaussian variance scaling, and portmanteau argument checked independently; matches Baslingker Theorem 4 and eq.(22).')
(ROOT/'data/audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
