from collections import deque
import json
from pathlib import Path
import re

root=Path(__file__).resolve().parent
base=Path('~/Downloads/Probability_1000_intake_claude_20260907/sources')
jobs=[('levine_peres_sandpiles_2017',r'Gamma|Γ|superharmonic|are they isolated'),('heydenreich_hofstad_highd_2017',r'Open Problem 13\.2|Open Problem 16\.7|right.derivative'),('biskup_dgff_extrema_2020',r'Problem 16\.10|ergodic.*conductance')]
receipts=[]
for source,pattern in jobs:
    path=base/source/'text.txt'
    receipt={'path':str(path),'matches':[]}
    regex=re.compile(pattern,re.I)
    preceding=deque(maxlen=2)
    after=0;count=0
    with path.open(encoding='utf-8-sig',errors='replace') as stream:
        for lineno,line in enumerate(stream,1):
            if lineno<=3:
                print('FORMAT',source,lineno,repr(line[:160]))
            if regex.search(line) and count<8:
                text=''.join(preceding)+line
                receipt['matches'].append({'line':lineno,'text':text[:1800]})
                print('MATCH',source,lineno,text[:1800])
                count+=1;after=2
            elif after:
                print('AFTER',source,lineno,line[:500])
                receipt['matches'][-1]['text']+=line[:500]
                after-=1
            preceding.append(line)
    receipts.append(receipt)
(root/'reports/cached_source_excerpts.json').write_text(json.dumps(receipts,indent=2,ensure_ascii=False),encoding='utf-8')
