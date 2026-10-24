from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
folder=Path('~/.codex/worktrees/probability-1000-20h-20260906/06_math_research/probability_1000_20h_20260906')
result={'target':'P0321','record_root':str(folder),'problems':[],'attempts':[],'sources':[]}
for name in ['problems','attempts']:
    path=folder/f'{name}.jsonl'
    if not path.is_file():
        result[name+'_missing']=True
        continue
    with path.open(encoding='utf-8-sig') as stream:
        for line_number,line in enumerate(stream,1):
            if 'P0321' not in line:
                continue
            row=json.loads(line)
            if row.get('problem_id')=='P0321' or row.get('id')=='P0321':
                result[name].append({'line':line_number,'row':row})
source_ids={item['row'].get('source_id') for item in result['problems']}
path=folder/'sources.jsonl'
if path.is_file():
    with path.open(encoding='utf-8-sig') as stream:
        for line_number,line in enumerate(stream,1):
            if not any(source_id and source_id in line for source_id in source_ids):
                continue
            row=json.loads(line)
            if row.get('source_id') in source_ids:
                result['sources'].append({'line':line_number,'row':row})
(ROOT/'ORIGINAL_RECORD.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
