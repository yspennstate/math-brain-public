Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime does not expose authenticated completed-run effort telemetry, so I do not claim otherwise.

# P07-A — reciprocal variance and generator-orbit influence reduction

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `d704fd2e52a69f1ceb52fe0c2ec8fefa823e72c6`  
**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1008+0300__profiled_gibbs_flat_homotopy.md`, creation commit `4c358240ab500c3c1d47a89fa018b0a10803d7bd`.  
**Complementary checkpoint consulted:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1028+0300__bounded_transverse_interpolation.md`. P07-B owns the Fourier-dual / exceptional-frequency and bounded-interpolation route. The present report takes a different primal/concentration route.

**Outside target:** *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18; primary partial-result paper A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227 / SampTA 2025.  
**Source model:** odd `n`; `m=(n-1)/2` independent fair bits, one for each conjugate difference pair `{a,-a}`.  
**Source endpoint:**
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]
The primary paper still states the exact asymptotics as open and proves
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
A bounded current/later search on 20 September 2026 found the same source-matching status and no later proof of Conjecture 18. This is a bounded status check, not a worldwide-open certificate.

The fixed full-source metric therefore remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. The result below is an exact expectation/concentration reduction for the full odd-`n` source model; it is not a high-probability theta estimate and not an arbitrary-`n` improvement of the published upper bound by itself.

---

## 0. Preserved predecessor handoff: SRG69 remains OPEN / PARTIAL

The reassigned SRG69 track remains preserved under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve its exact no-Cayley result, rooted `L/B/C` system, centered spectral transfer, endpoint/cycle restrictions, block-moment / Gram reductions and star-complement handoff. Nothing in this report edits that root or claims the graph problem was solved.

---

# 1. New exact theorem: reciprocal symmetry turns the conjecture into a sublinear-variance problem

Let
\[
M=\{1,\ldots,(n-1)/2\}
\]
for odd `n`, let `D\subset M` be the random selected edge-pair set, and write
\[
T(D):=\vartheta(G_D),\qquad X(D):=\frac{T(D)}{\sqrt n}.
\]

Every circulant graph is vertex-transitive. Therefore Lovász's exact vertex-transitive identity gives
\[
T(D)\,T(D^c)=n.
\tag{1.1}
\]
For the fair source mask, `D` and `D^c` have the same law. Hence
\[
\boxed{X\stackrel d=X^{-1}.}
\tag{1.2}
\]

This elementary symmetry has a stronger consequence than the lower bound `E T >= sqrt(n)` used in the primary paper.

## Theorem P07-A.21 — reciprocal-variance bridge

For every odd `n` in the exact fair dense random-circulant model,
\[
\boxed{
0\le \frac{\mathbb E T}{\sqrt n}-1
\le \frac{\operatorname{Var}(T)}{2n}.
}
\tag{1.3}
\]
In particular,
\[
\boxed{
\operatorname{Var}(\vartheta(G_n))=o(n)
\quad\Longrightarrow\quad
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
}
\tag{1.4}
\]

### Proof

Put
\[
\mu:=\mathbb E X,
\qquad
\sigma^2:=\operatorname{Var}(X)=\frac{\operatorname{Var}(T)}n.
\]
By (1.2),
\[
\mathbb E X^{-1}=\mu,
\qquad
\operatorname{Var}(X^{-1})=\sigma^2.
\tag{1.5}
\]
Since `X X^{-1}=1` pointwise,
\[
1
=\mathbb E[XX^{-1}]
=\mu^2+\operatorname{Cov}(X,X^{-1}).
\tag{1.6}
\]
Cauchy-Schwarz and (1.5) imply
\[
\mu^2-1
=-\operatorname{Cov}(X,X^{-1})
\le \sigma^2.
\tag{1.7}
\]
Also `mu>=1`: by Cauchy-Schwarz,
\[
1=\mathbb E\sqrt{X X^{-1}}
\le \sqrt{\mathbb E X\,\mathbb E X^{-1}}=\mu.
\tag{1.8}
\]
Therefore
\[
0\le \mu-1
=\frac{\mu^2-1}{\mu+1}
\le\frac{\sigma^2}{\mu+1}
\le\frac{\sigma^2}{2}.
\tag{1.9}
\]
Substituting `sigma^2=Var(T)/n` proves (1.3). `square`

### Why this matters

The source conjecture does **not** require a pointwise `1+o(1)` theta certificate. It is enough to prove the much weaker-looking statement that theta has sublinear variance under the `(n-1)/2` independent generator-pair bits. This is an expectation-level reduction and uses the exact complement symmetry of the source; no unverified Fourier independence is introduced.

