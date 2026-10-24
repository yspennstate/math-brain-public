import urllib.request, urllib.parse, json, pathlib, concurrent.futures, datetime
ROOT=pathlib.Path(__file__).resolve().parent
def fetch(name,url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'F0137-research/1.0','Accept':'*/*'})
        with urllib.request.urlopen(req,timeout=45) as r:
            data=r.read(18000000); status=r.status
        (ROOT/name).write_bytes(data)
        result={'name':name,'url':url,'status':status,'bytes':len(data)}
    except Exception as e: result={'name':name,'url':url,'error':str(e)}
    with (ROOT/'fetch_log.jsonl').open('a',encoding='utf8') as f: f.write(json.dumps({'date':str(datetime.date.today()),**result})+'\n')
    print(json.dumps(result),flush=True)
    return result
if __name__=='__main__':
    q='random walk Dirichlet environment ballisticity'
    jobs=[('source.pdf','https://arxiv.org/pdf/1601.08219'),
      ('arxiv.xml','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Dirichlet environment"','start':0,'max_results':60,'sortBy':'submittedDate','sortOrder':'descending'})),
      ('openalex.json','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':q,'per-page':60})),
      ('crossref.json','https://api.crossref.org/works?'+urllib.parse.urlencode({'query':q,'rows':40})),
      ('semantic.json','https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':q,'limit':50,'fields':'title,year,authors,abstract,url,externalIds'})),
      ('github.json','https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'Dirichlet random walk','per_page':30}))]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: list(ex.map(lambda j:fetch(*j),jobs))
