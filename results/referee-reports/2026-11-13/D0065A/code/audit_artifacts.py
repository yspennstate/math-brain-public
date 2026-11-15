"""Independent recomputation of saved summaries and artifact restrictions."""
import os
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import csv,json,math,re,hashlib,datetime
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parents[1]
meta=json.loads((R/'data/simulation_summary.json').read_text())
with (R/'data/brw_samples.csv').open() as f: records=list(csv.DictReader(f))
assert len(records)==8192
checks=[]
for s in meta['summaries']:
    a=np.array([[float(r[k]) for k in ['centered_max','signed_derivative_mass','seneta_heyde_mass_proxy']] for r in records if int(r['d'])==s['d'] and int(r['depth'])==s['n']])
    m,D,Z=a.T;alpha=math.sqrt(2*s['d'])
    assert len(m)==1024 and (Z>0).all() and np.isfinite(a).all()
    assert abs(float(np.median(m))-s['median'])<1e-12
    assert abs(float(m.mean())-s['mean'])<1e-12
    assert abs(float(m.std(ddof=1))-s['standard_deviation'])<1e-12
    assert int((D<=0).sum())==s['negative_D_count']
    # scalar-loop CDF independent of vectorized simulator evaluation.
    test=sorted(m[640:]);C=s['C_SH_proxy'];masses=Z[:256]
    F=[sum(math.exp(-C*z*math.exp(-alpha*x)) for z in masses)/len(masses) for x in test]
    ks=max(max((i+1)/len(test)-v,v-i/len(test)) for i,v in enumerate(F))
    assert abs(ks-s['validation_KS'])<1e-12
    calibration_median=float(np.median(m[256:640]))
    assert abs(sum(math.exp(-C*z*math.exp(-alpha*calibration_median)) for z in masses)/len(masses)-.5)<1e-10
    checks.append({'d':s['d'],'n':s['n'],'independent_KS':ks})
assert meta['nice']>=10 and meta['peak_rss_bytes']<4*1024**3
assert (R/'REPORT.md').read_text().splitlines()[0]=='PARTIAL'
assert not [p for p in (R/'sources').rglob('*') if p.is_file() and p.suffix!='.txt']
assert not [p for p in R.rglob('*') if p.is_file() and p.suffix.lower() in {'.pdf','.djvu','.ps','.eps'}]
# Check perturbation expansion two algebraic ways, independently of stochastic theorem.
for d in (1,2,3):
    alpha=math.sqrt(2*d);b=1.5/alpha
    for n in (10,100,1000,10000):
        delta=1.;factor=1+delta/n;u=.3
        rawmax=alpha*n-b*math.log(n)+u
        lhs=factor*rawmax-alpha*factor**2*n+b*math.log(factor**2*n)
        rhs=factor*u+alpha*n*(factor-factor**2)+b*((1-factor)*math.log(n)+2*math.log(factor))
        assert abs(lhs-rhs)<1e-10
manifest={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((R/'sources').glob('*.txt'))}
(R/'data/source_text_sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'csv_rows':len(records),'independent_summary_checks':checks,'maximum_gamma_check_absolute_error':max(c['absolute_error'] for c in meta['identity_checks']),'nice':meta['nice'],'peak_rss_bytes':meta['peak_rss_bytes'],'forbidden_document_files':0,'source_text_count':len(manifest),'perturbation_algebra_checked':True}
(R/'data/final_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
