# A03 registry and candidate audit
Date: 2026-10-23. Read-only remote inspection; no repository changes or messages to people.

## Registry located and pinned

Repository: <private-repo>, branch main.
Path: 06_math_research/top200_probability_2026_10_14/list.jsonl
Git blob SHA: b8d4607e60eafcce5b3e8286cf882e8931737bd6
Local exact text: registry422.jsonl.
Validation: 422 nonempty JSON records, first T001, last T422. The blank final line is not a record.
Frontier path: 06_math_research/frontier/rows/TNNN/.
The explicit rows are primary evidence of portfolio scope; the publication cited by a row is evidence for the external mathematical frontier.

Current math-brain snapshot is main, not release, and its repository pushed_at is 2026-10-13T06:31:25Z. Its open-problems results are therefore not the current T-series registry. math-research-brain AGENTS.md was read; historical scheduled FEI-only assignment is superseded for this interactive task by the owner-authorized instruction, while privacy/holds remain.

## T228 scope adjudication — priority recommendation

The exact current registry says: “Verify it for a concrete nonlinear model” and later “Prove that the iterates have a stationary law, that the recursion contracts on average and is asymptotically linear with a non-arithmetic multiplier and a nonzero tail constant, so that the stationary tail is a power law with index given by the Lyapunov equation, with alpha < 2 in a nonempty range of (eta, b).”

A single explicitly specified nonlinear model is sufficient. The title and where_it_stands prose do not impose a universal theorem across neural-network losses. The listed generalized linear model and two-layer bounded-activation model are examples, not an obligation to solve both. The audit's replacement likewise asks to choose one concrete nonlinear regression law; its solver_shape explicitly allows a scalar smooth bounded perturbation of linear regression.

For the parent's small-c tanh perturbation route, b=1 and an open eta interval (e.g. within [.99,1.01]) satisfy a nonempty range in (eta,b), provided batch is explicitly fixed. An unbounded linear part plus a bounded tanh perturbation is genuinely nonlinear and aligns with the audit's concrete-model allowance; describe it precisely as such, without calling the entire activation bounded.

The exact completion obligations are:
1. Specify model, loss, iid Gaussian input law, persistent label noise law, update, batch b and parameter interval.
2. Prove a stationary law and uniqueness using actual average contraction of the random maps: E log Lip(Psi) < 0 (or a valid weaker theorem with all its hypotheses).
3. Prove asymptotic linearity with the exact random multiplier A and an integrable remainder envelope. A bounded function perturbation alone is insufficient if differentiation introduces an unbounded state factor; verify the actual SGD gradient.
4. Verify nonarithmetic log|A|, existence and uniqueness of alpha>0 from E|A|^alpha=1, and required moment bounds.
5. Prove the relevant tail constant is strictly positive, not merely that a renewal theorem gives a nonnegative constant. Support/nondegeneracy conditions must exclude a bounded stationary law.
6. Prove alpha<2 on the claimed interval, and identify the observable and whether the conclusion is two-sided or absolute-tail regular variation.
7. Reconcile bias/normalization and eta/b conventions with the cited theorem. No monotonicity in eta/b is demanded by the final imperative of this repaired row.

If all seven are established, T228 can be a whole-row closure under its literal current wording. This is materially stronger than a new lemma on an auxiliary target.

Source attached to the row: Gurbuzbalaban, Simsekli and Zhu, arXiv:2006.04740, Theorem 1, PDF p4; scalar/linear results Theorems 2–4 and Proposition 5, pp7–8. The repository's stored audit says these pages were read. I did not independently inspect that paper in this subtask.

## Ranked alternatives outside T228/T336

These are ranked by proximity of existing work to an auditable theorem. I cannot honestly certify three “genuinely close full rows”: two contain major remaining steps or scope mismatches.

### 1. T354 — strongest written theorem, but original full row is broader

Exact registry request: prove or disprove stationary-point convergence for Adam at fixed problem-independent beta2, beta1<sqrt(beta2), decaying or small constant step, on smooth nonconvex finite sums under standard noise assumptions; AND explain Adam's empirical transformer advantage in a provable model.

