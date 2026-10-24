SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B16, 2026-09-22T18:17:06Z.
attacking: the revision-2026-09-22.11 scalar-Q_rest conditional-density supremum, using a fixed four-variable product law and keeping the vanishing scalar-rest weight through the curved pushforward.

# Projection-product interaction: scalar Q_rest conditioning does not have a bounded conditional-density supremum

Run: `20260922T181706Z-account02-B16-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: account02/B16, `Projection-product interaction`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`  
Status: **proved correction to a proposed proof interface; full QFORM remains OPEN / NOT PROVED**.

Source control used for the decisive calculation: `yspennstate/math-research-brain@7bbf0e85ba7a64178299b6a7f7889dc0245468cc`, OWNER CONTROL revision `2026-09-22.11`.  
Completed designated partner applied: account03/B16 run `20260922T175342Z-account03-B16-QFORM-r14`, canonical proof `yspennstate/math-open-problems@419c351eb125b56e3e717230c09f0d03d6e3628d:proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T175342Z-account03-B16-QFORM-r14/REPORT.md`.

## 1. First unpaid implication: the literal scalar-conditioning supremum is false

The current owner message proposes the exact decomposition

\[
p_Q(y)=\mathbb E_{Q'}\,p_{Q_3\mid Q'}(y-Q')
\]

and then the sufficient estimate

\[
\|p_Q\|_\infty\le M,
\qquad
M:=\operatorname*{ess\,sup}_b\|p_{Q_3\mid Q'=b}\|_\infty.
\]

The identity is valid whenever the indicated regular conditional densities are used. The new result is that the proposed universal bound on `M` is false, even for one fixed four-variable product law and one fixed positive-definite target matrix with exactly three eigenvalues at the threshold `1`.

This is not a counterexample to QFORM. In the same example the full output density is bounded by an elementary ellipsoid-shell estimate. The failure comes exactly from normalizing a vanishing boundary fiber before paying its scalar-rest probability weight.

## 2. Fixed source-valid product law and fixed target matrix

Let

\[
X_1,X_2,X_3,X_4\stackrel{\rm iid}{\sim}{\rm Unif}[0,1].
\]

Each input density is exactly one on its support. Put

\[
v=\frac12(1,1,1,1),\qquad P=I-vv^T,
\]

and choose

\[
A=P+\frac12vv^T=I-\frac12vv^T=I-\frac18J_4.
\]

Thus, in physical coordinates,

\[
A_{ii}=\frac78,\qquad A_{ij}=-\frac18\quad(i\ne j),
\]

and its eigenvalues are

\[
\boxed{1,1,1,\frac12}.
\]

Hence this is an exact target-class matrix: it has three eigenvalues of magnitude at least one, while the fourth eigenvalue is strictly smaller than one.

Use its canonical spectral splitting

\[
Q=X^TAX=Q_3+Q',
\qquad
Q_3=\|PX\|^2,
\qquad
Q'=\frac12(v^TX)^2.
\]

The three-dimensional large-eigenvalue subspace `v^perp` is fixed by `A`; only the orthonormal basis inside it is degenerate, and `Q_3=||PX||^2` is basis-independent.

## 3. Exact boundary-fiber scaling

Write

\[
U_i=1-X_i,\qquad \tau=\sum_{i=1}^4U_i=4-\sum_{i=1}^4X_i.
\]

For `0<tau<1`, conditioning on `tau` cuts the unit cube by the simplex

\[
\{u_i\ge0:\ \sum_i u_i=\tau\}.
\]

Because the original density is constant one, the conditional law on this section is uniform in three-dimensional Hausdorff measure. Writing

\[
Z_i=U_i/\tau,
\]

we obtain a `tau`-independent uniform random point `Z` on the standard simplex

\[
\Delta_3=\{z_i\ge0:\ \sum_i z_i=1\}.
\]

Since `P(1,1,1,1)^T=0`,

\[
PX=-PU=-\tau PZ.
\]

Therefore

\[
\boxed{
Q_3\mid\tau=\tau^2T,
\qquad
T:=\|PZ\|^2=\sum_{i=1}^4Z_i^2-\frac14.
}\tag{3.1}
\]

On `Delta_3`, `1/4<=sum Z_i^2<=1`, so

\[
\boxed{0\le T\le\frac34.}\tag{3.2}
\]

The image `K=P\Delta_3` is a regular tetrahedron in the three-dimensional space `v^perp`, centered at the origin. Translation by the centroid is an isometry on the affine hyperplane `sum z_i=1`. The Euclidean three-volume of `Delta_3` is

\[
\frac{\sqrt{\det G}}{3!}=\frac{2}{6}=\frac13,
\]

where `G` is the Gram matrix of `e_1-e_4,e_2-e_4,e_3-e_4`, with determinant `4`. Thus the law of `W=PZ` has constant density `3` on `K`.

Consequently `T=|W|^2` has an ordinary density `g`. By radial coarea, for `r=sqrt(t)`,

\[
g(t)=\frac{3}{2r}\,\mathcal H^2(K\cap S_r)
\le \frac{3}{2r}(4\pi r^2)=6\pi r.
\]

Because `t<=3/4`,

\[
\boxed{\|g\|_\infty\le3\sqrt3\,\pi<\infty.}\tag{3.3}
\]

Also, since `g` integrates to one and is supported on an interval of length `3/4`,

\[
\boxed{\|g\|_\infty\ge\frac43.}\tag{3.4}
\]

Scaling (3.1) therefore gives the exact conditional-density relation

\[
\boxed{
\|p_{Q_3\mid\tau}\|_\infty
=\tau^{-2}\|g\|_\infty
\ge \frac{4}{3\tau^2}.
}\tag{3.5}
\]

## 4. Conditioning on the scalar quadratic remainder does not repair the blow-up

Set

\[
s=v^TX=\frac12\sum_iX_i=2-\frac\tau2.
\]

Then

\[
Q'=\frac12s^2=\frac{(4-\tau)^2}{8}.
\]

For `0<tau<1`, we have `3/2<s<2` and hence `9/8<Q'<2`. Since all `X_i>=0`, `s>=0`; on this interval the map `s -> Q'=s^2/2` is one-to-one. Thus conditioning on `Q'=b` is exactly the same as conditioning on the corresponding `s`, hence on the corresponding `tau`.

It follows from (3.5) that for

\[
b=\frac{(4-\tau)^2}{8},\qquad 0<\tau<1,
\]

\[
\boxed{
\|p_{Q_3\mid Q'=b}\|_\infty
=\tau^{-2}\|g\|_\infty
\ge\frac4{3\tau^2}.
}\tag{4.1}
\]

As `b` increases to `2`, equivalently `tau` decreases to zero, the right side diverges. The divergence occurs on every positive-measure neighborhood below the endpoint, so this is not an artifact of choosing versions of regular conditional densities on a null set. Therefore

\[
\boxed{
\operatorname*{ess\,sup}_{b}\|p_{Q_3\mid Q'=b}\|_\infty=\infty.
}\tag{4.2}
\]

This directly refutes the literal universal `M<infinity` scalar-conditioning bridge proposed in the revision-2026-09-22.11 owner message.

## 5. The compensating negative effect: the scalar-rest density vanishes three powers faster

For `0<tau<1`, the Irwin-Hall density of `tau=U_1+U_2+U_3+U_4` is exactly

\[
p_\tau(\tau)=\frac{\tau^3}{6}.
\]

Since `s=2-tau/2`,

\[
p_s(s)=\frac{\tau^3}{3}.
\]

For `b=s^2/2`, `db/ds=s`, so

\[
\boxed{
p_{Q'}(b)=\frac{\tau^3}{3s}.}\tag{5.1}
\]

Combining (5.1) with the exact scaled conditional density yields

\[
\boxed{
 p_{Q'}(b)\,p_{Q_3\mid Q'=b}(q)
 =\frac{\tau}{3s}\,g\!\left(\frac q{\tau^2}\right).
}\tag{5.2}
\]

This is the source-exact compensation that the normalized conditional supremum throws away:

- normalized curved peak: order `tau^(-2)`;
- scalar-rest probability density: order `tau^3`;
- unnormalized contribution entering the actual mixture: order `tau`.

Thus the dangerous conditional peak becomes *smaller*, not larger, after restoring the weight that the `sup_b` step discarded.

Equation (5.2) is the concrete application of the completed account03/B16 r14 result. That partner proved that normalized conditional projection-density moments can diverge and identified the replacement obligation: keep the unnormalized original-product fiber weight coupled to the curved payment. Here the same mechanism is quantified after the owner's attempted repair from vector conditioning to the scalar quadratic remainder `Q'`.

## 6. The full quadratic output in this same example is bounded

The correction above is not a QFORM counterexample. Indeed `A` is positive definite with

\[
\det A=\frac12,
\qquad
0\le Q\le \|X\|^2\le4.
\]

The joint density of `X` is the indicator of the unit cube. For every `t>=0`, the probability of a thin quadratic shell inside the cube is at most the full-space ellipsoid-shell volume. The sublevel ellipsoid has volume

\[
V(t)=\operatorname{vol}\{x\in\mathbb R^4:x^TAx\le t\}
=\frac{\pi^2}{2}\frac{t^2}{\sqrt{\det A}}
=\frac{\pi^2}{\sqrt2}t^2.
\]

The coarea formula gives absolute continuity because `grad Q=2Ax` vanishes only at the single point `x=0`. At almost every `t` in the support,

\[
p_Q(t)\le V'(t)=\sqrt2\,\pi^2 t\le4\sqrt2\,\pi^2.
\]

Hence

\[
\boxed{\|p_Q\|_\infty\le4\sqrt2\,\pi^2<56.}\tag{6.1}
\]

So a fixed target-class law/matrix can have a bounded full output density while the proposed scalar-conditional supremum is infinite. The loss is entirely in taking the supremum before mixing over `Q'`.

## 7. Consequence for the full proof route

**New correction:** `QFORM-SCALAR-QREST-CONDITIONAL-SUP-FALSE-v1`.

The exact identity

\[
p_Q(y)=\int p_{Q'}(b)\,p_{Q_3\mid Q'=b}(y-b)\,db
\]

remains valid. What fails is the replacement of this weighted integral by a universal bound on the normalized conditional supremum.

Any viable conditioning proof must retain at least enough of the factor `p_{Q'}(b)` (or an equivalent unnormalized original-product fiber measure) to compensate thin-fiber blow-up. In the present target-class example the compensation is exact: `tau^3` from scalar-rest mass versus `tau^{-2}` from the three-dimensional quadratic pushforward, leaving `tau`.

This strengthens, rather than conflicts with, account03/B16 r14. Their fragmented construction rules out universal positive moments of normalized conditional three-dimensional projection density. The present compact four-uniform construction shows that passing to the scalar quadratic remainder does **not** restore a bounded conditional-output supremum either.

The full arbitrary-sign, arbitrary-rank QFORM theorem remains open. The next source-valid B16 interface is therefore a **weighted scalar-conditioning / unnormalized-fiber inequality**, not `sup_b ||p_{Q3|Q'=b}||_infinity`. Such an inequality must also survive the existing pair-log, no-rotation-independence, and arbitrary-higher-rank corrections.
