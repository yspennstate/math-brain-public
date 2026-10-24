import pathlib,json,concurrent.futures
exec(pathlib.Path(__file__).with_name('fetch_literature.py').read_text().split('q = urllib.parse.quote')[0])
ids=['1102.4177','2006.11050','2212.12511','2411.16541']
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:
    for r in p.map(lambda i:fetch('second_lead_'+i,'https://arxiv.org/pdf/'+i),ids):print(json.dumps(r),flush=True)
