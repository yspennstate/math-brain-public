from research import fetch,q,ROOT
import concurrent.futures, json, pymupdf
jobs=[('arxiv_local','https://export.arxiv.org/api/query?search_query='+q('all:"Coulomb gas" AND (all:"local laws" OR all:"high temperature" OR all:"Poissonian")')+'&max_results=80&sortBy=submittedDate&sortOrder=descending'),
('arxiv_debye','https://export.arxiv.org/api/query?search_query='+q('all:"Debye" AND (all:"jellium" OR all:"sharpness" OR all:"Serfaty")')+'&max_results=30'),
('openalex_retry','https://api.openalex.org/works?search='+q('Lectures on Coulomb and Riesz gases')+'&per_page=3'),
('semantic_source','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2407.21194?fields=title,citations.title,citations.year,citations.externalIds'),
('openalex_citing','https://api.openalex.org/works?filter=cites:W4401113170&per-page=100')]
# Last ID is not presumed valid: discard unless source lookup confirms identity.
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    for x in ex.map(lambda x:fetch(*x),jobs): print(json.dumps(x),flush=True)
d=pymupdf.open(ROOT/'source.raw')
with (ROOT/'source_hypotheses.txt').open('w',encoding='utf8') as f:
    for a,b in [(98,100),(106,108),(145,147),(169,171),(285,287),(298,300)]:
        for i in range(a,b): f.write('PDF PAGE '+str(i+1)+'\n'+d[i].get_text()+'\n')
