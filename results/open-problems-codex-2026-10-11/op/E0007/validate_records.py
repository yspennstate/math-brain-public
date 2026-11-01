from pathlib import Path
import json

status = Path('STATUS.md').read_text(encoding='utf8')
assert status.splitlines()[0] == 'STATE: DONE'
assert 'VERDICT: PARTIAL' in status
lit = Path('LITERATURE.md').read_text(encoding='utf8')
assert 'Final citation check' in lit
assert '2783\u20132820' in lit
assert 'openalex_citing_final.json' in lit
attempt = Path('ATTEMPT.md').read_text(encoding='utf8')
assert '## Final assessment' in attempt
claims = [json.loads(line) for line in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims) == 10
assert all(c['problem_id'] == 'E0007' for c in claims)
assert 'Exit: 0' in Path('lean_check.txt').read_text(encoding='utf8')
checks = json.loads(Path('checks.json').read_text(encoding='utf8'))
assert checks['states_exhaustively_checked'] == 19683
json.loads(Path('simulation.json').read_text(encoding='utf8'))
message = 'Record consistency checks passed: DONE/PARTIAL, 10 claims, Lean exit 0.\n'
Path('record_validation.txt').write_text(message, encoding='utf8')
print(message, end='')
