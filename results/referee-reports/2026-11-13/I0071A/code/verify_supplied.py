"""Independently re-fetch supplied source URLs and check their PDF fingerprints."""
import hashlib
import json
import re
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
records = []
for name in ['survey_published.txt', 'survey_v5.txt', 'reaction_2026.txt', 'reaction_2026_v3.txt']:
    header = (ROOT/'sources'/name).read_text()[:1200]
    url = re.search(r'SOURCE URL: (\S+)', header).group(1)
    expected = re.search(r'PDF SHA256 \(bytes never saved\): (\w+)', header).group(1)
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        actual = hashlib.sha256(response.content).hexdigest()
        record = {'file': name, 'url': url, 'expected_pdf_sha256': expected,
                  'actual_pdf_sha256': actual, 'match': actual == expected,
                  'is_pdf': response.content.startswith(b'%PDF')}
    except Exception as exc:
        record = {'file': name, 'url': url, 'error': str(exc)}
    records.append(record)
    print(json.dumps(record), flush=True)
(ROOT/'data'/'supplied_source_verification.json').write_text(json.dumps(records, indent=2)+'\n')
