from pathlib import Path
import concurrent.futures, urllib.request, urllib.parse, json

ROOT = Path(__file__).resolve().parent
urls = {
    'source.pdf': 'https://arxiv.org/pdf/math/9906194',
    'convergence.pdf': 'https://arxiv.org/pdf/1804.06148',
    'supercritical.pdf': 'https://arxiv.org/pdf/1411.4318',
    'arxiv_search.xml': 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query':'all:"zero-range" AND all:"convergence"','max_results':20}),
    'openalex_search.json': 'https://api.openalex.org/works?' + urllib.parse.urlencode({'search':'disordered zero range quenched convergence','per-page':15}),
    'earlier.pdf': 'https://arxiv.org/pdf/math/9911205',
}
def fetch(item):
    name, url = item
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Independent mathematical audit'})
        with urllib.request.urlopen(req, timeout=55) as response:
            data = response.read()
            status = response.status
        (ROOT/name).write_bytes(data)
        result = dict(file=name,url=url,status=status,bytes=len(data))
        if name.endswith('.pdf'):
            import fitz
            doc = fitz.open(ROOT/name)
            txt = '\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+page.get_text() for i,page in enumerate(doc))
            (ROOT/name.replace('.pdf','.txt')).write_text(txt,encoding='utf-8')
            result['pages'] = len(doc)
        return result
    except Exception as e:
        return dict(file=name,url=url,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results = list(pool.map(fetch,urls.items()))
(ROOT/'fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
for result in results: print(json.dumps(result))
