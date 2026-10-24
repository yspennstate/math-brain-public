import json
from pathlib import Path

root = Path(__file__).resolve().parent
campaign = Path('~/Downloads/Probability_1000_20h_20260906')
ids = ['P0174','P0389','C0089','P0030','P0234','C0010','C0068','C0101','C0148','P0022']
source_ids = set()
for pid in ids:
    packetpath = root/'reports'/f'{pid}_sources.json'
    packet = json.loads(packetpath.read_text(encoding='utf-8'))
    for name in ['problems.jsonl','attempts.jsonl']:
        path = campaign/name
        if path.is_file():
            for lineno,line in enumerate(path.open(encoding='utf-8-sig'),1):
                if '"'+pid+'"' in line:
                    row = json.loads(line)
                    packet['ledger_rows'].append({'path':str(path),'line':lineno,'record':row})
                    if row.get('source_id'):
                        source_ids.add(row['source_id'])
                    keys=['problem_id','title','statement','source_id','source_locator','locator','current_status','result_status','status_notes','method','result','obstruction','check','independent_check']
                    print('ROW',pid,json.dumps({k:row[k] for k in keys if k in row}, ensure_ascii=False))
    packetpath.write_text(json.dumps(packet,indent=2,ensure_ascii=False),encoding='utf-8')
path = campaign/'sources.jsonl'
selected=[]
if path.is_file():
    for lineno,line in enumerate(path.open(encoding='utf-8-sig'),1):
        row=json.loads(line)
        if row.get('source_id') in source_ids:
            selected.append({'path':str(path),'line':lineno,'record':row})
            print('SOURCE',json.dumps(row,ensure_ascii=False))
(root/'reports'/'campaign_sources.json').write_text(json.dumps(selected,indent=2,ensure_ascii=False),encoding='utf-8')
