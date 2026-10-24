exec(open('fetch.py',encoding='utf-8-sig').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
 'oa_title':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'title.search:Hunt','search':'hypothesis','per-page':100}),
 'oa_sum':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':"Hunt’s Hypothesis for the sum of two independent Lévy processes",'per-page':15}),
 'cr_sum':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':'Hu Sun Hunt’s hypothesis Lévy processes','rows':50}),
 'arxiv_search':'https://arxiv.org/search/?'+urllib.parse.urlencode({'query':'Hunt hypothesis','searchtype':'all','abstracts':'show','order':'-announced_date_first','size':50}),
 's2_bulk':'https://api.semanticscholar.org/graph/v1/paper/search/bulk?'+urllib.parse.urlencode({'query':'"Hunt" + "hypothesis"','fields':'title,year,authors,externalIds','sort':'publicationDate:desc'}),
 'rao_pdf':'https://www.ams.org/proc/1988-104-02/S0002-9939-1988-0962838-6/S0002-9939-1988-0962838-6.pdf',
 'diffusion_pdf':'https://arxiv.org/pdf/2107.06163'}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 for r in ex.map(fetch,queries.items()): print(json.dumps(r),flush=True)
