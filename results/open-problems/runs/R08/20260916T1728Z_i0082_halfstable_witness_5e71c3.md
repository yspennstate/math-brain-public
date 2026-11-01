Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this scheduler exposes no model selector or reasoning-effort selector, so I do not claim otherwise. **METRIC MOVEMENT: UNMEASURED -> 2/3 for the frozen explicit candidate. Section-B moves actually tried: 2, 5, 27.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, ALEA 15 (2018), arXiv:1710.08240v2, **Problem 3.11**.

# R08 CLOSABLE OUTSIDE — I0082 admission, positive free-half-stable candidate, and explicit unimodal counter-witness

Run ID: `20260916T1728Z_i0082_halfstable_witness_5e71c3`  
Date checked: 2026-09-16  
Repository: `yspennstate/math-open-problems`, branch `master`  
Source status: **OPEN in the bounded current-status search**  
Track status: **OPEN**  
Frozen metric: number of the following obligations proved for one explicit candidate:
1. a non-Dirac probability law;
2. unimodality;
3. free convolution with **every** unimodal input law is unimodal.

The third obligation is universal; finitely many sampled convolutions do not count.

Before this first admitted I0082 run: **UNMEASURED**.  
After: **2/3** for the standard positive free strictly `1/2`-stable law.  
The third obligation is in fact **disproved for this candidate by one explicit unimodal witness**, so this candidate is eliminated. This does **not** refute Problem 3.11.

Unchanged-run count: **0**.

## 1. Admission, repository continuity, and the retired R08-FPP handoff

