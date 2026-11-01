exec(open('research.py',encoding='utf8').read().split('queries=')[0])
exec('def fetch'+open('research.py',encoding='utf8').read().split('def fetch')[1].split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
 'bremont_quasi_pdf':'https://arxiv.org/pdf/2007.01573',
 'bremont_stratified_pdf':'https://arxiv.org/pdf/1606.00716',
 'gpln_pdf':'https://arxiv.org/pdf/math/0601102',
 'bremont_quasi_abs':'https://arxiv.org/abs/2007.01573',
 'arxiv_since_source':'https://export.arxiv.org/api/query?search_query=(all:%22random%20walk%22%20AND%20all:%22rotation%22)%20AND%20submittedDate:[20260901%20TO%20261013]&max_results=30',
 'openalex_citing_explicit':'https://api.openalex.org/works?filter=cites:doi:10.48550/arXiv.2609.07621&per-page=20',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(lambda kv:fetch(*kv),queries.items()))
(ROOT/'papers_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results: print(json.dumps(r))
import importlib.util
print('PDF modules',[(x,importlib.util.find_spec(x) is not None) for x in ['pymupdf','pypdf','numpy','scipy']])
