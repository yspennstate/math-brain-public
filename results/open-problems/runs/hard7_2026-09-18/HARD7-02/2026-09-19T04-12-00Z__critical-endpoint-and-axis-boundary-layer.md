Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed automation/runtime surface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement in the frozen source metric: `S=5 -> 5`. Methods tried: B17, B28, B29.**

# HARD7-02 run 8 — critical endpoint, exact prior-art correction, and the exponentially thin triangular boundary layer

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question still OPEN_BY_BOUNDED_SEARCH.**

This run does three things that materially change the route without pretending to solve the source question.

1. It finds the exact classical random-digraph paper underlying run 7's order-biased axis model: Łuczak–Cohen (1992). Their three-parameter digraph with `t=0` is precisely the unweighted support graph of the axis hard-pair truncation, and their critical surface is exactly run 7's `Lambda(p)`. Thus the graph threshold itself is **prior art**, not a new random-graph theorem. Run 7's formula remains mathematically correct, but any novelty claim for the threshold/cycle mechanism is withdrawn.
2. It proves a source-relevant spectral statement at the **critical endpoint**, which run 7 did not cover: at `lambda=Lambda(p)` the number of vertices belonging to directed cycles is `O_P(sqrt(n))`, hence the weighted matrix still has ESD converging to `delta_0`. More generally the same conclusion survives a quantified `n`-dependent slightly-supercritical window.
3. It compactifies the C2 boundary `p -> 0,1` and computes the exact first two terms of the boundary layer. If `lambda=h^(-alpha)` is large, the critical axis mass is

   `p_*(lambda)=e^(-lambda)+(2lambda-1)e^(-2lambda)+O(lambda^2 e^(-3lambda))`.

   Therefore the triangular endpoint is exponentially singular in the cutoff scale: fixed interior `p` eventually lies deep in the giant-SCC regime as `h->0`, while `p` must shrink essentially like `exp(-h^(-alpha))` to stay on the zero-ESD side of the support transition.

These results do **not** show that the full source limit is `delta_0` for any fixed interior axis law, and a giant strongly connected component does **not** by itself imply a positive proportion of nonzero eigenvalues. The full classification problem remains open.

## 1. Continuity, ownership, required repository state, and fresh source check

