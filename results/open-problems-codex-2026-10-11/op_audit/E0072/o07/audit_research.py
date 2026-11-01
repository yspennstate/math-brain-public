import concurrent.futures, json, pathlib, urllib.parse, urllib.request
import fitz

ROOT = pathlib.Path(__file__).resolve().parent
queries = {
    'source': 'https://arxiv.org/pdf/1406.0763',
    'norm_paper': 'https://arxiv.org/pdf/1310.2921',
    'arxiv_search': 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': '(all:"cancellation norm" OR all:"cancelation norm" OR all:"spelling length") AND (all:"random" OR all:"drift")', 'max_results': 30}),
    'arxiv_biinvariant': 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': '(all:"bi-invariant" OR all:"conjugation-invariant") AND all:"drift"', 'max_results': 30}),
    'openalex': 'https://api.openalex.org/works?' + urllib.parse.urlencode({'search': 'cancellation norm random walk drift', 'per-page': 15}),
    'openalex_source': 'https://api.openalex.org/works?' + urllib.parse.urlencode({'search': 'Five remarks about random walks on groups', 'per-page': 5}),
}

def fetch(item):
    name, url = item
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'IndependentMathematicalAudit/1.0'})
        with urllib.request.urlopen(req, timeout=40) as response:
            data = response.read()
        suffix = '.pdf' if name in ('source', 'norm_paper') else '.txt'
        (ROOT / (name + suffix)).write_bytes(data)
        if suffix == '.pdf':
            doc = fitz.open(stream=data, filetype='pdf')
            pages = [p.get_text() for p in doc]
            (ROOT / (name + '_text.txt')).write_text('\n'.join(f'PDF PAGE {i+1}\n{p}' for i,p in enumerate(pages)), encoding='utf-8')
            if name == 'source':
                print('SOURCE PAGE 1\n' + pages[0], flush=True)
                for i,p in enumerate(pages):
                    if 'Problem 4' in p:
                        print(f'SOURCE PAGE {i+1}\n' + p, flush=True)
        else:
            if name.startswith('openalex'):
                result = json.loads(data)
                print(name, json.dumps([{'title': w.get('title'), 'year': w.get('publication_year'), 'doi': w.get('doi'), 'id': w.get('id')} for w in result.get('results', [])], ensure_ascii=False), flush=True)
            else:
                import xml.etree.ElementTree as ET
                root = ET.fromstring(data)
                ns = {'a': 'http://www.w3.org/2005/Atom'}
                entries = [{'title': e.findtext('a:title', namespaces=ns), 'id': e.findtext('a:id', namespaces=ns), 'abstract': e.findtext('a:summary', namespaces=ns)} for e in root.findall('a:entry', ns)]
                (ROOT / (name + '_summary.json')).write_text(json.dumps(entries, indent=2), encoding='utf-8')
                print(name, json.dumps(entries, ensure_ascii=False), flush=True)
        return {'name': name, 'url': url, 'ok': True, 'bytes': len(data)}
    except Exception as e:
        return {'name': name, 'url': url, 'ok': False, 'error': str(e)}

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results = list(pool.map(fetch, queries.items()))
(ROOT / 'research_log.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
print(json.dumps(results, indent=2), flush=True)
