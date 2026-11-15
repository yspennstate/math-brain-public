"""Fetch primary texts and independent OpenAlex records into this workspace."""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from pathlib import Path
import json, subprocess
out=Path('referee_results/literature');out.mkdir(exist_ok=True)
log=[]
def fetch(name,url):
    try:
        r=urlopen(Request(url,headers={'User-Agent':'Independent mathematical referee (local audit)'}),timeout=25)
        data=r.read();out.joinpath(name).write_bytes(data)
        log.append(dict(file=name,url=url,status=r.status,bytes=len(data)))
        print(name,r.status,len(data),flush=True)
        return data
    except Exception as e:
        log.append(dict(file=name,url=url,error=str(e)));print(name,str(e),flush=True)
        return None
def api(name,params):
    data=fetch(name,'https://api.openalex.org/works?'+urlencode(params))
    return json.loads(data) if data else None
chapter=api('chapter_search.json',{'search':'Patterns in random walks and Brownian motion','per-page':30})
thesis=api('thesis_search.json',{'search':'Continuous paths in Brownian motion and related problems','per-page':30})
citers=[]; seeds=[]
for data,needle in ((chapter,'patterns in random walks and brownian motion'),(thesis,'continuous paths in brownian motion and related problems')):
    if data:
        for w in data['results']:
            if w['title'].lower().strip()==needle:
                seeds.append(dict(id=w['id'],title=w['title'],doi=w['doi'],cited_by_count=w['cited_by_count']))
                c=api(w['id'].split('/')[-1]+'_citations.json',{'filter':'cites:'+w['id'].split('/')[-1],'per-page':200})
                if c:
                    for v in c['results']: citers.append(dict(id=v['id'],title=v['title'],doi=v['doi'],year=v['publication_year'],locations=v.get('locations')))
fetch('arxiv_source.pdf','https://arxiv.org/pdf/1411.0041v3')
for name,url in [('argmin','https://arxiv.org/pdf/1610.01524'),('spans','https://arxiv.org/pdf/1506.02021'),('slepian','https://arxiv.org/pdf/1411.0040')]:
    fetch(name+'.pdf',url)
for pdf in out.glob('*.pdf'):
    if pdf.read_bytes().startswith(b'%PDF'):subprocess.run(['/opt/homebrew/bin/pdftotext','-layout',str(pdf),str(pdf.with_suffix('.txt'))],check=True)
out.joinpath('fetch_log.json').write_text(json.dumps(log,indent=2)+'\n')
out.joinpath('citation_summary.json').write_text(json.dumps(dict(seeds=seeds,citers=citers),indent=2)+'\n')
