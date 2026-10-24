Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed scheduler/runtime surface provides no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement in the frozen source metric: `S=5 -> 5`. Methods tried: B1, B16, B25.**

# HARD7-02 run 7 — an order-biased directed-cycle threshold beyond the forest regime

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question still OPEN_BY_BOUNDED_SEARCH.**

This run attacks the exact place where run 5's forest proof stopped. For the source-valid axis family

`theta_p = p delta_(1,0) + (1-p) delta_(0,1)`, `0<p<1`,

the hard-pair truncation is not merely an undirected Erdos–Renyi graph: every retained edge has exactly one nonzero direction, and its direction is biased by the ambient vertex order. Passing to that directed graph reveals a second threshold. The limiting ESD of the truncation is still exactly `delta_0` throughout a regime in which the undirected exceedance graph is already supercritical.

The rigorous threshold produced here is

`Lambda(p) = log(p/(1-p))/(2p-1)` for `p != 1/2`,

with the continuous value `Lambda(1/2)=2`. For every fixed hard cutoff `h>0` satisfying

`h^(-alpha) < Lambda(p)`,

the empirical spectral law of the axis-family hard-pair truncation converges in probability to `delta_0`. Since `Lambda(p)>=2`, this strictly extends run 5's generic forest range `h^(-alpha)<1`; at the symmetric axis point the certified mean-degree range improves from `<1` to `<2`, and it grows without bound as `p` approaches `0` or `1`.

This is **not** the full source limit: for fixed `0<p<1`, sending `h` down to zero sends `h^(-alpha)` to infinity and eventually exits this window. It is therefore a genuine new route and obstruction diagnosis, not a closure claim.

## 1. Continuity, ownership, required repository state, and current-status check

