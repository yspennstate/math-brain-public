import xml.etree.ElementTree as E,json
ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv_matching.xml','arxiv_noncross.xml']:
 for e in E.parse(name).getroot().findall('a:entry',ns):
  title=e.find('a:title',ns).text; summary=e.find('a:summary',ns).text
  if any(x in (title+' '+summary).lower() for x in ['holroyd','non-cross','minimal matching','geometric properties']):print(e.find('a:id',ns).text,title,summary)
for e in json.load(open('crossref_minimal.json',encoding='utf8'))['message']['items'][:5]:print(e.get('title'),e.get('DOI'),e.get('author'))
