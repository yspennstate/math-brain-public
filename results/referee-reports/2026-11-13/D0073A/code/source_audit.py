"""Plain-text source hygiene, hashes, and theorem-to-PDF-page navigation."""
import hashlib, json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
records = []
for path in sorted((root / 'sources').glob('*.txt')):
    text = path.read_text()
    if not text.startswith('SOURCE URL: '):
        continue
    if '\0' in text:
        text = text.replace('\0', '[NULL]')
        path.write_text(text)
    page, hits = 0, []
    for line in text.splitlines():
        match = re.match(r'===== PDF PAGE (\d+) =====', line)
        if match:
            page = int(match[1])
        if re.search(r'(?:Theorem|THEOREM|Corollary|COROLLARY|Lemma|LEMMA|Question)\s+\d', line):
            hits.append({'pdf_page': page, 'text': line.strip()})
    records.append({'file': str(path.relative_to(root)),
                    'sha256_text': hashlib.sha256(path.read_bytes()).hexdigest(),
                    'bytes': path.stat().st_size,
                    'source_url': text.splitlines()[0].removeprefix('SOURCE URL: '),
                    'theorem_locations': hits})
(root / 'data' / 'source_index.json').write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n')
print(f'Indexed {len(records)} plain-text sources')
