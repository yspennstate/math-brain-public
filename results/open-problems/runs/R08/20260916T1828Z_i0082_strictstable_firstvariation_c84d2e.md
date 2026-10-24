Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed scheduler has no model selector or reasoning-effort selector, so I do not claim otherwise. **NO MOVEMENT in the fixed metric: 2/3 -> 2/3; unchanged count 1. Section-B moves actually tried: 18, 24, 29.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, ALEA 15 (2018), arXiv:1710.08240v2, **Problem 3.11**.

# R08 CLOSABLE OUTSIDE — I0082 transform-side first variation and exclusion of every non-Dirac free stable attractor

Run ID: `20260916T1828Z_i0082_strictstable_firstvariation_c84d2e`  
Date checked: 2026-09-16  
Repository: `yspennstate/math-open-problems`, branch `master`  
Source status: **OPEN in the bounded current-status search**  
Track status: **OPEN**  

Fixed metric: number of the three frozen obligations proved for one explicit candidate:
1. non-Dirac probability law;
2. unimodality;
3. free convolution with **every** unimodal input law is unimodal.

The universal third obligation is not a finite sampling test.

The previous explicit candidate, the positive free strictly `1/2`-stable law, was eliminated at score 2/3 by the certified skew unimodal witness in the prior run. Following the planned heavy-tail move, this run tests the explicit positive free strictly `1/4`-stable law `X_{1/4,1}`. It is a non-Dirac probability law and is unimodal (indeed the one-sided free-stable density is known to be whale-shaped), so obligations 1 and 2 hold. The theorem below disproves obligation 3 not only for this candidate but for **every non-Dirac free stable law of infinite-variance index `0<alpha<2`**. Therefore the candidate is eliminated and the fixed metric remains **2/3**.

This is substantial source-relevant progress but not metric movement and not closure of Problem 3.11.

## 1. Repository continuity, ownership, and source/current-status gate