I resumed the exclusive canonical claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T02-12-00Z__mass-normalization-homogeneity.md`.

At run start I re-read the controlling HARD7 and new-methods files, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical claim, the current HARD7-02 report chain, the previously screened C0026--C0032 intake neighborhood, and the newest neighboring heavy-tail work I located. The neighboring R7-06 claim `C0032` remains the distinct Bordenave–Chafai explicit-density problem; its newest located report is `research7_2026-09-17/R7-06/runs/2026-09-19/2026-09-19T030300Z__report.md`. Repository claim search still assigns Campbell–O'Rourke Question 1.8 only to HARD7-02. No posted, retired, Bernoulli-singularity, personal least-singular-value, Toeplitz/Hankel, additive-spike, gated-product, or equivalent claimed target was found.

### Primary source recheck

Source: Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability 27 (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

The arXiv record checked on 2026-09-19 still lists v3, revised 2022-02-02, as the current version. Definition 1.1 permits the mirrored pair `(xi_1,xi_2)` to have two different marginal laws; the pairs over `i<j` are iid copies of that vector. Conditions C1/C2 use a finite angular measure `theta_d`, the no-complex-hyperplane support condition, and `a_n/n^(1/alpha)->c>0`. Theorem 1.6 supplies the deterministic limit `mu_{alpha,theta_d}`. Section 1.3, Question 1.8 asks exactly:

> “What properties of `theta_d` determine `mu_{alpha,theta_d}`?”

### Fresh bounded literature check, 2026-09-19

I searched the exact source title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, `dependence measure`, `erratum`, `corrigendum`, and 2023--2026 terms. The search recovered the 2022 source, Campbell--O'Rourke's later Levy--Khintchine Laplacian paper and later elliptic/Laplacian work, but no located paper claiming a complete solution of Question 1.8 and no located correction resolving the orientation issue recorded in runs 2--3. This is bounded negative evidence only.

For the directed-graph mechanism below I also searched combinations of `biased orientation`, `vertex order`, `directed cycles`, `random graph`, `cyclic ascents`, and `acyclicity`. Nearby literature includes Ralaivaosaona--Rasendrahasina--Wagner on acyclicity of the **symmetric** sparse random digraph and orientation-Ramsey work on cycles. I did not locate this exact order-biased model/formula in the bounded search. The cyclic-Eulerian enumeration itself is classical combinatorics. I therefore make no standalone novelty claim for that identity or for the random-digraph lemma pending a broader prior-art check.

### Scheduler/interface capability statement

The currently exposed task surface still has prompt/schedule/timing/enabled controls but no model selector or reasoning-effort selector. Hence the requested GPT-6/maximum setting cannot be bound or authenticated by this worker. Historical modification probes for P26/P01/P03 returned `You cannot modify this task`; repository policy records that some later edits succeeded from a different authorized context. If a task still refuses modification, the compliant remedy is the authorized owner/account/workspace interface or platform support/ownership transfer, not a bypass or duplicate schedule. This run made no scheduler changes.

## 2. Frozen source metric and the auxiliary quantity that actually moved

The canonical frozen metric remains

`S = number of exact nontrivial full-source transformation laws theta -> mu_{alpha,theta}`

proved by this track under C2.

Before: `S=5`.

After: **`S=5` (no movement).**

The preceding run moved `S`, so the ordinary unchanged streak is now `1`; Section I is not triggered.

For this run only, a source-relevant auxiliary quantity does move:

`Lambda_axis(p) = largest mean-degree threshold certified by this track below which the axis-family hard-pair truncation has ESD -> delta_0`.

Before, run 5's forest argument certified `Lambda_axis(p)>=1` uniformly in `p`.

After this run,

`Lambda_axis(p) >= Lambda(p) := log(p/(1-p))/(2p-1)`,

with `Lambda(1/2)=2`. In fact the proof below establishes the strict range `lambda<Lambda(p)` exactly for the directed-cycle summability mechanism. Thus at `p=1/2` the certified range improves `1 -> 2`; for `p=2/3`, `Lambda=3 log 2 = 2.07944...`; for `p=3/4`, `Lambda=2 log 3 = 2.19722...`; and `Lambda(p)->infinity` as `p->0,1`.

## 3. B1 — change the category: a source-valid axis dependence measure becomes an order-biased sparse digraph

Fix `0<alpha<2` and `0<p<1`; write `q=1-p`. Let `Y` be positive Pareto with

`P(Y>t)=t^(-alpha)`, `t>=1`,

and define the mirrored atom pair by

`(xi_1,xi_2)=(Y,0)` with probability `p`,

`(xi_1,xi_2)=(0,Y)` with probability `q`,

independently over unordered pairs `i<j`. Set the diagonal atom `zeta=0` and `a_n=n^(1/alpha)`.

Then C1 holds exactly with

`theta_p=p delta_(1,0)+q delta_(0,1)`.

Indeed, for every angular continuity set `D` and fixed `r>0`, once `r a_n>=1`,

`n P( ||(xi_1,xi_2)||>r a_n, angle in D )`

`= r^(-alpha) [ p 1{(1,0) in D} + q 1{(0,1) in D} ]`.

The support contains the two complex-linearly independent coordinate vectors, so it is not contained in any complex hyperplane; and `a_n/n^(1/alpha)=1`. Thus this is a genuine C2 family, not a boundary ensemble outside the source theorem.

For a fixed hard cutoff `h>0`, retain an unordered pair iff `Y>h a_n`, and keep the one nonzero directed entry. For large `n`, the edge-retention probability is exactly

`c_n = h^(-alpha)/n`.

Conditional on retention, an edge `{i,j}`, `i<j`, points upward `i->j` with probability `p` and downward `j->i` with probability `q`. The weights and directions are independent across unordered pairs. Therefore the hard-pair truncation has become a weighted **order-biased orientation of `G(n,c_n)`**.

This is the category change: the relevant obstruction is no longer whether the undirected graph contains cycles, but whether a positive number of vertices can enter nontrivial strongly connected components.

**B1 outcome:** successful. The axis family converts the random-matrix cutoff problem into an exact directed-cycle counting problem while staying inside C2.

## 4. B16 — compute the small cases and identify the cyclic-Eulerian law

Consider a prescribed directed simple cycle order

`v_1 -> v_2 -> ... -> v_k -> v_1`.

Write the relative ranks of `(v_1,...,v_k)` as a permutation `sigma in S_k`. Let `a_cyc(sigma)` be its number of cyclic ascents,

`a_cyc(sigma)=#{i: sigma_i < sigma_{i+1}}`, with `sigma_{k+1}=sigma_1`.

Given that all `k` underlying undirected edges are present, the probability that they point in this prescribed cyclic direction is

`p^(a_cyc(sigma)) q^(k-a_cyc(sigma))`.

Define the average

`I_k(p) = (1/k!) sum_{sigma in S_k} p^(a_cyc(sigma)) q^(k-a_cyc(sigma)).`      (4.1)

Exact enumeration for `3<=k<=8` produced cyclic-ascent counts

- `k=3: 3,3`;
- `k=4: 4,16,4`;
- `k=5: 5,55,55,5`;
- `k=6: 6,156,396,156,6`;
- `k=7: 7,399,2114,2114,399,7`;
- `k=8: 8,960,9528,19328,9528,960,8`.

These are exactly

`#{sigma in S_k: a_cyc(sigma)=j} = k A(k-1,j-1)`,                (4.2)

