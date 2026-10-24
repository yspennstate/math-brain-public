Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only: the exposed scheduler/runtime interface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed run duration. **No movement in the frozen source metric: `S=4 -> 4`. Methods tried: B3, B12, B24.**

# HARD7-02 run 5 — product universality for the subcritical hard-edge truncation, and the cycle obstruction

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question still OPEN_BY_BOUNDED_SEARCH.**

This run did not manufacture a fifth full-source transformation law. Instead it tested the strongest tempting simplification left by run 4 — whether the single complex edge product `zw` might already contain all the dependence information relevant to the limiting eigenvalue law. The result is a rigorous positive theorem in the entire subcritical hard-edge truncation and an exact obstruction to extending that proof mechanically through the supercritical cyclic regime.

The main new theorem is:

> For every fixed pair-norm cutoff whose exceedance graph has limiting mean degree strictly below one, the empirical spectral law of the off-diagonal hard-edge truncation depends on the heavy-tail dependence measure `theta_d` **only through the pushforward under**
> 
> `pi(z,w)=zw`.
> 
> Thus any two source models with the same `pi#theta_d` have the same limiting ESD at that truncation level.

The theorem is not the full Campbell–O'Rourke limit. Sending the cutoff down to zero drives the exceedance graph through the mean-degree-one transition and into a giant cyclic component. An exact triangle computation shows why the tree matching-polynomial proof genuinely stops there: on a cycle, all undirected edge products can be fixed while the characteristic polynomial changes.

## 1. Continuity, source, ownership, fleet state

I resumed the exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T00-12-00Z__relative-phase-gauge-quotient.md`.

This run re-read the required controlling and fleet files:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the canonical HARD7-02 claim and all four preceding HARD7-02 reports found by repository search;
- current claim/alias searches for Campbell–O'Rourke, `theta_d`, heavy-tailed elliptic matrices, and neighboring heavy-tail targets;
- the newest directly neighboring heavy-tail report located at `research7_2026-09-17/R7-06/runs/2026-09-19/2026-09-19T010050Z__report.md`.

The neighboring `C0032` track remains a distinct Bordenave–Chafaï i.i.d. heavy-tailed circular-density identification problem owned by R7-06. `C0031` is likewise distinct. Repository claim searches still identify Campbell–O'Rourke Question 1.8 as exclusively owned by HARD7-02. No posted, retired, personal-manuscript, Bernoulli-singularity, or equivalent claimed target was found under an alias.

### Exact primary-source statement and hypotheses rechecked

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability 27 (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Primary links:

- `https://arxiv.org/abs/2010.01261`
- `https://arxiv.org/pdf/2010.01261`

The arXiv record checked on 2026-09-19 UTC still lists v3, revised 2022-02-02, as the latest version. Section 1.3, Question 1.8, still asks exactly:

> “What properties of `theta_d` determine `mu_{alpha,theta_d}`?”

Condition C1 gives regular variation of the mirrored atom pair with angular finite measure `theta_d` and radial intensity `m_alpha(dr)=alpha r^{-1-alpha}dr`. Condition C2 adds the non-hyperplane-support condition and `a_n/n^(1/alpha) -> c>0`. Theorem 1.6 gives convergence in probability of the empirical eigenvalue measure to the deterministic `mu_{alpha,theta_d}` under C2. The source itself says immediately before Question 1.8 that the limit depends on `theta_d`, but not on every aspect of it.

### Fresh bounded current-literature check

A dated search on 2026-09-19 UTC used the exact paper title and authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, `dependence measure`, `PWIT`, `corrigendum`, `erratum`, `heavy-tailed elliptic`, and 2023--2026 date terms.

It recovered the 2022 source and later elliptic/Laplacian work, including the 2023 elliptic-Laplacian paper and the 2025 Carpenter–O'Rourke sparse elliptic preprint (`arXiv:2508.04891`). The latter studies a different sparse elliptic regime and does not state a solution of the heavy-tailed dependence-classification Question 1.8. I found no later paper in this bounded search claiming a full solution of Question 1.8 and no located corrigendum resolving the rank-orientation issue isolated in HARD7-02 runs 2--3. This is **negative evidence only**, not a proof of worldwide openness or novelty.

### Runtime/scheduler capability statement

