from pathlib import Path
import json
import re

p = Path('~/brain_workers/TRIO_1011/op/F0021')
lean = json.loads((p / 'SECOND_LEAN_CHECK.json').read_text(encoding='utf-8'))
assert lean['exit_code'] == 0, 'Do not mark the new Lean lemmas checked on a failed run.'
code = (p / 'SECOND_F0021.lean').read_text(encoding='utf-8')
assert not re.search(r'\b(sorry|native_decide)\b', code)
finite = json.loads((p / 'SECOND_CHECKS.json').read_text(encoding='utf-8'))
holder = json.loads((p / 'SECOND_HOLDER_CHECKS.json').read_text(encoding='utf-8'))
large = json.loads((p / 'SECOND_LARGE_N_CHECKS.json').read_text(encoding='utf-8'))
assert holder['finite_holder_and_temperature_cases_passed'] == 200
assert finite['checks']['exact_entropy_coarsenings'] == 45044
assert large['elapsed_seconds'] < 600

rows = [json.loads(line) for line in (p / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
for row in rows:
    row['checks'] = row['checks'].replace(
        'second Lean check pending.',
        'SECOND_F0021.lean merge_entropy kernel-checked, exit 0.')
    row['checks'] = row['checks'].replace(
        'second Lean algebra pending.',
        'SECOND_F0021.lean merge_entropy, sparse_exponents, and layer_allocation kernel-checked, exit 0; the full probability proof is handwritten.')
    row['checks'] = row['checks'].replace(
        'additional finite validation pending.',
        'SECOND_HOLDER_CHECKS.json: 200 finite Holder/temperature checks and entropy-identity maximum error 2.67e-14; growing-temperature asymptotics have a complete handwritten proof.')

rows.append({
    'problem_id': 'F0021',
    'claim': 'Sparse Pareto experiments at alpha=5.5, kappa=0.32 display slow decay in the finite probability of violating the exponential rare-reward bound; no KPZ limit is inferred.',
    'status': 'numerical_evidence',
    'proof_location': 'SECOND_CHECKS.json; SECOND_LARGE_N_CHECKS.json; second_verify.py; second_large_n.py',
    'remaining_gap': 'Finite Monte Carlo and floating-point kernels do not prove an asymptotic law or a result for the full random-background polymer.',
    'checks': 'Exhaustive small-size expansion check; sparse conditional Pareto sampling up to n=2^30, with bounded memory and 330.64 seconds runtime for the extended job.'
})
assert all('pending' not in row['checks'] for row in rows)
(p / 'CLAIMS.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows), encoding='utf-8')

formal = f'''

## Formal checks of the additional attempt

`SECOND_F0021.lean` passed with exit code 0 using targeted imports only. It kernel-checks the merged-increment entropy inequality, the sparse-layer exponent signs, and the allocation of layer energies below half the chain entropy. Command: `lake env lean ~/brain_workers/TRIO_1011/op/F0021/SECOND_F0021.lean`, from `~/lean_verify`, with a 3600-second timeout; recorded elapsed time {lean['elapsed_seconds']:.2f} seconds. The file contains no `sorry` and no `native_decide`. Encoding and tactic-layout failures were corrected, and their failed logs are retained separately. No probability theorem, total-variation theorem, or Holder asymptotic is claimed formally checked: their full proofs are in SECOND_ATTEMPT.md and their finite components are corroborated by the saved computations.

**Final verdict of this additional attempt: PARTIAL.** Both proposed approaches are written down. The entropy-controlled-chain approach was pursued through a rare-reward path-law theorem and an unconditional sublinear truncation bound for the original polymer. The other approach was checked against an admissible infinite-third-moment construction. The necessary KPZ-scale random-background comparison and a fixed-temperature KPZ/Airy universality theorem remain unproved; no counterexample satisfying Assumption 3 was found.
'''
with (p / 'SECOND_ATTEMPT.md').open('a', encoding='utf-8') as f:
    f.write(formal)
with (p / 'SECOND_REFEREE.md').open('a', encoding='utf-8') as f:
    f.write(formal)
with (p / 'LITERATURE.md').open('a', encoding='utf-8') as f:
    f.write('''
The additional attempt read the remaining gap, queried the math store twice as recorded above, and fetched the neighbouring entropy-controlled LPP paper. It did not find or claim a new solution in print. No additional global literature-status assertion supersedes the bounded search and OpenAlex access limitation from the first attempt. Saved computational and Lean records independently document the additional mathematical work.
''')

(p / 'STATUS.md').write_text('''STATE: DONE
NEXT: In a future attempt, improve the random-background truncation comparison from the proved n^(1-r) bound to o_P(n^(1/3)), and establish fixed-temperature KPZ/Airy universality for the capped model.
VERDICT: PARTIAL

2026-10-12: First attempt verified the source, searched later literature, proved isolated-spike/truncation reductions, and concluded PARTIAL. OpenAlex was rate-limited; no checked literature closure was identified.
2026-10-12: Reopened at the user's request. Read ATTEMPT.md and queried the brain for the confinement/Lindeberg gap and Berger-Torri entropy-controlled chains. Wrote two new approaches in SECOND_ATTEMPT.md and pursued the chain approach.
2026-10-12: Proved the lattice chain-count estimate, entropy coarsening, and a many-spike rare-reward theorem with quenched total-variation convergence to the bare walk. Proved its slowly growing-temperature version.
2026-10-12: Holder and finite path relative entropy yielded an unconditional original-polymer cap error bound (n log 2+exp(-n^(1/3)/4))/(1+n^r), for any 0<r<(alpha-5)/(3 alpha) with a suitable cutoff below n^(1/3). This is sublinear but much larger than the KPZ scale.
2026-10-12: Refuted deterministic transfer shortcuts and constructed an admissible infinite-third-moment law. Exact finite checks passed; additional Lean algebra passed. Sparse experiments used bounded memory and remained numerical evidence only.
2026-10-12: Additional attempt concluded PARTIAL, with all proofs and remaining gaps written in SECOND_ATTEMPT.md and audited in SECOND_REFEREE.md. No full KPZ/Airy theorem or iid counterexample to F0021 was obtained.
''', encoding='utf-8')

assert (p / 'STATUS.md').read_text(encoding='utf-8').splitlines()[0] == 'STATE: DONE'
print('Additional attempt finalized: STATE DONE; VERDICT PARTIAL;', len(rows), 'claim rows; new Lean exit 0.')
