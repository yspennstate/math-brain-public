import json, urllib.request, urllib.parse, concurrent.futures, datetime
from pathlib import Path
queries = {
 'arxiv_title': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Boundedness of discounted tree sums"','max_results':30}),
 'arxiv_rays': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"branching random walk" AND (all:"ray" OR all:"heavy-tailed")','sortBy':'submittedDate','sortOrder':'descending','max_results':50}),
 'openalex_title':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Boundedness of discounted tree sums','per-page':10}),
 'openalex_rays':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'branching random walk heavy tailed rays','per-page':25}),
 'crossref_title':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':'Boundedness of discounted tree sums','rows':10}),
 'crossref_rays':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'branching random walk extremal ray heavy tail','rows':20}),
 'semantic_title':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'Boundedness of discounted tree sums','limit':10,'fields':'title,authors,year,externalIds,url,citationCount'}),
 'semantic_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2409.01048/citations?fields=title,authors,year,externalIds,url,abstract&limit=100',
 'github_title':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"discounted tree sums"','per_page':30}),
 'github_rays':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"branching random walk" "heavy"','per_page':30}),
}
Path('searches').mkdir(exist_ok=True)
def fetch(item):
 key,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0','Accept':'application/json, application/atom+xml, */*'})
  with urllib.request.urlopen(req,timeout=50) as r: data=r.read().decode('utf-8'); status=r.status
 except Exception as e: data=str(e); status='ERROR'
 Path('searches',key+'.txt').write_text(data,encoding='utf-8')
 entry={'service_query':key,'url':url,'date':datetime.datetime.now().isoformat(),'status':status,'file':'searches/'+key+'.txt'}
 with Path('search_log.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(entry)+'\n')
 print(key,status,len(data),flush=True)
 return key,data,status
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(fetch,queries.items()))
 for key,data,status in results:
  if key=='openalex_title' and status==200:
   js=json.loads(data)
   for w in js['results']:
    print(w['id'],w['title'],w.get('doi'),w.get('cited_by_count'),flush=True)
    if 'boundedness of discounted tree sums' in w['title'].lower():
     fetch(('openalex_citations','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+w['id'].split('/')[-1],'per-page':100})))
