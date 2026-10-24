import concurrent.futures
import json
import pathlib
import requests
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
queries = [
    ('arxiv_boundary', 'https://export.arxiv.org/api/query', {'search_query': 'all:"random walk" AND all:"boundary" AND all:"local time"', 'max_results': 25, 'sortBy': 'submittedDate', 'sortOrder': 'descending'}),
    ('arxiv_offsets', 'https://export.arxiv.org/api/query', {'search_query': 'all:"random walk" AND (all:"moving offset" OR all:"generalized boundary" OR all:"annular")', 'max_results': 25}),
    ('arxiv_favorites', 'https://export.arxiv.org/api/query', {'search_query': 'all:"favorite sites" AND all:"random walk"', 'max_results': 25, 'sortBy': 'submittedDate', 'sortOrder': 'descending'}),
    ('openalex_source', 'https://api.openalex.org/works', {'search': 'Topics and problems on favorite sites of random walks', 'per_page': 5}),
    ('openalex_offsets', 'https://api.openalex.org/works', {'search': 'random walk moving boundary maximal local time annulus', 'per_page': 10}),
    ('crossref_thick', 'https://api.crossref.org/works', {'query.title': 'Thick points for planar Brownian motion and the Erdos Taylor conjecture on random walk', 'rows': 3}),
]

def run(item):
    name, url, params = item
    try:
        response = requests.get(url, params=params, timeout=35)
        (ROOT / (name + '_referee.txt')).write_text(response.text, encoding='utf-8')
        result = {'name': name, 'url': response.url, 'status': response.status_code}
        if response.ok and name.startswith('arxiv'):
            ns = {'a': 'http://www.w3.org/2005/Atom'}
            entries = ET.fromstring(response.text).findall('a:entry', ns)
            result['entries'] = [{'id': e.findtext('a:id', namespaces=ns), 'title': ' '.join(e.findtext('a:title', namespaces=ns).split()), 'abstract': ' '.join(e.findtext('a:summary', namespaces=ns).split())} for e in entries]
        elif response.ok and name.startswith('openalex'):
            result['entries'] = [{'title': e.get('title'), 'doi': e.get('doi'), 'year': e.get('publication_year')} for e in response.json()['results']]
        elif response.ok:
            result['entries'] = [{'title': e.get('title'), 'DOI': e.get('DOI'), 'abstract': e.get('abstract')} for e in response.json()['message']['items']]
        return result
    except Exception as exc:
        return {'name': name, 'error': str(exc)}

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results = list(pool.map(run, queries))
(ROOT / 'referee_search_log.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
for result in results:
    print(json.dumps(result, ensure_ascii=False))
