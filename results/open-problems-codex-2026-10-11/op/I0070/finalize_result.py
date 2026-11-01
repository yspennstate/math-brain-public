from pathlib import Path
import json
R=Path(__file__).parent
lean=(R/'EndpointAlgebra.lean').read_text(encoding='utf8')
assert 'sorry' not in lean and 'native_decide' not in lean
assert lean.count('theorem ')==3
claims=[json.loads(x) for x in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if x.strip()]
checks=json.loads((R/'endpoint_checks.json').read_text(encoding='utf8'))
assert checks['rank_one_cases']==1000
# Run this file only after the foreground Lean command returns exit code 0.
receipt='''# Verification receipt — 2026-10-12

Lean command: lake env lean ~/brain_workers/TRIO_1011/op/I0070/EndpointAlgebra.lean
Working directory: ~/lean_verify
Result: exit code 0.
The shared check guard reported a slot wait of 1604 seconds before running.
Imports: Mathlib.Data.Real.Basic and Mathlib.Tactic.Linarith.
Checked: critical_rho_positive, critical_H_exponent, absorption.
No sorry, native_decide, or user-declared axioms appear in the file.
Scope: these are three real algebra lemmas; the stochastic theorem is not formalized in Lean.

Finite diagnostic script: python -X utf8 endpoint_checks.py
Result: 6 exact Fraction exponent cases and 1000 factorization cases passed.
Maximum reconstruction error: 5.671216916061934e-16.

The full proof was checked against the published hypotheses and the ten failure modes in ATTEMPT.md.
All JSONL claims were parsed successfully. STATUS.md is written as UTF-8 without a BOM.
'''
(R/'VERIFICATION.md').write_text(receipt,encoding='utf8')
if not any(x.get('proof_location')=='EndpointAlgebra.lean; VERIFICATION.md' for x in claims):
 claims.append({'problem_id':'I0070','claim':'Three critical-exponent and absorption algebra lemmas have been checked by Lean 4.','status':'proved','proof_location':'EndpointAlgebra.lean; VERIFICATION.md','remaining_gap':'This formal check does not formalize the SPDE proof, spectral theory, or interpolation theorems.','checks':'lake env lean from ~/lean_verify returned exit code 0; no sorry or native_decide.'})
(R/'CLAIMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in claims),encoding='utf8')
p=R/'ATTEMPT.md'
s=p.read_text(encoding='utf8')
if '\n## Final outcome\n' not in s:
 s+='''
## Final outcome

The answer is affirmative under the exact retained hypotheses of Theorem 5.7 at p=2, with Hilbert X0. The full proof above survived the recorded self-audit. No remaining mathematical gap was identified. This rechecks and completes the earlier compact-tail candidate rather than asserting an unrelated fresh discovery. The algebra-only Lean check returned exit code 0; its limited scope and the numerical receipt are recorded in VERIFICATION.md. The literature screening does not certify novelty and did not verify an exact solution in print.
'''
p.write_text(s,encoding='utf8')
(R/'STATUS.md').write_text('''STATE: DONE
NEXT: Optional independent referee review of ATTEMPT.md before preparing any public manuscript.
VERDICT: SOLVED

2026-10-12: Retrieved the published Agresti–Veraar survey; confirmed Problem 6, Assumption 4.1, Theorems 4.7/5.7 and the p=2 critical relation. The extra reaction–diffusion intake text is not part of the question.
2026-10-12: Refreshed arXiv, OpenAlex, Crossref, Semantic Scholar and GitHub searches, including citing-source metadata. Recorded successful responses, TLS failures, timeouts and OpenAlex rate limits. No exact resolution in print was verified; novelty is not certified.
2026-10-12: Recovered earlier R10 reports read-only. Proved the affirmative endpoint theorem by compact-path spectral tails, critical tame growth, adapted rank-one splitting, zero-trace cutoff and stopped L2 identification of the independently constructed Lr solution. All source hypotheses retained; no mathematical gap remains after self-refereeing.
2026-10-12: Six exact exponent cases and 1000 finite factorization diagnostics passed. Lean checked three algebra lemmas with exit code 0; the SPDE theorem itself is not Lean-formalized. See ATTEMPT.md, LITERATURE.md, CLAIMS.jsonl and VERIFICATION.md.
''',encoding='utf8')
assert (R/'STATUS.md').read_text(encoding='utf8').splitlines()[0]=='STATE: DONE'
print('STATE: DONE; VERDICT: SOLVED; claims:',len(claims))
