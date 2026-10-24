from pathlib import Path
import json,xml.etree.ElementTree as ET
p=Path('ATTEMPT.md')
t=p.read_text(encoding='utf-8')
t=t.replace('**Theorem 2.** Let n=2m+1 be odd, and let X have the parity-conditioned Gaussian law in Theorem 1 (also valid for n=1).','**Theorem 2.** Let n=2m+1>=3 be odd, and let X have the parity-conditioned Gaussian law in Theorem 1.')
note='The integral formula also extends algebraically to n=1, where parity conditioning makes X half-normal. The n=1 quadrature entry is only a normalization check for the integral; that one-coordinate law is not an admissible standard-Gaussian marginal counterexample.'
if note not in t:t=t.replace('## 3. A self-contained upper bound',note+'\n\n## 3. A self-contained upper bound')
p.write_text(t,encoding='utf-8')
p=Path('LITERATURE.md');t=p.read_text(encoding='utf-8')
t=t.replace('arXiv:2103.07809v2, 2021.','arXiv:2103.07809v2, 9 Feb 2022 (initial arXiv posting 2021).')
p.write_text(t,encoding='utf-8')
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','checks.json','scalar_barrier_checks.json','ParityCheck.lean']:
 assert Path(name).exists() and Path(name).stat().st_size>0
for line in Path('CLAIMS.jsonl').read_text(encoding='utf-8').splitlines():
 r=json.loads(line);assert r['problem_id']=='P0170'
 assert r['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture']
for name in ['checks.json','scalar_barrier_checks.json']:json.loads(Path(name).read_text(encoding='utf-8'))
lean=Path('ParityCheck.lean').read_text(encoding='utf-8')
assert 'sorry' not in lean and 'native_decide' not in lean
assert lean.count('decide +kernel')==4
print('Required files, JSON schemas, and Lean proof-method checks pass.',flush=True)
print('Lean log:',Path('lean_check.log').read_text(encoding='utf-8')[-2000:],flush=True)
ns={'a':'http://www.w3.org/2005/Atom'}
for e in ET.parse('arxiv_api.xml').findall('a:entry',ns):
 id=e.find('a:id',ns).text
 if any(k in id for k in ['2103.14134','2103.07809']):
  print(id,e.find('a:updated',ns).text,flush=True)
