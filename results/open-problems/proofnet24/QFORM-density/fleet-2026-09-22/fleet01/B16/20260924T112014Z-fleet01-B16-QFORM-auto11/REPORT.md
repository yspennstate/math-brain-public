# fleet01/B16 — product-projection discriminant transducer for a nonzero separated-scalar pivot

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T112014Z-fleet01-B16-QFORM-auto11`  
Role: Projection-product interaction  
Status: **NEW SUPPORTING THEOREM / STRICT TARGET APPLICATIONS / FULL QFORM OPEN**  
Full-target continuity: **OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The previous B16 run paid every invertible **zero separated-scalar pivot** carrier

\[
B=\begin{pmatrix}C&d\\ d^T&0\end{pmatrix}
\]

when the first two statistics form a genuinely dependent two-dimensional product projection and the last statistic is source-disjoint. The newest completed fleet02/B16 result independently gives a determinant-homogeneous version of the same zero-pivot mechanism and proves that a bounded joint pair density plus a bounded independent scalar density does **not** suffice when the separated scalar has its own nonzero square.

The first unpaid implication was therefore:

`QFORM-SHAREDBANK-NONZERO-SCALARPIVOT-PRODUCTTRANSDUCER-v1`.

This run proves a sign-free quantitative transducer for every **nonzero** scalar pivot by retaining the full product provenance of the dependent pair inside the quadratic discriminant. It does not yet make the estimate uniform as that pivot tends to zero.

## 2. Source-pinned inputs actually used

All original physical inputs are independent and have scalar densities at most one. No moments, support bounds, log-concavity, smoothness, identical-law assumption, diagonal-basis independence, or post-rotation independence are introduced.

The proved rank-two fractional input is source-pinned at

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an orthonormal two-frame `U`, invertible symmetric `Lambda`, and arbitrary original-coordinate affine term `b`, it proves

\[
\sup_w \mathbb E\left| (U^TX)^T\Lambda(U^TX)+b^TX-w\right|^{-1/2}
\le 128 |\det\Lambda|^{-1/4}.
\]

When the affine term lies in `range(U)`, the same report gives the sharper constant

\[
16\sqrt{30}\,|\det\Lambda|^{-1/4}.
\]

The actual bounded-density projection input is source-pinned at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For a full-rank two-column coefficient matrix `R` with Gram `G=R^TR`, and a scalar coefficient vector `v`, it gives

\[
\|p_{R^TX}\|_\infty\le 2(\det G)^{-1/2},\qquad
\|p_{v^TX}\|_\infty\le \sqrt2/\|v\|_2.
\]

No independence between the two coordinates of `R^TX` is inferred.

The prior definite-discriminant receiver used in the positive-sign branch is source-pinned at

`yspennstate/math-open-problems@407fb7555d24b85565afbce0caea98bdad914c08`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/fleet01-B16-20260923T234226Z-auto11/REPORT.md`.

The newest completed designated partner is fleet02/B16 at

