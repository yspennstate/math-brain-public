import pathlib,json
root=pathlib.Path(__file__).resolve().parent
(root/'STATUS.md').write_text('''STATE: DONE
NEXT: Prove the unresolved neighbor-refresh dual occupation limit for finite nonempty starts, then extend beyond the single-infection primal subclass.
VERDICT: PARTIAL

2026-10-11: Exact source Conjecture 1 confirmed, including spin convention, all-q quantifier and arbitrary nonempty initial-law hypothesis.
2026-10-11: Searched arXiv, OpenAlex, Crossref, Semantic Scholar and GitHub. No exact later resolution verified. OpenAlex and Semantic Scholar repeatedly rate-limited; their citation results are unavailable, not negative evidence.
2026-10-11: Read the brain, intake attempts and the repository's D0027 handoff read-only. Corrected the old attempt's false survival obstruction and unsupported density-regularization equivalence.
2026-10-11: Proved deterministic-start reduction; finite-seed nonextinction and persistent singularity; total-variation convergence for every nu absolutely continuous relative to pi; Cesaro stationary-mixture reduction and occupation upper bound; finite-interval convergence; non-attractiveness; exact single-infection dual reduction. None solves the full singular-start conjecture.
2026-10-11: Exact finite rational computations passed. FiniteChecks.lean compiled successfully using decide +kernel and no sorry/native_decide, certifying only finite/combinatorial facts.
2026-10-11: Referee audit complete in REFEREE.md. Present attempt exhausted with precise gaps in ATTEMPT.md. DONE means this attempt is finished; the full problem is not solved.
''',encoding='utf-8')
claims=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
for c in claims:
 if 'semigroup does not preserve' in c['claim']:
  c['checks']='Explicit generator derivative witness; FiniteChecks.lean orderWitness and healingPreservesAnInfection compiled with exit code 0. Only these combinatorial facts are Lean-checked.'
assert all(c['problem_id']=='D0026' and c['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'} for c in claims)
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','CHECKS.md','REFEREE.md']:
 p=root/name;assert p.is_file() and p.stat().st_size>0
assert (root/'STATUS.md').read_bytes().splitlines()[0] == b'STATE: DONE'
print('Final records validated:',len(claims),'claims; STATE DONE / VERDICT PARTIAL')
