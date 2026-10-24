exec(open('search.py',encoding='utf-8-sig').read().split('with concurrent')[0])
u='https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('(all:"stable allocation" OR all:"stable marriage") AND (all:vacant OR all:unclaimed OR all:percolation)')+'&max_results=100'
r=fetch('arxiv_allocation',u)
old=json.loads((P/'search_log.json').read_text(encoding='utf8'));(P/'search_log.json').write_text(json.dumps(old+[r],indent=2),encoding='utf8');print(r)
if 'status' in r:
 import xml.etree.ElementTree as E
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in E.parse('arxiv_allocation.json').findall('a:entry',ns):print(e.find('a:id',ns).text,e.find('a:title',ns).text)
j=json.loads((P/'semantic_source_citing.json').read_text(encoding='utf8'));print('Source citation count',len(j['data']),'next',j.get('next'))
