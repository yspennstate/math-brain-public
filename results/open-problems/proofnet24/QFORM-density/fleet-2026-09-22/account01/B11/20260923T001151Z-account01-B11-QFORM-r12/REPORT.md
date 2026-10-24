# QFORM B11 r12 — null-ruling translation and matched minority curvature

Status: **PROVED_SUPPORTING_THEOREM / FULL TARGET OPEN**.

Run: `20260923T001151Z-account01-B11-QFORM-r12`.

Assignment: indefinite signatures `(2,1)` and `(1,2)`.  The purpose of this note is to isolate, in original-coordinate/product-preserving form, the extra curvature that is absent from the rank-two opposite-sign saddle.

## 1. Setting

Let

\[
A=RMR^T,\qquad R\in\mathbb R^{n\times 3},\quad R^TR=I_3,
\]

where `M` is real symmetric, invertible, of inertia `(2,1)` or `(1,2)`, and

\[
s:=\min_{1\le k\le 3}|\lambda_k(M)|>0.
\]

Assume throughout this theorem that the physical diagonal vanishes:

\[
A_{jj}=0\quad (1\le j\le n).
\]

Write `r_i^T` for the `i`th row of `R` and

\[
c_i:=\|r_i\|_2^2.
\]

Because `R^TR=I_3`,

\[
\operatorname{tr}M=\operatorname{tr}(RMR^T)=\operatorname{tr}A=0.
\]

Thus, in inertia `(2,1)`, the eigenvalues can be written `p,q,-(p+q)` with `p,q>0`; in inertia `(1,2)` they can be written `p+q,-p,-q`.

The latest designated-partner result used below is account02/B11, run `20260922T233948Z-account02-B11-QFORM-b35bb6c3`, canonical mathematics

