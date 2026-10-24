import requests,pathlib,json,concurrent.futures
q={'broman_pdf':'https://arxiv.org/pdf/math/0605641','broman_abs':'https://arxiv.org/abs/math/0605641','liggett_steif_pdf':'https://arxiv.org/pdf/math/0504530'}
def f(k,u):
 try:
  r=requests.get(u,timeout=40);pathlib.Path('second_'+k+('.pdf' if r.content.startswith(b'%PDF') else '.txt')).write_bytes(r.content);return {'service':k,'url':u,'date':'2026-10-11','status':r.status_code,'bytes':len(r.content)}
 except Exception as e:return {'service':k,'url':u,'date':'2026-10-11','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:a=list(ex.map(lambda kv:f(*kv),q.items()))
p=pathlib.Path('second_search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+a,indent=2));print(json.dumps(a,indent=2))
