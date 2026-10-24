SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-24T11:03:54Z.
attacking: prove the maximal zero-loss translation-localization lemma and isolate the exact no-go: environment-dependent recentering removes arbitrary shifts but can never create missing quadratic curvature in a bad physical anchor block.

# account03/B14 — translation localization is zero-loss but curvature-invariant

Run: `20260924T110354Z-account03-B14-QFORM-auto11`.
Programme: `QFORM-DENSITY-3EIG-20260922`.
Fresh control read before publication: `yspennstate/math-research-brain@7b7d3a07b929a1935d45bbbccde70ba7968d4ccd`, OWNER CONTROL revision `2026-09-22.15`.
Status: **SUPPORTING LOCALIZATION THEOREM + RIGOROUS NO-GO FOR TRANSLATION-ONLY CURVATURE REPAIR / PARTNER RESULT APPLIED / FULL QFORM OPEN**.
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. No Gaussian, log-concavity, moment, bounded-support, connected-support, finite-fragment, post-rotation independence, arbitrary-joint coarea, conditional-density-cap, or law-uniform pointwise oscillatory-decay premise is used.

## 1. Source-valid partner theorem actually used

Completed account04/B14 result:

- repository: `yspennstate/math-open-problems`,
- commit: `deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`,
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260924T001624Z-account04-B14-scaled-schur-localization-r10/REPORT.md`.

If three original coordinates are independent cap-one variables and their symmetric quadratic Hessian is an invertible `3x3` matrix `H`, then arbitrary deterministic affine terms are allowed and

\[
\|p_{U^T H U+\ell^T U+c}\|_{\infty,\mathrm{ess}}
\le \frac{6\sqrt\pi}{\sigma(H)},
\qquad
\sigma(H):=\min_j |\lambda_j(H)|.
\tag{1}
\]

The source theorem is uniform in the affine term and imposes no support, fragment, tail or moment condition. Its own conclusion is essential boundedness; continuity is separate.

The latest account04/B14 r12 handoff, source `math-open-problems@a660ad837e01bdaa7459104cfbaa37b9172b3b8e`, records the reflection-block special case under a linear translation bank. The theorem below identifies the exact general conditioning principle behind that mechanism and, crucially, its structural limit.

## 2. Main theorem: arbitrary environment-dependent translation localization

### Theorem `QFORM-TRANSLATION-CURVATURE-INVARIANCE-v1`

Let `U=(U_1,...,U_k)` be independent real random variables, and let `T` be any random element independent of `U`. No density, support, moment or dimensional assumption is imposed on `T`. Let `H` be a fixed real symmetric `k x k` matrix. Let

\[
g:T\to\mathbb R^k,\qquad r:T\to\mathbb R
\]

be arbitrary measurable functions for which the displayed random variables are finite almost surely, and put

\[
Q=U^T H U+2U^T g(T)+r(T).
\tag{2}
\]

For an arbitrary measurable recentering `psi:T->R^k`, define `S=U+psi(T)`. Then samplewise

\[
Q=S^T H S+2S^T\bigl(g(T)-H\psi(T)\bigr)
 +r(T)+\psi(T)^T H\psi(T)-2\psi(T)^T g(T).
\tag{3}
\]

In particular:

1. the conditional quadratic Hessian in the anchor variables is **exactly `H` for every value of the environment**, regardless of the choice or size of `psi`;
2. any conditional interval-density bound uniform over deterministic affine terms passes through arbitrary environment-dependent recentering with **zero constant loss**;
3. conversely, recentering alone can never improve the rank, inertia, eigenvalues, or smallest absolute eigenvalue of the anchor Hessian.

More explicitly, assume that for some finite `C_H`, every deterministic `a in R^k` and `c in R` satisfy

\[
\Pr\{U^T H U+2a^T U+c\in I\}\le C_H |I|
\tag{4}
\]

for every interval `I`. Then (2) satisfies

\[
\boxed{\Pr\{Q\in I\}\le C_H|I|}
\tag{5}
\]

for every interval `I`, with the same constant. This remains true after any measurable recentering (3), even if `psi(T)`, `g(T)` and `r(T)` are unbounded and even if `T` has arbitrarily fragmented or unbounded support.

### Proof

The algebraic identity (3) follows from `U=S-psi(T)`:

\[
(U)^THU=S^THS-2S^TH\psi+\psi^TH\psi,
\]
\[
2U^Tg=2S^Tg-2\psi^Tg.
\]

Adding gives (3). The coefficient of the quadratic term in `S` is therefore exactly `H`; no translation can alter it.

For the probabilistic statement, condition on `T=t`. Independence of `U` and `T` means the conditional law of `U` is its original law. Equation (2) becomes

\[
U^T H U+2g(t)^TU+r(t),
\]

so (4) yields

\[
\Pr\{Q\in I\mid T=t\}\le C_H|I|
\]

for almost every `t`. Integrating with respect to the law of `T` gives (5). No normalization of fragments, tail truncation, expectation of `|T|`, or bound on `g,r,psi` occurs. QED.

### Physical-coordinate corollary

Let the original coordinates be partitioned as `I sqcup J`, with `|I|=3`, `U=X_I`, `T=X_J`, and let the original quadratic matrix be

\[
A=\begin{pmatrix}H&C\\C^T&D\end{pmatrix}.
\]

Then

\[
X^TAX=U^THU+2U^TCT+T^TDT.
\]

Thus every measurable outside-dependent recentering `U -> U+psi(T)` leaves the anchor Hessian `H=A_{I,I}` unchanged. Applying the account04/B14 partner theorem (1), if `H` is invertible and the three anchor inputs have density caps at most one,

\[
\boxed{\|p_{X^TAX}\|_{\infty,\mathrm{ess}}\le \frac{6\sqrt\pi}{\sigma(H)}}.
\tag{6}
\]

This remains valid with arbitrary deterministic coordinate translations, arbitrary outside curvature and cross-couplings, and arbitrary unbounded/fragmented outside laws, because all such changes are absorbed into the affine environment after conditioning.

## 3. Translation-only no-go on a genuine diffuse target family

Let `m>=1`. Split `3m` original coordinates into three disjoint banks `I_1,I_2,I_3`, each of size `m`, and set

\[
u_r=m^{-1/2}\mathbf 1_{I_r},\qquad U_0=[u_1\ u_2\ u_3].
\]

Let

\[
B_*=I_3-\frac23\mathbf1\mathbf1^T,
\qquad \operatorname{spec}(B_*)=\{1,1,-1\},
\tag{7}
\]

and define

\[
A_m=U_0B_*U_0^T.
\tag{8}
\]

Since `U_0^T U_0=I_3`, the nonzero spectrum of `A_m` is exactly `{1,1,-1}`. Hence every `A_m` is a literal instance of the owner's full three-large-eigenvalue target.

Take any three physical anchor coordinates `I`.

- If two anchors lie in the same bank, the corresponding rows of the bank-membership matrix coincide, so `(A_m)_{I,I}` is singular.
- If one anchor is taken from each bank, then up to simultaneous permutation

\[
(A_m)_{I,I}=\frac1m B_*,
\]

hence

\[
\sigma\bigl((A_m)_{I,I}\bigr)=\frac1m.
\tag{9}
\]

Therefore

\[
\boxed{\max_{|I|=3}\sigma\bigl((A_m)_{I,I}\bigr)=\frac1m.}
\tag{10}
\]

By the main theorem, **no measurable translation/recentering of any chosen three physical anchors by any function of all remaining coordinates can change (10)**. In particular the completed account04/B14 physical-triple theorem can give, at best, the actual inequality

\[
\boxed{\|p_{X^TA_mX}\|_{\infty,\mathrm{ess}}\le 6\sqrt\pi\,m}
\tag{11}
\]

from any physical triple, even after the most general outside-dependent recentering allowed above.

This deterioration is not a property of the output law. The previously completed disjoint-bank localization theorem for exactly the same `A_m` family, source

`yspennstate/math-open-problems@4366a5648435eb9bfd6dcc40d4aa6fc3b3e67f6c`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260924T013955Z-account03-B14-QFORM-auto11/REPORT.md`

