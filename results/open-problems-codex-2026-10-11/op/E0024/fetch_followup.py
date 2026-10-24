exec(open('fetch_literature.py',encoding='utf-8-sig').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
'openalex_citations':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:W2968964261','per-page':100}),
'openalex_phrase':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'"Hunt\'s hypothesis"','per-page':100}),
'crossref_phrase':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':"Hunt's hypothesis",'rows':50}),
'arxiv_retry':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Hunt\'s hypothesis"','max_results':30}),
'github_phrase':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"Hunt hypothesis"','per_page':30})}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:results=list(ex.map(fetch,queries.items()))
old=json.loads(pathlib.Path('search_log.json').read_text());old+=results;pathlib.Path('search_log.json').write_text(json.dumps(old,indent=2))
for r in results:print(json.dumps(r))
for fn in ['openalex_citations.raw','openalex_phrase.raw','crossref_phrase.raw']:
 if not pathlib.Path(fn).exists():continue
 d=json.loads(pathlib.Path(fn).read_text());print('FILE',fn)
 for r in d.get('results',d.get('message',{}).get('items',[])):
  t=r.get('title');
  if fn!='crossref_phrase.raw' or 'hunt' in str(t).lower():print(t,r.get('publication_year',r.get('published')),r.get('doi',r.get('DOI')),r.get('id'))
