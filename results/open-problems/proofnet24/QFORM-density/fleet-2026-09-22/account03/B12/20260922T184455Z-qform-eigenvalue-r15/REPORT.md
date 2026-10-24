SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B12, 2026-09-22T18:44:55Z.
attacking: additional-eigenvalue control after scalar-rest conditioning fails; derive and apply the account04/B12 endpoint-Schur stability mechanism, retaining scalar-level-set averaging rather than a worst-fiber supremum.

# account03/B12 — additional-eigenvalue control: worst scalar fibers can blow up while endpoint Schur stability improves

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `account03/B12`  
**Run:** `20260922T184455Z-qform-eigenvalue-r15`  
**Assignment:** Additional eigenvalue control  
**Status:** `PROVED_SUPPORTING_REDUCTION / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Fresh state and scope

The run began from `yspennstate/math-research-brain` main commit `8b8965c357c28044bd9450f9c568114c5dc5b849`, owner control revision `2026-09-22.11`, and was refreshed during the run. The full target is unchanged: independent cap-one coordinate densities and a real symmetric matrix with at least three eigenvalues of modulus at least one, with one dimension-free density constant.

The owner message proposed the sufficient scalar-conditioning interface

\[
M:=\sup_b\|p_{Q_3\mid Q'=b}\|_\infty.
\]

Before publication, account03/B14 independently produced a target-valid refutation of a universal bound on this `M` (`20260922T183537Z-account03-B14-QFORM-r16`). I therefore do **not** claim the scalar-fiber refutation below as a new fleet correction. I keep it because it is an especially transparent spectral/cube model that exposes exactly how an added eigenvalue creates bad fibers, and because the same model admits a direct application of the assigned partner account04/B12 theorem.

No pointwise van-der-Corput decay, rotated-coordinate independence, fiber-sup integration over many dimensions, Gaussianity, log-concavity, compact-support reduction, or Monte Carlo inference is used.

## 2. Exact spectral cube model: the worst scalar conditional core density is infinite

Let

\[
v=\frac12(1,1,1,1)^T,
\]

and let `U` be any `4 x 3` matrix whose columns form an orthonormal basis of `v^perp`. Fix

\[
\Lambda=\operatorname{diag}(1,3/2,2),\qquad \mu=-1/2,
\]

and define

\[
A=U\Lambda U^T+\mu vv^T.
\]

Then the spectrum of `A` is exactly

\[
\{2,3/2,1,-1/2\},
\]

so this matrix has exactly three eigenvalues of modulus at least one. Let `X_1,...,X_4` be iid `Unif[0,1]`. Put

\[
Q_3=X^TU\Lambda U^TX,\qquad Q'=\mu(v^TX)^2.
\]

Set `Z_i=1-X_i`, `S=sum_i Z_i`. Since

\[
v^TX=2-S/2,
\]

the map `S -> Q'` is one-to-one on `0<S<4` (away from the harmless endpoint derivative degeneracy). For `0<s<1`, conditioning on `S=s` makes

\[
q:=Z/s
\]

uniform on the standard 3-simplex, i.e. `Dirichlet(1,1,1,1)`. Because `U^T 1=0`,

\[
U^TX=-U^TZ=-sU^Tq,
\]

and hence

\[
Q_3\mid\{S=s\}=s^2T,\qquad
T:=(U^Tq)^T\Lambda(U^Tq).
\tag{2.1}
\]

The law of `T` is absolutely continuous. Indeed, on the affine three-dimensional simplex it is a positive-definite quadratic form centered at the barycenter; its only critical point is the barycenter, a null set, so the coarea formula supplies a density `h`.

Moreover `0<=T<=lambda_max=2` (the sharper bound `T<=3lambda_max/4` is used below). Since `h` integrates to one over an interval of length at most two,

\[
\|h\|_\infty\ge 1/2.
\]

Scaling (2.1) therefore gives

\[
\boxed{
\|p_{Q_3\mid S=s}\|_\infty
=s^{-2}\|h\|_\infty
\ge \frac1{2s^2}
}
\qquad(0<s<1).
\tag{2.2}
\]

Because `Q'=mu(2-s/2)^2` determines `s`, the same estimate holds on the corresponding ordinary scalar remainder fibers. As `s downarrow 0` (equivalently `b=Q' -> 4mu=-2` through an interval of positive `Q'`-measure),

