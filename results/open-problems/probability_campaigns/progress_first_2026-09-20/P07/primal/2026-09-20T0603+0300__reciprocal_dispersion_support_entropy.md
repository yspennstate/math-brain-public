Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime does not expose authenticated completed-run effort telemetry, so I do not claim otherwise.

# P07-A — reciprocal dispersion and a positive-Fourier support/entropy pivot

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `55c33878f7188489e5df4c2211c9ebe992952475`  
**Previous own report:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0445+0300__critical_householder_orthant.md`, blob `eb3512758485899c244f7ce4b4d2fc37307dd8c8` on current master.  
**Complementary checkpoint read:** P07-B `2026-09-20T0512+0300__damped_schur_threshold_count.md`. P07-B continues to own Fourier-dual exceptional-frequency / Schur-repair work; nothing below duplicates that route.  
**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, *The Lovasz number of random circulant graphs*, arXiv:2502.16227 / SampTA 2025.  
**Exact source endpoint:** for the source dense random circulant ensemble,
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]

**Inherited rigorous source bound:**
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
The frozen full-source metric is therefore still
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No improvement of the published iterated-log exponent is claimed in this run. The progress is a materially different structural reduction after three unchanged P07-A iterations: an exact reciprocal-dispersion identity for the expectation gap, an exact upper-tail integral formula, and a new positive-Fourier support/entropy formulation with a matching-order Fejer obstruction showing what this route must and must not try to prove.

The archived SRG69 line remains **OPEN / PARTIAL** under its historical root; no SRG69 file or claim is edited here.

## Current-source continuity check — 20 September 2026

The current Randomstrasse101 page still states Conjecture 18 as `E theta(G)=(1+o(1))sqrt(n)`. The current primary-paper abstract / published SampTA record still says the exact behavior is open and gives square-root scaling only up to a `log log` factor. A bounded fresh search for the exact title, Conjecture 18, and later random-circulant theta work found no later sharp-asymptotic proof. This is bounded continuity evidence, not a worldwide novelty certificate.

---

# 1. Fresh pivot forced by three unchanged runs: use complement symmetry before another cone estimate

Every circulant graph is vertex-transitive. Lovasz's vertex-transitive identity gives, for every realization,
\[
\vartheta(G)\vartheta(\bar G)=n.
\tag{1.1}
\]
In the source model each nonzero conjugate frequency pair is selected independently with probability `1/2`, so complementing the graph is exactly complementing all those fair bits. Hence
\[
G\stackrel d=\bar G.
\tag{1.2}
\]
Define the normalized random variable
\[
X_n:=\frac{\vartheta(G_n)}{\sqrt n}.
\tag{1.3}
\]
Then (1.1)-(1.2) imply the exact distributional reciprocity
\[
\boxed{X_n\stackrel d=X_n^{-1}.}
\tag{1.4}
\]
This simple identity changes the correct primal target: the conjecture is not merely an upper-tail problem; it is a **reciprocal concentration** problem around the unique fixed point `1`.

## Theorem P07-A.8 — exact reciprocal-dispersion identity

For every source-admissible odd `n`,
\[
\boxed{
\frac{\mathbb E\vartheta(G_n)}{\sqrt n}-1
=\frac12\,\mathbb E\!\left[\frac{(X_n-1)^2}{X_n}\right].
}
\tag{1.5}
\]
Equivalently, if `Y_n=log X_n`, then `Y_n` has a symmetric distribution and
\[
\boxed{
\frac{\mathbb E\vartheta(G_n)}{\sqrt n}
=\mathbb E\cosh(Y_n).
}
\tag{1.6}
\]

### Proof

From (1.4), `E X_n=E X_n^{-1}`. Therefore
\[
\mathbb E\frac{(X_n-1)^2}{X_n}
=\mathbb E(X_n+X_n^{-1}-2)
=2(\mathbb E X_n-1),
\]
which is (1.5). Taking logarithms in (1.4) gives `Y_n d= -Y_n`; hence
\[
\mathbb E X_n=\mathbb E e^{Y_n}=\mathbb E\cosh(Y_n),
\]
giving (1.6). All moments here are finite because `1<=theta(G)<=n`. ∎

### Consequences

1. The standard lower bound `E theta(G)>=sqrt(n)` is immediate from the nonnegative right side of (1.5).
2. The sharp constant conjecture is **exactly equivalent** to
   \[
   \mathbb E\!\left[\frac{(X_n-1)^2}{X_n}\right]\to0.
   \tag{1.7}
   \]
   Thus a constant-factor `O(sqrt(n))` theorem alone cannot establish the leading constant; one needs reciprocal dispersion to vanish.
3. For every `c>1`, reciprocity gives
   \[
   \Pr\{X_n\ge c\}=\Pr\{X_n\le c^{-1}\}.
   \tag{1.8}
   \]
   The two sides of the critical value are therefore not separate phenomena.

---

# 2. Exact expectation-gap formula using only the upper tail

The previous P07-A report used the sufficient target
\[
\Pr\{X_n\ge1+\varepsilon\}=o(n^{-1/2})
\tag{2.1}
\]
for each fixed `epsilon>0`, because the crude bound `theta<=n` then controls the expectation. That target is valid but substantially stronger than necessary.

## Theorem P07-A.9 — reciprocal upper-tail integral

For every source-admissible `n`,
\[
\boxed{
\frac{\mathbb E\vartheta(G_n)}{\sqrt n}-1
=\int_1^{\sqrt n}(1-c^{-2})\,\Pr\{X_n>c\}\,dc.
}
\tag{2.2}
\]
(Changing strict to weak inequalities changes only atom conventions and not the integral.)

### Proof

Let `Y=|log X_n|`. Since `X_n in [n^{-1/2},n^{1/2}]`, we have `0<=Y<=L=(1/2)log n`. By (1.6),
\[
\mathbb E X_n-1
=\mathbb E(\cosh Y-1)
=\int_0^L \sinh u\,\Pr\{Y>u\}\,du.
\tag{2.3}
\]
The symmetry of `log X_n` gives
\[
\Pr\{Y>u\}=2\Pr\{X_n>e^u\}.
\tag{2.4}
\]
Set `c=e^u`; then `du=dc/c` and
\[
2\sinh u\,du
=(c-c^{-1})\frac{dc}{c}
=(1-c^{-2})dc.
\]
Substitution in (2.3) yields (2.2). ∎

### Why this matters

The source conjecture is therefore equivalent to the integrated statement
\[
\boxed{
\int_1^{\sqrt n}(1-c^{-2})\Pr\{\vartheta(G_n)>c\sqrt n\}\,dc=o(1).
}
\tag{2.5}
\]
This is a strictly better-calibrated target for P07-A than asking for the uniform `o(n^{-1/2})` fixed-`epsilon` tail (2.1). For example, one may choose any `delta_n downarrow0`; the interval `[1,1+delta_n]` contributes at most `delta_n`, and it is enough to control the weighted tail beyond `1+delta_n` in aggregate. This gives room for a multiscale argument whose probability bound degrades as `c downarrow1`.

This reduction is primal/structural and does not overlap P07-B's exceptional-frequency completion machinery.

---

# 3. A fixed positive witness is exponentially unlikely to survive the random mask

I now change language from the orthant coordinates back to the exact source **frequency-domain primal LP**, because positivity itself gives a deterministic support barrier.

The source LP may be written
\[
\vartheta(G_E)=n\max y_0
\tag{3.1}
\]
subject to
\[
y\ge0,\qquad \sum_{j\in\mathbb Z_n}y_j=1,
\qquad \widehat y(k)=0\quad(k\in E),
\tag{3.2}
\]
with the source's real symmetry. Put
\[
h=ny,
\qquad
c_k:=\frac1n\sum_{j\in\mathbb Z_n}h_j\omega^{-kj}.
\tag{3.3}
\]
Then `h>=0`, `(1/n)sum h=1`, so `c_0=1`, and
\[
|c_k|\le1
\tag{3.4}
\]
for every `k` simply by the triangle inequality against the probability measure `h/n`.

## Lemma P07-A.10 — deterministic positive-Fourier support barrier

If `h(0)>=t` and `h` is real, nonnegative, and has mean `1`, then
\[
\boxed{|\operatorname{supp}\widehat h|\ge t.}
\tag{3.5}
\]
If `s(h)` is the number of **nonzero conjugate frequency pairs** on which `c_k` is nonzero, then
\[
\boxed{s(h)\ge\frac{t-1}{2}.}
\tag{3.6}
\]

### Proof

Fourier inversion at zero gives
\[
h(0)=\sum_{k\in\mathbb Z_n}c_k.
\]
Using (3.4),
\[
t\le h(0)\le\sum_{k\in\operatorname{supp}\widehat h}|c_k|
\le|\operatorname{supp}\widehat h|.
\]
For real `h`, nonzero support occurs in conjugate pairs and includes `0`, giving (3.6). ∎

For a **fixed** candidate witness `h` with exactly `s` nonzero conjugate Fourier pairs, source feasibility requires that none of these pairs be chosen into the random edge mask `E`. The pair bits are independent fair bits, hence
\[
\boxed{
\Pr\{\text{this fixed }h\text{ survives the source mask}\}=2^{-s}
\le2^{-(t-1)/2}.
}
\tag{3.7}
\]
At `t=c sqrt(n)` this is `exp(-Omega(sqrt(n)))` for every fixed witness.

The problem is therefore not survival of one candidate. It is **entropy of the family of positive candidates**.

---

# 4. Exact support-entropy reduction

Let `m=(n-1)/2` be the number of nonzero conjugate frequency pairs. For a threshold `t`, define `A_n(t,s)` to be the collection of pair-support sets `S subset {1,...,m}` with `|S|=s` for which there exists a real nonnegative mean-one function `h` satisfying
\[
h(0)\ge t,
\qquad
\operatorname{supp}\widehat h\setminus\{0\}\subseteq\pm S.
\tag{4.1}
\]
Let `N_n(t,s)=|A_n(t,s)|`.

Every primal feasible witness at level `t` has an exact nonzero pair support `S` contained in the random complement of `E`. Taking a union bound over exact supports gives
\[
\boxed{
\Pr\{\vartheta(G_E)\ge t\}
\le
\sum_{s\ge (t-1)/2}N_n(t,s)2^{-s}.
}
\tag{4.2}
\]
This is not yet a useful numerical bound: the crude replacement `N_n(t,s)<=binom(m,s)` is far too large around `s~sqrt(n)`. But (4.2) isolates a concrete **primal sign-entropy problem** which is absent from the RIP proof:

> quantify how many Fourier support patterns can carry a nonnegative mean-one function with a prescribed `sqrt(n)`-scale spike.

If one can prove a weighted estimate strong enough that, uniformly for `t=c sqrt(n)` outside a shrinking critical window,
\[
\sum_s N_n(t,s)2^{-s}
\tag{4.3}
\]
has an integrable `c`-tail in the sense of (2.5), then Conjecture 18 follows. No generic all-sign RIP estimate is required.

I emphasize the limitation: (4.2) is a reduction, not a source-level upper bound yet. In particular, the prior prime positive-circuit theorem shows that extremizers can have large allowed Fourier support, so a low-support count by itself cannot finish the problem.

---

# 5. Why a deterministic linear-support theorem cannot be the missing argument

One might hope to strengthen (3.6) all the way to `s(h)>=c n` for every positive `sqrt(n)`-spike. That is false even deterministically.

For an integer `q` with `2q-1<n`, define the cyclic Fejer kernel
\[
H_q(j)=\frac1q\left|\sum_{\ell=0}^{q-1}\omega^{\ell j}\right|^2.
\tag{5.1}
\]
Then
\[
H_q(j)\ge0,
\qquad
\frac1n\sum_jH_q(j)=1,
\qquad
H_q(0)=q.
\tag{5.2}
\]
Expanding the square gives
\[
\widehat H_q(d)=
\begin{cases}
1-|d|/q,& |d|<q,\\
0,&\text{otherwise},
\end{cases}
\tag{5.3}
\]
with no wraparound because `2q-1<n`. Hence exactly `q-1` nonzero conjugate frequency pairs occur.

Taking `q~sqrt(n)` gives a nonnegative mean-one function of height `~sqrt(n)` with only `O(sqrt(n))` active Fourier pairs. Therefore:

\[
\boxed{
\text{positivity plus a }\sqrt n\text{-spike does not deterministically force }\Omega(n)\text{ Fourier support.}
}
\tag{5.4}
\]

This is a useful obstruction to an overly optimistic version of the paper's positive-kernel heuristic. The correct theorem must use **random-mask avoidance plus structural entropy**, not a deterministic linear-support claim.

At the same time the most obvious structured near-extremizers are themselves harmless. If `n` is prime, dilating `H_q(j)` by a nonzero frequency multiplier gives at most `(n-1)/2` distinct symmetric arithmetic-progression pair supports. Each contains `q-1` nonzero pair frequencies, so
\[
\Pr\{\text{some dilated Fejer support is entirely available}\}
\le\frac{n-1}{2}\,2^{-(q-1)}.
\tag{5.5}
\]
For `q~c sqrt(n)`, this is `exp(-Omega(sqrt(n)))`. Thus the elementary structured family does not explain a constant larger than one; any obstruction must come from a vastly richer family of positive supports/circuits.

I do **not** claim the Fejer observation is externally novel. Its purpose here is to determine the correct scale and to rule out a false route before spending more runs on it.

---

# 6. What changed mathematically

The headline source metric did not move, but the proof target did:

- **Before:** a sufficient but very strong target was `P(theta>(1+epsilon)sqrt(n))=o(n^-1/2)` for every fixed epsilon.
- **Now:** the source expectation conjecture is exactly the weighted upper-tail statement (2.5).
- **Before:** the primal geometry was an orthant / trimmed-simplex escape event for a near-flat unitary.
- **Now:** complement symmetry shows the expectation gap itself is exactly reciprocal dispersion, and positivity gives a separate support-survival cost `2^{-s}` for every fixed witness.
- **Obstruction found:** deterministic positivity cannot force linear Fourier support; Fejer kernels already achieve `sqrt(n)` height with `Theta(sqrt(n))` pair support. The missing theorem is an entropy/inverse theorem for **how many** such supports or positive circuits can occur, not a support-size theorem alone.

This is the required materially fresh pivot after three unchanged P07-A runs.

---

# 7. Remaining gap and next attack

The exact remaining source-level gap can now be stated as either of two equivalent/primal objectives:

1. prove the integrated source-tail bound
   \[
   \int_1^{\sqrt n}(1-c^{-2})\Pr\{\vartheta(G_n)>c\sqrt n\}\,dc=o(1),
   \tag{7.1}
   \]
   preferably by a multiscale estimate which is allowed to deteriorate as `c downarrow1`; or
2. prove a positivity-sensitive support/circuit entropy estimate strong enough to make the weighted union bound (4.2) integrable on the supercritical range.

The next P07-A attack should therefore be **inverse uncertainty / sign entropy**, not another generic cone-statistical-dimension computation and not P07-B's Schur repair. A concrete prime-order subproblem is:

> classify or sharply count pair sets `S` of size `s=O(sqrt(n))` for which a positive trigonometric polynomial on `Z_n` with mean `1` can attain height `c sqrt(n)`, with enough quantitative structure that the `2^{-s}` random-mask cost beats the count.

The Fejer family suggests arithmetic-progressive / small-doubling supports are extremal candidates. A useful theorem would show that near-minimal support at a `sqrt(n)` spike forces approximate additive structure; then Freiman-type counting could potentially make (4.2) effective. For larger support, return to the already-developed prime positive-circuit determinant route and count **positive sign patterns**, rather than all minors.

No full-source solution is claimed. No finite numerical theta value is promoted to an arbitrary-`n` theorem. No independent audit is requested before proof development.

---

## SRG69 handoff preservation

The superseded SHPECTOROV-ZHAO-2026-SRG69 work remains preserved under
`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/` with mathematical status **OPEN / PARTIAL**, including its exact rooted `L/B/C` reduction, spectral transfer, cycle identities, incidence factorization, Euclidean filters and Section-I handoff. This run neither edits that history nor claims the graph existence question was solved.

## Ledger delta

```yaml
native_task_id: "6aa7b46f70a8819184095c277974c256"
role: "P07-A primal / structural"
target: "Randomstrasse101 Conjecture 18 / dense random circulant Lovasz theta"
source_metric:
  name: alpha_LL
  before: 1/2
  after: 1/2
  movement: none
status: "OPEN / PROVED PARTIAL"
new_proved_partial:
  - "exact distributional reciprocity X=theta/sqrt(n) d=1/X"
  - "exact expectation-gap identity E[X]-1=(1/2)E[(X-1)^2/X]"
  - "exact upper-tail integral E[X]-1=int_1^sqrt(n)(1-c^-2) P(X>c) dc"
  - "positive witness with height t needs at least (t-1)/2 nonzero conjugate Fourier pairs"
  - "fixed s-pair witness survives random source mask with probability exactly 2^-s"
  - "support-entropy union-bound reduction"
  - "Fejer kernels show sqrt(n)-height positivity is compatible with Theta(sqrt(n)) pair support; linear deterministic support route is false"
remaining_gap: "positivity-sensitive entropy/inverse theorem or another source-specific bound making the exact reciprocal upper-tail integral o(1)"
next_attack: "prime inverse uncertainty for positive sqrt(n)-spike trigonometric polynomials; count near-minimal/additively structured supports, then positivity-conditioned circuit sign entropy for larger supports"
P07B_boundary: "do not duplicate Fourier-dual exceptional-frequency / Schur-repair work"
SRG69: "preserved OPEN/PARTIAL; untouched"
```
