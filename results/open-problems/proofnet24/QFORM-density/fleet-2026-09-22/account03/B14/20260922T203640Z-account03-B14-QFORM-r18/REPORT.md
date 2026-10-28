# account03/B14 — active-block Fourier localization and exact translation quotient

Run: `20260922T203640Z-account03-B14-QFORM-r18`

Status: `SUPPORTING_THEOREM_PROVED / TARGET_RELEVANT / FULL_QFORM_OPEN / CONTINUITY_CONDITIONAL / WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction-aware scope

The full target remains open: for every finite `n`, independent real coordinates with densities `0 <= f_i <= 1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a dimension-free bound on the density of `Q=X^T A X`, or construct a valid counterexample.

This report does not use the refuted law-uniform pointwise van-der-Corput estimate, the refuted arbitrary-joint 3D coarea inequality, a positive moment of conditional projection-density suprema, or independence after rotating to eigen-coordinates. It also does not normalize individual support fragments.

The purpose is narrower and directly tied to B14: identify exactly how arbitrary outside-coordinate translations and unbounded fragmented laws enter an **integrated Fourier** proof, and remove every range-compatible translation and every localization loss before any reciprocal geometric estimate is paid.

## 2. Setup

Choose an original-coordinate subset of size `m` and write the symmetric matrix in physical coordinates as

\[
A=\begin{pmatrix}B&C\\ C^T&D\end{pmatrix},
\qquad X=(U,V),
\]

where `B` is `m x m`. Because this is an original-coordinate split, `U` and `V` are independent and the coordinates within `U` remain independent.

For an admissible product law `mu` of `U` and `b in R^m`, define

\[
\psi_{B,b,\mu}(t)
:=\mathbb E_\mu e^{it(U^TBU+b^TU)},
\qquad
J_B(b;\mu):=\int_{\mathbb R}|\psi_{B,b,\mu}(t)|\,dt
\in[0,\infty].
\tag{2.1}
\]

All statements below are valid as extended-real inequalities; finiteness is asserted only when explicitly assumed or proved.

Let `D_m` denote the class of cap-one product laws on `R^m`. Let `F_m` denote product laws whose one-dimensional marginals are indicators `1_E`, where every `E` is a compact finite union of intervals with total Lebesgue measure one.

## 3. Conditional active-block inequality

For fixed outside value `V=v`,

\[
Q(U,v)=U^TBU+2U^TCv+v^TDv.
\]

Therefore the characteristic function of the full quadratic form satisfies the exact identity

\[
\phi_Q(t)
=\mathbb E_V\left[e^{itV^TDV}\,\psi_{B,2CV,\mu_U}(t)\right].
\tag{3.1}
\]

Taking the absolute value **after** retaining the whole active block, then using only the triangle inequality in the outside variable,

\[
|\phi_Q(t)|
\le \mathbb E_V|\psi_{B,2CV,\mu_U}(t)|.
\tag{3.2}
\]

Tonelli now gives

\[
\boxed{
\int_{\mathbb R}|\phi_Q(t)|\,dt
\le
\mathbb E_V J_B(2CV;\mu_U)
\le
\sup_{b\in\operatorname{Range}(C)}J_B(b;\mu_U).
}
\tag{3.3}
\]

(The factor `2` is immaterial because `Range(C)` is a linear subspace.)

This inequality has no assumption on the law, support, moments, or dimension of `V`, and no dependence on `D`. Arbitrary outside quadratic terms only contribute the unimodular phase in (3.1). Arbitrary outside couplings enter solely through the affine vector `2Cv`.

## 4. Exact translation quotient: only kernel leakage is essential

Because `B` is real symmetric,

\[
\mathbb R^m=\operatorname{Range}(B)\oplus\ker B.
\]

Write

\[
b=b_R+b_0,
\qquad b_R\in\operatorname{Range}(B),
\qquad b_0=P_{\ker B}b.
\]

Choose `s` with

\[
2Bs=-b_R.
\tag{4.1}
\]

Putting `U=Y+s`,

\[
U^TBU+b^TU
=Y^TBY+b_0^TY+\kappa,
\tag{4.2}
\]

for a deterministic constant `kappa`. Translation preserves coordinate independence and every marginal density cap `<=1`; the constant in (4.2) contributes only a unimodular Fourier factor. Hence translation is a bijection of `D_m` and

\[
\boxed{
\sup_{\mu\in D_m}J_B(b;\mu)
=
\sup_{\mu\in D_m}J_B(P_{\ker B}b;\mu).
}
\tag{4.3}
\]

Exactly the same equality holds with `D_m` replaced by `F_m`, because translating a compact finite union of intervals preserves compactness, finite fragment count, and total measure one.

Thus the genuine outside-affine obstruction is the subspace

\[
K(B,C):=P_{\ker B}\operatorname{Range}(C)\subseteq\ker B.
\tag{4.4}
\]

If `B` is invertible then `K(B,C)={0}`: **all** outside-induced affine terms are removable with no constant loss, regardless of the size of `C` or the outside support.

## 5. Law-level localization of the Fourier budget

Here the designated partner result is applied to an actual inequality.

Account04/B14 proved `QFORM-LAW-LEVEL-FINITE-MIXTURE-LOCALIZATION-v1` at

