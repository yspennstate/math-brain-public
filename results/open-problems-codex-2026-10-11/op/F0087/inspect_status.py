from pathlib import Path
import json
P=Path('.')
for w in json.loads((P/'crossref_pinson.json').read_text())['message']['items'][:2]: print(w.get('title'),w.get('author'),w.get('abstract'))
J=json.loads((P/'semantic_kenyon_citations.json').read_text());print('first-page next',J.get('next'),'count',len(J['data']))
for c in J['data']:
 t=c['citingPaper']['title']
 if any(s in t.lower() for s in ['chaos','electric','vertex','gaussian','boson']):print(c['citingPaper'])
