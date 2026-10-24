SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-24T11:34:52Z.
attacking: exact translation quotient after whole-law finite-fragment localization — remove absolute location with no approximation by pushing every coordinate shift into the precise affine space Range(A), while keeping the optimal QFORM density constant unchanged.

# Exact centered-extreme translation quotient

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Run: `20260924T113452Z-account03-B14-QFORM-auto11`.  
Status: **SUPPORTING LOCALIZATION IDENTITY / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN / CONTINUITY OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem is not claimed here. The point of this run is to finish a precise translation/localization interface: after the now-completed whole-law extreme-product reduction, absolute locations of all one-dimensional fragments can be quotiented out **exactly**, not by a weak limit, and the only price is the deterministic affine parameter that a translation can genuinely create. That parameter space is `Range(A)`, not all of `R^n` when `A` is singular.

## 1. Sources actually used

### 1.1 Whole-law finite-fragment localization

I use the completed account01/B14 theorem

`QFORM-FINITE-FRAGMENT-DENSE-EXTREME-LOCALIZATION-v1`,

at

`yspennstate/math-open-problems@801205dcdefd30acfe1609146aeead485c4a7c71`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B14/20260924T101356Z-account01-B14-QFORM-auto11/REPORT.md`.

For

`K={f:R->[0,1] measurable : integral f=1}`

and `F_1` the class of bounded finite unions of intervals of total Lebesgue measure one, it proves for every fixed dimension and every fixed real symmetric matrix `A`

\[
\sup_{f_1,\ldots,f_n\in K} D(\mathcal L(X^TAX))
=
\sup_{F_1,\ldots,F_n\in\mathcal F_1}
D(\mathcal L(X^TAX)),
\tag{1.1}
\]

where each `X_i` on the right has density `1_{F_i}` and

\[
D(\mu)=\sup_{I}\frac{\mu(I)}{|I|}
\tag{1.2}
\]

with the supremum over bounded intervals of positive length. This is exactly the essential density height when finite. No common bound on fragment count, support diameter, or fragment locations is asserted.

### 1.2 Designated partner

The newest completed compatible account04/B14 theorem used at an actual inequality is

`QFORM-ANCHOR-RECYCLING-v1`,

at

`yspennstate/math-open-problems@a660ad837e01bdaa7459104cfbaa37b9172b3b8e`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260924T101606Z-account04-B14-anchor-recycling-r12/REPORT.md`.

In particular, with

\[
B_*=I_3-\frac23\mathbf1\mathbf1^T,
\qquad \operatorname{spec}(B_*)=\{1,1,-1\},
\tag{1.3}
\]

three literal independent cap-one anchors and an arbitrary independent environment carrying arbitrary affine fields and arbitrary dense environment curvature yield

\[
\|p_Q\|_{\infty,\mathrm{ess}}\le 6\sqrt\pi.
\tag{1.4}
\]

The partner also proves exact mass-linearity under finite/countable localization of the environment. I do not relabel either of those results as new.

### 1.3 Earlier same-slot work

This slot previously proved a smooth quantile-gauge equality using approximation and affine homogenization. The present result is different: it is an **exact fixed-matrix identity on the extreme finite-fragment class**, with no coefficient limit, no weak approximation in the translation step, and the exact affine space `Range(A)` exposed. The finite-fragment theorem and the earlier quantile theorem are inputs/background, not renamed results.

## 2. Main theorem: exact centered-extreme translation quotient

Fix `p in (0,1)`. For a probability law with distribution function `F`, write

\[
q_p=\inf\{x:F(x)\ge p\}
\tag{2.1}
\]

for its lower `p`-quantile. Let `\mathcal F_{1,p}^0` be the class of bounded finite unions `E` of intervals such that

\[
|E|=1,
\qquad q_p(1_E)=0.
\tag{2.2}
\]

For a fixed real symmetric `n x n` matrix `A`, define

\[
C(A)=
\sup_{\substack{X_i\text{ independent}\\0\le f_i\le1}}
D\!\left(\mathcal L(X^TAX)\right).
\tag{2.3}
\]

### Theorem `QFORM-CENTERED-EXTREME-RANGE-AFFINE-QUOTIENT-v1`

For every real symmetric `A` and every fixed `p in (0,1)`, including the value `+infinity`,

\[
\boxed{
C(A)=
\sup_{\substack{Y_i\text{ independent},\;p_{Y_i}=1_{E_i}\\E_i\in\mathcal F_{1,p}^0\\b\in\operatorname{Range}(A)}}
D\!\left(\mathcal L(Y^TAY+b^TY)\right).
}
\tag{2.4}
\]

Thus every absolute coordinate location can be removed exactly. Arbitrary translations survive only as the deterministic linear coefficient `b`, and the exact translation-generated parameter space is

