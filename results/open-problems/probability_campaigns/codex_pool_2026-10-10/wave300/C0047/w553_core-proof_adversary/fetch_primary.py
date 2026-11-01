"""Fetch only named public primary files, with bounded requests and provenance."""
from pathlib import Path
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'sources'
OUT.mkdir(exist_ok=True)
base = 'https://raw.githubusercontent.com/openai/math/main/'
targets = {
    'public_result_214.md': base + 'lean/docs/214.md',
    'public_comparator_BenjaminiSchramm.lean': base + 'lean/ComparatorChallenges/BenjaminiSchramm.lean',
    'public_comparator_CayleyPercolation.lean': base + 'lean/ComparatorChallenges/CayleyPercolation.lean',
    'public_repo_README.md': base + 'README.md',
    'public_nonuniqueness_paper.pdf': base + 'preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf',
    'hutchcroft_l2_1904.05804.pdf': 'https://arxiv.org/pdf/1904.05804',
}
records = []
for name, url in targets.items():
    record = {'file': name, 'url': url}
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'C0047-primary-audit/1.0'})
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read(8_000_001)
            if len(data) > 8_000_000:
                raise ValueError('Scoped source size limit exceeded')
            record.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), content_type=response.headers.get('Content-Type'))
        (OUT / name).write_bytes(data)
        record['status'] = 'FETCHED_NOT_MATHEMATICALLY_VALIDATED'
    except Exception as exc:
        record.update(status='UNAVAILABLE', error=str(exc))
    records.append(record)
    (OUT / 'FETCH_RECEIPT.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
    print(json.dumps(record), flush=True)