`yspennstate/math-open-problems@e47740cfec219112c826613bec5785af4b96cf3f`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260922T233948Z-account02-B11-QFORM-b35bb6c3/REPORT.md`.

Its two facts used here are

\[
\max_i c_i\ge \frac{1-D_0}{3},
\tag{P1}
\]

and the existence of an original-coordinate cut `S` with

\[
\sigma_3(A[S,S^c])\ge \frac{s\sqrt{D_0}}8.
\tag{P2}
\]

Here `D_0` is the partner's disjoint Pluecker-volume mass.  No conclusion below treats repository provenance as a proof of those facts; the present theorem is conditional on their completed proof at the source just pinned.

## 2. Exact null-ruling theorem

Fix an original coordinate `i` with `0<c_i<1`.  Delete row `i` from `R` and write

\[
R_-:=R_{\{1,\dots,n\}\setminus\{i\}},\qquad
G:=R_-^TR_-=I_3-r_ir_i^T.
\]

Set

\[
B:=R_-MR_-^T,\qquad a:=R_-Mr_i,
\]

so the full quadratic form, separating the original coordinate `x_i`, is

\[
Q(x_i,x_-)=x_-^TBx_-+2x_i a^Tx_-
\]

because `A_{ii}=r_i^TMr_i=0`.

Define

\[
v:=R_-G^{-1}r_i.
\]

### Theorem 2.1 (exact null-ruling translation)

One has

\[
Bv=a,\qquad v^TBv=0,
\tag{2.1}
\]

and hence the exact identity

\[
\boxed{
Q(x_i,x_-)= (x_-+v x_i)^TB(x_-+v x_i).
}
\tag{2.2}
\]

Moreover

\[
\boxed{\|v\|_2^2=\frac{c_i}{1-c_i}.}
\tag{2.3}
\]

#### Proof

Since `R_-^TR_-=G`,

\[
Bv=R_-MR_-^TR_-G^{-1}r_i=R_-MGG^{-1}r_i=R_-Mr_i=a.
\]

Also

\[
v^TBv=(G^{-1}r_i)^TGMG(G^{-1}r_i)=r_i^TMr_i=0.
\]

Expanding `(x_-+v x_i)^TB(x_-+v x_i)` now gives (2.2).  Finally,

\[
\|v\|^2=(G^{-1}r_i)^TG(G^{-1}r_i)=r_i^TG^{-1}r_i.
\]

Sherman--Morrison for `G=I-r_ir_i^T` gives `G^{-1}r_i=r_i/(1-c_i)`, hence (2.3).  QED.

### Product-law meaning

Conditioning on the **original** variable `X_i=x` preserves independence of every remaining input coordinate and preserves each density cap `<=1`.  Formula (2.2) says the conditional problem is not an arbitrary correlated translation in spectral coordinates: it is the same residual quadratic form `B`, evaluated on the coordinatewise translated product vector `X_-+vx`.  This is the precise product-preserving null ruling through the indefinite cone.

## 3. The third direction is forced onto the hub slope

The rank-two saddle by itself has no transverse curvature.  In rank three with vanishing physical diagonal the hub slope `a` necessarily carries a minority-sign quadratic curvature of order `s`.

### Theorem 3.1 (matched minority curvature)

With the notation above,

\[
\boxed{\|a\|_2^2=r_i^TM^2r_i\ge s^2 c_i.}
\tag{3.1}
\]

Furthermore

\[
\boxed{a^TBa=\det(M)c_i.}
\tag{3.2}
\]

Consequently, for `u=a/\|a\|`,

\[
\boxed{
 u^TBu=\frac{\det(M)c_i}{r_i^TM^2r_i},
 \qquad |u^TBu|\ge \frac{s}{2}.
}
\tag{3.3}
\]

The sign of `u^TBu` is the minority inertia sign: negative in signature `(2,1)` and positive in signature `(1,2)`.

#### Proof of (3.1)

Using `G=I-r_ir_i^T` and `r_i^TMr_i=0`,

\[
\|a\|^2=r_i^TMR_-^TR_-Mr_i=r_i^TMGM r_i=r_i^TM^2r_i.
\]

Since `M^2\succeq s^2I`, this is at least `s^2c_i`.

#### Proof of (3.2)

Again using `G=R_-^TR_-`,

\[
a^TBa=r_i^TMGMGM r_i.
\]

Because `r_i^TMr_i=0`, both `GM r_i=Mr_i` after the rank-one correction at the right endpoint, and `r_i^TMG=r_i^TM` at the left endpoint.  Therefore

\[
a^TBa=r_i^TM^3r_i.
\]

For a `3x3` matrix with `tr M=0`, Cayley--Hamilton is

\[
M^3-\frac{\operatorname{tr}(M^2)}2M-\det(M)I=0.
\]

Sandwiching by `r_i` and using `r_i^TMr_i=0` gives

\[
r_i^TM^3r_i=\det(M)\|r_i\|^2=\det(M)c_i.
\]

This proves (3.2).

#### Proof of the uniform lower bound in (3.3)

The denominator in (3.3) is at most `\|M\|_{op}^2c_i`, so

\[
|u^TBu|\ge \frac{|\det M|}{\|M\|_{op}^2}.
\]

For inertia `(2,1)` and trace zero, write the eigenvalues as `p,q,-(p+q)`, where `p,q>=s`.  Then

\[
\frac{|\det M|}{\|M\|_{op}^2}
=\frac{pq(p+q)}{(p+q)^2}
=\frac{pq}{p+q}
\ge \frac{\min(p,q)}2\ge \frac{s}{2}.
\]

The `(1,2)` case is identical after multiplying by `-1`.  Since the determinant is negative in `(2,1)` and positive in `(1,2)`, its sign is exactly the minority sign.  QED.

## 4. Physical triangle identity

For every distinct triple `i,j,k`, the physical principal block has zero diagonal, so

\[
\det A_{\{i,j,k\}}=2A_{ij}A_{ik}A_{jk}.
\]

On the other hand Cauchy--Binet gives

\[
\det A_{\{i,j,k\}}=\det(M)\det(R_{\{i,j,k\}})^2.
\]

Thus, with `w_{ijk}:=det(R_{ijk})^2`,

\[
\boxed{2A_{ij}A_{ik}A_{jk}=\det(M)w_{ijk}.}
\tag{4.1}
\]

In particular every nonzero physical triangle product has the same sign, namely `sign(det M)`.

Using the partner inclusion identity `sum_{B\ni i}w_B=c_i`, (4.1) sums to

\[
\boxed{
2\sum_{j<k:\ j,k\ne i} A_{ij}A_{ik}A_{jk}=\det(M)c_i,
}
\tag{4.2}
\]

which is the physical-coordinate form of (3.2).

## 5. A product-preserving residual cut forced by the matched curvature

Because the residual physical diagonal is also zero, for `u=a/\|a\|` we have

\[
u^TBu=2\sum_{j<k}B_{jk}u_ju_k.
\]

Put each residual original coordinate independently into a fair random set `S`; let `T=S^c`.  Then

\[
\mathbb E\,[u_S^TB_{S,T}u_T]=\frac14u^TBu.
\]

Therefore some deterministic original-coordinate cut satisfies

\[
|u_S^TB_{S,T}u_T|\ge \frac14|u^TBu|\ge \frac{s}{8}.
\]

Since `\|u_S\|\|u_T\|<=1/2`,

\[
\boxed{\|B_{S,T}\|_{op}\ge \frac{s}{4}.}
\tag{5.1}
\]

This is only a rank-one cross certificate, not yet a density theorem.  Its importance is that it is aligned with the **same** hub slope which appears in the exact translation (2.2), and it is obtained by an original-coordinate cut, so product provenance is retained.

## 6. Applying the designated partner theorem to an actual inequality

Let `D_0` be the latest account02/B11 disjoint-Pluecker mass.

From (P1), choose `i` with

\[
c_i\ge\frac{1-D_0}{3}.
\]

Then Theorems 2.1 and 3.1 yield the explicit inequalities

\[
\boxed{
\|a_i\|\ge s\sqrt{\frac{1-D_0}{3}},
}
\tag{6.1}
\]

and, whenever `c_i<1`,

\[
\boxed{
\|v_i\|\ge \sqrt{\frac{1-D_0}{2+D_0}},
\qquad |u_i^TB_iu_i|\ge\frac{s}{2}.
}
\tag{6.2}
\]

Combined with partner fact (P2), this gives an exhaustive quantitative structural split:

* If `D_0>=1/2`, some original-coordinate cut has

\[
\boxed{\sigma_3(A[S,S^c])\ge \frac{s}{8\sqrt2}.}
\tag{6.3}
\]

* If `0<D_0<1/2`, some original hub coordinate has

\[
\boxed{
 c_i\ge\frac16,\qquad
 \|a_i\|\ge\frac{s}{\sqrt6},\qquad
 \|v_i\|\ge\frac1{\sqrt5},\qquad
 |u_i^TB_iu_i|\ge\frac{s}{2},
}
\tag{6.4}
\]

and there is an original-coordinate residual cut satisfying

\[
\boxed{\|B_i[S,T]\|_{op}\ge\frac{s}{4}.}
\tag{6.5}
\]

At `D_0=0`, the completed account03/B11 r18 endpoint theorem already compresses the null frame to at most five projective null-ray banks and supplies a universal density bound in its stated exact-rank-three scope; this note does not reprove that endpoint.

Thus the previously vague `small positive D_0` chamber has a new rigid feature: a quantitatively heavy null hub and a quantitatively large **minority-sign curvature along its own cross slope**.

## 7. Why this is the third-direction mechanism, and why it does not yet finish QFORM

For the rank-two opposite-sign control `2XY`, with centered unit uniforms, the density has the genuine logarithmic singularity

\[
p_{2XY}(t)=\log\frac1{2|t|},\qquad 0<|t|<1/2.
\]

The rank-two saddle has no identity analogous to (3.2) forcing curvature on the hyperbolic slope.

In the rank-three zero-diagonal chamber, Cayley--Hamilton forces exactly

\[
a^TBa=\det(M)c,
\]

and therefore forces a minority-sign residual Rayleigh curvature at least `s/2` after normalizing the cross slope.  This is an exact algebraic identification of the missing third direction, made without rotating the independent inputs.

What remains unpaid is analytic: `u` is generally a dense direction in the residual **original-coordinate** space.  Rotating the residual variables to put `u` on a coordinate axis would destroy independence.  Likewise, a bounded conditional density cannot substitute for independence (the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`).  Hence (3.3)--(6.5) are a new structural compiler, not a full density bound.

A natural next implication is:

`QFORM-NULL-MATCHED-CURVATURE-PRODUCT-TRACE-v1` — under the `0<D_0<1/2` certificate (6.4), exploit the exact null-ruling translation (2.2), the minority curvature `|u^TBu|>=s/2`, and the product-preserving residual cut (6.5) to prove a uniform density/small-ball bound, or route every failure to an already paid ridge/pair/bank certificate.  The proof must aggregate original coordinates before any rotation or fiber supremum.

## 8. Continuity and full-target status

This report proves structural identities and quantitative certificates.  It does **not** by itself establish an output density bound in the new small-positive-`D_0` chamber and therefore proves neither essential boundedness nor continuity there.

The full conjecture, including arbitrary additional spectrum, remains OPEN.
