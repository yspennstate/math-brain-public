from pathlib import Path
import json
base=Path('~/brain_workers/FEI100_20261011')
protocol=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
d=json.loads(protocol.read_text(encoding='utf-8'))
def walk(d):
    if isinstance(d,dict):
        for k,v in d.items():
            if 'fields' in k:print(k,json.dumps(v))
            walk(v)
    elif isinstance(d,list):
        for v in d:walk(v)
walk(d)
old=base/'agents/A017/runs/20261023T115918Z-account03-A017-recursive-addressing'
for fn in ['CLAIMS.json','PROGRESS.json']:
    print(fn,(old/fn).read_text(encoding='utf-8')[:12000])
print('REPORT headings',[x for x in (old/'REPORT.md').read_text(encoding='utf-8').splitlines() if x.startswith('#')])
p=base/'agents/A024/runs/20261023T125238Z-account03-A024-biased-child-stability'
for fn in p.glob('*.md'):
    text=fn.read_text(encoding='utf-8')
    lines=[line for line in text.splitlines() if any(s in line.lower() for s in ['overlap','union','a(f)','unpaid'])]
    print('A024',fn.name,'\n'.join(lines)[:2500])
