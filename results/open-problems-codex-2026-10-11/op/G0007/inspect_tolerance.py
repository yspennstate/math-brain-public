import xml.etree.ElementTree as E,json
ns={'a':'http://www.w3.org/2005/Atom'}
for fn in ['arxiv_critical_tree.txt','arxiv_tolerance.txt']:
 print(fn)
 for e in E.parse(fn).findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns))
for x in json.load(open('crossref_tolerance.txt',encoding='utf8'))['message']['items']:print(x.get('title'),x.get('DOI'))
