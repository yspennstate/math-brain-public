Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise.** No authenticated runtime model/effort telemetry or binding selector was exposed.

# P0458 — the standardized degree law throughout the full interior growing-budget regime

Source target: Dabirian–Subramanian, *Connectivity of a family of bilateral preference random graphs*, J. Appl. Probab. 63(2) (2026), §1.1 first additional question: characterize the limiting distribution of `(D-E[D])/sqrt(Var[D])` for a vertex degree `D` in `LK(n,k)`.

Canonical target: `P0458`.  
R7-03 classification: CLOSABLE OUTSIDE / PARTIAL.  
Pre-research claim: `operations/claims/P0458.md`, creation commit `fe14e2db92625b3f6259dab1cdeb597b2e025595`.

## 1. What is new relative to the recovered campaign packet

The prior packet

`probability_campaign_2026_09/codex_20h_20260906/proofs/Bilateral_degree_fluctuations_partial.md`

proved the candidate law only when `k→∞` and `k=o(n^(2/5))`. Its sole range bottleneck was the crude comparison

`0 <= D^0-D <= 2J`,

where `J` counts edges internal to the root's `k` selected neighbors that lie below the root cutoff. Squaring that global count produced the term `k^5/n^2`.

The key observation here is that this comparison throws away almost all locality. Two bilateral-retention indicators at the root share **exactly one** non-root edge. That makes their covariance a one-edge influence calculation, whose total contribution is bounded independently of `k` on the high-probability cutoff event. This removes the `n^(2/5)` barrier completely.

The theorem below covers every sequence with

`k→∞` and `n-k→∞`,

including sparse `k=o(n)`, proportional `k/n→rho in (0,1)`, and near-complete graphs with `n-k→∞` arbitrarily slowly.

## 2. Model and notation

Use the equivalent “smaller score is preferred” version of the model: assign iid `Uniform(0,1)` scores to the edges of `K_n`; each vertex prefers its `k` incident edges with smallest scores; an edge is retained iff both endpoints prefer it. The source uses only score ranks, so reversing the score order does not change the graph law.

Fix a root `0`, and let `D=D_{n,k}` be its degree in `LK(n,k)`. Let `S` be the set of its `k` preferred neighbors and let `X` be the root's `(k+1)`st smallest incident score. Conditional on `X` and on the label set `S`, the `k` scores `(U_i)_{i in S}` of the selected root edges are iid `Uniform(0,X)`, and every edge not incident to the root remains iid `Uniform(0,1)` and independent of these scores.

Write

`H := k-D`

for the number of root-preferred edges rejected by the other endpoint. Define

`p_n := k/n`,

`s_n^2 := k(n-k)/n`,

`sigma_n := s_n/n = sqrt(k(n-k)/n^3)`.

Throughout the theorem assume

`k=k(n)→∞`,  `n-k→∞`.

Then `s_n→∞`.

Let `phi` and `Phi` be the standard normal density and CDF, and define

`g(z) := phi(z)+z Phi(z) = E[(z-Z')_+]`,

where `Z'~N(0,1)`.

Finally set

`v := Var(g(Z)) = 1/3 + (sqrt(3)-2)/(2*pi) ≈ 0.29068789486043867`.

## 3. Main theorem

### Theorem 3.1 (full interior-growth law)

If `k→∞` and `n-k→∞`, then

`H/s_n  =>  g(Z)`

and the first two moments converge. Consequently,

`E[D] = k - s_n/sqrt(pi) + o(s_n)`,

`Var(D) = v s_n^2 + o(s_n^2)`,

and

`(D-E[D])/sqrt(Var(D))  =>  (1/sqrt(pi)-g(Z))/sqrt(v)`.

In particular the standardized limiting law is universal across the whole interior growing-budget regime and is non-Gaussian. Its support is bounded above because `g(z)>0`, strictly increasing, and has range `(0,infinity)`.

For `k=o(n)`, `s_n~sqrt(k)`, so this strictly extends the recovered `k=o(n^(2/5))` packet. For `k/n→rho in (0,1)`, the fluctuation scale is

`s_n ~ sqrt(rho(1-rho)n)`.

For `n-k=o(n)` with `n-k→∞`, the fluctuation scale is

`s_n ~ sqrt(n-k)`.

### Proof overview

The proof has three parts corresponding to the run's Section-B methods:

- **B18 SAY IT IN ANOTHER LANGUAGE:** express each rejection as an order-statistic threshold event and reduce the conditional mean to one beta integral;
- **B25 COUNT THE SAME THING TWICE:** compute pair dependence through the unique shared edge and integrate its exact one-edge influence;
- **B3 PROVE SOMETHING STRONGER:** use that local covariance control to prove the limit for all `k→∞, n-k→∞`, not merely a sparse polynomial window.

The detailed proof follows.

## 4. B18 — exact order-statistic representation

Fix `i in S`. Let `T_i` be the `k`th smallest score among the `n-2` edges incident to `i` other than the root edge `(0,i)`. Then

