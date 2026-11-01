Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO MOVEMENT on `BLANC-RENAUDIE-2026-MEANFIELD-7-10`: `M_A=0 -> 0`; stagnation count remains UNKNOWN. Methods used: #7, #18, #25.**

# R09 — polynomializing the first local-modification threshold in Blanc-Renaudie

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**

## 1. Continuity, source status, and frozen metric

I continued from `runs/R09/20260918T2130Z_blanc_palm_sizebias_adaptive_core_4f72c9.md`; I did not reopen Tang Question 4.11, G0013, the Chen--Wang Gaussian-subuniformity successor, or the distinct C0064 Fourier-infrared-bound problem. Before research I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the exclusive claim `operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md`, the newest own R09 report, and the neighboring C0064 history.

The active source remains Arthur Blanc-Renaudie, *Markovian renormalisation for percolation in high-dimension: Semi-decidability of mean field behavior*, arXiv:2609.20764v1. A fresh exact-title/arXiv-ID/author search on 2026-09-18 recovered the source (submitted 2026-09-17, current arXiv metadata updated 2026-09-18) and no later primary-source resolution of the nearest-neighbor cases `d=7,8,9,10`. This is bounded negative evidence, not a worldwide novelty certificate.

The source's Theorem 1.1 says that, for each `d>6`, critical mean-field behavior is equivalent to existence of a subcritical `p_0` and `C` satisfying

\[
\chi(p_0)\ge f_d(C),\qquad
\tau_{p_0}(x)\le C\langle x\rangle^{2-d}\quad\forall x\in\mathbb Z^d,
\tag{C}
\]

for a computable but not explicitly expanded function `f_d`. The paper states that the constants were not expanded because the quantitative local modifications make them enormous. The source also records nearest-neighbor `d>=11` as known and `d=7,8,9,10` as the unresolved numerical-proof regime.

The frozen R09 metric remains

\[
M_A:=\#\{d\in\{7,8,9,10\}:\text{a complete rigorous source-valid initialization certificate is obtained}\}.
\]

No dimension is certified here:

\[
\boxed{M_A:0\longrightarrow0.}
\]

The stagnation count remains **UNKNOWN**; I do not reconstruct it from incomplete shared ledgers.

The preceding Blanc-Renaudie run used `#1/#12/#27`. This run uses three different and previously unused-on-this-target moves: **#7 TAKE THE LIMIT, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE.**

---

## 2. What I attacked

The immediate target is Proposition 3.8 of the source. It constructs a modified cut relation `C_cut^r` and proves, assuming `(C)`, that for `r` large enough and then `chi(p)` large enough,

\[
\mathbb P_p^\otimes\big((\vec A_1,\vec A_2)\in C_{\rm cut}^r\big)<\frac14.
\tag{2.1}
\]

This estimate is the first place where the source's local-modification constants enter the Perron/mixing machinery. The published proof establishes the required smallness by dominated convergence and repeated `large enough` choices; it does not record an explicit rate.

The main result of this run is that this particular layer can be made explicit with **polynomial** dependence on `C`. The proof is not a new probabilistic mechanism: it is an exact re-indexing and quantitative completion of the source's own Lemmas 3.9--3.12. I do not claim priority for BK/tree-graph or discrete Riesz convolution estimates.

---

## 3. Method #18 — say the local modifications in convolution language

Write

\[
g_\alpha(x):=\langle x\rangle^{\alpha-d},\qquad
\langle x\rangle=\max(1,\|x\|_2),
\]

and in particular `g=g_2`. Under `(C)`, `tau_p <= C g` pointwise. Since `tau_p(0)=1`, every admissible `C` satisfies `C>=1`.

I will repeatedly use the following standard discrete Riesz estimate.

### Lemma 3.1 — discrete Riesz convolution bound

Let `alpha,beta>0` with `alpha+beta<d`. There is an effectively computable constant `K_{d,alpha,beta}` such that

\[
\sum_{y\in\mathbb Z^d}g_\alpha(y)g_\beta(x-y)
\le K_{d,\alpha,\beta}g_{\alpha+\beta}(x).
\tag{3.1}
\]

Moreover, for `alpha>0`,

