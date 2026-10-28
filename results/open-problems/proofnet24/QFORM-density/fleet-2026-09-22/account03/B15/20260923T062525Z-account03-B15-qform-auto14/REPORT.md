SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B15, 2026-09-23T06:25:25Z.
attacking: one-scale regularity compiler — collapse every output smoothing/small-ball scale into the third spectral singular value and obtain an exact fixed-kernel formulation of the full target.

# QFORM account03/B15 auto14 — exact one-scale fixed-kernel normal form

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `account03/B15`  
**Run:** `20260923T062525Z-account03-B15-qform-auto14`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_ONE_SCALE_KERNEL_NORMAL_FORM / FULL_TARGET_OPEN`

## 1. Exact target and the first unpaid implication

Let `s_3(A)` denote the third largest singular value of the real symmetric matrix `A`, equivalently the third largest absolute eigenvalue, with `s_3(A)=0` when `rank(A)<3`. For independent real coordinates with probability densities `0<=f_i<=1`, write

\[
Q_A=X^TAX.
\]

Define the extended density height of a probability law `mu` by

\[
\mathcal H(\mu)=\inf\{M:\mu\le M\,dx\}\in[0,\infty],
\]

so that `mathcal H(mu)=||p_mu||_infinity` when a bounded density exists and `+infinity` otherwise. The optimal constant in the owner's conjecture is

\[
C_*:=\sup_{\substack{n,\,f_i\le1\\s_3(A)\ge1}}\mathcal H(\mathcal L(Q_A)).
\tag{1.1}
\]

The full conjecture is `C_*<infinity`.

This run proves that **all output scales can be removed exactly**. The price is to let the matrix spectral scale vary and retain the natural factor `s_3(A)`. The resulting target is a single fixed smoothing or small-ball scale.

The central theorem is:

> **Fixed-kernel spectral normal form.** Let `K` be any bounded nonnegative probability density on `R`, and let the supremum below range over every finite dimension, every cap-one independent product input law, and every real symmetric matrix of rank at least three. Then
> \[
> \boxed{
> C_*
> =\sup_{\operatorname{rank}A\ge3}
> s_3(A)\,\sup_{y\in\mathbb R}
> \mathbb E\,K(y-Q_A).
> }
> \tag{1.2}
> \]
> The equality holds in the extended sense, including `+infinity`.

Thus the conjecture is equivalent, with **zero constant loss**, to proving the right side of (1.2) finite for **one arbitrarily chosen fixed probability kernel**. One may choose the kernel to fit the proof mechanism: a unit interval, a centered box, a tent, a Gaussian, an annular shell, or a compactly supported `C_c^infinity` bump with Schwartz Fourier transform.

This is a target-level regularity lemma. It does not assume that `Q_A` already has a density.

## 2. Kernel-height lemma for an arbitrary law

For a probability density `K`, define

\[
K_\varepsilon(u)=\varepsilon^{-1}K(u/\varepsilon),\qquad \varepsilon>0.
\]

### Lemma 2.1

For every probability law `mu` on `R`,

\[
\boxed{
\mathcal H(\mu)
=\sup_{\varepsilon>0}\|\mu*K_\varepsilon\|_\infty.
}
\tag{2.1}
\]

This includes the value `+infinity`.

### Proof

Suppose first `mu=p dx` with `||p||_infinity=M<infinity`. Since `K_epsilon` is a probability density,

\[
\|p*K_\varepsilon\|_\infty\le M.
\tag{2.2}
\]

Also `K_epsilon` is an approximate identity, so

\[
\|p*K_\varepsilon-p\|_1\to0.
\tag{2.3}
\]

If for some `eta>0` all sufficiently small `epsilon` had

\[
\|p*K_\varepsilon\|_\infty\le M-\eta,
\]

then from (2.3) one may choose a subsequence converging almost everywhere to `p`, forcing `p<=M-eta` almost everywhere, contradicting the definition of `M`. Hence the supremum in (2.1) is at least `M`, and (2.2) gives equality.

Conversely, suppose

\[
\sup_{\varepsilon>0}\|\mu*K_\varepsilon\|_\infty\le M<\infty.
\tag{2.4}
\]

For every nonnegative compactly supported continuous `phi`,

\[
\int \phi(x)(\mu*K_\varepsilon)(x)\,dx\le M\int\phi(x)\,dx.
\]

As `epsilon->0`, the measures `(mu*K_epsilon)(x)dx` converge weakly to `mu`. Therefore

\[
\int\phi\,d\mu\le M\int\phi\,dx
\]

for every such `phi`, hence `mu<=M dx`. Thus a finite right side in (2.1) forces a bounded density with the same bound. If `mu` has no bounded density, the right side must therefore be infinite. QED.

This proof uses no continuity of the target output and no Fourier decay.

## 3. Exact collapse of the smoothing scale into `s_3(A)`

Apply Lemma 2.1 to `mu=L(Q_A)` in (1.1):

\[
C_*
=
\sup_{\substack{s_3(A_0)\ge1\\\varepsilon>0,\,y}}
\mathbb E K_\varepsilon(y-Q_{A_0}).
\tag{3.1}
\]

Set

\[
B=A_0/\varepsilon,\qquad z=y/\varepsilon.
\]

Since `Q_{A_0}=epsilon Q_B`,

\[
\mathbb E K_\varepsilon(y-Q_{A_0})
=
\varepsilon^{-1}\mathbb E K(z-Q_B).
\tag{3.2}
\]

The target constraint becomes

\[
s_3(A_0)=\varepsilon s_3(B)\ge1,
\]

or

\[
\varepsilon\ge s_3(B)^{-1}.
\tag{3.3}
\]

For fixed `B,z`, the right side of (3.2) is maximized subject to (3.3) at

\[
\varepsilon=s_3(B)^{-1},
\]

giving

\[
s_3(B)\mathbb E K(z-Q_B).
\]

Conversely, for every rank-`>=3` `B`, choosing `epsilon=1/s_3(B)` and `A_0=epsilon B` gives `s_3(A_0)=1`, so every term on the right side of (1.2) occurs in (3.1). This proves (1.2) exactly.

No matrix rotation is used. The input variables are unchanged under the scalar rescaling of `A`, so independence and the marginal density caps are untouched.

## 4. The cleanest corollary: a unit-interval concentration theorem

Choose the one-sided box probability density

\[
K_\Box(u)=\mathbf 1_{[0,1]}(u).
\]

Then (1.2) becomes

\[
\boxed{
C_*
=
\sup_{\operatorname{rank}A\ge3}
 s_3(A)\,
 \sup_{a\in\mathbb R}
 \Pr\{Q_A\in[a,a+1]\}.
}
\tag{4.1}
\]

Therefore the full conjecture is **exactly equivalent** to the single-scale anti-concentration inequality

\[
\boxed{
\sup_a\Pr\{X^TAX\in[a,a+1]\}
\le \frac C{s_3(A)}
}
\tag{4.2}
\]

for every symmetric `A` of rank at least three and every cap-one product law.

This formulation has no density hypothesis and no small parameter.

### Scaling back recovers every interval and absolute continuity

Assume (4.2). For any rank-`>=3` matrix `A`, any interval `I` of length `ell>0`, apply (4.2) to `B=A/ell`. Since

\[
s_3(B)=s_3(A)/\ell
\]

and `Q_B=Q_A/ell`, one obtains

\[
\boxed{
\Pr\{Q_A\in I\}
\le C\frac{|I|}{s_3(A)}.
}
\tag{4.3}
\]

Hence

\[
\mathcal L(Q_A)\le \frac C{s_3(A)}\,dx,
\tag{4.4}
\]

and in particular every owner-target matrix `s_3(A)>=1` has density at most `C`.

Thus **one unit interval is enough** because scalar multiples of `A` regenerate all physical output scales.

### Counterexample normal form

If `C_*=infinity`, (4.1) gives a sequence `(A_m,f^{(m)})` for which

\[
s_3(A_m)\sup_a\Pr(Q_{A_m}\in[a,a+1])\to\infty.
\tag{4.5}
\]

Because every probability is at most one, necessarily

\[
\boxed{s_3(A_m)\to\infty.}
\tag{4.6}
\]

So any failure can be witnessed at a **fixed unit output window with spectral scale tending to infinity**. This is exactly the rescaled image of narrower and narrower bad output intervals in the normalized `s_3=1` class.

## 5. Assigned-partner application: exact unit Gaussian heat theorem

The completed assigned partner `account04/B15` proves, for every probability law `mu`,

\[
\sup_{\varepsilon>0,y}(\mu*\gamma_\varepsilon)(y)
=\mathcal H(\mu),
\tag{5.1}
\]

where

\[
\gamma_\varepsilon(u)
=\frac1{\sqrt{2\pi}\varepsilon}
 e^{-u^2/(2\varepsilon^2)}.
\]

Source actually used:

- `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

