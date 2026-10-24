"""Small bounded public reads, saved in this worker's folder; no credentials."""
import hashlib
import json
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / 'sources'
OUT.mkdir(exist_ok=True)
PIN = 'fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb'
BASE = 'https://raw.githubusercontent.com/openai/math/' + PIN + '/'
FILES = {
    'BenjaminiSchramm.lean': BASE + 'lean/ComparatorChallenges/BenjaminiSchramm.lean',
    'CayleyPercolation.lean': BASE + 'lean/ComparatorChallenges/CayleyPercolation.lean',
    '214.md': BASE + 'lean/docs/214.md',
    'claimed_resolution.pdf': BASE + 'preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf',
}
receipt = []
for name, url in FILES.items():
    record = {'name': name, 'url': url, 'commit': PIN}
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'C0047-source-audit'})
        with urllib.request.urlopen(request, timeout=15) as response:
            data = response.read(4 * 1024 * 1024 + 1)
        if len(data) > 4 * 1024 * 1024:
            raise ValueError('source exceeds bounded read limit')
        (OUT / name).write_bytes(data)
        record.update({'ok': True, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    except Exception as exc:
        record.update({'ok': False, 'error': type(exc).__name__ + ': ' + str(exc)})
    receipt.append(record)
    (HERE / 'PUBLIC_SOURCE_HASHES.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
    print(json.dumps(record))
