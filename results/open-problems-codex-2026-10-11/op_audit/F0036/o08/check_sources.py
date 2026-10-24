from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests, fitz, json

ROOT = Path(__file__).resolve().parent
def fetch(item):
    name, url = item
    try:
        r = requests.get(url, timeout=50)
        r.raise_for_status()
        (ROOT / (name + '.pdf')).write_bytes(r.content)
        doc = fitz.open(stream=r.content, filetype='pdf')
        (ROOT / (name + '.txt')).write_text('\n'.join(page.get_text() for page in doc), encoding='utf-8')
        return [name, r.status_code, len(doc)]
    except Exception as e:
        return [name, str(e)]

urls = {'source': 'https://arxiv.org/pdf/1506.00724', 'special_points': 'https://arxiv.org/pdf/0806.2326', 'brownian_net': 'https://arxiv.org/pdf/math/0610625'}
print(list(ThreadPoolExecutor(max_workers=3).map(fetch, urls.items())), flush=True)
out = []
for i, q in enumerate(['potential most recent common ancestors', 'Brownian net meeting points', 'Brownian net']):
    try:
        r = requests.get('https://api.openalex.org/works', params={'search': q, 'per-page': 50}, timeout=40)
        r.raise_for_status()
        j = r.json()
        (ROOT / ('search_' + str(i) + '.json')).write_text(json.dumps(j), encoding='utf-8')
        item = [q, j['meta']['count'], [[w['display_name'], w['publication_year'], w.get('doi')] for w in j['results']]]
    except Exception as e:
        item = [q, str(e)]
    out.append(item)
    print(json.dumps(item, ensure_ascii=False), flush=True)
(ROOT / 'search_summary.json').write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