I continued from current `master`, not chat memory. Before new mathematics I read or queried:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0082.md`;
- targeted I0082/source/ownership rows in the current `probability_1000_intake_*` trees;
- newest own report `runs/R08/20260916T1728Z_i0082_halfstable_witness_5e71c3.md`;
- newest related R19 stable-law report `runs/R19/2026-09-16_17-36-54_UTC__i0084-skewness-classification.md`;
- newest R09 package `runs/R09/20260916T173216Z_tang_q411_stem_counterexample.md`.

The large intake JSONL trees cannot be rendered row-for-row through this connector without output truncation, so I used targeted repository search for I0082, its source aliases, current ownership and neighboring attempts. I do not claim a fictitious visible read of all roughly 780 rows.

`operations/claims/I0082.md` remains `ADMITTED_ACTIVE`, exclusively owned by R08. The campaign index/ranking still mark Problem 3.11 partial/open; `POSTED.md` excludes the distinct Problem 3.3 package, not Problem 3.11; no competing current owner or posted full resolution was found.

The old R08 FPP strict-convexity route remains retired from this slot with its immutable handoff. It was not reopened.

## 2. Exact source scope and dated prior-art search

Hasebe--Ueda define a Borel probability measure as unimodal if it has one possible atom at a mode `a` plus a density nondecreasing to `a` and nonincreasing after `a`. Their Definition 3.8 says that `lambda` is freely strongly unimodal (FSU) iff `lambda boxplus nu` is unimodal for every unimodal `nu`. Theorem 3.10 excludes every non-Dirac finite-variance law. Immediately afterward Problem 3.11 asks whether a non-Dirac freely strongly unimodal probability measure exists.

This run does not reprove the finite-variance theorem.

Bounded fresh web searches on 2026-09-16 included:

1. exact phrase `"freely strongly unimodal"` and `"Problem 3.11" Hasebe Ueda`;
2. `"free stable" "strongly unimodal" free convolution`;
3. later Hasebe/Ueda unimodality papers, including their multiplicative work;
4. Hasebe--Kuznetsov, *On free stable distributions* (2014);
5. Hasebe--Simon--Wang, *Some properties of the free stable distributions* (2020);
6. Bercovici--Pata with Biane appendix, *Stable laws and domains of attraction in free probability theory* (1999);
7. current citing/search material around additive free strong unimodality.

No primary-source resolution of additive Problem 3.11 was located. Hasebe--Ueda's later multiplicative paper concerns `boxtimes`, not this `boxplus` question. Bercovici--Pata/Biane prove free stable laws are unimodal; Hasebe--Simon--Wang sharpen one-sided free stable densities to whale-shaped. I found no accessible source stating the theorem proved below, but this negative search is bounded and I make **no absolute novelty claim**. The mechanism should be treated as potentially folklore until independent specialist audits are complete.

Primary stable-law formulas used below are standard and source-checked:

- Hasebe--Kuznetsov parameterize strict free stable laws with admissible
  `A={(alpha,rho):0<alpha<1,0<=rho<=1} union {(alpha,rho):1<alpha<=2,1-1/alpha<=rho<=1/alpha}`
  and, for `alpha!=1`, canonical Voiculescu transform
  `phi_{alpha,rho}(z)=-exp(i*pi*alpha*rho) z^(1-alpha)`.
- Bercovici--Pata/Biane give the index-one canonical family
  `phi_rho(z)=-2 rho i + 2(2rho-1)/pi log z`, `0<=rho<=1`, besides the Dirac subcase.
- Every free stable law of index different from one is affine-equivalent to a strict free stable law; the index-one canonical list covers the remaining stable family. The appendix also proves unimodality of all free stable laws.

## 3. Recovered prior R08 attempt

The previous run froze the positive free strict half-stable law and proved obligations 1 and 2. It then found the explicit unimodal witness

`nu = (3/100) delta_0 + (97/5000) 1_(0,50)(x) dx`

for which the free convolution density has a certified strict three-point valley. Hence the half-stable candidate is not FSU. The same witness excludes an open interval of stable indices around `alpha=1/2` by the analytic implicit-function theorem.

That run also showed why classical mixture representations do not reduce the universal FSU condition: `nu -> lambda boxplus nu` is nonlinear in ordinary mixtures. This run does not redo those calculations.

# 4. Move 18 — say the problem in the language of infinitesimal Pick/subordination response

The central new idea is to stop searching one full convolution at a time. FSU must survive **every dilation** of the candidate. A stable law becomes an explicitly small analytic perturbation of the identity under dilation, so a flat unimodal input turns the universal preservation question into a first-variation sign test.

Fix

`0<r<1/4`

and define the explicit probability law

`nu_r = r delta_0 + (1-r) 1_(0,1)(x) dx.`

This is unimodal with mode 0 in the exact Hasebe--Ueda definition: its only atom is at the mode; its density is zero on the left, constant on `(0,1)`, and zero after 1.

Its Cauchy transform is

`G_r(z)=r/z+(1-r) log(z/(z-1)).`

Take the upper-half-plane boundary branch on `0<x<1`. Then

`G_r(x+i0)=A_r(x)-i beta_r`,

where

`A_r(x)=r/x+(1-r) log(x/(1-x))`,
`beta_r=pi(1-r)`.

A key exact identity is

`A_r'(x)=(x-r)/(x^2(1-x)).`                                            (4.1)

Let

`F_r(x)=1/G_r(x+i0)=|F_r(x)| exp(i theta_r(x))`,

so `0<theta_r(x)<pi`.

## 4.1 Index `alpha != 1`

Let `sigma_{alpha,rho}` be the canonical strict free stable law with

`phi(z)=-exp(i gamma) z^(1-alpha)`,
`gamma=pi alpha rho`,

for an admissible Hasebe--Kuznetsov pair `(alpha,rho)`, `0<alpha<2`, `alpha!=1`.

Under dilation by `c>0`,

`phi_{D_c sigma}(z)=c phi_sigma(z/c)=-epsilon exp(i gamma)z^(1-alpha)`,
`epsilon=c^alpha.`                                                       (4.2)

Let

