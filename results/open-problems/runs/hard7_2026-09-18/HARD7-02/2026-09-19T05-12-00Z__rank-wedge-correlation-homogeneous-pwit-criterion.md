Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed automation/runtime surface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement in the frozen source metric: `S=5 -> 5`. Methods tried: B9, B10, B26.**

# HARD7-02 run 9 — exact rank-wedge correlation and the sharp homogeneous-PWIT collapse criterion

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question still OPEN_BY_BOUNDED_SEARCH.**

This run attacks a tempting sixth-law route rather than extending the cutoff calculations from runs 7--8. The tempting route is: randomly relabel the elliptic matrix, observe that every individual mirrored edge is marginally symmetrized under coordinate swap, and hope that the full limit therefore depends only on the swap-symmetrized dependence measure. That route is false at the local-process level for an exact and quantifiable reason.

The main new facts are:

1. for a uniformly relabeled root and two distinct incident edges, the two order signs have the exact law
   `P(++ )=P(--)=1/3`, `P(+-)=P(-+)=1/6`, for every finite `n>=3`;
2. after the heavy-tail angular limit, if `bar theta` is the normalized angular measure and `tau(z,w)=(w,z)`, then the two-edge angular law is
   `s⊗s + (1/12)(bar theta-tau#bar theta)⊗(bar theta-tau#bar theta)`,
   where `s=(bar theta+tau#bar theta)/2`;
3. consequently the corrected rank-marked PWIT of run 3 collapses, after forgetting rank types, to an ordinary homogeneous independently marked PWIT **if and only if** `theta=tau#theta`;
4. in the source-valid axis family `theta_p=p delta_(1,0)+(1-p)delta_(0,1)`, the local outgoing degree at a hard cutoff has variance
   `lambda/2 + lambda^2(2p-1)^2/12`,
   so the hidden rank variable leaves an explicit nonzero local signature for every `p!=1/2`.

These statements do **not** prove that `mu_{alpha,theta_p}` differs from `mu_{alpha,theta_{1/2}}`; local singular/resolvent data can differ without yet proving different Brown/eigenvalue limits. Therefore no sixth full-source transformation law is claimed. What is proved is a sharp obstruction to deriving such a law by random relabeling or by replacing the rank-marked limit with independently swap-symmetrized edges.

## 1. Continuity, ownership, required repository state, and current-status check

I resumed the exclusive canonical claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T04-12-00Z__critical-endpoint-and-axis-boundary-layer.md`.

At run start I re-read the controlling HARD7/new-methods files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical claim, the current HARD7-02 report chain, and the newest neighboring heavy-tail report located at

`research7_2026-09-17/R7-06/runs/2026-09-19/2026-09-19T050300Z__report.md`.

The neighboring R7-06 target remains the distinct Bordenave--Chafai explicit-density problem `C0032`; it is not an alias of Campbell--O'Rourke Question 1.8. Repository-wide claim search still assigns the present question only to HARD7-02. No posted, retired, Bernoulli-singularity, personal least-singular-value, Gaussian row-submatrix, Toeplitz/Hankel, additive-spike, gated-product, or equivalent current claim was found.

The fresh `master` observed immediately before persistence preparation was

`e589240238b4c364b8de32e9676e60e8959ffefd`.

Shared root ledgers are not modified by this worker; the structured delta is recorded below for the designated maintainer.

### Primary source and bounded fresh literature search

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability 27 (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Primary URL:

`https://arxiv.org/abs/2010.01261`

The live arXiv record checked on 2026-09-19 still lists v3, revised 2 February 2022, as the latest version. Definition 1.1 still defines iid mirrored pairs over unordered vertex pairs. Conditions C1/C2 still use the finite angular measure `theta_d`, the no-complex-hyperplane support condition, and `a_n/n^(1/alpha)->c>0`. Theorem 1.6 still gives the deterministic limiting ESD `mu_{alpha,theta_d}`. Section 1.3 still asks exactly:

> “What properties of `theta_d` determine `mu_{alpha,theta_d}`?”

A fresh bounded search on 2026-09-19 used the exact title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, `dependence`, `spectral measure`, `PWIT`, `correction`, `erratum`, and 2023--2026 date terms. It recovered the source, Campbell--O'Rourke's later Levy--Khintchine random-Laplacian paper, and a 2025 finite-moment global-elliptic paper, but no located source claiming a complete solution of Question 1.8 or a correction that removes the rank-orientation issue isolated by HARD7-02. This is bounded negative evidence only, not a worldwide novelty or openness certificate.

