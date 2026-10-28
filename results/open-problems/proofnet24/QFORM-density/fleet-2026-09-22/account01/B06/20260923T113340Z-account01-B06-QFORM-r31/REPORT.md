SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T11:33:40Z.
attacking: the r30 collision obstruction.  Keep the entire bordered third-compound packet, use exact rank-three Pluecker factorization before any localization, and prove an exhaustive disjoint-cut versus aggregate rank-one physical-hub alternative.

# account01/B06 r31 — exact-rank-three collision compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_THEOREM_PROVED / FULL_TARGET_OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Continuity: the new collision theorem is deterministic and does not itself prove continuity.  Continuity remains available only on imported branches whose Fourier proof already supplies it.

## 1. Source boundary actually used


Immediate predecessor: account01/B06 r30, canonical `yspennstate/math-open-problems@c17a14105e7cb453bbca9576ab7df54f504eff67`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T103846Z-account01-B06-QFORM-r30/REPORT.md`.  It proved the bordered compound identity and the random-cut estimate, but left high compound collision as an unpaid grouped-hub regime.

Designated partner actually applied below: account02/B06 `QFORM-191-STAR-HUB-INTERNAL-PAYMENT-v1` and `QFORM-191-ROBUST-LIGHT-ROW-AREA-OR-COMMON-DIRECTION-v1`, canonical `yspennstate/math-open-problems@328a550b1ddde3d2d9b7c2d245678f0b6fd5e7ae`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T105551Z-182f201f81de/REPORT.md`.

## 2. Exact setup

Let

\[
A=U\Lambda U^T,\qquad U^TU=I_3,
\]

be a real symmetric exact-rank-three matrix in the **original physical coordinates**, with `Lambda` invertible.  Fix two distinct physical coordinates `x,y` and put

\[
Z=[n]\setminus\{x,y\}.
\]

For two-subsets `R,T` of `Z`, define the bordered third minor

\[
D_{R,T}:=\det A[\{x\}\cup R,\{y\}\cup T].
\]

Set

\[
W:=\sum_{R,T}D_{R,T}^2,\qquad
W_{\rm disj}:=\sum_{R\cap T=\varnothing}D_{R,T}^2.
\]

Assume `W>0`.  Put

\[
r_R:=\det U[\{x\}\cup R,:]^2,\qquad
c_T:=\det U[\{y\}\cup T,:]^2,
\]

and

\[
A_x:=\sum_Rr_R,\qquad A_y:=\sum_Tc_T.
\]

Then `A_x,A_y>0` and we may define probability measures

\[
\mu_x(R)=r_R/A_x,\qquad \mu_y(T)=c_T/A_y.
\]

For `j in Z`, let the two conditional inclusion marginals be

\[
q_j^x:=\mu_x\{R:j\in R\},\qquad q_j^y:=\mu_y\{T:j\in T\}.
\]

Since every sampled set has cardinality two,

\[
\sum_{j\in Z}q_j^x=\sum_{j\in Z}q_j^y=2.                 \tag{2.1}
\]

## 3. Main theorem: cut or aggregate rank-one collision hub

### Theorem 3.1 — `QFORM-RANK3-COLLISION-CUT-OR-RANKONE-HUB-v1`

With the setup above, exactly the following quantitative alternative is available.

**Low-collision alternative.** If

\[
\chi:=1-W_{\rm disj}/W\le \frac12,
\]

then a fair physical partition of `Z` has an orientation for which the bordered third-volume contribution is at least

\[
\boxed{W/32}.                                                   \tag{3.1}
\]

In particular, the r30 disjoint-cut receiver is available with no loss depending on `n`.

**High-collision alternative.** If `chi>1/2`, then there is one physical coordinate `j in Z` such that the whole matrix

\[
\mathcal D^{(j)}=(D_{\{j,k\},\{j,\ell\}})_{k,\ell\in Z\setminus\{j\}}
\]

has rank at most one and

\[
\boxed{
\|\mathcal D^{(j)}\|_{\rm op}^2
=\|\mathcal D^{(j)}\|_F^2
>W/16.
}                                                             \tag{3.2}
\]

Equivalently,

\[
\boxed{\|\mathcal D^{(j)}\|_{\rm op}>\sqrt W/4.}             \tag{3.3}
\]

This is an aggregate local hub, not a selected physical minor.

### Proof

Because `A=U Lambda U^T` has exact rank three, Cauchy--Binet on each 3 by 3 minor gives the exact factorization

\[
D_{R,T}=\det(\Lambda)\,
\det U[\{x\}\cup R,:]\,
\det U[\{y\}\cup T,:].                                      \tag{3.4}
\]

Therefore

\[
\boxed{W=|\det\Lambda|^2A_xA_y}.                             \tag{3.5}
\]

Moreover, if `R~mu_x` and `T~mu_y` are sampled independently, then

