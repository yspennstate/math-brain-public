import urllib.request
import pathlib
import json
import concurrent.futures

BASE = pathlib.Path(__file__).resolve().parent
URLS = {
    'arxiv': 'https://export.arxiv.org/api/query?search_query=all%3A%22Erlang%20Weighted%20Tree%22%20OR%20all%3A%22La-Kabkab%22&max_results=20',
    'arxiv_bilateral': 'https://export.arxiv.org/api/query?search_query=all%3A%22bilateral%20preference%22&max_results=30',
    'openalex': 'https://api.openalex.org/works?search=Erlang%20Weighted%20Tree&per-page=10',
    'source': 'https://arxiv.org/pdf/2002.03993v5',
    'connectivity': 'https://arxiv.org/pdf/2209.05677v3',
    'citations': 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2002.03993/citations?fields=title,year,externalIds&limit=100',
}

def fetch(item):
    name, url = item
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'IndependentProbabilityAudit/1.0'})
        with urllib.request.urlopen(request, timeout=45) as r:
            b = r.read()
            filename = name + ('.pdf' if name in ('source', 'connectivity') else '.txt')
            (BASE / filename).write_bytes(b)
            return dict(name=name, url=url, status=r.status, bytes=len(b))
    except Exception as e:
        return dict(name=name, url=url, error=str(e))

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        records = list(pool.map(fetch, URLS.items()))
    (BASE / 'fetch_log.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
    print(json.dumps(records, indent=2))
