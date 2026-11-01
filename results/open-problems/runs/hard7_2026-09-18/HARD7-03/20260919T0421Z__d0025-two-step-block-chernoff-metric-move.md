Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**, and I do not claim otherwise. **Frozen metric MOVED: `L <= Delta_2(Q): 500000/6578563 -> 5000/61903`. Methods tried: B6, B15, B22.**

# HARD7-03 — two-step homogeneous block bound, deformation stress test, and current prior-art screen

Status: **PARTIAL / source Problem 4 remains open as a whole.** This run does not audit or close the preceding all-`K` plateau theorem candidate. It produces a new self-contained homogeneous `K=2` last-passage upper bound, uses that bound to move the frozen source-relevant plateau-width certificate, and then stress-tests the mechanism against weak disorder, nonreversible environments, and current adjacent literature.

## 1. Continuity, ownership, and required repository state

I resumed the exclusive canonical claim

`operations/claims/D0025.md`

for Seppäläinen's 1999 Problem 4, rather than reopening admission or changing targets. The active source clause is the site-disordered totally asymmetric `K`-exclusion flux-flatness question around density `K/2`; known `K=1` results remain prior art, and particlewise disorder is not silently identified with the present site-disorder theorem candidate.

At run start I re-read:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_1000_intake_D_20260908/problems.jsonl`, including the exact `D0025` row keyed by `disordered_asep_open_1999::problem_4`;
- the newest own checkpoint `runs/hard7_2026-09-18/HARD7-03/20260919T0325Z__d0025-general-k-site-disorder-plateau.md` and the preceding HARD7-03 chain;
- the newest neighboring HARD7-02 checkpoint, commit `21899f7de6247504441ef25ee0029a1cb309185a` (`critical endpoint and axis boundary layer`), and newest neighboring HARD7-04 checkpoint, commit `ba8a186432c966bc838f034e9e7cc80d8c2710d2` (`absorbing hub-kernel iteration`).

The claim search still assigns `D0025` to HARD7-03. I found no posted/retired equivalent target that supersedes it. Shared root ledgers were not edited because the HARD7 policy requires an immutable per-run `ledger_delta` instead of concurrent worker mutations.

The exact source was rechecked in the primary 1999 paper, arXiv `math/9906194`, Section 3 and Problem 4. The source defines the totally asymmetric `K`-exclusion generator

\[
L^\alpha f(\eta)=\sum_x \alpha_x
\mathbf 1\{\eta(x)\ge1,\eta(x+1)\le K-1\}
[f(\eta^{x,x+1})-f(\eta)],
\]

states the iid-site-rate hydrodynamic theorem for fixed `K`, and asks whether the disordered flux `f_K` has a flat segment around `K/2`. The journal record is Resenhas IME-USP 4(1), published 1999-07-01, DOI `10.11606/resimeusp.v4i1.74889`.

## 2. Frozen metric

The frozen metric remains the one admitted for the binary `K=2` test law

\[
Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

namely

\[
L=\text{a rigorously certified lower bound on the half-width }\Delta_2(Q)
\]

of the flux plateau around density `1`, within the current self-checked theorem chain.

Before this run:

\[
L_{\rm old}=\frac{500000}{6578563}=0.07600444\ldots .
\]

After this run:

\[
\boxed{L_{\rm new}=\frac{5000}{61903}=0.08077152\ldots .}
\]

The exact increase is

\[
L_{\rm new}-L_{\rm old}
=\frac{1941315000}{407232785389}>0.
\]

Thus the frozen metric genuinely moves and the Section-I stagnation counter resets to zero.

## 3. B6 — deform the infinite homogeneous problem to an exact two-step transfer block

The preceding checkpoint reduced the binary plateau bound to an upper bound on the homogeneous `K=2` central lazy-LPP shape constant. In its notation,

\[
\Delta_2(Q)\ge \frac{1}{4G_1(0)}.
\tag{3.1}
\]

The old bound used a one-path union bound over `3^n` lazy paths and obtained

\[
G_1(0)<3.2892815.
\]

That argument throws away almost all overlap between paths. The new move is to preserve the complete overlap structure inside **two consecutive time layers**, and union only over the coarse boundary heights between two-step blocks.

### Theorem 3.1 — exact two-step Chernoff upper bound

For the homogeneous rate-one `K=2` lazy last-passage representation from the preceding checkpoints,

\[
\boxed{G_1(0)\le \frac{61903}{20000}=3.09515.}
\tag{3.2}
\]

#### Proof

Work on the unrestricted lazy lattice with increments `-1,0,+1`; this only enlarges the source path family if a wedge/boundary restriction is present, so an upper bound here is valid for the source central passage time. Count the starting weight separately; it contributes only `O(1)` and is irrelevant for the shape.

Break a path of length `2m` into `m` two-step blocks. Fix a block start height and a two-step displacement

\[
d\in\{-2,-1,0,1,2\}.
\]

Let `X_2(d)` be the maximum weight collected in the two **new** time layers among paths with that fixed block displacement. All paths with the same `d` share the final endpoint weight. Consequently, if all site weights are iid `Exp(1)`, then

\[
X_2(\pm2)=E+E',
\]

\[
X_2(\pm1)=E'+\max(E_1,E_2),
\]

and

\[
X_2(0)=E'+\max(E_1,E_2,E_3),
\tag{3.3}
\]

with the displayed exponentials independent inside each identity.

For `0<theta<1`, put

\[
H_j(\theta)=\mathbb E\exp\{\theta\max_{1\le i\le j}E_i\}.
\]

The density of the maximum gives the exact formula

\[
H_j(\theta)=\frac{j!}{\prod_{r=1}^j(r-\theta)}.
\tag{3.4}
\]

Hence the five fixed-displacement block moment-generating functions sum to

\[
\begin{aligned}
A_2(\theta)
&:=\sum_{d=-2}^2\mathbb E e^{\theta X_2(d)}\\
&=\frac{1}{(1-\theta)^2}
\left[
2+\frac{4}{2-\theta}
+\frac{6}{(2-\theta)(3-\theta)}
\right].
\end{aligned}
\tag{3.5}
\]

Now fix a coarse boundary sequence

\[
y_0=0,y_1,\ldots,y_m=0,
\qquad |y_j-y_{j-1}|\le2.
\]

For this fixed sequence, the maximum passage weight is the sum of the `m` block maxima with displacements `d_j=y_j-y_{j-1}`. The block fields use disjoint time layers, so these block maxima are independent. Chernoff therefore gives

\[
\Pr\left\{
\sum_{j=1}^mX_{2,j}(d_j)\ge2ma
\right\}
\le e^{-2m\theta a}
\prod_{j=1}^m M_{d_j}(\theta),
\tag{3.6}
\]

where `M_d(theta)=E exp(theta X_2(d))`.

Union over all coarse boundary sequences ending at zero. Instead of counting them crudely, sum their products. The endpoint-zero coefficient is at most the total coefficient mass, so

\[
\Pr\{T_1(2m,0)\ge2ma\}
\le
\left[A_2(\theta)e^{-2\theta a}\right]^m.
\tag{3.7}
\]

Choose

\[
\theta=\frac{16}{25},
\qquad
a=\frac{61903}{20000}.
\]

The exact checker evaluates

\[
A_2(16/25)=\frac{158125}{3009},
\qquad
2\theta a=\frac{61903}{15625}.
\tag{3.8}
\]

Let `S_15(x)=sum_{k=0}^{15}x^k/k!`. Since `x>0`, `S_15(x)<e^x`, while exact rational arithmetic gives

\[
S_{15}\!\left(\frac{61903}{15625}\right)
-rac{158125}{3009}>0.
\tag{3.9}
\]

The archived output contains the full positive rational numerator/denominator. Thus the bracket in (3.7) is strictly below one. The probabilities are geometrically summable in `m`, so Borel--Cantelli yields

\[
\limsup_{m\to\infty}\frac{T_1(2m,0)}{2m}\le a
\quad\text{a.s.}
\]

and the existing shape limit gives (3.2). `QED`

### Consequence for the frozen binary metric

For the frozen binary law,

\[
r=\frac12,
\qquad
\mathbb E\frac1\alpha=\frac32,
\qquad
1-r\mathbb E\frac1\alpha=\frac14.
\]

Combining the preceding all-`K` plateau theorem candidate with (3.2),

\[
\Delta_2(Q)
\ge\frac{1}{4G_1(0)}
\ge\frac{1}{4(61903/20000)}
=\boxed{\frac{5000}{61903}}.
\tag{3.10}
\]

This is the run's source-relevant metric movement.

**B6 outcome:** successful. The infinite homogeneous optimization is deformed to an exactly analyzable two-step transfer block. Unlike the earlier `3^n` path count, the block calculation retains the shared endpoint weight and therefore lowers the certified homogeneous shape upper bound from `3.2892815` to `3.09515`.

## 4. B6 second stress test — the general formula exactly recovers Sly at `K=1`

A deformation toward the solvable `K=1` endpoint gives an independent consistency test of the previous all-`K` theorem candidate.

The candidate half-width from the preceding checkpoint is

\[
\delta_{K,Q}
=\frac{1-r\,\mathbb E(1/\alpha)}{\gamma_{K,1}(1,0)}.
\tag{4.1}
\]

For ordinary TASEP (`K=1`), the homogeneous central shape is explicit:

\[
\gamma_{1,1}(1,0)=4.
\]

Therefore (4.1) becomes

\[
\delta_{1,Q}
=\frac{1-r\,\mathbb E(1/\alpha)}4
=\frac{r}{4}\left(\frac1r-\mathbb E\frac1\alpha\right).
\tag{4.2}
\]

Allan Sly's 2016 Theorem 1 in *Note on the flux for TASEP with general disorder* (arXiv:1609.06589) proves a plateau on exactly

\[
\left[
\frac12-\frac{\mu r}{4},
\frac12+\frac{\mu r}{4}
\right],
\qquad
\mu=\frac1r-\mathbb E\frac1\alpha.
\]

Thus the all-`K` formula reduces **exactly** to the known `K=1` theorem, not merely to the same order of magnitude.

For the two-point weak-disorder family

\[
Q_{p,\varepsilon}
=p\,\delta_{1-\varepsilon}+(1-p)\delta_1,
\qquad 0<p<1,
\]

one has

\[
1-r\mathbb E(1/\alpha)=(1-p)\varepsilon.
\tag{4.3}
\]

The bound is consequently singular as `p downarrow 0`: arbitrarily rare slow sites still leave a positive limiting lower bound before the exact `p=0` endpoint removes the slow essential infimum. This is consistent with the rare-strip mechanism and warns against a smooth perturbative expansion in the disorder probability.

## 5. B15 — break symmetry on purpose: what actually carries the plateau proof?

The previous report mentioned reversibility of the iid rate field when discussing centering at `K/2`. This run stress-tested that point and found a useful correction:

**the proof does not actually need reflection symmetry of the disordered environment to locate the center.** The tangent slope `-K/2` is taken from the **constant-rate homogeneous comparator** `g_{K,r}`, whose particle-hole/reflection symmetry is automatic. The disorder enters through central saturation and the row-crossing bonus.

To isolate the real load-bearing assumption, consider a random-phase three-periodic environment

\[
\alpha_j=w_{j+U\;({\rm mod}\;3)},
\qquad
w=(r,a,b),
\qquad r<a<b\le1,
\]

with `U` uniform on `{0,1,2}`. The shift acts transitively on the three phases, so this law is stationary and ergodic. For `a != b`, reflection changes the cyclic order and the law is not reflection-invariant. The Birkhoff average of the bonus

\[
d_j=\frac1r-\frac1{\alpha_j}
\]

still exists and is positive. But for every

\[
0<\varepsilon<\min(a-r,b-r),
\]

there are no two consecutive rows with rates at most `r+epsilon`, let alone arbitrarily wide near-minimum strips.

So the row-crossing coupling survives while the central-saturation argument fails at precisely the slow-strip step. This does **not** prove that the plateau itself fails in this periodic model; it proves that `ess inf + ergodicity + positive mean bonus` is not enough for the present route. The iid hypothesis supplies a stronger property: every finite near-minimum cylinder has positive probability and hence occurs almost surely somewhere.

A useful abstract formulation of the mechanism is therefore:

1. two-sided ergodic averages of `d_j` give the linear crossing bonus;
2. arbitrary-width near-minimum row strips pin the zero-tilt shape to the homogeneous minimum-rate comparator;
3. homogeneous particle-hole symmetry centers the induced subgradient interval at `K/2`.

This separates the proof into three logically distinct ingredients and removes an unnecessary appeal to reversibility of `Q`.

**B15 outcome:** successful as a stress test. Breaking symmetry did not break the centering mechanism; breaking the slow-strip property did. That identifies the actual obstruction to extending the theorem from iid disorder to general stationary ergodic disorder.

## 6. B22 — read the failures and adjacent literature, not just successful `K=1`

I ran a fresh bounded literature check on 2026-09-19 using combinations of

- `site disorder K-exclusion flux plateau`;
- `disordered K-exclusion flat segment`;
- `partial exclusion random environment asymmetric flux`;
- `Seppäläinen K-exclusion disorder plateau`;
- `translation invariant stationary measures asymmetric K-exclusion`.

The most relevant located items are:

1. **Seppäläinen (1999), Problem 4** — the primary source itself. Section 3 emphasizes that for disordered totally asymmetric `K`-exclusion the flux is not explicit and asks for the flat segment around `K/2`.
2. **Sly (2016), arXiv:1609.06589** — solves the iid site-disorder plateau for ordinary `K=1` TASEP and supplies the exact comparator/coupling mechanism recovered in Section 4 above.
3. **Balázs--Bowen (2018), Ann. IHP 54, 514--528, DOI 10.1214/16-AIHP813** — for asymmetric `K>=2` exclusion, product blocking measures exist but constant-parameter product measures are not stationary; they explicitly state that translation-invariant stationary distributions remain unknown. This confirms why replacing the homogeneous `K=2` shape by a guessed product current would be invalid.
4. **Bahadoran--Bodineau (2016/2018)** — plateau results for ordinary `K=1` TASEP with site disorder, not the rate-one `K>=2` model here.
5. **Floreani--Redig--Sau (2021), SPA 142, 124--158** — random **capacities** and a different partial-exclusion random environment, not Seppäläinen's site-rate disorder.
6. **Gonçalves--Hayashi--Sasada (2024/2025)** — gradient/product-measure partial exclusion with different jump-rate structure.
7. **Ayyer--Misra (2024), J. Phys. A 57, 315001** — an exactly solvable deformed `K`-exclusion model with modified rates; it is not the source rate-one process.

I did **not** locate a paper claiming the full iid site-rate `K>=2` plateau in Seppäläinen's model, nor a paper containing the two-step homogeneous Chernoff estimate above. This is bounded negative evidence, not a completed novelty audit. In particular, the current all-`K` theorem candidate still requires independent proof audit and a citation-graph prior-art audit before any closure or paper claim.

**B22 outcome:** useful. It rules out the tempting but false shortcut through translation-invariant product measures and keeps the nearest exact solved comparator at `K=1`.

## 7. Exact checker and execution record

This run creates only one substantive checker pair, after the new block idea was established:

- `artifacts/hard7_2026-09-18/HARD7-03/two_step_block_chernoff_20260919T0421Z.py` — commit `89116199b24fa14e9c6f1b54368ab8331dcb31f2`;
- `artifacts/hard7_2026-09-18/HARD7-03/two_step_block_chernoff_20260919T0421Z.out` — commit `5ef459f50825a80a2f051df096954d86417d66ec`.

The executed output was read back from commit `5ef459f50825a80a2f051df096954d86417d66ec` and ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker verifies exactly:

- the three block MGFs `H_1,H_2,H_3` at `theta=16/25`;
- the closed form `A_2(theta)=158125/3009`;
- the degree-15 Taylor certificate `S_15(2 theta a)>A_2(theta)` for `a=61903/20000`;
- `L_new=5000/61903`;
- strict improvement over `500000/6578563`.

The checker does **not** replace the probabilistic block argument, Borel--Cantelli step, or the inherited plateau theorem; those are written on the page and remain self-checks pending independent audit.

## 8. What this run did not prove

- It did not independently audit the preceding general-`K` central-saturation/cusp argument.
- It did not resolve particlewise disorder.
- It did not prove that every stationary ergodic site environment has a plateau.
- It did not identify the exact homogeneous `K=2` central shape constant.
- It did not establish novelty of the all-`K` theorem candidate or of the two-step block bound beyond the bounded search.
- It did not call the source Problem 4 closed.

The improvement is nevertheless source-relevant and rigorous at the finite/probabilistic level: it strengthens the certified binary `K=2` plateau half-width through an exact homogeneous block bound.

## 9. Next route

Because the frozen metric moved, there is no stuck run and no rotation. The next execution must use a different triple. The strongest continuation I see is:

- **B4 — prove something weaker completely:** push the homogeneous transfer bound to an exact four-step block before touching the all-`K` proof again;
- **B11 — dualize:** rewrite the block Chernoff sum as a positive transfer operator / Perron--Frobenius bound, so longer blocks can be certified without enumerating all paths independently;
- **B30 — one scale at a time:** localize by block length and displacement, proving a monotone sequence of explicit upper bounds on `G_1(0)` if the transfer construction supports it.

A four-step bound that beats `61903/20000` would move the same frozen metric again without changing the target. If it does not, the run should report that failure rather than manufacture a checker-only commit.

## 10. Capability statement

The currently exposed automation/task surface still provides prompt/title/schedule/timing/enabled controls but no binding model selector, reasoning-effort selector, authenticated maximum-reasoning telemetry, or guaranteed execution duration. GPT-6/maximum is therefore prompt-requested only. The actual model exposed to this run is **GPT-5.6 Sol** and the reasoning level is **UNVERIFIED**.

The repository records historical scheduler errors of the form `You cannot modify this task`, including the earlier P26 case; it also records that P26 was later editable from a different authorized context. This worker did not probe or modify P26 or any other schedule. If a task still returns that permission error, the compliant remedy is the authorized owner/account/workspace interface or platform support/ownership correction. A GitHub edit does not repair scheduler permissions, and creating a duplicate task would violate the policy.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  owner_claim: operations/claims/D0025.md
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  fixed_metric: "rigorous certified lower bound L <= Delta_2(Q) for Q=1/2 delta_{1/2}+1/2 delta_1"
  before: 500000/6578563
  after: 5000/61903
  movement: true
  methods: [6, 15, 22]
  new_homogeneous_bound:
    object: "K=2 homogeneous lazy-LPP central shape G_1(0)"
    before_upper: 6578563/2000000
    after_upper: 61903/20000
    theta: 16/25
    block_length: 2
    proof_status: "self-contained theorem on page + exact finite algebra checker"
  inherited_plateau_candidate:
    scope: "every fixed K>=1, iid nondegenerate site rates Q subset [r,1], r>0"
    audit_status: "self-check only; not closed"
  stress_test:
    conclusion: "disorder reflection symmetry is not load-bearing; arbitrary-width near-minimum strips are"
  prior_art:
    closest_exact: "Sly 2016, K=1 iid site-disorder plateau"
    general_K_plateau_found: false
    search_scope: "bounded 2026-09-19 web/current-literature check"
  exact_artifacts:
    - artifacts/hard7_2026-09-18/HARD7-03/two_step_block_chernoff_20260919T0421Z.py
    - artifacts/hard7_2026-09-18/HARD7-03/two_step_block_chernoff_20260919T0421Z.out
  exact_output_status: "ALL_EXACT_CHECKS_PASS = True"
  section_I_state: "metric moved; stagnation reset to 0"
  next_methods: [4, 11, 30]
  posted_changed: false
  results_changed: false
  queue_changed: false
  claim_changed: false
```

No shared-root mutation, public posting, email, Drive write, independent audit, closure claim, or scheduler change was made in this run.