Applying the same spectral homogeneity calculation in Section 3 to the partner identity gives the **actual target inequality**

\[
\boxed{
C_*
=
\sup_{\operatorname{rank}A\ge3}
 s_3(A)\,
 \sup_y\mathbb E\gamma_1(Q_A-y).
}
\tag{5.2}
\]

Equivalently, if `G~N(0,1)` is independent,

\[
\boxed{
C_*
=
\sup_{\operatorname{rank}A\ge3}
 s_3(A)\,\|p_{Q_A+G}\|_\infty.
}
\tag{5.3}
\]

This is a useful regularity transfer: `Q_A+G` always has a bounded `C^infinity` (indeed real-analytic) density, regardless of whether `Q_A` has yet been shown absolutely continuous. The full rough-output conjecture is still encoded exactly in the rate

\[
\boxed{
\|p_{Q_A+G}\|_\infty\lesssim s_3(A)^{-1}.
}
\tag{5.4}
\]

No limit `epsilon->0` appears in (5.4).

The partner's concrete inequality

\[
\Pr(|Q_A-y|\le1)
\le\sqrt{2\pi e}\,\mathbb E\gamma_1(Q_A-y)
\tag{5.5}
\]

also gives, after multiplication by `s_3(A)`, a direct same-instance comparison between the centered unit small-ball functional and the unit Gaussian functional.

