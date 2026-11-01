from pathlib import Path
import urllib.request,json,concurrent.futures,pymupdf
base='https://projecteuclid.org/journalArticle/Download?urlid=10.1214%2FECP.v7-1060'
qs={'zerner_download':base,'zerner_download_reader':'https://r.jina.ai/'+base,'zerner_correct_pdf':'https://projecteuclid.org/journals/electronic-communications-in-probability/volume-7/issue-none/A-Non-Ballistic-Law-of-Large-Numbers-for-Random-Walks/10.1214/ECP.v7-1060.pdf'}
def f(k,u):
 try:
  r=urllib.request.urlopen(u,timeout=45);b=r.read();reader=k.endswith('reader');Path(k+('.txt' if reader else '.pdf')).write_bytes(b)
  if not reader:
   try:
    doc=pymupdf.open(stream=b,filetype='pdf');s='\n'.join(f'=== PDF PAGE {i+1} ===\n'+pg.get_text() for i,pg in enumerate(doc));Path(k+'.txt').write_text(s,encoding='utf8');return k,r.status,len(b),s[:21000]
   except Exception as e:return k,r.status,len(b),str(e)
  return k,r.status,len(b),b.decode('utf8',errors='replace')[:24000]
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(lambda x:f(*x),qs.items()))
Path('second_download_log.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':[x[:3] for x in rs]},indent=2))
for r in rs:print(r)
