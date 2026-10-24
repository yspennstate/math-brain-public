from pathlib import Path
import concurrent.futures
import json
import urllib.request
import fitz

ROOT = Path(__file__).resolve().parent
URLS = {
    'source.pdf': 'https://arxiv.org/pdf/math/0510518',
    'resolution.pdf': 'https://arxiv.org/pdf/2405.20019v2',
    'crossref.json': 'https://api.crossref.org/works/10.1007/s10959-024-01399-1',
    'arxiv_search.xml': 'https://export.arxiv.org/api/query?search_query=all%3A%22Brownian%20sheet%22%20AND%20%28all%3Aprojection%20OR%20all%3AMarstrand%29&max_results=20',
}

def fetch(item):
    name, url = item
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Independent-mathematical-audit/1.0'})
        with urllib.request.urlopen(req, timeout=60) as response:
            data = response.read()
            status = response.status
        (ROOT / name).write_bytes(data)
        print(name, status, len(data), url, flush=True)
        if name.endswith('.pdf'):
            doc = fitz.open(stream=data, filetype='pdf')
            pages = ['\n===== PDF PAGE %d =====\n%s' % (i+1, p.get_text()) for i,p in enumerate(doc)]
            (ROOT / name.replace('.pdf', '.txt')).write_text(''.join(pages), encoding='utf-8')
        elif name == 'crossref.json':
            m = json.loads(data)['message']
            print(json.dumps({k:m.get(k) for k in ['title','author','published','container-title','volume','article-number','DOI']}, ensure_ascii=False), flush=True)
    except Exception as exc:
        print(name, type(exc).__name__, str(exc), flush=True)

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(fetch, URLS.items()))
