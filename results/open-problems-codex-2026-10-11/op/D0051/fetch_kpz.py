import requests,pathlib,json,datetime,concurrent.futures,pymupdf
from urllib.parse import urlencode
R=pathlib.Path(__file__).resolve().parent
jobs={'kpz':'https://arxiv.org/pdf/1905.11790','openalex_correct_citations':'https://api.openalex.org/works?'+urlencode({'filter':'cites:https://doi.org/10.4171/icm2022/40','per-page':100}),'openalex_correct_source':'https://api.openalex.org/works/https://doi.org/10.4171/icm2022/40'}
def run(it):
 k,u=it
 try:
  r=requests.get(u,timeout=45);(R/(k+('.pdf' if k=='kpz' else '.response'))).write_bytes(r.content);v={'service':k,'url':u,'date':str(datetime.date.today()),'status':r.status_code,'bytes':len(r.content)}
  if k=='kpz' and r.status_code==200:
   d=pymupdf.open(R/'kpz.pdf');(R/'kpz.txt').write_text('\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
 except Exception as e:v={'service':k,'url':u,'error':str(e),'date':str(datetime.date.today())}
 with (R/'search_log.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(v)+'\n')
 print(json.dumps(v),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p:list(p.map(run,jobs.items()))