The current exposed scheduler interface still does not provide a model selector or reasoning-effort selector. It therefore cannot bind the requested GPT-6/maximum setting from this worker. The actual model visible to this run is GPT-5.6 Sol; authenticated reasoning level is unavailable, hence `UNVERIFIED`.

The repository's current `RESULTS.md` also preserves the distinction that historical native modification probes for P26/P01/P03 returned `You cannot modify this task`, while P26 later succeeded from a different authorized native context. For any task that still refuses modification, the policy-compliant workaround remains the authorized owner/account/workspace interface or platform support/ownership transfer. Do not bypass the permission boundary and do not create a duplicate job. This run made no scheduler changes.

## 2. Frozen metric

The canonical claim fixes

`S = number of exact nontrivial transformation laws for theta_d -> mu_{alpha,theta_d}`

proved by HARD7-02 at the **full source limiting-measure level** under C2, with exact mathematics rather than numerical sampling.

Before: `S=4`.

After: **`S=4` (no movement).**

The subcritical truncation theorem below is deliberately **not counted** as a fifth unit because it concerns a frozen hard-edge cutoff, not the full `mu_{alpha,theta_d}` after all smaller edges are restored. Run 4 had moved `S` from 3 to 4, so the present ordinary unchanged streak is **1**. Section I is not triggered.

## 3. Starting point from run 4

Run 4 proved that opposite coordinate phase is a tree gauge. Writing

`g_phi(z,w)=(e^{i phi}z,e^{-i phi}w)`, 

it proved

`mu_{alpha,g_phi#theta}=mu_{alpha,theta}`

and even invariance under arbitrary edgewise independent mixing of those relative phases at the rank-marked PWIT level. It then showed that

`q(z,w)=(|z|^2,zw)`

is a sufficient statistic: if `q#theta_1=q#theta_2`, then the two full limiting ESDs agree.

The obvious next question is whether `q` is still redundant. Since `|z|^2+|w|^2=1`, fixing the product `p=zw` fixes `|z|^2` up to the coordinate swap `x <-> 1-x`, and global coordinate swap is already an exact invariance from run 1. That makes the following stronger conjectural reduction extremely tempting:

`pi(z,w)=zw` alone might determine `mu_{alpha,theta}`.

This run attacked that route rather than adding another local PWIT lemma.

## 4. B12 — find what is conserved: the exact tree invariant is the edge product

Let `T` be a finite tree with zero diagonal and, for every unoriented edge `{u,v}`, two directed complex weights

`a_{uv}, a_{vu}`.

Let `A_T` be the resulting weighted adjacency matrix. Define the unoriented product mark

`P_e = a_{uv}a_{vu}`.

### Lemma 1 — weighted-tree matching polynomial

For every finite tree `T` with `m` vertices,

`det(lambda I-A_T)
 = sum_{M matching in T} (-1)^|M| lambda^(m-2|M|) prod_{e in M} P_e`.      (4.1)

In particular, the complete eigenvalue multiset of `A_T` depends on the directed edge weights only through the collection of products `{P_e}`.

### Proof

Expand the determinant by permutations. A nonzero term can use only directed matrix entries along graph edges or fixed points from the diagonal `lambda I`. Any permutation cycle of length at least three would trace an undirected cycle in `T`, impossible because `T` is a tree. Thus every nontrivial permutation cycle is a transposition `(uv)` along one tree edge. Distinct transpositions must be vertex-disjoint, hence form a matching `M`. A transposition contributes

`(-1) a_{uv}a_{vu} = -P_{uv}`,

while every unmatched vertex contributes `lambda`. Summing over matchings gives (4.1). `QED`

This is stronger than the unitary relative-phase gauge from run 4 at the finite-tree eigenvalue level: on a tree, **any** transformation

`(a_{uv},a_{vu}) -> (r_e a_{uv}, r_e^{-1} a_{vu})`, `r_e != 0`,

preserves the characteristic polynomial, not merely unit-modulus `r_e`.

Equivalently, because a tree has no cycles, choose a root and solve recursively for nonzero vertex factors `d_v` so that `d_u/d_v=r_e` on each oriented edge. Then the transformed tree matrix is exactly `D A_T D^{-1}`. The distinction from run 4 is crucial: this is generally a **nonunitary** diagonal similarity. It preserves finite-tree eigenvalues exactly but does not automatically preserve the infinite-tree Hermitized root law, because the diagonal cocycle can be unbounded.

The conserved object suggested by the eigenvalue side is therefore