\[
\sum_{\|x\|_2\le R}g_\alpha(x)\le K_{d,\alpha}\langle R\rangle^\alpha,
\tag{3.2}
\]

and if `alpha+beta<d` and `u` is bounded while `R` is at least a fixed multiple of `1+||u||`,

\[
\sum_{\|x\|_2>R}g_\alpha(x)g_\beta(x+u)
\le K'_{d,\alpha,\beta,u}R^{\alpha+\beta-d}.
\tag{3.3}
\]

#### Proof

For (3.1), take `R=||x||_2` and split the `y`-sum into `||y||<=R/2`, `||x-y||<=R/2`, and the complement. In the first region, `g_beta(x-y)=O(R^{beta-d})` while the `g_alpha` mass in the radius-`R/2` ball is `O(R^alpha)`; the second region is symmetric. In the complement, dyadically decompose into shells of radius `2^k R`; the contribution is

\[
O\!\left(R^{\alpha+\beta-d}\sum_{k\ge0}2^{k(\alpha+\beta-d)}\right),
\]

which converges because `alpha+beta<d`. The same shell count gives (3.2). Equation (3.3) follows from the same annular argument after using comparability of `||x||` and `||x+u||` outside a sufficiently large ball. Every constant can be replaced by the elementary cardinality bound for integer lattice shells, hence is computable. `square`

In our dimensions `d>6`, this gives

\[
g*g\le K_2 g_4,\qquad g*g*g\le K_3 g_6.
\tag{3.4}
\]

This is the useful language change: the source's apparently cluster-specific local-modification sums become ordinary two- and three-fold Riesz diagrams.

---

## 4. Method #25 — count the source's six error terms twice

I now follow the source's proof of Proposition 3.8, but instead of stopping at `finite` or `goes to zero`, re-index each sum to expose its exact convolution order. Constants below depend only on `(d,L)`; the active target has nearest-neighbor `L=1`. Replacing the source's mixture of `l1`, `l2`, and `l-infinity` balls changes only those fixed constants.

### 4.1 Lemma 3.9: marked head too close

The source writes

\[
\mathbb P_p^\otimes(\|a_i^+\|_\infty<3r)
=\frac1{\Omega\chi(p)}
\sum_{(A,\vec a)}\mathbb P_p(C(0)=A)
1_{\{a^-\in A,\ \|a^+\|_\infty<3r\}}.
\]

Dropping `a^- in A`, summing over `A`, and counting oriented edges with head in the box gives

\[
E_9(r)\le K_9\frac{r^d}{\chi(p)}.
\tag{4.1}
\]

For nearest-neighbor percolation one can take the exact pre-asymptotic count `(6 floor(r)+1)^d/chi(p)` up to the strict/non-strict boundary convention.

### 4.2 Lemma 3.10: middle-path collision

After BK and the cancellations of the two `Omega chi(p)` factors, the source reduces the bad event to

\[
\frac1\Omega
\sum_{w\notin B_{r-L}(0)}
\sum_{\vec a:\ \|-a^+-w\|_1\le9L}
\tau_p(a^-)\tau_p(w).
\tag{4.2}
\]

Under `(C)`, the head constraint places `a^-` within a bounded distance of `-w`. For `r` larger than a fixed multiple of `L sqrt(d)`, (3.3) therefore gives

\[
\boxed{E_{10}(r)\le K_{10}C^2 r^{4-d}.}
\tag{4.3}
\]

This makes the dominated-convergence step quantitative.

### 4.3 Lemma 3.11(a): a far vertex of the middle segment is hit by the other cluster

The source's BK/tree-graph reduction is

\[
E_{11,a}(r)
\le
\frac1\Omega
\sum_{z\notin B_r(0)}\sum_y\sum_{\delta\in\mathcal D_L}
\tau_p(z-y)\tau_p(y-\delta)\tau_p(z),
\tag{4.4}
\]

where `D_L` is the finite set of allowed edge displacements. Thus, by (3.4),

\[
E_{11,a}(r)
\le K C^3
\sum_{\|z\|>r}g_2(z)g_4(z+O_L(1))
\le
\boxed{K_{11,a}C^3r^{6-d}.}
\tag{4.5}
\]

