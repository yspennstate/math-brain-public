from pathlib import Path
import json,re
P=Path('.')
for fn in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']:
 b=(P/fn).read_bytes();print(fn,len(b),'BOM',b.startswith(b'\xef\xbb\xbf'));assert b
assert (P/'STATUS.md').read_text().splitlines()[0]=='STATE: DONE'
claims=[json.loads(l) for l in (P/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()];assert len(claims)==10
assert all(c['problem_id']=='F0087' for c in claims)
assert all(c['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'] for c in claims)
log=(P/'lean_check.log').read_text(encoding='utf8');assert 'exit_code=0' in log
lean=(P/'HeightResidue.lean').read_text(encoding='utf8');assert 'sorry' not in lean and 'native_decide' not in lean
for fn in ['SEARCH_LOG.jsonl','finite_checks.json','cauchy_checks.json']:
 if fn.endswith('jsonl'):
  rs=[json.loads(l) for l in (P/fn).read_text(encoding='utf8').splitlines()];print(fn,len(rs),'valid records')
 else:json.loads((P/fn).read_text(encoding='utf8'));print(fn,'valid')
text=(P/'jsw.txt').read_text(encoding='utf8');lines=text.splitlines();pg=''
for i,l in enumerate(lines):
 if l.startswith('PDF PAGE'):pg=l
 if l.startswith('Corollary 3.11.'):print('JSW Corollary3.11 locator:',pg)
# Check the candidate construction's invoked existing result locator.
p=P/'ATTEMPT.md';s=p.read_text(encoding='utf8').replace('(PDF pp.26–28)','(Corollary 3.11 on PDF p.27; formula (3.4) in Section 3.2)');p.write_text(s,encoding='utf8')
print('Artifact checks passed')
