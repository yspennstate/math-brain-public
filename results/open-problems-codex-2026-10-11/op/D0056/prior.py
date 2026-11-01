from pathlib import Path
import json,xml.etree.ElementTree as ET,subprocess
r=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:research7_2026-09-17/R7-02/paper_d0059_stable_tail_refutation/main.tex'],capture_output=True,text=True,encoding='utf8')
Path('prior_D0059_readonly.txt').write_text(r.stdout,encoding='utf8')
print(r.stdout[:19000])
d=json.load(open('crossref.json',encoding='utf8'))
for x in d['message']['items']:
 t=' '.join(x.get('title',[]))
 if any(w in t.lower() for w in ['max-type','stable derrida','sustainability']):
  print(json.dumps({k:x.get(k) for k in ['title','author','DOI','published','container-title','volume','issue','page']},ensure_ascii=False))
