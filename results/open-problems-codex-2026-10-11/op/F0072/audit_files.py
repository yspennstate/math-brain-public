from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','checks.json','MixtureAlgebra.lean']:
 p=R/name; assert p.exists() and p.stat().st_size>0
 print(name,p.stat().st_size)
claims=[json.loads(line) for line in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if line.strip()]
for c in claims:
 assert c['problem_id']=='F0072'
 assert c['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture']
 assert set(['claim','proof_location','remaining_gap','checks'])<=set(c)
print('Claim records valid:',len(claims))
source=(R/'MixtureAlgebra.lean').read_text(encoding='utf8')
assert 'sorry' not in source and 'native_decide' not in source and 'import Mathlib\n' not in source
p=R/'lean_check.json'
if p.exists():
 x=json.loads(p.read_text(encoding='utf8'))
 print('Latest Lean result',x.get('exit_code'),'hash matches',x.get('source_sha256')==hashlib.sha256((R/'MixtureAlgebra.lean').read_bytes()).hexdigest())
p=R/'crossref_focused.json'
if p.exists():
 print('Crossref focused titles:')
 for x in json.loads(p.read_text(encoding='utf8')).get('message',{}).get('items',[]):
  print(x.get('title'),x.get('DOI'))
p=R/'semantic_source.json'
if p.exists():
 d=json.loads(p.read_text(encoding='utf8'));print('Semantic Scholar citing titles:')
 for x in d.get('citations',[]):
  if any(s in x.get('title','').lower() for s in ['repulsion','convex','continuous','gradient','quadratic']):print(x.get('year'),x.get('title'),x.get('externalIds'))
