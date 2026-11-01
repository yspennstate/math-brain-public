from pathlib import Path
import json
import sys

finish = '--finish' in sys.argv
check = json.loads(Path('fork_refined_checks.json').read_text(encoding='utf8'))
assert check['local_radius_2_binary_patterns'] == 8192
assert check['largest_generator_G_plus_kappa_r'] == '0'
forcing = json.loads(Path('forcing_checks.json').read_text(encoding='utf8'))
assert forcing['incoming_edges'] == 20
lean_files = ['fork_lean_check.txt', 'fork_refined_lean_check.txt']
lean_passed = all(Path(f).exists() and 'Exit: 0' in Path(f).read_text(encoding='utf8') for f in lean_files)
if finish:
    assert lean_passed, 'Both Lean certificates must finish successfully before final recording.'

new_claims = [
    {
        'problem_id': 'E0007',
        'claim': 'For common nearest-neighbor dispersal on Z^2, type 2 is locally extinct from every initial law whenever beta_2/delta_2 is at most (2 sqrt(213)-6)/17 + 1/(1000*3^11*5^5*13^2), independently of type-1 parameters.',
        'status': 'proved_special_case',
        'proof_location': 'SECOND_ATTEMPT.md: Full proof, refinement, and stationary endpoint extension',
        'remaining_gap': 'Does not settle ratio-only competition between two supercritical types. Exponential decay is proved strictly below the algebraic root; only local extinction is proved in the endpoint extension.',
        'checks': 'Complete graphical domination, exact fork generators, positive Lyapunov bounds, and controlled stationary event. 8192 radius-two patterns, 40960 changes, 512 periodic states and 4464 transitions checked exactly. Exact forcing-event counts and rational endpoint margins in forcing_checks.json; '+('both Lean certificates passed.' if lean_passed else 'Lean verification pending.'),
    },
    {
        'problem_id': 'E0007',
        'claim': 'For the normalized nearest-neighbor single-type contact process with total birth rate 109/80, the fork Lyapunov certificate gives occupation probability from all occupied at most exp(-46640*t/57637989).',
        'status': 'proved_special_case',
        'proof_location': 'SECOND_ATTEMPT.md: Refinement; fork_refined_checks.json; ForkRefinedCertificate.lean',
        'remaining_gap': 'Single-type extinction certificate only; not a theorem about the general ratio-ordered two-supercritical competition case.',
        'checks': 'Exact rational coefficients and exhaustive finite generator check passed. '+('Lean rational certificate and symbolic identity passed.' if lean_passed else 'Lean certificate pending.'),
    },
]
new_claims.append({
    'problem_id': 'E0007',
    'claim': 'For the two-site single-type contact process initially all occupied with birth rate K and death rate 1, the limits K to infinity and time to infinity of single-site occupation probability do not commute: the two iterated limits are 0 and 1.',
    'status': 'counterexample',
    'proof_location': 'SECOND_ATTEMPT.md: A boundary-case check on Approach A',
    'remaining_gap': 'Counterexample to an interchange of limits in an auxiliary finite model; not a counterexample to E0007 on Z^2.',
    'checks': 'Complete three-state CTMC equations and integrating-factor bound; independent unit-interval emptying events prove finite-K absorption.'
})
p = Path('CLAIMS.jsonl')
claims = [json.loads(s) for s in p.read_text(encoding='utf8').splitlines() if s.strip()]
for c in claims:
    c['proof_location'] = c.get('proof_location', '').replace('ATTEMPT.md ?', 'ATTEMPT.md section ')
for c in new_claims:
    claims = [old for old in claims if old['claim'] != c['claim']]
    claims.append(c)
p.write_text(''.join(json.dumps(c, ensure_ascii=False)+'\n' for c in claims), encoding='utf8')

p = Path('ATTEMPT.md')
s = p.read_text(encoding='utf8')
marker = '## Second attempt at user request'
if marker in s:
    s = s.split(marker)[0].rstrip()+'\n'
s += '''
## Second attempt at user request

2026-10-12: The prior final assessment describes the first attempt.
The second attempt and full new proofs are in SECOND_ATTEMPT.md.
Two new routes were considered: fast-birth death-birth voter reduction,
and a Lyapunov function retaining occupied/vacant three-site forks.
The latter was pursued and improves the nearest-neighbor type-2
extinction special case to

    beta_2/delta_2 <= (2 sqrt(213)-6)/17
                     + 1/(1000*3^11*5^5*13^2).

The algebraic root is approximately 1.3640611199207557. This conclusion
holds regardless of type-1 parameters and from every initial law by
single-type graphical domination. The tiny explicit extension includes
the algebraic endpoint, using a stationary finite-energy argument.
For beta_2/delta_2 strictly below the root the proof gives an explicit
exponential rate; no exponential rate is asserted for the extension.
No claim of novelty relative to published one-type critical-value bounds
is made. This is stronger than the first attempt's 4/3 bound.

Exact checks pass on 8192 radius-two patterns and 512 periodic states.
The central remaining gap is unchanged: no exclusion proof or
counterexample for two supercritical types under only the ratio ordering.
VERDICT: PARTIAL.
'''
if lean_passed:
    s += '\nBoth new Lean certificates passed; see fork_lean_check.txt and fork_refined_lean_check.txt.\n'
