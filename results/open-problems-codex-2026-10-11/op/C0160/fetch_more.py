import concurrent.futures, pathlib, requests, json
R=pathlib.Path(__file__).parent
urls={
 'survey_arxiv_search':'https://export.arxiv.org/api/query?search_query=ti:%22Uniqueness%20and%20non-uniqueness%20in%20percolation%20theory%22&max_results=5',
 'survey_euclid_alt':'https://projecteuclid.org/journalArticle/Download?urlId=10.1214%2F154957806000000096',
 'survey_arxiv_html':'https://arxiv.org/html/math/0612812',
 'subgroup_html':'https://arxiv.org/html/2409.12283v1',
 'subgroup_pdf':'https://arxiv.org/pdf/2409.12283',
 'openalex_retry':'https://api.openalex.org/works?search=Uniqueness%20and%20non-uniqueness%20in%20percolation%20theory&per-page=5',
 'github_retry':'https://api.github.com/search/repositories?q=percolation+uniqueness',
}
def f(item):
 name,url=item
 try:
  r=requests.get(url,timeout=25)
  pdf=r.content.startswith(b'%PDF')
  path=R/(name+('.pdf' if pdf else '.txt')); path.write_bytes(r.content)
  row={'service':name,'url':url,'date':'2026-10-11','status':r.status_code,'bytes':len(r.content),'pdf':pdf}
  if pdf:
   import pymupdf
   d=pymupdf.open(path); (R/(name+'_extracted.txt')).write_text('\n'.join(p.get_text() for p in d),encoding='utf-8')
  print(json.dumps(row),flush=True); return row
 except Exception as e:
  row={'service':name,'url':url,'date':'2026-10-11','error':str(e)}; print(json.dumps(row),flush=True); return row
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: rows=list(ex.map(f,urls.items()))
(R/'more_log.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
