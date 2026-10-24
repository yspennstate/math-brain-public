from pathlib import Path
import urllib.request,concurrent.futures,urllib.parse
jobs=[('borodin_rains','https://arxiv.org/pdf/math-ph/0409059'),('finite_determinant_search','https://api.crossref.org/works?query='+urllib.parse.quote('Plancherel growth hitting times joint finite determinant Hammersley')+'&rows=10')]
def f(it):
 n,u=it
 try:
  b=urllib.request.urlopen(u,timeout=35).read();Path(n+('.pdf' if n=='borodin_rains' else '.json')).write_bytes(b);r='OK '+str(len(b))
 except Exception as e:r=str(e)
 return n,u,r
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
 for n,u,r in ex.map(f,jobs):
  with Path('LITERATURE.md').open('a',encoding='utf8') as out:out.write('\n- Continuation 2026-10-11 '+n+': '+u+'\n  Result: '+r+'\n')
  print(n,r)
p=Path('SECOND_ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write('\n\nExact finite validation: finite_block_check.py compared all power-series coefficients through degree 7 with exhaustive uniform permutations and independent Poisson interval compositions. All 15 cases passed, including scalar caps, repeated times, nonmonotone caps, fractional times, a d=0 boundary, and a 14-by-14 matrix for five particles. Output saved in finite_block_checks.json. These checks support signs/time conventions; a full proof is still being completed.\n')