\[
\frac{W_{\rm disj}}W=\mathbb P(R\cap T=\varnothing),
\qquad
\chi=\mathbb P(R\cap T\ne\varnothing).                      \tag{3.6}
\]

If `chi<=1/2`, then `W_disj>=W/2`.  The r30 fair-cut identity says that each disjoint ordered pair `(R,T)` lands in the required row/column orientation with probability `2^{-4}=1/16`.  Hence the expected bordered volume on a fair cut is `W_disj/16>=W/32`; some actual original-coordinate cut has at least that much.  This proves (3.1).

Now assume `chi>1/2`.  By the union bound and independence of `R,T`,

\[
\chi
\le \sum_{j\in Z}\mathbb P(j\in R,j\in T)
=\sum_{j\in Z}q_j^xq_j^y.                                    \tag{3.7}
\]

Let

\[
m:=\max_j q_j^xq_j^y.
\]

Cauchy--Schwarz and (2.1) give

\[
\sum_j\sqrt{q_j^xq_j^y}
\le\sqrt{\sum_jq_j^x}\sqrt{\sum_jq_j^y}=2.                  \tag{3.8}
\]

Thus

\[
\sum_jq_j^xq_j^y
\le \sqrt m\sum_j\sqrt{q_j^xq_j^y}
\le2\sqrt m.                                                  \tag{3.9}
\]

Combining (3.7)--(3.9),

\[
\boxed{m\ge\chi^2/4>1/16.}                                  \tag{3.10}
\]

Choose `j` attaining `m`.  For `k,l != j`, (3.4) yields

\[
D_{\{j,k\},\{j,\ell\}}
=\det\Lambda\,r_k^{(x,j)}s_\ell^{(y,j)},                     \tag{3.11}
\]

where

\[
r_k^{(x,j)}=\det U[\{x,j,k\},:],\qquad
s_\ell^{(y,j)}=\det U[\{y,j,\ell\},:].                       \tag{3.12}
\]

Hence

\[
\boxed{\mathcal D^{(j)}=\det\Lambda\,r^{(x,j)}(s^{(y,j)})^T} \tag{3.13}
\]

is rank at most one.  Its unique nonzero singular value squared is

\[
\|\mathcal D^{(j)}\|_F^2
=|\det\Lambda|^2
 \Big(\sum_{k\ne j}(r_k^{(x,j)})^2\Big)
 \Big(\sum_{\ell\ne j}(s_\ell^{(y,j)})^2\Big).               \tag{3.14}
\]

But the two bracketed terms are exactly `A_x q_j^x` and `A_y q_j^y`.  By (3.5),

\[
\boxed{
\|\mathcal D^{(j)}\|_F^2=Wq_j^xq_j^y=Wm.
}                                                             \tag{3.15}
\]

Use (3.10) and `chi>1/2` to obtain (3.2)--(3.3).  QED.

### General threshold form

For any `0<theta<1`, either

\[
W_{\rm disj}\ge(1-\theta)W
\]

and some cut carries at least `(1-theta)W/16`, or there is a physical `j` with

\[
\boxed{
\|\mathcal D^{(j)}\|_{\rm op}
\ge \frac\theta2\sqrt W.
}                                                             \tag{3.16}
\]

The choice `theta=1/2` gives the balanced constants above.

## 4. Original-coordinate formula for the aggregate hub

This section makes clear that (3.13) is not a hidden spectral rotation of the random inputs.

Assume additionally the r30 zero-anchor form `A_xy=0`, and write in original coordinates

\[
a=A_{xZ},\qquad b=A_{yZ},\qquad C=A_{ZZ}.
\]

Fix the hub `j`, remove its coordinate from these arrays, and write

\[
a'=a_{Z\setminus\{j\}},\quad b'=b_{Z\setminus\{j\}},\quad
r=C_{j,Z\setminus\{j\}},\quad C'=C_{Z\setminus\{j\},Z\setminus\{j\}}.
\]

Direct expansion of the bordered 3 by 3 determinant gives the **physical-coordinate contraction identity**

\[
\boxed{
\mathcal D^{(j)}
=-a_jb_jC'
+a_j b'r^T
+b_j r(a')^T
-C_{jj}b'(a')^T.
}                                                             \tag{4.1}
\]

For a generic matrix the right side need not have low rank.  The exact-rank-three hypothesis forces the whole four-term matrix in (4.1) to collapse to the rank-one outer product (3.13).  This is the correct high-collision object to feed into a grouped hub/bank receiver.  Selecting one entry of (4.1) would contradict the live local-collision correction; retaining its whole operator does not.

There is also an exact accounting identity.  If

\[
H_j:=\|\mathcal D^{(j)}\|_F^2,
\]

then summing over physical `j` counts collision terms with intersection size one once and diagonal collisions `R=T` twice:

\[
W_{\rm coll}\le\sum_jH_j\le2W_{\rm coll}.                    \tag{4.2}
\]

The new theorem is stronger than dimension-dependent pigeonholing of (4.2): exact rank-three factorization upgrades `chi>1/2` directly to one `H_j>W/16`.

