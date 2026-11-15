#!/usr/bin/env python3
"""Audit retained source hashes and recompute search values from Fourier SVD."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
if os.getpriority(os.PRIO_PROCESS,0) < 10:
    os.nice(10-os.getpriority(os.PRIO_PROCESS,0))
import hashlib
import json
from pathlib import Path
import re
import resource
import numpy as np

root = Path(__file__).resolve().parents[1]
assert Path.cwd().resolve() == root
source_count = 0
for line in (root/'data/source_manifest.jsonl').read_text().splitlines():
    record = json.loads(line)
    assert 'error' not in record, record
    filename = record.get('name') or (record['id']+'.txt')
    body = (root/'sources'/filename).read_bytes()
    assert hashlib.sha256(body).hexdigest() == record['text_sha256'], filename
    assert not body.startswith(b'%PDF'), filename
    body.decode('utf-8')
    source_count += 1

index=[]
for path in sorted((root/'sources').glob('*_metadata.txt')):
    text=path.read_text()
    identifier=path.name.removesuffix('_metadata.txt')
    title=re.search(r'<meta name="citation_title" content="([^"]*)',text).group(1)
    authors=re.findall(r'<meta name="citation_author" content="([^"]*)',text)
    versions=re.findall(r'\[v(\d+)\]',text)
    pages=(root/'sources'/(identifier+'.txt')).read_text().split('\f')
    index.append(dict(file=identifier+'.txt',title=title,authors=authors,
                      versions=sorted(set(versions),key=int),
                      pdf_pages=len(pages)-1))
(root/'data/source_index.json').write_text(json.dumps(index,indent=2,ensure_ascii=False)+'\n')

results=[]
for record in json.loads((root/'data/search_results.json').read_text()):
    p=record['p']
    chi=-np.ones(p,dtype=int)
    chi[0]=0
    chi[(np.arange(1,p,dtype=np.int64)**2)%p]=1
    residues=np.flatnonzero(chi==1)
    indices=record['indices']
    phi=np.zeros(((p+1)//2,len(indices)),dtype=complex)
    for j,index in enumerate(indices):
        if index==p:
            phi[0,j]=1
        else:
            phi[0,j]=1/np.sqrt(p)
            phi[1:,j]=np.sqrt(2/p)*np.exp(-2j*np.pi*residues*index/p)
    singular=np.linalg.svd(phi,compute_uv=False)
    recovered=dict(lambda_min=float(singular[-1]**2),
                   lambda_max=float(singular[0]**2),
                   condition=float(singular[0]/singular[-1]))
    errors={key:abs(recovered[key]-record[key]) for key in recovered}
    assert max(errors.values())<1e-10
    results.append(dict(p=p,k=record['k'],errors=errors))

report=(root/'REPORT.md').read_text()
assert report.splitlines()[0]=='PARTIAL'
for opening,closing in [(r'\(',r'\)'),(r'\[',r'\]')]:
    assert report.count(opening)==report.count(closing),(opening,report.count(opening),report.count(closing))
for path in (root/'code').glob('*.py'):
    compile(path.read_text(),str(path),'exec')
for path in root.rglob('*'):
    if path.is_file():
        assert path.suffix.lower() not in {'.pdf','.png','.jpg','.jpeg','.tif','.tiff','.webp','.gif'},path
        with path.open('rb') as infile:
            assert not infile.read(8).startswith(b'%PDF'),path

checks=dict(all_passed=True,source_hashes_verified=source_count,
            fourier_svd_witness_checks=results,
            maximum_svd_disagreement=max(max(x['errors'].values()) for x in results),
            no_pdf_or_page_image_files=True,report_math_delimiters_balanced=True,
            nice=os.getpriority(os.PRIO_PROCESS,0),
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
(root/'data/audit.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
