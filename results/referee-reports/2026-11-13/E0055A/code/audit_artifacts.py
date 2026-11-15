#!/usr/bin/env python3
"""Check report status, source formats, provenance consistency, and page markers."""
import hashlib, json, re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
report=(root/'REPORT.md').read_text()
assert report.splitlines()[0]=='PARTIAL'
assert (root/'LOG.md').is_file()
assert (root/'data/literature_search.txt').is_file()
provenance=[]
for p in sorted((root/'data').glob('*_provenance.json')):
    meta=json.loads(p.read_text())
    source=root/'sources'/f"{meta['name']}.txt"
    text=source.read_text()
    pages=[int(x) for x in re.findall(r'===== PDF PAGE (\d+) =====',text)]
    assert pages==list(range(1,meta['pdf_pages']+1)), source
    assert meta['pdf_sha256'] in text and meta['url'] in text
    provenance.append({'source':str(source.relative_to(root)),'pages':len(pages),'pdf_sha256':meta['pdf_sha256']})
for key,original in [('bandeira_eth_key_pages','bandeira_eth'),('zhong_boumal_key_pages','zhong_boumal_arxiv_v1'),('gao_zhang_key_pages','gao_zhang_journal')]:
    txt=(root/'sources'/f'{key}.txt').read_text()
    meta=json.loads((root/'data'/f'{original}_provenance.json').read_text())
    assert meta['pdf_sha256'] in txt
for p in (root/'sources').iterdir():
    assert p.is_file() and p.suffix=='.txt',p
    p.read_text(encoding='utf-8')
for p in root.rglob('*'):
    if not p.is_file(): continue
    assert p.suffix.lower() not in {'.pdf','.png','.jpg','.jpeg','.webp','.gif','.tif','.tiff','.bmp'},p
    with p.open('rb') as f: magic=f.read(8)
    assert not magic.startswith((b'%PDF',b'\x89PNG',b'\xff\xd8\xff',b'GIF87a',b'GIF89a')),p
summary={
 'status':'PARTIAL','full_source_count':len(provenance),'full_sources':provenance,
 'independent_extraction_hash_matches':3,
 'source_files_plain_text_only':True,'no_pdf_or_image_artifacts':True,
 'simulation_performed':False,'reason':'User stage-1 stopping rule: published parameter-range/initialization result found.',
 'main_theorem_checks':{'edition':'arXiv:1703.06605v1','algorithm_page':3,'theorems_6_and_7_page':12,'noise_assumptions_page':11,'rate':'2^(2-t) sqrt(n)','noise_bound':'sigma <= c0 sqrt(n/log n)','initialization':'leading eigenvector with norm sqrt(n)'},
 'artifact_hashes':{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in ['REPORT.md','data/literature_search.txt']}
}
(root/'data/audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({'status':'passed','full_sources':len(provenance),'independent_extracts':3,'forbidden_artifacts':0}))