I resumed the exclusive canonical claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T03-12-00Z__axis-biased-directed-cycle-window.md`.

At run start I re-read the controlling HARD7 and new-methods files, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical claim, the complete current HARD7-02 report chain, the C0026 neighborhood of the intake ledger, and the newest neighboring R7-06 heavy-tail report. Repository claim search still assigns Campbell–O'Rourke Question 1.8 only to HARD7-02. The neighboring R7-06 target remains the distinct Bordenave–Chafaï explicit-density problem. No posted, retired, Bernoulli-singularity, personal least-singular-value, Toeplitz/Hankel, additive-spike, gated-product, or equivalent claimed target was found.

The current `master` observed before this write was `3effc580115f111db1338a1510a0ab72bd08230c`; unrelated concurrent fleet writes were active, so this run does not edit a shared root ledger.

### Primary source recheck

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability 27 (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

The arXiv record checked on 2026-09-19 still lists v3, last revised 2 February 2022. Section 1.3 still asks exactly:

> “What properties of `theta_d` determine `mu_{alpha,theta_d}`?”

Definition 1.1 still gives iid mirrored pairs over unordered vertex pairs; Condition C1 uses the finite angular measure `theta_d`; Condition C2 adds the non-hyperplane support condition and `a_n/n^(1/alpha)->c>0`; Theorem 1.6 gives the deterministic limiting ESD.

A fresh bounded search on 2026-09-19 used the exact paper title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, `dependence`, `spectral measure`, `corrigendum`, and 2023--2026 date terms. It recovered the 2022 source and later Campbell–O'Rourke work on Lévy–Khintchine random Laplacians, but no located paper claiming a complete solution of Question 1.8. This is bounded negative evidence only.

### Scheduler/interface capability statement

The currently exposed automation interface still offers prompt/title/schedule/timing/enabled controls but no model selector or reasoning-effort selector. It therefore cannot bind or authenticate GPT-6/maximum from this worker. Changing that requires an authenticated platform surface that actually exposes model and reasoning controls. Historical probes for P26/P01/P03 returned `You cannot modify this task`; the repository records that P26 later became editable in a different authorized context. If a task still refuses modification, the compliant remedy is the authorized owner/account/workspace interface or platform support/ownership transfer, not a bypass or duplicate schedule. This run made no scheduler changes.

## 2. Frozen metric

The canonical frozen quantity remains

`S = number of exact nontrivial full-source transformation laws theta -> mu_{alpha,theta}`

proved by HARD7-02 under C2.

Before: `S=5`.

After: **`S=5` (no movement).**

The five laws remain transpose/swap invariance, common-phase covariance, conjugation covariance, opposite-coordinate-phase invariance, and positive mass/scaling covariance. The critical hard-cutoff theorem below is a theorem about the axis truncation, not a sixth full-source transformation law.

Run 6 moved `S`; run 7 was the first unchanged run; this is the second consecutive unchanged run. The ordinary unchanged streak is therefore `2`. Section I is not yet triggered. If the next substantive run also leaves `S` unchanged, the subsequent run must obey the stuck protocol rather than manufacture another lemma.

For comparison only, the auxiliary axis cutoff region does move:

- before: certified `mu_{T_n^(h)} => delta_0` for `h^(-alpha)<Lambda(p)`;
- after: certified at the endpoint too, `h^(-alpha)<=Lambda(p)`, plus the `n`-dependent near-critical window in Theorem 3 below.

This auxiliary improvement does not reset the frozen `S` streak.

## 3. B17 — the number already existed: exact identification with Łuczak–Cohen (1992)

Run 7 derived

`Lambda(p)=log(p/(1-p))/(2p-1)`,                                (3.1)

with continuous value `Lambda(1/2)=2`, as the convergence radius of the directed-cycle series for the source-valid axis family

`theta_p=p delta_(1,0)+(1-p)delta_(0,1)`.

A wider prior-art search for the *order-biased directed graph itself*, rather than for the random-matrix problem, located the exact model:

Tomasz Łuczak and Joel E. Cohen, **“Giant components in three-parameter random directed graphs,”** *Advances in Applied Probability* 24 (1992), 845–857, DOI `10.2307/1427715`.

For `i>j`, their `D_n(r,s,t)` has only the downward arrow `i->j` with probability `r/n`, only the upward arrow `j->i` with probability `s/n`, both arrows with probability `t/n`, and neither otherwise. Their critical surface is expressed through the smaller root `x(c)` of

`x e^(-x)=c e^(-c)`.                                           (3.2)

Our axis hard-cutoff support graph with `n c_n -> lambda` is exactly their `t=0` model with, for `p<=1/2`,

`r=lambda(1-p),   s=lambda p`.                                 (3.3)

At their critical surface `s=x(r)`, equation (3.2) becomes

`lambda p e^(-lambda p)=lambda(1-p)e^(-lambda(1-p))`,           (3.4)

hence

`log(p/(1-p))=lambda(2p-1)`,                                   (3.5)

which is exactly `lambda=Lambda(p)`.

Their theorem says that below this surface all nontrivial strongly connected components are small cycles (for `t=0`), while strictly above it a strongly connected component of linear order appears. They also state that on the critical surface the probability of having no directed cycle of length at least three tends to zero.

Therefore:

**Prior-art correction.** Run 7's order-biased support threshold `Lambda(p)` and the qualitative small-cycle/giant-SCC transition are classical. The run-7 exact cyclic-Eulerian derivation is a self-contained rederivation of that special case, not a novelty claim. The weighted ESD corollary is not stated in the 1992 paper, but I make no novelty claim for that corollary without a broader spectral prior-art search.

This correction strengthens rather than weakens the route: it tells us exactly where the support-only method must fail. For every fixed `lambda>Lambda(p)`, Łuczak–Cohen give a positive-density SCC. Thus no argument based only on showing that the union of nontrivial SCCs has `o(n)` vertices can work there.

**B17 outcome:** successful. Looking for the derived constant/model in another field found the exact 1992 theory and removed a false novelty risk.

## 4. B28 — replace “all cycles are small” by the typical-eigenvalue statement at criticality

The 1992 theorem leaves the critical surface qualitatively different from the strict subcritical phase: cycles occur with probability tending to one. But for ESD convergence we do **not** need absence of cycles. We only need the fraction of vertices that can belong to nontrivial SCC blocks to vanish. This weaker, typical-eigenvalue target survives at criticality.

Keep `q=1-p` and let `I_k(p)` be the run-7 cyclic orientation factor

`I_k(p)=(1/k!) sum_{sigma in S_k} p^(a_cyc(sigma)) q^(k-a_cyc(sigma)).` (4.1)

Run 7 proved

`F_p(t):=sum_{k>=2} I_k(p)t^k
 = p t[(p-q)/(p-q exp((p-q)t))-1]`                              (4.2)

for `p!=q`, and

`F_(1/2)(t)=t^2/(4-2t)`.                                       (4.3)

### Lemma 1 — critical coefficients are bounded after normalization

For every fixed `0<p<1`, if `Lambda=Lambda(p)`, then there is a finite constant `C_p` such that

`Lambda^k I_k(p) <= C_p`                                       (4.4)

for every `k>=2`. In fact, for `p!=1/2`,

`I_k(p)=Lambda^(-k)+O(R_p^(-k))`                               (4.5)

for some `R_p>Lambda`; for `p=1/2`, equality `I_k=2^(-k)=Lambda^(-k)` holds for all `k>=2`.

#### Proof

For `p!=q`, the poles of (4.2) occur at

`t_m=[log(p/q)+2 pi i m]/(p-q),    m in Z`.                    (4.6)

The positive real pole is `t_0=Lambda`. Every other pole has modulus strictly larger than `Lambda`. At `t=Lambda`,

`p-q exp((p-q)t)=-p(p-q)(t-Lambda)+O((t-Lambda)^2)`.            (4.7)

Therefore the singular part of the first term in (4.2) is

`p t (p-q)/(p-q exp((p-q)t))
 = t/(Lambda-t)+analytic
 = 1/(1-t/Lambda)-1+analytic`.                                 (4.8)

Hence

`F_p(t)-1/(1-t/Lambda)`                                        (4.9)

extends analytically across `Lambda` and is analytic in a disk of radius `R_p>Lambda`, chosen below the modulus of the next pole. Cauchy's coefficient estimate gives (4.5), and (4.4) follows after absorbing finitely many initial coefficients. When `p=q=1/2`, (4.3) gives `I_k=2^(-k)` directly. `QED`

### Theorem 2 — critical weighted spectral zero law

Consider the order-biased weighted digraph of run 7: independently for each unordered pair `{i,j}`, retain it with probability `c_n`; conditional on retention, orient it upward with probability `p` and downward with probability `q`; assign any nonzero complex weight to the retained arc, independently across pairs conditional on directions. Assume

`n c_n = Lambda(p)`                                            (4.10)

for all sufficiently large `n`. Let `A_n` be the weighted adjacency matrix, with zero diagonal. Then

`mu_(A_n) => delta_0` in probability.                           (4.11)

More quantitatively, if `V_n^cyc` denotes the number of vertices lying on at least one directed simple cycle, then

`V_n^cyc = O_P(sqrt(n))`.                                      (4.12)

#### Proof

Let `N_(n,k)` be the number of directed simple cycles of length `k`, counted modulo cyclic rotation. As in run 7,

`E N_(n,k)=((n)_k/k)c_n^k I_k(p)`.                             (4.13)

Therefore Lemma 1 gives

`E[sum_(k=3)^n k N_(n,k)]
 = sum_(k=3)^n ((n)_k/n^k) Lambda^k I_k(p)
 <= C_p sum_(k=3)^n ((n)_k/n^k)`.                              (4.14)

But

`(n)_k/n^k = product_(j=0)^(k-1)(1-j/n)
 <= exp[-k(k-1)/(2n)]`.                                       (4.15)

Thus

`E[sum_(k=3)^n kN_(n,k)]
 <= C_p sum_(k=3)^n exp[-k(k-1)/(2n)]
 = O_p(sqrt(n))`.                                              (4.16)

Every vertex on a directed cycle is counted at least once in the left incidence sum, so

`V_n^cyc <= sum kN_(n,k)=O_P(sqrt(n))`.                         (4.17)

Every vertex in a nontrivial strongly connected component lies on a directed cycle. Topologically order the SCC condensation and permute `A_n` into block upper-triangular form. Every singleton SCC contributes the diagonal block `[0]`. Hence at least

`n-O_P(sqrt(n))`                                               (4.18)

of the eigenvalues, with algebraic multiplicity, are exactly zero. For every bounded continuous test function `f`, the contribution of the remaining blocks is bounded by `2||f||_infty O_P(n^(-1/2))`; therefore the ESD converges weakly in probability to `delta_0`. `QED`

### Corollary 2.1 — endpoint included for the source-valid Pareto axis cutoff

For the explicit C2 axis ensemble of run 7, the hard cutoff satisfies eventually

`n c_n=h^(-alpha)`.                                            (4.19)

Therefore the certified zero-ESD regime is now

`h^(-alpha) <= Lambda(p)`,                                     (4.20)

or equivalently

`h >= Lambda(p)^(-1/alpha)`.                                  (4.21)

Run 7 had only the strict inequality. This is an actual theorem-level extension, but it is still a cutoff theorem rather than a full-source classification law.

### Theorem 3 — a quantified slightly-supercritical spectral window

Let `p` be fixed and `Lambda=Lambda(p)`. Suppose

`n c_n = Lambda exp(eta_n)`,   `eta_n>=0`,                      (4.22)

and for some fixed `delta>0`, eventually

`n eta_n^2 <= (1-delta) log n`.                                (4.23)

Then again

`mu_(A_n) => delta_0` in probability.                           (4.24)

#### Proof

Using Lemma 1 and (4.15),

`E[sum kN_(n,k)]
 <= C_p sum_(k=3)^n exp[-k(k-1)/(2n)+eta_n k]`.                 (4.25)

Completing the square gives the bound

`sum_(k=3)^n exp[-k(k-1)/(2n)+eta_n k]
 = O(sqrt(n) exp(n eta_n^2/2+O(eta_n+1/n)))`.                  (4.26)

By (4.23) this is

`O(n^(1-delta/2+o(1)))=o(n)`.                                  (4.27)

Markov's inequality gives `V_n^cyc=o_P(n)`, and the same SCC block-triangular argument proves (4.24). `QED`

This theorem should not be confused with a sharp random-digraph critical-window theorem. It is only a sufficient window for the **empirical spectral mass at nonzero SCC blocks** to vanish.

**B28 outcome:** successful. The ESD question needs only a typical-vertex statement, and that weaker target includes the exact critical surface and a quantified shrinking supercritical window.

## 5. B29 — add the triangular endpoints and resolve the nonuniform boundary layer

At `p=0` or `p=1`, every retained axis edge points monotonically with the ambient vertex order. Every finite hard-cutoff matrix is triangular with zero diagonal, hence nilpotent, so its ESD is exactly `delta_0`. These endpoints fail the source C2 non-hyperplane support condition and therefore cannot simply be substituted for an interior source law.

The question is how thin the approach to those endpoints must be to remain on the subcritical/critical side when the cutoff is removed.

By symmetry restrict to `0<p<=1/2`. Write

`Lambda(p)= log((1-p)/p)/(1-2p)`.                              (5.1)

Set `x=(1-p)/p>=1`. Then

`Lambda(p)=f(x):=(1+x)log x/(x-1)`.                            (5.2)

A direct derivative gives

`f'(x)=[x-1/x-2log x]/(x-1)^2 >0` for `x>1`,                  (5.3)

