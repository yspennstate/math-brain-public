exec(open('fetch_literature.py',encoding='utf-8-sig').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
'crossref_math':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':"Hunt hypothesis Levy processes Hu Sun",'rows':30}),
'published_metadata':'https://api.crossref.org/works/10.1007/s10114-021-9343-7',
'openalex_published':'https://api.openalex.org/works/https://doi.org/10.1007/s10114-021-9343-7',
'arxiv_search_html':'https://arxiv.org/search/?'+urllib.parse.urlencode({'query':"Hunt's hypothesis",'searchtype':'all','abstracts':'show','order':'-announced_date_first','size':50}),
'li_pdf':'https://arxiv.org/pdf/2107.06163',
'concentration_pdf':'https://arxiv.org/pdf/2310.03471'}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:results=list(ex.map(fetch,queries.items()))
old=json.loads(pathlib.Path('search_log.json').read_text());old+=results;pathlib.Path('search_log.json').write_text(json.dumps(old,indent=2))
for r in results:print(json.dumps(r))
import pymupdf
for f in ['li_pdf','concentration_pdf']:
 if pathlib.Path(f+'.raw').exists():
  doc=pymupdf.open(stream=pathlib.Path(f+'.raw').read_bytes(),filetype='pdf');pathlib.Path(f+'.txt').write_text('\n'.join(f'PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8');print(f,doc[0].get_text()[:4000])
if pathlib.Path('openalex_published.raw').exists():
 d=json.loads(pathlib.Path('openalex_published.raw').read_text());print('Published OpenAlex',d.get('id'),d.get('cited_by_count'),d.get('title'))
