"""Check final report/data consistency, source hashes, and artifact restrictions."""
import hashlib, json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
report = (root/'REPORT.md').read_text()
assert report.splitlines()[0] == 'PARTIAL'
assert not any(ord(c)<32 and c not in '\n\r\t' for c in report)
assert all(line.count('$') % 2 == 0 for line in report.splitlines())
data = json.loads((root/'data'/'enumeration.json').read_text())
verification = json.loads((root/'data'/'verification.json').read_text())
assert verification['all_passed']
assert data['niceness'] >= 10 and data['threads'] == 1
assert data['max_rss_bytes'] < 4*1024**3
table = []
for line in report.splitlines():
    cells = [x.strip() for x in line.split('|')]
    if len(cells) == 7 and re.fullmatch(r'\d+', cells[3]):
        table.append(tuple(int(x.replace(',','')) for x in cells[3:6]))
expected = [(x['common_n'],x['G_count'],x['H_count']) for x in data['comparisons']]
assert table == expected, (table,expected)
sources = json.loads((root/'data'/'source_index.json').read_text())
for item in sources:
    path = root/item['file']
    content = path.read_bytes()
    assert hashlib.sha256(content).hexdigest() == item['sha256_text']
    assert b'\0' not in content
    content.decode('utf-8')
for path in root.rglob('*'):
    if not path.is_file(): continue
    assert path.suffix.lower() not in {'.pdf','.png','.jpg','.jpeg','.webp','.tiff','.tif','.djvu'}
    with path.open('rb') as f:
        assert f.read(5) != b'%PDF-'
summary = {'report_status':'PARTIAL','comparison_rows_verified':len(table),
           'graphs_independently_checked_through_6':len(data['graphs']),
           'extracted_source_hashes_verified':len(sources),
           'source_files_utf8_plain_text':True,'no_pdfs_or_paper_images':True,
           'niceness':data['niceness'],'threads':data['threads'],
           'peak_enumeration_rss_MiB':data['max_rss_bytes']/1024**2}
(root/'data'/'artifact_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
