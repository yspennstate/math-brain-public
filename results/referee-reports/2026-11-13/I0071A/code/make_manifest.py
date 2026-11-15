"""Record the retained plain-text source inventory and available PDF provenance."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
retrieved = {}
for line in (ROOT/'data'/'retrievals.jsonl').read_text().splitlines():
    record = json.loads(line)
    retrieved[Path(record['file']).name] = record
manifest = []
for path in sorted((ROOT/'sources').glob('*.txt')):
    raw = path.read_bytes()
    text = raw.decode()
    header = text[:1500]
    entry = {'file': str(path.relative_to(ROOT)),
             'text_sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw),
             'pdf_pages': len(re.findall(r'===== PDF PAGE \d+ =====', text))}
    if path.name in retrieved:
        entry.update({k: retrieved[path.name][k] for k in ['url', 'pdf_sha256']})
    else:
        for key, pattern in [('url', r'SOURCE URL: (\S+)'),
                             ('pdf_sha256', r'PDF SHA256 \(bytes never saved\): (\w+)')]:
            match = re.search(pattern, header)
            if match:
                entry[key] = match.group(1)
    manifest.append(entry)
(ROOT/'data'/'source_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
print(f'{len(manifest)} plain-text sources, {sum(x["bytes"] for x in manifest)} bytes')