where `A(n,m)` is the Eulerian number. The checker below verifies (4.2) exhaustively through `k=8`, but the identity has a direct proof: mark the position of the largest element `k`, rotate the cyclic word so that `k` occupies a distinguished location, and delete it. The remaining linear word is a permutation of `k-1` elements; the cyclic ascent count shifts by one, and the `k` possible rotations give the factor `k`.

Hence

`I_k(p) = [p q^(k-1)/(k-1)!] A_{k-1}(p/q)`,                    (4.3)

where `A_n(x)=sum_{m=0}^{n-1} A(n,m)x^m`.

At `p=q=1/2`, this reduces to the sanity check

`I_k(1/2)=2^(-k)`.

Using the classical Eulerian-polynomial exponential generating function gives, for `p!=q`,

`sum_{k>=2} I_k(p) t^k`

`= p t [ (p-q)/(p-q exp((p-q)t)) - 1 ].`                       (4.4)

For `p=q=1/2`, the continuous limit is

`sum_{k>=2} I_k(1/2)t^k = t^2/(4-2t)`.                         (4.5)

Because all coefficients are nonnegative, the positive real singularity gives the convergence radius

`Lambda(p)=log(p/q)/(p-q)`,                                    (4.6)

with `Lambda(1/2)=2`.

Writing `x=p/q`, one has

`Lambda(p)=(1+x) log x/(x-1)`.

The elementary inequality `log x >= 2(x-1)/(x+1)` for `x>=1`, plus symmetry `x<->1/x`, yields

`Lambda(p)>=2`, with equality only at `p=1/2`.                  (4.7)

**B16 outcome:** successful. The small-case sequence identifies the exact all-`k` cycle generating function and a new cutoff scale for this source-valid family.

## 5. B25 — count the same thing twice: directed-cycle summability forces spectral mass to zero

The counting identity becomes useful because eigenvalues of a directed adjacency matrix are controlled by strongly connected components, not by undirected components.

### Theorem 1 — order-biased directed-cycle zero law

Let `D_n` be a random weighted digraph on ordered vertex set `[n]`. Independently for every unordered pair `{i,j}`, `i<j`:

1. retain the pair with probability `c_n`;
2. if retained, orient it `i->j` with probability `p` and `j->i` with probability `q=1-p`;
3. assign any nonzero complex weight to the retained arc (the weight law may be unbounded and may depend on the orientation), independently across pairs conditional on the directions.

Assume

`n c_n -> lambda < Lambda(p)`.

Let `A_n` be its weighted adjacency matrix with zero diagonal. Then

`mu_{A_n} => delta_0` in probability.                            (5.1)

#### Proof

Let `N_{n,k}` be the number of directed simple cycles of length `k`, counted modulo cyclic rotation but not reversal. There are `(n)_k/k` possible directed cycle orders. Averaging over the relative ranks of the chosen vertices and using (4.1),

`E N_{n,k} = ((n)_k/k) c_n^k I_k(p)`.                           (5.2)

Thus

`E[ sum_{k=3}^n k N_{n,k} ]`

`= sum_{k=3}^n (n)_k c_n^k I_k(p)`.                            (5.3)

Choose `lambda'` with `lambda<lambda'<Lambda(p)`. For all sufficiently large `n`, `n c_n<=lambda'`, and `(n)_k<=n^k`, so

`E[ sum_{k=3}^n k N_{n,k} ]`

`<= sum_{k=3}^infinity (lambda')^k I_k(p) < infinity`           (5.4)

by the convergence radius (4.6). Therefore the total number `V_n^cyc` of vertices lying on at least one directed cycle satisfies

`V_n^cyc <= sum_{k=3}^n k N_{n,k} = O_P(1)`.                   (5.5)

Now decompose `D_n` into strongly connected components. Every vertex in a nontrivial strongly connected component lies on a directed cycle, so all nontrivial SCCs together contain `O_P(1)` vertices. Permuting vertices according to a topological ordering of the SCC condensation puts `A_n` into block upper-triangular form. Every singleton SCC contributes the one-by-one diagonal block `[0]`. Hence at least

`n-O_P(1)`

of the eigenvalues of `A_n`, counted with algebraic multiplicity, are **exactly zero**. The remaining `O_P(1)` eigenvalues may be arbitrarily large; that is irrelevant for weak convergence against bounded continuous test functions. Therefore

`mu_{A_n} => delta_0` in probability. `QED`

No nonnormal low-rank perturbation inequality is used. The conclusion comes from the exact block-triangular characteristic polynomial after SCC decomposition.

### Corollary 2 — hard-edge window for the C2 axis family

For the explicit `theta_p` ensemble in Section 3, the hard cutoff has

`n c_n = h^(-alpha)`

exactly for all sufficiently large `n`. Therefore

