# fleet01/B05 r29 — same-sign spectral-plane overlap Gram exit

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound  
**Run:** `20260923T082703Z-fleet01-B05-QFORM-r29`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / PRECISE_REMAINING_FACTOR_IDENTIFIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full owner target remains open. This report proves a product-preserving exact-rank-three exit that is uniform on an order-one overlap-gap branch. It does not assume spectral-coordinate independence. Continuity of the output density is not claimed.

## 1. Setup

Let

\[
A=R\Lambda R^\top,\qquad R^\top R=I_3,
\]

be an exact-rank-three active form, with

\[
\Lambda=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3),
\qquad |\lambda_j|\ge1.
\]

Choose two eigenvalues of the same sign and relabel so that \(\lambda_1\lambda_2>0\). Write every physical row of \(R\) as

\[
r_i=(p_i,z_i),\qquad p_i\in\mathbb R^2,\ z_i\in\mathbb R,
\]

relative to the same-sign spectral plane \(E=\operatorname{span}(e_1,e_2)\) and remaining line \(L=\operatorname{span}(e_3)\).

Define the plane/line overlap support

\[
H:=\{i:p_i\ne0\text{ and }z_i\ne0\}
\]

and overlap Gram

\[
K_E:=\sum_{i\in H}p_ip_i^\top.
\]

Since \(\sum_i p_ip_i^\top=I_2\), one has \(0\preceq K_E\preceq I_2\). Put

\[
\eta:=\lambda_{\min}(I_2-K_E)=1-\|K_E\|_{\rm op}.
\]

## 2. Assigned partner theorem used at the decisive inequality

The designated partner fleet02/B05 proved `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1` in

