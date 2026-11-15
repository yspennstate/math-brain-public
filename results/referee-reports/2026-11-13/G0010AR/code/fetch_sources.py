"""Fetch primary-source PDF bytes in RAM and retain only extracted text."""
import hashlib, json, os, subprocess, urllib.request
from pathlib import Path
os.environ.update(OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
SOURCES = {
 'CMW_2608.19145v1': 'https://arxiv.org/pdf/2608.19145v1',
 'DEKK_2209.03722v3': 'https://arxiv.org/pdf/2209.03722v3',
}
if __name__ == '__main__':
    records=[]
    for name,url in SOURCES.items():
        req=urllib.request.Request(url,headers={'User-Agent':'Independent mathematical referee source verification'})
        with urllib.request.urlopen(req,timeout=90) as r: raw=r.read()
        assert raw.startswith(b'%PDF'), (url,raw[:100])
        proc=subprocess.run(['pdftotext','-layout','-','-'],input=raw,capture_output=True,check=True)
        content=proc.stdout.decode('utf-8')
        Path('sources',name+'.txt').write_text(content)
        record=dict(name=name,url=url,pdf_sha256=hashlib.sha256(raw).hexdigest(),text_sha256=hashlib.sha256(proc.stdout).hexdigest(),pages=content.count('\f'),pdf_bytes=len(raw))
        records.append(record)
        print(record,flush=True)
    Path('sources/download_manifest.txt').write_text(json.dumps(records,indent=2)+'\n')
