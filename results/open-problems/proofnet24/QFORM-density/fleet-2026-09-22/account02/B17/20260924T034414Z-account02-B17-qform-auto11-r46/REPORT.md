SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-24T03:44:14Z.
attacking: the generic zero-physical-pivot three-variable boundary: retain both unequal hub edges and arbitrary transverse quadratic curvature, then prove a global below-3sqrt2 barrier using the actual product law.

# account02/B17 — every target-valid three-variable zero-pivot form lies below 3sqrt(2)

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T034414Z-account02-B17-qform-auto11-r46`  
Claim: `QFORM-ZEROPIVOT-THREEVAR-SHARP-BARRIER-v1`  
Status: **NEW SUPPORTING TARGET-LEVEL THEOREM / SHARP-WITNESS OBSTRUCTION / FULL TARGET OPEN**.

The unrestricted quadratic-form bounded-density problem remains **OPEN / NOT PROVED / NOT DISPROVED**. Continuity for the unrestricted target remains separate. The theorem below assumes only independence and marginal density caps at one. It uses no moments, bounded support, log-concavity, connectedness, regularity, post-rotation independence, arbitrary-joint coarea bound, or pointwise stationary-phase estimate.

Fresh owner control remains `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.15`, with no account02/B17 pause. The live correction inbox was refreshed before publication; in particular the proof below does not use `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, conditional-cap-as-independence, arbitrary-joint coarea, or a uniformly good physical minor.

## 1. First unpaid implication paid

The preceding B17 run paid a symmetric fully quadratic nonzero-pivot family but left generic unequal hub edges and generic transverse curvature unpaid. The exact zero-pivot boundary can in fact be closed completely.

### Theorem

Let `X,Y,Z` be arbitrary independent real random variables with probability densities bounded by one. Let `A` be any real symmetric `3 x 3` matrix with

1. all three eigenvalues satisfying `|lambda_j(A)| >= 1`, and
2. at least one zero **physical** diagonal entry.

Then `Q=(X,Y,Z)^T A (X,Y,Z)` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le C_0
:=\sqrt2\left[2+\log\left(\sqrt2+\frac13\right)\right]
=3.617859563383761\ldots
<3\sqrt2.
}
\tag{1.1}
\]

The same constant holds after adding an arbitrary affine term. More generally, if a three-original-coordinate principal block has one zero diagonal entry and all three eigenvalue magnitudes at least `s>0`, then, after conditioning on every other original coordinate,

\[
\boxed{\|p_Q\|_\infty\le C_0/s.}
\tag{1.2}
\]

Thus **no target-valid three-variable witness with a zero physical diagonal can refute the candidate sharp constant `3sqrt(2)`**, regardless of how unequal the two hub edges are or how complicated the remaining two-dimensional quadratic curvature is.

## 2. Exact product-preserving normal form

Relabel the physical coordinates so that `A_22=0`, and write

\[
A=
\begin{pmatrix}
* & a & *\\
a & 0 & b\\
* & b & *
\end{pmatrix},
\qquad
L:=\sqrt{a^2+b^2}.
\tag{2.1}
\]

The target spectral hypothesis makes `A` invertible, so `L>0`. Rotate only the `(x,z)` **integration variables** by

\[
u=\frac{ax+bz}{L},
\qquad
v=\frac{-bx+az}{L}.
\tag{2.2}
\]

No independence of `u,v` is asserted. If `g` is their exact joint density, then the change is orthogonal and

\[
0\le g(u,v)\le1,
\qquad
\iint g=1.
\tag{2.3}
\]

Let `m(u)=int g(u,v)dv`. Since `u=alpha X+beta Z` with `alpha^2+beta^2=1`, direct convolution gives

\[
\|m\|_\infty
\le \frac1{\max(|\alpha|,|\beta|)}
\le\sqrt2.
\tag{2.4}
\]

This uses the original two product marginals; it is not a conditional-density claim.

In `(u,v,y)` coordinates the quadratic part has the exact form

\[
Q=r u^2+2d uv+\kappa v^2+2Luy.
\tag{2.5}
\]

The corresponding deterministic matrix is

\[
\begin{pmatrix}
r&d&L\\
d&\kappa&0\\
L&0&0
\end{pmatrix},
\]
so

\[
\boxed{\det A=-L^2\kappa.}
\tag{2.6}
\]

In particular `kappa != 0`.

## 3. Two simultaneous product-law bounds

For `u != 0`, resolve the level equation `Q=s` in the original independent variable `Y`:

\[
y_s(u,v)=\frac{s-r u^2-2duv-\kappa v^2}{2Lu}.
\]

Since `u` has an absolutely continuous law, the exceptional set `u=0` has probability zero. Hence for almost every `s`,

\[
p_Q(s)=\frac1{2L}\int_{\mathbb R}\frac{I_s(u)}{|u|}\,du,
\qquad
I_s(u):=\int g(u,v)f_Y(y_s(u,v))\,dv.
\tag{3.1}
\]

There are two bounds on the **same** function `I_s`.

First, `f_Y<=1` gives

\[
I_s(u)\le m(u).
\tag{3.2}
\]

