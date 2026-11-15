"""Check saved source provenance, file types, report locators, and sample counts."""
from pathlib import Path
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
latest={}
for line in (root/'sources'/'manifest.jsonl').read_text().splitlines():
    record=json.loads(line)
    latest[record['name']]=record
output=[]
for p in sorted((root/'sources').glob('*.txt')):
    body=p.read_bytes()
    text=body.decode('utf-8')
    record=latest.get(p.stem,{})
    digest=hashlib.sha256(body).hexdigest()
    paper=bool(text.strip()) and not text.startswith('RETRIEVAL') and p.stem not in ['RETRIEVAL_NOTES']
    if paper:
        assert digest==record['text_sha256'],p.name
        assert '<html' not in text[:1000].lower()
    output.append({'file':str(p.relative_to(root)),'paper_text':paper,
                   'pages':text.count('\f'),'sha256':digest,
                   'url':record.get('url'),'version':re.findall(r'arXiv:\S+',text[:3000])})
locators={
 'diaconis_2013':['Question 2.'],
 'alon_roichman':['Theorem 1:','Corollary 1:'],
 'landau_russell':['Theorem 2.'],
 'hough_published':['Theorem 1.1.','Theorem 1.6.','Theorem 1.7.'],
 'hermon_olesker_cutoff_published':['Theorem A.','Theorem D.','Theorem 7.1 (','Theorem 7.2.'],
 'hermon_olesker_triangular':['Theorem 3.3 (Cutoff).'],
 'zhu_2026':['Theorem 1.2.','Theorem 1.4.'],
}
found={}
for name,needles in locators.items():
    pages=(root/'sources'/(name+'.txt')).read_text().split('\f')
    found[name]={needle:next(i+1 for i,p in enumerate(pages) if needle in p) for needle in needles}
for p in root.rglob('*'):
    if p.is_file():
        with p.open('rb') as f:head=f.read(16)
        assert not head.startswith(b'%PDF'),p
        assert p.suffix.lower() not in ['.pdf','.png','.jpg','.jpeg','.tiff','.tif','.webp','.gif','.ps','.dvi'],p
report=(root/'REPORT.md').read_text()
assert report.splitlines()[0]=='PARTIAL'
assert report.count('$$')%2==0
assert not any(ord(c)<32 and c not in '\n\t' for c in report)
assert 'verify locator' not in report and '1295–1305' not in report
rows=[json.loads(l) for l in (root/'data'/'samples.jsonl').read_text().splitlines()]
assert len(rows)==288 and len({r['group'] for r in rows})==24
assert max(r['order'] for r in rows)==40320
assert all(len(set(tuple(g) for g in r['generators']))==r['k'] for r in rows)
(root/'data'/'artifact_audit.json').write_text(json.dumps(
    {'sources':output,'first_matching_pdf_pages':found,'sample_records':len(rows),
     'accepted_sets':len(rows)//2,'groups':24,'no_pdf_or_page_images':True,
     'report_sha256':hashlib.sha256(report.encode()).hexdigest()},indent=2)+'\n')
print('Artifact audit passed:',len(output),'text files;',len(rows),'walk records; no PDFs or images.')
