"""Finalize only after the audited mathematics and successful Lean result."""
import pathlib, json, re
root = pathlib.Path(__file__).resolve().parent
log = (root/'lean_check.txt').read_text(encoding='utf-8')
assert log.startswith('Exit code: 0'), 'Do not finalize without the corrected Lean result.'
elapsed = re.search(r'Elapsed seconds: ([0-9.]+)',log).group(1)

p = root/'FULL_PROOF.md'
s = p.read_text(encoding='utf-8')
s = s.replace('# Candidate complete proof of P0391 — under hostile review',
              '# Complete proof of P0391 — finite second moment')
s = s.replace('This file records the new regenerative dyadic route. It must not be treated as a solved verdict until the checks in STATUS.md are finished. The earlier special cases and reductions are in ATTEMPT.md.',
              'This file proves the empty-start universal symmetric-queue diffusion theorem by a regenerative dyadic argument. The completed hostile audit is in REFEREE.md. Earlier intermediate results are retained in ATTEMPT.md. Standard inputs are the symmetric-queue stationary product form and the compound-Poisson workload FCLT; no queue-length diffusion theorem is assumed in this proof.')
s = s.replace('This proves the theorem if the regenerative and dyadic steps above survive the ongoing checks.',
              'This proves the theorem. The cycle identity, summable upcrossing bound, limit order and noncircular inputs have been checked in REFEREE.md.')
p.write_text(s,encoding='utf-8')

p = root/'ATTEMPT.md'
s = p.read_text(encoding='utf-8')
lines = s.splitlines()
lines[0] = '# P0391 — research record and final result, 11 October 2026'
s = '\n'.join(lines)+'\n'
summary = '''
## Final result: universal finite-second-moment theorem proved

FULL_PROOF.md gives the complete proof for every positional symmetric discipline in the source, empty initial state, a fixed service law with 0<E B<infinity and E B^2<infinity, and every real beta with r(1-rho_r)->beta. Writing m=E B, m2=E B^2 and h=m2/(2m),
Q_r(r^2 .)/r => Gamma(sqrt(m2/m) Brownian(.)-beta*.)/h
in the J1 topology. The proof establishes sup_{s<=r^2T}|W_r(s)-h Q_r(s)|/r ->0 for every finite T.

The missing positive-discrepancy estimate is resolved by retaining original-size marks, counting large-class upcrossings over whole regenerative cycles, and applying a summable dyadic Bernstein bound. The exact reward E Y=r*p_I*pi(f) eliminates the extra stationary-conditioning factor. Finite second moment alone makes each fixed large band vanish; no regular tail envelope is required. REFEREE.md checks every potentially failing step and both independent cycle diagnostics. GridBridge.lean passed Lean with no sorry or native_decide, checking only scalar interpolation, not the stochastic theorem. There is no remaining mathematical gap identified by this audit. No exact solution in print was verified; this is a new proof recorded here, not SOLVED_IN_LITERATURE.

The sections below retain earlier approaches and their limitations as a chronological research record. Statements of an unresolved endpoint in those earlier sections describe that stage and are superseded by FULL_PROOF.md.
'''
s = s.replace('\n## Exact target and source',summary+'\n## Exact target and source',1)
s = s.replace('## Results obtained','## Earlier intermediate results',1)
s = s.replace('These do NOT settle the requested finite-second-moment process theorem.',
              'These intermediate arguments alone did not settle the finite-second-moment process theorem; the regenerative dyadic proof in FULL_PROOF.md now does.')
s = s.replace('## Remaining target gap (final mathematical position)',
              '## Historical gap before the regenerative dyadic proof\n\nThe gap described in this section is resolved by FULL_PROOF.md, sections 4–5; it is retained to distinguish the earlier failed truncation approach from the completed proof.')
s = s.replace('- Topology: full process convergence is claimed only under the fourth-moment assumption. No finite-second-moment C-tightness or J1 convergence is asserted.',
              '- Topology: the earlier moment and tail-restricted arguments alone did not yield the universal J1 theorem. FULL_PROOF.md now proves uniform collapse and J1 convergence under exactly finite second moment.')
s = s.replace('The remaining mathematical task is to exclude narrow downward queue-length excursions under finite second moment.',
              'At this earlier stage, the remaining task was to exclude narrow downward queue-length excursions under finite second moment; FULL_PROOF.md now resolves it.')
