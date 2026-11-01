# C0031 — separable bounded-profile invertibility and two exact obstructions to the naive smoothing route

Date: 2026-09-19 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Canonical target: `C0031`, Bordenave–Chafaï heavy-tailed circular-law almost-sure upgrade  
Methods: **B4 / B20 / B28**  
Start-of-run master: `5d7b0066e93077ddbe249cfc2a9a217a632b64c4`  
Fresh pre-write master: `eee9de63878addea36144fe484444bf066cb2168`

## 1. Cumulative starting point

The fixed source metric is `BC_AS`: it equals `1` only if the full Bordenave–Chafaï no-density almost-sure endpoint is proved, and `0` otherwise. It enters this run at `0` after five ordinary no-movement research runs on C0031.

The preceding run proved two facts that materially narrow the remaining hard edge.

First, if the heavy-tailed entry law admits an independent finite-variance smoothing component, `xi=H+sigma Z`, then conditioning on `H` reduces the square hard edge to the shifted-iid invertibility theorem, yielding a polynomial least-singular-value floor for Lebesgue-a.e. complex shift and hence the full almost-sure heavy-tailed limit for that restricted no-density subclass.

Second, the symmetric discrete-Pareto benchmark has an exact fair edge-flow decomposition

`2 xi = Z + K epsilon`,

where `epsilon` is an independent fair Rademacher sign and `K in {1,2}`. Entrywise, after conditioning on the latent edge variables,

`2(X_n-a_n z I)=D_n(z)+K_n circ E_n`,

with iid fair signs `E_n`, a bounded amplitude profile `K_n in {1,2}^{n x n}`, and a deterministic conditional core `D_n(z)` of polynomial norm outside a summable event. Thus the benchmark would close if one had an arbitrarily high polynomial-confidence least-singular-value theorem for polynomial deterministic cores and such bounded non-iid amplitude profiles.

This run asks three different questions: which non-iid profiles are already reducible to the iid theorem; why the most obvious algorithm for extracting iid noise actually fails; and whether a typical random `{1,2}` profile contains a large iid constant-amplitude core.

## 2. B4 — prove something weaker completely: all separable bounded profiles reduce exactly to iid noise

### Theorem 1 (high-confidence invertibility for bounded separable profiles)

Let `E_n=(epsilon_ij)` have iid centered unit-variance entries from a fixed law for which the Tao–Vu/Jain shifted-iid theorem applies; in particular iid Rademacher signs are allowed. Let

`A_ij = r_i c_j`

with deterministic complex scalars satisfying

`0 < a <= |r_i|, |c_j| <= b < infinity`

uniformly in `i,j,n`. Let `D_n` be any deterministic complex `n x n` matrix with

`||D_n|| <= n^C`.

Then for every desired failure exponent `L>0` there exists a finite exponent `B=B(C,L,a,b,law(E_11))` such that

`P( s_min(D_n + A circ E_n) <= n^{-B} ) <= n^{-L}`

for all sufficiently large `n`.

### Proof

Put

`R=diag(r_1,...,r_n)`, `C0=diag(c_1,...,c_n)`.

Since `A_ij=r_i c_j`, one has the exact factorization

`A circ E_n = R E_n C0`.

Therefore

`D_n + A circ E_n
 = R [ R^{-1} D_n C0^{-1} + E_n ] C0`.

The diagonal factors obey

`s_min(R) >= a`, `s_min(C0) >= a`,

and the transformed deterministic core obeys

`||R^{-1}D_n C0^{-1}|| <= a^{-2} n^C`.

The shifted-iid quantitative invertibility theorem applied to

`E_n + R^{-1}D_n C0^{-1}`

gives, for every `L>0`, a finite `B0` such that

`P( s_min(E_n + R^{-1}D_n C0^{-1}) <= n^{-B0}) <= n^{-L}`.

Finally, for arbitrary square matrices `P,Q,M`,

`s_min(PMQ) >= s_min(P) s_min(M) s_min(Q)`.

Hence

`s_min(D_n + A circ E_n)
 >= a^2 s_min(E_n + R^{-1}D_n C0^{-1})`.

Absorbing the fixed `a^2` into the polynomial exponent proves the claim. QED.

### Corollary 2

The preceding discrete-Pareto hard-edge reduction would be complete if its conditional amplitude matrix `K_n` were separable with uniformly bounded row/column factors. In particular constant, row-constant, column-constant, and more generally rank-one multiplicative amplitude profiles are not a genuine obstruction.

