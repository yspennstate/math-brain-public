import pathlib,pymupdf,xml.etree.ElementTree as E
p=pymupdf.open('rolla.pdf')
for i in range(27,32): print('PAGE',i+1, p[i].get_text())
r=E.parse('arxiv_http.xml'); ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns): print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns))
