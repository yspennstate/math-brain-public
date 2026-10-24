from fetch_status import fetch
import concurrent.futures,urllib.parse,json
q=urllib.parse.quote
queries={
 'arxiv_followup':'http://export.arxiv.org/api/query?search_query='+q('(all:"self-intersection" AND all:"non-backtracking") OR all:"Alon-Peres"')+'&max_results=50&sortBy=submittedDate&sortOrder=descending',
 'openalex_source':'https://api.openalex.org/works?filter=title.search:'+q('Birthday Paradox for non-backtracking')+'&per-page=10',
 'openalex_citing':'https://api.openalex.org/works?filter=cites:doi:https://doi.org/10.48550/arXiv.2608.26321&per-page=50',
 'semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?query='+q('non-backtracking self-intersection')+'&limit=20&fields=title,authors,year,externalIds',
 'github_birthday':'https://api.github.com/search/repositories?q='+q('non-backtracking birthday'),
 'related_pdf':'https://arxiv.org/pdf/2608.09729',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 for result in pool.map(fetch,queries.items()): print(json.dumps(result))
import pymupdf,pathlib
p=pathlib.Path(__file__).resolve().parent
if (p/'related_pdf.txt').exists():
 doc=pymupdf.open(p/'related_pdf.txt')
 (p/'related_source.txt').write_text('\n'.join(page.get_text() for page in doc),encoding='utf8')
