import requests,json,pathlib
url='https://api.openalex.org/works/https://doi.org/10.1090/bull/1573'
r=requests.get(url,timeout=40);pathlib.Path('openalex_correct_source.json').write_bytes(r.content)
log=json.loads(pathlib.Path('search_log.json').read_text());log.append(dict(service='openalex_correct_source',url=url,status=r.status_code,date='2026-10-12'))
print(r.status_code,r.text[:400])
if r.status_code==200:
 j=r.json();wid=j['id'].split('/')[-1];url2=f'https://api.openalex.org/works?filter=cites:{wid}&per_page=100';r2=requests.get(url2,timeout=40);pathlib.Path('openalex_correct_citations.json').write_bytes(r2.content);log.append(dict(service='openalex_correct_citations',url=url2,status=r2.status_code,date='2026-10-12'));print('citations',r2.status_code)
pathlib.Path('search_log.json').write_text(json.dumps(log,indent=2))
