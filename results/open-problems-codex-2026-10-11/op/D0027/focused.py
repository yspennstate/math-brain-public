from pathlib import Path
import urllib.request,urllib.parse,concurrent.futures,json,xml.etree.ElementTree as E
qs={
'arxiv_gap_title':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"Kinetically constrained spin models"')+'&max_results=20',
'arxiv_fa_title':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"Fredrickson Andersen one spin facilitated model out of equilibrium"')+'&max_results=10',
'arxiv_exp_title':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:Fredrickson AND ti:"Exponential Convergence"')+'&max_results=10',
'crossref_source_title':'https://api.crossref.org/works?query.title='+urllib.parse.quote('Long time behaviour of one facilitated kinetically constrained models results and open problems')+'&rows=5',
'openalex_source_lookup':'https://api.openalex.org/works/https://arxiv.org/abs/2510.20461',
'openalex_citing_source_attempt':'https://api.openalex.org/works?filter=cites:'+urllib.parse.quote('https://arxiv.org/abs/2510.20461',safe='')+'&per-page=100'
}
def fetch(item):
 k,u=item
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathematicalResearch/1.0'}),timeout=40) as r:b=r.read()
  Path(k+'.response').write_bytes(b);return [k,u,'OK',len(b)]
 except Exception as e:
  Path(k+'.response').write_text(str(e),encoding='utf8');return [k,u,'ERROR',str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:rows=list(ex.map(fetch,qs.items()))
j=json.loads(Path('search_log.json').read_text());j['results']+=rows;Path('search_log.json').write_text(json.dumps(j,indent=2),encoding='utf8')
with Path('LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('\n## Further focused retrievals\n\nTwo guessed identifiers (math/0610109 and 1205.4582) proved unrelated on opening their PDFs: Jacobi polynomials and literary-network analysis, respectively. They are excluded from mathematical evidence. Replaced the guesses with exact-title arXiv queries.\n\n')
 for k,u,st,info in rows:f.write(f'- 2026-10-11 — {k}: {u}; {st}: {info}.\n')
for row in rows:
 print(row,flush=True)
 if row[2]=='OK' and row[0].startswith('arxiv'):
  ns={'a':'http://www.w3.org/2005/Atom'};r=E.fromstring(Path(row[0]+'.response').read_bytes())
  for e in r.findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns),flush=True)
