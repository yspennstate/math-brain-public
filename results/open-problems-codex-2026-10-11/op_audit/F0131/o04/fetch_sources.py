from pathlib import Path
import concurrent.futures, requests, pymupdf, json
root=Path.cwd()
items={'source':'https://arxiv.org/pdf/0801.3306','pegden':'https://arxiv.org/pdf/1105.0111','random':'https://arxiv.org/pdf/1909.07849','arxiv_search':'https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:holes+OR+all:polygon+OR+all:shape)&max_results=25&sortBy=submittedDate&sortOrder=descending','openalex_search':'https://api.openalex.org/works?search=sandpile%20holes%20polygon%20limiting%20shape&per-page=10'}
def fetch(item):
    name,url=item
    try:
        r=requests.get(url,timeout=70); (root/(name+('.pdf' if name in ('source','pegden','random') else '.response'))).write_bytes(r.content)
        print(name,r.status_code,len(r.content),flush=True)
        if r.status_code==200 and name in ('source','pegden','random'):
            doc=pymupdf.open(stream=r.content,filetype='pdf')
            text='\n'.join('PDF PAGE %d\n%s'%(i+1,p.get_text()) for i,p in enumerate(doc))
            (root/(name+'.txt')).write_text(text,encoding='utf-8')
    except Exception as e: print(name,str(e),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: list(pool.map(fetch,items.items()))