`T_i ~ Beta(k,n-k-1)`.

Moreover `T_i` is independent of `X` and of `U_i` marginally. The edge `(0,i)` fails bilateral acceptance precisely when

`U_i >= T_i`.

Let `T` be an independent `Beta(k,n-k-1)` variable and define

`q_n(x) := P(U_i>=T_i | X=x)
          = (1/x) E[(x-T)_+]`.

Therefore, with `R_i=1_{U_i>=T_i}` and `H=sum_{i in S}R_i`,

`E[H | X,S] = k q_n(X)`.

The label set `S` is irrelevant to the right side, so we write simply `E[H|X]=kq_n(X)` below.

This is the exact conditional mean of the **actual** degree deficit. No comparison variable `D^0` is used.

## 5. B25 — the unique-shared-edge covariance identity

The issue left by the conditional mean is dependence between `R_i` and `R_j` for two selected neighbors `i!=j`. Their non-root stars share exactly one random edge, namely `(i,j)`. Call its score `W`.

Conditional on `(X,W)`, the random variables `R_i` and `R_j` are independent: after removing their shared edge, they depend on disjoint edge sets, and their root-edge scores are independent conditional on `X`.

Hence

`Cov(R_i,R_j | X) = Var(p_X(W) | X)`,

where `p_X(w)=P(R_i=1 | X,W=w)`.

To calculate the oscillation of `p_X`, condition further on `U_i=u`. Let

`B_u ~ Bin(n-3,u)`

count scores below `u` among the other `n-3` competitors at `i` after removing both the root edge and `W`. Rejection occurs iff

`B_u + 1_{w<u} >= k`.

Thus

`p_X(w)
 = b_X + (1/X) integral_{w}^{X} P(Bin(n-3,u)=k-1) du`

for `0<=w<X`, and equals `b_X` for `w>=X`, where `b_X` does not depend on `w`.

Therefore the total oscillation satisfies

`osc(p_X)
 <= (1/X) integral_0^1 C(n-3,k-1) u^(k-1)(1-u)^(n-k-2) du`.

The beta integral is exact:

`integral_0^1 C(n-3,k-1) u^(k-1)(1-u)^(n-k-2) du = 1/(n-2)`.

Hence

`osc(p_X) <= 1/((n-2)X)`.

By Popoviciu's variance inequality,

`Cov(R_i,R_j|X) <= 1/[4(n-2)^2 X^2]`.

This is the crucial localization. The old comparison paid for the square of the **total number** of internal selected-neighbor edges. The exact covariance calculation pays only for the one shared edge relevant to each pair.

## 6. Conditional noise is negligible on the natural scale

Since `Var(R_i|X)<=q_n(X)`, summing variances and the pair covariance bound gives

`Var(H|X)
 <= k q_n(X) + k(k-1)/[4(n-2)^2 X^2]`.

Let

`G_n := { X >= k/(2n) }`.

Because `X` is the `(k+1)`st order statistic of `n-1` iid uniforms,

`P(G_n^c)
 = P(Bin(n-1,k/(2n)) >= k+1)
 <= exp(-(log 2 - 1/2)k)`

by the exponential Markov bound with multiplier `2`.

On `G_n`,

`k(k-1)/[4(n-2)^2 X^2] <= C`

for a universal constant `C` and all large `n`.

It remains to control the first term. On `G_n`,

`k q_n(X)
 = (k/X) E[(X-T)_+ | X]
 <= 2n E[|X-T| | X]`.

Taking expectations and using Cauchy–Schwarz,

`E[kq_n(X);G_n]
 <= 2n sqrt(E[(X-T)^2])`.

Here

`X ~ Beta(k+1,n-k-1)`,

`T ~ Beta(k,n-k-1)`,

independently. Their variances are

`Var(X)=(k+1)(n-k-1)/(n^2(n+1))`,

`Var(T)=k(n-k-1)/((n-1)^2 n)`,

and their mean difference is `O(1/n)`. Hence

`n sqrt(E[(X-T)^2]) = O(s_n+1)=O(s_n)`.

On `G_n^c`, trivially `0<=H<=k`, while the event has exponentially small probability in `k`. Since `s_n→∞`, this contribution is negligible at scale `s_n^2`.

Combining the preceding bounds yields

`E[ Var(H|X) ] = O(s_n)+O(1)+o(s_n^2)`

and therefore

`E[(H-kq_n(X))^2]/s_n^2 -> 0`.      (6.1)

Thus the entire conditional Bernoulli/dependence noise disappears on the natural `s_n` scale. The leading randomness comes from the root cutoff `X` itself.

## 7. B3 — asymptotics of the conditional mean for every interior regime

Set

`U_n := (X-p_n)/sigma_n`,

`V_n := (T-p_n)/sigma_n`.

Because both beta shape parameters tend to infinity, the beta central limit theorem gives

`U_n => Z`,  `V_n => Z'`,

