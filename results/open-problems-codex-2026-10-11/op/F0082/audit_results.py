from pathlib import Path
p=Path('FiniteChecks.lean');p.write_text(p.read_text(encoding='utf-8-sig'),encoding='utf8')
import json
s=json.load(open('semantic_citations.json',encoding='utf8'));print('keys',s.keys(),'next',s.get('next'))
for d in s.get('data',[]):
 p=d.get('citingPaper',{});print(p.get('year'),p.get('title'),p.get('externalIds'))
for p in json.load(open('crossref_planar.json',encoding='utf8'))['message']['items']:
 print('CROSSREF',p.get('title'),p.get('DOI'))
