import pathlib,json
exec(pathlib.Path(__file__).with_name('fetch_literature.py').read_text().split('q = urllib.parse.quote')[0])
# Source ID lookup was rate limited. Try the DOI alias directly; record any
# validation/rate-limit error, without pretending that citations were searched.
print(json.dumps(fetch('openalex_cites_alias','https://api.openalex.org/works?filter=cites:https://doi.org/10.48550/arXiv.2606.10496&per_page=100')),flush=True)