I read or queried before research:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0082.md`;
- targeted current intake rows under `probability_1000_intake_*/problems.jsonl`;
- newest own R08 report `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`;
- current related free-probability R19 reports, especially `runs/R19/2026-09-16_16-39-03_UTC__i0084-all-positive-alpha.md`;
- newest R09 package `runs/R09/20260916T162904Z_7a42c1e9.md`.

The intake JSONL families are too large for the connector to render every roughly 780 rows byte-for-byte in one response. I used targeted repository search for I0082, its aliases/source, existing ownership and neighboring work. I do not claim a fictitious line-by-line display of all intake rows.

### Admission decision

The source, current-status, posting and ownership gates are now complete:

- campaign `INDEX.md` records Hasebe--Ueda Problem 3.11 only as **PARTIAL**, with the exact Cauchy exclusion and numerical stable-law work;
- `RANKING.md` places 3.11 among partial/open items;
- `POSTED.md` excludes the distinct Problem 3.3 work, not Problem 3.11;
- `QUEUE.md` lists I0082 as the non-point-mass freely strongly unimodal existence problem;
- repository-wide ownership search found the provisional R08 I0082 claim and no competing current owner;
- the ALEA version of record still states Problem 3.11 after the finite-variance exclusion;
- bounded fresh searches on 2026-09-16 found no later primary source resolving additive Problem 3.11.

I updated the own claim from `PENDING_ADMISSION` to `ADMITTED_ACTIVE`. No shared root ledger was edited; P26 remains the shared-ledger writer.

### Old R08 FPP handoff — retired from this slot, not solved

The preceding R08 assignment, Auffinger--Damron--Hanson Question 4 on strict convexity of the Exp(1) FPP limit shape, is **RETIRED_FROM_R08_SLOT / mathematically OPEN**.

Preserved handoff:

- frozen pair `e1,e2`, strict-gap metric remained `c=0`;
- `R08-X001`: positive local deletion margins may all share one bypass, so naive independent surgery does not tensorize;
- `R08-L001`: a conflict-controlled expected saving `gamma n-o(n)` would compile to a positive strict triangle gap;
- `R08-L002`: equality for the axis pair is equivalent to the whole shape being the corresponding `l1`-diamond;
- `R08-X002`: exact finite triangle equality occurs on positive-probability cylinder events, so pointwise finite strictness is impossible;
- `R08-L003`: certified axis lower bound `mu(e1)>=0.30024`;
- a sufficient diagonal target was `mu(1,1)<0.60048`, but exact full-square blocks `m<=3` did not reach it;
- Busemann/coalescence routes encountered shape-dependent/circular hypotheses;
- if reassigned, the clean next routes are a fixed-width diagonal transfer matrix with rigorous asymptotic upper bound, or genuinely conflict-controlled cross-leg surgery.

This report is the immutable handoff; no FPP work continues in the present R08 slot.

## 2. Exact source scope and current literature check

The ALEA source defines free strong unimodality in Definition 3.8:

`lambda is freely strongly unimodal iff lambda boxplus nu is unimodal for every unimodal nu.`

Theorem 3.10 proves:

> every non-Dirac probability law of finite variance is not freely strongly unimodal.

Immediately afterward:

> **Problem 3.11.** Does there exist a freely strongly unimodal probability measure that is not a delta measure?

Therefore the remaining source-admissible scope is necessarily infinite variance.

Dated bounded searches on 2026-09-16 included:

1. exact phrases `"freely strongly unimodal"` and `"Problem 3.11" Hasebe Ueda`;
2. later Hasebe/Ueda papers on unimodality and free multiplicative convolution;
3. Hasebe--Kuznetsov and Hasebe--Simon--Wang on free stable laws;
4. Huang--Wang on regularity of free Levy processes;
5. current citing material and 2026 searches around free additive unimodality.

Findings:

- Hasebe--Ueda's later multiplicative work is a distinct `boxtimes` problem;
- Hasebe--Simon--Wang prove one-sided free stable densities are whale-shaped, hence in particular unimodal, but do not prove free **strong** unimodality;
- Huang--Wang provide regularity/subordination machinery but not a resolution of Problem 3.11;
- a September 2026 unrefereed candidate on **symmetric** unimodality under free addition explicitly says it does not resolve strong unimodality against arbitrary nonsymmetric unimodal laws;
- no primary-source additive Problem-3.11 resolution was located.

This is a bounded dated search, not a claim of worldwide bibliographic completeness.

Prior R08/I0082 campaign work was recovered rather than reproved:

- the Cauchy laws are exactly excluded using the identity `C_t boxplus nu = C_t * nu`;
- numerical subordination experiments excluded several free stable laws (reported down to roughly `alpha≈0.7`), but except for the Cauchy identity those numerical exclusions are not promoted here to theorems.

R19's current I0084 work is separate. Its source is Hasebe--Ueda Conjecture 5.5 on large-time stable convolution with arbitrary initial law. Its sparse counterexample initial measures are not unimodal, so they are not witnesses for Definition 3.8 and do not settle I0082.

## 3. Frozen explicit candidate and obligations 1--2

Choose the standard positive free strictly `1/2`-stable law
`lambda=X_{1/2,1}`.

A standard explicit density is

`f_lambda(x)=sqrt(4x-1)/(2 pi x^2) 1_{x>=1/4}`.

Its Voiculescu transform is

`phi_lambda(z)=-i sqrt(z)`,

with the principal square root.

### Obligation 1 — non-Dirac probability law: PROVED

Put `r=sqrt(4x-1)`, so `x=(1+r^2)/4`, `dx=r/2 dr`. Then

`int f_lambda = (4/pi) int_0^infty r^2/(1+r^2)^2 dr = 1`.

The law has a nonzero continuous density, hence is non-Dirac. Moreover `f_lambda(x)~1/(pi x^(3/2))`, so its variance is infinite. Thus it genuinely lies outside Theorem 3.10 rather than reproving the excluded finite-variance case.

### Obligation 2 — unimodality: PROVED

On `x>1/4`,

`f_lambda'(x)/f_lambda(x) = 2/(4x-1)-2/x = 2(1-3x)/(x(4x-1))`.

Hence the density is strictly increasing on `(1/4,1/3)` and strictly decreasing on `(1/3,infinity)`, with unique mode `1/3`. This is consistent with the stronger Hasebe--Simon--Wang whale-shape theorem.

Therefore the frozen metric moves to **2/3**.

## 4. Move 2 — attack the universal preservation claim by trying to kill the candidate

The negation of obligation 3 for a fixed candidate is existential:

`exists unimodal nu such that lambda boxplus nu is not unimodal`.

I first attacked canonical stress families before searching a new witness.

### 4.1 The Cauchy family does not kill the candidate

The inverse reciprocal Cauchy transform satisfies `F_lambda^{-1}(z)=z-i sqrt(z)`. Writing `s=sqrt(4z-1)` gives

`G_lambda(z)=4/(s+i)^2`.

For centered Cauchy `C_t`, constant Voiculescu transform gives `lambda boxplus C_t=lambda*C_t`; its density is `p_t(x)=-(1/pi) Im G_lambda(x+it)`.

Write `s=a+ib`, `a,b>0`, `ab=2t`. Differentiating gives

`G_lambda'(z)=-16/[s(s+i)^3]`.

Direct expansion:

`Im[s(s+i)^3]=a[a^2(4b+3)-(b+1)^2(4b+1)]`.

Thus critical points correspond to

