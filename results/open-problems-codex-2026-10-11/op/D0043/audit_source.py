from pathlib import Path
import xml.etree.ElementTree as E,json,subprocess
r=Path(__file__).resolve().parent
s=(r/'source.txt').read_text(encoding='utf8'); pos=s.find('Conjecture 5')
print('SOURCE CONTEXT\n',s[max(0,pos-4000):pos+3500],flush=True)
ns={'a':'http://www.w3.org/2005/Atom'}
for fn in ['arxiv.xml','arxiv_exotic.xml']:
 print('\nFILE',fn,flush=True)
 for e in E.parse(r/fn).findall('a:entry',ns):
  print(e.find('a:id',ns).text,e.find('a:title',ns).text,e.find('a:published',ns).text,flush=True)
  if any(w in e.find('a:title',ns).text.lower() for w in ['edge','operator','multicritical','stochastic']):print(e.find('a:summary',ns).text,flush=True)
print('\nCROSSREF',flush=True)
for i in json.loads((r/'crossref.json').read_text(encoding='utf8'))['message']['items']:print(i.get('title'),i.get('DOI'),flush=True)
base=Path('~/<private-repo>/06_math_research')
matches=[]
for d in base.glob('probability_1000_intake_*'):
 for fn in ['problems.jsonl','attempts.jsonl','sources.jsonl']:
  f=d/fn
  if f.exists():
   for line in f.read_text(encoding='utf8').splitlines():
    if 'D0043' in line: matches.append(str(f)+'\n'+line)
(r/'prior_ledger_matches.txt').write_text('\n'.join(matches),encoding='utf8')
print('\nPRIOR LEDGERS', '\n'.join(matches)[:15000],flush=True)
p=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8',timeout=90)
paths=[x for x in p.stdout.splitlines() if 'd0043' in x.lower()]
(r/'prior_repository_paths.txt').write_text('\n'.join(paths),encoding='utf8')
print('REPOSITORY D0043 PATHS', '\n'.join(paths)[:4000],flush=True)
