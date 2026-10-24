from pathlib import Path
from urllib.request import urlopen,Request
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import json,xml.etree.ElementTree as ET
jobs={
'notes1993.pdf':'https://www.stat.berkeley.edu/~aldous/Research/OP/patience.pdf',
'paper1999.pdf':'https://www.stat.berkeley.edu/~aldous/Papers/me86.pdf',
'borodin_rains.pdf':'https://arxiv.org/pdf/math-ph/0409059',
'arxiv_drift.xml':'https://export.arxiv.org/api/query?'+urlencode({'search_query':'all:Hammersley AND (all:drift OR all:leftmost OR all:stationary)','max_results':25}),
'arxiv_plancherel.xml':'https://export.arxiv.org/api/query?'+urlencode({'search_query':'all:Plancherel AND (all:"hitting times" OR all:"finite determinant")','max_results':15}),
'openalex.json':'https://api.openalex.org/works?'+urlencode({'search':'Hammersley drift jump stationary','per-page':15}),
'crossref.json':'https://api.crossref.org/works?'+urlencode({'query':'Plancherel growth Hammersley joint stationary finite determinant','rows':10}),
}
def fetch(item):
    name,url=item
    try:
        data=urlopen(Request(url,headers={'User-Agent':'P0220 independent mathematical referee'}),timeout=45).read()
        Path(name).write_bytes(data)
        return {'file':name,'url':url,'bytes':len(data),'success':True}
    except Exception as e:return {'file':name,'url':url,'success':False,'error':str(e)}
with ThreadPoolExecutor(max_workers=7) as pool: results=list(pool.map(fetch,jobs.items()))
from pypdf import PdfReader
for row in results:
    print(json.dumps(row))
    if not row['success']:continue
    f=row['file']
    if f.endswith('.pdf'):
        text='\n'.join(f'\nPDF PAGE {i+1}\n'+(page.extract_text() or '') for i,page in enumerate(PdfReader(f).pages))
        Path(f+'.txt').write_text(text,encoding='utf-8')
        print('extracted',f,len(text))
    elif f.endswith('.xml'):
        root=ET.fromstring(Path(f).read_bytes()); ns={'a':'http://www.w3.org/2005/Atom'}
        for entry in root.findall('a:entry',ns):
            print('ARXIV',entry.findtext('a:id',namespaces=ns),entry.findtext('a:title',namespaces=ns))
            print('ABSTRACT',entry.findtext('a:summary',namespaces=ns))
    elif f=='openalex.json':
        data=json.loads(Path(f).read_bytes())
        for work in data.get('results',[]):print('OPENALEX',work.get('title'),work.get('doi'),work.get('publication_year'))
    elif f=='crossref.json':
        data=json.loads(Path(f).read_bytes())
        for work in data.get('message',{}).get('items',[]):print('CROSSREF',work.get('title'),work.get('DOI'))
Path('literature_requests.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
