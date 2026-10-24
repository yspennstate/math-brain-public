import pathlib,urllib.request,urllib.parse,json,concurrent.futures
R=pathlib.Path(__file__).resolve().parent
jobs=[('saburov2015','paper','Saburov 2015 higher-order means','https://projecteuclid.org/journals/annals-of-functional-analysis/volume-6/issue-4/On-divergence-of-any-order-Ces%c3%a0ro-mean-of-Lotka/10.15352/afa/06-4-247.pdf'),
('degenerate2026','Crossref','DOI 10.1007/s10958-026-08610-0','https://api.crossref.org/works/10.1007/s10958-026-08610-0'),
('springer2026','publisher','DEGENERATE FIXED-POINT CONFIGURATIONS OF A DISCRETE LOTKA–VOLTERRA OPERATOR','https://link.springer.com/article/10.1007/s10958-026-08610-0'),
('gz2025','Crossref','DOI 10.1007/978-3-032-09176-5_9','https://api.crossref.org/works/10.1007%2F978-3-032-09176-5_9')]
for i,q in enumerate(['Volterra quadratic stochastic four cycle zero coefficients ergodic','Volterra ergodic theorem necessary sufficient 2025 2026','Volterra quadratic stochastic operators product Lyapunov four species']):
 jobs.append((f'target_openalex_{i}','OpenAlex',q,'https://api.openalex.org/works?search='+urllib.parse.quote(q)+'&per-page=20'))
def run(j):
 name,svc,q,url=j
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'}),timeout=40) as r: data=r.read()
  (R/(name+('.pdf' if svc=='paper' else '.response'))).write_bytes(data)
  if svc=='paper':
   import pymupdf
   d=pymupdf.open(stream=data,filetype='pdf'); (R/(name+'.txt')).write_text('\n'.join(f'--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d)),encoding='utf-8')
  outcome=f'OK {len(data)} bytes'
 except Exception as e: outcome=f'ERROR {e}'
 return f'- 2026-10-12; {svc}; query: {q}; URL: {url}; {outcome}\n'
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: out=list(ex.map(run,jobs))
with (R/'LITERATURE.md').open('a',encoding='utf-8') as f: f.write('\n## Targeted follow-up\n\n'+''.join(out))
print(''.join(out))
for p in R.glob('target_openalex*.response'):
 for w in json.loads(p.read_text())['results']: print(p.name,w['title'],w['doi'],w['open_access'].get('oa_url'))
for name in ['degenerate2026','gz2025']:
 p=R/(name+'.response')
 if p.exists(): print(name,json.dumps(json.loads(p.read_text())['message'],ensure_ascii=False))
