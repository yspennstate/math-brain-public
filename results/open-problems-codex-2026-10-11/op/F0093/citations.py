import json
from pathlib import Path
s=json.loads(Path('semantic_retry.response').read_text())
for x in s.get('data',[]):
 p=x.get('citingPaper',{});t=p.get('title','')
 if any(w in t.lower() for w in ['noise','walk','group','liouville']):print(p)
