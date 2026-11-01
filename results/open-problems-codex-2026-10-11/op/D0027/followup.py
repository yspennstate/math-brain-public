from pathlib import Path
import subprocess,urllib.request,urllib.parse,concurrent.futures,json
paths=Path('prior_repository_paths.txt').read_text().splitlines()
for i,p in enumerate(paths):
 r=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+p],capture_output=True,text=True,encoding='utf8');Path('prior_repo_'+str(i)+'.md').write_text(r.stdout,encoding='utf8');print('PRIOR',p,r.stdout[:14000],flush=True)
queries={
'arxiv_fredrickson':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:Fredrickson')+'&max_results=70&sortBy=submittedDate&sortOrder=descending',
'arxiv_kcm':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"kinetically constrained"')+'&max_results=40&sortBy=submittedDate&sortOrder=descending',
'crossref_precise':'https://api.crossref.org/works?query.title='+urllib.parse.quote('Fredrickson Andersen one spin facilitated relaxation')+'&rows=20',
'openalex_retry':'https://api.openalex.org/works?search='+urllib.parse.quote('Long time behaviour of one facilitated')+'&per_page=5',
'ss_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2510.20461?fields=title,year,externalIds,citationCount',
'github_precise':'https://api.github.com/search/repositories?q='+urllib.parse.quote('"Fredrickson" "Andersen"'),
'spectral_pdf':'https://arxiv.org/pdf/math/0610109',
'fa_2013_pdf':'https://arxiv.org/pdf/1205.4582'
}
def fetch(item):
 k,u=item
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathematicalResearch/1.0'}),timeout=45) as r:b=r.read()
  Path(k+('.pdf' if k.endswith('pdf') else '.response')).write_bytes(b)
  return [k,u,'OK',len(b)]
 except Exception as e:return [k,u,'ERROR',str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:results=list(ex.map(fetch,queries.items()))
j=json.loads(Path('search_log.json').read_text());j['results']+=results;Path('search_log.json').write_text(json.dumps(j,indent=2),encoding='utf8')
for r in results:print(r,flush=True)
