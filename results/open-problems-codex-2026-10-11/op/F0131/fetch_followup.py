from pathlib import Path
import requests,concurrent.futures,json
from pypdf import PdfReader
jobs=[('pegden_smart','https://arxiv.org/pdf/1105.0111'),('apollonian','https://arxiv.org/pdf/1208.4839'),('matrices','https://arxiv.org/pdf/1309.3267'),('survey','https://arxiv.org/pdf/1611.00411'),('boundary','https://arxiv.org/pdf/1607.01525'),('arxiv_target','https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:background+OR+all:polygon+OR+all:shape)&max_results=80&sortBy=submittedDate&sortOrder=descending'),('crossref_target','https://api.crossref.org/works?query.title=Chip-firing%20and%20rotor-routing%20on%20directed%20graphs&rows=5'),('openalex_retry','https://api.openalex.org/works?search=Chip-firing%20and%20rotor-routing%20on%20directed%20graphs&per_page=5'),('semantic_source','https://api.semanticscholar.org/graph/v1/paper/ARXIV:0801.3306?fields=title,citations.title,citations.year,citations.externalIds'),('github_target','https://api.github.com/search/repositories?q=abelian+sandpile&per_page=30')]
def fetch(j):
 name,url=j
 try:
  r=requests.get(url,timeout=50); pdf=r.content.startswith(b'%PDF');path=Path('downloads')/(name+('.pdf' if pdf else '.txt'));path.write_bytes(r.content)
  if pdf:Path('downloads',name+'.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.extract_text() for i,p in enumerate(PdfReader(path).pages)),encoding='utf8')
  return dict(service=name,url=url,date='2026-10-11',status=r.status_code,bytes=len(r.content))
 except Exception as e:return dict(service=name,url=url,date='2026-10-11',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 for row in pool.map(fetch,jobs):
  with open('search_log.jsonl','a',encoding='utf8') as f:f.write(json.dumps(row)+'\n')
  print(row)
