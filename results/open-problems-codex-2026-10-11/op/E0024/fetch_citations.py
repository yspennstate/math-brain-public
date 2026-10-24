exec(open('fetch_literature.py',encoding='utf-8-sig').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
results=[fetch(('openalex_published_citations','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:W3121518416','per-page':100})))]
old=json.loads(pathlib.Path('search_log.json').read_text());old+=results;pathlib.Path('search_log.json').write_text(json.dumps(old,indent=2));print(results)
if pathlib.Path('openalex_published_citations.raw').exists():
 for r in json.loads(pathlib.Path('openalex_published_citations.raw').read_text())['results']:print(r['title'],r['publication_year'],r.get('doi'),r.get('primary_location'))