At unit Gaussian scale there is complete law-uniform smoothness:

\[
\|p_{Q_A+G}\|_\infty\le\|\gamma_1\|_\infty=(2\pi)^{-1/2},
\]

\[
\|(p_{Q_A+G})'\|_\infty
\le\|\gamma_1'\|_\infty=(2\pi e)^{-1/2},
\tag{5.6}
\]

and similarly every fixed derivative is bounded by the corresponding Gaussian derivative. Thus the prior obstruction to a uniform modulus of continuity for the **raw** target densities disappears after this external unit smoothing, while the conjecture remains exactly equivalent to the spectral decay (5.4).

## 6. Other exact one-scale interfaces

The freedom in (1.2) is useful because the kernel can be matched to the proof.

### 6.1 Centered box

Take

\[
K_c(u)=\frac12\mathbf 1_{[-1,1]}(u).
\]

Then

\[
\boxed{
C_*
=\frac12\sup_{\operatorname{rank}A\ge3}
 s_3(A)\sup_y\Pr(|Q_A-y|\le1).
}
\tag{6.1}
\]

### 6.2 Annular box

Take

\[
K_{ann}(u)=\frac12\mathbf 1_{\{1<|u|<2\}}.
\]

This is again a probability density, so

\[
\boxed{
C_*
=\frac12\sup_{\operatorname{rank}A\ge3}
 s_3(A)\sup_y\Pr(1<|Q_A-y|<2).
}
\tag{6.2}
\]

Thus even a fixed punctured shell has exactly the same global optimal constant once spectral homogeneity is retained. This does **not** by itself cure the free-center two-sheet obstruction from the previous B15 run; it only removes the irrelevant all-scale bookkeeping.

### 6.3 Tent kernel: compact physical support and an integrable Fourier multiplier

Take

\[
K_T(u)=(1-|u|)_+.
\]

It is a probability density. Hence

\[
\boxed{
C_*
=
\sup_{\operatorname{rank}A\ge3}
 s_3(A)\sup_y
 \mathbb E(1-|Q_A-y|)_+.
}
\tag{6.3}
\]

With Fourier convention

\[
\widehat f(t)=\int e^{itu}f(u)\,du,
\]

one has

\[
\widehat K_T(t)
=\left(\frac{\sin(t/2)}{t/2}\right)^2.
\tag{6.4}
\]

Therefore

\[
\mathbb E(1-|Q_A-y|)_+
=\frac1{2\pi}\int_{\mathbb R}
 e^{-ity}\phi_A(t)
 \left(\frac{\sin(t/2)}{t/2}\right)^2dt,
\tag{6.5}
\]

and this integral is absolutely convergent for **every** law because `|phi_A(t)|<=1` and the multiplier in (6.4) is integrable.

Hence the full QFORM conjecture is exactly equivalent to bounding the fixed-scale, automatically Fourier-regularized functional

\[
\boxed{
\sup_{A,f,y}
\frac{s_3(A)}{2\pi}
\left|
\int e^{-ity}\phi_A(t)
\left(\frac{\sin(t/2)}{t/2}\right)^2dt
\right|<\infty.
}
\tag{6.6}
\]

The integral itself equals a nonnegative expectation, so the absolute value outside is harmless. Crucially, (6.6) requires neither an undamped Wiener norm nor law-uniform pointwise van-der-Corput decay.

### 6.4 Arbitrarily smooth compact kernel

Choose any nonnegative `K in C_c^infinity(R)` with `integral K=1`. Then `hat K` is Schwartz and

\[
\boxed{
C_*
=
\sup_{\operatorname{rank}A\ge3}
 s_3(A)\sup_y
\frac1{2\pi}\int e^{-ity}\phi_A(t)\widehat K(t)\,dt.
}
\tag{6.7}
\]

