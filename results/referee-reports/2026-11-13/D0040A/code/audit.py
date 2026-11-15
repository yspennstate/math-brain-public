#!/usr/bin/env python3
"""Independent algebra and saved-artifact checks for the D0040 report."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import ast, json, hashlib, re, fractions
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parents[1]
rng=np.random.default_rng(400099)
out={}
# Independent finite-dimensional checks of reversal/transposition and arrow completion.
errors=[];arrows=[];residues=[]
for _ in range(100):
    n=6
    B=np.diag(rng.uniform(0.2,3,n))+np.diag(rng.uniform(0.2,3,n-1),-1)
    R=np.eye(n)[::-1]
    C=R@B.T@R
    errors.append(float(np.max(abs(np.linalg.eigvalsh(B@B.T)-np.linalg.eigvalsh(C@C.T)))))
    H=B@B.T
    for k in range(1,n+1):
        errors.append(float(np.max(abs(H[:k,:k]-B[:k,:k]@B[:k,:k].T))))
    x=np.sort(rng.normal(size=n))
    y=x[:-1]+rng.uniform(0.1,0.9,n-1)*np.diff(x)
    P=np.poly(x);Q=np.poly(y)
    v2=-np.polyval(P,y)/np.polyval(np.polyder(Q),y)
    assert np.all(v2>0)
    A=np.zeros((n,n));A[:-1,:-1]=np.diag(y)
    A[-1,-1]=x.sum()-y.sum();A[-1,:-1]=A[:-1,-1]=np.sqrt(v2)
    arrows.append(float(np.max(abs(np.linalg.eigvalsh(A)-x))))
    q=np.array([np.prod(xi-y)/np.prod(xi-np.delete(x,i)) for i,xi in enumerate(x)])
    assert np.all(q>0)
    residues.append(abs(float(q.sum()-1)))
out.update(max_Laguerre_algebra_error=max(errors),max_arrow_spectrum_error=max(arrows),max_residue_sum_error=max(residues))
assert max(errors)<1e-11 and max(arrows)<1e-9 and max(residues)<1e-10
# Re-derive the KN mean as exact rational arithmetic, without calling the sampler.
F=fractions.Fraction
p,q=F(3,10),F(11,10);S=p+q+2;d=p-q
for beta in (F(1,2),F(1),F(2),F(4)):
    theta=beta/2
    mean_odd=(theta-S)/(theta+S)
    mean_b=(1-mean_odd)*d/S-(1+mean_odd)*d/(S+2*theta)
    transformed=(mean_b+2)/4
    closed=F(1,2)+d/(2*(S+beta))
    assert transformed==closed
    assert transformed!=(p+1)/S
out['exact_rational_KN_mean_identities']=4
# Independently recompute the Holm correction.
saved=json.loads((root/'data/checks.json').read_text())
checks=saved['positive_checks'];m=len(checks)
sortedchecks=sorted(checks,key=lambda c:c['p'])
acc=0
for i,c in enumerate(sortedchecks):
    acc=max(acc,min(1,(m-i)*c['p']))
    assert abs(acc-c['holm_p'])<1e-13
assert saved['metadata']['code_sha256']==hashlib.sha256((root/'code/check_models.py').read_bytes()).hexdigest()
assert saved['metadata']['niceness']>=10
assert saved['metadata']['peak_rss_bytes']<4*1024**3
assert saved['metadata']['holm_rejections_005']==0
out['verified_positive_check_count']=m
out['Holm_correction_recomputed']=True
out['simulation_code_hash_matches_saved_data']=True
# Every retained sample array has the stated count and ordered spectra.
with np.load(root/'data/samples.npz') as samples:
    for key in samples.files:
        x=samples[key]
        assert len(x)==saved['metadata']['samples_per_case']
        assert np.all(np.isfinite(x))
        if x.ndim==2:assert np.all(np.diff(x,axis=1)>=0)
    out['sample_arrays_checked']=len(samples.files)
# Source page markers and metadata; no retained PDF magic or prohibited paper-image extension.
src=[]
for path in sorted((root/'sources').glob('*')):
    assert path.suffix=='.txt'
    text=path.read_text()
    if path.name in ('INDEX.txt','SEARCH_LOG.txt'):continue
    count=int(re.search(r'PDF PAGES: (\d+)',text).group(1))
    pages=list(map(int,re.findall(r'===== PDF PAGE (\d+) =====',text)))
    assert pages==list(range(1,count+1))
    src.append(dict(file=path.name,pages=count,text_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
for path in root.rglob('*'):
    if path.is_file():
        with path.open('rb') as f:assert f.read(5)!=b'%PDF-'
        assert path.suffix.lower() not in ('.pdf','.png','.jpg','.jpeg','.tiff','.webp')
report=(root/'REPORT.md').read_text()
assert report.splitlines()[0]=='PARTIAL'
for link in re.findall(r'\]\(([^)]+)\)',report):
    if '://' not in link:assert (root/link).exists(),link
for path in (root/'code').glob('*.py'):ast.parse(path.read_text())
out.update(sources=src,no_PDF_or_paper_images=True,report_local_links_exist=True,python_sources_parse=True)
(root/'data/audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='sources'},indent=2))
