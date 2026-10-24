import fitz,xml.etree.ElementTree as E
for name,pages in [('source.pdf',[22,43,44,52,53,56,60]),('budd.pdf',[15,16]),('conditioned.pdf',[1,3])]:
 d=fitz.open(name)
 for p in pages:print('\nDOCUMENT',name,'PDF PAGE',p+1,'\n',d[p].get_text())
r=E.parse('arxiv.xml').getroot(); ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns):
 print('SEARCH HIT',e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),' '.join(e.findtext('a:summary',namespaces=ns).split()))
