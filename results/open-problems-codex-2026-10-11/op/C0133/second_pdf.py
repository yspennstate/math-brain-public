from pathlib import Path
import urllib.request,json,xml.etree.ElementTree as ET
if Path('zerner_openalex.json').exists():
 d=json.loads(Path('zerner_openalex.json').read_text());
 for r in d['results']:
  print(r['title'],r['id'],r.get('doi'));print(json.dumps(r.get('locations'),indent=2)[:7000])
if Path('zerner_arxiv.xml').exists():
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in ET.parse('zerner_arxiv.xml').findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns))
u='https://projecteuclid.org/download/pdf_1/euclid.ecp/1463434786'
try:
 b=urllib.request.urlopen(u,timeout=40).read();Path('zerner2002.pdf').write_bytes(b);print('zerner pdf',len(b));result=[200,len(b)]
except Exception as e:print(e);result=[str(e)]
Path('second_fetch_log.json').write_text(json.dumps({'date':'2026-10-12','queries':{'zerner_pdf':u},'results':result},indent=2))
