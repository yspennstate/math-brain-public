from pathlib import Path
import concurrent.futures, hashlib, json, urllib.request, urllib.parse
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
urls = {
    'source': 'https://arxiv.org/pdf/2608.21125',
    'chen': 'https://arxiv.org/pdf/1402.5864',
    'aidekon': 'https://arxiv.org/pdf/1101.1810',
    'arxiv_search': 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query':'all:"threshold cascades" AND all:"Bramson"','max_results':20}),
    'arxiv_recent': 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query':'all:"threshold cascades" AND submittedDate:[20260821 TO 20261011]','max_results':30}),
    'openalex': 'https://api.openalex.org/works?' + urllib.parse.urlencode({'search':'threshold cascades Bramson','per_page':10}),
}
def fetch(item):
    name, url = item
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'ProbabilityAudit/1.0'})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
            status = r.status
        pdf = data.startswith(b'%PDF')
        path = ROOT / (name + ('.pdf' if pdf else '.txt'))
        path.write_bytes(data)
        if pdf:
            reader = PdfReader(path)
            (ROOT / (name + '_extracted.txt')).write_text('\n'.join(f'\nPAGE {i+1}\n{p.extract_text()}' for i,p in enumerate(reader.pages)), encoding='utf-8')
        return {'name':name,'url':url,'status':status,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    except Exception as e:
        return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results = list(pool.map(fetch, urls.items()))
(ROOT / 'source_checks.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
print(json.dumps(results, indent=2))