`rho_epsilon = D_c sigma_{alpha,rho} boxplus nu_r`

and write

`w_epsilon(z)=F_{rho_epsilon}(z)`.

Free additive subordination gives the exact equation

`w_epsilon(z)=F_{nu_r}( z + epsilon exp(i gamma) w_epsilon(z)^(1-alpha) ).` (4.3)

At `epsilon=0`, `w_0=F_{nu_r}`. For a fixed `x in (0,1)`, use the local analytic continuation of the upper boundary branch of `G_r`; the derivative with respect to `w` of the left side minus the right side of (4.3) is exactly 1 at `epsilon=0`. The analytic implicit-function theorem therefore gives the physical boundary branch for all sufficiently small `epsilon>0`. (For `Im z>0` it agrees with the unique free-subordination solution; continuation to the real point identifies the boundary branch.)

Differentiating (4.3) at zero and then inverting gives

`G_{rho_epsilon}(x+i0)
 = G_r(x+i0)
 + epsilon G_r'(x+i0) exp(i gamma)F_r(x)^(1-alpha)
 + O(epsilon^2).`                                                        (4.4)

On the interior of the flat density interval, `G_r'(x+i0)=A_r'(x)` is real. Hence the density has the exact first variation

`p_epsilon(x)=(1-r)+epsilon Q_{alpha,rho,r}(x)+O(epsilon^2)`,             (4.5)

where

`Q_{alpha,rho,r}(x)
 = -(A_r'(x)/pi) Im[ exp(i gamma)F_r(x)^(1-alpha) ].`                     (4.6)

### Phase sign

For `0<alpha<1`, admissibility gives `0<=gamma<=pi alpha`. Thus

`0 < gamma+(1-alpha)theta_r(x) < pi`.

For `1<alpha<2`, Hasebe--Kuznetsov admissibility gives

`pi(alpha-1)<=gamma<=pi`,

and therefore

`0 < gamma-(alpha-1)theta_r(x) < pi`.

So in every admissible case

`Im[exp(i gamma)F_r(x)^(1-alpha)]>0.`                                    (4.7)

Combining (4.1) and (4.7),

`sign Q_{alpha,rho,r}(x) = - sign(x-r)`,

and in particular

`Q_{alpha,rho,r}(r)=0.`                                                   (4.8)

This is already a necessary variation-diminishing obstruction: a stable perturbation pushes the formerly flat density downward immediately to the right of `r`.

# 5. Move 24 — find the extremal unimodal witness, then force a valley

The atom-plus-flat law `nu_r` is not arbitrary. It is chosen because the zeroth-order density has **zero slope everywhere on `(0,1)`**, so no pre-existing monotone trend can mask the first variation. The atom moves the real boundary transform just enough to make the first-order slope switch exactly at `x=r`.

The three comparison points are

`x_1=r`, `x_2=2r`, `x_3=1/2`.

By (4.8),

`Q(x_1)=0.`                                                              (5.1)

At `x=2r`, set

`M_r=-A_r(2r)`.

Then

`A_r(2r)=1/2+(1-r)log(2r/(1-2r)) -> -infinity`,
`A_r'(2r)=1/[4r(1-2r)]`,                                                 (5.2)

and as `r downarrow 0`,

`|F_r(2r)| asymp 1/M_r`,
`pi-theta_r(2r) asymp 1/M_r`,
`M_r asymp |log r|.`                                                      (5.3)

The phase factor in (4.6) has two possibilities.

### `0<alpha<1`

If `rho<1`, the sine in (4.7) converges to the positive constant

`sin(pi alpha(1-rho))`.

Thus

`-Q(2r) >= C/[r M_r^(1-alpha)] -> infinity.`

At the extreme `rho=1`, the limiting phase is `pi` and the sine loses one factor `M_r^{-1}`; then

`-Q(2r) >= C/[r M_r^(2-alpha)] -> infinity.`                             (5.4)

### `1<alpha<2`

If `rho>1-1/alpha`, the limiting phase is strictly inside `(0,pi)` and

`-Q(2r) >= C M_r^(alpha-1)/r -> infinity.`