`pi(z,w)=zw`.                                                   (4.2)

## 5. B3 — prove something stronger in the regime where the graph is actually a forest

The preceding lemma is finite and exact. The useful question is whether it controls a genuine asymptotic random-matrix regime rather than isolated trees. It does.

Fix one source model satisfying C1 with index `0<alpha<2`, scaling `a_n`, and angular finite measure `theta`. Put

`M_theta = theta(S(C^2))`.

For a fixed cutoff `R>0`, define the **off-diagonal hard-pair truncation**

`T_n^(R)(i,j)
 = (X_ij/a_n) 1{ ||(X_ij,X_ji)|| > R a_n }`,  `i != j`,          (5.1)

and set `T_n^(R)(i,i)=0`.

The same indicator is used for both orientations of an unordered pair. Let

`G_n^(R)`

be the undirected graph whose edge `{i,j}` is present iff the mirrored pair exceeds the cutoff. By the elliptic-matrix definition these edge indicators are iid across unordered pairs. C1 gives

`n P(||(xi_1,xi_2)||>R a_n) -> lambda_R := M_theta R^(-alpha)`.  (5.2)

Thus `G_n^(R)` is exactly an Erdos–Renyi graph `G(n,p_n)` with `n p_n -> lambda_R`.

### Theorem 2 — subcritical hard-edge product universality

Assume

`lambda_R = M_theta R^(-alpha) < 1`.                            (5.3)

Then the empirical spectral measure of `T_n^(R)` converges in probability, weakly against bounded continuous functions on `C`, to a deterministic probability measure

`mu_R^prod`.

Moreover `mu_R^prod` depends on `theta` only through the finite pushforward measure

`pi#theta`, `pi(z,w)=zw`.                                      (5.4)

Consequently, if two C1 models have the same `alpha` and satisfy

`pi#theta_1 = pi#theta_2`,                                     (5.5)

then for every fixed `R` in their common subcritical regime their hard-pair truncations have the **same limiting ESD**.

If the source normalization makes `theta` a probability measure, (5.3) is simply `R>1`.

### Proof, step 1: the exceedance graph is uniformly subcritical

By (5.2), choose `lambda'` with

`lambda_R < lambda' < 1`.

For all sufficiently large `n`, `(n-1)p_n <= lambda'`. Standard breadth-first exploration is then dominated by a subcritical Galton–Watson process with binomial offspring of mean at most `lambda'`; in particular component-size tails are uniformly exponentially bounded up to an immaterial change of constants.

The expected number of simple cycles is bounded uniformly in `n`:

`E[# cycles]
 <= sum_{k>=3} (n)_k p_n^k/(2k)
 <= sum_{k>=3} (lambda')^k/(2k) < infinity`.                   (5.6)

Starting from the vertices of those cycles, the expected size of all attached subcritical trees is bounded by a geometric factor depending only on `lambda'`. Hence the expected number `C_n` of vertices lying in components that contain a cycle is `O(1)`, and therefore

`C_n/n -> 0` in probability.                                   (5.7)

Deleting every cyclic component leaves a forest and removes only `o_P(n)` vertices. Since the matrix is block diagonal after permuting vertices by connected components, for every bounded continuous test function `f`, deleting those whole components changes the ESD integral by at most

`2 ||f||_infty C_n/n = o_P(1)`.                                (5.8)

No nonnormal rank inequality is being used here; whole direct-sum blocks are removed.

### Proof, step 2: the limiting product mark is determined by `pi#theta`

Let

`Y_n=(xi_1,xi_2)/a_n`

conditioned on `||Y_n||>R`. Regular variation in C1 implies convergence of this conditional law to the normalized restriction of

`nu(dr,ds) = alpha r^(-1-alpha) dr theta(ds)`                  (5.9)

on `r>R`, where `s=(z,w)` lies on the unit sphere and a tail vector is `rs`.

On a retained edge the product mark is

`P_n = Y_{n,1}Y_{n,2}`.

Its limiting value is

`P = r^2 z w = r^2 pi(s)`.                                     (5.10)

Therefore the limiting retained-edge product distribution is the pushforward of the normalized measure in (5.9) under `(r,s)->r^2 pi(s)`. This law depends on the angular dependence measure **only through `pi#theta`**. Conditional marks on distinct retained unordered edges remain independent.

### Proof, step 3: every tree component sees only those product marks