\[
\boxed{b\in\operatorname{Range}(A).}
\tag{2.5}
\]

If `A` is invertible, `Range(A)=R^n`, so the centered extreme core may carry an arbitrary deterministic affine linear term. If `A` is singular, no affine kernel component needs to be controlled in order to solve the original homogeneous problem by translation localization.

### Proof

By the completed finite-fragment theorem (1.1), it is enough to optimize over product densities `1_{F_i}` with `F_i` bounded finite unions of total length one.

Take such a product law and define

\[
m_i=q_p(1_{F_i}),
\qquad
G_i=F_i-m_i.
\tag{2.6}
\]

Translation preserves finite-union structure and Lebesgue measure, and the lower quantile translates exactly, hence

\[
G_i\in\mathcal F_{1,p}^0.
\tag{2.7}
\]

Writing `X=Y+m`, we have the samplewise algebraic identity

\[
X^TAX
=Y^TAY+2(Am)^TY+m^TAm.
\tag{2.8}
\]

The functional `D` is invariant under deterministic translation of the one-dimensional output, so the final scalar in (2.8) is irrelevant. Put

\[
b=2Am\in\operatorname{Range}(A).
\tag{2.9}
\]

This proves the `<=` direction in (2.4).

Conversely, let `Y_i` have densities `1_{G_i}` with `G_i in \mathcal F_{1,p}^0`, and let

\[
b\in\operatorname{Range}(A).
\]

Choose `m in R^n` satisfying

\[
2Am=b.
\tag{2.10}
\]

Set `X=Y+m`. Each `X_i` still has a cap-one density which is the indicator of a bounded finite union of total length one. Rearranging (2.8) gives

\[
Y^TAY+b^TY
=X^TAX-m^TAm.
\tag{2.11}
\]

Again `D` ignores the scalar output translation. Therefore the right side of (2.4) is at most `C(A)`. This proves equality. QED.

## 3. Full-target constant: zero loss under simultaneous centering and finite-fragment localization

Let `\mathcal A_3` denote the class of all real symmetric matrices, in all finite dimensions, with at least three eigenvalues of absolute value at least one. Define the optimal universal height

\[
C_{\rm full}=\sup_{A\in\mathcal A_3} C(A).
\tag{3.1}
\]

Taking the supremum of (2.4) over `A in \mathcal A_3` gives the exact identity

\[
\boxed{
C_{\rm full}
=
\sup_{\substack{A\in\mathcal A_3\\E_i\in\mathcal F_{1,p}^0\\b\in\operatorname{Range}(A)}}
D\!\left(\mathcal L(Y^TAY+b^TY)\right).
}
\tag{3.2}
\]

There is no support-radius parameter, no fragment-count parameter, no separation parameter, and no moment parameter on the right. Each individual input has bounded finite support, but the complexity and location-spread before centering may diverge across the optimizing sequence. Equation (3.2) therefore removes **unbounded support and absolute location as separate analytic obstructions with exactly zero loss in the universal constant**.

For `p=1/2`, the hard input laws may be taken to be median-zero bounded finite unions of intervals of total length one. The only remaining translation information is the finite-dimensional range-affine vector `b`.

This does not contradict the live corrections ruling out a universal bounded support diameter or universal fragment count: neither quantity is bounded in (3.2).

## 4. Why `Range(A)` is the sharp translation space

A deterministic coordinate translation `x -> x+m` changes a homogeneous quadratic polynomial by

\[
(x+m)^TA(x+m)-x^TAx
=2(Am)^Tx+m^TAm.
\tag{4.1}
\]

Hence every translation-generated linear coefficient lies in `Range(A)`. Conversely every `b in Range(A)` is `2Am` for some `m`, so every such affine term is generated by an actual coordinate translation.

Therefore (2.5) is exact, not merely sufficient. In particular, when `A` has a kernel, requiring a localization theorem to control arbitrary `b in R^n` is stronger than what translation removal itself needs. Any proof module whose only purpose is to absorb deterministic coordinate shifts may restrict its affine uniformity obligation to `Range(A)` without losing the homogeneous target.

This is potentially useful near singular/low-rank Schur branches: kernel-direction affine leakage must be justified by some other operation if it occurs; it is not forced merely by recentering the original product laws.

## 5. Actual application of account04/B14 r12

Take an arbitrary number `m>=0` of outside coordinates and the full original-coordinate matrix

\[
\mathcal A=
\begin{pmatrix}
B_*&C\\
C^T&D
\end{pmatrix},
\tag{5.1}
\]

where `C in R^{3 x m}` is arbitrary and `D` is any real symmetric `m x m` matrix. The anchor principal block is exactly `B_*`. Cauchy interlacing therefore gives at least two eigenvalues of `\mathcal A` at least `1` and at least one eigenvalue at most `-1`; every matrix (5.1) lies in the owner's exact target.

