exec(open('fetch.py',encoding='utf-8-sig').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={'concentration_pdf':'https://arxiv.org/pdf/2310.03471','bhp_survey_pdf':'https://www.aimsciences.org/data/article/export-pdf?id=685bc7da9dd09246775c791d','bhp_search':'https://arxiv.org/search/?'+urllib.parse.urlencode({'query':'Boundary Harnack principle for nonlocal operators on metric measure spaces','searchtype':'title','abstracts':'show','size':50})}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(fetch,queries.items()): print(json.dumps(r),flush=True)
