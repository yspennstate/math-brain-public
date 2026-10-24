import pathlib, urllib.request, pymupdf, concurrent.futures,json
ROOT=pathlib.Path(__file__).resolve().parent
def fetch(ident):
 url='https://arxiv.org/pdf/'+ident
 try:
  with urllib.request.urlopen(url,timeout=35) as resp: data=resp.read()
  (ROOT/(ident+'.pdf')).write_bytes(data)
  doc=pymupdf.open(stream=data,filetype='pdf')
  (ROOT/(ident+'.txt')).write_text('\n'.join(p.get_text() for p in doc),encoding='utf-8')
  return {'url':url,'status':'OK'}
 except Exception as e: return {'url':url,'status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: results=list(ex.map(fetch,['0711.0503','1107.3227','2208.10699']))
(ROOT/'leads_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(results)