### Scheduler/interface capability statement

The exposed automation surface still offers prompt/title/schedule/timing/enabled controls but no binding model selector or reasoning-effort selector. It therefore cannot enforce or authenticate GPT-6/maximum from this worker. Changing that requires an authorized platform surface whose schema actually exposes model and reasoning controls.

The repository preserves historical native modification failures reading `You cannot modify this task` for P26/P01/P03, while current `RESULTS.md` records that P26 later became editable in a different authorized context. If a task still refuses modification, the compliant workaround remains the authorized owner/account/workspace interface or platform support/ownership transfer; do not bypass the restriction and do not create a duplicate task. This run made no scheduler changes.

## 2. Frozen metric and stuck counter

The canonical frozen quantity remains

`S = number of exact nontrivial full-source transformation laws theta -> mu_{alpha,theta}`

proved by HARD7-02 under C2.

Before: `S=5`.

After: **`S=5` (no movement).**

The five laws remain:

1. transpose / coordinate-swap invariance;
2. common-phase covariance;
3. complex-conjugation covariance;
4. opposite-coordinate-phase invariance, with run 4's arbitrary relative-phase mixing and `q`-quotient consequence;
5. positive mass/scaling covariance.

Run 6 moved `S`; runs 7 and 8 left it unchanged; this run is the **third consecutive unchanged run**. Therefore the ordinary unchanged streak is now `3`, and the **next HARD7-02 execution must obey Section I's thinking-only stuck protocol**. It must not manufacture another auxiliary lemma while pretending the frozen source quantity moved.

The auxiliary quantity that *does* become exact in this run is the rank-wedge dependence defect:
for two incident extreme edge marks,
`Delta_wedge(f,g)=(1/12) delta(f) delta(g)`,
where `delta=bar theta-tau#bar theta`. This is source-relevant route information but is not counted as movement in `S`.

## 3. Setup from the corrected rank-marked local limit

Normalize the finite angular measure using run 6:

`m=theta(S(C^2))`,
`bar theta=theta/m`.

Let

`tau(z,w)=(w,z)`.

Write `bar nu=bar theta x m_alpha` for the normalized angular/radial intensity; restoring the scalar mass `m` only rescales the radial intensity and does not affect the rank-order calculation below.

Run 3 proved that the correct local heavy-edge limit retains the normalized original rank `u in [0,1]`. Conditional on a vertex of type `u`, its marked offspring process has kernel

`K_u(dv,dy)
 = 1_{v>u} dv nu(dy) + 1_{v<u} dv (tau#nu)(dy).`               (3.1)

The pair norm law is the same on both sides because `tau` preserves norm, but the angular orientation need not be the same. Runs 2--3 showed that forgetting `u` prematurely is precisely where the homogeneous-PWIT argument can fail.

This run quantifies that failure exactly.

## 4. B9 — RANDOMIZE: exact two-edge order correlations survive uniform relabeling

Uniform random relabeling is an exact spectral similarity, so it is a natural candidate for producing a new transformation law. The one-edge marginal is indeed swap-symmetrized. The mistake is to infer independence from that marginal statement.

Fix `n>=3`. Choose a root rank

`R` uniformly from `{1,...,n}`

and then choose two **ordered distinct** neighbor ranks `J_1,J_2` uniformly without replacement from the other `n-1` ranks. Define

`H_i = 1{J_i>R}`.

### Lemma 1 — exact finite-n order-sign law

For every `n>=3`,

`P(H_1=1,H_2=1)=1/3`,                                         (4.1)

`P(H_1=0,H_2=0)=1/3`,                                         (4.2)

`P(H_1=1,H_2=0)=P(H_1=0,H_2=1)=1/6`.                          (4.3)

In particular

`P(H_i=1)=1/2`,                                                (4.4)

but

`Cov(H_1,H_2)=1/12`.                                           (4.5)

#### Proof

Condition on `R=r`. There are `h=n-r` higher ranks and `l=r-1` lower ranks. Thus

`P(H_1=H_2=1 | R=r)
 = h(h-1)/[(n-1)(n-2)].`

Averaging over `r`, and writing `k=n-r`,

`(1/n) sum_{k=0}^{n-1} k(k-1)
 = (n-1)(n-2)/3.`

Dividing by `(n-1)(n-2)` gives (4.1). Equation (4.2) follows by rank reversal. For the ordered mixed event,

`P(H_1=1,H_2=0 | R=r)
 = (n-r)(r-1)/[(n-1)(n-2)]`.