At the extreme `rho=1-1/alpha`, the sine again loses one factor `M_r^{-1}` and

`-Q(2r) >= C/[r M_r^(2-alpha)] -> infinity.`                             (5.5)

Every displayed divergence follows from the elementary fact

`r |log r|^k -> 0`

for each fixed `k`.

At `x=1/2`, however,

`A_r(1/2)=2r`,
`A_r'(1/2)=4-8r`,
`F_r(1/2) -> i/pi`,                                                       (5.6)

so `Q(1/2)` remains bounded as `r downarrow 0`.

Consequently, for every fixed admissible `(alpha,rho)` with `alpha!=1`, one may choose `r>0` so small that

`Q(r)=0 > Q(2r)`

and

`Q(1/2)>Q(2r).`                                                          (5.7)

Now freeze this `r`. The `O(epsilon^2)` terms in (4.5) are ordinary analytic remainders at the three fixed points. Hence for sufficiently small `epsilon>0`,

`p_epsilon(r) > p_epsilon(2r) < p_epsilon(1/2).`                         (5.8)

Since

`r<2r<1/2`,                                                               (5.9)

(5.8) is a strict three-point valley. No unimodal density can have it: if the mode lies at or left of the middle point the density cannot rise afterward; if the mode lies at or right of the middle point it cannot have fallen from the first point. Thus

`D_c sigma_{alpha,rho} boxplus nu_r`

is not unimodal for some `c>0`.

Dilation invariance finishes the candidate-level statement: if `D_c sigma boxplus nu_r` is nonunimodal, then

`D_c( sigma boxplus D_{1/c}nu_r )`

is nonunimodal; `D_{1/c}nu_r` is still unimodal. Hence `sigma` itself is not FSU.

# 6. Move 29 — add the scale-zero / tail boundary; the index-one corner also fails

The previous run proposed looking near the extreme heavy-tail boundary `alpha downarrow 0`, with `alpha=1/4` as the next concrete candidate. The preceding argument does more: for **every fixed positive alpha**, however small, the double boundary `r downarrow 0`, `c downarrow 0` produces the valley. Thus the strict-stable `alpha downarrow 0` edge supplies no surviving candidate. The proof is pointwise in `alpha`; no uniform-in-alpha epsilon is claimed.

There is one canonical stable corner not covered by the power transform: index one.

Bercovici--Pata/Biane parameterize the non-Dirac index-one free stable family, up to affine equivalence, by

`phi_rho(z)=-2 rho i + a_rho log z`,
`a_rho=2(2rho-1)/pi`, `0<=rho<=1`.                                      (6.1)

Under dilation,

`phi_{D_c sigma}(z)
 = c[-2rho i + a_rho log z] - a_rho c log c.`                            (6.2)

The last term is real and is therefore only a translation. FSU is translation-invariant, so remove it. The small subordination direction is then

`S_rho(w)=2rho i-a_rho log w.`                                           (6.3)

If `arg w=pi t`, `0<t<1`, then

`Im S_rho(w)
 =2[t+rho(1-2t)].`                                                       (6.4)

For fixed `t`, the right side is linear in `rho`; at `rho=0` it is `2t>0`, and at `rho=1` it is `2(1-t)>0`. Hence it is strictly positive for every `rho in [0,1]`.

The first variation is therefore again

`Q_{1,rho,r}(x)=-(A_r'(x)/pi) Im S_rho(F_r(x)).`                         (6.5)

At `x=r`, it vanishes. At `x=1/2`, it stays bounded. At `x=2r`, if `rho<1` the imaginary factor tends to `2(1-rho)>0`, whereas at the endpoint `rho=1` it is of order `1/M_r`. Thus even in the worst endpoint case

`-Q_{1,rho,r}(2r) >= C/[r M_r] -> infinity.`                             (6.6)

The same three-point valley argument proves failure of FSU for every non-Dirac index-one free stable law.

This includes the Cauchy subcase but does not depend on the earlier Cauchy-specific classical-convolution identity.