Condition on a forest component `T` of `G_n^(R)`. Its directed retained weights are the conditioned pair marks above. By Lemma 1, the characteristic polynomial and hence the eigenvalue multiset of the corresponding matrix block depend only on the edge products `{P_e}`.

Thus for every fixed finite tree shape, the limiting distribution of its entire block spectrum is determined by `lambda_R` and the limiting product-mark law from (5.10), hence by `alpha`, `R`, and `pi#theta`.

### Proof, step 4: pass from finite components to the empirical ESD

Let `V_n` be a uniform random vertex. In a subcritical `G(n,p_n)` with `n p_n -> lambda_R<1`, the rooted component of `V_n` converges to a finite Poisson Galton–Watson tree `T_lambda` with offspring mean `lambda_R`. The retained edge product marks converge jointly on every fixed finite component to iid copies of (5.10). The uniform exponential component-size bound makes this convergence uniformly integrable at the level needed for bounded test functions.

For a finite component `C`, set

`F_f(C) = (1/|C|) sum_{j=1}^{|C|} f(lambda_j(A_C))`.             (5.11)

The empirical integral is exactly the vertex-size-biased component average

`int f dmu_{T_n^(R)}
 = (1/n) sum_C |C| F_f(C)`.                                    (5.12)

Counts of every fixed marked tree component satisfy the usual subcritical law of large numbers (equivalently, apply the second-moment method after first truncating component size at `K`, then send `K->infinity` using the uniform exponential tail). Hence (5.12) converges in probability to

`E[ F_f(T_lambda, {P_e}) ]`.                                   (5.13)

Equation (5.13) defines a deterministic probability measure `mu_R^prod`. By Steps 2--3, it depends on `theta` only through `pi#theta`. This proves the theorem. `QED`

### What the theorem buys

This is not a simulation and not a finite-size fit. It is an asymptotic equality of limiting ESDs for a fully specified truncation of the exact source model. It shows that the strongest candidate statistic `pi#theta` is **rigorously sufficient for all sufficiently extreme retained pairs**, throughout the complete strict subcritical range

`M_theta R^(-alpha) < 1`.                                      (5.14)

That is a real source-facing reduction: dependence information beyond the product cannot first become visible through the forest of extreme mirrored pairs. Any such extra information must enter when smaller edges accumulate enough connectivity to defeat the forest mechanism.

## 6. B24 — find the extremal obstruction: the mean-degree-one boundary is where this proof dies

The critical cutoff for the forest route is

`R_c = M_theta^(1/alpha)`,                                     (6.1)

so that `lambda_R=1`. For probability-normalized `theta`, `R_c=1`.

I tried to extend Theorem 2 below this boundary by arguing that a finite graph spectrum might always depend only on the products `a_uv a_vu`. That stronger algebraic statement is false.

For a zero-diagonal triangle write

`A = [[0,a,c],
      [b,0,e],
      [d,f,0]]`.

Direct expansion gives

`det(lambda I-A)
 = lambda^3 - lambda(ab+cd+ef) - (a e d + c f b)`.             (6.2)

The first three terms use the unoriented edge products; the constant term contains the two directed cycle monomials.

Take the exact integer matrices

`A = [[0,1,7],
      [2,0,3],
      [11,5,0]]`,

`B = [[0,2,7],
      [1,0,3],
      [11,5,0]]`.                                               (6.3)

`B` is obtained by swapping only the two directed weights on edge `{1,2}`. Both have the same three unoriented edge products

`(2,77,15)`,                                                     (6.4)

but

`det(lambda I-A)=lambda^3-94 lambda-103`,

`det(lambda I-B)=lambda^3-94 lambda-101`.                       (6.5)

So product marks do **not** determine the spectrum of a general cyclic weighted graph.

For `lambda_R>1`, the exceedance graph has a positive-density giant component and the simple deletion-of-cyclic-components argument is unavailable. The triangle calculation therefore identifies the exact structural obligation a full `pi#theta` theorem would have to overcome: one needs a probabilistic cancellation, a Hermitization identity, or a Brown-measure/similarity argument that neutralizes directed cycle holonomy in the random limit. Tree matching polynomials alone cannot do it.

This is **not** a counterexample to the full conjectural statement that `pi#theta` might determine `mu_{alpha,theta}`. It is a counterexample only to the naive finite-graph algebraic proof route. The random supercritical model may still wash out the extra cycle data, but that now has to be proved rather than assumed.

