exec(open('fetch.py',encoding='utf-8-sig').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
a=json.loads(Path('oa_published_source.json').read_text())['id'].rsplit('/',1)[1]
b=json.loads(Path('oa_published_sum.json').read_text())['id'].rsplit('/',1)[1]
queries={'oa_citing_published':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+a,'per-page':100}), 'oa_citing_sum_actual':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+b,'per-page':100}), 'cr_sum_exact':'https://api.crossref.org/works/10.1007/s40304-018-0136-y', 'rao_alternate':'https://www.ams.org/journals/proc/1988-104-02/S0002-9939-1988-0962838-6/S0002-9939-1988-0962838-6.pdf'}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(fetch,queries.items()): print(json.dumps(r),flush=True)
