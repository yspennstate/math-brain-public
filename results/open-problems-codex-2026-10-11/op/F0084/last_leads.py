import research,json,concurrent.futures,pymupdf
q={'hyperuniform_pdf':'https://arxiv.org/pdf/1810.00265',
 'lead_metadata':'https://export.arxiv.org/api/query?id_list=1810.00265,1103.5259,2106.04524&max_results=3'}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex: out=list(ex.map(lambda kv:research.fetch(*kv),q.items()))
p=research.ROOT/'search_log.json';p.write_text(json.dumps(json.loads(p.read_text())+out,indent=2));print(json.dumps(out,indent=2))
try:
 doc=pymupdf.open(research.ROOT/'hyperuniform_pdf.pdf')
 (research.ROOT/'hyperuniform.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+x.get_text() for i,x in enumerate(doc)),encoding='utf8')
except Exception as e:print(e)