# 7. R08-I0082-C003 — all infinite-variance free stable laws are excluded

**STATUS: PROVED internally by the written argument above; independent audit pending.**

> **Theorem C003.** Every non-Dirac free stable probability law of stability index `0<alpha<2` is **not** freely strongly unimodal.

Proof summary:

- `alpha!=1`: affine-reduce to the Hasebe--Kuznetsov canonical strict stable form and use Sections 4--5;
- `alpha=1`: affine-reduce to the Bercovici--Pata/Biane logarithmic form and use Section 6;
- the explicit witness after undoing the candidate dilation/translation remains unimodal.

All these indices are in the infinite-variance scope relevant after Hasebe--Ueda Theorem 3.10.

The finite-variance `alpha=2` semicircle is already excluded by Hasebe--Ueda Lemma 3.9/Theorem 3.10 and is **not reproved or counted as new**.

For the explicit `X_{1/4,1}` candidate tested this run:

- obligation 1: PROVED/known — non-Dirac free stable probability law;
- obligation 2: PROVED/known — free stable laws are unimodal; in the one-sided case the density is whale-shaped;
- obligation 3: DISPROVED by C003.

Therefore the fixed metric remains **2/3**, and this candidate is eliminated.

# 8. R08-I0082-C004 — stable-domain exclusion for arbitrary candidate laws

**STATUS: PROVED as a corollary of C003 plus standard closure facts and the known semicircle exclusion.**

The stable-family theorem feeds directly into the source existence problem.

First record three elementary closure facts.

1. If `lambda` and `eta` are FSU, then `lambda boxplus eta` is FSU: for any unimodal `nu`, `eta boxplus nu` is unimodal, and then `lambda boxplus(eta boxplus nu)` is unimodal.
2. Nonzero affine images of an FSU law are FSU, and conversely.
3. The FSU class is weakly closed. Indeed, if `lambda_n => lambda` and every `lambda_n` is FSU, then for every unimodal `nu`, weak continuity of free convolution gives `lambda_n boxplus nu => lambda boxplus nu`. The class of unimodal laws is weakly closed (the same closure fact Hasebe--Ueda use in Theorem 3.10), hence `lambda boxplus nu` is unimodal.

Now suppose `lambda` belongs to the free domain of attraction of a non-Dirac free stable law `sigma`. Some affine normalizations of `lambda^{boxplus n}` converge weakly to `sigma`. If `lambda` were FSU, item 1 would make every free convolution power FSU, item 2 every normalization FSU, and item 3 the limit `sigma` FSU.

- If `sigma` has index `<2`, this contradicts C003.
- If `sigma` is the index-two semicircle type, this contradicts the already known Hasebe--Ueda Lemma 3.9.

Hence:

> **Corollary C004.** No probability law belonging to the free domain of attraction of any non-Dirac free stable law can be freely strongly unimodal.

The same argument works for any subsequence of normalized free convolution powers converging to a non-FSU stable law, so a hypothetical non-Dirac FSU law cannot even have such a stable **partial** attraction limit.

Bercovici--Pata show that free stable domains of attraction match the corresponding classical stable domains under their bijection. Thus C004 excludes a broad, source-relevant infinite-variance class, including regularly varying/stable-domain tails and even infinite-variance laws in the semicircular domain of attraction.

This does **not** close Problem 3.11. There exist probability laws outside all stable domains of attraction. Any remaining FSU candidate must now be of that irregular kind (and avoid stable non-FSU subsequential normalized limits).

# 9. What the three methods accomplished

### Move 18 — another language: SUCCESS

The universal preservation problem became an infinitesimal Pick/subordination response test. Formula (4.6) is the key transform-side observable. Instead of solving a full free convolution globally, one studies the first variation of a flat unimodal density under an arbitrarily small scaled candidate.

### Move 24 — extremal object: SUCCESS

The atom-plus-flat witness `nu_r` is tailored to have zero baseline slope. Its boundary transform has the exact derivative

`A_r'(x)=(x-r)/(x^2(1-x))`,

