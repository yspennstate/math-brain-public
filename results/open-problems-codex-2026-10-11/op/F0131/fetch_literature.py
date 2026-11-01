from pathlib import Path
import requests, concurrent.futures, json, datetime
root=Path('.'); (root/'downloads').mkdir(exist_ok=True)
jobs=[('source','https://arxiv.org/pdf/0801.3306'),('arxiv','http://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:holes+OR+all:polygon+OR+all:scaling)&max_results=40'),('openalex','https://api.openalex.org/works?search=sandpile%20holes%20limiting%20shape&per-page=30'),('openalex_source','https://api.openalex.org/works?search=Chip-firing%20and%20rotor-routing%20on%20directed%20graphs&per-page=5'),('crossref','https://api.crossref.org/works?query=sandpile%20holes%20limiting%20shape&rows=25'),('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query=sandpile%20holes%20limiting%20shape&limit=20&fields=title,authors,year,url,abstract'),('github','https://api.github.com/search/repositories?q=sandpile+shape&per_page=20')]
def fetch(job):
 name,url=job
 try:
  r=requests.get(url,timeout=55); ext='pdf' if name=='source' else 'txt'
  (root/'downloads'/f'{name}.{ext}').write_bytes(r.content)
  return {'service':name,'url':url,'date':'2026-10-11','status':r.status_code,'bytes':len(r.content)}
 except Exception as e:return {'service':name,'url':url,'date':'2026-10-11','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 for row in pool.map(fetch,jobs):
  with open('search_log.jsonl','a',encoding='utf8') as f:f.write(json.dumps(row)+'\n')
  print(row)
if (root/'downloads/source.pdf').read_bytes().startswith(b'%PDF'):
 from pypdf import PdfReader
 reader=PdfReader('downloads/source.pdf')
 (root/'downloads/source.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.extract_text() for i,p in enumerate(reader.pages)),encoding='utf8')
