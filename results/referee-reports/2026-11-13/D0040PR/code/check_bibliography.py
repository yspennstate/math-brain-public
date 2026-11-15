"""Save arXiv landing pages and targeted Crossref records as plain text."""
import json,sys,urllib.parse,re
from pathlib import Path
from html.parser import HTMLParser
sys.path.insert(0,str(Path(__file__).parent))
from fetch_sources import get,S
class Plain(HTMLParser):
    def __init__(self): super().__init__(); self.out=[]; self.skip=0
    def handle_starttag(self,t,a):
        if t in ('script','style'): self.skip+=1
        if t in ('p','div','h1','h2','br','li','meta'): self.out.append('\n')
    def handle_endtag(self,t):
        if t in ('script','style'): self.skip-=1
    def handle_data(self,d):
        if not self.skip:self.out.append(d)
    def text(self): return '\n'.join(' '.join(l.split()) for l in ''.join(self.out).splitlines() if l.strip())
ids={'Assiotis':'1609.03764','AN':'1905.08684','BG':'1305.3627','DE':'math-ph/0206043','DF':'0904.2216','GS':'1401.5595','KN':'math/0410034','KRV':'1306.4832','Neretin':'math/0301070','RRV':'math/0607331','VVSine':'1604.04381','VVCirc':'1710.06988','Virag':'1804.06953'}
for key,i in ids.items():
    u='https://arxiv.org/abs/'+i
    try:
        d,t=get(u); p=Plain();p.feed(d.decode());s=p.text();(S/('arxiv_'+key+'.txt')).write_text('Source: '+u+'\n\n'+s)
        print(key, s[:110],flush=True)
    except Exception as e: print(key,e,flush=True)
for key,query in [('KN','Matrix models for circular ensembles Killip Nenciu'),('Virag','Operator limits of random matrices Virag Seoul 2014'),('Trotter','Eigenvalue distributions of large Hermitian matrices Trotter'),('ES','The beta-Jacobi matrix model Edelman Sutton')]:
    u='https://api.crossref.org/works?rows=3&query.bibliographic='+urllib.parse.quote(query)
    try:
        d,t=get(u);o=json.loads(d);(S/('metadata_'+key+'_targeted.json.txt')).write_text(json.dumps({'source_url':u,'crossref':o},indent=2,ensure_ascii=False))
        print(key,[(v.get('title'),v.get('DOI'),v.get('volume'),v.get('page')) for v in o['message']['items']],flush=True)
    except Exception as e: print(key,e,flush=True)
p=S/'metadata_ES_publisher.txt'
if p.exists():
    parser=Plain();parser.feed(p.read_text());p.write_text(parser.text())