` t=Theta(b)= b(b+1)/2 * sqrt((4b+1)/(4b+3)) `.

But

`Theta'/Theta = 1/b + 1/(b+1) + 2/(4b+1) - 2/(4b+3) > 0`,

with `Theta(0+)=0`, `Theta(infinity)=infinity`. Hence exactly one critical point and a strict increase-then-decrease sign change. Therefore `lambda*C_t` is strictly unimodal for every `t>0`.

The checker reduces the derivative to the positive rational function with numerator `32b^3+52b^2+26b+3`.

Hasebe--Ueda's Lemma 3.1/Theorem 3.6 criterion then shows `lambda boxplus S(0,t)` is unimodal for every semicircle time: the required Poisson-kernel function is, up to a positive constant, the density of `lambda*C_R`, which is strictly unimodal.

So Cauchy and semicircle inputs do not supply the negation.

### 4.2 A new explicit unimodal witness does kill the candidate

Take

`nu = (3/100) delta_0 + (97/5000) 1_(0,50)(x) dx`.

It is a probability law and is unimodal with mode 0 in the source's definition: the only atom is at the mode, the density is zero on the left, constant on `(0,50)`, and then drops to zero.

Its Cauchy transform is

`G_nu(z)=3/(100z)+(97/5000) log(z/(z-50))`.

Let `rho=lambda boxplus nu`. Standard additive free subordination gives

`F_rho(z)=F_nu(omega(z))`,
`omega(z)=z-phi_lambda(F_rho(z))=z+i sqrt(F_rho(z))`.

Put `q=sqrt(F_rho(z))` (principal root). Then at a real boundary point `x`, `q` lies in the first quadrant and solves

`H_x(q)=q^2 G_nu(x+iq)-1=0`.

The physical root is not selected by a heuristic branch choice. For fixed real `x`, `q -> sqrt(F_nu(x+iq))` is a holomorphic self-map of the first quadrant. A nonidentity self-map of a hyperbolic simply connected domain has at most one interior fixed point (conjugate to the disk and use Schwarz--Pick). The interval boxes below certify one simple first-quadrant solution. The implicit-function theorem continues it to `x+i eta`, `eta>0`, where subordination has its unique physical fixed point, so the certified root is the physical boundary value.

At such an analytic boundary point, `G_rho(x)=1/q^2` and

`p_rho(x)=-(1/pi) Im(1/q^2)`.

I used interval Krawczyk validation with radius `1e-5`, not a floating root sample, at

`x1=16/5`, `x2=61/10`, `x3=43/2`.

The outward density enclosures are:

- `p_rho(x1) in [0.018655620916870393339, 0.018656893536199606332]`;
- `p_rho(x2) in [0.017411437674322609998, 0.017412448263206693061]`;
- `p_rho(x3) in [0.018039153023312388957, 0.018039956514758512945]`.

Therefore, with large certified margins,

`p_rho(x1)>p_rho(x2)<p_rho(x3)`, with `x1<x2<x3`.

The density is analytic near these points by the simple-root branch. No unimodal density can have such a strict valley: if its mode is left of `x2`, it cannot rise from `x2` to `x3`; if its mode is right of `x2`, it cannot fall from `x1` to `x2`. Hence

**`lambda boxplus nu` is not unimodal.**

So obligation 3 for the explicit positive half-stable candidate is **DISPROVED**.

### Checker status

The analytic derivation is written above. The computational certificate uses `mpmath.iv` outward interval arithmetic and Krawczyk inclusion. It is a validated interval self-check, not a formal proof-assistant kernel. The inclusions are strict and the density gaps are orders of magnitude larger than the interval widths.

Artifact commits:

- candidate checker source: `71571f9203e79dc9b16887d8c3b136620e68cc97`;
- archived output: `320cad2e18d5771e66a25ca22a9d185b8e5ac4a6`.

The output ends `ALL_CANDIDATE_CHECKS_PASS`.

This eliminates one candidate. It does **not** refute the existential Problem 3.11.

## 5. Move 5 — vary the tail index, not the irrelevant scale

A nonzero affine dilation/translation preserves the property of being freely strongly unimodal. Thus changing only the scale of a stable law is not a genuine parameter attack.

The meaningful parameter is the one-sided free-stable tail index `0<alpha<1`, with

`phi_{alpha,1}(z)=-exp(i pi alpha) z^(1-alpha)`.

For `rho_alpha=X_{alpha,1} boxplus nu`, let `w=F_{rho_alpha}(z)`. Then

`w = F_nu(z+exp(i pi alpha) w^(1-alpha))`.

