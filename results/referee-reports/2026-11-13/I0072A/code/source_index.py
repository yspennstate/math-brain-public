#!/usr/bin/env python3
import pathlib,re,json
root=pathlib.Path(__file__).resolve().parents[1]
rows=[]
for p in sorted((root/'sources').glob('*.txt')):
    page=0
    for no,line in enumerate(p.read_text(errors='replace').splitlines(),1):
        m=re.search(r'===== PDF PAGE (\d+) =====',line)
        if m: page=int(m.group(1))
        if re.match(r'\s*(?:Theorem|Corollary|Proposition|Assumption|Problem|Lemma)\s+(?:[0-9]+\.[0-9]+|[0-9]+\b)',line):
            rows.append({'file':p.name,'pdf_page':page,'line':no,'text':line.strip()})
(root/'data'/'source_index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
for row in rows:
    if any(key in row['file'] for key in ['leocata','psy','reaction_2026_v','av_global.txt','flow_dgnm','fmt.txt','cgv.txt']):
        if row['text'].startswith(('Theorem','Corollary','Problem')): print(row['file'],row['pdf_page'],row['text'])
