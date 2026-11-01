import pathlib,concurrent.futures,json
exec(pathlib.Path(__file__).with_name('fetch_literature.py').read_text().split('q = urllib.parse.quote')[0])
jobs=[('lead_'+i,'https://arxiv.org/pdf/'+i) for i in ['2608.22693','2609.27861','2609.17826','2610.10501','2512.09219']]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:
    for r in p.map(lambda j:fetch(*j),jobs): print(json.dumps(r),flush=True)