---

# 2. Exact Efron-Stein reduction to deletion energy of generator orbits

For `a\in M`, write
\[
D\triangle\{a\}
\]
for flipping the corresponding conjugate generator pair. Define the hypercube squared influence energy
\[
I_2(D)
:=\sum_{a\in M}
\bigl(T(D\triangle\{a\})-T(D)\bigr)^2.
\tag{2.1}
\]
Also define the one-sided **deletion energy**
\[
\boxed{
S_-(D)
:=\sum_{a\in D}
\bigl(T(D\setminus\{a\})-T(D)\bigr)^2.
}
\tag{2.2}
\]
The summands are nonnegative before squaring because deleting graph edges can only enlarge the theta primal feasible set.

## Proposition P07-A.22 — orbit-influence criterion

For the exact fair source model,
\[
\boxed{
\operatorname{Var}(T)
\le \frac14\,\mathbb E I_2(D)
=\frac12\,\mathbb E S_-(D).
}
\tag{2.3}
\]
Consequently,
\[
\boxed{
0\le\frac{\mathbb ET}{\sqrt n}-1
\le\frac{\mathbb E S_-(D)}{4n}.
}
\tag{2.4}
\]
Thus the theorem-sized missing implication is reduced to
\[
\boxed{
\mathbb E S_-(D)=o(n).
}
\tag{2.5}
\]

### Proof

Let `D^{(a)}` be obtained by independently resampling the fair bit at coordinate `a`, with all other bits fixed. Efron-Stein gives
\[
\operatorname{Var}(T)
\le\frac12\sum_{a\in M}
\mathbb E\bigl(T(D)-T(D^{(a)})\bigr)^2.
\tag{2.6}
\]
Conditional on all coordinates other than `a`, the resampled bit differs from the original bit with probability `1/2`; if it differs, the squared difference is exactly the squared flip difference across that hypercube edge. Therefore
\[
\mathbb E\bigl(T(D)-T(D^{(a)})\bigr)^2
=\frac12\,\mathbb E
\bigl(T(D\triangle\{a\})-T(D)\bigr)^2.
\tag{2.7}
\]
Substitution into (2.6) gives the first inequality in (2.3).

For a fixed coordinate `a`, the squared flip difference is the same from the `a=0` and `a=1` endpoints. Under the fair mask, the one-sided deletion energy counts that edge exactly on the `a=1` endpoint, hence with probability `1/2`. Summing over `a`,
\[
\mathbb E I_2(D)=2\,\mathbb E S_-(D).
\tag{2.8}
\]
Combining (1.3), (2.3) and (2.8) proves (2.4). `square`

---

# 3. A surprisingly weak self-bounding estimate would already close Conjecture 18

The published expectation upper bound is
\[
\mathbb ET=O\!\left(\sqrt{n\log\log n}\right)=o(n).
\tag{3.1}
\]
Therefore it would be enough to prove any source-valid estimate of the form
\[
\boxed{
\mathbb E S_-(D)\le C\,\mathbb E T(D)
}
\tag{3.2}
\]
with an absolute constant `C`; indeed (2.4) and (3.1) would yield
\[
0\le\frac{\mathbb ET}{\sqrt n}-1
=O\!\left(\sqrt{\frac{\log\log n}{n}}\right)=o(1).
\tag{3.3}
\]

A complement-symmetric variant is equally sufficient:
\[
\boxed{
\mathbb E S_-(D)
\le C\,\mathbb E\left(T(D)+\frac n{T(D)}\right).
}
\tag{3.4}
\]
Indeed `n/T(D)=T(D^c)` pointwise and `D^c` has the same law, so the right-hand side of (3.4) equals `2C E T=o(n)`.

This is a considerably more concrete primal target than controlling every sparse Fourier vector or proving a full pathwise covariance lower bound. It asks only for **average squared sensitivity of the optimum to deleting one random generator orbit**.

---

# 4. Exact first-order influence identity for the biased model

For orientation, let `D_q` be the same pair model with each generator pair selected independently with probability `q`, and define
\[
\mu(q):=\mathbb E_q T(D_q).
\]
For a configuration of the other coordinates let
\[
\Delta_a:=T(D^{a=0})-T(D^{a=1})\ge0.
\]
The standard product-measure differentiation identity gives
\[
\boxed{
-\mu'(q)=\sum_{a\in M}\mathbb E_q\Delta_a.
}
\tag{4.1}
\]
At `q=1/2`, if
\[
S_1^-(D):=\sum_{a\in D}\bigl(T(D\setminus\{a\})-T(D)\bigr),
\]
then
\[
\boxed{
\mathbb E S_1^-(D)=-\frac12\mu'(1/2).
}
\tag{4.2}
\]
This does not by itself control the square energy `S_-`; it records exactly what a successful self-bounding argument must add beyond Russo-type first-order sensitivity.

