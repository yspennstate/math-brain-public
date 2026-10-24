SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T15:36:52Z.
attacking: whole-law bilinear receiver localization: combine a translation-uniform L2 core with an untouched product receiver bank before any thin-fragment normalization.

# account03/B14 auto11 — L2-to-Linfinity bilinear receiver localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `SUPPORTING_THEOREM_PROVED / FULL_QFORM_OPEN`  
Continuity: only existence of an essentially bounded density is proved in the stated scope; continuity is not claimed.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Purpose

This run addresses a localization failure mode that survives arbitrary remote fragments and unbounded supports: a smoothing coefficient may vanish on a moving hyperplane of a conditioned product bank, so a pointwise conditional Linfinity estimate contains a reciprocal coefficient and cannot simply be supremized over the conditioning variable. The new lemma aggregates that singularity against the whole product law before normalization. The singularity is only a half-power and is therefore uniformly integrable under the cap-one hypothesis.

The mechanism is useful with the completed account04/B14 affine slice-Fresnel theorem: that theorem supplies an L2 core uniformly under arbitrary conditioning-generated affine terms and arbitrary hub chirps, while a disjoint bilinear driver/receiver bank upgrades L2 to Linfinity with no support, moment, translation, fragment-count, or fragment-separation tax.

## 2. Abstract bilinear receiver theorem

Let `Z=(Z_1,...,Z_m)` and `W=(W_1,...,W_k)` be independent vectors, all scalar coordinates mutually independent and each having a probability density bounded by one. Let `C` be a nonzero real `k x m` matrix and `d in R^k`. Let `T_z` be a family of real random variables, built from coordinates independent of `W`, such that for almost every `z` the conditional law of `T_z` has a density `q_z` satisfying

\[
\|q_z\|_2\le K
\tag{2.1}
\]

with the same constant `K`. No moment or support assumption is made, and `T_z` may depend arbitrarily measurably on `z` through translations or other affine parameters.

Define

\[
Q=T_Z+(2CZ+d)^T W.
\tag{2.2}
\]

### Theorem 2.1 — `QFORM-L2-BILINEAR-RECEIVER-LOCALIZATION-v1`

Writing `sigma=||C||_op`,

\[
\boxed{
\|p_Q\|_\infty\le 2^{3/2}K\,\sigma^{-1/2}.
}
\tag{2.3}
\]

The constant is uniform in `d`, the dimensions `m,k`, all translations of `Z,W`, all support locations, all fragment counts and separations, and all moments.

### Proof

Fix `z` and write

\[
b_z=2Cz+d.
\]

The Rogozin-Ball product projection bound for cap-one independent coordinates gives the scalar projection density estimate

\[
\|p_{b_z^T W}\|_\infty\le {\sqrt2\over \|b_z\|_2}.
\tag{2.4}
\]

Since this density has mass one,

\[
\|p_{b_z^T W}\|_2
\le \|p_{b_z^T W}\|_\infty^{1/2}
\le 2^{1/4}\|b_z\|_2^{-1/2}.
\tag{2.5}
\]

Conditional on `Z=z`, `T_z` and `b_z^T W` are independent, so Cauchy-Schwarz in the convolution variable gives

\[
\|p_{Q\mid Z=z}\|_\infty
\le \|q_z\|_2\,\|p_{b_z^TW}\|_2
\le K2^{1/4}\|2Cz+d\|_2^{-1/2}.
\tag{2.6}
\]

It remains to average the moving reciprocal coefficient without imposing a tail or support cutoff. Choose a unit left singular vector `u` of `C` with

\[
\|C^T u\|_2=\sigma.
\]

Then

\[
\|2CZ+d\|_2\ge |2(C^Tu)^T Z+u^Td|.
\tag{2.7}
\]

The scalar variable on the right has a density bounded by

\[
M\le {\sqrt2\over 2\sigma}={1\over \sqrt2\,\sigma}
\tag{2.8}
\]

