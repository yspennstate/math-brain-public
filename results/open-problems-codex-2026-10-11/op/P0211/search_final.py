import urllib.request,urllib.parse,pathlib,json,concurrent.futures,xml.etree.ElementTree as E
q=urllib.parse.quote
jobs=[('arxiv_finite.xml','http://export.arxiv.org/api/query?search_query='+q('ti:"Stochastic coagulation-fragmentation processes"')+'&max_results=10'),('arxiv_aldous.xml','http://export.arxiv.org/api/query?search_query='+q('all:"Aldous" AND all:"fragmentation" AND (all:"mixing" OR all:"relaxation")')+'&max_results=30'),('crossref_survey.json','https://api.crossref.org/works?query.title='+q('Deterministic and Stochastic Becker-Doring equations Past and Recent Mathematical Developments')+'&rows=5'),('openalex_citing_source.json','https://api.openalex.org/works?filter=locations.landing_page_url:'+q('https://www.stat.berkeley.edu/~aldous/Research/OP/coag_frag_mix.pdf')+'&per_page=10'),('semantic_source.json','https://api.semanticscholar.org/graph/v1/paper/URL:'+q('https://www.stat.berkeley.edu/~aldous/Research/OP/coag_frag_mix.pdf')+'?fields=title,citations.title,citations.year,citations.externalIds')]
def fetch(j):
 name,url=j
 try:
  b=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'P0211Research/1.0'}),timeout=35).read();pathlib.Path(name).write_bytes(b);r={'date':'2026-10-11','file':name,'url':url,'status':'OK','bytes':len(b)}
 except Exception as e:r={'date':'2026-10-11','file':name,'url':url,'status':str(e)}
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:rows=list(ex.map(fetch,jobs))
with open('search_log.jsonl','a',encoding='utf8') as f:
 for r in rows:f.write(json.dumps(r)+'\n')
print(json.dumps(rows,indent=2))
ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv_finite.xml','arxiv_aldous.xml']:
 if pathlib.Path(name).exists():
  for e in E.parse(name).getroot().findall('a:entry',ns):print(e.find('a:id',ns).text,e.find('a:title',ns).text,e.find('a:summary',ns).text[:2000])
print(pathlib.Path('granovsky.txt').read_text(encoding='utf8')[:3800])