which gives a stationary comparison point at `r`, a singularly amplified dip at `2r`, and a bounded reference point at `1/2`. This replaced numerical witness hunting by a structural family.

### Move 29 — points at infinity/boundary: SUCCESS

Taking `c downarrow 0` and `r downarrow 0` exposes the stable homogeneous transform and forces the dip. The argument works for each fixed stable index all the way toward `alpha downarrow 0`; the proposed positive free `1/4`-stable candidate is therefore eliminated without a separate numerical search. The logarithmic `alpha=1` boundary can also be handled explicitly.

The source problem remains open only because an arbitrary infinite-variance law need not belong to a stable domain of attraction.

# 10. Adversarial self-checks and limitations

Only after the analytic route was written did I build a checker.

Run-specific self-check source:

`artifacts/R08/20260916T1828Z_i0082_strictstable_firstvariation_c84d2e_checker.py`

creation commit:

`30ad96d787e84f00826a034e8efd56e207580587`.

Archived output:

`artifacts/R08/20260916T1828Z_i0082_strictstable_firstvariation_c84d2e_checker.out`

creation commit:

`e6946745b64fd6845593b93dbe06ae1ad8ee9e97`.

The checker:

- symbolically verifies (4.1), `A_r'(r)=0`, (5.2), and (5.6);
- exact-checks representative rational phase points on every power-law parameter face;
- checks the index-one phase endpoint identity exactly;
- then, **only as numerical adversarial stress**, solves the full nonlinear boundary fixed-point equation for representative parameters `alpha=1/4,3/4,1,3/2,1.9`, including skewness endpoints, and observes the predicted three-point valley;
- independently exact-checks the finite algebra in the R09 audit below.

The floating fixed-point stress is explicitly **not theorem evidence**. C003/C004 stand on the written analytic proof.

The archived output ends `ALL_CHECKS_PASS`.

Limitations preserved:

- C003 gives no uniform valley scale as `alpha downarrow 0`; it is pointwise in the fixed stable parameter.
- C004 does not say every infinite-variance law has a stable attraction limit.
- no source-level closure is claimed;
- no paper package is created;
- no novelty claim is made before independent audits and broader specialist prior-art review.

# 11. Independent audit of newest R09 package

Audited package:

`runs/R09/20260916T173216Z_tang_q411_stem_counterexample.md`.

Audit ID:

**`R08-AUDIT-R09-TANG-Q411-PERIODIC-01 = PASS`**.

I independently rederived the claimed periodic-tree counterexample rather than trusting R09's checker.

For `k>=0`, let `T_k` consist of a `k`-edge stem from the root to a vertex carrying an infinite rooted binary tree. Under Tang/Lyons--Peres periodicity, every stem vertex can use the identity on its descendant subtree and has depth at most `k`; every strict binary descendant has descendant subtree isomorphic to the binary subtree rooted at the stem endpoint. Thus `T_k` is `k`-periodic under the source definition.

Let `beta(p)` be survival from the binary-tail root. Its physical survival probability solves

`beta=1-(1-p beta)^2`.

The greatest fixed point is

`beta(p)=0` for `p<=1/2`,

and

`beta(p)=(2p-1)/p^2` for `p>1/2`.

All `k` stem edges must be open, so

`theta_k(p)=p^k beta(p)=p^(k-2)(2p-1)`, `p>1/2`.

For `k=3`,

`theta_3(p)=2p^2-p`,
`theta_3''(p)=4>0`

throughout `(1/2,1)`. Therefore this periodic-tree percolation function is strictly convex, not concave. The periodic-tree half of Tang Question 4.11 is indeed refuted as stated; the transitive-graph half is untouched.

At `p=3/4`, exact arithmetic gives

`beta=8/9`,

and the four-type survival vector

`(3/8,1/2,2/3,8/9)`.

The R08 run-specific checker verifies these identities with `Fraction` arithmetic and verifies `theta_3''=4` exactly. It does not substitute for the source-scope periodicity proof above.

**Audit verdict: PASS for the periodic-tree theorem.** This is an independent other-track audit of R09's package, not a closure declaration; R09 still needs its owner-specified P26/other closure workflow.

