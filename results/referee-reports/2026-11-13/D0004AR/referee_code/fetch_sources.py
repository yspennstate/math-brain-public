#!/usr/bin/env python3
"""Retrieve primary sources independently; all output stays in referee_sources/."""
from pathlib import Path
import urllib.request
import subprocess
import hashlib
import json
import datetime

root=Path('referee_sources')
papers={
 'wang2011':'https://www.math.uwaterloo.ca/~wang/papers/2011Wang-Wang-JMVA.pdf',
 'wang2016':'https://www.math.uwaterloo.ca/~wang/papers/2015Wang-Wang-MOR.pdf',
 'puccetti2012':'https://www.math.uwaterloo.ca/~wang/papers/2012Puccetti-Wang-Wang-JAP.pdf',
 'puccetti2013':'https://www.math.uwaterloo.ca/~wang/papers/2013Puccetti-Wang-Wang-IME.pdf',
 'mao2015':'https://www.math.uwaterloo.ca/~wang/papers/2015Mao-Wang-JMVA.pdf',
 'koike2024':'https://www.math.uwaterloo.ca/~wang/papers/2024Koike-Lin-Wang-MOR.pdf',
 'mao2019':'https://www.math.uwaterloo.ca/~wang/papers/2019Mao-Wang-Wang-JAP.pdf',
 'mohammed2026':'https://arxiv.org/pdf/2604.17490v4',
 'mutti_semeraro2025':'https://arxiv.org/pdf/2309.17346',
 'komisarski2024':'https://d-nb.info/1313203912/34',
 'wang2015':'https://arxiv.org/pdf/1411.6190',
 'yin_zhu2023':'https://arxiv.org/pdf/1706.05499v4',
 'bellini2016':'https://repository.bilkent.edu.tr/bitstreams/4e7bc6f3-b404-426a-b768-29db24e9fecd/download',
}
manifest=[]
for name,url in papers.items():
    dest=root/(name+'.pdf')
    try:
        if not dest.exists():
            req=urllib.request.Request(url,headers={'User-Agent':'Independent mathematics referee source check'})
            with urllib.request.urlopen(req,timeout=25) as response:
                data=response.read(15000000)
            assert data.startswith(b'%PDF'), (name,data[:60])
            dest.write_bytes(data)
        subprocess.run(['pdftotext','-layout',str(dest),str(dest.with_suffix('.txt'))],check=True)
        manifest.append({'name':name,'url':url,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
                         'bytes':dest.stat().st_size,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
        print(name,'OK',dest.stat().st_size,flush=True)
    except Exception as e:
        manifest.append({'name':name,'url':url,'error':str(e)})
        print(name,'ERROR',str(e),flush=True)
(root/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
