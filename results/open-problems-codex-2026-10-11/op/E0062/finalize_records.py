"""Finalize the partial research record only after the bounded check ends."""
from pathlib import Path
import datetime, hashlib, json

root = Path(__file__).resolve().parent
result = json.loads((root/'lean_check_result.json').read_text(encoding='utf-8'))
state = result['state']
if state == 'RUNNING':
    raise SystemExit('The Lean check is still running; no finalization performed.')
if state not in ('COMPLETE', 'TIMEOUT', 'UNRECOVERED'):
    raise SystemExit('Repair the verification runner error before finalizing.')
checked = state == 'COMPLETE' and result.get('exit_code') == 0
if state == 'COMPLETE' and not checked:
    raise SystemExit('Compiler errors need repair before finalization.')
source = (root/'Prefix.lean').read_bytes()
sha = hashlib.sha256(source).hexdigest()
log = (root/'lean_check.log').read_text(encoding='utf-8', errors='replace')
if checked:
    assert sha == result['source_sha256'] == result['source_sha256_after']
    for name in ['alternating_increment_bound', 'balanced_product_identity',
                 'rate_complementarity_forces_independent_support',
                 'weighted_cyclic_rate_identity']:
        assert name in log, f'Missing final-version axiom print: {name}'
    assert 'sorryAx' not in log and 'error:' not in log.lower()
    text = source.decode('utf-8')
    assert 'sorry' not in text and 'native_decide' not in text
    assert '\nimport Mathlib\n' not in '\n'+text

claims = [json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
for claim in claims:
    claim['claim'] = claim['claim'].replace('divergent coordinate Cesaro averages', 'a nonconvergent Cesaro-average vector')
    claim['claim'] = claim['claim'].replace('nonconvergent coordinate Cesaro averages', 'a nonconvergent Cesaro-average vector')
    old = claim['checks']
    if checked:
        old = old.replace('exact rational and Lean algebra checks in progress.',
            '2,187 exact rational prefix/cut checks passed; the four-species prefix algebra was kernel-checked in Prefix.lean.')
        old = old.replace('Lean product expansion check in progress.',
            'the product expansion and kappa-bound algebra were kernel-checked in Prefix.lean.')
        if 'Section 10' in claim['proof_location'] or 'Section 12' in claim['proof_location'] or 'Section 14' in claim['proof_location']:
            old += ' The relevant finite rate identities/cancellations were kernel-checked; the analytic proof is ordinary mathematics.'
    else:
        failed_verification = ('the one-hour shared Lean check timed out' if state == 'TIMEOUT' else
            'the shared Lean compiler outcome is unrecovered after an interrupted slot wait')
        old = old.replace('exact rational and Lean algebra checks in progress.',
            f'2,187 exact rational prefix/cut checks passed; {failed_verification} and is not certified.')
        old = old.replace('Lean product expansion check in progress.',
            f'Lean formalization supplied, but {failed_verification} and is not certified.')
    claim['checks'] = old + ' Author continuation rereading: REFEREE.md; no general solution claimed.'
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False)+'\n' for c in claims), encoding='utf-8')

stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
if checked:
    summary = ('Finite algebra and independent-support implication compiled successfully; '
               'the full analytic proofs are not Lean-formalized.')
elif state == 'TIMEOUT':
    summary = ('The bounded one-hour shared Lean attempt timed out; no Lean-checked claim is made. '
               'Ordinary proofs survived the author rereading.')
else:
    summary = ('The shared Lean compiler outcome is unrecovered: the log records only a slot wait, '
               'the result marker remained RUNNING past its nominal hour, and no matching live '
               'runner/checker process was found. No Lean-checked claim is made. '
               'Ordinary proofs survived the author rereading.')
