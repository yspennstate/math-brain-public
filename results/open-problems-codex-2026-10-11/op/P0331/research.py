import urllib.request, urllib.parse, json, concurrent.futures, pathlib, datetime
ROOT=pathlib.Path(__file__).resolve().parent
def fetch(name,url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'})
        with urllib.request.urlopen(req,timeout=45) as r: data=r.read(25000000)
        (ROOT/(name+'.raw')).write_bytes(data)
        result={'name':name,'url':url,'date':str(datetime.date.today()),'bytes':len(data),'status':'ok'}
    except Exception as e: result={'name':name,'url':url,'date':str(datetime.date.today()),'status':str(e)}
    with (ROOT/'search_log.jsonl').open('a',encoding='utf8') as f: f.write(json.dumps(result)+'\n')
    return result
q=urllib.parse.quote
jobs=[('source','https://arxiv.org/pdf/2407.21194'),
('arxiv','https://export.arxiv.org/api/query?search_query='+q('all:"Coulomb" AND (all:"Debye" OR all:"Poisson")')+'&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending'),
('openalex','https://api.openalex.org/works?search='+q('Coulomb Debye Poisson')+'&per-page=30'),
('openalex_source','https://api.openalex.org/works?search='+q('Lectures on Coulomb and Riesz gases')+'&per-page=5'),
('crossref','https://api.crossref.org/works?query='+q('Coulomb gas Debye Poisson')+'&rows=30'),
('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query='+q('Coulomb Debye Poisson')+'&limit=30&fields=title,authors,year,externalIds,abstract'),
('github','https://api.github.com/search/repositories?q='+q('Coulomb Debye'))]
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
        for result in ex.map(lambda x:fetch(*x),jobs): print(json.dumps(result),flush=True)
