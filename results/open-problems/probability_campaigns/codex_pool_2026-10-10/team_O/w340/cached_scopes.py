"""Locate only the named public sources and extract narrowly cited problem clauses."""
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
report=json.loads((ROOT/'SOURCE_REPORT.json').read_text(encoding='utf-8'))
for problem in report:
    report[problem]['ledger_rows']=[x for x in report[problem]['ledger_rows'] if str(x['payload'].get('problem_id',problem)).upper()==problem]
old=Path('~/Downloads/Probability_1000_20h_20260906')
wanted={'P0276','P0109','P0441','P0012','P0038'}
source_ids={}
for name in ['problems.jsonl','attempts.jsonl']:
    path=old/name
    with path.open(encoding='utf-8-sig',errors='replace') as handle:
        for number,line in enumerate(handle,1):
            if not any(pid in line for pid in wanted): continue
            data=json.loads(line)
            pid=data.get('problem_id')
            if pid not in wanted: continue
            if not any(x['path']==str(path) and x['line']==number for x in report[pid]['ledger_rows']):
                report[pid]['ledger_rows'].append({'path':str(path),'line':number,'payload':data})
            if name=='problems.jsonl': source_ids[pid]=data['source_id']

for pid in report:
    for row in report[pid]['ledger_rows']:
        if row['payload'].get('source_id'):
            source_ids.setdefault(pid,row['payload']['source_id'])

registries=[(old/'sources.jsonl',old),(Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/sources.jsonl'),Path('~/Downloads/Probability_1000_intake_claude_20260907'))]
sources={}
for registry,cache in registries:
    with registry.open(encoding='utf-8-sig',errors='replace') as handle:
        for line in handle:
            if not any(value in line for value in source_ids.values()): continue
            data=json.loads(line)
            source_id=data.get('source_id')
            if source_id in source_ids.values(): sources[source_id]=(data,cache)

patterns={
 'P0276':r'Problem\s*2\s*\.\s*4',
 'C0033':r'Conjecture\s*(?:2\s*\.\s*6|5\s*\.\s*3)',
 'C0135':r'(?:Theorem\s*6\s*\.\s*3|Problem\s*6\s*\.\s*4)',
 'P0109':r'Question\s*21',
 'P0441':r'Delayed\s*Off',
 'C0045':r'(?:Open\s*question\s*3\s*\.\s*20)',
 'C0081':r'(?:Open\s*Problem\s*15\s*\.\s*8)',
 'C0123':r'(?:\bbridges?\b|\bislands?\b)',
 'P0012':r'Conjecture\s*16',
 'P0038':r'Conjecture\s*6\s*\.\s*44'
}
scopes={}
for pid,source_id in source_ids.items():
    source,cache=sources[source_id]
    relative=source.get('text_relative_to_downloads',source.get('text_path',''))
    path=cache/relative if relative else cache/'sources'/source_id/'text.txt'
    if not path.is_file():
        candidates=list((cache/'sources'/source_id).glob('*.txt'))
        path=candidates[0] if candidates else path
    info={'source_id':source_id,'source_url':source.get('url',source.get('final_url')),'cached_text_path':str(path),'literature_status':'CURRENT_OPENNESS_UNVERIFIED_OFFLINE','matches':[]}
    if path.is_file():
        text=path.read_text(encoding='utf-8-sig',errors='replace')
        matches=list(re.finditer(patterns[pid],text,re.I))
        if pid in ['P0441','C0123']: matches=matches[-2:]
        else: matches=matches[:3]
        for match in matches:
            lo=max(0,match.start()-100)
            hi=min(len(text),match.end()+650)
            excerpt=text[lo:hi]
            info['matches'].append({'char_offset':match.start(),'line':text.count('\n',0,match.start())+1,'context':excerpt})
    scopes[pid]=info
    print(pid,json.dumps(info,ensure_ascii=False))
(ROOT/'SOURCE_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'CACHED_SOURCE_REPORT.json').write_text(json.dumps(scopes,ensure_ascii=False,indent=2),encoding='utf-8')