The identity

`sum_{k=0}^{n-1} k(n-1-k)
 = n(n-1)(n-2)/6`

gives (4.3). The marginal and covariance follow immediately. `QED`

The coefficient `1/12` is therefore not an asymptotic approximation: it is an exact order-statistic identity at every finite size.

### Theorem 2 — the extreme two-edge angular law

Take the uniformly relabeled elliptic matrix and orient each incident mirrored pair away from the random root. Pick two distinct incident unordered pairs independently of their values, and condition on both pair norms exceeding `r a_n`, with fixed `r>0`. Let `Y_1,Y_2` be their angular directions as viewed away from the root.

Then under C1,

`Law(Y_1,Y_2 | both exceed r a_n)`

converges weakly to

`J_theta
 = (1/3) bar theta⊗bar theta
 + (1/6) bar theta⊗(tau#bar theta)
 + (1/6) (tau#bar theta)⊗bar theta
 + (1/3) (tau#bar theta)⊗(tau#bar theta).`                      (4.6)

Let

`s = (bar theta+tau#bar theta)/2`,
`delta = bar theta-tau#bar theta`.

Then exactly

`J_theta = s⊗s + (1/12) delta⊗delta.`                           (4.7)

Consequently, for bounded continuous test functions `f,g`,

`Cov(f(Y_1),g(Y_2))
 -> (1/12) delta(f) delta(g).`                                 (4.8)

#### Proof

The two unordered matrix-edge variables are independent and identically distributed before relabeling. C1 implies that, conditional on a pair-norm exceedance, the angular law converges to `bar theta`; viewing the same pair from the larger original rank swaps its two coordinates and hence gives `tau#bar theta`.

The order signs `(H_1,H_2)` are independent of the edge values, and Lemma 1 gives their exact four probabilities. Conditioning on each of the four sign patterns therefore gives (4.6). Expanding `s⊗s` shows

`J_theta-s⊗s
 = (1/12)(bar theta-tau#bar theta)
             ⊗(bar theta-tau#bar theta)`,

which is (4.7), and testing against `f⊗g` gives (4.8). `QED`

**B9 outcome:** the randomization route does not produce edgewise iid swap symmetrization. It produces a latent-rank mixture whose one-edge marginal is symmetrized but whose two-edge law contains the exact rank-one tensor defect `(1/12) delta⊗delta`.

This is the obstruction a putative sixth law based only on random relabeling has to survive.

## 5. B10 — DERANDOMIZE: an iff criterion for when the rank mark can actually be erased

The previous calculation can be lifted from two sampled edges to the whole root offspring point process.

Fix a Borel mark set `B` bounded away from zero, so `nu(B)` and `(tau#nu)(B)` are finite. Conditional on the root type `U=u`, the corrected rank-marked PWIT has a Poisson number of `B`-marked children with mean

`Lambda_u(B)
 = (1-u) nu(B) + u (tau#nu)(B).`                               (5.1)

After forgetting `U`, this is a mixed Poisson variable.

### Theorem 3 — sharp homogeneous-PWIT collapse criterion

For the corrected local limit, the following are equivalent.

1. After forgetting rank types, the root offspring point process is an ordinary Poisson point process with deterministic mark intensity.
2. For every finite-intensity Borel mark set `B`, the count `N(B)` is Poisson with its own mean.
3. `nu=tau#nu`.
4. `theta=tau#theta`.

Hence **swap symmetry is exactly the class in which the rank variable is spectrally/local-process redundant at the point-process level**.

#### Proof

`(4) => (3)` is immediate because the radial intensity is swap invariant. If `(3)` holds, (5.1) is independent of `u`, so the conditional offspring PPP has the same deterministic intensity for every root type; forgetting `U` changes nothing. Thus `(3)=>(1)=>(2)`.

For `(2)=>(3)`, write

`a=nu(B)`, `b=(tau#nu)(B)`.

A mixed Poisson variable satisfies

`E N(B)=E Lambda_U(B)=(a+b)/2`,                                (5.2)

and

`Var N(B)
 = E Lambda_U(B) + Var Lambda_U(B)
 = (a+b)/2 + (a-b)^2/12`.                                     (5.3)

If `N(B)` is Poisson, its variance equals its mean, hence `a=b`. This holds for every finite-intensity set bounded away from zero; a monotone-class exhaustion gives `nu=tau#nu`. Since the radial factor is common, this is equivalent to `theta=tau#theta`. `QED`

