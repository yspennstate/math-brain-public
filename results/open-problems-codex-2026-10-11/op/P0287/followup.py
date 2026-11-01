import concurrent.futures,json,pathlib,urllib.request,urllib.parse,xml.etree.ElementTree as E
P=pathlib.Path(__file__).parent; q=urllib.parse.quote
jobs={
'workshop_page':'https://lpetrov.cc/kpz2025/index.html',
'arxiv_removal':'https://export.arxiv.org/api/query?search_query='+q('all:TASEP AND (all:killing OR all:removal OR all:sink)')+'&max_results=100&sortBy=submittedDate&sortOrder=descending',
'arxiv_halfline':'https://export.arxiv.org/api/query?search_query='+q('all:ASEP AND (all:semi-infinite OR all:half-line) AND all:stationary')+'&max_results=30',
'openalex_retry':'https://api.openalex.org/works?search='+q('TASEP killing at one site')+'&per_page=5',
'openalex_report_retry':'https://api.openalex.org/works?search='+q('roadtokpzrep')+'&per_page=5',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/search?query='+q('TASEP particle removal invariant')+'&limit=5&fields=title,year,authors,url',
'crossref_target':'https://api.crossref.org/works?query.bibliographic='+q('TASEP particle removal single site')+'&rows=20',
'github_target':'https://api.github.com/search/repositories?q='+q('TASEP stationary')+'&per_page=20',
}
def fetch(item):
 name,url=item
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r: data=r.read(); code=r.status
  file=name+('.json' if data.lstrip().startswith(b'{') else '.txt'); (P/file).write_bytes(data)
  out={'service':name,'url':url,'date':'2026-10-12','status':code,'file':file,'bytes':len(data)}
 except Exception as e: out={'service':name,'url':url,'date':'2026-10-12','error':str(e)}
 print(json.dumps(out),flush=True); return out
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: out=list(ex.map(fetch,jobs.items()))
(P/'followup_log.json').write_text(json.dumps(out,indent=2),encoding='utf8')
