from pathlib import Path
import json

root = Path(__file__).resolve().parent
def append(name, text):
    with (root / name).open('a', encoding='utf-8') as f:
        f.write('\n\n' + text.strip() + '\n')

log = json.loads((root / 'second_search_log.json').read_text(encoding='utf-8'))
searches = '\n'.join(f"- {r['date']}, {r['service']}: `{r['url']}`; HTTP {r['status']}, {r['bytes']} bytes." for r in log)
append('LITERATURE.md', '''## Second serious attempt, 2026-10-11

The additional searches and fetches were performed with Python, not a built-in web search. Exact URLs and response status:
''' + searches + '''

Gap-directed, read-only brain queries:
- math_recall.py "contact process percolation critical exponent derivative susceptibility healthy upper invariant tree"
- brain.py recall "contact process percolation critical derivative mistakes"
- math_recall.py "Broman Steif downward movability contact process stochastic domination independent thinning"
The results cautioned about susceptibility, exchanging derivative limits, and qualitative stochastic domination. No matching derivative theorem was supplied. The returned hints were not treated as verdicts.

Verified additional references:
1. Erik I. Broman and Jeffrey E. Steif, *Dynamical stability of percolation for some interacting particle systems and epsilon-movability*, Annals of Probability 34(2) (2006), 539--576. DOI: 10.1214/009117905000000602. arXiv:math/0605641. Theorem 1.11, PDF p. 7, gives downward movability of the ordered upper invariant contact-process measures on bounded-degree graphs. Specifically nu_lambda1 is dominated by an independently thinned nu_lambda2 for some positive deletion probability, when 0<lambda1<lambda2. Complementation reverses the order. Proposition 4.1 and the contact-process application were read to check that direction. This does NOT identify independent enhancement criticality of the healthy law at its parameter threshold, or prove either requested derivative assertion. A lead only.
2. Thomas M. Liggett and Jeffrey E. Steif, *Stochastic domination: the contact process, Ising models and FKG measures*, Annales de l'Institut Henri Poincare, Probabilites et Statistiques 42(2) (2006), 223--243. DOI: 10.1016/j.anihpb.2005.04.002. arXiv:math/0504530. Equation (5), PDF p. 7, states that nu satisfies downward FKG, explicitly for the contact process on a general graph; it cites van den Berg, Haggstrom and Kahn. Definition 1.1 defines association after conditioning a finite set to zero. This input proves the conditional-neighbor covariance inequality in SECOND_PROOFS.md, not the original derivative assertion. The paper also warns against stronger conditional positivity assumptions; no uniform contact-process insertion constant is inferred.
3. Primary reference as printed in Liggett--Steif's bibliography: J. van den Berg, O. Haggstrom and J. Kahn, *Some conditional correlation inequalities for percolation and related processes*, Random Structures and Algorithms, then listed as 'to appear'. This primary paper was not separately fetched in this second attempt; the general-graph statement was checked in Liggett--Steif itself.

No paper inspected in this second attempt states and proves the full G0007 question. No SOLVED_IN_LITERATURE classification is made. The new proofs are author-derived and are written out in SECOND_PROOFS.md.
''')