Equation (5.3) is a quantitative obstruction, not just an iff statement. Any set `B` on which the mirrored tail measure is asymmetric produces positive overdispersion exactly equal to `(a-b)^2/12`.

### Corollary 3.1 — quantitative two-edge total-variation obstruction

Let the angular measures be probability-normalized and let

`d = sup_A |bar theta(A)-(tau#bar theta)(A)|`.

Then the two-edge law from Theorem 2 obeys

`d_TV(J_theta,s⊗s) >= d^2/12`.                                 (5.4)

Indeed, for any angular set `A`,

`J_theta(A x A)-s(A)^2
 = [bar theta(A)-(tau#bar theta)(A)]^2/12`.                     (5.5)

Taking the supremum gives (5.4).

This makes the failure of iid symmetrization robust: unless `theta` is swap symmetric, there is a fixed positive two-edge discrepancy that does not vanish with matrix dimension.

### Relation to the run-4 gauge quotient

Run 4 proved that relative phase along each edge is a tree gauge and that

`q(z,w)=(|z|^2,zw)`                                            (5.6)

gives a sufficient statistic for the full limiting ESD.

Some of the signed measure `delta=bar theta-tau#bar theta` can therefore live in spectrally irrelevant phase fibers. The rank-wedge obstruction still survives after quotienting whenever the normalized quotient law

`Q=q#bar theta`

is not invariant under

`R(x,p)=(1-x,p)`.                                               (5.7)

Indeed, for any test function `F` on the quotient and `f=F o q`,

`delta(f)
 = Q(F)-(R#Q)(F)`.                                             (5.8)

Thus the exact covariance (4.8) can be witnessed by a **gauge-invariant** observable whenever `Q != R#Q`. Random relabeling therefore cannot erase the `|z|^2` coordinate of the run-4 quotient by a mere independence argument.

**B10 outcome:** successful. The vague statement “rank information matters” is replaced by an exact necessary-and-sufficient criterion plus a quantitative defect.

## 6. B26 — HUNT THE SPORADIC CASE: the axis family and its unique homogeneous point

Return to the source-valid axis family used in runs 7--8,

`theta_p
 = p delta_(1,0) + (1-p) delta_(0,1)`,
`0<p<1`.                                                       (6.1)

It is swap symmetric exactly at

`p=1/2`.                                                        (6.2)

This is therefore the unique interior axis parameter at which Theorem 3 allows the rank mark to disappear from the offspring point process.

### Exact wedge signature

Let `A` be the first-axis atom `(1,0)`. The one-edge symmetrized marginal satisfies

`s(A)=1/2`

for every `p`. But Theorem 2 gives

`J_{theta_p}(A x A)-1/4
 = (2p-1)^2/12`.                                               (6.3)

Thus two incident extreme edges recover the imbalance `|2p-1|` exactly even though one incident edge cannot.

For example, at `p=3/4` the discrepancy is `1/48`; at `p=1/2` it is exactly zero.

### Hard-cutoff outgoing degree

At a fixed hard cutoff whose retained unordered-pair mean degree tends to `lambda`, condition on the limiting root rank `U=u`. An incident retained edge points **outward** from the root with probability

`m_p(u)=p(1-u)+(1-p)u`.                                        (6.4)

Therefore the limiting outgoing degree conditional on `U=u` is

`D_out | U=u ~ Poisson(lambda m_p(u)).`                         (6.5)

Averaging over `U~Uniform[0,1]`,

`E D_out = lambda/2`,                                          (6.6)

while

`Var D_out
 = lambda/2 + lambda^2(2p-1)^2/12`.                            (6.7)

At the symmetric point `p=1/2`, (6.5) loses all `u` dependence and (6.7) reduces to the ordinary Poisson variance `lambda/2`. For every `p!=1/2`, the positive extra variance is the exact local footprint of the global random ordering.

This also explains why the Łuczak--Cohen support threshold from runs 7--8 can depend strongly on `p` despite the one-edge swap-symmetrized marginal being independent of `p`: the dependence is stored in correlations around common vertices, not in isolated edges.

**B26 outcome:** successful. The sporadic parameter `p=1/2` is characterized as the unique interior axis point at which the corrected local process truly homogenizes.

## 7. What this rules out, and what it does not

### Ruled out as a proof route

A prospective sixth law

`mu_{alpha,theta}
 ?= mu_{alpha,(theta+tau#theta)/2}`                             (7.1)

