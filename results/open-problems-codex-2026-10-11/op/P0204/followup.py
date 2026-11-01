exec(open('search.py',encoding='utf8').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
 'arxiv_target':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:hypercube AND (all:monotone OR all:censoring)')+'&max_results=70&sortBy=submittedDate&sortOrder=descending',
 'arxiv_fei_html':'https://arxiv.org/html/2505.02685v2',
 'arxiv_santos_html':'https://arxiv.org/html/2606.09221v1',
 'arxiv_ding_html':'https://arxiv.org/html/1311.5945v2',
 'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.1214/ECP.v19-3157',
 'openalex_retry':'https://api.openalex.org/works?search='+urllib.parse.quote('Mixing under monotone censoring')+'&per_page=10',
 'semantic_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1311.5945/citations?fields=title,authors,year,externalIds&limit=100',
 'crossref_new':'https://api.crossref.org/works?query='+urllib.parse.quote('spectral expansion monotone subsets hypercube')+'&rows=12',
 'github_broad':'https://api.github.com/search/repositories?q='+urllib.parse.quote('"monotone censoring"'),
}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(fetch,queries.items()))
with (ROOT/'LITERATURE.md').open('a',encoding='utf8') as f:
 for name,url,status,data in results:
  f.write(f'\n- 2026-10-11 | {name} | {url} | {status}; raw response: {name}.txt\n')
  print(name,status,len(data))
  if 'openalex' in name and data: print(data[:5000])
  if name=='semantic_citations' and data: print(data[:14000])
  if name=='crossref_new' and data:
   for w in json.loads(data)['message']['items']: print(w.get('title'),w.get('DOI'))
  if name.endswith('html') and data:
   cleaned=re.sub('<[^>]+>',' ',data)
   cleaned=re.sub(r'\s+',' ',cleaned)
   (ROOT/(name+'_plain.txt')).write_text(cleaned,encoding='utf8')
   print(cleaned[:15000])
