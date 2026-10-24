exec(open('search.py',encoding='utf-8-sig').read().split('pathlib.Path(\'LITERATURE.md\').write_text')[0])
queries=[('arxiv_unimodal','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:unimodality AND all:Brownian')+'&max_results=50&sortBy=lastUpdatedDate&sortOrder=descending'),('openalex_doi','https://api.openalex.org/works/https://doi.org/10.30757/ALEA.v15-15'),('openalex_retry','https://api.openalex.org/works?search=Brownian%20unimodality&per_page=30'),('semantic_citations','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1710.08240/citations?fields=title,year,abstract&limit=100'),('openalex_citations','https://api.openalex.org/works?filter=cites:W2765978315&per_page=100')]
exec(open('search.py',encoding='utf-8-sig').read().split('def run(q):')[1].join(['def run(q):','']).split('with concurrent')[0])
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for name,url,result in ex.map(run,queries):
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- '+name+': '+url+'\n  '+result+'\n')
  print(name,result)