At `alpha=1/2`, the three roots certified above are simple. Since `w!=0`, simplicity in `q=sqrt(w)` is equivalent to simplicity in `w`. The equation is analytic jointly in `w,z,alpha` after fixing the local logarithm branch. By the analytic implicit-function theorem, the three physical boundary values and densities vary continuously with `alpha` near `1/2`.

The two strict valley gaps therefore persist on an open interval.

### R08-I0082-C002 — open stable-index exclusion

**STATUS: PROVED qualitatively from the strict certified gap + implicit-function theorem.**

There exists `epsilon>0` such that every one-sided free strictly `alpha`-stable law with `|alpha-1/2|<epsilon` is **not** freely strongly unimodal; the same fixed unimodal witness above works.

This is qualitative; no numerical epsilon is certified this run. Exploratory computations suggested similar valleys at several larger alpha values, but those are not promoted to theorem claims. The low-index regime, especially around `alpha<=1/4`, remains a plausible next candidate region.

## 6. Move 27 — swap the quantifiers and identify what does and does not reduce

The source asks

`exists lambda != delta for all unimodal nu: lambda boxplus nu is unimodal`.

For a fixed candidate, its negation is only existential, which is why one explicit witness decisively kills `lambda` without any finite sampling approximation.

The proof direction remains genuinely universal. Classical one-dimensional unimodal laws admit interval-mixture/Khintchine representations, but this does not reduce the free problem to the interval components: `nu -> lambda boxplus nu` is not affine in classical mixtures. `G_nu` is mixture-linear, but `F_nu=1/G_nu`, functional inversion, Voiculescu transforms and free convolution are nonlinear. A reduction to interval-uniform extremals would itself require a new convexity or variation-diminishing theorem.

Thus move 27 produced a successful candidate-refutation mechanism but no valid universal-preserver proof reduction.

## 7. What the three new methods taught

- **Move 2 succeeded for candidate elimination.** The half-stable law survives Cauchy and semicircle inputs but fails on the simple skew atom-plus-uniform unimodal law.
- **Move 5 succeeded structurally.** The failure persists under small changes of the stable tail index, so it is not an isolated alpha=1/2 accident.
- **Move 27 exposed the proof bottleneck.** Refutation is existential and tractable; verification remains genuinely universal because free convolution does not commute with classical mixture decomposition.

The strongest new direction is to search the very-heavy-tail boundary instead of staying near alpha=1/2, while seeking a transform-side variation-diminishing criterion that can act on the entire unimodal class.

## 8. Independent audit of newest R09 finite package

I independently audited the finite core of R09-C180 from `runs/R09/20260916T162904Z_7a42c1e9.md`.

Audit ID: **`R08-AUDIT-R09-C180-FINITE-CORE-01 = PASS`**.

I did not copy R09's checker. The R08 audit independently:

1. constructs the six `S1` and eighteen `S2` sites in `Z^3`;
2. enumerates all `2^18-1` nonempty `Y subset S2`;
3. conditions on all `2^6` S1-open masks and computes exact connection probabilities `rho(Y)`;
4. reproduces every reported minimum `rho_1=1/8,...,rho_18=16457991/33554432`;
5. independently evaluates all type-composition terms for `13<=|A|<=38`;
6. reproduces exactly
   `D_tail=22279745927407414101879263/680564733841876926926749214863536422912`;
7. reproduces exactly
   `B_new=333335964186725761866309721803685680673/680564733841876926926749214863536422912`.

This is a PASS for the **C180 finite exact core**, not an audit of the entire R09 critical-percolation program.

Artifact commits:

- audit source: `feb225caa0ad98d7922e14791a13a8eb1739f86b`;
- audit output: `c3048ce91fda76f34a936b7fe599033feba6d296`.

The output ends `R08_AUDIT_R09_C180_FINITE_CORE_PASS`.

## 9. Model/scheduler interface and the denied-task issue

The requested GPT-6 / maximum setting remains **prompt-only and unverified**.

The scheduler interface exposed to this runtime offers task title, prompt, schedule/start offset, enabled state, and timing mode. It exposes **no model selector and no reasoning-effort selector**. Therefore there is nothing in this interface that R08 can set to force GPT-6 or maximum reasoning. Prompt text cannot certify runtime model selection.

To actually change it, one of the following must happen at platform level:

1. the native scheduled-task UI/API must expose model and reasoning-effort fields for this task; or
2. an authorized workspace/task owner must migrate or modify the native task in a context that has those permissions; or
3. platform support must repair the task ownership/configuration.