This isolates the difficulty much more sharply: it is not non-identical variance by itself, but non-separable entrywise modulation.

## 3. B20 — find why the obvious algorithm fails

There are two tempting algorithms.

### 3.1 Algorithm A: extract one independent iid Rademacher component from every discrete-Pareto entry

The independent-smoothing theorem from the preceding run would immediately finish the discrete-Pareto benchmark if one could write

`xi = Y + epsilon`

with `epsilon` an independent fair unit Rademacher and `Y` arbitrary. This exact decomposition is impossible.

### Proposition 3 (no independent unit-Rademacher convolution factor)

Let `xi` be any integer-valued random variable satisfying

- `P(xi=0)=0`,
- `P(xi=2)=p_2>0`,
- `P(xi=4)=p_4`, with `p_4<p_2`.

Then there do not exist independent random variables `Y` and a fair `epsilon in {-1,+1}` such that

`xi=Y+epsilon`.

In particular this applies to the symmetric discrete-Pareto law `P(xi=+/- k)=c_alpha k^{-1-alpha}`.

#### Proof

Let `q_j=P(Y=j)`. Since

`0=P(xi=0)=(q_{-1}+q_1)/2`,

nonnegativity gives

`q_{-1}=q_1=0`.

Next

`p_2=P(xi=2)=(q_1+q_3)/2=q_3/2`,

so `q_3=2p_2`. But

`p_4=P(xi=4)=(q_3+q_5)/2`,

so

`q_5=2p_4-q_3=2(p_4-p_2)<0`,

contradicting `q_5>=0`. QED.

Thus the state-dependent amplitude `K in {1,2}` in the exact fair edge-flow representation is not merely a poor choice of decomposition that can be replaced by the simplest constant-amplitude iid smoothing factor.

### 3.2 Algorithm B: run the iid high-confidence proof row-by-row anyway

For a fixed deterministic vector `x`, each row sum

`sum_j k_ij epsilon_ij x_j`

is still a standard weighted Rademacher Littlewood–Offord object. Elementary forward anti-concentration therefore survives the profile `K`.

The obstruction appears in the inverse/counting step. The high-confidence iid arguments exploit that every row tests the same coefficient structure `x` against the same entry law. With a row-dependent profile, row `i` tests instead the row-dependent coefficient vector

`K_i circ x`.

A vector that is arithmetically structured after one row modulation need not have the same arithmetic description after another. A naive proof that assigns a separate inverse-Littlewood–Offord certificate to every possible row profile would face up to `2^n` possible `{1,2}` row modulations before even counting candidate vectors. That destroys the common low-complexity object that the iid counting theorem exploits.

Theorem 1 explains exactly when this obstruction disappears: if `K_ij=r_i c_j`, then every modulation is globally conjugate to the same iid problem through two diagonal matrices, so no row-specific arithmetic classification is needed.

This is a structural diagnosis rather than a theorem that the general bounded-profile result is false. It identifies what a successful extension must replace: one needs a **profile-stable arithmetic complexity/counting object**, not merely another one-row small-ball estimate.

## 4. B28 — replace `for all profiles` by `for a typical profile`

In the fair edge-flow decomposition, before conditioning the latent edge variables are iid across entries. Thus the amplitude matrix `K_n` is an iid two-valued random profile. Let

`P(K_ij=1)=p`, `P(K_ij=2)=1-p`,

with `0<p<1`, and put `p_* = max(p,1-p)<1`.

It is natural to ask whether typicality lets us extract a large constant-amplitude square block and fall back on the shifted-iid theorem. The answer is no at any macroscopic scale.

### Proposition 4 (largest constant-amplitude square is logarithmic)

For every constant

`C > 2/|log p_*|`,

with probability one, for all sufficiently large `n`, the iid profile `K_n` contains no constant-amplitude `k x k` submatrix with

`k >= C log n`.

#### Proof

For fixed row and column sets `I,J` of cardinality `k`, the probability that `K_{I,J}` is all `1` or all `2` is

`p^{k^2}+(1-p)^{k^2} <= 2 p_*^{k^2}`.

There are at most `binom(n,k)^2` such pairs `(I,J)`. Hence

`P(exists constant k x k block)
 <= 2 binom(n,k)^2 p_*^{k^2}
 <= 2 exp( 2k log(en/k) + k^2 log p_* ).`

Set `k=ceil(C log n)`. The coefficient of `(log n)^2` in the exponent is

