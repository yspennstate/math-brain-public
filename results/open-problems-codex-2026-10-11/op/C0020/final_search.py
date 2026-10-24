exec(open('targeted_search.py',encoding='utf-8-sig').read().split('with concurrent.futures')[0])
Q={'openalex_citing_retry':'https://api.openalex.org/works?filter=cites:W1590619386&per-page=25',
'arxiv_hex':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"Random-turn hex"','max_results':4}),
'arxiv_cost_exact':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'abs:percolation AND (abs:"algorithmic complexity" OR abs:"computational complexity")','max_results':40})}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rows=list(ex.map(lambda kv:f(*kv),Q.items()))
with (R/'search_log.jsonl').open('a',encoding='utf8') as o:
 for x in rows:o.write(json.dumps(x)+'\n');print(x)
