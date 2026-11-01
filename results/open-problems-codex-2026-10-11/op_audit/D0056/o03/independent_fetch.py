from pathlib import Path
import urllib.request, concurrent.futures, json, xml.etree.ElementTree as ET
base=Path.cwd()
urls={'source':'https://arxiv.org/pdf/1705.04787','stable':'https://arxiv.org/pdf/2006.06140','survival':'https://arxiv.org/pdf/2108.05610','arxiv_search':'https://export.arxiv.org/api/query?search_query=all:%22Derrida%22+AND+all:%22Retaux%22&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending','openalex':'https://api.openalex.org/works?search=Derrida%20Retaux&per-page=50'}
def fetch(item):
    key,url=item
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Probability-audit/1.0'})
        with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
        suffix='.pdf' if key in ('source','stable','survival') else '.xml' if key=='arxiv_search' else '.json'
        (base/(key+suffix)).write_bytes(data)
        return {'key':key,'url':url,'bytes':len(data),'status':'OK'}
    except Exception as e: return {'key':key,'url':url,'status':repr(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(fetch,urls.items()))
(base/'fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
try:
    import fitz
    for key in ('source','stable','survival'):
        doc=fitz.open(base/(key+'.pdf'))
        texts=[p.get_text() for p in doc]
        (base/(key+'.txt')).write_text('\n'.join(f'PDF PAGE {i+1}\n{t}' for i,t in enumerate(texts)),encoding='utf-8')
        for i in ([0,2,3] if key!='stable' else [0,1,2,3,19,20]):
            if i<len(texts): print(f'EXTRACT {key} PAGE {i+1}\n{texts[i]}')
except Exception as e: print('EXTRACT ERROR',repr(e))
if (base/'arxiv_search.xml').exists():
    root=ET.fromstring((base/'arxiv_search.xml').read_bytes()); ns={'a':'http://www.w3.org/2005/Atom'}
    for e in root.findall('a:entry',ns): print('SEARCH',e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns),e.findtext('a:summary',namespaces=ns))
