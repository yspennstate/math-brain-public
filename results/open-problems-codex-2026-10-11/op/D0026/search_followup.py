import concurrent.futures, datetime,json,pathlib,urllib.request,urllib.parse,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
Q=urllib.parse.quote
queries=[
 ('arxiv_fredrickson','all:Fredrickson AND all:Andersen','https://export.arxiv.org/api/query?search_query='+Q('all:Fredrickson AND all:Andersen')+'&sortBy=submittedDate&sortOrder=descending&max_results=100'),
 ('arxiv_facilitated','all:"facilitated" AND all:"equilibrium"','https://export.arxiv.org/api/query?search_query='+Q('all:"facilitated" AND all:"equilibrium"')+'&sortBy=submittedDate&sortOrder=descending&max_results=80'),
 ('crossref_recent','Fredrickson Andersen; published since 2025-10-23','https://api.crossref.org/works?query.title='+Q('Fredrickson Andersen')+'&filter=from-pub-date:2025-10-23&rows=60'),
 ('crossref_source','Long time behaviour of one facilitated kinetically constrained models','https://api.crossref.org/works?query.title='+Q('Long time behaviour of one facilitated kinetically constrained models')+'&rows=10'),
 ('openalex_source_retry','arxiv:2510.20461','https://api.openalex.org/works?search=2510.20461&per_page=5'),
 ('semantic_source_retry','ARXIV:2510.20461','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2510.20461?fields=title,authors,year,citationCount,citations.title,citations.year,citations.externalIds'),
 ('front_pdf','1803.08761','https://arxiv.org/pdf/1803.08761'),
]
def fetch(item):
 name,query,url=item;r={'service':name,'query':query,'url':url,'date':datetime.datetime.now().isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'}),timeout=45) as f:data=f.read();r['http_status']=f.status
  suffix='.pdf' if name.endswith('_pdf') else '.response'
  (ROOT/(name+suffix)).write_bytes(data);r['saved']=name+suffix
  if suffix=='.pdf':
   import pymupdf
   doc=pymupdf.open(ROOT/(name+suffix));(ROOT/(name+'.txt')).write_text('\n'.join('\n--- PAGE '+str(i+1)+' ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
  print(name,len(data),flush=True)
 except Exception as e:r['error']=repr(e);print(name,repr(e),flush=True)
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:records=list(ex.map(fetch,queries))
# Explicit title-search -> source-ID -> cites query in OpenAlex.
records.append(fetch(('openalex_title_retry','one facilitated kinetically constrained models','https://api.openalex.org/works?search='+Q('one facilitated kinetically constrained models')+'&per_page=5')))
for name in ['openalex_source_retry','openalex_title_retry']:
 try:
  for w in json.loads((ROOT/(name+'.response')).read_text()).get('results',[]):
   if 'one facilitated' in w.get('title','').lower():
    wid=w['id'].split('/')[-1];records.append(fetch(('openalex_citing_retry','cites:'+wid,'https://api.openalex.org/works?filter=cites:'+wid+'&per_page=100')))
 except Exception:pass
(ROOT/'followup_log.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
for name in ['arxiv_fredrickson','arxiv_facilitated']:
 try:
  ns={'a':'http://www.w3.org/2005/Atom'}
  for e in ET.fromstring((ROOT/(name+'.response')).read_bytes()).findall('a:entry',ns):
   print(name,e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns),e.findtext('a:title',namespaces=ns),flush=True)
 except Exception:pass