Dossier replaces this with random reshuffling, bias correction, PyTorch denominator sqrt(v)+eps, eta_k=eta/sqrt(k), and an explicit residual-neighborhood upper bound or matching lower bound. That repair has NOT been copied into the master registry: changed_since_audit=false, audit={}. Thus a residual theorem does not alone resolve the literal current row, and it does not address the transformer clause.

Strong artifact:
06_math_research/frontier/rows/T354/general_99aebc7f/THEOREM.md
local T354_theorem.md, fetched blob as returned by GitHub.
Theorem 3 now proves the claimed rho_* + O(T^(-1/4) polylog T) rate under globally bounded Lipschitz per-example gradients, global coordinatewise second-moment floor B2_j>=beta>0, eps>0, small eta and a sufficiently large horizon. The residual is O(1-beta2) plus an exponential tail term; the filter-tracking constants depend badly on n through beta2^(2n).
The theorem text has folded in independent audit corrections; stale DOSSIER and NEXT still say the audit is owed.

Independent audit:
06_math_research/frontier/rows/T354/audit_738954b6/AUDIT.md
local T354_independent_prior_audit.md.
Verdict PASS WITH CORRECTIONS, dated 21 Oct. It checks the fresh-epoch conditional coupling and the Jensen step, and fixes horizon/denominator and dimension constants. It explicitly TAKES Proposition 1 as audited rather than independently auditing it. Consequently do not advertise two independent full audits of Proposition 1 plus Theorem 3.

Precise remaining obligations for full original row:
- decide and prove the stationary-point convergence/disproof under explicitly selected standard-noise hypotheses, with the quantifiers of fixed beta2 preserved;
- either prove a model of transformer Adam/SGD separation or identify a primary literature theorem that actually supplies that conjunct;
- if using the repaired residual problem instead, obtain an explicit authorized scope reconciliation rather than silently counting the different statement;
- the global B2 floor excludes interpolation; no extension to all bounded smooth finite sums has been proved in this subtask.

Substantive route worth carrying forward: replace the derivative-in-v coupling by a coupling of sqrt(v), which is a weighted l2 norm of the past gradient sequence. Minkowski gives
|sqrt(v_live)-sqrt(v_frozen)| <= L_g r + 2G beta2^(L/2)
(up to bias-correction factors). The update is Lipschitz in (m,sqrt(v)) for eps>0 with constants 1/eps and G/eps^2. This removes the exponentially small v_lo from the TRACKING constant and may remove the B2 floor from that part of the argument. It does not by itself make the frozen-drift O(1-beta2) bound uniform as B2 approaches zero. This is an unpromoted route suggestion, not a new claimed whole-row result.

External primary source verified in this subtask:
https://arxiv.org/abs/2208.09632 and PDF https://arxiv.org/pdf/2208.09632 (v5).
The paper states problem-first hyperparameter tuning, convergence to a noise-dependent neighborhood, and exact stationarity under strong growth. Its Theorem 3.1/Corollary 3.2 and discussion in section 4 establish that quantifier distinction. Web source refs: turn31view1, turn33view1, turn34view3.

### 2. T357 — ridge results are close, GD/full training path remains open

Exact registry request: a comparable overconfidence theorem for a two-layer network TRAINED BY GRADIENT DESCENT on cross-entropy in a solvable random-features or mean-field single-index-teacher regime, with calibration as a function of n/d, width and TRAINING TIME, and the effect of early stopping.

Dossier's named target is instead fixed-lambda RF logistic ERM: calibration curve and calibration-optimal lambda under a risk constraint. It explicitly states that gradient flow/ridge equivalence for squared loss does not hold for logistic loss. Do not substitute the ridge path for training time.

Strongest exact artifact:
06_math_research/frontier/rows/T357/DOSSIER.md, local rows_T357_DOSSIER.md.
Relevant sections: 20 Oct 17:34 sign lemma; 20 Oct 22:18 and 21 Oct 04:56 first-order RF risk coefficients; formulas use Gaussian-equivalent RF covariance and reduced CGMT fixed point.
For a jointly Gaussian teacher score Z* and fitted score S, the calibration curve is obtained from E[sigma(beta Z*)|S=s]-sigma(s). The finite-alpha fixed point and large-alpha expansion are written, but existing evidence is primarily formulas, numerical agreement and limited audit; the GD path is not derived.

