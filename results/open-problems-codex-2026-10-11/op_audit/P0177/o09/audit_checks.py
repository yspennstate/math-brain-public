from pathlib import Path
import urllib.request, urllib.parse, json, importlib.util

ROOT = Path(__file__).resolve().parent

def fetch(name, url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Independent-mathematical-audit/1.0'})
        with urllib.request.urlopen(req, timeout=45) as response:
            data = response.read()
        (ROOT/name).write_bytes(data)
        print(name, 'OK', len(data), flush=True)
        return data
    except Exception as e:
        print(name, repr(e), flush=True)
        (ROOT/(name+'.error.txt')).write_text(repr(e), encoding='utf-8')

if __name__ == '__main__':
    import sys
    if 'arxiv_source' in sys.argv:
        fetch('arxiv_source.pdf', 'https://arxiv.org/pdf/1710.08240')
    if 'source' in sys.argv:
        data = fetch('published_source.pdf', 'https://alea.math.cnrs.fr/articles/v15/15-15.pdf')
        print('PDF modules:', {m: bool(importlib.util.find_spec(m)) for m in ['pypdf','fitz','sympy','mpmath','scipy']}, flush=True)
        if data:
            import pymupdf
            doc = pymupdf.open(ROOT/'published_source.pdf')
            (ROOT/'published_source.txt').write_text('\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)), encoding='utf-8')
            for i in [3,4,11,14]:
                print(f'PDF PAGE {i+1}\n'+doc[i].get_text(), flush=True)
    if 'search' in sys.argv:
        queries = [('arxiv_modes.xml', 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"free Brownian" AND (all:mode OR all:maximum OR all:location)','max_results':30})),
                   ('arxiv_unimodality.xml', 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:unimodality AND all:Brownian','max_results':40})),
                   ('openalex_modes.json', 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Brownian motion mode location unimodality','per-page':20}))]
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=3) as pool:
            results=list(pool.map(lambda p: (p[0],fetch(*p)), queries))
        import xml.etree.ElementTree as ET
        for name,data in results:
            if not data: continue
            if name.endswith('.xml'):
                root=ET.fromstring(data)
                ns={'a':'http://www.w3.org/2005/Atom'}
                for entry in root.findall('a:entry',ns):
                    print(entry.findtext('a:id',namespaces=ns),entry.findtext('a:title',namespaces=ns),entry.findtext('a:summary',namespaces=ns),flush=True)
            else:
                for work in json.loads(data).get('results',[]):
                    print(work.get('id'),work.get('title'),work.get('publication_year'),flush=True)
