import pathlib,json,xml.etree.ElementTree as ET,importlib.util
R=pathlib.Path(__file__).resolve().parent
print('PDF libraries',[(x,bool(importlib.util.find_spec(x))) for x in ['fitz','pypdf']],flush=True)
if importlib.util.find_spec('fitz'):
 import fitz
 for p in R.glob('*.pdf'):
  doc=fitz.open(p)
  (R/(p.stem+'.txt')).write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+pg.get_text() for i,pg in enumerate(doc)),encoding='utf8')
elif importlib.util.find_spec('pypdf'):
 from pypdf import PdfReader
 for p in R.glob('*.pdf'):
  (R/(p.stem+'.txt')).write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+pg.extract_text() for i,pg in enumerate(PdfReader(p).pages)),encoding='utf8')
if (R/'arxiv.xml').exists():
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in ET.parse(R/'arxiv.xml').findall('a:entry',ns):
  print('\nARXIV',e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns),e.findtext('a:title',namespaces=ns), '\n',e.findtext('a:summary',namespaces=ns))
if (R/'crossref.json').exists():
 for x in json.loads((R/'crossref.json').read_text())['message']['items']:
  print('CROSSREF',x.get('title'),x.get('DOI'),x.get('published'))