append('ATTEMPT.md', '''## Second serious attempt completed, 2026-10-11

Two previously untried approaches were formulated in SECOND_ATTEMPT.md: parameter/noise comparison via Broman--Steif, and the exact all-healthy stationary generator hierarchy. Complete new proofs, hypotheses, limitations, and the audit of the earlier argument are in SECOND_PROOFS.md.

New proved contact-process results: exact all-healthy pair/triple identities, conditional healthy-degree variance and covariance, h>=1/[lambda*d-1/(d-1)], and lambda_p^c(T_d)>d/[2(d-1)] for d>=3. The denominator's positivity follows directly from h[lambda*d-1/(d-1)]>=1. The strict threshold conclusion uses the earlier author proof of critical healthy nonpercolation. Further exact bounds are lambda_p^c(T_4)>2/3+25/553472 and lambda_p^c(T_5)>5/8+16807/84321000. Their complete stationary isolated-site proof is in SECOND_PROOFS.md Section 3.4.

A different-model construction proves that invariant ergodicity, downward FKG, uniform finite energy, weak continuity and even linear independent-noise comparisons do not identify the enhancement threshold of a critical parameter law. This countermodel is NOT a contact-process counterexample. It has a continuous, nondifferentiable onset with finite endpoint susceptibility and positive independent-enhancement threshold. All its claims and the limitation concerning finite-cylinder differentiability are explicit in SECOND_PROOFS.md Section 2.

Remaining gap: for the actual contact-process healthy law, prove theta_H(c-h)=o(h), differentiability on a left neighborhood and derivative limit zero, or disprove one of these. For the infected law, establish a positive critical right slope or another obstruction to continuous differentiability. The hierarchy introduces disconnected correlations and multiple shapes already at four sites and supplies no uniform radius-response bound. No independent-enhancement criticality or sharpness theorem for the actual critical healthy law was proved. Threshold bounds do not settle either derivative assertion. Overall VERDICT remains PARTIAL; the earlier continuity proofs are retained.
''')

append('SECOND_ATTEMPT.md', '''## Final audit and disposition

Complete proofs are in SECOND_PROOFS.md. Both approaches were pursued: the initially more promising noise approach led to an explicit countermodel to its missing inference; the hierarchy approach yielded rigorous new threshold bounds. All four finite/algebraic check scripts completed successfully. These checks support the written proofs and do not certify the infinite-volume derivative assertions.

Correction to the denominator note above: no external lambda_1 lower bound is needed. Algebra gives h[lambda*d-1/(d-1)]>=1 directly, hence positivity of the bracket. This is the argument used in the complete proof.

Both derivative clauses remain open in this work. Future work needs an actual contact-process enhancement/response theorem or uniform large-radius correlation control. Closing this second attempt with STATE: DONE and VERDICT: PARTIAL records completion of the attempt, not solution of the full problem.
''')

new_claims = [
 ('For the upper invariant contact process, the finite all-healthy generator hierarchy and the exact pair/triple, healthy-degree variance and conditional neighbor covariance identities hold.', 'proved', 'SECOND_PROOFS.md Sections 3.1 and 3.5', '', 'Bounded-cylinder stationarity proof; independent SymPy simplification in second_symbolic_checks.json.'),
 ('For lambda>lambda_1 on T_d, the healthy density satisfies h>=1/[lambda*d-1/(d-1)] and the healthy conditional mean degree is at least d/[lambda*(d-1)].', 'proved', 'SECOND_PROOFS.md Section 3.2', '', 'General-graph downward FKG verified in Liggett--Steif equation (5); denominator positivity derived, not assumed.'),
 ('For every d>=3, lambda_p^c(T_d)>d/[2*(d-1)].', 'proved', 'SECOND_PROOFS.md Section 3.3', 'Strictness uses the earlier author proof of critical healthy nonpercolation; original derivative questions remain unresolved.', 'Exact degree inequality and invariant-tree reciprocal-cluster identity; complete proof.'),
 ('lambda_p^c(T_4)>2/3+25/553472 and lambda_p^c(T_5)>5/8+16807/84321000.', 'proved', 'SECOND_PROOFS.md Section 3.4', 'These bounds do not determine the critical derivative.', 'Exact stationary Poisson isolated-site event; rational constants and positive margins in second_threshold_bounds.json.'),
 ('A different, non-contact-process invariant ergodic downward-FKG finite-energy family on T_3 has linear independent-noise comparisons but a continuous nondifferentiable percolation onset, finite endpoint susceptibility and strictly positive endpoint independent-enhancement threshold.', 'counterexample', 'SECOND_PROOFS.md Sections 2.1--2.4', 'Counterexample only to the proposed abstract noise-criticality inference, not to G0007; the family lacks contact-process stationarity and local differentiability across its threshold.', 'Full explicit bond-cluster-label construction; exact rational tests in second_countermodel_checks.json; 256 finite-star lattice checks in second_fkg_checks.json.'),
 ('If the actual critical healthy law has a linear parameter-to-enhancement comparison and linear enhanced root percolation lower bound, then its critical healthy order parameter is not differentiable.', 'proved', 'SECOND_PROOFS.md Section 2.5', 'Neither actual contact-process enhancement hypothesis is established.', 'Direct stochastic domination and one-sided difference quotient; conditional reduction only.'),
]
with (root / 'CLAIMS.jsonl').open('a', encoding='utf-8') as f:
    for claim, status, location, gap, checks in new_claims:
        f.write(json.dumps(dict(problem_id='G0007', claim=claim, status=status, proof_location=location, remaining_gap=gap, checks=checks), ensure_ascii=False)+'\n')
