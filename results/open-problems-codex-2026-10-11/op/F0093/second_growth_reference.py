import urllib.request,urllib.parse,json
from pathlib import Path
url='https://api.crossref.org/works?query.title='+urllib.parse.quote("The growth of Grigorchuk's torsion group")+'&rows=3'
try:
 data=urllib.request.urlopen(url,timeout=25).read();Path('second_growth_crossref.response').write_bytes(data);j=json.loads(data)
 for x in j['message']['items']:print({k:x.get(k) for k in ['title','author','DOI','page','volume','issue','published','container-title']})
 status='OK'
except Exception as e:status=str(e)
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\n- 2026-10-12 Crossref growth title query: '+url+'; '+status+'\n- Additional read-only brain query: "Bartholdi Grigorchuk growth upper bound 0.767".\n')
s=Path('bartholdi_growth.txt').read_text(encoding='utf8');i=s.index('Theorem 1.1.');j=s.index('2. Growth of Groups',i)
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\n### Bartholdi growth input (not a solution of F0093)\n\nLaurent Bartholdi, *The Growth of Grigorchuk’s Torsion Group*, arXiv:math/0012108, Theorem 1.1, PDF p.1. Exact extracted statement:\n\n```text\n'+s[i:j].strip()+'\n```\n\nThe definition of growth domination on PDF p.1 is gamma(n)<=delta(Cn); hence the theorem gives |B(n)|<=exp(C_prime n^alpha) after absorbing the change of finite generating weights using Lemma 2.1 (PDF p.2). This verifies the external input used by Proposition A4. The result concerns group growth, not endpoint noise sensitivity.\n')
