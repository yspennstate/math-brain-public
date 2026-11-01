from pathlib import Path
import json,re
root=Path(__file__).resolve().parent
claims=[json.loads(x) for x in (root/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for c in claims:
 assert c['problem_id']=='F0084'
 assert c['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'}
assert 'sorry' not in (root/'FlowCheck.lean').read_text()
assert 'native_decide' not in (root/'FlowCheck.lean').read_text()
assert not re.search(r'^\s*axiom\b',(root/'FlowCheck.lean').read_text(),re.M)
assert (root/'matching_journal_pdf.pdf').stat().st_size>1000000
assert (root/'second_checks.json').exists()
required=['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','SECOND_ATTEMPT.md','SOLUTION.md']
assert all((root/f).exists() for f in required)
print(json.dumps({'claims':len(claims),'second_requests':json.loads((root/'second_search_log.json').read_text()),'record_validation':'passed'},indent=2))