\[
\boxed{
\operatorname*{ess\,sup}_b
\|p_{Q_3\mid Q'=b}\|_\infty=\infty.
}
\tag{2.3}
\]

Thus an added spectral direction can make the worst scalar conditional core density arbitrarily bad even in an exact-three-large-eigenvalue instance. This does **not** refute QFORM and, by the B14 report cited above, is now an independently corroborated obstruction rather than a new fleet-level correction.

## 3. The lost quantity is endpoint rarity: an averaged cap stays finite

The exact mixture identity only requires

\[
p_Q(y)=\mathbb E\big[p_{Q_3\mid Q'}(y-Q')\big],
\]

so a strictly weaker sufficient estimate is

\[
\|p_Q\|_\infty
\le \mathbb E\|p_{Q_3\mid Q'}\|_\infty,
\tag{3.1}
\]

not the worst-fiber supremum.

For the cube model we can quantify the compensation on the entire singular endpoint layer `0<S<1`. Relative to Euclidean volume on the affine hyperplane `sum q_i=1`, the Dirichlet(1,1,1,1) density is `3`. Under the isometry `x=U^Tq`,

\[
h(t)
\le 3\int_{\mathbb R^3}\delta(t-x^T\Lambda x)\,dx
=\frac{6\pi\sqrt t}{\sqrt{\det\Lambda}}.
\]

Since the simplex lies at Euclidean distance at most `sqrt(3)/2` from its barycenter,

\[
t\le \frac34\lambda_{\max},
\]

and therefore

\[
H_\Lambda:=\|h\|_\infty
\le
\frac{3\pi\sqrt{3\lambda_{\max}}}{\sqrt{\det\Lambda}}.
\tag{3.2}
\]

For `Lambda=diag(1,3/2,2)`, this is

\[
H_\Lambda\le 3\pi\sqrt2.
\]

On `0<s<1`, the Irwin-Hall density of `S=sum_i(1-X_i)` is exactly `s^3/6`. Hence

\[
\begin{aligned}
\mathbb E\left[
\|p_{Q_3\mid Q'}\|_\infty;\,S<1
\right]
&=\int_0^1 s^{-2}H_\Lambda\,\frac{s^3}{6}\,ds\\
&=\frac{H_\Lambda}{12}
\le \boxed{\frac{\pi\sqrt2}{4}}.
\end{aligned}
\tag{3.3}
\]

So the `s^{-2}` conditional-density blow-up is exactly overpaid by the `s^3` scarcity of the scalar level near the cube corner. This is the quantitative reason `sup_b` is too destructive: it throws away the scalar-level weight before smoothing.

Equation (3.3) is only a theorem for this explicit model; it is not asserted as the universal missing inequality. It identifies a replacement interface that remains plausible: **mass-weighted scalar conditioning / aggregate before supremum**.

## 4. Apply the completed account04/B12 additional-eigenvalue theorem to the same geometry

Completed partner result actually consumed:

- `account04/B12`, run `20260922T181535Z-account04-B12-endpoint-tail-r1`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260922T181535Z-account04-B12-endpoint-tail-r1/REPORT.md`;
- theorem: for `A_tau=A_0+tau vv^T`, an original-coordinate pivot gives

\[
\operatorname{Sc}_i(A_\tau)
=S_\infty-a_\tau^{-1}zz^T,
\]

and if a physical residual triple of `sigma S_infty` has second eigenvalue at least `L`, while `sigma a_tau<0`, then with zero additional tail

\[
\|p_{X^TA_\tau X}\|_\infty
\le 2\sqrt{\frac{C_*}{L|a_\tau|}},
\qquad C_*=24.183038289961516\ldots.
\tag{4.1}
\]

Now take the especially transparent added-eigenvalue family

\[
A_0=P_{v^\perp}=I-vv^T,
\qquad
A_\tau=P_{v^\perp}+\tau vv^T.
\tag{4.2}
\]

Its spectrum is `{1,1,1,tau}`. Split on physical coordinate 1. Then

\[
\alpha=3/4,\quad
b=(-1/4,-1/4,-1/4)^T,\quad
C=I_3-\frac14J_3,
\]

and

\[
u=1/2,\qquad w=(1/2,1/2,1/2)^T.
\]

The partner endpoint matrix is exactly

\[
\begin{aligned}
S_\infty
&=C-\frac{bw^T+wb^T}{u}+\frac{\alpha}{u^2}ww^T\\
&=I_3+J_3,
\end{aligned}
\tag{4.3}
\]

whose eigenvalues are `(4,1,1)`. Thus `L=1` and `sigma=+1`. For `tau=-T` with `T>3`,

\[
a_\tau=\frac34-\frac T4=-\frac{T-3}{4}<0.
\]

Applying the partner theorem (4.1) gives the concrete added-eigenvalue estimate

\[
\boxed{
\|p_{X^TA_{-T}X}\|_\infty
\le
4\sqrt{\frac{C_*}{T-3}}
=
\frac{19.6705010774\ldots}{\sqrt{T-3}}
}
\qquad(T>3).
\tag{4.4}
\]

For example at `T=6`, the bound is `<11.357`. As the magnitude of the extra opposite-sign eigenvalue tends to infinity, the certified density bound **improves** like `T^{-1/2}`.

At the same time, for iid `Unif[0,1]` inputs the scalar split

\[
Q_3=X^TP_{v^\perp}X,\qquad Q'=-T(v^TX)^2
\]

has the same `s^{-2}` worst-fiber explosion as Section 2. Hence (4.4) proves a sharp mechanism separation on one and the same family:

> the added eigenvalue is not the problem; taking a worst conditional spectral fiber is the problem.

This is a genuine use of the assigned account04/B12 result in an actual inequality, not a citation-only handoff.

## 5. Endpoint compression identity behind the partner application

The previous calculation is a special case of a useful exact identity. Suppose `A_0 v=0`, write `v=(u,w)` with `u!=0` relative to one original coordinate, and write

\[
A_0=\begin{pmatrix}\alpha&b^T\\b&C\end{pmatrix}.
\]

Define

\[
R y=\left(-\frac{w^Ty}{u},\,y\right).
\]

Then `Ry` lies in `v^perp`, and direct expansion gives

\[
\boxed{S_\infty=R^TA_0R.}
\tag{5.1}
\]

Consequently, if on `v^perp`

\[
A_0\succeq L P_{v^\perp},
\]

then

\[
S_\infty\succeq L R^TR
=L\left(I+\frac{ww^T}{u^2}\right)
\succeq LI.
\tag{5.2}
\]

Thus for a positive core with a kernel along the added eigendirection, the endpoint spectral reserve needed by the account04/B12 theorem is automatic in original-coordinate Schur geometry. No rotation of the independent inputs is used. The remaining prices are the physical pivot overlap `u`, the sign of the added spike, and any genuinely nonseparable tail in the partner theorem.

This identity is useful as a reduction but does not solve the full conjecture, because a general three-large-eigenvalue matrix need not split into a positive codimension-one core plus one spike with a universally favorable physical coordinate.

## 6. What is proved, what is not, and the replacement obligation

**Proved here:**

1. In a target-valid exact-three-large-eigenvalue cube model, worst scalar spectral conditioning has essential supremum infinity, with explicit `s^{-2}` blow-up.
2. On the same endpoint layer, the mass-weighted conditional cap is finite and explicitly at most `pi sqrt(2)/4` for the chosen core.
3. Applying the completed account04/B12 endpoint theorem to `P_{v^perp}-T vv^T` gives the explicit full-output bound (4.4), decaying like the inverse square root of the added eigenvalue magnitude.
4. The endpoint Schur matrix has the exact compression representation (5.1), giving the monotone reserve (5.2).

**Not proved:** the universal QFORM conjecture. The scalar-conditioning `sup_b` route was already refuted concurrently by account03/B14 and is not revived. A universal bound on the **mass-weighted** scalar conditional cap is also not proved here.

**Continuity:** this report proves `L^infinity` density bounds in the stated partner-controlled branch. It does not independently prove continuity. The shared state records a separate rank-at-least-three regularity theorem; that theorem, not the Schur estimate itself, is the source for continuity where its hypotheses are invoked.

**Next target-level obligation for B12:** replace worst-fiber scalar conditioning by an aggregate-before-supremum inequality stable under arbitrary added spectrum, or show how the endpoint-Schur branch and grouped original-coordinate bank branches exhaust the matrices left after the exact-three core reduction. The critical requirement is to keep the scalar-level-set weight (or an equivalent original-product mass budget) until after the curvature payment.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.