Precise remaining obligations:
- rigorous dynamical Gaussian equivalence/DMFT or another theorem for the actual RF GD trajectory at finite proportional ratios;
- convergence of its teacher alignment/norm processes with training time, enough to identify the calibration curve and risk;
- quantify an actual stopping rule and joint calibration-risk comparison;
- for the narrower ridge target, verify the exact applicable GE/CGMT theorem and differentiability/uniqueness needed for the claimed expansions, then audit the calibration and risk coefficients without changing OC to FM.

Primary source verified:
Bai, Mei, Wang, Xiong, ICML 2021, https://proceedings.mlr.press/v139/bai21c.html and its PDF.
It establishes overconfidence for unregularized well-specified logistic regression in an underparameterized high-dimensional regime; it does not supply the row's RF gradient-descent time theorem. Source refs turn31view2, turn33view2.

### 3. T366 — important exact obstruction, not close to full closure

Exact registry request: determine the optimal worst-case dimension/similarity-independent forgetting rate under uniformly random task ordering, with matching lower bounds.
The repaired dossier fixes jointly realizable tasks, iid uniform task sampling with replacement, exact unregularized projections and historical seen-task squared residual.

Existing results do not settle the uniform bound. The two-projector and symmetric simplex families behave like C/k. Later work studies a sufficient “Condition (B)” and a singular heavy/light cluster family. The pencil-family bound (3+sqrt21)/6 = 1.263763 is NOT a global bound. The latest dossier states an outside-pencil construction with a plateau 1.26788367915, so earlier optimism about the pencil constant has already been falsified.

Artifact:
06_math_research/frontier/rows/T366/DOSSIER.md, local rows_T366_DOSSIER.md.
Latest relevant section: 21 Oct 03:5x, outside the pencil.
Required full-row steps:
- prove some dimension-free Condition(B) bound for ALL projector/task geometries, or construct a family whose historical forgetting truly violates O(1/k);
- bridge any population/all-task last-iterate estimate to historical seen-task forgetting without silently replacing the metric;
- cover the quantifier range (number/rank/dimension of tasks) of the selected random-ordering model;
- supply matching lower rate. A larger finite Condition(B) constant does not move the rate obstruction.

Primary source verified:
Attia, Schliserman, Sherman, Koren, arXiv:2507.11274, abstract and indexed paper source.
At interpolating SGD step eta=1/beta, their O(T^-1/2) bound improves the earlier O(T^-1/4); a tuned smaller step gives a near O(1/T) rate. This does not close the full-step projection question. Source refs turn18search2, turn18search5, turn18search23.

## Deferrals

T248: the literal row requires edge convergence and Tracy-Widom universality, then an explicit finite-rank spike rule. The dossier still says OPEN AS A THEOREM. Finite-size simulations, TW-like quantiles, and a successful information-plus-noise predictor do not provide a local law, edge rigidity or universality comparison. This is below the three candidates above for a near-term whole-row closure.

T421: delegated onward to A06 by parent. Primary source 2608.20638v2 was read through its rank-one statements and exceptions. It proves liminf/limsup crossing for RMSProp and cutoff crossing for Adam, not eventual vanishing-width tracking. It contains four-cycles for beta2<beta1^2 (so not a direct default-Adam counterexample) and exceptional persistently misaligned supercritical trajectories for suitable initial states (not automatically positive-probability random initialization). Do not overclaim either as a refutation of the repaired random-init row. Exact relevant sections: Proposition 3.1, Theorems 3.2/3.3, Appendix F.1.1 and F.2.2. URL https://arxiv.org/html/2608.20638v2, source refs turn33view0, turn34view0, turn34view1, turn34view2.

## Integrity notes

No new problem has been declared solved by this subtask. T069 remains the sole counted solved row as instructed. T353's conjecture refutation is distinct from its broader accounting row. Stale high-level status was checked against exact current proof files wherever available.
A relevant Gmail read hit a 403 RATE_LIMIT_EXCEEDED; that read operation stopped. It supplied no mathematical evidence.

