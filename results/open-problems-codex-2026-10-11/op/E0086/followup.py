from pathlib import Path
import json, urllib.request, urllib.parse, concurrent.futures, xml.etree.ElementTree as ET

P = Path(__file__).parent
urls = {
    'openalex_doi': 'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1606.03787',
    'semantic_citing': 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1606.03787/citations?fields=title,year,externalIds&limit=100',
    'arxiv_okada': 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query':'au:Okada AND (all:"boundary" OR all:"favorite")','max_results':30}),
    'favorite_2024': 'https://arxiv.org/pdf/2409.00995',
    'potential_book': 'https://www.math.uchicago.edu/~lawler/srwbook.pdf',
}
def fetch(item):
    name, url = item
    try:
        b = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'E0086 probability research'}),timeout=40).read()
        path = P / ('search_' + name + ('.pdf' if b.startswith(b'%PDF') else '.txt'))
        path.write_bytes(b)
        if b.startswith(b'%PDF'):
            import pymupdf
            doc = pymupdf.open(path)
            path.with_suffix('.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+page.get_text() for i,page in enumerate(doc)),encoding='utf-8')
        return name,url,'OK',len(b)
    except Exception as e:
        return name,url,'ERROR',str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    results=list(pool.map(fetch, urls.items()))
source_path=P/'search_openalex_doi.txt'
if source_path.exists():
    data=json.loads(source_path.read_text(encoding='utf-8'))
    if data.get('title','').lower()=='topics and problems on favorite sites of random walks':
        wid=data['id'].rsplit('/',1)[-1]
        results.append(fetch(('openalex_citing','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+wid,'per-page':100}))))
(P/'search_log3.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
for r in results: print(r)