because the numerator has derivative `(x-1)^2/x^2` and vanishes at `x=1`. Since `x` decreases as `p` increases, `Lambda(p)` is strictly decreasing on `(0,1/2]`, from `+infinity` to `2`.

Hence for every `lambda>2` there is a unique critical mass

`p_*(lambda) in (0,1/2)` such that `Lambda(p_*)=lambda`.        (5.4)

For small `p`, putting `L=log(1/p)`, expansion of (5.1) gives

`Lambda(p)
 = L+(2L-1)p+(4L-5/2)p^2+O(Lp^3)`.                            (5.5)

Reversion at `lambda->infinity` yields

`p_*(lambda)
 = e^(-lambda)+(2lambda-1)e^(-2lambda)
   +O(lambda^2 e^(-3lambda))`.                                 (5.6)

For the source-valid hard cutoff, `lambda=h^(-alpha)`. Thus the C2 boundary layer is

`p_*(h^(-alpha))
 = exp(-h^(-alpha))
   +(2h^(-alpha)-1)exp(-2h^(-alpha))
   +O(h^(-2alpha)exp(-3h^(-alpha)))`.                           (5.7)

In particular, if one explores a *joint* deformation

`p(h)=exp[-beta h^(-alpha)]`,                                  (5.8)

then as `h->0`:

- if `beta>1`, `Lambda(p(h))>h^(-alpha)` eventually, so the support graph stays on the zero-ESD side;
- if `beta<1`, `Lambda(p(h))<h^(-alpha)` eventually, so Łuczak–Cohen place the support graph in the giant-SCC phase;
- if `beta=1`, one is still slightly on the zero-ESD side, because

  `Lambda(e^(-lambda))-lambda
   =(2lambda-1)e^(-lambda)+O(lambda e^(-2lambda))>0`.           (5.9)

The true critical curve needs the second-order enlargement in (5.6).

This makes the noncommutation explicit:

- first take `p->0` at fixed cutoff: the matrix approaches the triangular/nilpotent boundary;
- first fix any interior `p>0` and send `h->0`: `lambda=h^(-alpha)->infinity` eventually exceeds the finite `Lambda(p)`, so the support graph enters the giant-SCC phase.

Therefore the triangular endpoint cannot justify a full-source conclusion for any fixed interior `theta_p`. Any proof that uses the boundary must control an exponentially thin layer in the pair `(p,h)` and then separately justify exchanging limits. The source question keeps `theta` fixed, so a joint `p=p(h)` deformation is diagnostic, not a solution.

**B29 outcome:** successful. Compactifying the endpoint exposes the exact singular scale that a boundary deformation must overcome.

