from pathlib import Path
import concurrent.futures, requests, json, math, itertools

ROOT = Path(__file__).resolve().parent
QUERIES = {
    'openalex_exact': 'https://api.openalex.org/works?search=%22potential%20most%20recent%20common%20ancestors%22&per-page=20',
    'openalex_net': 'https://api.openalex.org/works?search=Brownian%20net&per-page=100',
    'arxiv': 'https://export.arxiv.org/api/query?search_query=all:%22Brownian%20net%22&max_results=20&sortBy=submittedDate&sortOrder=descending',
}

def fetch(item):
    name, url = item
    try:
        r = requests.get(url, timeout=35)
        (ROOT / (name + '_search.txt')).write_text(r.text, encoding='utf-8')
        record = dict(name=name, url=url, status=r.status_code)
        if name.startswith('openalex') and r.ok:
            record['count'] = r.json().get('meta', {}).get('count')
            record['works'] = [dict(title=w.get('title'), year=w.get('publication_year'), doi=w.get('doi')) for w in r.json().get('results', [])]
        return record
    except Exception as e:
        return dict(name=name, url=url, error=str(e))

with concurrent.futures.ThreadPoolExecutor(3) as pool:
    results = list(pool.map(fetch, QUERIES.items()))
(ROOT / 'literature_search_log.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
for r in results:
    print(json.dumps(r), flush=True)

# Independent scalar and Gaussian checks; these do not certify stochastic theorems.
count = 0
for l, f, g, r in itertools.product(range(-5, 6), repeat=4):
    if l <= f < g <= r:
        assert l < r
        count += 1
for x in [0.01, 0.1, 0.5, 1, 2, 5, 10]:
    assert 4 * (0.5 * math.erfc(x / math.sqrt(2))) <= 4 * math.exp(-x*x/2)
print('Exact scalar checks:', count, '; Gaussian tail checks: 7')
