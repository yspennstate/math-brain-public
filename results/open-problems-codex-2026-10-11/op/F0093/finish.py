from pathlib import Path
import json
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf-8-sig');s += '\nFinal formal verification: `lake env lean ~/brain_workers/TRIO_1011/op/F0093/FiniteCovariance.lean` ran from `~/lean_verify` and exited 0 in 102.984 seconds. All three named algebraic theorems passed Lean kernel checking. No sorry, axiom declarations, native_decide, or whole-Mathlib import occur in the checked file. The failed first run is retained separately in `lean_initial_error.txt`.\n';p.write_text(s,encoding='utf8')
p=Path('CLAIMS.jsonl')
with p.open('a',encoding='utf8') as f:f.write(json.dumps({'problem_id':'F0093','claim':'The two-point conditional covariance equals w(1-w)(a-b)^2 and is nonnegative for 0<=w<=1; the scalar tensor-difference identity holds.','status':'proved','proof_location':'FiniteCovariance.lean','remaining_gap':'Formalization covers these finite algebraic identities only, not the conjecture or full probabilistic reductions.','checks':'Lean 4 via lake env lean from ~/lean_verify; exit_code=0; no sorry/native_decide; lean_check.txt.'})+'\n')
Path('STATUS.md').write_text('''STATE: DONE
NEXT: Obtain a quantitative n-uniform bound on the shared-mask information or endpoint matrix trace for Grigorchuk SRW.
VERDICT: PARTIAL

2026-10-12: Verified Kalai Section 3.3.4 on PDF page 22. Bounded arXiv, Crossref, Semantic Scholar (including source citations), GitHub and OpenAlex searches recorded; OpenAlex repeatedly rate-limited. No exact full-conjecture solution found. The 2025 virtually abelian theorem answers the existential SRW question in a special case, but not the specified Liouville/no-virtual-homomorphism conjecture.
2026-10-12: Proved a shared-information sufficient criterion, an exact positive endpoint matrix/chi-squared criterion, and exponential noise sensitivity on every fixed finite quotient, including periodic quotients. Corrected two invalid information-theoretic inferences in the prior ledger. Full target and Grigorchuk case remain unresolved.
2026-10-12: Deterministic endpoint recursion on five models and exact Fraction checks on two S3 walks passed. Three finite algebraic lemmas passed Lean kernel checking, exit 0. Complete proofs, hostile-referee audit, numerical outputs and precise remaining gaps are saved. This attempt is concluded at PARTIAL, not SOLVED.
''',encoding='utf8')
# Final consistency and artifact check.
assert Path('STATUS.md').read_bytes().startswith(b'STATE: DONE\n')
for line in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines():
 obj=json.loads(line);assert obj['problem_id']=='F0093';assert obj['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture']
lean=Path('FiniteCovariance.lean').read_text(encoding='utf8');assert 'sorry' not in lean and 'native_decide' not in lean and '\nimport Mathlib\n' not in lean
assert Path('lean_check.txt').read_text().startswith('exit_code=0')
print('Final artifacts consistent; STATE DONE, VERDICT PARTIAL; 7 claims.')
