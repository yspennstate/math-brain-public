from pathlib import Path
import json,xml.etree.ElementTree as ET,re
p=Path(__file__).parent
ns={'a':'http://www.w3.org/2005/Atom'}
for e in ET.parse(p/'arxiv.txt').getroot().findall('a:entry',ns):
 if '2602.21277' in e.findtext('a:id',namespaces=ns):print('WIRED AUTHORS',','.join(a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns)))
for name in ['bht_cover','wired_planar']:
 text=(p/(name+'_full.txt')).read_text(encoding='utf-8')
 print(name,'FIRST',text[:8500])
 for pattern in [r'7\.10',r'last.{0,25}vertex',r'uniform.{0,80}uncovered',r'uncovered.{0,80}uniform']:
  for match in list(re.finditer(pattern,text,re.I))[:6]:print('MATCH',pattern,text[max(0,match.start()-300):match.end()+500])
claims=[json.loads(line) for line in (p/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
print('CLAIMS parsed',len(claims))
for filename in ['computations.json','bound_checks.json','product_search.json']:
 vals=json.loads((p/filename).read_text(encoding='utf-8'));print(filename,len(vals))
print('LEAN RESULT', (p/'lean_check.txt').read_text(encoding='utf-8') if (p/'lean_check.txt').exists() else 'PENDING')
print('LITERATURE LOG END', (p/'LITERATURE.md').read_text(encoding='utf-8')[-4000:])
