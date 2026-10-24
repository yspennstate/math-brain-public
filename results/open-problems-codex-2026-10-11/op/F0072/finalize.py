from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
x=json.loads((R/'lean_check.json').read_text(encoding='utf8'))
assert x.get('exit_code')==0, 'Lean has not passed'
assert x.get('source_sha256')==hashlib.sha256((R/'MixtureAlgebra.lean').read_bytes()).hexdigest(), 'Lean result is for a different source'
lean=(R/'MixtureAlgebra.lean').read_text(encoding='utf8')
assert 'sorry' not in lean and 'native_decide' not in lean
with (R/'ATTEMPT.md').open('a',encoding='utf8') as stream:
 stream.write('\nFinal Lean result: the corrected MixtureAlgebra.lean passed `lake env lean` from ~/lean_verify (exit code 0). The exact checked source SHA-256 is '+x['source_sha256']+'. Its two identities use ring proofs checked by Lean; no sorry or native_decide occurs. This formally checks only the finite algebraic identities, not the probabilistic theorem. The first missing-import failure is retained in lean_check_initial.json.\n')
claim={'problem_id':'F0072','claim':'The displayed two-by-two symmetric rank-one determinant identity and internal-edge cancellation algebra are Lean-checked over the reals.','status':'proved','proof_location':'MixtureAlgebra.lean; lean_check.json','remaining_gap':'This does not formalize the general finite-graph determinant lemma or the probability proof.','checks':'lake env lean, exit 0; exact source SHA-256 '+x['source_sha256']+'; ring proofs; no sorry or native_decide.'}
with (R/'CLAIMS.jsonl').open('a',encoding='utf8') as stream:stream.write(json.dumps(claim)+'\n')
status='''STATE: DONE
NEXT: Prove a uniform logarithmic lower bound at every site of the partially constrained wall subbox, including its edges and corners; then establish any requested general-potential extension.
VERDICT: PARTIAL

2026-10-12: Verified Velenik Open Problem 5 in PDF pp. 22-23 and its hypotheses. Searched arXiv, OpenAlex (including 93 citing works), Crossref, Semantic Scholar and GitHub; no matching theorem verified. API rate limits and publisher challenge are recorded in LITERATURE.md.
2026-10-12: Read the earlier F0072-A001 ledger attempt and original brain recall results. The prior Gaussian-mixture idea was checked and advanced without invoking a random-environment wall theorem.
2026-10-12: Proved the boundary/contact identity; averaged logarithmic lower bounds; uniform order-log-N bulk heights for the full-wall continuous SOS model in every d>=2; matching bounds on strict interior subboxes of partial walls; O(log M) higher-dimensional upper bounds uniform in ambient volume; and subsequential free-law conditioning limits with the stated partial bounds. Full proofs and referee audit are in ATTEMPT.md.
2026-10-12: Exact rational flow checks passed in 27 small configurations; chain formulas and MGF inequalities passed; the corrected Lean algebra file passed (exit 0). Initial missing-import failure retained. No claim that the full probability theorem was formalized.
2026-10-12: Closed this attempt with the precise gap above. The source's full uniform-wall-site quantifiers and broad interaction class are not solved here.
'''
(R/'STATUS.md').write_text(status,encoding='utf8')
print('STATE: DONE; VERDICT: PARTIAL; Lean algebra checked.')