This is the slowest genuine `r -> infinity` term. Its exponent is exactly where `d>6` enters.

### 4.4 Lemma 3.11(b): the translated head falls back into the radius-r repair box

The source's second case is bounded by

\[
\frac{C^2}{\Omega\chi(p)}
\sum_{z\notin B_r(0)}
\sum_{\vec a:\ \|z+a^+\|_1\le r}
 g_2(a^-)g_2(z).
\tag{4.6}
\]

Set `q=z+a^+`. Summing first over `z` turns the inner expression into a two-fold convolution evaluated at `q` plus a bounded edge displacement. Hence

\[
E_{11,b}(r)
\le \frac{KC^2}{\chi(p)}
\sum_{q\in B_r}g_4(q+O_L(1))
\le
\boxed{K_{11,b}\frac{C^2r^4}{\chi(p)}}.
\tag{4.7}
\]

### 4.5 Lemma 3.12(a): the terminal repair segment meets the other cluster

After the source's tree-graph inequality and its first `chi(p)` cancellation, the remaining sum has the form

\[
\frac{C^3}{\Omega^2\chi(p)}
\sum_{\vec a_2}\sum_y\sum_{z\in B_r(a_2^+)}
\sum_{\delta\in\mathcal D_L}
 g_2(z-y)g_2(y-\delta)g_2(a_2^-).
\tag{4.8}
\]

Write `z=a_2^+ + q`, `q in B_r`, and let `delta_2=a_2^+-a_2^-`. Counting the same tuples in the order `(q,delta,delta_2,a_2^-,y)` turns the two infinite sums into

\[
(g_2*g_2*g_2)(q+\delta_2-\delta).
\]

Therefore

\[
E_{12,a}(r)
\le \frac{KC^3}{\chi(p)}
\sum_{q\in B_r}g_6(q+O_L(1))
\le
\boxed{K_{12,a}\frac{C^3r^6}{\chi(p)}}.
\tag{4.9}
\]

### 4.6 Lemma 3.12(b): both translated heads lie in the same repair window

The source bounds this case by

\[
\frac{C^2}{\Omega^2\chi(p)^2}
\sum_z\sum_{\vec a_1,\vec a_2}
1_{\{\|z+a_1^+\|_1\le r\}}
1_{\{\|z-a_2^+\|_1\le r\}}
 g_2(a_1^-)g_2(a_2^-).
\tag{4.10}
\]

Put `q_1=z+a_1^+`, `q_2=z-a_2^+`. Summing over `z` first produces a two-fold convolution at `q_1-q_2` plus a bounded edge displacement. Thus

\[
E_{12,b}(r)
\le
\frac{KC^2}{\chi(p)^2}
\sum_{q_1,q_2\in B_r}g_4(q_1-q_2+O_L(1)).
\tag{4.11}
\]

For each `q_1`, (3.2) bounds the `q_2`-sum by `Kr^4`, and there are `O(r^d)` choices of `q_1`. Hence

\[
\boxed{E_{12,b}(r)\le K_{12,b}\frac{C^2r^{d+4}}{\chi(p)^2}.}
\tag{4.12}
\]

These are exactly the six pieces that the source treats qualitatively in Lemmas 3.9--3.12.

---

## 5. Method #7 — take the large-r limit and obtain an explicit polynomial threshold

The source's proof of Proposition 3.8 is a union bound over two copies of Lemma 3.9 and one copy each of Lemmas 3.10, 3.11, and 3.12. Combining (4.1)--(4.12) gives the following.

### Theorem 5.1 — polynomial quantitative form of source Proposition 3.8

Fix `d>6` and finite range `L`. There are effectively computable positive constants `r_0,K_1,...,K_6`, depending only on `(d,L)`, such that whenever `(C)` holds, `r>=r_0`, and `chi=chi(p)`,

\[
\boxed{
\begin{aligned}
\mathbb P_p^\otimes((\vec A_1,\vec A_2)\in C_{\rm cut}^r)
\le{}&K_1C^2r^{4-d}+K_2C^3r^{6-d}\\
&+\frac{K_3r^d+K_4C^2r^4+K_5C^3r^6}{\chi}\\
&+K_6\frac{C^2r^{d+4}}{\chi^2}.
\end{aligned}}
\tag{5.1}
\]