The exact finite arithmetic in (6.3)--(6.5), together with the path control case, was executed and archived:

- checker: `artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T01-12-00Z__subcritical-product-universality-check.py` @ `245e303a8402fac3204a425d8e921b634a9d4b4e`;
- output: `artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T01-12-00Z__subcritical-product-universality-check.out` @ `c102e9b2dcee04a7d0fe698fd7048f62e6df023b`.

The archived output ends

`ALL_EXACT_CHECKS_PASS=True`.

## 7. What changed mathematically this run

The source metric did not move, but the route did. Before this run, run 4 established the two-real-dimensional sufficient statistic `q#theta`, with

`q(z,w)=(|z|^2,zw)`.

After this run we now have a rigorous theorem showing that, on every strict subcritical hard-edge truncation, the first coordinate of `q` is unnecessary: the limit factors all the way through the **one-complex-dimensional product pushforward** `pi#theta`.

The obstruction is also sharp at the level of this method: the forest proof works when `lambda_R<1`, while cyclic holonomy is algebraically real and a giant cyclic component appears for `lambda_R>1`. The unresolved bridge is therefore no longer “guess another dependence parameter”; it is:

> **Can the directed-cycle information that is visible in finite supercritical truncations be shown to disappear from the normalized logarithmic potential as the truncation is removed?**

A positive answer would strongly support `pi#theta` as a full sufficient statistic. A negative answer would require constructing two C2 dependence measures with the same `pi#theta` but a provably different limiting logarithmic potential.

## 8. Route accounting

The run used three Section-B moves not previously used on this target:

- **B3 — PROVE SOMETHING STRONGER.** Rather than another special symmetry, I promoted the tree product identity to an entire asymptotic subcritical truncation theorem. Outcome: success, Theorem 2.
- **B12 — FIND WHAT IS CONSERVED.** The conserved quantity under arbitrary tree diagonal similarity is the directed-pair product `a_uv a_vu`; on source angular data this is `pi(z,w)=zw`. Outcome: success, exact matching-polynomial mechanism.
- **B24 — FIND THE EXTREMAL OBJECT.** The extremal obstruction is the onset of cyclic components at mean degree one. An exact triangle with fixed edge products but different characteristic polynomial proves that the forest mechanism cannot simply be extended to cyclic graphs. Outcome: successful obstruction isolation, not a source counterexample.

No method number from the immediately preceding triple B5/B11/B14 was repeated, and none of B3/B12/B24 had appeared in HARD7-02 runs 1--4.

## 9. Next checkpoint

Status remains **PARTIAL**. The frozen metric is `S=4`; unchanged streak `1`.

The next run should not repeat B3/B12/B24. A useful unused triple is **B4/B19/B29**:

- B4: prove the critical endpoint `lambda_R=1` product-universality theorem completely, if the cyclic-vertex mass can be shown `o(n)` with mark control;
- B19: formulate the supercritical cycle-holonomy contribution as an explicit exploration/log-determinant algorithm rather than an informal obstruction;
- B29: compactify the multiplicative diagonal-gauge cocycle and test whether its boundary growth is negligible in normalized Fuglede–Kadison/log-determinant scale.

The source-level remaining obligation is still the full Question 1.8 classification. No closure, novelty certificate, paper package, or independent-audit request is claimed this run.

## 10. Structured ledger delta (report-only; shared root not edited)

```yaml
ledger_delta:
  track: HARD7-02
  canonical_claim: CAMPBELL-OROURKE-2022-Q1.8
  source_status: OPEN_BY_BOUNDED_SEARCH
  status: PARTIAL
  metric: S
  before: 4
  after: 4
  movement: no movement
  ordinary_unchanged_streak: 1
  methods: [B3, B12, B24]
  new_result: "For every hard-pair cutoff with M_theta R^{-alpha}<1, the truncated ESD limit depends on theta only through pi#theta, pi(z,w)=zw."
  obstruction: "Cyclic components carry directed cycle monomials not determined by edge products; exact triangle witness archived."
  next_obligation: "Decide critical endpoint and then control or refute supercritical cycle holonomy in normalized log potential."
  closure: false
  audits_requested: 0
```

Shared `RESULTS.md` was not edited: under the current policy P26/designated coordinators own shared-root maintenance unless separately assigned, and this worker records its delta immutably here instead.
