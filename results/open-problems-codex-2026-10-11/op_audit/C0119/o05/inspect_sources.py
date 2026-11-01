from pypdf import PdfReader
import xml.etree.ElementTree as ET
for name,pages in [('surface',[8,9]),('source',[37,38])]:
 r=PdfReader(name+'.pdf')
 for p in pages: print('\nFILE',name,'PAGE',p,'\n',r.pages[p-1].extract_text())
r=ET.parse('arxiv_search.txt').getroot();ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns):
 title=' '.join(e.findtext('a:title',namespaces=ns).split());abstract=' '.join(e.findtext('a:summary',namespaces=ns).split())
 print('\nSEARCH',e.findtext('a:id',namespaces=ns),title,'\n',abstract)