aggregates each entire bank before paying inverse curvature and proves

\[
\boxed{\|p_{X^TA_mX}\|_{\infty,\mathrm{ess}}\le 12\sqrt\pi}
\tag{12}
\]

uniformly in `m` and in every admissible cap-one product law.

Equations (11)-(12) isolate a genuine architectural boundary: **translation localization is zero-loss for affine nuisance terms, but translation localization cannot repair delocalized curvature. Aggregation must occur before reciprocal physical-minor payment.**

For reference,

\[
6\sqrt\pi\approx 10.6347231054,\qquad 12\sqrt\pi\approx21.2694462109.
\]

Thus once `m>=3`, the uniform grouped certificate (12) is already strictly stronger than the best partner physical-triple certificate obtainable after arbitrary recentering; the gap grows linearly with `m`.

## 4. Why this matters for translations, fragments and unbounded supports

The positive part of the theorem completely removes a common hidden assumption. One may center an anchor block by an arbitrary function of the outside coordinates, even one whose magnitude has no finite moment and whose range has infinitely many distant fragments. Since the partner theorem is uniform over the induced affine coefficient, all such shifts cost exactly zero.

The negative part is equally important. A localization proof may not claim that clever choice of centers, quantiles, fragment-dependent shifts, Schur translations, or other environment-dependent recenterings turns a tiny physical principal block into a uniformly curved one. The quadratic Hessian is invariant under every such operation. On the family (8), its best physical scale is exactly `1/m` forever.

This is compatible with the live corrections that one good physical triple is not forced by the bare spectral hypothesis and that product aggregation has to occur before fiberwise trace or reciprocal-minor payment.

## 5. Continuity ledger

The theorem above transfers interval-density bounds and essential `L^infinity` bounds. The account04/B14 r10 premise used here does not itself claim continuity, so this report does not infer a continuous representative from (6) or (11). The full target's continuity conclusion remains OPEN.

## 6. Exact remaining implication

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

For B14, the useful translation/localization conclusion is now sharp:

- arbitrary deterministic or outside-dependent shifts are harmless once a valid affine-uniform anchor compiler is available;
- remote fragments and unbounded environments cost zero because the conditional estimate is mass-linear;
- but recentering cannot improve curvature.

The remaining structural work must therefore create a paid receiver by **grouping/aggregating independent source banks before conditioning**, or by a genuinely joint small-ball/Fourier mechanism that does not pay an inverse tiny physical block. Translation-only refinements cannot close that gap.

## 7. Integrity

Fresh control and live corrections were re-read before publication. Repository retrieval/write/readback is distinct from native learned-memory ingestion; no authenticated native receiver-memory use was observed, so the execution status remains `WITHOUT_VERIFIED_BRAIN`.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort and provider reasoning-token/thinking-time counters were not exposed and are reported as `UNKNOWN`/`null`. No schedule, task identity, enabled/paused state, email, push notification, cross-account authentication, paid API/Codex call, remote workflow, permission, or public-release state was changed.