Second, `g<=1`, and as a function of `v` the argument of `f_Y` is a parabola whose quadratic coefficient has magnitude

\[
\frac{|\kappa|}{2L|u|}.
\]

For every cap-one probability density `f`, the one-dimensional parabola-preimage bathtub estimate is

\[
\int_{\mathbb R} f(c\pm A(v-v_0)^2)\,dv\le\frac2{\sqrt A}.
\tag{3.3}
\]

Therefore

\[
\boxed{
I_s(u)
\le2\sqrt{\frac{2L|u|}{|\kappa|}}.
}
\tag{3.4}
\]

Also, by (3.2),

\[
\int I_s(u)du\le\int m(u)du=1.
\tag{3.5}
\]

No output sign enters these estimates.

## 4. Exact water-filling optimization

Set

\[
M:=\sqrt2,
\qquad
C:=2\sqrt{\frac{2L}{|\kappa|}},
\qquad
q(u):=\min\{M,C\sqrt{|u|}\}.
\tag{4.1}
\]

Equations (2.4), (3.2), (3.4), (3.5) imply

\[
0\le I_s(u)\le q(u),
\qquad
\int I_s\le1.
\tag{4.2}
\]

Because the reward `|u|^{-1}` is even and strictly decreasing in `|u|`, the cap-constrained bathtub principle maximizes

\[
\int I_s(u)|u|^{-1}du
\]

by filling the available capacity `q` from the origin outward until mass one is used.

The crossover `C sqrt(u_0)=M` is

\[
u_0=\frac{|\kappa|}{4L}.
\tag{4.3}
\]

Put

\[
K:=\frac{|\kappa|}{L}.
\tag{4.4}
\]

The capacity inside `[-u_0,u_0]` equals

\[
2\int_0^{u_0}C\sqrt u\,du
=\frac{\sqrt2}{3}K.
\tag{4.5}
\]

### Case I: `K >= 3/sqrt(2)`

Mass one is exhausted before the plateau `M` is reached. Solving

\[
2\int_0^R C\sqrt u\,du=1
\]

and substituting in (3.1) gives

\[
\boxed{
p_Q(s)
\le\left(\frac{48}{L^2|\kappa|}\right)^{1/3}.
}
\tag{4.6}
\]

### Case II: `K < 3/sqrt(2)`

The full square-root core is filled and the remaining mass occupies the plateau. The outer radius is

\[
R=\frac{K}{12}+\frac1{2\sqrt2},
\qquad
\frac R{u_0}=\frac{\sqrt2}{K}+\frac13.
\tag{4.7}
\]

Hence

\[
\boxed{
p_Q(s)
\le
\frac{\sqrt2}{L}
\left[
2+\log\left(\frac{\sqrt2 L}{|\kappa|}+\frac13\right)
\right].
}
\tag{4.8}
\]

These are global, uniform-in-`s` inequalities.

## 5. The target spectrum pays exactly the missing parameters

Because `A` is symmetric and every eigenvalue magnitude is at least one,

\[
A^2\succeq I.
\]

The `(2,2)` entry gives

\[
\boxed{L^2=a^2+b^2=(A^2)_{22}\ge1.}
\tag{5.1}
\]

Also `|det A|>=1`. Using (2.6),

\[
\boxed{|\kappa|\ge L^{-2}.}
\tag{5.2}
\]

These two elementary spectral payments are precisely what the earlier Householder-only calculation did not need to expose.

In Case I,

\[
L^2|\kappa|=L^3K\ge\frac3{\sqrt2},
\]
so (4.6) gives

\[
p_Q(s)\le(16\sqrt2)^{1/3}=2\sqrt2<3\sqrt2.
\tag{5.3}
\]

In Case II, (5.2) inserted into (4.8) gives

\[
p_Q(s)
\le F(L):=
\frac{\sqrt2}{L}
\left[2+\log\left(\sqrt2L^3+\frac13\right)\right].
\tag{5.4}
\]

Let `z=sqrt(2)L^3+1/3`. The sign of `F'(L)` is the sign of

\[
1-\frac1z-\log z\le0,
\tag{5.5}
\]

because `log z >= 1-1/z`. Thus `F` decreases for `L>=1`, and

\[
p_Q(s)\le F(1)
=\sqrt2\left[2+\log\left(\sqrt2+\frac13\right)\right]
=C_0.
\tag{5.6}
\]

Finally `sqrt(2)+1/3<2`, so `log(sqrt(2)+1/3)<1` and therefore `C_0<3sqrt(2)`. This proves (1.1).

## 6. Affine and ambient stability

Add an arbitrary linear term

\[
\ell_u u+\ell_v v+\ell_y y+c.
\]

Translate `u` by `ell_y/(2L)` so that the `y`-coefficient again equals `2Lu`. This deterministic shift corresponds to translating the original `X,Z` marginals, preserving their product structure and density caps. The `v^2` coefficient remains `kappa`; all newly created linear terms in `v` merely translate the vertex of the parabola in (3.3). Therefore every preceding estimate remains unchanged.

