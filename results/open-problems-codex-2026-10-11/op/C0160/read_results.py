from pathlib import Path
import json, pymupdf
R=Path(__file__).parent
p=R/'subgroup_pdf_extracted.txt'
if p.exists():
 lines=p.read_text(encoding='utf-8').splitlines()
 for i,line in enumerate(lines):
  if any(s in line.lower() for s in ['monotonicity','schonmann','theorem 1.1','nonunimodular']): print('\n'.join(lines[max(0,i-4):i+12]))
p=R/'github_retry.txt'
if p.exists():
 for x in json.loads(p.read_text(encoding='utf-8')).get('items',[]): print('GITHUB',x['full_name'],x.get('description'))
if (R/'survey.pdf').exists():
 try:
  d=pymupdf.open(R/'survey.pdf')
  for i,p in enumerate(d):
   t=p.get_text()
   if any(s in t.lower() for s in ['monotonicity','quasi-transitive','nonunimodular','harris','kesten','theorem 3.1']): print('PDF PAGE',i+1,'\n',t)
 except Exception as e: print(e)
