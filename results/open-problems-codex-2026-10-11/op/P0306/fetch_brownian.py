import pathlib,json,urllib.parse
exec(pathlib.Path(__file__).with_name('fetch_literature.py').read_text().split('q = urllib.parse.quote')[0])
query='all:"Brownian disk" AND (all:"star" OR all:"geodesic")'
url='https://export.arxiv.org/api/query?search_query='+urllib.parse.quote(query)+'&max_results=30&sortBy=submittedDate&sortOrder=descending'
print(json.dumps(fetch('arxiv_brownian_boundary',url)),flush=True)
