from pathlib import Path
import xml.etree.ElementTree as E,json
r=Path(__file__).resolve().parent
s=(r/'source.txt').read_text(encoding='utf8')
print('SOURCE START',s[:1200])
for word in ['[9]','[31]','[38]']:
 pos=s.rfind(word);print('REFERENCE',word,s[pos:pos+900])
print('MATRIX LAW CONTEXT',s[s.find('PDF PAGE 3'):s.find('PDF PAGE 5')])
ns={'a':'http://www.w3.org/2005/Atom'}
for fn in ['arxiv_higher.xml','arxiv_critical.xml','arxiv_virag.xml']:
 f=r/fn
 if not f.exists():continue
 print('\nFOLLOWUP',fn)
 for e in E.parse(f).findall('a:entry',ns):
  title=e.find('a:title',ns).text
  print(e.find('a:id',ns).text,title,e.find('a:published',ns).text)
  if any(w in title.lower() for w in ['tracy','operator','random matr','edge']): print(e.find('a:summary',ns).text)
for fn in ['openalex_citing.json','crossref_higher.json']:
 f=r/fn
 if f.exists():
  d=json.loads(f.read_text());items=d.get('results',d.get('message',{}).get('items',[]))
  print('\nFOLLOWUP',fn)
  for i in items:print(i.get('title'),i.get('publication_year',i.get('published')),i.get('doi',i.get('DOI')))
