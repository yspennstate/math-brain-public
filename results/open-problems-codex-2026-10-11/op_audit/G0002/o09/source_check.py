from pathlib import Path
import urllib.request, xml.etree.ElementTree as ET, json
R=Path(__file__).resolve().parent
C=Path('~/brain_workers/TRIO_1011/op/G0002')
try:
 import pymupdf as fitz
except ImportError:
 import fitz
d=fitz.open(C/'source_pdf.pdf')
for p in [269,373,391,394,398,453]:
 print('\nSOURCE PDF PAGE',p,flush=True)
 print(d[p-1].get_text(),flush=True)
ns={'a':'http://www.w3.org/2005/Atom'}
t=ET.fromstring((R/'arxiv.txt').read_bytes())
print('\nNEW ARXIV SEARCH TITLES',flush=True)
for e in t.findall('a:entry',ns): print(e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns),flush=True)
print('FRESH SOURCE ABSTRACT TITLE',flush=True)
html=(R/'source_abstract.txt').read_text(encoding='utf-8')
start=html.find('<title>'); print(html[start:start+250],flush=True)
# Download independently and compare content, no reliance on claimant transcription.
try:
 data=urllib.request.urlopen('https://arxiv.org/pdf/2608.23661',timeout=45).read()
 (R/'source_verified.pdf').write_bytes(data)
 fresh=fitz.open(stream=data,filetype='pdf')
 print('FRESH PDF',len(fresh),'pages',flush=True)
 assert all(fresh[p-1].get_text()==d[p-1].get_text() for p in [269,373,391,394,398,453])
 print('FRESH SELECTED PAGES IDENTICAL',flush=True)
except Exception as e: print('FRESH PDF ERROR',str(e),flush=True)