Thus high-frequency integrability can be built into the **test kernel itself with zero loss of equivalence**. What remains is the genuine product-geometry problem: prove the necessary `1/s_3(A)` gain in this fixed-scale smoothed expectation.

## 7. Precise separation of absolute continuity, boundedness, and continuity

The new normal form cleanly separates the logical issues.

1. **Absolute continuity and the universal `L^infinity` bound.** Proving any one of the one-scale inequalities (4.2), (5.4), (6.3), or (6.7) with one universal constant automatically gives (4.3) at every interval length, hence absolute continuity and the homogeneous density bound
   \[
   \|p_{Q_A}\|_\infty\le C/s_3(A).
   \tag{7.1}
   \]
   No continuity premise is needed.

2. **Continuity is stronger and does not follow merely from a bounded-density estimate for an arbitrary law.** The shared `CLAIMS.json` still lists the full continuous-representative claim as open. Separately, the completed `account02/B15` fixed-matrix report `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056` gives a source-reported theorem that every fixed rank-`>=3` target output has an instance-dependent bounded `C_0` density, using the earlier account03/B15 nonzero-diagonal theorem plus a zero-diagonal triangle/triangle-free proof. This run does not mutate the shared claim status.

3. **External unit Gaussian smoothing is uniformly regular even before raw continuity is used.** Equation (5.3) shows that the central universal constant can be studied entirely on these analytic unit-smoothed densities; the missing content is their `1/s_3(A)` height decay.

This is exactly the requested separation: raw continuity is not required to attack the central universal height, and the central height can be encoded in a uniformly smooth fixed-scale observable.

## 8. Why this changes the proof interface

Earlier formulations carried a free small scale `epsilon` or radius `r`, and several failed routes paid a reciprocal tiny physical minor at each scale. The identity (1.2) removes that parameter exactly. Every scale is converted into spectral size.

For a future proof one may now fix, once and for all, a convenient kernel `K`, for example the tent or a `C_c^infinity` bump, and prove only

\[
\boxed{
 s_3(A)\sup_y\mathbb E K(X^TAX-y)\le C.
}
\tag{8.1}
\]

The hard regime in this normal form is `s_3(A)->infinity`; bounded spectral scale contributes at most `s_3(A)||K||_infinity`. Any counterexample sequence must therefore be a high-spectral-scale sequence.

This form is compatible with the live corrections:

- no post-rotation independence is assumed;
- no law-uniform pointwise quadratic-phase decay is used;
- no arbitrary-joint rank-three coarea bound is used;
- no fiber-supremum dimension-free bound is used;
- no single physical minor is selected;
- the annular version is not presented as a cure for the known free-center/two-sheet obstruction;
- numerical histograms are not used.

The useful next mathematical question is now very sharp:

> For one fixed proof-friendly probability kernel `K` (preferably compactly supported smooth, or the tent), prove directly from original-coordinate product structure that
> \[
> \sup_y\mathbb E K(X^TAX-y)\lesssim s_3(A)^{-1}
> \]
> for every rank-`>=3` symmetric `A`.

Because `hat K` may be chosen Schwartz, an integrated Fourier proof no longer needs to establish any high-frequency tail merely to justify inversion; all mathematical effort can be spent on extracting the **linear spectral gain** `1/s_3(A)` from the coupled product quadratic phase.

## 9. Integrity ledger

- Full unrestricted QFORM universal constant: **OPEN / NOT PROVED**.
- Valid counterexample to QFORM: **none produced**.
- New result: exact fixed-kernel/single-scale spectral normal form (1.2), proved for every bounded probability kernel.
- Assigned partner actually applied: account04/B15 Gaussian heat-height theorem at `math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`, yielding the concrete one-scale equality (5.2) and the unit-noise formulation (5.3).
- Exact unit-interval concentration formulation: (4.1)-(4.2).
- Exact compact tent / absolutely convergent Fourier formulation: (6.3)-(6.6).
- Exact compact smooth / Schwartz-multiplier formulation: (6.7).
- Absolute continuity and `L^infinity` follow from a universal one-scale estimate by scaling; continuity remains a separate stronger issue.
- Source-reported fixed-matrix `C_0` theorem was noted but not promoted in shared `CLAIMS.json` by this worker.
- Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval occurred, but no authenticated native mathematical receiver context was consumed.

**First unpaid implication:** prove (8.1) with a universal constant for one fixed kernel `K`, uniformly over dimension, all cap-one independent product marginals, all signatures, and every symmetric rank-`>=3` matrix. This is exactly equivalent to the owner's full target.
