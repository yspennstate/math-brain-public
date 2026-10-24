import xml.etree.ElementTree as E,json
ns={'a':'http://www.w3.org/2005/Atom'}
r=E.parse('arxiv_recent.txt')
print('TOTAL',r.findtext('{http://a9.com/-/spec/opensearch/1.1/}totalResults'))
for e in r.findall('a:entry',ns):
 print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns).replace('\n',' '))
 s=e.findtext('a:summary',namespaces=ns)
 if any(x in s.lower() for x in ['universality','bounded-degree','bounded degree','threshold']):print(s)
for e in json.load(open('crossref_exact.txt',encoding='utf8'))['message']['items']:print(e.get('title'),e.get('DOI'),e.get('published'))
