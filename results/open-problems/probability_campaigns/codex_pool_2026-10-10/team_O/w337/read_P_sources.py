from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parent
BASE=Path('~/Downloads/Probability_1000_20h_20260906')
IDS={'aldous_fill_2014','bilateral_connectivity_2025','grimmett_2022_selected',
     'lyons_peres_20260819','reinforcement_matrix_2023','ot_limit_survey_2026'}
PATTERNS={'aldous_fill_2014':r'Open Problem\s*4\.?\s*30',
 'bilateral_connectivity_2025':r'concentrat|smallest|uniform|independent',
 'grimmett_2022_selected':r'Manhattan|Question\s*3\.?\s*5',
 'lyons_peres_20260819':r'Question\s*3\.?\s*11',
 'reinforcement_matrix_2023':r'(?:Problem|problem)\s*23',
 'ot_limit_survey_2026':r'Problem\s*4'}
records=[]
for line in (BASE/'sources.jsonl').open(encoding='utf-8-sig'):
    record=json.loads(line)
    if record.get('source_id') in IDS:
        records.append(record)
evidence=[]
for record in records:
    sid=record['source_id']
    print('SOURCE '+sid+': '+json.dumps({k:v for k,v in record.items() if k not in ('sha256','extracted_sha256')},ensure_ascii=False)[:2000])
    p=BASE/'sources'/sid/'text.txt'
    if not p.is_file():
        print('DEFAULT CACHED TEXT NOT FOUND')
        continue
    raw=p.read_bytes()
    enc='utf-16' if raw.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8-sig'
    lines=raw.decode(enc).splitlines()
    hits=[i for i,line in enumerate(lines) if re.search(PATTERNS[sid],line,re.I)]
    for i in hits[:3]:
        excerpt='\n'.join(f'{j+1}: {lines[j]}' for j in range(max(0,i-3),min(len(lines),i+13)))
        evidence.append({'source_id':sid,'path':p.as_posix(),'excerpt':excerpt})
        print(excerpt)
for relative in ['proofs/P0209_uniform_clt_counterexample_candidate.md','proofs/Bilateral_degree_fluctuations_partial.md']:
    p=BASE/relative
    if p.is_file():
        lines=p.read_text(encoding='utf-8-sig').splitlines()
        print('PRIOR PROOF '+relative+': '+str(len(lines))+' lines')
        for i,line in enumerate(lines):
            if re.search(r'mean|variance|normaliz|beta|Cauchy|uniform|concentrat',line,re.I):
                print(f'{i+1}: {line[:900]}')
(ROOT/'evidence'/'P_source_excerpts.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