`yspennstate/math-open-problems@321ec7899f4972d125d641408512fe9e5e9dcf4c`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T201507Z-account04-B14-mixture-localization-r4/REPORT.md`.

It states that every cap-one product law is a total-variation limit of finite convex mixtures of laws in `F_m`, with no support-radius, translation, separation, or fragment-count parameter.

Fix `b`. The functional

\[
\mu\mapsto J_B(b;\mu)
\tag{5.1}
\]

is convex: the characteristic function is linear in `mu`, absolute value is convex, and integration preserves convexity. It is also lower semicontinuous under total variation. Indeed, total-variation convergence implies pointwise (in fact uniform) convergence of characteristic functions, so Fatou gives

\[
J_B(b;\mu)
\le\liminf_r J_B(b;\mu_r).
\tag{5.2}
\]

Let `mu_r` be the finite-mixture approximants supplied by the partner theorem. If

\[
\mu_r=\sum_\alpha \theta_{r,\alpha}\nu_{r,\alpha},
\qquad \nu_{r,\alpha}\in F_m,
\]

then

\[
J_B(b;\mu_r)
\le\sum_\alpha\theta_{r,\alpha}J_B(b;\nu_{r,\alpha})
\le \sup_{\nu\in F_m}J_B(b;\nu).
\tag{5.3}
\]

Combining (5.2)--(5.3), and using the reverse inclusion `F_m subset D_m`, proves the exact equality

\[
\boxed{
\sup_{\mu\in D_m}J_B(b;\mu)
=
\sup_{\nu\in F_m}J_B(b;\nu).
}
\tag{5.4}
\]

This is the partner theorem applied directly to the nonlinear integrated-Fourier functional. It is consistent with the earlier general convex-output transfer theorem, but here it is inserted into the active-block conditional inequality and the translation quotient.

Taking the supremum over any affine subspace of `b` preserves (5.4).

## 6. Main theorem: active-block Fourier localization with kernel leakage

Define the extreme active-block Fourier constant

\[
\mathcal L(B,K)
:=
\sup_{\nu\in F_m}\sup_{k\in K}
\int_{\mathbb R}
\left|
\mathbb E_\nu e^{it(U^TBU+k^TU)}
\right|dt,
\tag{6.1}
\]

where `K` is a linear subspace of `ker B`.

### Theorem `QFORM-ACTIVE-BLOCK-FOURIER-LOCALIZATION-v1`

For every original-coordinate block decomposition

\[
A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix}
\]

and every admissible independent cap-one product input,

\[
\boxed{
\int_{\mathbb R}|\phi_{X^TAX}(t)|\,dt
\le
\mathcal L\!\left(B,P_{\ker B}\operatorname{Range}(C)\right).
}
\tag{6.2}
\]

No moment, compact-support, connected-support, fragment-count, support-diameter, translation-size, or outside-dimension assumption is present.

### Proof

Equation (3.3) gives

\[
\int|\phi_Q|
\le \sup_{b\in\operatorname{Range}(C)}J_B(b;\mu_U).
\]

Taking the supremum over the active law can only enlarge the right side. Equation (4.3) replaces each `b` by `P_{ker B}b`. The image of `Range(C)` under that projection is exactly `K(B,C)`. Finally (5.4) replaces the supremum over all cap-one active product laws by `F_m` with no change of constant. This is (6.2). QED.

### Invertible-block corollary

If `B` is invertible,

\[
\boxed{
\int|\phi_Q(t)|dt
\le
\sup_{\nu\in F_m}
\int\left|\mathbb E_\nu e^{itU^TBU}\right|dt.
}
\tag{6.3}
\]

Thus once a uniform integrated-Fourier estimate is proved for an invertible original-coordinate active block, arbitrary outside blocks, cross-couplings, translations, distant fragments, and unbounded supports are automatically harmless. There is no need to localize or normalize the outside coordinates at all.

## 7. Density and continuity consequence

If the right side of (6.2) is finite and bounded by `L`, then `phi_Q in L^1(R)`. Fourier inversion therefore supplies a bounded **continuous** density with

\[
\boxed{\|p_Q\|_\infty\le L/(2\pi).}
\tag{7.1}
\]

So, unlike total-variation transfer of an already-known `L^infinity` density estimate, the integrated-Fourier route automatically carries the requested continuity conclusion once `mathcal L` is finite.

This does **not** prove continuity for the full QFORM target because a universal bound on the right side of (6.2) has not been proved under the bare three-large-eigenvalue hypothesis.

## 8. Why this avoids the previous fragmentwise scale tax

Earlier B14 work showed that if one first decomposes a unit-measure extreme set into fragments, normalizes each fragment, rescales it to unit width, applies a reciprocal-scale estimate, and then averages conditional sup bounds, a factor such as `N^2` can be manufactured even for an unchanged `I_3` law split into `N` labels.

The present theorem never performs that operation. The entire finite-fragment set remains one probability law inside `J_B`. Translation is applied once to the entire active law, and the absolute Fourier integral is estimated only after the full active law is retained. Therefore no fragment length, number, or separation enters (6.2).

## 9. Exact remaining implication

The theorem isolates the next unpaid step rather than renaming it:

> Find, from the bare hypothesis that the full symmetric `A` has at least three eigenvalues with absolute value at least one, an original-coordinate active block/grouped-coordinate mechanism for which `mathcal L(B,K(B,C))` is bounded by one universal constant; or prove the equivalent joint estimate without selecting one block.

For invertible `B`, this reduces to the homogeneous active-block Fourier budget. For singular `B`, only the kernel-leakage subspace `K(B,C)` survives translation. The latter is precisely where a grouped/ridge mechanism must pay; range-affine terms are not part of the remaining difficulty.

The three-large-eigenvalue condition does not itself guarantee one uniformly conditioned physical principal triple, so (6.3) alone is not a full proof.

## 10. Source integrity and status


Repository retrieval was genuine but no authenticated native brain receiver-memory use occurred, hence `WITHOUT_VERIFIED_BRAIN` remains required. No scheduler mutation, new task, notification change, email/Drive action, public release, remote workflow, paid API/model/Codex call, credential access, or unrelated private data was used.