else:
    s += '\nThe new Lean checks are still pending; the written proof and finite checks are saved.\n'
p.write_text(s, encoding='utf8')

p = Path('LITERATURE.md')
s = p.read_text(encoding='utf8')
marker = '## Second-attempt brain recall'
if marker in s:
    s = s.split(marker)[0].rstrip()+'\n'
s += '''
## Second-attempt brain recall

2026-10-12, read-only math store calls:

- math_recall.py "multitype contact process unequal death rates vacancy correlation competitive exclusion"
- math_recall.py "Broman Stover contact process stochastic domination"

The first query asks directly about the remaining vacancy-correlation
gap. It returned generic IPS material and unrelated correlation,
queueing and branching cards, including claim_48be9b2fde60ef90775544c92dc25dd9,
claim_e72e75e02d0527594e059eccf53d2e760053821def0e437a4d1825a84a416179,
and claim_10d710827b89fea7a492417ab4897ceeeac651ddf0e4d26e7f75bc3739620e4e.
These do not provide a theorem controlling the needed two-type
correlation integral. The named-result query is also treated as hints,
not a verdict. No new online literature claim or novelty claim is made
in the second attempt; the earlier exact-match search limitations remain.

The named Broman/Stover query returned generic stochastic-domination
material (claim_6e108f8c5133f68c71bd2763fce36f07) and unrelated cards,
not a Broman/Stover theorem card. None of the returned cards supplies
the missing exclusion argument, and none is used as a proof premise.
'''
p.write_text(s, encoding='utf8')

p = Path('SECOND_ATTEMPT.md')
s = p.read_text(encoding='utf8')
marker = '## Final check record and verdict'
if marker in s:
    s = s.split(marker)[0].rstrip()+'\n'
s += '''
## Final check record and verdict

Exact finite checks passed: 8192 radius-two binary patterns, 40960
site changes, 512 periodic binary configurations, and 4464 nonzero-rate
transitions. Both the initial fork certificate and the refined shared-event
certificate are retained separately in fork_checks.json and
fork_refined_checks.json. The job for the refinement completed in about
175 seconds; memory is limited to small fixed arrays and rational numbers.
forcing_checks.json verifies the twenty incoming edges, forbidden
edge/site times and every rational endpoint margin. Decimal values there
are for display only. The full hostile-referee audit is FORK_REFEREE.md.

The exact forcing constant is C0=1/93555759375, so the extension
epsilon is 1/93555759375000. Its positive stationary-drift margin
is 37/140333639062500. Neither number is obtained by sampling.

VERDICT: PARTIAL. The stronger extinction special case and the finite
limit-interchange counterexample are fully proved above. No proof or
counterexample is obtained for the central two-supercritical species
problem with only birth/death ratio ordering.
'''
if lean_passed:
    s += '\nBoth new Lean files compiled successfully, with exit 0, one at a time. The logs are fork_lean_check.txt and fork_refined_lean_check.txt. These certify the polynomial identities and finite rational linear inequalities, not the probabilistic construction or convergence argument. No sorry, native_decide or full Mathlib import is used.\n'
else:
    s += '\nLean verification is still pending; no successful formal check is inferred from source-file presence.\n'
p.write_text(s, encoding='utf8')

p = Path('STATUS.md')
s = p.read_text(encoding='utf8')
lines = s.splitlines()
lines[0] = 'STATE: DONE' if finish else 'STATE: WORKING'
lines[1] = ('NEXT: Control the long-time vacancy-correlation correction for two supercritical types with conflicting birth/death advantages; the stronger extinction certificate does not cover that case.' if finish else 'NEXT: Complete the sequential Lean certificate checks and final record validation.')
lines[2] = 'VERDICT: PARTIAL'
s = '\n'.join(lines)+'\n'
log = '2026-10-12 (second attempt): Proved stronger nearest-neighbor type-2 extinction using a fork Lyapunov function, then an explicit stationary endpoint extension. Exact local and finite checks passed. The two-supercritical ratio-only case remains unresolved.'
if log not in s:
    s += '\n'+log+'\n'
if finish:
    s += '2026-10-12 (second attempt complete): Both Lean certificates passed; full proof and limits recorded in SECOND_ATTEMPT.md. STATE: DONE; VERDICT: PARTIAL.\n'
p.write_text(s, encoding='utf8')
print('Recorded second-attempt results; '+('DONE/PARTIAL' if finish else 'WORKING/PARTIAL'))
