from pathlib import Path
import json,xml.etree.ElementTree as E,subprocess,requests,concurrent.futures
ns={'a':'http://www.w3.org/2005/Atom'}
for e in E.parse('arxiv_target.xml').findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns))
for file in ['semantic_retry.json','openalex_citing.json']:
 if Path(file).exists():
  o=json.loads(Path(file).read_text(encoding='utf8'))
  for e in o.get('data',o.get('results',[])):
   a=e.get('citingPaper',e);print(file,a.get('title'),a.get('year',a.get('publication_year')),a.get('doi'))
roots=Path('~/<private-repo>/06_math_research')
with open('prior_hits.txt','w',encoding='utf8') as out:
 for d in list(roots.glob('probability_1000_intake_*'))+[roots/'codex_pool_2026_10_10']:
  for p in d.rglob('*'):
   if p.is_file() and p.suffix in ['.jsonl','.md','.json']:
    try:
     for line in p.read_text(encoding='utf8').splitlines():
      if 'E0007' in line:out.write(str(p)+'\n'+line+'\n')
    except (UnicodeError,OSError):pass
 print('prior_hits:',Path('prior_hits.txt').read_text(encoding='utf8')[:16000])
names=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8').stdout
hits=[s for s in names.splitlines() if 'e0007' in s.lower() or 'unequal-death' in s.lower()]
Path('repo_paths.txt').write_text('\n'.join(hits),encoding='utf8');print('repo paths',hits[:30])
for k,u in [('comparison.pdf','https://arxiv.org/pdf/1908.06628'),('neuhauser_metadata.json','https://api.crossref.org/works/10.1007/BF01192067')]:
 try:
  r=requests.get(u,timeout=35);Path(k).write_bytes(r.content);print(k,r.status_code)
 except Exception as e:print(e)
import pymupdf
if Path('comparison.pdf').exists():
 d=pymupdf.open('comparison.pdf');txt='\n'.join('\nPDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d));Path('comparison.txt').write_text(txt,encoding='utf8');print(txt[:23000])
