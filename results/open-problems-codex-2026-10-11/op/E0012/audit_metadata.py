import pathlib,json,xml.etree.ElementTree as ET,subprocess
p=pathlib.Path.cwd()
s=(p/'source.txt').read_text(encoding='utf8'); lines=s.splitlines()
for i,l in enumerate(lines):
 if 'colicin' in l.lower() or 'Problem 6' in l:
  print('\nSOURCE LINE',i+1,'\n','\n'.join(lines[max(0,i-20):i+60]))
ns={'a':'http://www.w3.org/2005/Atom'}
for e in ET.parse(p/'arxiv.json').findall('a:entry',ns):
 print('ARXIV',e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns),e.findtext('a:summary',namespaces=ns))
for w in json.loads((p/'crossref.json').read_text())['message']['items']:
 print('CROSSREF',w.get('title'),w.get('DOI'),w.get('published'),w.get('author'))
for w in json.loads((p/'github.json').read_text())['items']: print('GITHUB',w['full_name'],w.get('description'))
base=pathlib.Path('~/<private-repo>/06_math_research')
for d in list(base.glob('probability_1000_intake_*'))+[base/'codex_pool_2026_10_10']:
 for f in d.rglob('*'):
  if f.is_file() and f.suffix in ('.jsonl','.md'):
   try:
    for line in f.read_text(encoding='utf8').splitlines():
     if 'E0012' in line or 'colicin' in line.lower(): print('PRIOR',str(f),line[:8000])
   except Exception: pass
r=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True)
print('PUBLISHED PATHS','\n'.join(x for x in r.stdout.splitlines() if 'E0012' in x or 'colicin' in x.lower()))
