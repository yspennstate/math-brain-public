import concurrent.futures
import io
import json
from pathlib import Path
import requests
import pypdf
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent
urls = {
    'source': 'https://arxiv.org/pdf/1107.0158',
    'zhang': 'https://arxiv.org/pdf/math/0301160',
    'mertens': 'https://arxiv.org/pdf/1602.00644',
    'arxiv_search': 'https://export.arxiv.org/api/query?search_query=all%3Apercolation+AND+%28all%3A%22free+energy%22+OR+all%3A%22cluster+number%22+OR+all%3A%22cluster+density%22%29&max_results=40&sortBy=submittedDate&sortOrder=descending',
    'openalex_search': 'https://api.openalex.org/works?search=percolation%20cluster%20number%20singularity&per-page=15',
}
def fetch(item):
    name, url = item
    try:
        r = requests.get(url, timeout=45)
        record = {'name':name, 'url':url, 'status':r.status_code}
        if name in ('source','zhang','mertens') and r.status_code == 200:
            (root/(name+'.pdf')).write_bytes(r.content)
            reader = pypdf.PdfReader(io.BytesIO(r.content))
            pages = [p.extract_text() for p in reader.pages]
            (root/(name+'.txt')).write_text('\n\n'.join(f'PDF PAGE {i+1}\n{t}' for i,t in enumerate(pages)), encoding='utf-8')
            record['pages'] = len(pages)
            if name == 'source':
                record['question_page'] = [{'page':i+1,'text':t} for i,t in enumerate(pages) if 'Question 1.' in t]
            if name == 'zhang':
                record['theorem_pages'] = [{'page':i+1,'text':t} for i,t in enumerate(pages[:7]) if 'Theorem.' in t or 'Remark 2' in t]
            if name == 'mertens':
                record['expansion_page'] = pages[1]
        else:
            (root/(name+'.response')).write_text(r.text, encoding='utf-8')
            if r.status_code == 200 and name == 'arxiv_search':
                tree = ET.fromstring(r.text)
                ns = {'a':'http://www.w3.org/2005/Atom'}
                record['results'] = [{'title':e.findtext('a:title',namespaces=ns), 'id':e.findtext('a:id',namespaces=ns), 'abstract':e.findtext('a:summary',namespaces=ns)} for e in tree.findall('a:entry',ns)]
            elif r.status_code == 200 and name == 'openalex_search':
                record['results'] = [{'title':w.get('title'), 'doi':w.get('doi'), 'year':w.get('publication_year')} for w in r.json().get('results',[])]
        return record
    except Exception as e:
        return {'name':name, 'url':url, 'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fetch, urls.items()))
(root/'literature_checks.json').write_text(json.dumps(results, indent=2, ensure_ascii=False),encoding='utf-8')
for r in results:
    print(json.dumps(r, ensure_ascii=False))