status_path = root/'STATUS.md'
lines = status_path.read_text(encoding='utf-8-sig').splitlines()
lines[0] = 'STATE: DONE'
lines = [
    'NEXT: Classify unbalanced chordless four-cycles (starting with a=c=1/2,b=d=2/5), then interacting cyclic supports.' if line.startswith('NEXT:') else
    'VERDICT: PARTIAL' if line.startswith('VERDICT:') else line
    for line in lines
]
lines.append(f'{stamp}: Finalized DONE / PARTIAL. {summary} Full zero-entry criterion unresolved; see RESULTS.md and ATTEMPT.md Section 9.')
status_path.write_text('\n'.join(lines)+'\n', encoding='utf-8')

verification = f'''# Verification report — 2026-10-12

Final research verdict: PARTIAL. {summary}

The old tool session 82004 was unavailable on continuation. A read-only
process query found no matching live old check. Its outcome remains
unrecovered; it is not credited as a successful or failed compilation.

The fresh run used run_lean_check.py and the ordinary serialized lake shim:

    lake env lean ~/brain_workers/TRIO_1011/op/E0062/Prefix.lean

Working directory: ~/lean_verify. Timeout: 3600 seconds.
Recorded runner state: {state}; exit code: {result.get('exit_code')}.
Source SHA256: {sha}.
Exact run timestamps and command: lean_check_result.json.
Preserved compiler/queue output: lean_check.log.
For UNRECOVERED, the original stale RUNNING marker is preserved verbatim
in lean_check_result.before_assessment.json. UNRECOVERED is an author
assessment of the unavailable result, not a compiler success, compiler
error, or confirmed timeout. The exact compiler exit code is unknown.

Formalization scope: prefix and pair cancellation algebra, cross-term
nonnegativity, product expansions and the kappa bound, balanced product
identities, the symmetric finite-rate independent-support implication,
and weighted payoff/rate identities. Standard ring, positivity, norm_num,
linarith and order reasoning only; no sorry or native_decide. Selective
Mathlib imports only. The probability-measure and convergence arguments
are written ordinary proofs, not Lean certificates.

Completed exact rational checks: 2,187 prefix/cut checks, 23,166 strict
product-bound checks and 858 equality-case checks. These existing runs
are preserved in experiments_output.txt, exact_checks.json and
equality_checks.json. No unrelated tests were repeated.

The author's continuation rereading is REFEREE.md. The final mathematical
results and remaining gap are summarized in RESULTS.md. All claims are
recorded in CLAIMS.jsonl. The general magnitude-dependent criterion for
arbitrary matrices with zeros remains unproved.
'''
(root/'VERIFICATION.md').write_text(verification, encoding='utf-8')
with (root/'ATTEMPT.md').open('a', encoding='utf-8') as out:
    out.write(f'\n## Final verification and verdict ({stamp})\n\n')
    out.write(summary+'\n\n')
    out.write('The continuation author rereading is REFEREE.md. The only mathematical edit was to make the weighted-AM-GM scaling explicit; divergence is understood as failure of the vector limit. See VERIFICATION.md for exact formalization scope and saved outputs.\n\n')
    out.write('STATE: DONE; VERDICT: PARTIAL. No general necessary-and-sufficient criterion has been proved or verified in print. The concrete remaining unbalanced four-cycle and coupled-zero-matrix gap is stated in Section 9 and RESULTS.md.\n')

required = ['STATUS.md', 'LITERATURE.md', 'ATTEMPT.md', 'CLAIMS.jsonl', 'REFEREE.md', 'RESULTS.md', 'VERIFICATION.md']
assert all((root/name).is_file() for name in required)
assert status_path.read_bytes().splitlines()[0] == b'STATE: DONE'
assert all(c['status'] in ['proved', 'counterexample', 'proved_special_case', 'numerical_evidence', 'conjecture'] for c in claims)
print(json.dumps({'state':'DONE', 'verdict':'PARTIAL', 'lean_checked':checked,
                  'claim_count':len(claims), 'sha256':sha, 'timestamp':stamp}, indent=2))
