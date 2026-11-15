#!/usr/bin/env python3
"""Check saved source provenance and the page anchors used in the report."""
import hashlib, json, os
from pathlib import Path
root=Path(__file__).resolve().parent.parent
records=[json.loads(line) for line in (root/'data/source_manifest.jsonl').read_text().splitlines()]
checks=[]
for r in records:
    p=root/'sources'/r['text_file']; b=p.read_bytes(); t=b.decode('utf-8')
    assert hashlib.sha256(b).hexdigest()==r['text_sha256'],p
    assert t.count('\f')==r['pages_formfeed'],p
    checks.append({'file':r['text_file'],'sha256_ok':True,'text_pages':r['pages_formfeed']})
anchors={
 'chatterjee_2008.txt':[(2,'Theorem 1.1.'),(6,'Definition 1.5.'),(12,'Theorem 3.2.'),(13,'Var(f (Y))'),(38,'Theorem 8.1.'),(59,'(2) Prove chaos')],
 'graham_2009.txt':[(14,'Theorem 6.1.')],
 'alexander_zygouras_2013.txt':[(2,'Theorem 1.1.')],
 'alexander_zygouras_published_2013.txt':[(2,'Theorem 1.1.')],
 'chatterjee_surface_2022.txt':[(9,'Theorem 2.4.')],
 'bates_chatterjee_endpoint_2020.txt':[(16,'Theorem 1.1.'),(17,'Theorem 1.2.')],
 'bates_chatterjee_localization_2020.txt':[(10,'Theorem 1.7.')],
 'bates_full_path_2021.txt':[(5,'Theorem 1.3.')],
 'ganguly_hammond_chaos_2024.txt':[(9,'Theorem 1.3.')],
 'junk_lacoin_2024.txt':[(4,'Theorem 2.2.')],
}
anchor_results=[]
for file, entries in anchors.items():
    pages=(root/'sources'/file).read_text().split('\f')
    for page, needle in entries:
        assert needle in pages[page-1],(file,page,needle)
        anchor_results.append({'file':file,'page_1_based':page,'anchor':needle})
for p in (root/'sources').iterdir():
    assert p.suffix=='.txt' and p.is_file(),p
for p in root.rglob('*'):
    if p.is_file():
        assert p.suffix.lower() not in {'.pdf','.png','.jpg','.jpeg','.tif','.tiff','.webp','.gif','.bmp'},p
        with p.open('rb') as f: prefix=f.read(8)
        assert not prefix.startswith((b'%PDF',b'\x89PNG',b'\xff\xd8\xff')),p
report=(root/'REPORT.md').read_text()
assert report.splitlines()[0]=='RESOLVED_IN_LITERATURE'
result={'source_checks':checks,'page_anchor_checks':anchor_results,
        'report_status':'RESOLVED_IN_LITERATURE','pdf_or_image_files':0,
        'inherited_nice':os.getpriority(os.PRIO_PROCESS,0)}
(root/'data/audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'sources_verified':len(checks),'page_anchors_verified':len(anchor_results),
                  'pdf_or_image_files':0,'inherited_nice':result['inherited_nice']}))
