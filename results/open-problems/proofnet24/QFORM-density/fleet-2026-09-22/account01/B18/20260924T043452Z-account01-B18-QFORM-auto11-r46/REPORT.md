SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-24T04:34:52Z.
attacking: fuse the source-valid rank-two zero-self cross-bank theorem with account02/B18's new private-square receiver, producing an exact spectral dichotomy for product-separated cross-plus-square cores.

# account01/B18 r46 — cross-rank / private-square spectral fusion

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: literature-to-proof transfer  
Status: **PROVED SUPPORTING TARGET-LEVEL SYNTHESIS / EXACT TARGET FAMILY CLOSED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

## 1. Result in one line

For a retained ORIGINAL-coordinate pattern consisting of a zero-self bank `I`, an arbitrary opposite bank `J`, and one original scalar square coordinate `w` which has no `I-w` edge, let

- `B=A[I,J]`, with singular values `sigma_1>=sigma_2>=...`;
- `a=A_ww`.

After conditioning arbitrary outside original coordinates, all `J-J` curvature and all `J-w` coupling may remain. Then

\[
\boxed{
\|p_Q\|_\infty
\le
\min\left\{
{2\sqrt\pi\over\sqrt{\sigma_1\sigma_2}},
{4\sqrt2\over\sqrt{|a|\sigma_1}}
\right\},
}
\tag{1.1}
\]

where the first entry is used only when `rank B>=2`, and the second only when `a!=0` and `B!=0`.

The first inequality is an **exact prior account02/B18 result**, rechecked against the primary Livshyts--Paouris--Pivovarov theorem; I make no novelty claim for it. The second is a literal application of the **latest completed account02/B18 theorem**, including its sharper singleton-square constant. The new content of this report is the source-matched synthesis, its physical-currency corollary, and the exact target-valid interpolation family below.

A useful immediate currency form is

\[
\boxed{
\max\{\sigma_1\sigma_2,\ |a|\sigma_1\}\ge1
\quad\Longrightarrow\quad
\|p_Q\|_\infty\le4\sqrt2<5.657.
}
\tag{1.2}
\]

This keeps a nonzero near-rank-one crossing tail exactly; no small singular direction is discarded.

## 2. Exact retained pattern and ambient conditioning

Let the original coordinates be partitioned as

\[
I\sqcup J\sqcup\{w\}\sqcup K.
\]

Assume on the retained principal block `I union J union {w}` that

\[
A_{II}=0,\qquad A_{Iw}=0.
\tag{2.1}
\]

No restriction is placed on

\[
A_{JJ},\qquad A_{Jw},\qquad A_{ww}=a.
\]

Write

\[
B=A_{IJ},\qquad h=A_{Jw}.
\]

Condition the outside ORIGINAL coordinates `X_K=y`. Independence of the original coordinates means the retained variables remain mutually independent with their original cap-one densities. The conditional polynomial is exactly

\[
\begin{aligned}
Q_y={}&2X_I^TBX_J+\ell_y^TX_I+G_y(X_J)\\
&+aW^2+\bigl(2h^TX_J+d_y\bigr)W+c_y,
\end{aligned}
\tag{2.2}
\]

where `W=X_w`, `G_y` is an arbitrary quadratic-affine function of `X_J`, and `ell_y,d_y,c_y` are deterministic after the conditioning.

Thus every estimate below is uniform in the outside value `y`, so averaging conditional laws yields the same essential-density estimate for the full ambient form. This conditioning is product-valid: it never conditions on a rotated projection.

## 3. Primary source and exact hypothesis match

The external projection theorem used in the rank-two branch is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949, Theorem 1.1. If

\[
f(x)=\prod_{j=1}^n f_j(x_j),\qquad \|f_j\|_\infty\le1,
\]

then every `k`-dimensional orthogonal marginal has density at most `2^{k/2}`. There are no moment, iid, compact-support, centering, symmetry, smoothness, or log-concavity assumptions.

The scalar linear-form cap used in the partner theorem is also source-valid under the present assumptions. Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492, Theorem 1.2, gives

\[
\|p_{v^TX}\|_\infty\le{\sqrt2\over\|v\|_2}
\tag{3.1}
\]

