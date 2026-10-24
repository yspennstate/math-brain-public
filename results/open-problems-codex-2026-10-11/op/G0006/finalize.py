import pathlib,json
r=pathlib.Path.cwd()
p=r/'ATTEMPT.md';s=p.read_text(encoding='utf-8-sig')
s=s.replace('It constructs every nonempty state, recovery rates, internal birth rates, and rates of exiting arrows from occupied leaves, then solves the rational linear system exactly.', 'It lumps the nonempty states into the nine classes (c,l), where c is the center occupancy and l is the number of infected leaves. This lumping is exact: center recovery has rate c, leaf recovery rate l, center birth rate (1-c)*lambda*l, leaf birth rate c*lambda*(4-l), and successful exit rate 3*lambda*l. All rates depend only on (c,l), so these counts form a Markov chain. Its transient generator determines the exit probabilities uniquely by Lemma 4. The script solves that nine-state rational linear system exactly.')
s=s.replace('These exact rational statements are separately checked in CertificateChecks.lean, if and only if the accompanying lean_check.txt reports exit 0.', 'These exact rational statements are separately kernel-checked in CertificateChecks.lean; lean_check.txt reports exit 0.')
s=s.replace('See lean_check.txt for actual success/failure.', 'The run in lean_check.txt exited 0 in 99.820 seconds. An initial BOM-related parser failure is preserved in lean_check_first.txt; it was fixed by saving the Lean source as UTF-8 without a BOM, then rerunning. All five displayed lemmas passed.')
s+='\nExact computation outputs: q_star(1/8)=212317/1809007; q_star(1/4)=174699/592418; q_star(2/5)=3285432/7123727; q_star(1/2)=11906/21991. In all four cases the exact residual is zero, all nine state probabilities lie in (0,1), and the prescribed two-step lower bound holds. Memory use is negligible (a 9-by-9 rational matrix). No thermodynamic claim follows from these finite values.\n'
p.write_text(s,encoding='utf8')
p=r/'CLAIMS.jsonl'; rows=[json.loads(l) for l in p.read_text(encoding='utf8').splitlines()]
for c in rows:
 if 'CertificateChecks.lean' in c['checks'] or 'submitted to Lean' in c['checks']:
  c['checks'] += ' Lean 4.33.1 run: exit 0; supporting finite/algebraic lemmas only, not probability formalization.'
p.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in rows),encoding='utf8')
# Final consistency checks.
for fn in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','CertificateChecks.lean','lean_check.txt','exit_results.json']:
 assert (r/fn).is_file(), fn
assert len(rows)==8
assert all(c['problem_id']=='G0006' and c['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'} for c in rows)
lean=(r/'CertificateChecks.lean').read_text(encoding='utf8')
assert 'sorry' not in lean and 'native_decide' not in lean and 'import Mathlib\n' not in lean
assert 'Exit: 0' in (r/'lean_check.txt').read_text(encoding='utf8')
results=json.loads((r/'exit_results.json').read_text(encoding='utf8'))
assert all(v['exact_linear_residual_zero'] and not v['certificate_passes'] for v in results['results'])
status='''STATE: DONE
NEXT: Obtain a genuinely stronger spatial-connectivity bound near lambda_c; the local-exit criterion studied here provably cannot reach that regime.
VERDICT: PARTIAL

2026-10-11: Verified Fernley--Jacob source, including per-edge normalization, lattice quantifiers, and PDF p. 3 question. Queried arXiv, OpenAlex, Crossref, Semantic Scholar and GitHub. No exact literature solution found; OpenAlex/Semantic Scholar rate limits and one unavailable lead PDF are documented.
2026-10-11: Proved elementary product upper comparison and lower bound on lambda_p; derived the stationary pair identity. Constructed a dependent percolating law with arbitrarily small density and mean occupied degree below 2, refuting auxiliary shortcuts only.
2026-10-11: Proved a finite local-exit nonpercolation criterion and proved it cannot work for any lambda >= 1/(2d), thus cannot certify the conjectured supercritical gap. Computed five-site exit probabilities by an exact nine-state rational system.
2026-10-11: Lean 4.33.1 checked all five supporting algebraic/rational lemmas, exit 0. Full probabilistic proofs, limitations and remaining gap are in ATTEMPT.md. Final file/claim consistency checks passed. The requested strict inequality remains unproved; this is closure of the bounded attempt, not closure of the open problem.
'''
(r/'STATUS.md').write_text(status,encoding='utf8')
(r/'record_checks.txt').write_text('Final consistency checks passed. Eight claim records. Required files present. Lean exit 0. Exact finite-system residuals zero. Original target recorded as conjecture only.\n',encoding='utf8')
print(status)
