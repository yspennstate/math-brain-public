from pathlib import Path
import json, hashlib, re

root = Path(__file__).resolve().parent
lean_receipt = (root/'kalikow_lean_check.txt').read_text(encoding='utf-8')
assert lean_receipt.startswith('exit_code=0'), lean_receipt
source = (root/'KalikowObstruction.lean').read_text(encoding='utf-8')
assert len(re.findall(r'^theorem ', source, re.M)) == 8
assert 'sorry' not in source and 'native_decide' not in source and 'axiom ' not in source
assert (root/'brain_gap_recall.txt').is_file()
assert (root/'brain_kalikow_recall.txt').is_file()
assert json.loads((root/'kalikow_closed_form.json').read_text())['left_pair_auxiliary_drift'][0] == '-5/22'
assert len(json.loads((root/'kalikow_probe.json').read_text())['family_exact_rational_tests']) == 100

for name in ('walk_probe.json', 'ballistic_control_probe.json'):
    result = json.loads((root/name).read_text())
    assert result['trials'] == 20 and result['steps_per_trial'] == 20000
    assert len({p['seed'] for p in result['paths']}) == 20
    for path in result['paths']:
        assert path['visited_sites'] <= 20000
        for n, obs in path['observed'].items():
            coords = obs.get('position', [obs.get('x'), obs.get('y')])
            assert sum(abs(x) for x in coords) <= int(n)
            assert sum(coords) % 2 == int(n) % 2

claims_path = root/'CLAIMS.jsonl'
claims = [json.loads(row) for row in claims_path.read_text(encoding='utf-8').splitlines() if row.strip()]
assert len(claims) == 14
assert all(c['problem_id'] == 'F0136' for c in claims)
for c in claims:
    if c['proof_location'].startswith('SECOND_ATTEMPT.md A2-A3') or c['proof_location'].startswith('SECOND_ATTEMPT.md A4'):
        c['checks'] += ' Corrected KalikowObstruction.lean passed with exit code 0; its eight theorems verify finite algebra/sign implications only.'
claims_path.write_text(''.join(json.dumps(c, ensure_ascii=False)+'\n' for c in claims), encoding='utf-8')

status_path = root/'STATUS.md'
lines = status_path.read_text(encoding='utf-8').splitlines()
assert lines[0] == 'STATE: WORKING'
lines[0] = 'STATE: DONE'
lines[1] = 'NEXT: Future work must prove quantitative finite-box clock growth and sufficiently strong regeneration-range tails without assuming Kalikow or (T)_gamma.'
lines += [
    '2026-10-11: Corrected KalikowObstruction.lean passed with exit code 0; eight finite algebra/sign theorems checked by the kernel. Initial timeout and reserved-keyword failure receipts retained.',
    '2026-10-11: Closed the requested additional attempt as DONE / PARTIAL. Two new approaches were written down and pursued: the universal Kalikow route was refuted by exact auxiliary-kernel computations, and the range/clock route was reduced to unproved quantitative inputs. F0136 itself remains unproved and no zero-speed counterexample is obtained.'
]
status_path.write_text('\n'.join(lines)+'\n', encoding='utf-8')

with (root/'SECOND_ATTEMPT.md').open('a', encoding='utf-8') as f:
    f.write('\n## Completed verification\n\n'
            'KalikowObstruction.lean passed `lake env lean` from ~/lean_verify with exit code 0. '
            'It contains eight finite arithmetic/sign theorems, including the exact -133/4779 prefix and the normalized -5/22 and 7/22 values. '
            'No placeholders, added axioms or native_decide are present. The kernel checks algebra only; the Dirichlet and beta-integral identities are the full prose proofs above. '
            'The first run timed out; the next exposed the reserved identifier prefix, which was renamed. All receipts are retained.\n\n'
            'The exact 100-point rational family probe and both finite-walk data sets passed their consistency checks. '
            'All new claims, including the distinction between a Kalikow counterexample and a counterexample to the target, are recorded in CLAIMS.jsonl. '
            'The final verdict is PARTIAL.\n')

with (root/'ATTEMPT.md').open('a', encoding='utf-8') as f:
    f.write('\nThe completed additional attempt also derives an exact beta-integral formula at A=1: '
            'alpha=(12,5,10,5)/32 has d_alpha=(1/16,0), kappa=21/16, and opposing auxiliary drifts -5/22 and 7/22. '
            'A dimension-three extension is provably ballistic while failing the same criterion, so this obstruction is explicitly not a zero-speed result. '
            'Eight new finite algebra/sign theorems passed Lean; all probabilistic steps are written in SECOND_ATTEMPT.md. '
            'The weak-drift planar regeneration gap remains open in this record.\n')
    f.write('\n\n## Appendix: full additional attempt record\n\n'
            + (root/'SECOND_ATTEMPT.md').read_text(encoding='utf-8'))

prior = root/'validation.json'
if prior.exists() and not (root/'validation_first_attempt.json').exists():
    (root/'validation_first_attempt.json').write_bytes(prior.read_bytes())
files = ['STATUS.md','ATTEMPT.md','SECOND_ATTEMPT.md','LITERATURE.md','CLAIMS.jsonl',
         'FiniteTrap.lean','lean_check.txt','KalikowObstruction.lean','kalikow_lean_check.txt',
         'kalikow_probe.json','kalikow_closed_form.json','walk_probe.json',
         'ballistic_control_probe.json','brain_gap_recall.txt','brain_kalikow_recall.txt']
validation = dict(problem_id='F0136', state='DONE', verdict='PARTIAL',
                  claim_rows=len(claims), new_lean_theorems=8, new_lean_exit_code=0,
                  rational_family_checks=100, finite_walk_steps=800000,
                  total_http_requests=len(json.loads((root/'search_log.json').read_text()))+
                                      len(json.loads((root/'second_attempt_search_log.json').read_text())),
                  limitations=['No proof or counterexample to F0136.',
                               'The counterexample refutes the Kalikow reduction only.',
                               'The range/clock sufficient criterion has two unproved quantitative inputs.',
                               'Finite walk experiments establish no asymptotic speed.',
                               'Lean checks finite algebra, not the stochastic arguments.'],
                  sha256={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in files})
prior.write_text(json.dumps(validation, indent=2), encoding='utf-8')
print(json.dumps({k:v for k,v in validation.items() if k!='sha256'}, indent=2))
