import requests, concurrent.futures, pathlib, json, pymupdf
R=pathlib.Path(__file__).parent
urls={
 'openalex_citations_attempt':'https://api.openalex.org/works?filter=cites:https://doi.org/10.1214/154957806000000096&per-page=100&sort=publication_date:desc',
 'openalex_doi_retry':'https://api.openalex.org/works/doi:10.1214/154957806000000096',
 'semantic_citations':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/154957806000000096/citations?fields=title,authors,year,url&limit=100',
 'arxiv_recent_retry':'https://export.arxiv.org/api/query?search_query=all:percolation+AND+all:uniqueness+AND+all:threshold&sortBy=submittedDate&sortOrder=descending&max_results=20',
 'crossref_schonmann':'https://api.crossref.org/works?query.title=Stability%20of%20infinite%20clusters%20in%20supercritical%20percolation&rows=3',
}
def f(item):
 name,url=item
 try:
  r=requests.get(url,timeout=25); (R/(name+'.txt')).write_text(r.text,encoding='utf-8')
  row={'service':name,'url':url,'date':'2026-10-11','status':r.status_code,'bytes':len(r.content)}
 except Exception as e: row={'service':name,'url':url,'date':'2026-10-11','error':str(e)}
 print(json.dumps(row),flush=True); return row
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: rows=list(ex.map(f,urls.items()))
(R/'final_search_log.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print('SUBGROUP FIRST PAGE',pymupdf.open('subgroup_pdf.pdf')[0].get_text(),flush=True)
for x in json.loads((R/'github_retry.txt').read_text(encoding='utf-8')).get('items',[]): print('GITHUB',x['full_name'],x.get('description'),flush=True)
