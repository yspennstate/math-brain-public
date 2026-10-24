import pathlib,urllib.request,concurrent.futures,pymupdf
r=pathlib.Path(__file__).resolve().parent
def f(pair):
 name,id=pair
 try:
  with urllib.request.urlopen('https://arxiv.org/pdf/'+id,timeout=40) as q:data=q.read(12000000)
  (r/(name+'.pdf')).write_bytes(data)
  doc=pymupdf.open(stream=data,filetype='pdf')
  text='\n'.join('\nPDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc))
  (r/(name+'.txt')).write_text(text,encoding='utf8')
  print(name,id,'pages',len(doc),flush=True)
  for word in ['Conjecture 45','s →+','s → +','right tail','large positive','positive s','[9]']:
   pos=text.find(word)
   if pos>=0:print(word,text[max(0,pos-600):pos+1800],flush=True)
 except Exception as e:print(name,e,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(f,[('KRV','1306.4832'),('CIK','0901.2473')]))
