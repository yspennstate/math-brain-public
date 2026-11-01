import pathlib,json,urllib.request,urllib.parse,concurrent.futures,xml.etree.ElementTree as E
p=pathlib.Path('.')
root=E.fromstring(p.joinpath('search_arxiv.txt').read_text()); ns={'a':'http://www.w3.org/2005/Atom'}
for e in root.findall('a:entry',ns):print(e.find('a:id',ns).text, e.find('a:title',ns).text, e.find('a:summary',ns).text[:140])
d=json.loads(p.joinpath('search_crossref.txt').read_text())
for w in d['message']['items'][:8]:print('CROSSREF',w.get('title'),w.get('DOI'))
urls={
'openalex_retry':'https://api.openalex.org/works?search=Topics%20and%20problems%20on%20favorite%20sites%20of%20random%20walks&per_page=3',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/search?query=Topics%20and%20problems%20on%20favorite%20sites%20of%20random%20walks&limit=5&fields=title,year,externalIds',
'arxiv_boundary':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"random walk" AND (all:"boundary" AND all:"local time")','max_results':40,'sortBy':'submittedDate','sortOrder':'descending'}),
'arxiv_covered':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"disc" AND all:"covered" AND all:"random walk"','max_results':15}),
'crossref_boundary':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'random walk frequently visited sites generalized boundary Okada','rows':15})}
def f(k,u):
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Research contact via public API'}),timeout=35).read();p.joinpath('search_'+k+'.txt').write_bytes(b);return k,u,'OK',len(b)
 except Exception as e:return k,u,'ERROR',str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:r=list(ex.map(lambda t:f(*t),urls.items()))
p.joinpath('search_log2.json').write_text(json.dumps(r,indent=2));print(*r,sep='\n')
