"""Fetch only C0047's named public source artifacts; write solely under this folder."""
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'sources'
OUT.mkdir(exist_ok=True)
BASE = 'https://raw.githubusercontent.com/openai/math/main/'
URLS = {
    'openai_214_scope.md': BASE + 'lean/docs/214.md',
    'openai_lean_README.md': BASE + 'lean/README.md',
    'openai_formalization.yaml': BASE + 'lean/formalization.yaml',
    'openai_BenjaminiSchramm_comparator.lean': BASE + 'lean/ComparatorChallenges/BenjaminiSchramm.lean',
    'openai_214_paper.pdf': BASE + 'preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf',
}
if __name__ == '__main__' and __import__('sys').argv[1:] == ['additional']:
    URLS = {
        'openai_214_Main.lean': BASE + 'lean/OAI/Probability/BenjaminiSchramm/Main.lean',
        'openai_214_comparator_config.json': BASE + 'lean/ComparatorChallenges/BenjaminiSchramm.json',
        'benjamini_schramm_1996.pdf': 'https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/978/978-3321-1-PB.pdf',
    }
receipts = []
receipt_file = OUT / ('ADDITIONAL_FETCH_RECEIPTS.json' if __import__('sys').argv[1:] == ['additional'] else 'FETCH_RECEIPTS.json')
for name, url in URLS.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'C0047-source-check'})
        with urllib.request.urlopen(req, timeout=20) as response:
            data = response.read(4_000_001)
        if len(data) > 4_000_000:
            raise ValueError('source exceeded 4 MB cap')
        (OUT / name).write_bytes(data)
        row = {'path': str(OUT / name), 'url': url, 'bytes': len(data),
               'sha256': hashlib.sha256(data).hexdigest(), 'status': 'fetched'}
        if name.endswith('README.md'):
            print(data.decode('utf-8'))
        if name.endswith('.yaml'):
            lines = data.decode('utf-8').splitlines()
            hits = [i for i, line in enumerate(lines) if '214' in line or 'BenjaminiSchramm' in line or 'CayleyPercolation' in line]
            for i in hits[:10]:
                print('\n'.join(f'{j+1}: {lines[j]}' for j in range(max(0,i-3),min(len(lines),i+12))))
        if name.endswith('.pdf'):
            import fitz
            doc = fitz.open(stream=data, filetype='pdf')
            pages = [p.get_text() for p in doc]
            (OUT / name.replace('.pdf','.txt')).write_text('\n\f\n'.join(pages), encoding='utf-8')
            print('PDF pages:', len(pages))
            for index, page in enumerate(pages):
                if ('1996' in name and index in (1,5)) or ('1996' not in name and (index == 0 or any(word in page for word in ['Theorem 1.1', 'critical operator', 'operator bound']))):
                    print('PAGE', index+1, page[:4000])
                    if index > 5:
                        break
        print(json.dumps(row), flush=True)
    except Exception as exc:
        row = {'path': str(OUT / name), 'url': url, 'status': 'unavailable', 'error': str(exc)}
        print(json.dumps(row), flush=True)
    receipts.append(row)
    receipt_file.write_text(json.dumps(receipts, indent=2), encoding='utf-8')
