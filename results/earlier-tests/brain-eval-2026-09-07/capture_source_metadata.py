"""Pin three already-selected official metadata pages for private source review."""
from pathlib import Path
import argparse
from datetime import datetime,timezone
import hashlib
import json
import time
import urllib.request

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--id',action='append');a=p.parse_args()
    a.output.mkdir(parents=True,exist_ok=False)
    receipts=[]
    for iid in (a.id or ('2601.10624v1','2601.09880v1','2602.08581v2')):
        url='https://arxiv.org/abs/'+iid
        request=urllib.request.Request(url,headers={'User-Agent':'proof-corpus-private-review/1.0'})
        with urllib.request.urlopen(request,timeout=30) as response:
            data=response.read(); code=response.status; final_url=response.url
        dest=a.output/(iid+'.html');dest.write_bytes(data)
        receipts.append({'url':url,'final_url':final_url,'status':code,'path':str(dest.resolve()),
                         'sha256':hashlib.sha256(data).hexdigest(),'observed_at':datetime.now(timezone.utc).isoformat()})
        time.sleep(3.5)
    (a.output/'RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipts,indent=2))

if __name__=='__main__':main()