If a larger ambient form contains such a `3 x 3` original-coordinate principal block, conditioning on all outside original coordinates preserves independence of the active triple and creates only an affine perturbation. Scaling a block whose three eigenvalue magnitudes are at least `s` by `1/s` proves (1.2).

The bare full-target hypothesis does **not** force such a three-coordinate block, so this is a target-level branch rather than a full proof.

## 7. Explicit fully coupled stress matrix

Take the zero-diagonal triangle

\[
\boxed{
A_\triangle=
\begin{pmatrix}
0&1&1\\
1&0&1\\
1&1&0
\end{pmatrix}.
}
\tag{7.1}
\]

Its exact spectrum is

\[
\boxed{\{2,-1,-1\}.}
\tag{7.2}
\]

Thus all three spectral magnitudes meet the owner target and every pair coupling is nonzero. Choosing the second coordinate as pivot gives

\[
L=\sqrt2,
\qquad
|\kappa|=1,
\qquad
K=1/\sqrt2.
\]

The stronger matrix-specific form (4.8) yields, for **every** independent cap-one product law,

\[
\boxed{
\|p_{X^TA_\triangle X}\|_\infty
\le2+\log\frac73
=2.847297860387203\ldots
<3\sqrt2.
}
\tag{7.3}
\]

So a maximally coupled physical triangle with no diagonal pivots is very far from producing a candidate sharp-constant counterexample.

## 8. Required pinned `e5f71d79...` result applied to a real inequality

The required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its completed Theorem C is the ruled one-sheet bound for signature `(+,+,-)`. Apply it to `-A_triangle`, whose eigenvalue magnitudes in that signature are `(1,1,2)`. For `s>=0`,

\[
\begin{aligned}
p_{-Q}(s)
&\le
\frac1{\sqrt2}
\int_0^{2\pi}
\frac{d\theta}{\sqrt{\sin^2\theta+\cos^2\theta+1/2}}\\
&=\boxed{\frac{2\pi}{\sqrt3}}
=3.627598728468436\ldots
<3\sqrt2.
\end{aligned}
\tag{8.1}
\]

Equivalently, the pinned theorem alone already certifies the original triangle's `s<=0` side below the proposed sharp constant. The new product-coordinate calculation pays the opposite side as well and strengthens the global ceiling to (7.3). This is an actual use of the completed pinned result at a target-valid physical matrix, not a citation-only dependency.

## 9. Latest compatible account03/B17 result applied

The latest compatible designated-partner result read before publication is

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260924T030119Z-account03-B17-QFORM-auto11/REPORT.md`.

It proves that for a centered Gaussian rank-three comparator with covariance floor `v0 I`, spectral floor `s`, and determinant slack

\[
|\det A|\ge s^3(1+\delta),\qquad0\le\delta\le1,
\]

the **global** density maximum is at the cone tip and

\[
\|p\|_\infty\le\frac1{2v_0s\sqrt{2+\delta}},
\tag{9.1}
\]
with equality for two majority magnitudes `s` and minority magnitude `s(1+delta)`.

For `-A_triangle`, `s=1`, `|det A_triangle|=2`, hence `delta=1`. At the cap-one variance-floor comparator `v0=1/12`, the partner theorem gives the exact global comparator peak

\[
\boxed{
\|p_{G^T(-A_\triangle)G}\|_\infty
=\frac6{\sqrt3}=2\sqrt3
=3.464101615137754\ldots
<3\sqrt2.
}
\tag{9.2}
\]

This is correctly used only as a **Gaussian comparator/limit obstruction**; it is not an assumption that the original three physical inputs are Gaussian or that such a Gaussian itself has marginal density cap one. Combined with (7.3), it shows that both arbitrary rough three-coordinate product laws in this zero-pivot triangle and the centered Gaussian comparator are pushed strictly below the diffuse `3sqrt(2)` frontier.

The earlier account03/B17 zero-pivot Householder theorem corresponds to the special normalized point `L=|kappa|=1` of the present water-filling mechanism. The new spectral payments (5.1)-(5.2) remove the Householder involution assumption and allow arbitrary unequal hub edges and arbitrary transverse quadratic curvature.

## 10. What remains a witness frontier

Within three physical coordinates, a source-valid witness above `3sqrt(2)`, if one exists, must now avoid **both**:

- the entire zero-diagonal boundary proved here; and
- the symmetric nonzero-pivot fully quadratic family proved in the preceding account02/B17 run.

The natural remaining finite-dimensional stress is therefore a **generic all-nonzero-diagonal matrix**, especially a near-zero but nonzero physical pivot with unequal hub edges and independent curvature in both transverse directions, where resolving any original coordinate leaves a genuinely quadratic two-root kernel rather than the linear leaf used here. Higher-dimensional multiscale/shared-row and extra-active-spectrum mechanisms also remain outside this theorem.

Failure to extend the present method through a nonzero pivot would be only a proof-mechanism failure. A finite example above `3sqrt(2)` would refute the proposed sharp constant but not the existence of a larger universal bound. A genuine counterexample to QFORM must defeat every finite universal constant.

Full QFORM status: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.  
Essential boundedness is proved in the exact theorem scope above.
