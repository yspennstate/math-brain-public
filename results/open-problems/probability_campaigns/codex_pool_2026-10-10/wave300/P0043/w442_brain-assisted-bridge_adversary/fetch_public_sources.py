"""Fetch only the named public proof-verification instructions and paper."""
import importlib.util
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent / 'sources'
ROOT.mkdir(exist_ok=True)
targets = {
    'comparator_verification.md': 'https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/README.md',
    'critical_percolation_comparator.lean': 'https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/CriticalPercolation.lean',
    'quasi_transitive_claim.pdf': 'https://raw.githubusercontent.com/openai/math/main/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf',
}
rows = []
for name, url in targets.items():
    row = {'name': name, 'url': url}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            content = response.read(2_000_001)
        if len(content)>2_000_000:
            raise ValueError('source exceeded the 2 MB gate')
        (ROOT/name).write_bytes(content)
        row.update(ok=True, bytes=len(content))
        if name.endswith('.md'):
            print(content.decode('utf-8', errors='replace')[:16000])
    except Exception as exc:
        row.update(ok=False, error=str(exc))
    rows.append(row)
    (ROOT/'fetch_receipt.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')
    print(json.dumps(row))
print('pdf_readers', {name: importlib.util.find_spec(name) is not None for name in ['pypdf', 'fitz']})
