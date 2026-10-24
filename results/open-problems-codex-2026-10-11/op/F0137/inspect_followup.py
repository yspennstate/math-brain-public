import pathlib,json,xml.etree.ElementTree as ET,fitz
R=pathlib.Path(__file__).resolve().parent
for name in ['perrel','2d']:
 doc=fitz.open(R/(name+'.pdf'))
 pages=[p.get_text() for p in doc]
 (R/(name+'.txt')).write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+t for i,t in enumerate(pages)),encoding='utf8')
 print('\nPAPER',name,'\n',pages[0][:1600])
 for i,t in enumerate(pages):
  if i<12 and any(w in t.lower() for w in ['conjectur','open problem','condition (t','theorem 1','theorem 2']):
   print('\nPAGE',i+1,'\n',t)
print('\nSEMANTIC CITATIONS')
for x in json.loads((R/'semantic_citations.json').read_text())['data']:
 y=x['citingPaper']; print(y['year'],y['title'],y.get('externalIds'),[a['name'] for a in y.get('authors',[])])
print('\nGITHUB RESULTS')
for x in json.loads((R/'github.json').read_text()).get('items',[]): print(x['full_name'],x.get('description'))
ns={'a':'http://www.w3.org/2005/Atom'}
print('\nARXIV FOLLOWUP')
for e in ET.parse(R/'arxiv_T.xml').findall('a:entry',ns):
 print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns))
