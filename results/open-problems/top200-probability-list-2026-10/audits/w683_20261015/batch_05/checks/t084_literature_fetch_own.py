"""Fetch only named primary sources and bounded recent arXiv metadata."""
from urllib.request import Request,urlopen
from urllib.parse import urlencode
from pathlib import Path
from hashlib import sha256
from datetime import datetime
import json,xml.etree.ElementTree as E

targets=[('https://arxiv.org/pdf/math/0302185','t084_grimmett_winkler.pdf','Negative association in uniform forests and connected graphs','Geoffrey Grimmett; Peter Winkler',2004),('https://arxiv.org/pdf/2603.10738','t084_tang_zhang.pdf','Pairwise Negative Correlation for Uniform Spanning Subgraphs of the Complete Graph','Pengfei Tang; Zibo Zhang',2026)]
query='(all:forest OR all:arboreal) AND (all:"complete graph" OR all:"mean-field") AND submittedDate:[202607170000 TO 202610152359]'
url='https://export.arxiv.org/api/query?'+urlencode({'search_query':query,'max_results':20,'sortBy':'submittedDate','sortOrder':'descending'})
targets.append((url,'t084_recent_own.xml','Recent complete-graph forest metadata screen','arXiv metadata',2026))
records=[]
for url,name,title,authors,year in targets:
    path=Path('papers')/name
    try:
        if path.exists():raw=path.read_bytes()
        else:
            with urlopen(Request(url,headers={'User-Agent':'ProbabilityAudit/1.0'}),timeout=40) as response:raw=response.read(5_000_001)
            assert len(raw)<=5_000_000
            path.write_bytes(raw)
        record={'url':url,'file':str(path),'sha256':sha256(raw).hexdigest(),'title':title,'authors':authors,'year':year,'what you used it for':'Independent prior-work/scope audit of T084 C015-C018','at':datetime.now().astimezone().isoformat()}
        with Path('SOURCES.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(record)+'\n')
        records.append(record)
    except Exception as e:records.append({'url':url,'error':type(e).__name__+': '+str(e)})
Path('checks/t084_literature_own.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf8')
print(json.dumps([{'file':r.get('file'),'bytes':Path(r['file']).stat().st_size if r.get('file') else None,'error':r.get('error')} for r in records]))
