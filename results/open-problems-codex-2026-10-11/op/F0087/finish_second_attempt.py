from pathlib import Path
import json
P=Path('.')
with (P/'SECOND_ATTEMPT.md').open('a',encoding='utf8') as f:
 f.write('''\n\n## Final check records\n\n`FusionExponents.lean` passes Lean 4 kernel checking (exit 0): fusion-divergence exponent, vanishing-volume exponent, admissible Holder exponent algebra, and the local mean lower bound. Imports are only Mathlib.Data.Real.Basic and Mathlib.Tactic.Linarith. No sorry, native_decide, or full Mathlib import; printed axioms are propext, Classical.choice, Quot.sound. The final transcript is `fusion_lean_check.log`.\n\n`verify_local_fusion_actual.py` checked the actual u=(i,-1,-i) determinant and det L as exact symbolic polynomial identities; `local_fusion_exact_check.log` records both. `nearest_neighbor_graph_checks.py` exhaustively checked leaf peeling and remaining cycles for 16,739 nonself successor maps on 2 through 6 vertices. This checks small finite cases of A3a's general graph proof; the proof for arbitrary m is the written argument, not an extrapolation from enumeration. Results are in `nearest_neighbor_graph_checks.json`.\n''')
rows=[json.loads(l) for l in (P/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for c in rows:
 if c['claim'].startswith('For any bounded planar K'):
  c['checks'] += '; exhaustive graph peeling checked for 16,739 maps on 2 through 6 vertices.'
 if c['claim'].startswith('At s=1/4'):
  c['checks'] += '; actual u=(i,-1,-i) expansion independently checked exactly by SymPy.'
(P/'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf8')
# Required integrity checks before completing the attempt.
assert len(rows)==16 and all(r['problem_id']=='F0087' for r in rows)
assert not any(r['status']=='conjecture' and '(MB)' in r['claim'] for r in rows)
assert 'exit_code=0' in (P/'fusion_lean_check.log').read_text(encoding='utf8')
lean=(P/'FusionExponents.lean').read_text(encoding='utf8')
assert 'sorry' not in lean and 'native_decide' not in lean and 'import Mathlib\n' not in lean
for fn in ['fusion_checks.json','distinct_fusion_checks.json','nearest_neighbor_graph_checks.json']:json.loads((P/fn).read_text(encoding='utf8'))
assert all((P/fn).stat().st_size>0 for fn in ['SECOND_ATTEMPT.md','ATTEMPT.md','LITERATURE.md','CLAIMS.jsonl'])
old=(P/'STATUS.md').read_text(encoding='utf8').splitlines();logs=old[3:]
status='''STATE: DONE
NEXT: Prove the corrected nearest-neighbor Onsager estimate OB uniformly across collision scales, or establish mixed singular/smooth determinant asymptotics; pinned phase and half-integer endpoint also remain.
VERDICT: PARTIAL
'''+ '\n'.join(logs)+'''\n2026-10-11: Second attempt recorded two new approaches; pursued compactification/charge fusion and asked the brain directly about the collision gap.
2026-10-11: Refuted the old matching bound MB for every nonzero principal charge, including an eight-distinct-face example at s=1/4. Proved a local fused mean modulus >=1/4 and its distant-cluster correlation limit >=1/16.
2026-10-11: Proved vanishing integrated contribution of the fully fused bad regions, nearest-neighbor-majorant integrability with collision tails, and conditional convergence under the repaired OB hypothesis.
2026-10-11: Exact algebra, finite tilings, Fourier checks, functional-graph checks and new Lean scalar lemmas completed. Corrected the previous MB conjecture record to a counterexample.
2026-10-11: Second attempt completed with VERDICT PARTIAL. OB for general n, the original pinned renormalized limit, and the half-integer endpoint remain unproved; no counterexample to Kenyon's question is asserted.
'''
(P/'STATUS.md').write_text(status,encoding='utf8')
assert (P/'STATUS.md').read_text(encoding='utf8').splitlines()[0] == 'STATE: DONE'
print('Completed second attempt; 16 reconciled claims; final STATE DONE / VERDICT PARTIAL.')
