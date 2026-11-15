# T080 work log

Task received: 2026-11-14, approximately 21:56 Asia/Tbilisi (17:56 UTC).
Task: “push this problem forward by one checkable piece.”

## 1. Start and scope

Read the folder listing, startup memory index, brain navigation index, and compute governor state. The folder initially contained PROMPT.md, codex.log, and run.pid. Governor: status warn, mode owner_away_open, CPU saturated; no heavy computation is planned.

The task's specific rule forbids writes outside this folder. Consequently no mesh/checklist/brain command that writes shared state is run. No git or subagents will be used. Any Python computation will use OMP_NUM_THREADS=1 and nice -n 15.

Literature search begins at 17:57 UTC and is limited to ten minutes. Choice of the concrete mathematical piece will be recorded before its proof is developed.

## 2. Literature check (17:57–17:59 UTC)

Web searches: “hard sphere crystallization rigorous proof phase transition continuum 2025 2026”; “hard disks orientational order rigorous proof phase transition 2025 2026”; “site.arxiv.org hard disks crystallization proof 2025 2026 Gibbs”; “hard sphere Euclidean crystallization theorem November 2026 Gibbs phase transition proof”.

Opened the arXiv abstract and full HTML of Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, arXiv:2607.23873, submitted 26 July 2026: https://arxiv.org/abs/2607.23873 and https://arxiv.org/html/2607.23873v1 . This is a genuine non-Euclidean phase transition, not a solution to T080. Its introduction explicitly leaves the Euclidean problem open. Section 1.4 already states the qualitative equality between optimal Euclidean packing density and the supremum over Poisson factors, using amenability. That qualitative obstruction will not be claimed as new.

Opened the abstract and full HTML of Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, arXiv:2606.28009: https://arxiv.org/abs/2606.28009 and https://arxiv.org/html/2606.28009v1 . It improves absence-of-transition bounds, rather than proving high-density ordering. These June/July papers precede the brief's November 2026 status date, but add useful detail omitted from that summary.

Also opened Thomas Richthammer, *Translation-invariance of two-dimensional Gibbsian point processes*, arXiv:0706.3637, https://arxiv.org/abs/0706.3637 . Opened the abstract of Victor M. Pergamenshchik, Taras Bryk, Andrij Trokhymchuk, *Closed analytical form of many-body free volume and thermodynamics of monodisperse hard disks*, arXiv:2610.08265, https://arxiv.org/abs/2610.08265 : it does not claim an infinite-volume Gibbs ordering theorem. A Nature review URL and PubMed URL could not be read substantively and are not evidence used here.

No solution or new Euclidean high-density ordering theorem was found in the bounded search. This is a search outcome, not a proof of absence. No SOLVED_ELSEWHERE.md is appropriate.

## 3. Choice, before proof

Prove a quantitative geometric obstruction: for every periodic diameter-one sphere packing, construct stationary, isotropic, mixing random packings with arbitrarily nearly the same density. Use independently rotated and translated copies in well-separated cores of Poisson–Voronoi grains. Obtain an explicit retained-density formula, its first-order loss, and a covariance bound. Then periodize finite packings to show that mixing laws approach the unrestricted optimal density in every dimension.

Why this piece: it isolates why optimal packing and high density alone do not imply macroscopic order, and makes the already-known qualitative Euclidean obstruction to the hyperbolic density-gap strategy explicit. The target is a fully checkable quantitative construction, not a freezing theorem or a novelty claim. The Gibbs condition remains essential. The proof must explicitly distinguish mixing at each fixed grain scale from a limit in which the grain scale diverges.

## 4. Proof written

Created PROOF.md. The construction retains a periodic packing in each Poisson nucleus's region where the second-nearest distance exceeds the nearest distance by more than one. A two-Lipschitz distance-difference argument checks exclusion across different grains. Uniform lattice phase gives exact intensity. Poisson radial order statistics give the retained fraction q_d(t). Two integral representations give the linear loss constant independently. A two-seed local determination event gives covariance at most 8(1+m)exp(-m). Periodization with a width-one guard band reduces the unrestricted optimum to periodic packings. Exact contacts provide a direct finite-activity DLR obstruction.

