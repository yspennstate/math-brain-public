import fitz,requests,urllib.parse,xml.etree.ElementTree as E
for name,pages in [('source.pdf',[26,47,48]),('budd.pdf',[16]),('conditioned.pdf',[1,3])]:
 d=fitz.open(name)
 for p in pages:print('\nDOCUMENT',name,'PDF PAGE',p+1,'\n',d[p].get_text())
url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"peeling" AND all:"Boltzmann"','max_results':40,'sortBy':'submittedDate','sortOrder':'descending'})
r=requests.get(url,timeout=55);r.raise_for_status();open('arxiv_boltzmann.xml','w',encoding='utf8').write(r.text)
ns={'a':'http://www.w3.org/2005/Atom'}
for e in E.fromstring(r.content).findall('a:entry',ns):
 print('SEARCH HIT',e.findtext('a:id',namespaces=ns),' '.join(e.findtext('a:title',namespaces=ns).split()),' '.join(e.findtext('a:summary',namespaces=ns).split()))
