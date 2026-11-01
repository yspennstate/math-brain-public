import search_literature as s
import urllib.parse as u
import concurrent.futures as c
import xml.etree.ElementTree as E
import pathlib,json
qs=[
 ('second_arxiv_firstpassage','http://export.arxiv.org/api/query?'+u.urlencode({'search_query':'cat:math.PR AND all:"Pitman" AND all:"Tang" AND all:"passage"','max_results':30})),
 ('second_crossref_firstpassage','https://api.crossref.org/works?'+u.urlencode({'query':'first passage patterns waiting time n log n Pitman Tang','rows':20})),
]
with c.ThreadPoolExecutor(max_workers=2) as p:list(p.map(s.fetch,qs))
p=pathlib.Path('second_arxiv_firstpassage.response'); ns={'a':'http://www.w3.org/2005/Atom'}
if p.exists():
 for x in E.fromstring(p.read_bytes()).findall('a:entry',ns):
  print(x.find('a:id',ns).text,x.find('a:title',ns).text,x.find('a:summary',ns).text[:1500])
p=pathlib.Path('second_crossref_firstpassage.response')
if p.exists():
 for x in json.loads(p.read_text())['message']['items'][:15]:print(x.get('title'),x.get('DOI'))
