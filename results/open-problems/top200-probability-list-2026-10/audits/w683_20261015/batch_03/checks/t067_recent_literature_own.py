"""Bounded primary metadata search; no novelty inference from an empty screen."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from hashlib import sha256
from datetime import datetime
import xml.etree.ElementTree as ET
import json

query='all:Potts AND (all:reconstruction OR all:nonreconstruction) AND submittedDate:[202607170000 TO 202610152359]'
url='https://export.arxiv.org/api/query?'+urlencode({'search_query':query,'start':0,'max_results':20,'sortBy':'submittedDate','sortOrder':'descending'})
out={'at':datetime.now().astimezone().isoformat(),'query':query,'url':url,'max_results':20,'priority':'unverified; bounded screen is not a priority proof'}
try:
    with urlopen(Request(url,headers={'User-Agent':'ProbabilityAudit/1.0'}),timeout=40) as response:
        raw=response.read(2_000_001)
    assert len(raw)<=2_000_000
    path=Path('papers/t067_recent_arxiv_own.xml'); path.write_bytes(raw)
    root=ET.fromstring(raw); ns={'a':'http://www.w3.org/2005/Atom'}
    out['entries']=[{'title':' '.join(e.findtext('a:title',default='',namespaces=ns).split()),'id':e.findtext('a:id',namespaces=ns),'published':e.findtext('a:published',namespaces=ns)} for e in root.findall('a:entry',ns)]
    out['status']='metadata screen completed'
    with Path('SOURCES.jsonl').open('a',encoding='utf8') as f:
        f.write(json.dumps({'url':url,'file':str(path),'sha256':sha256(raw).hexdigest(),'title':'arXiv recent Potts reconstruction metadata search','authors':'arXiv metadata','year':2026,'what you used it for':'Bounded last90day priority screen for T067 degree156; not an exhaustive literature finding'})+'\n')
except Exception as e:
    out.update(status='search unavailable',error=type(e).__name__+': '+str(e))
Path('checks/t067_recent_literature_own.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out))
