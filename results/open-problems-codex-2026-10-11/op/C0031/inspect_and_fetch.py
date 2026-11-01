import pathlib,json,xml.etree.ElementTree as ET, urllib.request,urllib.parse,concurrent.futures
R=pathlib.Path(__file__).parent
t=(R/'survey.txt').read_text(encoding='utf8')
start=t.find('6.6.', t.find('--- PDF PAGE 35'))
print('SURVEY SECTION\n'+t[start:start+17000],flush=True)
ns={'a':'http://www.w3.org/2005/Atom'}
for e in ET.parse(R/'arxiv.xml').findall('a:entry',ns): print('ARXIV',e.find('a:id',ns).text,e.find('a:title',ns).text,e.find('a:summary',ns).text,flush=True)
for e in json.loads((R/'crossref.json').read_text())['message']['items']:
 print('CROSSREF',e.get('title'),e.get('DOI'),e.get('published'),flush=True)
for e in json.loads((R/'github.json').read_text()).get('items',[]): print('GITHUB',e['full_name'],e.get('description'),flush=True)
jobs={
 'original.pdf':'https://arxiv.org/pdf/1006.1713',
 'openalex_source.json':'https://api.openalex.org/works/https://doi.org/10.1016/j.probab.2012.02.004',
 'openalex_retry.json':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Spectrum of non-Hermitian heavy tailed random matrices','per-page':20}),
 'semantic_retry.json':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1109.3343/citations?fields=title,year,authors,externalIds&limit=1000',
 'arxiv_broad.xml':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"heavy-tailed" AND (all:"non-Hermitian" OR all:"circular")','max_results':80,'sortBy':'submittedDate','sortOrder':'descending'}),
}
def fetch(item):
 name,url=item
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mathematics-research/1.0'}),timeout=50) as f:data=f.read()
  (R/name).write_bytes(data); s=f'OK {len(data)}'
 except Exception as e:s=f'FAILED {e}'
 print(name,s,flush=True)
 return {'file':name,'url':url,'date':'2026-10-11','status':s}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: out=list(ex.map(fetch,jobs.items()))
log=json.loads((R/'search_log.json').read_text());log+=out;(R/'search_log.json').write_text(json.dumps(log,indent=2),encoding='utf8')
import pymupdf
if (R/'original.pdf').exists():
 doc=pymupdf.open(R/'original.pdf');(R/'original.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