## 6. What is now known, what is prior art, and what remains

### Corrected prior-art status

The order-biased digraph support transition and its critical surface are classical Łuczak–Cohen 1992. Run 7's independent Eulerian derivation remains a valid proof/check of the special case but is not presented as a new graph theorem.

The critical weighted ESD argument in Section 4 is proved here from the cycle coefficients and SCC block decomposition. I did not locate it in the bounded search, but no novelty claim is made without a broader random-matrix/sparse-digraph search.

### Exact obstruction beyond the critical surface

For fixed `p in (0,1)` and fixed `lambda>Lambda(p)`, the support graph has a linear-size SCC by Łuczak–Cohen. Hence the support-count proof can no longer force an asymptotically full zero eigenspace. This is an exact reason to stop extending the same route.

But the converse is **not** proved: a giant SCC does not imply that its weighted block has a positive density of nonzero eigenvalues, nor does it prove that the full axis-family limit depends on `p`. Structural rank, logarithmic potential, and weight distribution still matter.

### Remaining source-level obligation

Run 6 reduced the normalized source dependence to the quotient law under

`q(z,w)=(|z|^2,zw)`.

The axis family has `zw=0` but different `|z|^2` mixtures. The useful next question is no longer the support threshold itself. It is whether the *weighted giant SCC / Hermitized logarithmic potential* retains the order-bias parameter `p` after the cutoff is removed, or whether that information washes out.

A genuinely different next triple should avoid the completed support-count route. Candidate moves are **B9/B10/B21**: randomize the weighted giant core, attempt to derandomize any resulting potential identity, and compare with non-Hermitian sparse-digraph/free-probability models having the same operator shape. If that fails to move `S`, the run will leave the ordinary unchanged streak at three and the following run must be the section-I thinking/stuck report.

No closure, no paper package, no independent audit request, and no finite computational certificate are claimed. No new checker was created because this run makes no finite exhaustive claim; the theorem-sized claims are proved on the page above.

```yaml
ledger_delta:
  track: HARD7-02
  target: Campbell-O'Rourke 2022 Question 1.8
  metric: S_full_source_transformation_laws
  before: 5
  after: 5
  movement: false
  ordinary_unchanged_streak: 2
  status: PARTIAL
  prior_art_correction: "axis support threshold Lambda(p) is the t=0 special case of Luczak-Cohen 1992"
  auxiliary_quantity: axis_zero_ESD_cutoff_region
  auxiliary_before: "lambda < Lambda(p)"
  auxiliary_after: "lambda <= Lambda(p), plus n-dependent eta window n eta^2 <= (1-delta) log n"
  shared_root_write_requested: false
```