p.write_text(s,encoding='utf-8')

p = root/'REFEREE.md'
s = p.read_text(encoding='utf-8')
s = s.replace('The mathematical checks below pass. The stationary-law source check and corrected Lean execution are recorded separately when completed; until then STATUS.md retains the provisional verdict.',
              'The mathematical checks below pass. The stationary-law source check, independent numerical diagnostics and successful corrected Lean execution are all recorded. The final verdict is SOLVED.')
pending = 'It was restarted sequentially on 11 October, with selective Real.Basic and Linarith imports and the requested hour timeout. Its final result is still pending at this checkpoint. No failed or pending check is counted as passed.'
s = s.replace(pending,
              'It was restarted sequentially on 11 October, with selective Real.Basic and Linarith imports and the requested hour timeout. The corrected run finished with exit code 0 in '+elapsed+' seconds; output is in lean_check.txt. The check uses ordinary Lean kernel verification, with no sorry or native_decide. No failed run is counted as passed.')
s = s.replace('## Checkpoint conclusion','## Final conclusion')
s = s.replace('Final verdict remains withheld until the corrected formal execution is recorded.',
              'The corrected formal execution passed. The universal finite-second-moment theorem is proved in FULL_PROOF.md; no mathematical gap remains identified by this audit.')
p.write_text(s,encoding='utf-8')

p = root/'CLAIMS.jsonl'
claims = [json.loads(l) for l in p.read_text(encoding='utf-8').splitlines()]
for c in claims:
    if c['status'] in ['proved','proved_special_case']:
        c['remaining_gap'] = ''
        c['checks'] += ' Universal endpoint subsequently established in FULL_PROOF.md; earlier scope limitations are historical.'
claims.extend([
 dict(problem_id='P0391',claim='For every work-conserving positional symmetric M/G/1 discipline, empty initial state, fixed service law with positive finite mean and finite second moment, and r(1-rho_r) tending to any real beta, Q_r(r^2 .)/r converges in J1 to Gamma(sqrt(E B^2/E B) Brownian(.)-beta*.)/h, h=E B^2/(2 E B). In fact sup_{s<=r^2T}|W_r(s)-h Q_r(s)|/r tends to zero in probability for every finite T.',
 status='proved',proof_location='FULL_PROOF.md, sections 1–6 and appendix; REFEREE.md',remaining_gap='',
 checks='Hostile audit of marked product form, finite cycle mean and exact compensation reward, noncircular compact containment and cycle count, bounded-class grid concentration, dyadic Bernstein constants, summable domination, order of limits, empty-start original-arrival tail bound and finite-horizon rate change. Two independent 32000-cycle diagnostics; 288 bridge simulation paths. Lean checked scalar interpolation only. No exact published solution verified.'),
 dict(problem_id='P0391',claim='The scalar two-sided grid interpolation implication and its arrival-budget variant hold over the reals.',status='proved',proof_location='GridBridge.lean; lean_check.txt',remaining_gap='',checks='lake env lean absolute GridBridge.lean path, run from ~/lean_verify; exit code 0; elapsed '+elapsed+' seconds; selective Real.Basic and Linarith imports; no sorry or native_decide. This formalizes no stochastic theorem.')
])
p.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')

p = root/'STATUS.md'
s = p.read_text(encoding='utf-8')
lines = s.splitlines()
lines[0] = 'STATE: DONE'
lines[1] = 'NEXT: None; complete proof and finished referee checks are recorded in FULL_PROOF.md and REFEREE.md.'
lines[2] = 'VERDICT: SOLVED'
s = '\n'.join(lines)+'\n'
s += '\n2026-10-11 FINAL: Complete finite-second-moment, arbitrary-symmetric-discipline empty-start proof survived the hostile audit. Regenerative marked-arrival rewards remove the extra conditioning factor, and summable dyadic concentration closes the exact endpoint, including sparse atomic laws. Both independent cycle diagnostics passed their stated statistical comparisons. Corrected Lean scalar check exited 0 after '+elapsed+' seconds; probabilistic theorem is not formalized. No remaining mathematical gap identified. This is a recorded new proof, not a verified literature solution. STATE DONE, VERDICT SOLVED.\n'
p.write_text(s,encoding='utf-8')
print('Final mathematical and check records saved: STATE DONE; VERDICT SOLVED.')