cannot be justified by saying “uniform permutation makes each edge independently choose its orientation with probability `1/2`.” Uniform permutation only gives the one-edge marginal in (7.1). The exact common-root wedge correlation is (4.7), and the full offspring process is the mixed PPP of Theorem 3.

Likewise, replacing the rank-marked PWIT by a homogeneous PWIT is source-valid without further work only on the swap-symmetric class.

### Not ruled out mathematically

Equations (4.7) and (5.3) do **not** prove that (7.1) is false at the level of the final eigenvalue law. It remains logically possible that Hermitization and the logarithmic-potential map discard precisely these rank correlations, even though the local singular/resolvent process sees them. Proving or refuting (7.1) therefore remains a legitimate hard route.

The same warning applies to the stronger product-only idea from run 5. The axis measures `theta_p` all have the same edge-product pushforward `pi#theta_p=delta_0`, yet this run proves that their corrected local extreme-edge processes differ for `p!=1/2`. That is a serious obstruction to a naive product-only proof, but it is not itself a counterexample to product-only dependence of `mu`.

### Sharp remaining obstruction

The cleanest next source-level question is now:

`Does the logarithmic-potential functional in Theorem 1.6
 annihilate the rank-wedge tensor (1/12) delta⊗delta,
 or can one extract from it a z-dependent scalar that is nonzero
 for some gauge-invariant delta?`                              (7.2)

A proof of annihilation for every `delta` would point toward a sixth symmetrization/product law. A single source-valid `z` and `theta` for which the induced log-singular-value integral changes would refute that route and show that more of the quotient law `q#theta` is genuinely needed.

Because `S` has now failed to move for three consecutive runs, however, the next execution must address this through Section I's required strategy review rather than immediately adding another technical lemma.

## 8. Exact self-check

The finite algebra used in Lemma 1, the tensor coefficient in (4.7), the axis defect (6.3), and the mixed-Poisson variance (6.7) were checked symbolically with exact rational arithmetic.

Artifacts:

- `artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T05-12-00Z__rank-wedge-exact-check.py`
- `artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T05-12-00Z__rank-wedge-exact-check.out`

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker is a self-check of the finite algebra only. The theorem-sized probabilistic statements are proved on the page above; the checker is not presented as a substitute for those proofs.

## 9. Section-I trigger for the next execution

This run makes the consecutive frozen-metric sequence

- run 7: `S=5 -> 5`;
- run 8: `S=5 -> 5`;
- run 9: `S=5 -> 5`.

Therefore HARD7-02 is now **STUCK by the owner's definition**. The **next** run must be a thinking-only Section-I report containing all five required items:

1. the exact blocking statement in one displayed formula;
2. every route tried and the precise reason each failed;
3. what a proof would need that no current route supplies;
4. the simplest special case still unproved;
5. the nearest solved literature analogue and the ingredient absent here.

It must then choose exactly one permitted recovery action and name a fresh three-method triple. It must not treat the auxiliary wedge theorem as movement in `S`.

This is the first Section-I trigger for the current target under the run-6 reset; no recovery is consumed until that next stuck report actually executes.

## 10. Ledger delta for the shared maintainer

```yaml
track: HARD7-02
claim: CAMPBELL-OROURKE-2022-Q1.8
target: Campbell-O'Rourke 2022 Question 1.8
status: PARTIAL / source OPEN_BY_BOUNDED_SEARCH
metric: S = exact nontrivial full-source transformation laws theta -> mu_alpha,theta
before: 5
after: 5
movement: no
consecutive_unchanged: 3
section_I_next_run: true
methods: [B9, B10, B26]
new_result:
  - exact finite-n root-order wedge law 1/3,1/6,1/6,1/3
  - two-edge heavy-tail angular defect (1/12)(theta-tau theta) tensor-square
  - homogeneous-PWIT collapse iff theta is swap symmetric
  - axis outgoing-degree variance lambda/2 + lambda^2(2p-1)^2/12
closure: false
audits_requested: 0
shared_root_edit: none
```

## 11. Checkpoint

Best current source-level structural information remains:

- five exact full-source covariance/invariance laws;
- canonical mass normalization;
- the full-source sufficient quotient `q#theta`, `q(z,w)=(|z|^2,zw)`;
- the corrected rank-marked local limit for nonswap-symmetric `theta`;
- subcritical hard-edge product universality;
- the source-valid axis hard-cutoff zero-ESD region through the critical endpoint and a near-critical window;
- and now the exact rank-wedge tensor showing precisely how swap asymmetry survives random relabeling.

The source question is not closed, no new paper package is warranted, and no independent closure audit is requested.
