exec(open('search.py',encoding='utf8').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
 'arxiv_csy_html':'https://arxiv.org/html/2506.09852v4',
 'arxiv_csy_metadata':'https://export.arxiv.org/api/query?id_list=2506.09852',
 'arxiv_exact':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"monotone censoring"')+'&max_results=50',
 'crossref_ding':'https://api.crossref.org/works/10.1214/ECP.v19-3157',
 'openalex_citations':'https://api.openalex.org/works?filter=cites:doi:10.1214/ECP.v19-3157&per-page=100',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(fetch,queries.items()))
with (ROOT/'LITERATURE.md').open('a',encoding='utf8') as f:
 for name,url,status,data in results:
  f.write(f'\n- 2026-10-11 | {name} | {url} | {status}; raw response: {name}.txt\n')
  print(name,status,len(data))
  if name.endswith('html') and data:
   cleaned=re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',data))
   (ROOT/(name+'_plain.txt')).write_text(cleaned,encoding='utf8')
   print(cleaned[3000:19000])
  elif name=='arxiv_csy_metadata': print(data)
