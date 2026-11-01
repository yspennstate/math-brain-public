from pathlib import Path
import hashlib
import json
import datetime

root = Path(__file__).resolve().parent
log = (root / 'lean_check.log').read_text(encoding='utf8')
if '\nExit: ' not in log and 'Run did not complete:' not in log:
    raise SystemExit('Lean check is still pending; records not finalized.')
digest = hashlib.sha256((root / 'FiniteAlgebra.lean').read_bytes()).hexdigest()
assert 'Source SHA256: ' + digest in log
names = ['density_event_lower_bound', 'joint_density_lower_bound',
         'two_slice_covariance', 'd3_peierls_threshold']
passed = ('\nExit: 0\n' in log and all(name in log for name in names)
          and 'sorryAx' not in log and 'error:' not in log)
if passed:
    result = ('The local FiniteAlgebra.lean check completed with exit 0. '
              'All four declarations were kernel checked; their printed axiom '
              'lists are in lean_check.log. Source SHA256: ' + digest + '. '
              'This verifies only the finite real-algebra steps, not the '
              'percolation proofs or external critical-site development.')
else:
    result = ('The local algebra check did not produce a successful receipt; '
              'no Lean-checked claim is made. See lean_check.log. '
              'The written hand proofs stand separately. Source SHA256: ' + digest + '.')
claims_path = root / 'CLAIMS.jsonl'
claims = [json.loads(line) for line in claims_path.read_text(encoding='utf8').splitlines() if line.strip()]
assert all(c['problem_id'] == 'G0001' for c in claims)
assert all(c['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'} for c in claims)
if passed and not any(c.get('proof_location') == 'FiniteAlgebra.lean; lean_check.log' for c in claims):
    claims.append({'problem_id':'G0001',
        'claim':'The four real-algebra declarations in FiniteAlgebra.lean are kernel checked: density lower bounds, two-slice covariance, and the explicit dimension-three Peierls parameter threshold.',
        'status':'proved', 'proof_location':'FiniteAlgebra.lean; lean_check.log',
        'remaining_gap':'Only algebra is formalized; neither the whole percolation argument nor the external critical-site certificate was replayed.',
        'checks':result})
claims_path.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf8')
for name in ['CHECK_RECEIPTS.md','ATTEMPT.md']:
    with (root / name).open('a',encoding='utf8') as f:
        f.write('\n\nFinal continuation receipt (2026-10-11): ' + result + '\n')
        f.write('Final verdict: PARTIAL. The complete full-scope consequence remains conditional on the public critical-site theorem. Its pinned statement and public verification reports were audited, but its full dependency closure was not independently kernel replayed. A successful replay would supply the missing endpoint; no exact numbered finite-tail theorem satisfying the requested literature criterion was found.\n')
old = (root / 'STATUS.md').read_text(encoding='utf8').splitlines()
body = '\n'.join(old[3:])
status = ('STATE: DONE\n'
    'NEXT: Independently kernel replay the complete critical-site proof closure at commit cd090736b8f5984d49926e80363910e7c6441a4f with its pinned toolchain, or obtain and check a standalone proof export; then apply the written endpoint reduction.\n'
    'VERDICT: PARTIAL\n'
    '2026-10-11 final continuation: ' + result + '\n'
    '2026-10-11 final continuation: Bounded attempt closed. New all-dimensional boundary obstruction and model-correspondence proofs saved. Pinned source/tree/statement checks passed, but public reports do not constitute an independent full certificate replay. No unconditional G0001 solution or exact printed solution is claimed. Earlier WORKING entries below are historical.\n' + body + '\n')
(root / 'STATUS.md').write_text(status,encoding='utf8')
required = ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl',
            'BOUNDARY_OBSTRUCTION.md','MODEL_CORRESPONDENCE.md','CERTIFICATE_AUDIT.md']
assert all((root / name).is_file() for name in required)
assert (root / 'STATUS.md').read_text(encoding='utf8').splitlines()[0] == 'STATE: DONE'
receipt = {'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'verdict':'PARTIAL', 'claims_count':len(claims), 'lean_algebra_checked':passed,
           'lean_source_sha256':digest, 'required_records_present':required,
           'external_critical_site_certificate_replayed':False}
(root / 'final_record_check.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt,indent=2))
