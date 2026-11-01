from search import fetch, ROOT, q
import concurrent.futures,json,xml.etree.ElementTree as E
jobs=[
 ('arxiv_general','https://export.arxiv.org/api/query?search_query='+q('all:"random Cayley"')+'&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending'),
 ('arxiv_hildebrand','https://export.arxiv.org/api/query?search_query='+q('ti:"survey" AND au:Hildebrand')+'&max_results=10'),
 ('openalex_source_retry','https://api.openalex.org/works/https://doi.org/10.3150/12-BEJSP09'),
 ('openalex_citing','https://api.openalex.org/works?filter=cites:doi:10.3150/12-BEJSP09&per-page=50'),
 ('semantic_source','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1309.7754?fields=title,year,citations.title,citations.year,citations.externalIds'),
 ('crossref_specific','https://api.crossref.org/works?query.title='+q('mixing random Cayley graphs')+'&rows=25'),
 ('nilpotent_pdf','https://arxiv.org/pdf/2403.12355'),
 ('abelian_pdf','https://arxiv.org/pdf/2102.02809'),
 ('dihedral_pdf','https://arxiv.org/pdf/2510.19942'),
 ('discussion_pdf','https://arxiv.org/pdf/1911.02975')]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(fetch,jobs))
(ROOT/'followup_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
import pymupdf
for name in ['nilpotent','abelian','dihedral','discussion']:
    try:
        doc=pymupdf.open(ROOT/(name+'_pdf.raw'))
        (ROOT/(name+'.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
    except Exception as e: print(name,repr(e))
for name in ['arxiv_general','arxiv_hildebrand']:
    try:
        r=E.fromstring((ROOT/(name+'.raw')).read_text()); ns={'a':'http://www.w3.org/2005/Atom'}
        entries=[]
        for x in r.findall('a:entry',ns):
            entries.append({k:x.find('a:'+k,ns).text for k in ['id','title','summary','published']})
            entries[-1]['authors']=[a.find('a:name',ns).text for a in x.findall('a:author',ns)]
        (ROOT/(name+'.json')).write_text(json.dumps(entries,indent=2),encoding='utf-8')
        print(name,'entries',len(entries))
    except Exception as e: print(name,repr(e))