where `Z,Z'` are independent standard normals. The centering differences are negligible because

`(E[X]-p_n)/sigma_n = 1/s_n ->0`,

and

`(E[T]-p_n)/sigma_n = O(1/s_n) ->0`.

Direct beta-moment formulas also give uniformly bounded fourth moments of `U_n` and `V_n`.

Define

`g_n(u):=E[(u-V_n)_+]`.

Convergence of `V_n` to `Z'` together with uniform integrability implies convergence in Wasserstein-1, so because `x -> (u-x)_+` is 1-Lipschitz,

`sup_u |g_n(u)-g(u)| -> 0`,

where

`g(u)=E[(u-Z')_+]=phi(u)+u Phi(u)`.

Now the exact conditional mean rescales as

`k q_n(X)/s_n
 = [k/(nX)] g_n(U_n)`.                         (7.1)

Indeed `sigma_n=s_n/n`. Also

`k/(nX)=p_n/X ->1`

in probability, because `X/p_n->1`; its relative standard deviation is asymptotically at most the reciprocal square root of the smaller beta shape.

Equations (7.1) and the uniform convergence of `g_n` therefore imply

`k q_n(X)/s_n => g(Z)`.                            (7.2)

The same good-event/beta-tail argument used above gives uniform fourth-moment control of the left side of (7.2): on `G_n`, `k/(nX)<=2` and

`g_n(U_n)<=|U_n|+E|V_n|`,

while on `G_n^c` the variable is at most `k/s_n` and `P(G_n^c)` decays exponentially in `k`. Hence the first two moments in (7.2) converge.

Finally combine (6.1) and (7.2):

`H/s_n => g(Z)`

with first-two-moment convergence.

## 8. Constants and standardization

Let `Z,Z_1,Z_2` be iid standard normals. Then

`E[g(Z)] = E[(Z-Z_1)_+] = 1/sqrt(pi)`.

Also

`E[g(Z)^2]
 = E[(Z-Z_1)_+(Z-Z_2)_+]
 = 1/3 + sqrt(3)/(2*pi)`.

Therefore

`v = Var(g(Z))
   = 1/3 + (sqrt(3)-2)/(2*pi)`.

Since `D=k-H`, moment convergence gives

`E[D]=k-s_n/sqrt(pi)+o(s_n)`

and

`Var(D)=v s_n^2+o(s_n^2)`.

Slutsky's theorem now yields

`(D-E[D])/sqrt(Var(D))
 => [1/sqrt(pi)-g(Z)]/sqrt(v)`.

This proves Theorem 3.1. ∎

## 9. Obstruction first / why this still does not close the entire source question

The source states the limiting-law question without imposing a sparse-growth hypothesis. Theorem 3.1 closes the entire interior growing class, but it deliberately does **not** fake a conclusion when the complement budget stays bounded:

`r_n := n-1-k = O(1)`.

In that regime `s_n` stays bounded, so the conditional Bernoulli noise discarded in (6.1) need not vanish. The root rejects only finitely many of its largest-score edges, and the surviving deficit is expected to have a discrete Poisson/point-process type limit depending on the eventual value of `r_n`. That boundary class must be proved separately.

Likewise fixed `k` is not new R7-03 territory: the source itself credits the Erlang weighted-tree limiting degree distribution there. Source closure must reconcile that known result with the two growing classes rather than claim it again.

Hence the frozen metric moves honestly

`R_unresolved: 2 -> 1`.

The remaining class is exactly `k→∞` with `n-1-k=O(1)`.

## 10. Literature and novelty discipline

The final source version was re-read on 2026-09-19 and still prints the standardized-degree question. Bounded current searches for the exact `LK(n,k)` limiting degree distribution/variance and later Dabirian–Subramanian work found the final 2025/2026 paper and author publication listings but no later source-matching solution. This is negative evidence only. The theorem above is an internal proof candidate until independent audit and a fuller prior-art review are completed.

## 11. Next attack

The next run should not repeat B3/B18/B25. The clean remaining problem is the finite-complement regime `r=n-1-k` fixed. A promising route is the upper-tail point process `n(1-U_e)`: the root's cutoff tends to the `r`th point of a rate-one Poisson process, while neighbor rejection is determined by a finite Poisson count above the root-edge score. The main proof obligation is to control the residual dependence created by shared non-root edges, rather than assuming an unjustified independent thinning.

`ledger_delta`:

```yaml
target: P0458
status_before: PARTIAL
status_after: PARTIAL
metric:
  name: R_unresolved
  before: 2
  after: 1
methods:
  - B18_SAY_IT_IN_ANOTHER_LANGUAGE
  - B25_COUNT_THE_SAME_THING_TWICE
  - B3_PROVE_SOMETHING_STRONGER
new_theorem: full interior growing-budget degree law for k->infinity and n-k->infinity
remaining_source_class: n-1-k=O(1) with k->infinity
fixed_k_status: KNOWN_PRIOR_ART_TO_RECONCILE
```