`2C + C^2 log p_*`,

which is negative precisely when `C>2/|log p_*|`. Therefore the bound is `exp(-c (log n)^2)` for some `c>0`, hence summable. Borel–Cantelli proves the assertion. QED.

So a typical edge-flow profile does **not** hide a linear-sized or even polynomial-sized monochromatic square on which one can simply invoke the iid theorem. The biggest such square is only logarithmic in `n` up to constants.

### Proposition 5 (typical profiles are nevertheless globally balanced)

Fix `delta>0`. There is `c=c(delta,p)>0` such that, with probability at least `1-exp(-c n^2)` for large `n`, every pair of index sets `I,J subset [n]` with `|I|,|J|>=delta n` has its proportion of `K_ij=1` entries within `delta` of `p` after adjusting the numerical constant in the deviation.

#### Proof

For each fixed `I,J`, the number of `1` entries is binomial with `|I||J|>=delta^2 n^2` trials. Hoeffding/Chernoff gives `exp(-c_0 n^2)` failure for a fixed pair. There are at most `4^n=exp(O(n))` pairs of subsets. A union bound leaves `exp(-c n^2)`. QED.

Thus the conditional amplitude profile is typically maximally dense and quasirandom at every macroscopic scale. The remaining confidence loss in the known structured-matrix theorem is therefore not plausibly attributable to a rare macroscopic sparsity defect of this particular profile.

## 5. Consequence for the discrete-Pareto benchmark

The benchmark has now been reduced to a very specific missing theorem.

> **Typical bounded-profile hard-edge problem.** Let `K_n` be an iid `{1,2}` profile generated jointly with a polynomial-norm core `D_n` by the fair edge-flow latent variables, and condition on the full latent profile. Prove a summable lower-tail estimate, at any inverse-polynomial threshold, for
>
> `s_min(D_n + K_n circ E_n)`,
>
> where `E_n` is iid fair Rademacher and independent of the latent variables.

Theorem 1 settles every bounded separable profile. Proposition 4 rules out the simplest attempt to find a large constant-amplitude iid submatrix in a typical non-separable profile. Proposition 3 rules out the simplest independent constant-amplitude convolution factor at the scalar-law level. What is missing is an inverse/counting theorem robust under a genuinely entrywise random modulation, or an argument that exploits the joint law of `(D_n,K_n)` before conditioning.

## 6. Literature boundary checked on 2026-09-19

- Bordenave–Chafaï, *Around the circular law*, arXiv:1109.3343 / Probability Surveys 9 (2012), remains the source. Its heavy-tail discussion gives weak smallest-singular-value control under weak assumptions; the cumulative target is the source's general no-density almost-sure endpoint.
- Vishesh Jain, *Quantitative invertibility of random matrices: a combinatorial perspective*, arXiv:1908.11255 / Discrete Analysis 2021, treats `M+N` with arbitrary deterministic complex `M` and `N` whose entries are independent copies of one common centered unit-variance law, obtaining extremely high probability bounds. This is exactly the iid input used in Theorem 1 after diagonal conjugation.
- Nicholas Cook, *Lower bounds for the smallest singular value of structured random matrices*, arXiv:1608.07347 / Ann. Probab. 46 (2018), treats `A circ X+B` with a deterministic variance profile and iid base entries. It confirms that non-identical profiles are a natural setting, but its general structured hypotheses/results do not supply the all-purpose arbitrarily-high-polynomial-confidence theorem for an arbitrary polynomial-norm core needed by the conditional discrete-Pareto reduction.

A bounded fresh search found no later theorem that directly supplies the exact missing combination: arbitrary polynomial-size deterministic core, dense bounded non-separable Bernoulli amplitude profile, square matrix, and summable/high-polynomial-confidence hard-edge control. This is negative evidence only, not a novelty or openness certificate.

## 7. Metric and retirement consequence

Frozen source metric: `BC_AS`.

Before: `0`.

After: `0` (**NO MOVEMENT**).

This is the sixth ordinary source-metric-unchanged C0031 research run. Under the owner protocol for a CLOSABLE target, C0031 must therefore be retired from this worker after preserving an immutable handoff. The restricted theorems above remain valid cumulative progress, but they do not close the full Bordenave–Chafaï source endpoint and are not relabeled as closure.

Status: **PARTIAL / SOURCE OPEN / R7-05 RESEARCH RETIRED AFTER SIX UNCHANGED RUNS**.
