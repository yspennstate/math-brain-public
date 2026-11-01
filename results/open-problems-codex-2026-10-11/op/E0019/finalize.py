from pathlib import Path
import json,re
root=Path('.')
required=['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','CHECKS.md','Algebra.lean','lean_result.json','numerics.json']
for n in required:
 assert (root/n).exists(),n
s=(root/'ATTEMPT.md').read_text(encoding='utf8')
assert 'rho_1||_{L^p(N_r(Gamma))}' in s
assert 'The endpoint requires more information' not in s
assert 'including the endpoint exponent' in s
for line in (root/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines():
 c=json.loads(line);assert c['problem_id']=='E0019';assert c['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'];assert c['proof_location'] and c['remaining_gap']
z=json.loads((root/'lean_result.json').read_text(encoding='utf8'));assert z['exit_code']==0
lean=(root/'Algebra.lean').read_text(encoding='utf8');assert 'sorry' not in lean and 'native_decide' not in lean and 'import Mathlib\n' not in lean
assert not (root/'Algebra.lean').read_bytes().startswith(b'\xef\xbb\xbf')
log='''STATE: DONE
NEXT: Classify the critical and intermediate switching regimes in Example 4.7; establish matching positive Lp bounds or a general singularity-set theorem.
VERDICT: PARTIAL

2026-10-12: Confirmed the exact source question on PDF p. 13 and Section 4 hypotheses on p. 8. Searched arXiv, OpenAlex, Crossref, Semantic Scholar and GitHub through Python HTTP requests; recorded every request and the OpenAlex rate-limit failures. Semantic Scholar source citations succeeded via the correct DOI. Found explicit later partial answers, especially Benaim--Bichard (2024 preprint; 2025 journal): C^k for the exact spiral example when min(lambda_0,lambda_1)>k+2. No same-hypotheses complete printed solution established.
2026-10-12: Read-only brain and intake review exposed an earlier erroneous drift-collinearity/bracket inference and determinant transcription; corrected them in ATTEMPT.md.
2026-10-12: Proved existence, uniqueness and absolute continuity for the exact spiral example by stationary convolution, coupling, and a fixed-time two-switch Jacobian. Proved the conformal-flow persistence lemma: if lambda<d*kappa, local Lp fails for p>=d*kappa/(d*kappa-lambda), including the endpoint.
2026-10-12: Proved essential unboundedness propagated along the other flow when the originating exit rate is below 1, and local Lp failure for p>=1/(1-lambda), including the endpoint after a final shrinking-tube audit. Recorded an elementary arbitrary-density example under the bare source hypotheses. These are special-case/obstruction results, not a solution of the entire open question.
2026-10-12: SymPy exact identities, 300 finite-difference Jacobian checks, and 30,000 stationary-convolution samples passed. Lean 4 kernel-checked real-variable algebra: exit code 0, no sorry/native_decide; analytic proofs remain handwritten. Complete proofs, scope limits and unresolved regimes are in ATTEMPT.md; check details are in CHECKS.md.
2026-10-12: Finished this bounded research attempt. Remaining gap: no full density regularity classification for arbitrary switched smooth flows with merely continuous spatial rates; no matching upper integrability bounds or complete analysis of critical/intermediate rates for the source example. STATE DONE means the attempt is complete, not that the open problem is solved.
'''
(root/'STATUS.md').write_text(log,encoding='utf8')
assert (root/'STATUS.md').read_bytes().splitlines()[0]==b'STATE: DONE'
print('Artifact validation passed. Claims:',len((root/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()))
print('Final status: DONE / PARTIAL. Lean checked; all four required research records present.')
