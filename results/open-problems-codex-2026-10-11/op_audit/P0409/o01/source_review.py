import concurrent.futures, json, pathlib, urllib.request
import fitz

BASE = pathlib.Path(__file__).resolve().parent
urls = {
 'source': 'https://arxiv.org/pdf/2303.16831',
 'arxiv_search': 'https://export.arxiv.org/api/query?search_query=all%3A%22ideal%22+AND+all%3A%22Voronoi%22&max_results=30',
 'openalex_search': 'https://api.openalex.org/works?search=ideal%20Voronoi%20neighboring%20vertices&per-page=20',
 'openalex_citations': 'https://api.openalex.org/works?filter=cites:W4361807156&per-page=100',
 'openalex_journal_citations': 'https://api.openalex.org/works?filter=cites:W7131653980&per-page=100',
}
def fetch(item):
 name, url = item
 try:
  req = urllib.request.Request(url, headers={'User-Agent':'ProbabilityAudit/1.0'})
  with urllib.request.urlopen(req, timeout=45) as r: data=r.read()
  target=BASE/(name+('.pdf' if name=='source' else '.txt'))
  target.write_bytes(data)
  if name=='source':
   doc=fitz.open(target)
   (BASE/'source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
   return name, f'{len(doc)} pages'
  if name.startswith('openalex'):
   obj=json.loads(data)
   return name, [{'title':v['title'],'year':v.get('publication_year'),'doi':v.get('doi'),'id':v['id']} for v in obj.get('results',[])]
  return name, data.decode()[:14000]
 except Exception as e: return name,repr(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 results=dict(pool.map(fetch,urls.items()))
(BASE/'literature_results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(results,indent=2,ensure_ascii=False))
