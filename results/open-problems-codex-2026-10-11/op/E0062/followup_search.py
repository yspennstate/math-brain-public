import pathlib,json,urllib.request,concurrent.futures
R=pathlib.Path(__file__).resolve().parent
jobs=[('regularity2011','paper','arXiv:1111.3101','https://arxiv.org/pdf/1111.3101'),
      ('gz2012','paper','arXiv:1205.3841','https://arxiv.org/pdf/1205.3841')]
for wid,count in [('W1544252356',1),('W2081343974',3)]:
    for page in range(1,count+1):
        url=f'https://api.openalex.org/works?filter=cites:{wid}&per-page=100&page={page}&select=id,title,publication_year,doi,authorships,open_access,primary_location,abstract_inverted_index'
        jobs.append((f'citing_{wid}_{page}','OpenAlex',f'works citing {wid}, page {page}',url))
def run(j):
    name,svc,q,url=j
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'}),timeout=50) as r: data=r.read()
        (R/(name+('.pdf' if svc=='paper' else '.response'))).write_bytes(data)
        if svc=='paper':
            import pymupdf
            doc=pymupdf.open(stream=data,filetype='pdf')
            (R/(name+'.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
        outcome=f'OK {len(data)} bytes'
    except Exception as e: outcome=f'ERROR {e}'
    return f'- 2026-10-12; {svc}; query: {q}; URL: {url}; {outcome}\n'
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: results=list(ex.map(run,jobs))
with (R/'LITERATURE.md').open('a',encoding='utf-8') as f:
    f.write('\n## Source citation searches and paper fetches\n\n'+''.join(results))
for s in results: print(s,flush=True)
for p in R.glob('citing*.response'):
    d=json.loads(p.read_text(encoding='utf-8'))
    print(p.name,d.get('meta'))
    for w in d['results']:
        print(w['publication_year'],w['title'],w['doi'],w['open_access'].get('oa_url'))
items={w['id']:w for p in R.glob('openalex*.response') for w in json.loads(p.read_text(encoding='utf-8'))['results']}
print('\nRELEVANT EXACT REFERENCES')
for w in items.values():
    if any(t in w['title'].lower() for t in ['ganikhod','nonergodic','non-ergodic','cesàro','regularity','strange','convex combination of volterra']):
        print(w['title'],w['publication_year'],[a['author']['display_name'] for a in w['authorships']],w['doi'],w['open_access'],w.get('abstract_inverted_index'))