#### Proof

The first line is (4.3)+(4.5), the only two terms whose smallness is obtained by taking `r -> infinity`. The second line is the two Lemma 3.9 terms absorbed into `K_3`, plus (4.7)+(4.9). The last line is (4.12). The deterministic path construction in the source shows that the complement of these six failure events is contained in the complement of `C_cut^r`; hence their union bounds `P(C_cut^r)`. `square`

The structure of (5.1) is more useful than a huge numerical constant: it separates the true long-range errors from the finite-window/large-susceptibility errors. In particular, **the first local-modification step has only polynomial scale separation**.

### Corollary 5.2 — explicit polynomial-in-C susceptibility exponents for d=7,8,9,10

Since admissible `C>=1`, define

\[
\kappa_d:=\max\left\{\frac2{d-4},\frac3{d-6}\right\}.
\tag{5.2}
\]

Choose

\[
r=R_{d,L}C^{\kappa_d}
\tag{5.3}
\]

with `R_{d,L}` sufficiently large. Then the first line of (5.1) is below any fixed prescribed constant (in particular below the budget needed for Proposition 3.8), uniformly in `C>=1`.

For the remaining terms it is enough to require

\[
\chi(p)\ge H_{d,L}C^{q_d},
\tag{5.4}
\]

where

\[
q_d:=\left\lceil\max\left\{
 d\kappa_d,\ 2+4\kappa_d,\ 3+6\kappa_d,\ 1+\frac{d+4}{2}\kappa_d
\right\}\right\rceil.
\tag{5.5}
\]

For the four active dimensions,

\[
\boxed{
(\kappa_7,q_7)=(3,21),\quad
(\kappa_8,q_8)=(3/2,12),\quad
(\kappa_9,q_9)=(1,9),\quad
(\kappa_{10},q_{10})=(3/4,8).
}
\tag{5.6}
\]

Thus there are computable constants `R_d,H_d` such that source Proposition 3.8 is guaranteed once

\[
\begin{array}{c|c|c}
d&r\ \text{sufficient at scale}&\chi\ \text{sufficient at scale}\\ \hline
7& C^3&C^{21}\\
8& C^{3/2}&C^{12}\\
9& C&C^9\\
10&C^{3/4}&C^8
\end{array}
\tag{5.7}
\]

up to the dimension/range-dependent multiplicative constants.

#### Proof

After (5.3), the `C`-exponents in the two tail terms are

\[
2+\kappa_d(4-d)\le0,
\qquad
3+\kappa_d(6-d)\le0.
\]

The four susceptibility requirements obtained from the other terms are respectively

\[
C^{d\kappa_d},\quad
C^{2+4\kappa_d},\quad
C^{3+6\kappa_d},\quad
C^{1+(d+4)\kappa_d/2}.
\]

Taking the ceiling of their maximum gives (5.5). The exact fraction arithmetic producing (5.6) is archived in the run artifact. `square`

The executed exact checker reports

```
d=7  kappa=3    q=21
d=8  kappa=3/2  q=12
d=9  kappa=1    q=9
d=10 kappa=3/4  q=8
ALL_EXACT_EXPONENT_CHECKS_PASS
```

at

- `artifacts/R09/20260918T2234Z_blanc_localmod_exponents_c2a941.py`
- `artifacts/R09/20260918T2234Z_blanc_localmod_exponents_c2a941.out`.

---

## 6. What this changes, and what it does not

This does **not** certify any of `d=7,8,9,10`, so `M_A` does not move. It also does not make Blanc-Renaudie's entire hidden function `f_d(C)` polynomial: later quantitative ingredients, especially the full uniform-mixing theorem (Theorem 3.14), the high-frequency Fourier step (Theorem 3.24 / Proposition 3.25), and subsequent renormalization constants still have to be made explicit or replaced.

It does, however, remove one specific ambiguity in the bottleneck map. The source says its hidden constants are large mainly because of local modifications. For the **first** local-modification block, Proposition 3.8, the source proof itself can be reorganized so that:

1. every infinite cluster-shape sum disappears in favor of two- and three-fold two-point-function convolutions;
2. the only genuinely asymptotic spatial errors have rates `r^(4-d)` and `r^(6-d)`;
3. all remaining errors are polynomial in `r,C` divided by one or two powers of `chi`;
4. the resulting sufficient susceptibility threshold is polynomial in `C` in each of the four target dimensions.

That is a materially cheaper certificate than brute-force enumeration of the adaptive `|A|<=N` core from the previous run. The previous core remains useful as a completely finite fallback, but (5.1) shows that at least this source subroutine should be certified through two-point diagrams instead of cluster animals.

There is also a conceptual reason the source threshold is `d>6`: the slow term is the far three-Green-kernel diagram `g_2*g_2*g_2`, whose tail is `r^(6-d)`. At `d=6` this ceases to decay; for every `d>6` it does.

---

## 7. Prior-art / ownership / honesty notes

- The probabilistic inequalities being quantified are the source's own Lemmas 3.9--3.12 and Proposition 3.8.
- BK, the tree-graph inequality, and discrete Riesz convolution estimates are classical. I claim no novelty for those mechanisms.
- The contribution of this run is the explicit re-indexing, rate extraction, and polynomial threshold bookkeeping tailored to the source's finite-certification program.
- A fresh 2026-09-18 source/title/author/arXiv search found no later paper resolving `d=7,8,9,10`; because the source is essentially new, this is bounded negative evidence only.
- C0064 remains a different source statement (the Fourier infrared bound in every `d>6`) and is not declared solved or absorbed.
- No other owner was overridden; `operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md` remains the exclusive R09 claim.

---

## 8. Next research moves

The next run should not enumerate larger fixed cluster families. The natural next unused moves on this target are **#3 PROVE SOMETHING STRONGER, #21 ASK WHO ELSE HAS THIS SHAPE, #30 ONE SCALE / ONE DIRECTION AT A TIME**:

- **#3:** try to prove a single diagram inequality that simultaneously implies the direct-bridge mixing minorization and the source Fourier contraction, so that the two remaining expensive local-modification branches collapse to one condition on `tau`.
- **#21:** compare the required shift-smoothness / bridge minorization with quantitative local-CLT and random-walk Green-kernel criteria where explicit constants are standard, looking for a theorem that can be ported without source-specific cluster surgery.
- **#30:** localize the remaining quantitative chain to one scale `r`, one coordinate displacement, and one finite diagram at a time, then identify exactly which inequality first fails numerically in `d=7,8,9,10`.

If these do not change the metric or remaining obligation and the supported unchanged-run threshold is reached, apply the owner's stuck/retirement rule rather than manufacture another constant audit.

---

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R09
  target: BLANC-RENAUDIE-2026-MEANFIELD-7-10
  metric: M_A
  before: 0
  after: 0
  movement: false
  stagnation_count: UNKNOWN
  status: PARTIAL_OPEN
  methods_used: [7, 18, 25]
  new_result:
    - quantitative polynomial form of source Proposition 3.8
    - local-modification error budget reduced to Riesz two-point diagrams
    - sufficient C-exponents q_7=21, q_8=12, q_9=9, q_10=8 for this subroutine only
  exact_artifact:
    script: artifacts/R09/20260918T2234Z_blanc_localmod_exponents_c2a941.py
    output: artifacts/R09/20260918T2234Z_blanc_localmod_exponents_c2a941.out
    result: ALL_EXACT_EXPONENT_CHECKS_PASS
  source_scope_closed: false
  audits: 0
  next_methods: [3, 21, 30]
```

## 10. Model / scheduler-control status

The exposed task-control surface still has no binding model-family selector, no reasoning-effort selector, and no authenticated per-run model telemetry. Therefore `GPT-6 / maximum` remains prompt text only here; I do not claim it ran. The repository's latest reconciled deployment evidence also records that the historical P26 modification denial was later followed by a successful update from another authorized context, while R-series edits were denied from that P/C context. A real native-task denial must be handled from the owning authorized context, by an authorized ownership/admin transfer, or through platform support; permission bypass or duplicate-task creation is not a valid workaround.
