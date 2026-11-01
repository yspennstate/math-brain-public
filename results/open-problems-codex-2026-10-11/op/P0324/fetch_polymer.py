from pathlib import Path
import urllib.request,json
jobs={'polymer_reference.pdf':'https://arxiv.org/pdf/math-ph/0605041','polymer_search.xml':'https://export.arxiv.org/api/query?search_query=au:Fernandez%20AND%20au:Procacci%20AND%20all:polymer&max_results=5'}
out=[]
for name,url in jobs.items():
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'P0324-mathematical-research'}),timeout=30) as r: data=r.read()
  Path(name).write_bytes(data)
  if name.endswith('pdf'):
   import pymupdf
   d=pymupdf.open(name);Path('polymer_reference.txt').write_text('\n'.join(f'--- PDF PAGE {i+1} ---\n'+p.get_text().replace('\x00','') for i,p in enumerate(d)),encoding='utf-8')
  result='OK '+str(len(data))
 except Exception as e: result=str(e)
 out.append(dict(date='2026-10-12',service_file=name,url=url,result=result));print(name,result)
Path('second_search_log.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
