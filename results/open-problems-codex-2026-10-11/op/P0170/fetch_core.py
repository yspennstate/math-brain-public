from search import fetch
import concurrent.futures,urllib.parse,json
from pathlib import Path
qs={
 'paper_1012_1614':'https://arxiv.org/pdf/1012.1614',
 'paper_1104_1209':'https://arxiv.org/pdf/1104.1209',
 'paper_1204_0543':'https://arxiv.org/pdf/1204.0543',
 'paper_2602_24178':'https://arxiv.org/pdf/2602.24178',
 'openalex_source_direct':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1204.6447',
 'openalex_citing_source':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:doi:10.48550/arXiv.1204.6447','per-page':50}),
 'semantic_bulk':'https://api.semanticscholar.org/graph/v1/paper/search/bulk?'+urllib.parse.urlencode({'query':'"polynomial threshold" "independence"','fields':'title,year,externalIds'}),
}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:list(p.map(fetch,qs.items()))
import pymupdf
for name in qs:
 if not name.startswith('paper'): continue
 try:
  doc=pymupdf.open(name+'.json',filetype='pdf')
  Path(name+'.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
  print(name,doc[0].get_text()[:2000],flush=True)
  for i,p in enumerate(doc):
   text=p.get_text()
   if any(s in text.lower() for s in ['lower bound','necessary','independence fools','k-independent','k-wise independent']):
    if i<8 or name=='paper_1012_1614': print('PAGE',i+1,text[:6500],flush=True)
 except Exception as e:print(name,repr(e),flush=True)