`h^(-alpha)<Lambda(p)`                                         (5.6)

implies

`mu_{T_n^(h)} => delta_0` in probability.                      (5.7)

Equivalently,

`h > Lambda(p)^(-1/alpha)`.                                    (5.8)

Run 5's forest theorem required `h>1` because it stopped at undirected mean degree one. Since `Lambda(p)>=2`, (5.8) reaches strictly below `1` for every `0<p<1`. At `p=1/2`, it reaches all

`h > 2^(-1/alpha)`.

As `p->0` or `p->1`, `Lambda(p)->infinity`, matching the exactly triangular endpoint intuition: at the excluded C2 endpoints all retained edges point monotonically in one vertex-order direction and every finite matrix is nilpotent.

**B25 outcome:** successful. The same cycle set is counted once by directed cycle orders and again through SCC support of nonzero eigenvalues, giving a source-relevant spectral theorem past the undirected percolation threshold.

## 6. What this changes about the main route

Run 5 identified the emergence of undirected cycles at mean degree one as the point where the weighted-tree matching-polynomial proof ceases to apply. The present theorem shows that, at least for a natural C2 axis family, **that is not the true spectral obstruction**. There is an interval

`1 < h^(-alpha) < Lambda(p)`

in which the undirected exceedance graph already has its giant component, yet the weighted directed matrix still has ESD converging to `delta_0`, because only `O_P(1)` vertices belong to directed cycles.

So the next source-level proof should not try to control all undirected cycles. It should identify the directed strongly connected core that survives Hermitization/cutoff removal. This is a materially different route from run 5.

It also clarifies what the axis family can and cannot test. All `theta_p` have the same product pushforward `pi#theta_p=delta_0`, while run 4's stronger quotient `q(z,w)=(|z|^2,zw)` retains `p`. The present zero-law is compatible with both statistics and does not yet decide whether `pi` alone determines the **full** source limit.

For every fixed `0<p<1`, the remaining gap is unavoidable in this method: as `h->0`, `h^(-alpha)->infinity`, eventually exceeding the finite `Lambda(p)`. A full solution therefore needs one of:

1. a proof that the supercritical directed SCC contributes only a quotient statistic already captured by `q#theta`;
2. a proof that its normalized logarithmic potential becomes insensitive to additional orientation information as `h->0`;
3. or a source-valid pair of normalized dependence measures with the same proposed statistic but different limiting potentials, refuting that statistic.

This run establishes none of those three and does not relabel the source as solved or refuted.

## 7. Exact finite-core verification

Executed exact checker:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T03-12-00Z__axis-biased-cycle-eulerian-check.py`

creation commit:

`7cbf665d9e595a0658e30fb78085065575f230d7`.

Archived output:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T03-12-00Z__axis-biased-cycle-eulerian-check.out`

creation commit:

`66ff9840804eb3363a0cdb8740a1f9809d33eb30`.

The checker exhaustively enumerates every permutation for `3<=k<=8`, verifies the cyclic-Eulerian count (4.2), verifies the exact rational `I_k(p)` formula at `p=1/2,2/3,3/4`, and checks the polynomial coefficients. The executed output ends

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit. The all-`k` theorem is proved on the page above; the finite enumeration is only a consistency certificate.

## 8. Next checkpoint

Frozen source status: **PARTIAL**.

Frozen metric: `S=5 -> 5`, ordinary unchanged streak `1` after run 6's movement.

Auxiliary source-relevant progress: axis-family hard-cutoff zero-law range improves from undirected `lambda<1` to directed

`lambda<Lambda(p)=log(p/(1-p))/(2p-1)`,

with minimum `2` and divergence at the triangular boundary.

A useful next triple, different from this run, is **B5/B20/B29**: vary `p` jointly with the cutoff to quantify the nonuniform C2-boundary layer; identify exactly what fails when the directed SCC first becomes extensive; and compactify the `p->0,1` boundary to test continuity of the normalized quotient law. Any such run must keep `theta` fixed when drawing conclusions about the source limit and must not turn a joint-parameter deformation into a solution of fixed-`theta` Question 1.8.

No closure, paper package, novelty certificate, or independent-audit request is claimed.

```yaml
ledger_delta:
  track: HARD7-02
  target: Campbell-O'Rourke 2022 Question 1.8
  metric: S_full_source_transformation_laws
  before: 5
  after: 5
  movement: false
  ordinary_unchanged_streak: 1
  status: PARTIAL
  auxiliary_quantity: Lambda_axis(p)
  auxiliary_before: ">= 1"
  auxiliary_after: ">= log(p/(1-p))/(2p-1), continuous value 2 at p=1/2"
  shared_root_write_requested: false
```
