from pathlib import Path
import urllib.request, hashlib, json, datetime
import fitz
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
old=R.parents[0]/'20261011T223137Z-account05-A093-literature-and-priority'/'out'
sources=[
 ('owz11','https://www.math.ias.edu/files/ODonnell_Fourier.pdf',None),
 ('ckls_corrected','https://eccc.weizmann.ac.il/report/2013/052/revision/2/download',old/'ckls_rev2.pdf'),
 ('kms12','https://arxiv.org/pdf/1105.2651v1',None),
 ('han25','https://arxiv.org/pdf/2312.08271v2',None),
 ('gmp26','https://arxiv.org/pdf/2606.00246v2',None),
 ('ckkls18','https://arxiv.org/pdf/1903.11635v1',None),
 ('potapov26','https://arxiv.org/pdf/2609.21563',None),
 ('chang25','https://arxiv.org/pdf/2511.07739v3',None),
]
receipts=[]
for key,url,local in sources:
 try:
  if local and local.exists(): data=local.read_bytes(); acquisition='REUSED_PREVIOUS_HASHED_DOWNLOAD'
  else:
   request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
   data=urllib.request.urlopen(request,timeout=20).read(); acquisition='FETCHED_PRIMARY'
  assert data.startswith(b'%PDF'),key
  (R/'out'/f'{key}.pdf').write_bytes(data)
  with fitz.open(stream=data,filetype='pdf') as doc:
   text='\n'.join(f'\n[[PDF PAGE {i+1}]]\n'+page.get_text() for i,page in enumerate(doc))
   pages=len(doc)
  (R/'out'/f'{key}.txt').write_text(text,encoding='utf-8')
  receipts.append({'key':key,'url':url,'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'acquisition':acquisition,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'pages':pages})
  print(key,pages,hashlib.sha256(data).hexdigest(),flush=True)
 except Exception as e:
  receipts.append({'key':key,'url':url,'error':str(e)})
 (R/'out'/'PRIMARY_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
