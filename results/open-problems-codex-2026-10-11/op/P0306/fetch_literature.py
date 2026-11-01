import concurrent.futures, datetime, json, pathlib, urllib.request, urllib.parse
ROOT = pathlib.Path(__file__).resolve().parent
def fetch(label, url):
    record = {'service_query': label, 'url': url, 'date': '2026-10-11'}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'ProbabilityResearch/1.0', 'Accept': '*/*'})
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read(12000000)
            record.update(status=r.status, content_type=r.headers.get('Content-Type'), bytes=len(data))
        suffix = '.pdf' if data.startswith(b'%PDF') else '.txt'
        path = ROOT / (label + suffix)
        path.write_bytes(data)
        record['saved'] = path.name
    except Exception as e:
        record['error'] = str(e)
    with (ROOT / 'search_log.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(record) + '\n')
    return record
q = urllib.parse.quote
jobs = [
 ('source_pdf','https://arxiv.org/pdf/2606.10496'),
 ('source_abs','https://arxiv.org/abs/2606.10496'),
 ('arxiv_title','http://export.arxiv.org/api/query?search_query='+q('all:"Dimension lower bounds in random geometry via Lipschitz functions"')+'&max_results=20'),
 ('arxiv_boundary','https://export.arxiv.org/api/query?search_query='+q('all:"Liouville" AND (all:"boundary" AND all:"star")')+'&max_results=40&sortBy=submittedDate&sortOrder=descending'),
 ('openalex_title','https://api.openalex.org/works?search='+q('Dimension lower bounds in random geometry via Lipschitz functions')+'&per-page=15'),
 ('openalex_boundary','https://api.openalex.org/works?search='+q('Liouville boundary geodesic stars')+'&per-page=30'),
 ('crossref_title','https://api.crossref.org/works?query.bibliographic='+q('Dimension lower bounds in random geometry via Lipschitz functions')+'&rows=15'),
 ('crossref_boundary','https://api.crossref.org/works?query='+q('Liouville quantum gravity boundary geodesic star')+'&rows=25'),
 ('semantic_title','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2606.10496?fields=title,authors,year,citationCount,citations.title,citations.year,citations.externalIds'),
 ('semantic_boundary','https://api.semanticscholar.org/graph/v1/paper/search?query='+q('Liouville boundary geodesic stars')+'&limit=20&fields=title,year,authors,externalIds'),
 ('github_boundary','https://api.github.com/search/repositories?q='+q('"Liouville" "boundary"')+'&per_page=30'),
 ('github_source','https://api.github.com/search/repositories?q='+q('"2606.10496"')+'&per_page=20'),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    for r in pool.map(lambda x: fetch(*x), jobs):
        print(json.dumps(r), flush=True)