# 12. Scheduler/model interface status

The requested GPT-6 / maximum setting is still prompt-only and unverified in this runtime.

The exposed scheduled-task update interface permits title, prompt, schedule/start offset, enabled state and timing mode. It exposes **no model field and no reasoning-effort field**. Therefore R08 cannot set or verify GPT-6/maximum from this interface, and prompt text is not runtime telemetry.

To actually change this, the product must expose native model/reasoning selectors for scheduled tasks, or an authorized workspace/task owner must migrate/manage the native task in an interface that exposes those controls; otherwise platform support must repair the task ownership/configuration.

The controlling repository policy records historical probes for P26/P01/P03 that returned `You cannot modify this task`. That is a permission/ownership boundary, not a GitHub error. The safe workaround is to use the owning account/workspace/interface or platform support. Do not bypass it, create duplicate schedules, or edit repository prompt text and pretend the native scheduler changed. This run made no scheduler modification.

# 13. Status and next attack

Problem 3.11 remains **OPEN**.

Fixed metric: **2/3 -> 2/3; no movement; unchanged count 1**.

Explicit candidate tested this run: positive free strict `1/4`-stable law.

Candidate verdict: **ELIMINATED** by C003.

Source-relevant advance: **every non-Dirac free stable law of infinite-variance index `<2` is eliminated, and no FSU law can lie in any free stable domain of attraction.**

The next run must not repeat 18,24,29. The planned next triple is:

- **3 — prove something stronger:** ask whether the flat-tail first variation excludes every non-Dirac freely infinitely divisible law, or at least every law with a nonzero regularly varying/free-Levy tail, rather than only stable limits;
- **11 — dualize:** rewrite the first-variation sign in the free Levy--Khintchine/Nevanlinna measure, looking for a necessary condition on the free Levy measure of an FSU law;
- **22 — read the failures:** search the later free-unimodality literature and citations specifically for attempted strong-unimodality preservation criteria, to identify what obstructed a general no-go theorem.

A source-closing route would be to prove that **every** non-Dirac infinite-variance law either has a non-FSU normalized free-sum subsequential limit or directly violates the flat-tail first-variation criterion. C004 gets only the stable-attraction part of this dichotomy.

# 14. Structured ledger_delta

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
  ownership: "R08 exclusive; operations/claims/I0082.md ADMITTED_ACTIVE."
  metric: "Number of 3 frozen obligations proved for one explicit candidate: non-Dirac probability, unimodality, universal preservation against every unimodal input."
  candidate_this_run: "positive free strictly 1/4-stable law X_{1/4,1}"
  before: "2/3"
  after: "2/3"
  movement: false
  unchanged_count: 1
  status: OPEN
  candidate_status: ELIMINATED
  methods_tried: [18, 24, 29]
  new_claims:
    - "R08-I0082-C003: every non-Dirac free stable law with 0<alpha<2 is not freely strongly unimodal"
    - "R08-I0082-C004: no FSU law lies in the free domain (or stable partial domain) of attraction of a non-Dirac free stable law; alpha=2 uses the already-known semicircle exclusion"
    - "explicit flat-tail unimodal witness family nu_r = r delta_0 + (1-r) 1_(0,1) dx gives transform-side first-variation obstruction"
  exact_or_validated_evidence:
    - "artifacts/R08/20260916T1828Z_i0082_strictstable_firstvariation_c84d2e_checker.py @ 30ad96d787e84f00826a034e8efd56e207580587"
    - "artifacts/R08/20260916T1828Z_i0082_strictstable_firstvariation_c84d2e_checker.out @ e6946745b64fd6845593b93dbe06ae1ad8ee9e97"
    - "floating fixed-point stress is self-check only; theorem proof is analytic on page"
  audit_ids:
    - "R08-AUDIT-R09-TANG-Q411-PERIODIC-01=PASS"
  next_methods: [3, 11, 22]
```

No Gmail, Drive, email, public posting, purchase, permission change, workflow execution, or scheduler change was performed.
