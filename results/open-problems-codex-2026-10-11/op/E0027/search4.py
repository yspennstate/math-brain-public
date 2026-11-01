exec(open('fetch.py',encoding='utf-8-sig').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={'sum_pdf':'https://arxiv.org/pdf/1702.07396','transforms_pdf':'https://arxiv.org/pdf/1903.00050','oa_citing_sum':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':"Hunt’s Hypothesis (H) for the Sum of Two Independent Lévy Processes",'per-page':5})}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(fetch,queries.items()): print(json.dumps(r),flush=True)