The historical `You cannot modify this task` response for P26/P01/P03 is a permission/ownership boundary, not a repository error. The current repository ledger records that P26 was later successfully updated in another authorized context, illustrating that the denial can be context-specific. The correct workaround is **not** to bypass the restriction, edit a repository prompt and pretend the native task changed, or create a duplicate scheduler job. Use the authorized owner/workspace context or platform support.

No scheduler modification was attempted in this research run.

## 10. Status and next attack

Source Problem 3.11 remains **OPEN**.

Current candidate: positive free strictly `1/2`-stable law.

Metric: **UNMEASURED -> 2/3**.

Candidate verdict: **ELIMINATED by the explicit unimodal witness above**.

This is real metric movement because obligations 1 and 2 are now proved for one frozen explicit infinite-variance candidate. Obligation 3 is not merely unproved; it is false for that candidate.

### Next three method moves

Do **not** repeat 2,5,27 next run. The planned next triple is:

- **18 — say it in another language:** seek a Pick/Nevanlinna or total-positivity/variation-diminishing characterization of the map induced by a candidate F-transform;
- **24 — find the extremal object:** optimize over simple one-mode atom-plus-uniform / one-sided-uniform inputs to identify what candidate transform makes a secondary peak hardest to create;
- **29 — add points at infinity:** analyze the `alpha downarrow 0` free-stable/regular-variation boundary, where any surviving non-Dirac FSU law must plausibly live after the finite-variance and neighborhood-of-1/2 exclusions.

A concrete next candidate is the positive one-sided free stable law with much smaller index, for example `alpha=1/4`, whose unimodality is known from the whale-shape theorem but whose universal strong-unimodality status is not settled by this run.

No closure package is created because the source problem remains open and no candidate reaches 3/3.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R08
  source:
    authors: Takahiro Hasebe; Yuki Ueda
    title: Large time unimodality for classical and free Brownian motions with initial distributions
    venue: ALEA 15 (2018)
    arxiv: "1710.08240v2"
    locator: "Problem 3.11; Definition 3.8; Theorem 3.10"
    intake: I0082
  target: "Existence of a non-Dirac freely strongly unimodal probability law; remaining infinite-variance scope."
  ownership: "R08 exclusive; admission completed 2026-09-16."
  metric: "Number of 3 frozen obligations proved for one explicit candidate: non-Dirac probability, unimodality, universal preservation against every unimodal input."
  candidate: "positive free strictly 1/2-stable law X_{1/2,1}"
  before: UNMEASURED
  after: "2/3"
  movement: true
  status: OPEN
  candidate_status: ELIMINATED
  unchanged_count: 0
  methods_tried: [2, 5, 27]
  new_claims:
    - "obligation 1 proved: candidate is a non-Dirac probability law of infinite variance"
    - "obligation 2 proved: candidate is strictly unimodal with mode 1/3"
    - "candidate survives all Cauchy and semicircle stress inputs"
    - "obligation 3 disproved for this candidate by explicit unimodal nu = 3/100 delta_0 + 97/5000 1_(0,50) dx"
    - "same witness excludes an open interval of one-sided free-stable indices around alpha=1/2"
  exact_or_validated_evidence:
    - "artifacts/R08/20260916T1728Z_i0082_halfstable_witness_5e71c3_candidate_checker.py @ 71571f9203e79dc9b16887d8c3b136620e68cc97"
    - "artifacts/R08/20260916T1728Z_i0082_halfstable_witness_5e71c3_candidate_checker.out @ 320cad2e18d5771e66a25ca22a9d185b8e5ac4a6"
    - "interval certificate uses mpmath.iv Krawczyk validation; not a proof-assistant kernel"
  audit_ids:
    - "R08-AUDIT-R09-C180-FINITE-CORE-01=PASS"
  r09_audit_evidence:
    - "artifacts/R08/20260916T1728Z_i0082_halfstable_witness_5e71c3_r09_audit.py @ feb225caa0ad98d7922e14791a13a8eb1739f86b"
    - "artifacts/R08/20260916T1728Z_i0082_halfstable_witness_5e71c3_r09_audit.out @ c3048ce91fda76f34a936b7fe599033feba6d296"
  retired_handoff:
    old_target: "ADH Question 4, Exp(1) 2D FPP strict convexity"
    old_metric: "c=0 for frozen e1,e2 strict triangle gap"
    mathematical_status: OPEN
    allocation_status: RETIRED_FROM_R08_SLOT
  next_methods: [18, 24, 29]
```

No Gmail, Drive, email, public posting, purchase, permission change, workflow execution, or scheduler change was performed.
