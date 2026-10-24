import requests, json, re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
root = Path(__file__).resolve().parent
queries = {
    'arxiv_query': ('https://export.arxiv.org/api/query', {'search_query': 'all:"Brownian net"', 'max_results': 40, 'sortBy': 'submittedDate', 'sortOrder': 'descending'}),
    'arxiv_search': ('https://arxiv.org/search/', {'query': 'Brownian net', 'searchtype': 'all', 'abstracts': 'show', 'order': '-announced_date_first', 'size': 50}),
    'crossref': ('https://api.crossref.org/works', {'query.title': 'Brownian net', 'rows': 30}),
    'kou_abstract': ('https://arxiv.org/abs/2512.10761', {}),
    'universality_abstract': ('https://arxiv.org/abs/2401.09370', {}),
}
def fetch(item):
    name, (url, params) = item
    try:
        r = requests.get(url, params=params, timeout=35)
        (root/(name+'.response.txt')).write_text(r.text, encoding='utf-8')
        r.raise_for_status()
        if name == 'crossref':
            summary = [[w.get('title'), w.get('DOI'), w.get('published', {})] for w in r.json()['message']['items']]
        elif name.endswith('abstract'):
            summary = re.findall(r'<blockquote[^>]*>(.*?)</blockquote>', r.text, re.S)
            summary = [re.sub('<[^>]+>', '', x).strip() for x in summary]
        else:
            summary = re.sub('<[^>]+>', ' ', r.text)
            summary = re.sub(r'\s+', ' ', summary)[:18000]
        result = [name, r.status_code, summary]
    except Exception as e:
        result = [name, str(e)]
    print(json.dumps(result, ensure_ascii=False), flush=True)
    return result
results = list(ThreadPoolExecutor(max_workers=5).map(fetch, queries.items()))
(root/'search_more_summary.json').write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding='utf-8')
