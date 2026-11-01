import pathlib,json
p=pathlib.Path('.')
lean=(p/'second_lean_check.txt').read_text(encoding='utf8')
assert lean.startswith('exit_code=0\n')
claims=[json.loads(s) for s in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==15,len(claims)
allowed={'proved','counterexample','proved_special_case','numerical_evidence','conjecture'}
for x in claims:
 assert set(x)=={'problem_id','claim','status','proof_location','remaining_gap','checks'}
 assert x['problem_id']=='P0030' and x['status'] in allowed
for name in ['STATUS.md','ATTEMPT.md','LITERATURE.md']:
 q=p/name;q.write_text(q.read_text(encoding='utf-8-sig'),encoding='utf8')
a=(p/'ATTEMPT.md').read_text(encoding='utf8')
for section in ['Two approaches not pursued','## Lemma E','## Lemma G','## Theorem J','## Example I','## Example L','## Reduction M','Updated precise remaining gap']:assert section in a,section
lean_src=(p/'HellingerFilling.lean').read_text(encoding='utf8')
assert 'sorry' not in lean_src and 'native_decide' not in lean_src
with (p/'ATTEMPT.md').open('a',encoding='utf8') as out:out.write('''

Second-attempt closing verdict (2026-10-12): PARTIAL. Both new approaches were recorded and the product-domination approach was carried through to exact finite shifts in additional special cases, with explicit auxiliary-randomness scope. The general compatibility questions are still unresolved. The next mathematical step would be to prove equality on the real-shift-invariant sigma field using only the independent cut plus Brownian certifications, or exhibit an invariant-null-event obstruction satisfying those hypotheses. A finite-window limit, marked-product singularity, or a failed integer-shift condition is insufficient.
''')
with (p/'LITERATURE.md').open('a',encoding='utf8') as out:out.write('\nReduction M applies the cited invariant-sigma-field theorem to the continuous centered-window-state process, with a full proof of the recentering/ordinary-shift correspondence in ATTEMPT.md. The new finite-shift results are conditional special cases obtained from classical tools; none is recorded as a published solution to Problems 7.1–7.3.\n')
(p/'STATUS.md').write_text('''STATE: DONE
NEXT: Derive equality on real-shift-invariant events from the exact independent-cut/Brownian hypotheses, or construct a Wiener-null invariant obstruction satisfying them; unresolved here.
VERDICT: PARTIAL

2026-10-12: First attempt confirmed the source and proved stationary-increment and finite-window total-variation results; full compatibility problem remained unresolved.
2026-10-12: Reopened at user request. Reread ATTEMPT.md and gap; recorded two new approaches: invariant-event shift coupling, and Kakutani comparison of full stopped-piece products. Queried the brain for the gap, named shift-coupling results and Hellinger product equivalence; read the linked filling card in full.
2026-10-12: Proved the needed reverse-direction filling lemma and full-law absolute-continuity stability under finite random centering, explicitly allowing auxiliary randomness. Proved the one-way product-domination lemma in full.
2026-10-12: Proved a stronger special case: only negative stopped pieces need summable Hellinger discrepancies from an iid finite-mean reference; positive pieces can be arbitrary allowed stopping rules. Proved a bounded nonidentical path-dependent example and a single infinite-mean hitting-piece exception.
2026-10-12: Checked the invariant-sigma-field criterion against Pitman–Tang Theorem 5.9 (Thorisson) and wrote the exact real-recentering invariant-event reduction. No proof that source hypotheses force that criterion.
2026-10-12: Refuted a shortcut from BBM to summability for the supplied marking using harmless alternating deterministic durations. Proved the periodic finite-mean positive control by grouping. A bounded nonperiodic likelihood probe through 128 increments found no counterexample signal, with no asymptotic conclusion claimed.
2026-10-12: Exact rational filling tests passed on 140 finite cycles; nonergodic control retained mass 1/2. Product identities, affinity quadratures and mean-bias simulation checked the explicit example. Lean supporting algebra exited 0, with narrow imports and no sorry/native_decide; no full probability theorem is claimed formalized.
2026-10-12: Second attempt closed honestly as PARTIAL. Both approaches, complete new proofs, all searches, 15 total typed claims and the precise remaining gap are saved. None of Problems 7.1–7.3 is claimed solved or solved in literature.
''',encoding='utf8')
assert (p/'STATUS.md').read_bytes().splitlines()[0]==b'STATE: DONE'
print('validated second attempt: DONE / PARTIAL; 15 claims; Lean exit 0; new approaches and remaining gap present')
