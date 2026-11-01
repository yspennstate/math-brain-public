import requests,pathlib,pymupdf,json
r=requests.get('https://arxiv.org/pdf/2001.10444',timeout=45); pathlib.Path('regular.pdf').write_bytes(r.content)
d=pymupdf.open('regular.pdf'); pathlib.Path('regular.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
u='https://api.openalex.org/works?search=Quadratic%20stochastic%20operators%20results%20and%20open%20problems&per-page=5'
r=requests.get(u,timeout=40); pathlib.Path('openalex_source.json').write_text(r.text,encoding='utf8')
for x in r.json()['results']: print(x['id'],x['title'],x['cited_by_count'])
