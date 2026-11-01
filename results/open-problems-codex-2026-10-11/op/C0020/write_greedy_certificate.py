import independent_greedy_check as source
from pathlib import Path
import json
rows=[]
for known in range(512):
    ones=known
    while True:
        state=tuple((ones>>i)&1 if known&(1<<i) else -1 for i in range(9))
        rows.append([known,ones,source.opt(state)])
        if not ones:break
        ones=(ones-1)&known
assert len(rows)==3**9
Path(__file__).resolve().with_name('bellman_3x3_certificate.json').write_text(
    json.dumps({'truth':source.f,'states':rows},separators=(',',':')),encoding='utf8')
print('Saved all',len(rows),'ternary states')
