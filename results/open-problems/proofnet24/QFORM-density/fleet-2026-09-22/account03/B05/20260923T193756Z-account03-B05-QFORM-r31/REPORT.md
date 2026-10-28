SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T19:37:56Z.
attacking: QFORM-TWISTED-MIXED-CUT-CROSSRANK3-v1 — convert the r29/r30 residual partner-plane currencies into an exact rank-three original-product crossing before reciprocal coarea inversion.

# account03/B05 — Pluecker aggregate to an exact rank-three crossing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `NEW SUPPORTING DENSITY/CONTINUITY THEOREM; FULL QFORM OPEN`  

The predecessor is

`yspennstate/math-open-problems@c2141e8758b0241ad18aedc7f9fb77654ff87fde:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T190745Z-account03-B05-QFORM-r30/REPORT.md`.

The fresh exact-cross mechanism used and refined here is

`yspennstate/math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae:proofnet24/QFORM-density/interactive/20260923T194300Z-exact-cross-rank-fourier/REPORT.md`.

The designated partner theorem is

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f:proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260923T041255Z-account04-B05-dominant-slope-r2/REPORT.md`.

No rotated eigen-coordinates are declared independent. Every split below is a split of original independent-coordinate banks.

## 1. Live ratio packet

Use the r30 packet. The first original-coordinate bank is `X=(X_i)_{i in G}` and

\[
V=\binom SR=\Gamma^T X,
\qquad \Gamma^T\Gamma=I_2,
\]

where the rows of `Gamma` are `g_i in R^2`. Two disjoint original-coordinate banks supply normalized scalar projections `Y,Z`, independent of `X` and one another. The compressed quadratic form is

\[
Q=V^TCV+2Yp^TV+2Zq^TV+
\begin{pmatrix}Y&Z\end{pmatrix}
B\binom YZ+\text{affine/outside terms},
\tag{1.1}
\]

with

\[
B=\begin{pmatrix}a&c\\c&d\end{pmatrix},
\quad p=\binom\alpha r,
\quad q=\binom\beta s,
\quad P=(p\ q),
\tag{1.2}
\]

and the ratio-packet Schur identity

\[
C-PB^{-1}P^T=\lambda m e_1e_1^T.
\tag{1.3}
\]

Put

\[
\mu=|\det B|\,|\lambda|,
\qquad
z=B^{-1}\binom rs=\binom{z_1}{z_2}.
\tag{1.4}
\]

The goal of this run is to pay the residual quantities `z_1,z_2` by a three-dimensional crossing before any fiber supremum or reciprocal minor is taken.

## 2. Determinant-sensitive exact-rank-three crossing lemma

### Lemma 2.1

Let two independent original-coordinate banks be compressed to `L,R in R^3`. Assume their densities exist with

\[
\|p_L\|_\infty\le H_L,
\qquad
\|p_R\|_\infty\le H_R.
\]

Suppose the entire cross term between the two banks is

\[
2L^TMR
\]

with `M` invertible, while arbitrary quadratic and affine terms are allowed inside either bank. Then

\[
|\varphi_Q(t)|
\le
\min\left\{1,
\frac{\pi^{3/2}(H_LH_R)^{1/2}}
{|t|^{3/2}|\det M|^{1/2}}
\right\}.
\tag{2.1}
\]

In particular, whenever one can write

\[
(H_LH_R)^{1/2}=2^{3/2}\,W^{-1/2},
\]

set

\[
\Delta=|\det M|W.
\tag{2.2}
\]

Then

\[
|\varphi_Q(t)|\le
\min\{1,(2\pi)^{3/2}\Delta^{-1/2}|t|^{-3/2}\},
\tag{2.3}
\]

and therefore `Q` has a bounded continuous density with

\[
\boxed{\|p_Q\|_\infty\le6\Delta^{-1/3}.}
\tag{2.4}
\]

### Proof

Disintegrate the within-bank phases into complex amplitudes `alpha_t(l),gamma_t(r)`. Their moduli are bounded by `p_L,p_R`; hence

\[
\|\alpha_t\|_2\le H_L^{1/2},
\qquad
\|\gamma_t\|_2\le H_R^{1/2}.
\]

Three-dimensional Plancherel applied to the exact cross phase `exp(2it l^TMr)` gives

\[
|\varphi_Q(t)|
\le
\frac{(2\pi)^{3/2}}{|\det(2tM)|^{1/2}}
\|\alpha_t\|_2\|\gamma_t\|_2,
\]

which is (2.1). Under (2.2), the nontrivial term is (2.3). Its crossing point with one is

\[
t_0=2\pi\Delta^{-1/3}.
\]

Thus

\[
\int_{\mathbb R}|\varphi_Q(t)|dt
\le
2\left(t_0+(2\pi)^{3/2}\Delta^{-1/2}
\int_{t_0}^\infty t^{-3/2}dt\right)
=12\pi\Delta^{-1/3}.
\]

Fourier inversion gives (2.4), and `phi_Q in L^1` gives a continuous density. QED.

This is the `k=3` exact-cross theorem with the product of the three crossing singular values retained, rather than replacing it by the smallest one.

## 3. Balanced Pluecker split of the two-dimensional first-bank projection

Let

\[
\ell_i=\|g_i\|_2^2,
\qquad q_X=\max_i\ell_i,
\qquad
w_{ij}=\det(g_i,g_j)^2.
\]

Cauchy-Binet gives

\[
\sum_{i<j}w_{ij}=\det(\Gamma^T\Gamma)=1.
\tag{3.1}
\]

For a subset `I`, write

\[
G_I=\Gamma_I^T\Gamma_I,
\qquad
D_I=\det G_I=\sum_{i<j\in I}w_{ij}.
\tag{3.2}
\]

For each vertex define

\[
d_i=\sum_{j\ne i}w_{ij}.
\]

Because `Gamma` is a Parseval two-frame,

\[
d_i
=\|g_i\|^2\sum_j\|g_j\|^2
-\sum_j\langle g_i,g_j\rangle^2
=2\ell_i-\ell_i=\ell_i.
\tag{3.3}
\]

Hence `sum_i d_i=2` and

\[
\sum_i d_i^2\le2q_X.
\tag{3.4}
\]

Now randomly place every original coordinate independently into `I` or `J` with probability `1/2`. In `D_ID_J`, an ordered pair of Pluecker edges contributes only when its two edges are vertex-disjoint, and then with probability `1/16`. The ordered weight of intersecting pairs is at most `sum_i d_i^2`. Therefore

\[
\mathbb E[D_ID_J]
\ge\frac{1-2q_X}{16}.
\tag{3.5}
\]

Thus, whenever `q_X<1/2`, there exists an original-coordinate split `I sqcup J` such that

\[
\boxed{
\sqrt{\det G_I\det G_J}
\ge\frac14\sqrt{1-2q_X}.
}
\tag{3.6}
\]

This is the aggregate-before-pair-selection step: no single physical minor is inverted.

For this split, whitening `Gamma_I` and `Gamma_J` and applying the two-dimensional product-projection bound gives

\[
\|p_{\Gamma_I^TX_I}\|_\infty\le\frac2{\sqrt{\det G_I}},
\qquad
\|p_{\Gamma_J^TX_J}\|_\infty\le\frac2{\sqrt{\det G_J}}.
\tag{3.7}
\]

## 4. Mixed Y/Z cut: the partner-plane U currency becomes a crossing determinant

Place the whole `Y` bank on the left and the whole `Z` bank on the right. With

\[
A_I=\Gamma_I^TX_I,
\qquad A_J=\Gamma_J^TX_J,
\]

the left/right compressed variables are `(A_I,Y)` and `(A_J,Z)`. Their entire `3 x 3` crossing matrix is

\[
M_{YZ}=
\begin{pmatrix}
C&q\\
p^T&c
\end{pmatrix}.
\tag{4.1}
\]

A direct determinant calculation gives

\[
\det M_{YZ}=c\det C-p^T\operatorname{adj}(C)q.
\tag{4.2}
\]

For symmetric `2 x 2` `C`, with `u=(-r,alpha)^T`, `v=(-s,beta)^T`, one has

\[
p^T\operatorname{adj}(C)q=u^TCv=U,
\]

so the r30 partner-plane mixed curvature appears exactly as

\[
\det M_{YZ}=c\det C-U.
\tag{4.3}
\]

Using the Schur identity (1.3) and `z=B^{-1}(r,s)^T`, exact algebra yields

\[
\boxed{
\det M_{YZ}=-\lambda m\det(B)z_1z_2,
\qquad
|\det M_{YZ}|=\mu m|z_1z_2|.
}
\tag{4.4}
\]

Since normalized scalar projections have density cap at most `sqrt(2)`, the left and right 3D density caps satisfy

\[
H_L\le\frac{2\sqrt2}{\sqrt{\det G_I}},
\qquad
H_R\le\frac{2\sqrt2}{\sqrt{\det G_J}}.
\]

Lemma 2.1 therefore applies with crossing volume

\[
\Delta_{YZ}
=|\det M_{YZ}|\sqrt{\det G_I\det G_J}.
\tag{4.5}
\]

By (3.6),

\[
\boxed{
\Delta_{YZ}
\ge
\frac{\mu m|z_1z_2|}{4}\sqrt{1-2q_X}.
}
\tag{4.6}
\]

We have proved the first main bound:

\[
\boxed{
\|p_Q\|_\infty
\le
6\left(
\frac{4}{\mu m|z_1z_2|\sqrt{1-2q_X}}
\right)^{1/3},
}
\tag{4.7}
\]

whenever the denominator is positive. The density is continuous in this branch.

This pays the r29/r30 mixed `U` currency without slicing both partner coordinates and without conditioning on the dependent residual `R`.

## 5. Axis-residual repair by splitting one scalar product bank

The mixed cut degenerates when one of `z_1,z_2` is zero. The original product provenance supplies two anisotropic alternatives.

Write the normalized scalar projection

\[
Z=\sum_j\zeta_jW_j,
\qquad \sum_j\zeta_j^2=1,
\qquad q_Z=\max_j\zeta_j^2,
\tag{5.1}
\]

where the `W_j` are independent original coordinates in the `Z` bank. Randomly split this bank into `K,L` and set `t=sum_{j in K} zeta_j^2`. Since

\[
\mathbb E[t(1-t)]
=\frac14\left(1-\sum_j\zeta_j^4\right)
\ge\frac14(1-q_Z),
\]

there exists a split with

\[
\boxed{
\|\zeta_K\|_2\|\zeta_L\|_2
\ge\frac12\sqrt{1-q_Z}.
}
\tag{5.2}
\]

Condition the entire independent `Y` bank, and split the first bank as in Section 3. Put `(A_I,Z_K)` on the left and `(A_J,Z_L)` on the right. The exact crossing matrix is

\[
H_Z=
\begin{pmatrix}
C&q\\q^T&d
\end{pmatrix}.
\tag{5.3}
\]

The Schur identity gives

\[
\boxed{
\det H_Z=\lambda m\det(B)z_1^2,
\qquad
|\det H_Z|=\mu m z_1^2.
}
\tag{5.4}
\]

The partial scalar projections have density caps `sqrt(2)/||zeta_K||` and `sqrt(2)/||zeta_L||`. Thus Lemma 2.1 uses

\[
\Delta_Z
=|\det H_Z|\sqrt{\det G_I\det G_J}
\|\zeta_K\|\|\zeta_L\|.
\]

Combining (3.6) and (5.2),

\[
\boxed{
\Delta_Z
\ge
\frac{\mu m z_1^2}{8}
\sqrt{1-2q_X}\sqrt{1-q_Z}.
}
\tag{5.5}
\]

Therefore

\[
\boxed{
\|p_Q\|_\infty
\le
6\left(
\frac{8}{\mu m z_1^2\sqrt{1-2q_X}\sqrt{1-q_Z}}
\right)^{1/3}.
}
\tag{5.6}
\]

Again the density is continuous.

Symmetrically, if

\[
Y=\sum_j\eta_jU_j,
\qquad q_Y=\max_j\eta_j^2,
\]

condition `Z` and split the `Y` bank. With

\[
H_Y=\begin{pmatrix}C&p\\p^T&a\end{pmatrix},
\]

one has

\[
|\det H_Y|=\mu m z_2^2,
\]

and hence

\[
\boxed{
\|p_Q\|_\infty
\le
6\left(
\frac{8}{\mu m z_2^2\sqrt{1-2q_X}\sqrt{1-q_Y}}
\right)^{1/3}.
}
\tag{5.7}
\]

## 6. Combined theorem — `QFORM-RATIOPACKET-PLUECKER-CROSSRANK3-v1`

Define the three original-product crossing currencies

\[
\Omega_{YZ}
=\frac{\mu m|z_1z_2|}{4}\sqrt{1-2q_X},
\tag{6.1}
\]

\[
\Omega_Z
=\frac{\mu m z_1^2}{8}
\sqrt{1-2q_X}\sqrt{1-q_Z},
\tag{6.2}
\]

\[
\Omega_Y
=\frac{\mu m z_2^2}{8}
\sqrt{1-2q_X}\sqrt{1-q_Y}.
\tag{6.3}
\]

Whenever `q_X<1/2`, every positive one of these currencies produces an exact rank-three crossing in original-coordinate banks. Consequently

\[
\boxed{
\|p_Q\|_\infty
\le
6\,[\max(\Omega_{YZ},\Omega_Z,\Omega_Y)]^{-1/3}
}
\tag{6.4}
\]

provided the maximum is positive, and this branch has a **continuous** density.

Concrete quantitative checks:

- if `q_X<=1/4`, `q_Z<=1/2`, and `mu m z_1^2>=1`, then `Omega_Z>=1/16`, so
  \[
  \boxed{\|p_Q\|_\infty\le6\,16^{1/3}<15.120.}
  \]
- under the same leverage bounds but `mu m z_1^2>=1/8`, one gets `Omega_Z>=1/128`, hence
  \[
  \boxed{\|p_Q\|_\infty\le6\,128^{1/3}<30.239.}
  \]
- if `q_X<=1/4` and `mu m|z_1z_2|>=1`, then
  \[
  \boxed{\|p_Q\|_\infty\le6(4\sqrt2)^{1/3}<10.691.}
  \]

No support, moment, log-concavity, centering, connectedness, or post-rotation independence hypothesis is used.

## 7. Designated partner result applied to an actual inequality

The completed `account04/B05` theorem proves

\[
\|p_Q\|_\infty<51.6(\mu m_*)^{-1/3}.
\]

Thus the concrete dominant exact-slope branch

\[
\mu\ge1,
\qquad m_*\ge\frac18
\]

satisfies

\[
\boxed{\|p_Q\|_\infty<103.2.}
\tag{7.1}
\]

This is complementary to (6.4): exact slope atoms are paid by the partner theorem, while the new crossing theorem pays diffuse Pluecker mass and the residual `z` currencies before a fiber supremum appears.

## 8. Precise remaining factor

This run removes the r30 need to attack the mixed `U` coefficient solely by a one-partner slice whenever a diffuse exact-rank-three physical cut can be formed. The surviving ratio-packet chamber must now lose that crossing volume. Concretely, at least one of the following must occur:

1. the first-bank two-frame is heavy enough that `q_X` approaches or exceeds `1/2`, so no dimension-free disjoint Pluecker-pair mass follows from (3.5);
2. an axis residual dominates while the corresponding scalar product projection is itself almost one-coordinate (`q_Z ->1` for the `z_1` branch, or `q_Y ->1` for the `z_2` branch);
3. the residual currencies `mu m z_1^2`, `mu m z_2^2`, and `mu m|z_1z_2|` all collapse, in which case the escaped-curvature/one-hub structural branch must supply the third resource.

These are localized/heavy-coordinate failures, not arbitrary-joint coarea failures. The next B05 implication is therefore

`QFORM-HEAVY-ROW-OR-HEAVY-SCALAR-PIVOT-COAREA-v1`:

> splice the exact rank-three crossing theorem above with a localized physical pivot when `q_X>=1/2` or the active scalar bank has leverage near one, and show that the bare three-large-eigenvalue hypothesis forces one of those localized receivers or a positive crossing currency.

The full conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity is still **OPEN**. The new theorem proves continuity only on its stated positive-crossing branches.
