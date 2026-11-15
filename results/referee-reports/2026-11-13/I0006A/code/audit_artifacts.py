#!/usr/bin/env python3
"""Verify cited pages and create a plain-text-source manifest."""
import datetime
import hashlib
import json
import re
from pathlib import Path

checks={
 '2609.02820v1.txt':[(13,'Lemma 3.1'),(14,'Theorem 3.4')],
 '2609.02829v1.txt':[(6,'(b) The order of the mean'),(15,'Theorem 2.2 ('),(51,'Theorem 6.1 ('),(52,'Corollary 6.2.'),(53,'Proposition 6.3 ('),(53,'Lemma 6.4.'),(54,'Lemma 6.5.'),(55,'Theorem 6.6 ('),(55,'(94)'),(56,'If ζ(0) is bounded below'),(58,'Proposition 6.11.'),(64,'(129)'),(65,'(131)')],
 '2604.13968v1.txt':[(11,'Theorem 3.2 (')],
 '1501.07258v2.txt':[(2,'Theorem 1.1.'),(4,'Theorem 1.2.'),(4,'Proposition 1.3.'),(21,'Lemma 7.1.')],
 '1604.03754.txt':[(3,'Theorem 1 ('),(4,'Theorem 2 (')],
 '1610.09863.txt':[(4,'Theorem 2 ('),(5,'Theorem 3 ('),(6,'Theorem 5.')],
 '0704.0688.txt':[(12,'Theorem 3.3.')],
 '1509.08903.txt':[(2,'Theorem 1. Let'),(17,'4.1 Proofs of basic properties of membrane model')],
 '1710.10529.txt':[(2,'Theorem 1.1.'),(6,'Theorem 2.1.'),(8,'Open Question 1.'),(9,'Open Question 2.')],
 '2104.12797.txt':[(5,'Theorem 1.3.')],
}
manifest=[]; count=0
for file in sorted(Path('sources').iterdir()):
 assert file.suffix=='.txt',file
 raw=file.read_bytes(); assert not raw.startswith(b'%PDF'),file
 text=raw.decode('utf-8'); pages=text.split('\f')
 for page,phrase in checks.get(file.name,[]):
  assert phrase in pages[page-1],(file.name,page,phrase)
  count+=1
 match=re.search(r'arXiv:([0-9.]+v\d+)',text)
 item={'path':str(file),'bytes':len(raw),'sha256_text':hashlib.sha256(raw).hexdigest()}
 if match:
  item.update({'version':match[1],'pdf_url':'https://arxiv.org/pdf/'+match[1],'pages':text.count('\f')})
 manifest.append(item)
report=Path('REPORT.md').read_text()
assert report.splitlines()[0]=='RESOLVED_IN_LITERATURE'
assert 'p. 17.' not in report
for p in Path('.').rglob('*'):
 if p.is_file():
  assert p.suffix.lower() not in ('.pdf','.png','.jpg','.jpeg','.webp','.gif','.tif','.tiff'),p
Path('data/source-manifest.json').write_text(json.dumps({'audit_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cited_page_checks':count,'sources':manifest},indent=2,ensure_ascii=False)+'\n')
print(f'Passed: {count} cited-page checks; {len(manifest)} plain-text source files; report status valid; no PDFs or page-image files.')
