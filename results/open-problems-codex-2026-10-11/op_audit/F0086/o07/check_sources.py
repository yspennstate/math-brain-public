from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
targets = {
    'branden': 'https://arxiv.org/pdf/1104.3531v2',
    'source': 'https://arxiv.org/pdf/math/0503110',
    'crossref': 'https://api.crossref.org/works/10.1016/j.laa.2011.06.022',
    'arxiv_search': 'https://export.arxiv.org/api/query?search_query=all:%22alpha-determinants%22&max_results=10',
    'openalex_search': 'https://api.openalex.org/works?search=Solutions%20to%20two%20problems%20on%20permanents&per-page=3',
}

def fetch(item):
    name, url = item
    try:
        r = requests.get(url, timeout=50)
        suffix = '.pdf' if name in ('branden', 'source') else '.txt'
        (ROOT / (name + suffix)).write_bytes(r.content)
        print(name, r.status_code, len(r.content), url, flush=True)
        if suffix == '.pdf' and r.ok:
            reader = PdfReader(ROOT / (name + suffix))
            pages = [f'PDF PAGE {i+1}\n{p.extract_text()}' for i,p in enumerate(reader.pages)]
            (ROOT / (name + '.txt')).write_text('\n\n'.join(pages), encoding='utf-8')
    except Exception as e:
        print(name, type(e).__name__, str(e), flush=True)

with ThreadPoolExecutor(max_workers=5) as pool:
    list(pool.map(fetch, targets.items()))
