exec(open('fetch_literature.py',encoding='utf-8-sig').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
'bhp2026_pdf':'https://arxiv.org/pdf/2608.13976',
'bhp2023_pdf':'https://arxiv.org/pdf/2312.02455',
'bhp2025_pdf':'https://www.aimsciences.org/data/article/export-pdf?id=685bc7da9dd09246775c791d',
'two_theorems_pdf':'https://arxiv.org/pdf/1903.00050'}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:results=list(ex.map(fetch,queries.items()))
old=json.loads(pathlib.Path('search_log.json').read_text());old+=results;pathlib.Path('search_log.json').write_text(json.dumps(old,indent=2))
import pymupdf
for r in results:
 print(r)
 if r['status']=='ok':
  doc=pymupdf.open(stream=pathlib.Path(r['file']).read_bytes(),filetype='pdf');s='\n'.join(f'PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc));pathlib.Path(r['service_query']+'.txt').write_text(s,encoding='utf8');print(doc[0].get_text()[:3000])
