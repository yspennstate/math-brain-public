from search import fetch, P
import json, requests, pymupdf
extra=[
('arxiv_recent','https://export.arxiv.org/api/query',{'search_query':'(all:"self-avoiding" AND (all:"1/d" OR all:"Borel" OR all:"divergent"))','max_results':60,'sortBy':'submittedDate','sortOrder':'descending'}),
('crossref_targeted','https://api.crossref.org/works',{'query.title':'self-avoiding walk connective constant','rows':40}),
('openalex_source_doi','https://api.openalex.org/works/https://doi.org/10.1090/cmp/015/03',{}),
('arxiv_clisby','https://export.arxiv.org/api/query',{'search_query':'ti:"Self-avoiding walk enumeration via the lace expansion"','max_results':5}),
]
log=[fetch(q) for q in extra]
(P/'followup_log.json').write_text(json.dumps(log,indent=2),encoding='utf-8')
for name,aid in [('graham','0911.5163'),('hypercube','2108.03682')]:
 r=requests.get('https://arxiv.org/pdf/'+aid,timeout=40)
 print(name,r.status_code,flush=True)
 if r.status_code==200:
  (P/(name+'.pdf')).write_bytes(r.content)
  doc=pymupdf.open(stream=r.content,filetype='pdf')
  (P/(name+'.txt')).write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
