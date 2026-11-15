#!/usr/bin/env python3
"""Verify text archives and record source page locations for the C0149 audit."""
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = [json.loads(line) for line in (ROOT/'data/source_manifest.jsonl').read_text().splitlines()]
checks = []
for item in manifest:
    matches = [p for p in (ROOT/'sources').glob('*.txt')
               if hashlib.sha256(p.read_bytes()).hexdigest() == item['text_sha256']]
    assert len(matches) == 1, (item['url'], matches)
    checks.append({'source': matches[0].name, 'sha256_verified': True,
                   'pages': item['pages_formfeed']})

report = (ROOT/'REPORT.md').read_text()
assert report.splitlines()[0] == 'RESOLVED_IN_LITERATURE'
assert '2(1+2d/\\gamma)' in report

locations = {
 'pete_pgg_current.txt': ['Conjecture 14.4 (Lewis Bowen)', 'Definition 7.8.', 'Theorem 14.8'],
 'kun_1606.04471v5.txt': ['Theorem 1.', 'Theorem 3.', 'Lemma 10.', 'Proposition 11.', 'Lemma 14.'],
 'oberwolfach_2016_41.txt': ['Theorem 1. Let Γ be a countably infinite Property (T)', 'Lewis Bowen,'],
 'aldous_lyons_2007.txt': ['Theorem 3.2. (Invariance and Unimodularity)'],
 'alekseev_finn_sell_1608.02242.txt': ['Theorem 7.4'],
 'bowen_1704.06349.txt': ['recently proved every sofic approximation'],
 'drigalla_2511.16515.txt': ['Corollary 5.4.', 'Theorem 6.3.'],
 'alekseev_thom_2512.15494.txt': ['Definition 6.1.'],
}
page_map = {}
for name, terms in locations.items():
    pages = (ROOT/'sources'/name).read_text().split('\f')
    page_map[name] = {term: [i+1 for i, page in enumerate(pages) if term in page] for term in terms}
    assert all(page_map[name].values()), name
(ROOT/'data/source_locations.json').write_text(json.dumps(page_map, indent=2, ensure_ascii=False)+'\n')

for path in (ROOT/'sources').iterdir():
    assert path.suffix == '.txt', path
    path.read_text(encoding='utf-8')
prohibited = {'.pdf','.png','.jpg','.jpeg','.webp','.gif','.tif','.tiff','.bmp','.heic'}
for path in ROOT.rglob('*'):
    if path.is_file():
        assert path.suffix.lower() not in prohibited, path
        with path.open('rb') as file:
            assert not file.read(5).startswith(b'%PDF'), path

chapter = (ROOT/'sources/pete_chapter14.txt').read_text()
assert chapter.count('===== PDF page ') == 21
result = {'archive_count': len(checks), 'archives': checks,
          'chapter14_pages': [195,215], 'chapter14_page_count': 21,
          'report_status': report.splitlines()[0], 'no_pdf_or_image_files': True,
          'source_files_plain_utf8': True, 'process_nice': os.getpriority(os.PRIO_PROCESS,0),
          'numerical_experiments': 'not run: literature stopping rule'}
(ROOT/'data/audit.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='archives'},indent=2))