Apply theorem (2.4) with `A=\mathcal A`. It is enough to control centered finite-union product inputs and arbitrary

\[
b\in\operatorname{Range}(\mathcal A).
\tag{5.2}
\]

Choose `q` with `2\mathcal A q=b`. Then

\[
Y^T\mathcal A Y+b^TY
=(Y+q)^T\mathcal A(Y+q)-q^T\mathcal A q.
\tag{5.3}
\]

The translated coordinates `Y+q` remain independent with density caps one. Account04/B14 r12 applies to (5.1), including arbitrary outside curvature/couplings and arbitrary deterministic translations, and gives

\[
\Pr\{Y^T\mathcal A Y+b^TY\in I\}
\le 6\sqrt\pi\,|I|.
\tag{5.4}
\]

Thus the new centered-extreme quotient and the designated partner result combine at the actual inequality

\[
\boxed{
\sup_{\substack{E_i\in\mathcal F_{1,p}^0\\b\in\operatorname{Range}(\mathcal A)}}
\left\|p_{Y^T\mathcal A Y+b^TY}\right\|_{\infty,\mathrm{ess}}
\le6\sqrt\pi.
}
\tag{5.5}
\]

By (2.4), this is exactly equivalent to the homogeneous arbitrary-cap-one input bound for this entire anchor chamber.

As a nontrivial numerical check, choose

\[
C=\begin{pmatrix}5&-2\\-3&7\\11&4\end{pmatrix},
\qquad
D=\begin{pmatrix}-20&6\\6&13\end{pmatrix}.
\tag{5.6}
\]

The resulting `5 x 5` matrix has numerical eigenvalues

\[
-26.57437708,\;-4.06299146,\;0.41885989,\;5.95088363,\;18.26762502,
\tag{5.7}
\]

and hence is far from an exact rank-three example while still satisfying the target. Equation (5.5) gives

\[
\boxed{\|p\|_{\infty,\mathrm{ess}}\le6\sqrt\pi
=10.634723105433096\ldots}
\tag{5.8}
\]

uniformly over the centered finite-fragment laws and every translation-generated affine term, equivalently over all arbitrary cap-one product laws in the homogeneous formulation.

## 6. What is resolved and what remains

This run, together with the completed account01/B14 whole-law extreme localization, resolves the **pure input-localization part** of the B14 assignment at the level of the optimal essential-density constant:

- unbounded supports can be replaced by bounded finite unions with zero loss;
- arbitrary distant fragments remain allowed and incur no diameter/separation tax;
- absolute coordinate location can be quotiented out exactly by fixing any quantile `p` at zero;
- deterministic translation freedom becomes precisely `b in Range(A)`;
- no moments are introduced;
- no rotation of the random coordinates is used.

What is not resolved is the unrestricted matrix/product interaction. The bare condition `s_3(A)>=1` still does not produce a uniformly conditioned literal anchor triple or a paid grouped-bank receiver. Finite-union complexity is unbounded, and the known phase-aligned examples still prohibit a law-uniform pointwise quadratic-phase decay argument.

The strongest immediate successor question inside this same target is therefore no longer how to truncate or center the one-dimensional laws. It is:

> prove a whole-law receiver on the centered finite-union extreme core which is uniform in fragment count, support diameter and fragment locations, while extracting its three curvature resources directly from `s_3(A)>=1` without paying a tiny physical principal minor.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 7. Continuity

Equations (2.4) and (3.2) are concentration/essential-height identities. They do **not** prove that the original arbitrary-law output has a continuous density. Continuity does pass through the exact coordinate translations in Section 2 for an individual law, but the extreme-product supremum reduction is an optimization identity, not an instancewise representation of every arbitrary law by one finite-union law. Therefore the owner's full-target continuous-density request remains **OPEN** separately.

## 8. Integrity

No Gaussian, log-concave, moment, compact-support-for-the-original-law, connected-support, finite-uniform-fragment-count, or post-rotation independence hypothesis is used. The finite-union restriction is only an exact supremum reduction and carries no uniform complexity bound.

The visible repository search did not reveal this exact fixed-matrix `Range(A)` centered-extreme identity; that search miss is not treated as a literature novelty claim. The two underlying ingredients are explicitly credited above.

Repository transport and native learned-memory ingestion are separate. This run remains `WITHOUT_VERIFIED_BRAIN`. Model self-report: `GPT-5.6 Sol`. Configured reasoning effort is `UNKNOWN`; provider reasoning-token and thinking-time counters are not exposed and are not estimated. No scheduler/task state, email, push notification, permission, cross-account authentication, paid model/API/Codex call, remote workflow, or public-release state was changed.
