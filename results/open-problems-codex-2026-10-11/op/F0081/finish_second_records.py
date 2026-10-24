from pathlib import Path
import json
p=Path('SECOND_ATTEMPT.md');s=p.read_text(encoding='utf8')
s=s.replace('subject to the finite-to-infinite argument written below','by the finite-to-infinite argument written below')
s=s.replace('Before this is treated as an improved theorem, the finite insertion lemma, variance argument, and localization are being checked independently by numerical and finite algebra tests. Full F0081 remains PARTIAL even if all those checks pass.','The finite insertion lemma, variance argument, and localization were audited as above. The finite numerical and algebra checks below passed. Full F0081 remains PARTIAL: these checks do not supply its missing lower half in d>=3.')
a=json.loads(Path('second_experiments.json').read_text());b=json.loads(Path('exhaustive_insertion.json').read_text())
s+='''
## G. Independent checks completed

1. `probe_monotonicity.py`: 4500 planar finite comparisons of red insertion passed both colourwise length inequalities.
2. `second_experiment.py`: 4500 new configurations in dimensions 1,2,3, with possibly unequal red/blue counts, checked all inter-edge thresholds. Every full signed residual-measure change was nonnegative with total mass exactly 1. No failure was found.
3. `exhaustive_insertion.py`: enumerated all 720 strict edge orders for insertion into a 2-red/2-blue instance, and all 40320 strict edge orders for insertion into a 3-red/2-blue instance. Every order and every integer threshold passed both comparative statics and the one-atom statement. These weights need not be Euclidean; the proof applies to symmetric bipartite preference weights without a triangle inequality. This is an exhaustive finite check, not a proof for arbitrary sizes.
4. Independent Poisson counts on flat tori (rather than balanced binomial counts) were sampled 350 times each in d=2 and d=3. Cubes of side 2 at threshold 2*sqrt(d) passed monochromatic residual checks. Descriptive second moments are below the theoretical bound; no inference rests on Monte Carlo confidence.

| d | cube volume | measured mean charge | measured second moment | proved second-moment upper bound |
|---|---|---|---|---|
'''
for x in a['records']:s+=f"| {x['d']} | {x['volume']:.0f} | {x['mean']:.8f} | {x['second_moment']:.8f} | {x['variance_bound']:.0f} |\n"
s+=f'''
Random check runtime: {a['elapsed']:.2f} seconds. Exhaustive check runtime: {b['elapsed']:.2f} seconds. Jobs were small (at most a few hundred points per colour, finite matrices well below 1 GB). Saved raw files: second_experiments.json, exhaustive_insertion.json.

`InsertionChecks.lean` compiled with exit code 0; second_lean_check.log records the invocation. Three arithmetic lemmas formalize the unique-unit-change step, restriction to a zero-or-one window increment, and equality of its square to itself. Imports are only Mathlib.Data.Int.Basic and Lean.Elab.Tactic.Omega. No sorry or native_decide. These lemmas are checked by the Lean kernel; the entire stochastic argument is not formalized.

The missing d>=3 endpoint lower bound has not been tested by pretending that finite-volume residual variance has a scale-uniform positive lower bound. Even a volume upper bound plus a local Poisson input does not force such a lower bound, because conservative redistribution can move covariance to spatial scales larger than r. Neither the earlier fourth-moment criterion nor association supplies the needed lower first absolute moment here.
'''
p.write_text(s,encoding='utf8')
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8')
s=s.replace('# F0081 attempt — 2026-10-11','# F0081 attempt — 2026-10-11\n\n**Second-attempt update:** [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md) proves the upper tail bound C_d r^(-d/2) in every dimension and, using the source lower theorem, the complete positive-moment criterion in d=2. The remaining gap is critical-moment divergence in d>=3. Sections 1-7 preserve the first attempt; statements below that no unconditional bound was improved describe that earlier stage.')
s+='''
## 9. Second attempt completed

The selected insertion/variance route succeeded in proving the variance upper bound from the first attempt, with constant 2, and therefore the conjectured upper-tail exponent. Full proofs, independent checks, and the precise remaining lower-half gap are in SECOND_ATTEMPT.md sections A-G. The all-dimensions problem is still PARTIAL. For d>=3, proving E*X^(d/2)=infinity would finish the conjectured positive-moment criterion; no proof of this has been obtained. The upper result and d=2 special case are mathematical derivations in this attempt, not claimed as solutions found in print.
'''
p.write_text(s,encoding='utf8')
claims=[
('One red insertion in any finite generic bipartite stable matching changes the signed threshold-residual measure by exactly one positive atom; blue insertion gives one negative atom.','proved','SECOND_ATTEMPT.md sections A-B','Finite deterministic lemma; does not establish the endpoint lower tail.'),
('For two independent intensity-one Poisson processes on any flat torus, signed threshold-residual charge in a Borel window Q has mean zero and second moment at most 2|Q|.','proved','SECOND_ATTEMPT.md section C','No matching positive lower bound is provided.'),
('For critical stable two-colour Poisson matching on Euclidean R^d, E D_r(Q)^2 <= 2|Q| for every fixed r>0 and bounded deterministic Q.','proved','SECOND_ATTEMPT.md section D','Second-moment lower bound and endpoint lower moment remain unresolved.'),
('In every d>=1, the stable two-colour critical Poisson matching satisfies P*(X>r) <= 2^((d-1)/2)/sqrt(kappa_d) * r^(-d/2), hence E*X^alpha is finite for every positive alpha<d/2.','proved','SECOND_ATTEMPT.md section E','In d>=3 this does not prove divergence at alpha=d/2.'),
('In dimension d=2, for stable matching of independent intensity-one red and blue Poisson processes, E*X^alpha is finite exactly for positive alpha<1.','proved_special_case','SECOND_ATTEMPT.md section E; source Theorem 2 PDF p.4','Full F0081 still requires the critical lower moment in every d>=3.'),
('All 41040 enumerated strict finite bipartite edge orders and 4500 additional Euclidean insertion samples obeyed the one-atom residual insertion property; independent Poisson torus samples respected the proved variance upper bound.','numerical_evidence','SECOND_ATTEMPT.md section G; second_experiments.json; exhaustive_insertion.json','Finite checks do not establish the remaining infinite critical lower moment.')]
old=[json.loads(x) for x in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for x in old:
 if x['claim'].startswith('Uniform second moment comparable'):
  x['remaining_gap']='The upper second-moment inequality is now proved in SECOND_ATTEMPT.md; the lower second-moment and fourth-moment hypotheses remain unproved.'
for claim,status,loc,gap in claims:old.append(dict(problem_id='F0081',claim=claim,status=status,proof_location=loc,remaining_gap=gap,checks='Complete proofs and hostile-referee audit in SECOND_ATTEMPT.md; 41040 exhaustive finite orders, 4500 insertion samples, Poisson torus checks, Lean finite arithmetic exit 0. Lean does not formalize the stochastic argument.'))
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in old),encoding='utf8')
Path('second_attempt_notes.md').write_text('COMPLETED: Conservative insertion and product variance proof establish subcritical moment finiteness in all d and full criterion for d=2. Remaining gap: E*X^(d/2)=infinity for d>=3. See SECOND_ATTEMPT.md.\n',encoding='utf8')
print('Updated proofs and claim ledger:',len(old),'claims')
