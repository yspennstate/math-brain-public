import requests,pathlib,xml.etree.ElementTree as E
for name,q in [('arxiv_stable','all:"stable maps" AND (all:"walk" OR all:"resistance")'),('arxiv_transience_b','ti:transience AND all:Boltzmann'),('arxiv_kammerer','au:Kammerer AND all:maps')]:
 try:
  r=requests.get('https://export.arxiv.org/api/query',params={'search_query':q,'max_results':60,'sortBy':'submittedDate','sortOrder':'descending'},timeout=35);pathlib.Path('search_'+name+'.txt').write_text(r.text,encoding='utf8')
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- 2026-10-12 arXiv: '+r.url+' HTTP '+str(r.status_code)+' raw search_'+name+'.txt\n')
  ns={'a':'http://www.w3.org/2005/Atom'};print(name,[(e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns)) for e in E.fromstring(r.text).findall('a:entry',ns)])
 except Exception as e:print(name,e)