## 5. Quantitative splice into r30

The predecessor r30 obtained, in its certified transverse-curvature chamber,

\[
W>s^6/128,\qquad s=s_3(A).                                      \tag{5.1}
\]

Theorem 3.1 now makes the r30 collision split exhaustive **inside exact rank three**:

* low collision gives the already-used physical cut with `E_3>s^6/4096`;
* high collision gives one physical hub `j` with

\[
\boxed{
\|\mathcal D^{(j)}\|_{\rm op}
>\frac{s^3}{\sqrt{2048}}
=\frac{s^3}{32\sqrt2}.
}                                                             \tag{5.2}
\]

Thus high collision can no longer remain an unstructured diffuse error term.  It is a target-scale **aggregate rank-one compound hub**.

## 6. Actual application of the designated account02/B06 result

The partner theorem is now applied to a real inequality, rather than merely cited.

Let `ell_i=||u_i||^2` be the physical leverage in the exact-rank-three factorization and let

\[
H=\{i:\ell_i>1/64\},\qquad L=H^c.
\]

For the high-collision hub from Theorem 3.1, put

\[
n_j^x=A_xq_j^x,\qquad n_j^y=A_yq_j^y.
\]

Each is a sub-sum of all rank-three Pluecker weights containing `j`, whose total is `ell_j`; hence

\[
\ell_j\ge\max(n_j^x,n_j^y)\ge\sqrt{n_j^xn_j^y}.              \tag{6.1}
\]

Using (3.10),

\[
\boxed{
\ell_j\ge\sqrt{A_xA_yq_j^xq_j^y}
>\frac14\sqrt{A_xA_y}.
}                                                             \tag{6.2}
\]

Consequently, on the quantitative anchored-volume subbranch

\[
A_xA_y\ge1/256,                                                \tag{6.3}
\]

we have `ell_j>1/64`, so this **same collision hub** belongs to the partner's bounded heavy set `H`.

Apply account02/B06 `QFORM-191-STAR-HUB-INTERNAL-PAYMENT-v1`.  In the r33/r31 unpaid star-hub state it gives the actual alternative

\[
\boxed{\|p_Q\|_\infty<1447/s}                                \tag{6.4}
\]

or, specifically for the collision hub `j`,

\[
\boxed{
\|A_{j,L}\|_2\ge\gamma s,
\qquad \gamma=1/(16\sqrt2).
}                                                             \tag{6.5}
\]

If (6.4) does not occur, the partner's second deterministic compiler applies to the complete heavy-to-light block `C=A_{H,L}`.  With `eta=1/128`, it yields either

\[
\sigma_2(C)\ge\eta s
\]

and some two heavy rows have coefficient area at least

\[
2.56316499669\times10^{-6}s^2,                                \tag{6.6}
\]

or there is a common light direction `r_0` and a rank-one approximation `C_1=\alpha r_0^T` with

\[
\|C-C_1\|_F<\gamma s/4,
\qquad
|\alpha_j|>3\gamma s/4.                                      \tag{6.7}
\]

Equation (6.7) is especially compatible with the rank-one compound contraction (3.13): both the collision obstruction and the unpaid heavy-to-light block are now forced into aggregate one-hub/one-bank geometry.  No individual light edge is selected.

The only new residual subbranch created by the splice is the small anchored-volume regime `A_xA_y<1/256`; in that regime the rank-one hub theorem (3.2) remains valid, but (6.2) alone does not put its hub into the `1/64` physical-leverage set.  This is a precise spectral-anchor normalization debt, not an unquantified collision debt.

## 7. What is and is not proved

New proved claim IDs:

* `QFORM-RANK3-COLLISION-CUT-OR-RANKONE-HUB-v1`;
* `QFORM-RANK3-COLLISION-HUB-CONTRACTION-v1`;
* `QFORM-BORDERED-HUB-PHYSICAL-CONTRACTION-IDENTITY-v1`.

What has been removed: in exact rank three, the r30 phrase “high compound collision may be diffuse over arbitrarily many physical coordinates” is no longer correct.  High collision forces one physical coordinate to carry an entire target-scale rank-one compound contraction.  This does **not** say that one entry or one physical pair is large.

First unpaid implication after this run:

`QFORM-RANKONE-COMPOUND-HUB-RECEIVER-v1`: retain the whole operator `mathcal D^(j)` from (3.13)/(4.1), and either (i) feed it together with the robust light star (6.5) into an aggregate mixed-hub/Fresnel receiver, or (ii) in the small anchored-volume regime `A_xA_y<1/256`, prove that the anchor normalization failure routes to an existing spectral-coloop/diffuse-frame exit.  Do not take a one-entry or one-pair reciprocal endpoint.

Full arbitrary-dimensional QFORM: **OPEN**.  No counterexample to the target was produced.  Universal continuity: **OPEN**.  Independent end-to-end review of the new theorem: pending.
