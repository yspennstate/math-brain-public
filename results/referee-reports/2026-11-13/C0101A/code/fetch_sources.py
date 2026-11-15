"""Fetch PDFs in memory, extract text, retain only text and provenance."""
import io, json, hashlib, urllib.request, datetime, os
from pathlib import Path
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
SOURCES={
 '1611.00411':'https://arxiv.org/pdf/1611.00411',
 '1309.3267':'https://arxiv.org/pdf/1309.3267',
 '1208.4839':'https://arxiv.org/pdf/1208.4839',
 '1708.09432':'https://arxiv.org/pdf/1708.09432',
 '2009.05968':'https://arxiv.org/pdf/2009.05968',
 '2110.07556':'https://arxiv.org/pdf/2110.07556',
 '1502.06284':'https://arxiv.org/pdf/1502.06284',
 '1909.07849':'https://arxiv.org/pdf/1909.07849',
 '1105.0111':'https://arxiv.org/pdf/1105.0111',
 'kalinin2023':'https://amj.math.stonybrook.edu/pdf-Springer-final/023-0224.pdf',
}
if __name__=='__main__':
 manifest=[]
 for key,url in SOURCES.items():
  dest=ROOT/'sources'/f'{key}.txt'
  if dest.exists():
   print(key,'already saved',flush=True); continue
  try:
   blob=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'C0101 research source retrieval'}), timeout=50).read()
   pdf=PdfReader(io.BytesIO(blob))
   pages=[f'\n\n===== PDF PAGE {i+1} =====\n\n'+p.extract_text() for i,p in enumerate(pdf.pages)]
   dest.write_text('Source: '+url+'\nRetrieved: '+datetime.datetime.now().isoformat()+'\n'+''.join(pages))
   row={'id':key,'url':url,'pages':len(pages),'pdf_sha256':hashlib.sha256(blob).hexdigest(),'text_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
   manifest.append(row)
   with (ROOT/'sources'/'manifest.jsonl').open('a') as f: f.write(json.dumps(row)+'\n')
   print(key,len(pages),'pages',flush=True)
  except Exception as e:
   print(key,type(e).__name__,str(e),flush=True)