`yspennstate/math-open-problems@e74a5d8fabe1c914be1ca2d3689a2cd65ba58f`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T155206Z-b05-qform-779c4c9b/REPORT.md`.

If independent cap-one scalar inputs have coefficient vectors \(a_j\in\mathbb R^2\) satisfying \(\sum_j a_ja_j^\top=I_2\), their two-dimensional projection has joint density at most \(e\). Thus, for any full-rank two-row coefficient matrix \(C\), with \(G=CC^\top\), normalization by \(G^{-1/2}\) gives the actual inequality used here:

\[
\boxed{\|p_{CX}\|_\infty\le {e\over\sqrt{\det G}}.}
\tag{2.1}
\]

The newest fleet02/B05 result `QFORM-RULED-ONESHEET-ROUGH-INTERVAL-v1`, canonical mathematics

`yspennstate/math-open-problems@afe6d696017f5a0eb48a14fa7a1dcb35ce97df3`,

also gives in signature \((+,+,-)\)

\[
\operatorname*{ess\,sup}_{t\ge0}p_Q(t)\le\pi\sqrt2.
\tag{2.2}
\]

## 3. New theorem

### Theorem `QFORM-SAMESIGN-PLANE-OVERLAP-GRAM-EXIT-v1`

Let \(X_1,\ldots,X_n\) be independent real variables with probability densities bounded by one, and let \(Q=X^\top AX\) with exact-rank-three \(A=R\Lambda R^\top\) as above. If

\[
\eta=1-\left\|\sum_{i\in H}p_ip_i^\top\right\|_{\rm op}>0,
\]

then \(Q\) has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le {\pi e\over \eta\sqrt{|\lambda_1\lambda_2|}}
\le {\pi e\over\eta}.
}
\tag{3.1}
\]

In particular,

\[
\boxed{\|K_E\|_{\rm op}\le\frac12
\Longrightarrow
\|p_Q\|_\infty\le2\pi e<17.08.}
\tag{3.2}
\]

The same proof allows additional affine terms lying in the active spectral range, but no arbitrary external affine term is claimed here.

### Proof

Partition \(H^c\) into

\[
P:=\{i\notin H:z_i=0\},\qquad
L:=\{i\notin H:p_i=0\}.
\]

Rows with both components zero are harmless. Condition on the original coordinates \(X_H\). Then the three spectral coordinates become

\[
Y_E=a+C X_P,\qquad
Y_3=d+\sum_{i\in L}z_iX_i,
\tag{3.3}
\]

for deterministic conditional translations \(a\in\mathbb R^2,d\in\mathbb R\). Because the original form is \(X^\top R\Lambda R^\top X\), conditioning creates only these translations inside the spectral coordinates; no independent affine variable outside the active range is introduced.

Parseval in the same-sign plane gives

\[
G:=CC^\top
=\sum_{i\in P}p_ip_i^\top
=I_2-K_E.
\tag{3.4}
\]

Hence \(G\succeq\eta I_2\) and

\[
\det G\ge\eta^2.
\tag{3.5}
\]

Applying the assigned-partner projection theorem (2.1) to the translated pair \(Y_E\), its conditional joint density \(h\) obeys

\[
\|h\|_\infty\le {e\over\sqrt{\det G}}\le {e\over\eta}.
\tag{3.6}
\]

The same-sign contribution is

\[
S=\lambda_1Y_1^2+\lambda_2Y_2^2.
\]

After translating by \(a\) and scaling \(w_j=\sqrt{|\lambda_j|}Y_j\), its nonconstant part is, up to an overall sign, \(w_1^2+w_2^2\). The joint density of \(w\) is bounded by

\[
{e\over\sqrt{\det G}\sqrt{|\lambda_1\lambda_2|}}.
\]

Polar coarea gives for a.e. \(s>0\)

\[
p_{w_1^2+w_2^2}(s)
={1\over2}\int_0^{2\pi}
 p_w(\sqrt{s}\cos\theta,\sqrt{s}\sin\theta)\,d\theta,
\]

so

\[
\|p_S\|_\infty
\le {\pi e\over\sqrt{\det G}\sqrt{|\lambda_1\lambda_2|}}
\le {\pi e\over\eta\sqrt{|\lambda_1\lambda_2|}}.
\tag{3.7}
\]

The remaining contribution \(\lambda_3Y_3^2\) depends only on \(X_L\). Conditional on \(X_H\), the original-coordinate sets \(P\) and \(L\) are disjoint, hence independent. Therefore the conditional law of the full \(Q\) is a convolution of the bounded-density law in (3.7) with an arbitrary probability law. Convolution cannot increase an \(L^\infty\) density norm, giving

\[
\|p_{Q\mid X_H}\|_\infty
\le {\pi e\over\eta\sqrt{|\lambda_1\lambda_2|}}
\]

uniformly in the conditioned values. Averaging over \(X_H\) proves (3.1). QED.

## 4. Structural meaning of the survivor

If \(\|K_E\|_{\rm op}>1/2\), there is a unit vector \(w\in E\) such that

\[
\sum_{i\in H}(w\cdot p_i)^2>\frac12.
\tag{4.1}
\]

At the exact endpoint \(\eta=0\), some unit \(w\in E\) satisfies \(K_Ew=w\). Since \(\sum_i(w\cdot p_i)^2=1\), necessarily

\[
\boxed{w\cdot p_i=0\quad\text{for every pair-only row }i\in P.}
\tag{4.2}
\]

Thus all coefficient energy in one same-sign spectral direction lies on original coordinates that simultaneously carry the third spectral line. This is the exact support-incidence obstruction left by this theorem.

## 5. Infinitesimal-overlap stress

The endpoint \(\eta=0\) is not excluded by small overlap coefficients. Fix \(0<\delta<1\) and \(m\ge1\). Take rows

\[
r_{k,+}=\left({1\over\sqrt{2m}},0,+\sqrt{\delta\over2m}\right),\qquad
r_{k,-}=\left({1\over\sqrt{2m}},0,-\sqrt{\delta\over2m}\right),
\quad1\le k\le m,
\tag{5.1}
\]

plus \(m\) pure \(e_2\)-rows \((0,m^{-1/2},0)\) and \(m\) pure \(e_3\)-rows \((0,0,\sqrt{(1-\delta)/m})\). Cross terms cancel pairwise and direct summation gives

\[
R^\top R=I_3.
\]

Every row carrying \(e_1\) is mixed, and

\[
K_E=e_1e_1^\top,\qquad \eta=0,
\tag{5.2}
\]

for every \(\delta>0\), while each mixed-row slope satisfies

\[
{|z_i|\over\|p_i\|}=\sqrt\delta\to0.
\tag{5.3}
\]

So a conditioning theorem based only on the *support* of nonzero overlaps is necessarily discontinuous at zero overlap. This family is a mechanism stress, not a QFORM counterexample.

## 6. Newest partner result on the indefinite branch

For signature \((+,+,-)\), fleet02/B05 r18 gives

\[
\operatorname*{ess\,sup}_{t\ge0}p_Q(t)\le\pi\sqrt2.
\tag{6.1}
\]

Under the overlap-gap hypothesis, the theorem above controls the opposite side by

\[
\operatorname*{ess\,sup}_{t<0}p_Q(t)
\le {\pi e\over\eta\sqrt{\lambda_1\lambda_2}}.
\tag{6.2}
\]

Hence for \(\eta\ge1/2\) the full-line density cap is at most \(2\pi e<17.08\). This is an actual combination with the newest designated-partner result; it does not claim the two-sheet endpoint \(\eta=0\) is solved.

## 7. Precise first unpaid implication

The first unpaid coarea implication is now

`QFORM-SAMESIGN-PLANE-FULL-OVERLAP-ENDPOINT-v1`:

> Prove a dimension-free interval/density bound when one direction in the same-sign spectral plane has essentially all of its coefficient energy on original coordinates that also carry the third spectral line, uniformly as those line coefficients tend to zero.

The stress family above shows why deleting/conditioning the mixed support cannot be stable. The next estimate must retain product-linear provenance inside the two-sheet/reciprocal-shear trace rather than relaxing to an arbitrary projected joint density or treating small overlap coefficients as a small random perturbation.

For higher-rank matrices in the owner's full target, extra spectral leakage remains after choosing a three-dimensional active eigenspace; this report does not pay that debt.

## 8. Status

- `QFORM-SAMESIGN-PLANE-OVERLAP-GRAM-EXIT-v1`: **PROVED**.
- Assigned partner `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1`: **ACTUALLY USED** in (2.1), (3.6).
- Newest partner `QFORM-RULED-ONESHEET-ROUGH-INTERVAL-v1`: **ACTUALLY APPLIED** in (6.1)-(6.2).
- Full QFORM: **OPEN**.
- Continuous density for the full target: **NOT PROVED**.
- No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis independence, or post-rotation independence assumption was used.