for a genuine original-coordinate product bank with one-dimensional densities bounded by one. Again no moments or iid assumption are imposed.

The present proof uses these theorems only on genuine original-coordinate product banks. Orthogonal projections are used for density caps only; their coordinates are never declared independent.

## 4. First exit: rank-two zero-self cross smoothing — exact prior result

The source-pinned prior account02/B18 theorem is

- `QFORM-ZEROBLOCK-CROSSRANK2PLUS-v1`;
- `math-open-problems@27627ef9d4fdc75d875861033dcd31c1cb47a386`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260922T230222Z-account02-B18-r11/REPORT.md`.

Its hypotheses match (2.2) after grouping the entire opposite side as `(X_J,W)`. The cross matrix from `I` to `(J,w)` is simply

\[
[B\ \ 0],
\]

so its nonzero singular values are those of `B`; all `J-J`, `J-w`, and `w-w` curvature is allowed as arbitrary opposite-bank curvature.

If `rank B>=2`, the theorem therefore gives

\[
\boxed{
\|p_Q\|_\infty
\le {2\sqrt\pi\over\sqrt{\sigma_1\sigma_2}}.
}
\tag{4.1}
\]

For completeness, its source-valid mechanism is: LPP bounds the density of the rank-two cross image of `X_J`; conditioning that bank leaves a genuine original-product linear form in `X_I`; the reciprocal norm of its random coefficient is integrable in two dimensions. No pointwise quadratic Fourier decay or arbitrary-joint coarea is used.

If in addition `|I|=2` and `rank B=2`, the same prior report proves the sharper physical two-pivot estimate

\[
\boxed{
\|p_Q\|_\infty
\le {2\sqrt2\over\sqrt{\sigma_1\sigma_2}}.
}
\tag{4.2}
\]

I am not claiming novelty for (4.1) or (4.2).

## 5. Second exit: latest account02/B18 private-square theorem

The latest completed designated-partner report used here is

- account02/B18 run `account02-B18-20260924T031145Z-auto11`;
- canonical commit `fedbabc70c2245476d15532f38c5c2555a0d6c31`;
- theorem `QFORM-CONDITIONAL-CROSS-PRIVATEBANK-WEAKL2-v1`.

In its notation,

\[
T=X^TMY+\alpha^TX+G(Y)+aU^2+r(Y)U+c,
\tag{5.1}
\]

with three disjoint original product banks, has

\[
\|p_T\|_\infty
\le {8\sqrt2\over\|\gamma\|_2\sqrt{|a|\,\|M\|_{op}}}
\tag{5.2}
\]

when `U=gamma^T Z`. Most importantly for the present retained pattern, the partner separately records the sharper singleton case: if `U=W` is one ORIGINAL scalar coordinate of cap one, then

\[
\boxed{
\|p_T\|_\infty
\le {8\over\sqrt{|a|\,\|M\|_{op}}}.
}
\tag{5.3}
\]

It still allows an arbitrary measurable `Y`-dependent coefficient `r(Y)W`.

Apply this theorem literally to (2.2):

\[
M=2B,\qquad \|M\|_{op}=2\sigma_1,
\]

and

\[
r(X_J)=2h^TX_J+d_y.
\]

Therefore

\[
\boxed{
\|p_Q\|_\infty
\le {8\over\sqrt{2|a|\sigma_1}}
={4\sqrt2\over\sqrt{|a|\sigma_1}}.
}
\tag{5.4}
\]

This is a genuine use of the completed partner theorem at an actual inequality. The whole physical cross matrix `B` remains present in the proof. In particular, if `B` has a tiny but nonzero second singular value, (5.4) does not delete it; the partner proof conditions on `Y` and uses the full coefficient vector `2BY+ell_y`, then pays it from the top singular direction.

## 6. Combined source-preserving theorem

Equations (4.1) and (5.4) prove `QFORM-ZEROSELF-CROSS-OR-SCALAR-SQUARE-FUSION-v1`:

> Under the retained original-coordinate hypotheses (2.1), with arbitrary `J-J` curvature, arbitrary `J-w` coupling and arbitrary outside couplings after original-coordinate conditioning,
> \[
> \|p_Q\|_\infty
> \le
> \min\left\{
> {2\sqrt\pi\over\sqrt{\sigma_1\sigma_2}},
> {4\sqrt2\over\sqrt{|a|\sigma_1}}
> \right\},
> \]
> with the rank-two entry omitted when `rank B<2` and the square entry omitted when `a=0`.

Hence if

\[
\sigma_1\sigma_2\ge1,
\tag{6.1}
\]

the first exit gives

\[
\|p_Q\|_\infty\le2\sqrt\pi=3.5449077018\ldots,
\tag{6.2}
\]

whereas if

\[
|a|\sigma_1\ge1,
\tag{6.3}
\]

the partner exit gives

\[
\|p_Q\|_\infty\le4\sqrt2=5.6568542495\ldots.
\tag{6.4}
\]

This proves (1.2).

The structural debt to the full conjecture is explicit: `s_3(A)>=1` does not currently force every matrix into (2.1) with one of the two currencies (6.1)/(6.3). The result pays this packet once a product-preserving zero-self bank and a physically separate scalar-square coordinate have been exposed.

## 7. Exact target-valid transition family, uniform through the near-rank-one collar

The synthesis is useful on a family where neither ingredient alone is uniform over the parameter.

Take `|I|=2`. Let `J` be any original-coordinate bank of dimension at least two, and let `B_t:I->J` have rank exactly two and singular values

\[
\sigma_1(B_t)=1,\qquad \sigma_2(B_t)=t,
\qquad t>0.
\tag{7.1}
\]

Take one more original coordinate `W`, and on the retained principal block define

\[
Q_t=2X_I^TB_tX_J+t^{-1}W^2.
\tag{7.2}
\]

Equivalently the retained physical matrix is

\[
A_t=
\begin{pmatrix}
0&B_t&0\\
B_t^T&0&0\\
0&0&t^{-1}
\end{pmatrix}.
\tag{7.3}
\]

The cross block `[[0,B_t],[B_t^T,0]]` has nonzero eigenvalues `+-1,+-t`, and the scalar block contributes `t^{-1}`. Therefore

\[
\boxed{
\operatorname{spec}_{\ne0}(A_t)
=\{1,-1,t,-t,t^{-1}\}.
}
\tag{7.4}
\]

For every `t>0`, this retained block has at least three eigenvalues of modulus at least one:

- if `0<t<=1`, use `1,-1,t^{-1}`;
- if `t>=1`, use `1,-1,t,-t`.

Thus this is a literal family inside the owner's target. Moreover any ambient symmetric matrix containing (7.3) as an ORIGINAL-coordinate principal block remains target-valid by Cauchy interlacing; arbitrary outside coefficients/couplings may then be conditioned, producing only the affine terms already allowed above.

### 7.1 Cross-rank payment

Because `|I|=2`, use the sharper prior two-pivot estimate (4.2):

\[
\|p_{Q_t}\|_\infty
\le 2\sqrt2\,t^{-1/2}.
\tag{7.5}
\]

This is strong for large `t` but diverges as `t downarrow0`.

### 7.2 Latest-partner private-square payment

Here `a=t^{-1}` and `sigma_1=1`. Equation (5.4) gives

\[
\|p_{Q_t}\|_\infty
\le 4\sqrt2\,t^{1/2}.
\tag{7.6}
\]

This is strong in the punctured near-rank-one regime `t downarrow0`, while becoming weak for large `t`. The nonzero `t`-crossing is retained exactly.

### 7.3 Uniform splice

Combining (7.5)-(7.6),

\[
\boxed{
\|p_{Q_t}\|_\infty
\le
\min\{2\sqrt2\,t^{-1/2},\ 4\sqrt2\,t^{1/2}\}.
}
\tag{7.7}
\]

The two quantities are equal exactly at

\[
t={1\over2},
\]

where both equal `4`. Hence

\[
\boxed{
\sup_{t>0}\|p_{Q_t}\|_\infty\le4.
}
\tag{7.8}
\]

This closes a genuine target-valid interpolation through a nonzero near-rank-one cross tail. It does not use perturbative deletion or continuity in the coefficient `t`; the two exact source-valid inequalities overlap quantitatively.

## 8. Continuity tracked separately

The general fusion theorem (Section 6) is asserted as an **essential bounded-density** theorem only. The latest partner theorem deliberately does not claim continuity when the scalar-square shift coefficient `r(Y)` is an arbitrary measurable function of the shared bank, and averaging conditional continuous densities is not by itself a uniform continuity argument.

For the standalone transition family (7.2), however, continuity is easy and independent of that issue. The cross variable

\[
R_t=2X_I^TB_tX_J
\]

has an `L^1` density (indeed the prior rank-two theorem gives a bounded continuous density). The independent variable `t^{-1}W^2` has an `L^1` density. Therefore their convolution belongs to `C_0(R)`, and the representative obeys the same bound (7.8). Thus

\[
\boxed{
Q_t\text{ has a }C_0\text{ density with }\|p_{Q_t}\|_\infty\le4
\quad(t>0).
}
\tag{8.1}
\]

I do not promote this continuity statement to the arbitrary ambient conditional lift.

## 9. Prior-solution / novelty audit

I found the two analytic ingredients already proved in fleet history:

1. the rank-two zero-self cross theorem at `27627ef9d4fdc75d875861033dcd31c1cb47a386`;
2. the latest private-bank theorem at `fedbabc70c2245476d15532f38c5c2555a0d6c31`.

Accordingly I make **no novelty claim for either analytic estimate**. A targeted repository search did not locate the exact two-currency fusion (1.1) or the `spec={+-1,+-t,t^{-1}}`, uniform-constant-4 interpolation (7.8), but a search miss is not novelty evidence. The correct status is a new worker synthesis/application of source-pinned prior theorems.

I also checked the general quadratic-form regularity literature represented by Herry--Malicet--Poly, arXiv:2303.09488. Their setup assumes iid variables whose common law is a sufficiently smooth function of a Gaussian field; it therefore does not match the present arbitrary non-iid cap-one hypotheses and is not used in the proof.

## 10. Corrections explicitly preserved

- No independence is asserted after an orthogonal rotation.
- No arbitrary-joint 3D coarea theorem is used.
- No conditional density cap is reinterpreted as independence.
- No coefficient-small quadratic or bilinear tail is deleted; `sigma_2=t>0` is retained exactly in Section 7.
- No law-uniform pointwise Fresnel decay is used.
- No fixed good physical minor is inferred from the three-large-eigenvalue hypothesis.
- No moment, support, centering, iid, symmetry, smoothness or log-concavity assumption is introduced.
- The full conjecture remains OPEN.

## 11. Remaining implication

The useful next compiler target is now sharper:

`QFORM-CROSS-OR-PRIVATE-SQUARE-EXTRACTION-v1` — starting only from `s_3(A)>=1`, force an original-coordinate retained packet with `A_II=0`, `A_Iw=0` and

\[
\max\{\sigma_1(A_{IJ})\sigma_2(A_{IJ}),\ |A_{ww}|\sigma_1(A_{IJ})\}\ge c>0,
\]

or route failure into an already-paid physical-pair, grouped-hub, ridge, or product-Fourier branch.

The hard survivor is when the candidate zero-self side itself acquires nonzero curvature, or every scalar-square direction is source-entangled with that side (`A_Iw!=0`) while the cross matrix remains effectively rank one. That is exactly where neither source theorem above can be invoked without a new dependence-safe receiver.

## 12. Source pins / integrity

Fresh control read before this run: `yspennstate/math-research-brain@254f0be44d564f9c4ca360004b2e598dbb579ccd`; a later fresh `AGENTS.md` refresh at `5b7cede1c0953bb2d5c0cfbc7d98fd4d91636bf2` contained no later stop and retained exclusive full-QFORM work.

Primary literature:

- G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1.
- M. Rudelson, R. Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492, Theorem 1.2.

Partner / fleet sources:

- cross-rank prior: `math-open-problems@27627ef9d4fdc75d875861033dcd31c1cb47a386`;
- latest account02/B18 private-bank theorem: `math-open-problems@fedbabc70c2245476d15532f38c5c2555a0d6c31`.

Changed-file allowlist for this run is restricted to this immutable account01/B18 run directory and the required account01/B18 handoff/memory/run-status records. Manual review finds only abstract mathematics, public bibliographic data and repository-relative source identifiers; no credentials, scheduler IDs, machine paths, signed URLs, personal/client/company/trading material, public-release action or permission change is present.
