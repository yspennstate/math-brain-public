import pathlib,urllib.parse,json,concurrent.futures
exec(pathlib.Path(__file__).with_name('fetch_literature.py').read_text().split('q = urllib.parse.quote')[0])
queries=[
('second_arxiv_records','all:"Brownian disk" AND (all:geodesics OR all:boundary)'),
('second_arxiv_stars','all:geodesic AND all:boundary AND all:stars'),
('second_arxiv_cactus','all:"Brownian cactus"'),
('second_arxiv_boundaryroot','all:"Brownian disk" AND all:"boundary point"'),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:
    for r in p.map(lambda j:fetch(j[0],'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote(j[1])+'&max_results=40&sortBy=submittedDate&sortOrder=descending'),queries):
        print(json.dumps(r),flush=True)
