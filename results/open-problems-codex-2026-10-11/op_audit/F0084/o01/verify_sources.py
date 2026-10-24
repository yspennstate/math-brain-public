from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
import fitz
import json

ROOT = Path(__file__).resolve().parent
SOURCES = {
    'matching_journal': 'https://www.numdam.org/item/AIHPB_2009__45_1_266_0.pdf',
    'original': 'https://arxiv.org/pdf/math/0505668',
    'matching_arxiv': 'https://arxiv.org/pdf/0712.1867',
    'crossref': 'https://api.crossref.org/works/10.1214/08-AIHP170',
    'search_arxiv': 'https://export.arxiv.org/api/query?search_query=all:%22stable%20marriage%22%20AND%20all:Poisson&max_results=15',
}

def fetch(item):
    name, url = item
    try:
        r = requests.get(url, timeout=45)
        info = {'name': name, 'url': url, 'status': r.status_code}
        if r.status_code == 200:
            if r.content.startswith(b'%PDF'):
                (ROOT / (name + '.pdf')).write_bytes(r.content)
                doc = fitz.open(stream=r.content, filetype='pdf')
                text = '\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc))
                (ROOT / (name + '.txt')).write_text(text, encoding='utf-8')
                info['pages'] = len(doc)
            else:
                (ROOT / (name + '.txt')).write_text(r.text, encoding='utf-8')
        return info
    except Exception as e:
        return {'name':name, 'url':url, 'error':str(e)}

with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fetch, SOURCES.items()))
(ROOT / 'retrieval_log.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
print(json.dumps(results, indent=2))
