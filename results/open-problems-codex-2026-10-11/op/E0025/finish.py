import pathlib,json
p=pathlib.Path(__file__).resolve().parent
lean=(p/'lean_check.txt').read_text(encoding='utf8')
assert lean.startswith('exit_code=0\n'), 'Lean has not passed; do not finalize'
src=(p/'Weights.lean').read_text(encoding='utf8')
assert 'sorry' not in src and 'native_decide' not in src
status='''STATE: DONE
NEXT: General case remains open; a future attempt must find finite-energy control without prescribed lacunary good bands.
VERDICT: PARTIAL

2026-10-12: Confirmed Question 5, PDF p. 25; pure jump means driftless in the subordinator statement. Verified Definition 2.28 and corrected the earlier intake reading of Theorem 2.29: it is a decomposition theorem.
2026-10-12: Searched arXiv, OpenAlex (including works citing the source), Crossref, Semantic Scholar, and GitHub. No exact solution identified. arXiv and Semantic Scholar API searches were rate-limited; limitations and every query are in LITERATURE.md.
2026-10-12: Proved an explicit type-(1/4,3/4) driftless infinite-activity subordinator satisfies (H) despite failing every Rao bound. Full proof and hostile-referee audit are in ATTEMPT.md; this uses the survey's finite-energy criterion and makes no novelty claim.
2026-10-12: Ran short 100-digit supplementary computations; corrected normalization of tiny quadrature integrands. Final results agree with analytic estimates.
2026-10-12: Lean 4 verified the reciprocal energy-weight comparison and rational exponent margins, with no sorry or native_decide. The full analytic proof is not formalized.
2026-10-12: Closed this bounded attempt as PARTIAL. Neither universal statement has a proof or counterexample here. The remaining gap is explicit in ATTEMPT.md.
'''
(p/'STATUS.md').write_text(status,encoding='utf8')
with (p/'ATTEMPT.md').open('a',encoding='utf8') as f:
 f.write('\n## Lean check\n\n`Weights.lean` passed `lake env lean` from ~/lean_verify (exit code 0; see lean_check.txt). The checked statements are the real reciprocal-weight comparison used in section 6 and five exact rational inequalities used for exponent margins. No `sorry` or `native_decide` occurs. The first run needed an explicit Mathlib.Data.Real.Basic import; the second rejected a redundant ring tactic after field_simp had already closed the goal. Both were corrected in the final passing version. This check does not formalize the analytic or probabilistic theorems.\n')
claim={'problem_id':'E0025','claim':'The algebraic energy-weight inequality 1/b <= k*(a/b^2), given b>0 and b<=k*a, and five rational exponent margins are Lean-checked.','status':'proved','proof_location':'Weights.lean; lean_check.txt','remaining_gap':'Only this algebraic step is formalized, not the full special-case proof.','checks':'lake env lean, exit 0; no sorry; no native_decide.'}
with (p/'CLAIMS.jsonl').open('a',encoding='utf8') as f: f.write(json.dumps(claim)+'\n')
claims=[json.loads(x) for x in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert all(x['problem_id']=='E0025' for x in claims)
assert (p/'STATUS.md').read_bytes().splitlines()[0]==b'STATE: DONE'
print('Final file audit passed; STATE: DONE; VERDICT: PARTIAL; claims:',len(claims))
