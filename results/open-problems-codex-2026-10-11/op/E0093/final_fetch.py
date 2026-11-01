from search import fetch,ROOT,q
import concurrent.futures,json,pymupdf
jobs=[
 ('hildebrand_pdf','https://arxiv.org/pdf/math/0401189'),
 ('uppertriangular_pdf','https://arxiv.org/pdf/1911.02974'),
 ('diameter2026_pdf','https://arxiv.org/pdf/2605.29457'),
 ('lie_pdf','https://arxiv.org/pdf/1309.1975'),
 ('openalex_doi_final','https://api.openalex.org/works/doi:10.3150/12-BEJSP09'),
 ('crossref_abelian','https://api.crossref.org/works/10.4171/JEMS/1743'),
 ('semantic_bulk','https://api.semanticscholar.org/graph/v1/paper/search/bulk?query='+q('"random Cayley" mixing')+'&fields=title,year,authors,externalIds')]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(fetch,jobs))
sourcepath=ROOT/'openalex_doi_final.raw'
if sourcepath.exists():
    try:
        source=json.loads(sourcepath.read_text())
        oid=source['id'].rsplit('/',1)[-1]
        results.append(fetch(('openalex_valid_citations','https://api.openalex.org/works?filter=cites:'+oid+'&per-page=100')))
    except Exception as e: print('OpenAlex citations unavailable:',e)
(ROOT/'final_fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
for name in ['hildebrand','uppertriangular','diameter2026','lie']:
    try:
        doc=pymupdf.open(ROOT/(name+'_pdf.raw'))
        (ROOT/(name+'.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
    except Exception as e: print(name,repr(e))
