from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
lean=(ROOT/'lean_check.log').read_text(encoding='utf8')
assert lean.startswith('exit_code: 0\n'), 'Do not finalize before the complete Lean file passes.'
text=(ROOT/'FiniteAlgebra.lean').read_text(encoding='utf8')
assert 'sorry' not in text and 'native_decide' not in text
lit=ROOT/'LITERATURE.md'
october=(ROOT/'october_literature.md').read_text(encoding='utf8')
if '## October 2026 GitHub leads' not in lit.read_text(encoding='utf8'):
    lit.write_text(lit.read_text(encoding='utf8')+'\n'+october,encoding='utf8')
attempt=ROOT/'ATTEMPT.md'
a=attempt.read_text(encoding='utf8')
if 'Final Lean result:' not in a:
    a+='\nFinal Lean result: `lake env lean` from `~/lean_verify` exited 0 for the complete `FiniteAlgebra.lean` file. All five algebraic theorems are kernel-checked, with no sorry or native_decide. The first two runs exposed only missing imports (Omega and Finset.mul_sum); both imports were corrected before the successful run. This does not formalize the full probabilistic statements.\n'
attempt.write_text(a,encoding='utf8')
claims=ROOT/'CLAIMS.jsonl'
rows=[json.loads(line) for line in claims.read_text(encoding='utf8').splitlines()]
for row in rows:
    if row['proof_location']=='ATTEMPT.md section A':
        row['checks'].append('Lean kernel checked integer sign second difference in FiniteAlgebra.lean')
    if row['proof_location']=='ATTEMPT.md section A2':
        row['checks'].append('Lean kernel checked mixed-ratio polynomial identity and transformed derivative numerator positivity; the complete rational derivative identity is checked by exact SymPy arithmetic')
    if row['proof_location']=='ATTEMPT.md section B' and row['status']=='proved':
        row['checks'].append('Lean kernel checked stochastic-row entry determinism from vanishing cross products')
rows.append({'problem_id':'F0118','claim':'For q1=3 or 4 and all sufficiently large b, reconstruction for q1 at fixed positive lambda implies reconstruction for every q2>q1.','status':'proved_special_case','proof_location':'ATTEMPT.md section C, Additional implication; LITERATURE.md Mossel–Sly–Sohn Theorem 1.12','remaining_gap':'Uses a published large-degree threshold theorem; does not settle arbitrary degrees or q1>=5. The recent all-degree q1=4 preprint is recorded separately as a scoped lead.','checks':['Offspring-family hypotheses verified using a floor/ceiling family with uniform bounded X_d/d','Reconstruction implies b*lambda^2>1 by the cited theorem','Independently proved all-q sufficient bound supplies the conclusion']})
claims.write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows),encoding='utf8')
(ROOT/'STATUS.md').write_text('''STATE: DONE
NEXT: Establish or refute pairwise-TV comparison at arbitrary depth for nondivisible alphabets in 1/b < lambda <= 1/sqrt(b).
VERDICT: PARTIAL

2026-10-12: Verified Conjecture 4 in Mossel's survey, PDF p.10, and its signed positive eigenvalue and ergodicity assumptions.
2026-10-12: Queried arXiv, OpenAlex, Crossref, Semantic Scholar and GitHub; followed relevant 2026 GitHub manuscripts. No retrieved theorem solves the full stated question. OpenAlex citing-work lookup was blocked by HTTP 429; Semantic Scholar searches were rate-limited or source lookup returned 404. Every request is in LITERATURE.md/search_log.jsonl.
2026-10-12: Proved finite-depth TV monotonicity at depth one for arbitrary b and at depth two for b=2, for every integer alphabet size and every 0<lambda<1. Wrote full proofs and an explicit positive derivative certificate. Re-proved standard bounds, divisible-alphabet case and the independent-recoloring obstruction; derived q1=3,4 large-degree cases from the verified published theorem.
2026-10-12: Checked 95 finite laws and 80 adjacent-q comparisons with exact integer/rational arithmetic; all passed. Depth-two symbolic formula independently matches all 35 depth-two laws. No infinite-depth conclusion drawn from these tests.
2026-10-12: Lean 4 kernel checked five algebraic lemmas after correcting two missing imports. Complete file exits 0; no sorry or native_decide. The probability arguments and full conjecture are not formalized.
2026-10-12: Stopped after referee audit. Full monotonicity remains unproved and no counterexample was obtained; the precise remaining gap is in ATTEMPT.md. DONE denotes completion of this bounded attempt, not solution of F0118.
''',encoding='utf8')
rows_boundary={'problem_id':'F0118','claim':'At b*lambda^2=1 with b>=2 and target alphabet q2>=5, the target Potts process reconstructs, so the proposed implication holds for every smaller alphabet.','status':'proved_special_case','proof_location':'ATTEMPT.md section C, Critical boundary; LITERATURE.md Sly Theorem 1.2','remaining_gap':'Does not compare two target thresholds in the strictly sub-Kesten-Stigum range; target q2=4 remains outside this consequence.','checks':['Retrieved Sly Theorem 1.2 has lambda_+(q2,b)<b^(-1/2)','The critical lambda is strictly above the positive reconstruction threshold']}
with claims.open('a',encoding='utf8') as f: f.write(json.dumps(rows_boundary,ensure_ascii=False)+'\n')
assert len(rows)==9
print('Finalized DONE / PARTIAL; ten valid claim records; Lean exit 0.',flush=True)