The proof also spells out the order of limits: mixing holds at fixed positive nucleus intensity; its bound degenerates as density approaches optimal. The construction is not claimed to be an unmarked Poisson factor or a Gibbs law.

## 5. First numerical audit: failed quadrature, corrected below

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt
```

Exit code 1. The command printed `nice: setpriority: Operation not permitted`. The numerical audit caught a defect in the adaptive Simpson implementation: at d=3, t=1, it returned 1.5978383088533094e-17 while the independent incomplete-gamma formula returned 0.015425533891858745. A single initial panel sampled only the far tail and missed the narrow peak near the left endpoint. This is a quadrature failure, not evidence against the analytic formula. Correct by seeding the adaptive integration with a fixed mesh; retain both independent calculations and rerun all checks. Also explicitly read the inherited scheduling priority before the numerical work, since this machine can already run agent children at nice 20.

## 6. Corrected numerical audit

Seeded adaptive Simpson quadrature with panels of width at most 1/8. Repeated the exact command above; exit code 0. Standard error again contained `nice: setpriority: Operation not permitted`. The script independently confirmed actual inherited nice priority 20, which is below-normal and lower priority than 15; no attempt was made to raise it. OMP_NUM_THREADS was 1. The script enforces a 60-second CPU limit and rejects actual nice priority less than 15.

Complete successful standard output (also saved in VERIFY_OUTPUT.txt):

```text
Independent numerical audit; no numerical claim is used as a proof.
inherited_nice_priority=20; OMP_NUM_THREADS=1
d,t,q_integral,q_closed,absolute_difference,linear_lower_bound
2,0,1,1,0,1
2,1e-06,0.999998227547,0.999998227547,2.22e-16,0.999998227546
2,0.001,0.998228546149,0.998228546149,1.11e-16,0.998227546149
2,0.01,0.982375459824,0.982375459824,1.11e-16,0.982275461491
2,0.1,0.832737981517,0.832737981517,0,0.822754614909
2,0.25,0.618743543677,0.618743543677,0,0.556886537274
2,0.5,0.353854864031,0.353854864031,0,0.113773074547
2,1,0.0890738558908,0.0890738558908,8.33e-17,-0.772453850906
2,2,0.00173350012739,0.00173350012739,9.02e-17,-2.54490770181
3,0,1,1,2.22e-16,1
3,1e-06,0.999997291767,0.999997291767,2.22e-16,0.999997291764
3,0.001,0.99729444206,0.99729444206,2.22e-16,0.997291764121
3,0.01,0.973184535065,0.973184535065,0,0.972917641211
3,0.1,0.754965847456,0.754965847456,1.11e-16,0.729176412115
3,0.25,0.474761873076,0.474761873076,1.11e-16,0.322941030287
3,0.5,0.191386500705,0.191386500705,2.5e-16,-0.354117939426
3,1,0.0154255338919,0.0154255338919,2.13e-16,-1.70823587885
3,2,7.82630017232e-07,7.82630017344e-07,1.12e-16,-4.41647175771
Constants: gamma expression, independent integral, small-t slope
d=2: 1.77245385091, 1.77245385091, 1.77245285071
d=3: 2.70823587885, 2.70823587885, 2.7082331997
d=4: 3.6762501074, 3.6762501074, 3.67624478959
d=8: 7.62756650196, 7.62756650196, 7.62754076755
Order-statistic Monte Carlo: N=200000, seed=80080, error allowance=0.0047400414
d=2, t=0.1: observed=0.833175, formula=0.83273798, error=0.00043702
d=2, t=0.5: observed=0.35317, formula=0.35385486, error=0.00068486
d=3, t=0.1: observed=0.75541, formula=0.75496585, error=0.00044415
d=3, t=0.5: observed=0.192435, formula=0.1913865, error=0.0010485
PASS: maximum formula discrepancy=2.5e-16
elapsed_seconds=0.222; peak_rss_mib=27.109
Wrote q_table.csv and verification.json
```

The table compares the original integral with independent erfc/incomplete-gamma formulas for d=2,3. Constants were checked both through gamma evaluation and quadrature in d=2,3,4,8; the small-t finite difference has the expected smaller slope. A separate radial-volume order-statistic simulation uses 200,000 samples per dimension. The quoted simultaneous error allowance is a Hoeffding/union-bound benchmark under ideal independent sampling; a seeded pseudorandom run is an audit, not a rigorous probability certificate. Numerical agreement is not an interval-arithmetic certification and is not used in the proof. Full precision data: q_table.csv and verification.json.

## 7. Attempts to break the proof

* Independently checked cross-grain separation: if the distance gap at x exceeds one, every point within distance 1/2 of x has the same nearest nucleus, by the two-Lipschitz inequality. The open radius-1/2 balls about centers from distinct regions therefore lie in disjoint Voronoi interiors. This separately checks the diameter-one normalization and the factor two.
* Checked that the regions used are only subsets of eroded Voronoi cells. Equating these sets would invalidate the exact density formula. The formula is specifically for the distance-gap regions.
* Re-derived the density probability by two independent routes: empty annuli conditional on the nearest radius, and the first two rate-one Poisson arrivals in scaled radial volume. The latter is what the separate simulation samples.
* Re-derived C_d from both integral representations: (d-1)Gamma(1-1/d) and d Gamma(2-1/d). The gamma recurrence equates them exactly. The positive sign of density loss and q_d(0)=1 agree with both low-dimensional formulas.
* Re-derived the covariance constant without the product-expectation route: expand Cov(F,G)=Cov(F-F_tilde,G)+Cov(F_tilde,G-G_tilde), using independence of the two truncated observables. Each term is at most 2 E|difference| <= 4p; total <= 8p. The two input balls have radius R/4+2a; they are disjoint exactly under the sufficient condition R>8a.
* Checked that one nearby nucleus would not suffice to determine the second distance. The proof deliberately uses at least two nuclei; its failure probability is (1+m)exp(-m), not exp(-m).
* Checked the periodization seam in any coordinate, including adjacent copies and half-open cube endpoints: period L+1 gives coordinate separation strictly greater than one across a shifted coordinate. No assumption of an optimal lattice, or even knowledge of the optimal density, is used.
* Checked all limiting quantifiers: positive fixed lambda gives mixing; lambda tends to zero for near-optimal density. No mixing assertion passes to the optimal-density limit. Negative values of 1-C_d t are harmless lower bounds, not claimed densities.
* Checked finite-z Gibbs incompatibility: one finite ball has positive probability of an exact contact in the construction, whereas the DLR density makes this event null. Contact-free periodic input can be rescaled to have a contact without losing density. This does not claim all stationary mixing packings fail DLR, only that these contact-containing examples do.
* Checked that the marks provide a stationary, isotropic law and translation-local determination, but do not silently prove equivariant extraction of marks from an unmarked Poisson process. The known qualitative Poisson-factor equality is credited to the opened paper, not reasserted as a new consequence in that exact class.

No Gibbs-ordering or contour estimate emerged. The completed piece is an explicit quantitative obstruction to a density-only argument. Its novelty relative to the broad literature is not established.

## 8. Final artifact audit (18:06 UTC)

Wrote REPORT.md with the required first-line PARTIAL verdict, exact reproduction command, numerical outcome, initial failed quadrature, limitations, and a concrete next lemma. A short read-only Python check, invoked under the same single-thread environment and `nice -n 15`, confirmed all seven deliverables are nonempty, the verdict line is exact, all 18 CSV rows match the saved PASS result, resource usage is within limits, and VERIFY_OUTPUT.txt appears verbatim in this log. Output:

```text
nice: setpriority: Operation not permitted
PASS: seven deliverables present; report verdict exact; 18 numerical rows consistent; complete output preserved in LOG.md; resource limits met.
```

Finished this bounded T080 piece. No files outside this folder were written, and no git, subagents, external posts, or heavy computation were used.
