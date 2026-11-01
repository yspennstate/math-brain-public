from pathlib import Path
import json,xml.etree.ElementTree as ET
p=Path(__file__).parent
ns={'a':'http://www.w3.org/2005/Atom'}
root=ET.parse(p/'arxiv.txt').getroot()
for e in root.findall('a:entry',ns):
 print('ARXIV',e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns))
j=json.loads((p/'crossref.txt').read_text())
for e in j['message']['items']:
 print('CROSSREF',e.get('title'),e.get('author'),e.get('published'),e.get('DOI'))
import pymupdf
d=pymupdf.open(p/'source.pdf')
for i in [228,229,230,245]:print('SOURCE PDF PAGE',i+1,d[i].get_text())
base=Path('~/<private-repo>/06_math_research')
for directory in list(base.glob('probability_1000_intake_*'))+[base/'codex_pool_2026_10_10']:
 for f in directory.rglob('*.json*'):
  try:
   for line in f.read_text(encoding='utf-8').splitlines():
    if 'P0247' in line:print('LEDGER',str(f),line[:10000])
  except (OSError,UnicodeError):pass
