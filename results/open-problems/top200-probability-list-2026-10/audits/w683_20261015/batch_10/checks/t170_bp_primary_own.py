from pathlib import Path
from urllib.request import Request,urlopen
from hashlib import sha256
import json,fitz
root=Path(__file__).resolve().parent.parent
url='https://arxiv.org/pdf/1705.08143v2';p=root/'papers/t170_bp1705.08143v2.pdf'
if p.exists():raw=p.read_bytes()
else:
    with urlopen(Request(url,headers={'User-Agent':'ProbabilityAudit/1.0'}),timeout=25) as r:raw=r.read(8000001)
    assert len(raw)<=8000000 and raw.startswith(b'%PDF');p.write_bytes(raw)
doc=fitz.open(p);out=root/'papers/t170_bp1705.08143v2.txt'
out.write_text('\n'.join(f'\n=== PDF PAGE{i+1} ===\n'+page.get_text() for i,page in enumerate(doc)),encoding='utf8')
record={'url':url,'file':str(p.relative_to(root)),'sha256':sha256(raw).hexdigest(),'title':"Dimension improvement in Dhar's refutation of the Eden conjecture",'authors':['Quentin Bertrand','Jules Pertinand'],'year':2017,'what you used it for':'D16 primary comparison: unidirectional model, slab recursion/terminal data and earlier numerical dimension threshold'}
with (root/'SOURCES.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(record)+'\n')
(root/'checks/t170_bp_primary_own.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print('Primary PDF fetched and hashed;pages',len(doc),'bytes',len(raw))