`yspennstate/math-open-problems@db3f2d55cd1c6ed9860bc92f6cd4101d8c3daa8d`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/B16-20260924T093003Z-auto11/REPORT.md`.

Its theorem `QFORM-DEPENDENTPAIR-NULLSCALAR-DETERMINANT-v1` is applied literally in Section 7.

## 3. Main theorem: product-pair discriminant half-Riesz transducer

Let `X=(X_i)_{i in I}` be one original product bank and let

\[
Z=R^TX\in\mathbb R^2,
\qquad R\in\mathbb R^{|I|\times2},
\qquad G=R^TR>0.
\]

Let `V` be a scalar random variable independent of the entire bank `X`, with density bounded by `N`. Let

\[
B=\begin{pmatrix}C&\ell\\ \ell^T&c\end{pmatrix},
\qquad C=C^T\in\mathbb R^{2\times2},
\qquad c\ne0,
\qquad \det B\ne0,
\]

and allow arbitrary affine coefficients `p in R^2`, `q,r in R`. Put

\[
Q=Z^TCZ+2V\ell^TZ+cV^2+p^TZ+qV+r.
\]

### Theorem 3.1 — `QFORM-PRODUCTPAIR-NONZERO-SCALARPIVOT-HALFRIESZ-v1`

The law of `Q` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le 16\sqrt{30}\,N
\bigl(|c\det B|\det G\bigr)^{-1/4}.
}
\tag{3.1}
\]

The estimate is valid for **both signs** of `c det B`. In particular it covers the hyperbolic-discriminant sign where a joint projected density cap alone is insufficient.

If an additional arbitrary original-coordinate linear term `b^TX` is inserted in the first bank, not necessarily lying in `range(R)`, the same proof gives the correction-safe fallback

\[
\boxed{
\|p_Q\|_\infty
\le 128\,N
\bigl(|c\det B|\det G\bigr)^{-1/4}.
}
\tag{3.2}
\]

No continuity claim is made by this argument.

### Proof

Fix the first bank `X=x`. Write

\[
d(x)=\ell^T Z(x)+q/2,
\qquad
e(x)=Z(x)^TCZ(x)+p^TZ(x)+r.
\]

Conditionally on `X=x`,

\[
Q=cV^2+2d(x)V+e(x).
\]

For a target level `y`, define the half-discriminant

\[
D_y(x)=d(x)^2-c(e(x)-y).
\tag{3.3}
\]

When `D_y(x)>0`, the two real roots have Jacobian magnitudes

\[
|2(cV+d(x))|=2\sqrt{D_y(x)}.
\]

Since the density of `V` is at most `N`, the conditional output density therefore satisfies

\[
p_{Q\mid X=x}(y)
\le N\,D_y(x)^{-1/2}{\bf1}_{\{D_y(x)>0\}}
\le N|D_y(x)|^{-1/2}.
\tag{3.4}
\]

Averaging gives

\[
p_Q(y)\le N\,\mathbb E|D_y(X)|^{-1/2}.
\tag{3.5}
\]

Now expand the discriminant as a quadratic form in the **actual product projection** `Z`:

\[
D_y(Z)
=Z^TKZ+m^TZ+\kappa_y,
\qquad
K=\ell\ell^T-cC.
\tag{3.6}
\]

The determinant is exact:

\[
\boxed{\det K=c\det B.}
\tag{3.7}
\]

Indeed, since `c!=0`,

\[
\det B=c\det(C-\ell\ell^T/c),
\qquad
K=-c(C-\ell\ell^T/c),
\]

and the latter is two-dimensional.

Take a thin QR factorization

\[
R=UT,
\qquad U^TU=I_2,
\qquad T\in GL_2(\mathbb R).
\]

Then

\[
Z=T^TU^TX,
\]

so the quadratic matrix seen by the orthonormal projection `U^TX` is

\[
\Lambda=TKT^T.
\]

Its determinant is

\[
|\det\Lambda|
=|\det K|\det(T^TT)
=|c\det B|\det G.
\tag{3.8}
\]

The affine term in (3.6) is a linear function of `Z`, hence its original-coordinate coefficient lies in `range(U)`. The source-pinned in-range rank-two affine half-Riesz theorem therefore yields, uniformly in `y`,

\[
\mathbb E|D_y(X)|^{-1/2}
\le16\sqrt{30}
\bigl(|c\det B|\det G\bigr)^{-1/4}.
\tag{3.9}
\]

Combining (3.5) and (3.9) proves (3.1). If an arbitrary extra first-bank affine term is present, the discriminant acquires an arbitrary original-coordinate affine term; use the `128` version of the same rank-two theorem to obtain (3.2). The uniform finite majorant in (3.5) also supplies absolute continuity by Fubini from the conditional scalar densities. QED.

### Why this is correction-safe

The proof never inserts a bounded joint projected density into an indefinite level-set integral. On the bad sign, the discriminant matrix `K` is indefinite and its planar shells have infinite-area arms; the prior cap-only coarea route is therefore invalid. Here the expectation of the hyperbolic half-Riesz kernel is controlled **before product provenance is discarded**, by the rank-two theorem on the original independent bank.

## 4. Sign synthesis with the actual projection theorem

When

\[
c\det B>0,
\]

the discriminant matrix `K` is definite. The previously proved conditional minority-sign theorem can then spend only the genuine two-dimensional projection cap

\[
M\le2(\det G)^{-1/2}
\]

and gives the sharper estimate

\[
\boxed{
\|p_Q\|_\infty
\le 2\sqrt{2\pi}\,N
(c\det B\det G)^{-1/4}.
}
\tag{4.1}
\]

When

\[
c\det B<0,
\]

the definite-shell mechanism is unavailable, but Theorem 3.1 gives

\[
\boxed{
\|p_Q\|_\infty
\le16\sqrt{30}\,N
(|c\det B|\det G)^{-1/4}.
}
\tag{4.2}
\]

Thus the source-valid receiver is now sign-free for every nonzero separated-scalar pivot. The two signs use different information for a reason: joint projection height is sufficient on definite discriminant shells, while the hyperbolic sign requires the retained product half-Riesz theorem.

## 5. Scalar projection corollary and exact-rank-three geometry

Now let the source-disjoint scalar itself be an actual projection

\[
V=v^TY,
\qquad \tau=\|v\|_2>0,
\]

of a second cap-one product bank. The scalar projection theorem gives

\[
N\le\sqrt2/\tau.
\]

Hence (4.1)-(4.2) become

\[
\|p_Q\|_\infty
\le
\begin{cases}
4\sqrt\pi\,\tau^{-1}(c\det B\det G)^{-1/4},&c\det B>0,\\[3pt]
16\sqrt{60}\,\tau^{-1}(|c\det B|\det G)^{-1/4},&c\det B<0.
\end{cases}
\tag{5.1}
\]

In particular the sign-free envelope is

\[
\boxed{
\|p_Q\|_\infty
\le16\sqrt{60}\,\tau^{-1}
(|c\det B|\det G)^{-1/4}.
}
\tag{5.2}
\]

Embed the two banks on disjoint original-coordinate supports and set

\[
T_{\rm phys}=[R,v],
\qquad
A=T_{\rm phys}BT_{\rm phys}^T.
\]

Then

\[
T_{\rm phys}^TT_{\rm phys}=\operatorname{diag}(G,\tau^2),
\]

and the product of the three nonzero eigenvalues is

\[
\operatorname{pdet}A=\det B\det G\,\tau^2.
\tag{5.3}
\]

The scalar pivot in the **normalized physical scalar direction** is

\[
a_V=c\tau^2.
\tag{5.4}
\]

Therefore (5.2) is exactly

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le16\sqrt{60}
\bigl(|a_V|\,|\operatorname{pdet}A|\bigr)^{-1/4}.
}
\tag{5.5}
\]

On an exact-rank-three owner-target form, `|pdet A|>=1`; consequently every such source-separated packet with `|a_V|>=eta>0` obeys

\[
\|p_{X^TAX}\|_\infty\le16\sqrt{60}\,\eta^{-1/4}.
\tag{5.6}
\]

The unresolved issue is precisely uniformity as `a_V ->0`, not either discriminant sign at fixed nonzero pivot.

## 6. Strict target on the hyperbolic sign: the caps-only obstruction is paid by product provenance

Take an orthonormal two-dimensional projection `(S,U)` of one arbitrary cap-one product bank and one genuinely independent **physical** cap-one input `V`. Consider

\[
Q_*=S^2-U^2+V^2.
\tag{6.1}
\]

The three-scalar carrier is

\[
B_*=\operatorname{diag}(1,-1,1),
\qquad
\operatorname{spec}(B_*)=\{-1,1,1\}.
\]

Thus this is exactly on the owner target. Moreover

\[
c\det B_*=-1<0,
\]

so the definite-discriminant theorem does not apply. The fresh fleet02/B16 caps-only obstruction is modeled on precisely this hyperbolic structure: an arbitrary bounded joint pair can make `S^2-U^2` almost flat on a tiny interval and cause `S^2-U^2+V^2` to have arbitrarily large height.

But for a **genuine product projection**, Theorem 3.1 applies with `G=I_2` and `N<=1`, giving

\[
\boxed{
\|p_{S^2-U^2+V^2}\|_\infty
\le16\sqrt{30}
=87.6356092008\ldots .
}
\tag{6.2}
\]

If `V` is instead a normalized scalar projection of a disjoint product bank, the actual scalar projection theorem gives the still-universal

\[
\|p_Q\|_\infty\le16\sqrt{60}=123.9354670786\ldots .
\]

This is the main projection-product interaction gained in this run: the exact caps-only counterexample carrier becomes bounded once the missing original-product provenance of the dependent pair is restored and spent through the half-Riesz transducer.

## 7. Completed designated partner applied to an actual strict-target inequality

Use the newest completed fleet02/B16 theorem

`QFORM-DEPENDENTPAIR-NULLSCALAR-DETERMINANT-v1`:

if a dependent pair has joint density cap `M`, an independent scalar has cap `N`, and

\[
B=\begin{pmatrix}C&\ell\\\ell^T&0\end{pmatrix},
\]

then

\[
\|p_Q\|_\infty\le6(MN)^{2/3}|\det B|^{-1/3}.
\]

Let `(S,U)` be an orthonormal two-dimensional projection of one cap-one product bank and `V` a normalized scalar projection of a disjoint cap-one product bank. The actual projection theorem gives

\[
M\le2,\qquad N\le\sqrt2.
\]

Take

\[
Q_{\rm partner}=-4S^2+4U^2+8UV.
\tag{7.1}
\]

Its carrier is

\[
B_p=
\begin{pmatrix}
-4&0&0\\
0&4&4\\
0&4&0
\end{pmatrix},
\qquad
\det B_p=64,
\]

with exact spectrum

\[
\operatorname{spec}(B_p)
=\{-4,\,2-2\sqrt5,\,2+2\sqrt5\}.
\]

All three eigenvalues have modulus greater than one, so this is a literal owner-target inequality. The completed partner theorem gives

\[
\boxed{
\|p_{Q_{\rm partner}}\|_\infty
\le6(2\sqrt2)^{2/3}64^{-1/3}=3.
}
\tag{7.2}
\]

No independence between `S` and `U` is used.

## 8. Corrections preserved

This run preserves all live corrections:

- arbitrary-joint rank-three/indefinite coarea is false;
- coordinates of a product projection are generally dependent;
- worst conditional projected-density caps are unavailable;
- positive-measure fiberwise indefinite traces can diverge even when the final product output is bounded;
- source-dependent shears cannot be followed by an unmasked factorization;
- small coefficients cannot be treated as small random perturbations under arbitrary unbounded laws.

The new theorem specifically avoids the first four: on the hyperbolic sign the discriminant is not integrated against the planar joint density at all. It is sent back to the original product bank and controlled by the source-pinned rank-two half-Riesz theorem.

## 9. Remaining implication

The nonzero separated-scalar pivot is now paid for both discriminant signs, but the estimate has the singular factor

\[
|a_V|^{-1/4}.
\]

The exact zero-pivot endpoint is independently paid by the previous B16 theorem and the newest fleet02/B16 determinant theorem. Therefore the first unpaid implication is now

`QFORM-SHAREDBANK-SMALL-NONZERO-SCALARPIVOT-BRIDGE-v1`:

> obtain a bound uniform as the normalized source-separated scalar pivot tends to zero, without treating `a_V V^2` as a small random perturbation and without replacing the product-projection pair by an arbitrary joint density.

The fresh fleet02/B16 counterexample explains why the bridge cannot be caps-only. A successful bridge must spend additional original-product provenance before absolute values, or produce a source-valid repartition with a quantitatively nondegenerate pivot/cross-volume currency.

The unrestricted QFORM theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.