Complementation also gives the exact biased relation
\[
T(D^c)=\frac n{T(D)},
\qquad
D_q^c\stackrel d=D_{1-q},
\tag{4.3}
\]
which can be used to keep any future sensitivity estimate self-dual around `q=1/2`.

---

# 5. What has and has not been proved

**Proved in this run:**

1. exact reciprocal-distribution identity `T/sqrt(n) d= sqrt(n)/T` for the source ensemble;
2. exact variance-to-mean-gap inequality (1.3);
3. exact Efron-Stein generator-orbit reduction (2.3)--(2.4);
4. the source conjecture follows from the single quantitative condition `E S_-=o(n)`;
5. even the stronger-looking but very usable self-bounding estimate `E S_- = O(E T)` would close Conjecture 18 immediately using the already-published bound.

**Not proved:** `E S_-=o(n)`, (3.2), or (3.4). Therefore this is **PROVED PARTIAL**, not a candidate full proof.

The theorem is expectation-level. No claim is made that `T=(1+o(1))sqrt(n)` with high probability. No finite numerical theta computation is used. The odd-`n` parity and exact pair-bit source model are preserved. The Fourier normalization of the canonical work is untouched because this reduction needs no renormalized transform.

---

# 6. Separation from P07-B and exact lemma handoff

P07-B's newest report reduces its dual route to bounded interpolation of the radial Gibbs residual, with missing lemma `TRBI(beta,C)`. This report does not attempt that interpolation or its exceptional-frequency analysis.

The exact lemma exported from P07-A is instead:

> **Orbit-energy lemma sufficient for the source conjecture.** If, in the fair odd-`n` dense random circulant model,
> \[
> \mathbb E\sum_{a\in D}
> [\vartheta(G_{D\setminus\{a\}})-\vartheta(G_D)]^2=o(n),
> \]
> then Conjecture 18 follows.

This is a complementary primal/concentration target. P07-B can use the lemma if its dual certificates happen to imply stability, but ownership of `TRBI` remains with P07-B.

---

# 7. Next attack

The next P07-A iteration should attack the deletion energy directly from the cyclically averaged theta LP/SDP. For each `a\in D`, deleting the generator pair relaxes exactly one conjugate orbit constraint. The goal is to relate the resulting squared value increment to the mass/shadow-price carried by that orbit in an optimal primal/dual pair and then sum over `a`.

The preferred theorem target is the self-dual estimate
\[
\boxed{
S_-(D)\ \lesssim\ T(D)+\frac n{T(D)}
}
\tag{7.1}
\]
either deterministically on a broad dense class or in source expectation with an `o(n)` exceptional contribution. By (2.4), complement invariance, and the inherited `O(sqrt(n log log n))` expectation bound, such an estimate would finish Conjecture 18.

If (7.1) is false, the next useful output is not another reformulation: identify an explicit mask family with large deletion energy and isolate the structural feature absent from a fair random mask, then prove that feature is rare. A second primal fallback is the positive Riesz-product fixed-point family, but it should be used only if the sensitivity route fails rather than duplicating P07-B's Fourier-dual work.

---

## Source/current check (20 September 2026)

- Randomstrasse101: arXiv:2603.29571, Conjecture 18 retains the endpoint `E theta(G)=(1+o(1)) sqrt(n)` for dense random circulants.
- Primary partial-result paper: https://arxiv.org/abs/2502.16227 . Its current abstract/text still says exact behavior remains open and proves the expectation bounds `sqrt(n) <= E theta <= C sqrt(n log log n)`.
- The primary source explicitly defines the odd-`n` model using `(n-1)/2` independent pair bits and notes that its RIP upper-bound argument omits positivity.
- A bounded later/source-matching search in this run found no later proof of the sharp constant. No worldwide-open or novelty certificate is claimed.

## Ledger delta

- role: `P07-A`
- native_id: `6aa7b46f70a8819184095c277974c256`
- target: Randomstrasse101 Conjecture 18 / dense random-circulant Lovász theta
- inherited full metric: `alpha_LL=1/2`
- after: `alpha_LL=1/2` (**no headline exponent movement**)
- new obligation: prove `E S_-(D)=o(n)`; sufficient stronger target `E S_-(D)=O(E theta(G_D))`
- status: `OPEN / PROVED PARTIAL`
- SRG69: preserved `OPEN / PARTIAL`, `R_SRG69=1`, historical root untouched