append('CHECKS.md', '''## Second-attempt checks, 2026-10-11

- second_symbolic.py: completed; conditional moment and covariance identities simplify exactly.
- second_countermodel_checks.py: completed; 30 rational comparison cases and exact transition, survival, enhancement and susceptibility constants.
- second_fkg_checks.py: completed; finite four-vertex star normalized and all 256 lattice pair comparisons passed. The general downward-FKG claim relies on the posterior-tree proof, not on this finite test.
- second_threshold_bounds.py: completed; exact degree-4 and degree-5 constants, delta<1/100 and positive branching-excess margins verified.
- The original MarkovObstruction.lean process handle is no longer available. No exit-zero result was captured, so it remains NOT kernel-checked.
- One new Lean command was launched from ~/lean_verify: lake env lean ~/brain_workers/TRIO_1011/op/G0007/NoiseComparison.lean. This file only formalizes the two scalar independent-noise inequalities. Minimal Mathlib.Tactic.Linarith import, no sorry or native_decide. Its captured outcome will be appended separately. The analytic infinite-volume proofs are not formalized.
- All second-attempt artifact writes were inside G0007. No brain, repository or external record was modified.
''')

# Validate every saved claim and finite check artifact before marking the attempt done.
claims = [json.loads(line) for line in (root / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
assert all(c['problem_id']=='G0007' for c in claims)
assert all(c['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'} for c in claims)
for name in ('second_symbolic_checks.json','second_countermodel_checks.json','second_fkg_checks.json','second_threshold_bounds.json'):
    json.loads((root / name).read_text(encoding='utf-8'))
print(f'Validated {len(claims)} claim rows and all four second-attempt check artifacts.')

(root / 'STATUS.md').write_text('''STATE: DONE
NEXT: Prove a contact-process critical healthy enhancement/response estimate or uniform large-radius hierarchy bound; both derivative assertions remain unresolved.
VERDICT: PARTIAL

2026-10-11: Reopened and completed one further serious attempt at the user's request. Read the full earlier attempt, audited its continuity proof, queried the brain for the derivative/susceptibility gap and Broman--Steif movability, and recorded two previously untried approaches.
2026-10-11: Noise comparison route yielded a proved different-model counterexample to the missing enhancement-criticality inference, not a counterexample to the contact process. Exact all-healthy stationary hierarchy yielded new moment/density identities and lambda_p^c(T_d)>d/[2(d-1)]. Strengthened low-degree bounds: T_4>2/3+25/553472 and T_5>5/8+16807/84321000. Complete proofs and remaining gap: SECOND_PROOFS.md.
2026-10-11: Four finite/algebraic check scripts passed. Retain author proofs of both threshold continuities; neither original derivative clause is proved or disproved. Lean checks have only the captured outcomes stated in CHECKS.md. DONE denotes a completed research attempt, not a solved full problem.
''', encoding='utf-8')
