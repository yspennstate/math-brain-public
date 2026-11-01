import urllib.request, urllib.parse, concurrent.futures, json, datetime
from pathlib import Path
root=Path(__file__).parent
queries={
"source_pdf":"https://arxiv.org/pdf/1601.08219",
"arxiv":"https://export.arxiv.org/api/query?search_query="+urllib.parse.quote('all:"Dirichlet" AND (all:"ballistic" OR all:"ballisticity")')+"&start=0&max_results=80&sortBy=submittedDate&sortOrder=descending",
"openalex":"https://api.openalex.org/works?search="+urllib.parse.quote("random walk Dirichlet environment ballisticity")+"&per-page=60",
"crossref":"https://api.crossref.org/works?query="+urllib.parse.quote("Dirichlet random environment ballisticity")+"&rows=40",
"semantic":"https://api.semanticscholar.org/graph/v1/paper/search?query="+urllib.parse.quote("Dirichlet random environment ballisticity")+"&limit=50&fields=title,authors,year,externalIds,abstract,url",
"github":"https://api.github.com/search/repositories?q="+urllib.parse.quote("Dirichlet random walk ballisticity")
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={"User-Agent":"ProbabilityResearch/1.0"})
  with urllib.request.urlopen(req,timeout=75) as r: data=r.read()
  out=root/(name+(".pdf" if name=="source_pdf" else ".json" if name not in ["arxiv"] else ".xml"));out.write_bytes(data)
  result={"service":name,"url":url,"date":"2026-10-11","status":"ok","bytes":len(data)}
 except Exception as e: result={"service":name,"url":url,"date":"2026-10-11","status":str(e)}
 print(json.dumps(result),flush=True)
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(fetch,queries.items()))
(root/"search_log.json").write_text(json.dumps(results,indent=2),encoding="utf-8")