by the same product projection theorem. For any real random variable `Y` with density bounded by `M`, symmetric decreasing rearrangement (equivalently, the bathtub principle) gives the exact cap-only half-Riesz bound

\[
\sup_a\mathbb E|Y-a|^{-1/2}
\le M\int_{-1/(2M)}^{1/(2M)}|x|^{-1/2}dx
=2\sqrt2\,M^{1/2}.
\tag{2.9}
\]

Using (2.8),

\[
\mathbb E\|2CZ+d\|_2^{-1/2}
\le 2^{5/4}\sigma^{-1/2}.
\tag{2.10}
\]

Average (2.6) over `Z` and combine (2.10):

\[
\|p_Q\|_\infty
\le K2^{1/4}\,2^{5/4}\sigma^{-1/2}
=2^{3/2}K\sigma^{-1/2}.
\]

The right side is finite, so the conditional densities integrate to a global density and the displayed essential-supremum bound follows. QED.

## 3. Exact translation/localization consequences

No localization of the driver bank is needed. The whole law of `Z` is used in (2.10), so countably many distant fragments are aggregated before any reciprocal coefficient is paid. In particular, splitting `Z` into thin pieces and normalizing them separately is unnecessary and can only lose information.

Physical translations are also free. Replacing `Z` by `Z+z_0` and `W` by `W+w_0` changes

\[
2W^TCZ
\]

by an affine `W` term, an affine `Z` term, and a constant. The affine `W` term is absorbed into `d`; the affine `Z` term is absorbed into the arbitrary `z`-dependence of `T_z`; the constant is irrelevant. Hence the same constant (2.3) survives arbitrary shifts, even with unbounded or disconnected supports.

A further outside original-coordinate block may be conditioned first. If it merely makes `d` and the affine parameters of `T_z` measurable functions of that outside block, (2.3) is uniform in those parameters and therefore survives the final averaging with no loss.

## 4. Application of the completed account04/B14 affine slice-Fresnel theorem

The assigned partner result actually applied is account04/B14 r9:

`yspennstate/math-open-problems@b5f173477a3889ad9432ea7d97767e969c83b279`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T141430Z-account04-B14-affine-slice-fresnel-r9/REPORT.md`.

Its Theorem 3.1 gives, on the residual-diffuse heavy-null slice branch, the unnormalised slice Fourier estimate

\[
|\widehat\mu_{v,g}(t)|\le 4\sqrt\pi\,|\gamma t|^{-1/2},
\tag{4.1}
\]

uniformly in the full affine vector `g`, the slice parameter `v`, support/tail geometry, and dimension. Put

\[
L=hV+q_0.
\]

Changing slice coordinates from `v` to `l` introduces only the Jacobian `1/|h|`, so the corresponding disintegration `nu_l` obeys

\[
|\widehat\nu_l(t)|
\le A|t|^{-1/2},
\qquad
A={4\sqrt\pi\over |h|\sqrt{|\gamma|}}.
\tag{4.2}
\]

Let `X_0` be the independent hub variable and allow an arbitrary measurable real hub phase `H_z(X_0)`; for a quadratic form this includes any self-pivot `aX_0^2` plus all conditioning-generated linear and constant terms. Define

\[
T_z=H_z(X_0)+2X_0L+Y_z.
\tag{4.3}
\]

The account04 slice estimate implies an L2 bound uniformly in `z`. Indeed, with

\[
G_{t,z}(l)=\int f_0(x)e^{itH_z(x)}e^{2itlx}\,dx,
\]

Plancherel gives

\[
\int_{\mathbb R}|G_{t,z}(l)|^2dl
={\pi\over |t|}\int f_0(x)^2dx
\le {\pi\over |t|}.
\tag{4.4}
\]

If `m(l)=nu_l(R)`, then `|nu_hat_l(t)|<=m(l)` and (4.2) imply

\[
|\widehat\nu_l(t)|^2\le A|t|^{-1/2}m(l).
\]

Since `int m(l)dl=1`, Cauchy-Schwarz in `l` and (4.4) yield

\[
|\phi_{T_z}(t)|
\le \sqrt{\pi A}\,|t|^{-3/4}.
\tag{4.5}
\]

Using also `|phi|<=1`, Fourier Plancherel gives

\[
\|p_{T_z}\|_2
\le \sqrt{3/\pi}(\pi A)^{1/3}
={2^{2/3}\sqrt3\over |h|^{1/3}|\gamma|^{1/6}}
=:K_{\rm core}.
\tag{4.6}
\]

This calculation is completely insensitive to `H_z`: multiplication of `f_0` by `e^{itH_z}` is unimodular. Thus the exact-null partner slice can be perturbed by an arbitrary nonzero hub self-quadratic coefficient without an L2 penalty.

Now add a disjoint driver bank `Z` and receiver bank `W` through

\[
2W^TCZ+d^TW,
\]

with `W` having no quadratic self-block and no coupling to the unconditioned core variables. Condition on `Z=z`. The partner theorem still supplies (4.6), because all cross-couplings from `z` into the core become arbitrary affine parameters already covered by account04/B14. Apply Theorem 2.1 to obtain the actual inequality

\[
\boxed{
\|p_Q\|_\infty
\le
{2^{13/6}\sqrt3
\over
|h|^{1/3}|\gamma|^{1/6}\sqrt{\|C\|_{\rm op}}}.
}
\tag{4.7}
\]

At the partner's normalized active scale

\[
|b|\ge1,\qquad c>1/2,\qquad h=b\sqrt c,\qquad |\gamma|\ge1,
\]

and if `||C||_op>=1`, then

\[
\boxed{
\|p_Q\|_\infty
\le 2^{7/3}\sqrt3
=8.7289890877\ldots .
}
\tag{4.8}
\]

This is an essential-boundedness result on the stated structured branch with arbitrary rough cap-one laws. It does not assert that the bare condition `s_3(A)>=1` always yields such a disjoint receiver block.

## 5. Why this is a genuine localization gain

A conditional Linfinity route would pay `||2CZ+d||^{-1}` and face a nonintegrable codimension-one singularity for ordinary bounded densities. The L2 receiver route pays only `||2CZ+d||^{-1/2}`, whose whole-law expectation is uniformly bounded by (2.10). Thus one gains an entire half power exactly by postponing the Linfinity endpoint until after the independent receiver bank is convolved.

This is especially relevant to the partner's near-null obstruction. The hub self-quadratic coefficient may be arbitrarily small or nonzero inside `H_z`; no truncation such as `|X_0|<=R` is introduced, so there is no tail or moment debt. The additional disjoint bilinear receiver is what converts the chirp-stable L2 core into a bounded density.

## 6. Scope and remaining debt

The full QFORM conjecture remains OPEN. The present theorem requires a structural decomposition exposing:

1. a core with the account04/B14 affine slice-Fresnel L2 certificate;
2. a disjoint original-coordinate receiver bank entering linearly after conditioning a driver bank;
3. a nonzero driver-receiver cross matrix `C`.

The bare three-large-eigenvalue condition has not been shown to force such a decomposition with `||C||_op` bounded below. Receiver self-curvature or receiver-core cross-couplings are also not handled by Theorem 2.1. Those are the next structural cases.

Continuity is separate: the proof constructs an essentially bounded density by conditional convolution and averaging, but no continuity modulus is obtained for arbitrary rough inputs.

## 7. Source integrity

Fresh owner controls and live corrections were read before publication. The argument does not use the refuted pointwise quadratic van-der-Corput bound, arbitrary-joint coarea, post-rotation independence, bounded-diameter localization, or fiber-sup dimension-free claims. The product-projection estimate is used only on genuine linear forms of untouched independent original-coordinate banks.

Partner actually applied at equation level: account04/B14 r9, commit `b5f173477a3889ad9432ea7d97767e969c83b279`, equations (3.6) and the affine-uniform conditioning interface.

Full target: OPEN.  
Native receiver-memory ingestion: NOT VERIFIED.
