import concurrent.futures,urllib.request,pathlib,json
P=pathlib.Path(__file__).parent
urls={
'liggett_modern':'https://projecteuclid.org/journals/annals-of-probability/volume-4/issue-3/Coupling-the-Simple-Exclusion-Process/10.1214/aop/1176996084.pdf',
'liggett_legacy':'https://projecteuclid.org/download/pdf_1/euclid.aop/1176996084',
}
def fetch(item):
 name,url=item
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r: data=r.read();status=r.status
  fn=name+('.pdf' if data.startswith(b'%PDF') else '.txt');(P/fn).write_bytes(data)
  result={'name':name,'url':url,'date':'2026-10-12','status':status,'file':fn,'bytes':len(data)}
  if data.startswith(b'%PDF'):
   import pymupdf
   d=pymupdf.open(P/fn);text='\n'.join('PAGE '+str(i+1)+'\n'+page.get_text() for i,page in enumerate(d))
   (P/(name+'_extracted.txt')).write_text(text,encoding='utf8')
 except Exception as e:result={'name':name,'url':url,'date':'2026-10-12','error':str(e)}
 print(json.dumps(result),flush=True);return result
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:out=list(ex.map(fetch,urls.items()))
(P/'liggett_fetch_log.json').write_text(json.dumps(out,indent=2),encoding='utf8')
