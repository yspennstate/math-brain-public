from pathlib import Path
import json
j=json.loads(Path('crossref_target.json').read_text())
for x in j['message']['items']:
 if x.get('DOI') in ['10.1007/s00023-020-00898-1','10.3934/dcds.2022029','10.1007/s00039-016-0358-7']:
  print({k:x.get(k) for k in ['title','author','container-title','volume','issue','page','published','DOI']})
t=Path('ellipse.txt').read_text(encoding='utf8');i=t.find('λ1');print(t[i-900:i+1600])
