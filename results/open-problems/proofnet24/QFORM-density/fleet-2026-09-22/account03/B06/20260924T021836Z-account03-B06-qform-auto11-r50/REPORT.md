SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-24T02:18:36Z.
attacking: the r49 small-pair-currency singular-T survivor; replace the remaining exact two-coordinate shear theorem by an arbitrary right-bank product theorem, and expose the rank-three shear volume that survives when the outer hyperbolic pair degenerates.

# account03/B06 r50 — right-bank shear integration and singular-T rank-three core volume

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control read at startup: revision `2026-09-22.15`; programme revision `2026-09-22.5`  
Assignment: curved fiber integration / quantitative inequalities and rigorous computations  
Status: `NEW SUPPORTING THEOREMS + r49 EXACT ENDPOINT REFINED + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted owner conjecture remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence assumption is added. Every probabilistic bank below is a set of literal original coordinates. Continuity is stated only on branches whose characteristic function is proved integrable.

## 1. Fresh source boundary and immediate debt

The immediate predecessor is

`yspennstate/math-open-problems@ac4d8963e32785d2191e535b0268fe451262a903`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T012256Z-account03-B06-qform-r49/REPORT.md`.

It works in the exact shear-flat normal form

\[
A=\begin{pmatrix}H&E\\E^T&C\end{pmatrix},\qquad
C-E^TH^{-1}E=D+E^TTE,                                      \tag{1.1}
\]
where `H` is a literal invertible physical `2 x 2` block, `D` is diagonal on the environment ORIGINAL coordinates, and `E` is a real `2 x m` matrix of row rank two. The singular endpoint is

\[
T=\lambda vv^T,\qquad \lambda\ne0,\qquad \|v\|_2=1.       \tag{1.2}
\]
Put

\[
G=EE^T,\qquad W=\det G>0,\qquad U:=H^{-1}+\lambda vv^T.   \tag{1.3}
\]
Then the actual environment block is

\[
C=D+E^TUE.                                                  \tag{1.4}
\]

r49 paid the pair-diffuse branch when its two physical diagonal pivots have nonzero aggregate currency. A newer compatible account02/B06 theorem subsequently proved a uniform square-root small-ball estimate for every diagonal-plus-rank-one Schur residual and hence paid the r49 zero-diagonal/tangency face whenever the physical-pair currency `|det H| sigma_min(H)` itself is quantitative. Its precise remaining debt is therefore structural:

> when the physical pair currency becomes small, compile the intact two-row shear frame `E`, the rank-one direction `v`, and the target's remaining curvature into a product-preserving exit without deleting `D` or the nonzero tail.

This run attacks that debt in two ways. First, it removes the artificial requirement that the right side of the rank-two transverse-shear theorem contain exactly two physical coordinates. Second, it identifies the exact rank-three pseudodeterminant carried by the entire singular-T nonseparable core.

The live correction set is retained: no law-uniform pointwise Fresnel decay, no arbitrary-joint coarea cap, no positive moment of worst conditional projection height, no post-rotation independence, no deletion of a small nonzero tail, and no unrestricted curved-fiber supremum.

## 2. Bank-valued extension of the transverse-shear theorem

The completed account01/B09 theorem `QFORM-RANK2-CROSS-TRANSVERSE-SHEAR-v1` treated a three-coordinate left packet and a **two-coordinate** right packet. Its proof used the right packet only through an `L^2` bound for the two active singular coordinates. For a general original-coordinate right bank, the genuine two-dimensional product-marginal theorem supplies the same input with one factor `sqrt(2)` loss.

### Theorem 2.1 — `QFORM-RANK2-CROSS-TRANSVERSE-SHEAR-RIGHTBANK-v1`

Partition the independent ORIGINAL coordinates into disjoint sets `S,T,R`, with `|S|=3` and `T` arbitrary. Condition on `R`. Write

\[
q(s,t)=s^TBs+2s^TMt+t^TCt+\ell_S^Ts+\ell_T^Tt+c_0,        \tag{2.1}
\]
where `B,C` are symmetric. Assume

1. `rank M=2`;
2. its nonzero singular values are `s_1,s_2>0`, and
   \[
   \Delta=s_1s_2;                                           \tag{2.2}
   \]
3. `e` is a unit vector spanning `ker(M^T)`;
4. the kernel curvature vanishes,
   \[
   e^TBe=0;                                                 \tag{2.3}
   \]
5. the transverse shear
   \[
   c=(I-ee^T)Be                                             \tag{2.4}
   \]
   is nonzero.

Then the complete conditional and unconditional quadratic form has a bounded continuous density vanishing at infinity and

\[
\boxed{
\|p_Q\|_\infty
\le C_{\rm sh,bank}\,\Delta^{-3/8}\|c\|^{-1/4},
\qquad C_{\rm sh,bank}<7.713 .}                            \tag{2.5}
\]

An exact admissible constant is

\[
C_{\rm sh,bank}=2^{3/8}C_{\rm sh},                         \tag{2.6}
\]
where the completed two-coordinate theorem has

\[
C_{\rm sh}=\frac4\pi\left(\frac K6\right)^{3/4},\qquad
K=2\pi\sqrt{\frac{3C_E}{2}},\qquad
C_E=3\,2^{2/3}\left(\frac32+2\pi\right).                  \tag{2.7}
\]
Numerically

\[
C_{\rm sh}=5.947408752586213\ldots,\qquad
C_{\rm sh,bank}=7.712834918031422\ldots .                  \tag{2.8}
\]

#### Proof

Take a thin SVD of `M`. Rotate analytically inside the three-dimensional left packet so that `z` is the kernel coordinate and `u in R^2` are the active coordinates. Because `S` consists of exactly three ORIGINAL independent coordinates, the transformed joint density `F(z,u)` is still bounded by one and has total mass one. The hypothesis `e^TBe=0` leaves the `z` phase linear:

\[
2z\,c\cdot u+\beta z+G(u).                                  \tag{2.9}
\]

Define, as in the completed theorem,

\[
a_t(u)=e^{itG(u)}\widehat h_u(t(2c\cdot u+\beta)),\qquad
h_u(z)=F(z,u).                                                \tag{2.10}
\]
The same one-dimensional weighted Plancherel calculation and the two-dimensional marginal cap on `u` give

\[
\int_0^\infty t^{-1/3}\|a_t\|_2^2dt
\le C_E\|c\|^{-2/3}.                                      \tag{2.11}
\]
Nothing on the right bank has entered yet.

Now let `V` be the `|T| x 2` matrix of the two active right singular vectors. Complete it to an orthogonal coordinate system on the right bank only for integration; no independence is asserted for those rotated coordinates. For fixed `t`, integrate every orthogonal right-bank coordinate into a complex amplitude `b_t(y)`, `y in R^2`. Its modulus is bounded by the genuine density `rho_T(y)` of the two-dimensional orthogonal projection `V^T X_T`. The product-marginal theorem gives

\[
\|\rho_T\|_\infty\le2,\qquad \int\rho_T=1,                \tag{2.12}
\]
so

\[
\|b_t\|_2^2\le\int \rho_T(y)^2dy\le2,\qquad
\|b_t\|_2\le\sqrt2.                                      \tag{2.13}
\]

The active two-dimensional bilinear Plancherel step therefore becomes

\[
|\phi(t)|
\le \pi\sqrt2\,\Delta^{-1/2}|t|^{-1}\|a_t\|_2.           \tag{2.14}
\]
This is exactly the old estimate with one additional factor `sqrt(2)`. Cauchy--Schwarz with (2.11), integration on both time half-lines, and optimization of the cutoff therefore replace `K` by `sqrt(2)K`. The minimizing cutoff is multiplied by `(sqrt(2))^{3/4}=2^{3/8}`, giving (2.5)-(2.8). Since the resulting characteristic function is in `L^1`, Fourier inversion gives a bounded continuous `C_0` density. All bounds are uniform in the initially conditioned original coordinates, so Tonelli gives the same unconditional estimate. QED.

The important feature is that the right bank can now have arbitrary cardinality and arbitrary same-bank quadratic curvature. The curved-fiber payment uses the whole two-dimensional product marginal before taking any reciprocal singular quantity.

## 3. Apply the new theorem to the singular-T shear-flat packet

Write the columns of `E` as `e_j in R^2`, and put

\[
w_j=v^Te_j,\qquad
r_0=1+\lambda v^THv.                                        \tag{3.1}
\]
For a literal environment coordinate `j`, let `J` be its complement in the environment bank and form the ORIGINAL three-coordinate left packet

\[
S_j=\{h_1,h_2,j\},\qquad T_j=J.                            \tag{3.2}
\]
The cross matrix is

\[
M_j=A[S_j,J]
=
\begin{pmatrix}
E_J\\ e_j^TUE_J
\end{pmatrix}.                                                \tag{3.3}
\]
If `E_J` has row rank two, then `M_j` has rank exactly two. An exact unnormalised left-kernel vector is

\[
z_j=\binom{-Ue_j}{1},\qquad M_j^Tz_j=0.                    \tag{3.4}
\]
Set

\[
L_j=\|z_j\|_2=\sqrt{1+\|Ue_j\|_2^2}.                       \tag{3.5}
\]
The within-`S_j` block is

\[
B_j=
\begin{pmatrix}
H&e_j\\ e_j^T&d_j+e_j^TUe_j
\end{pmatrix},                                                \tag{3.6}
\]
where `d_j=D_jj`. Direct multiplication gives the exact identity

\[
\boxed{
B_jz_j=inom{-\lambda w_jHv}{d_j}.}                         \tag{3.7}
\]
Moreover

\[
\boxed{
z_j^TB_jz_j=d_j+\lambda r_0w_j^2.}                  \tag{3.8}
\]
Thus for the unit kernel vector `\hat z_j=z_j/L_j`,

\[
\kappa_j:=\hat z_j^TB_j\hat z_j
=\frac{d_j+\lambda r_0w_j^2}{L_j^2}.                        \tag{3.9}
\]
When `\kappa_j=0`, the transverse shear has the exact norm

\[
\boxed{
\|c_j\|
=\frac{\sqrt{\lambda^2w_j^2\|Hv\|^2+d_j^2}}{L_j}.}         \tag{3.10}
\]
In particular, on the zero-curvature face,

\[
\|c_j\|=0\quad\Longleftrightarrow\quad w_j=0\text{ and }d_j=0. \tag{3.11}
\]
No small nonzero quantity is discarded.

Let

\[
\alpha_j=e_j^TG^{-1}e_j.                                    \tag{3.12}
\]
The matrix determinant lemma gives

\[
\det(E_JE_J^T)=W(1-\alpha_j).                               \tag{3.13}
\]
If `\Delta_j` denotes the product of the two nonzero singular values of `M_j`, then its squared second exterior energy contains the top-two-row minors of `E_J`, hence

\[
\boxed{
\Delta_j\ge\sqrt{W(1-\alpha_j)}.}                           \tag{3.14}
\]
Therefore, whenever `\alpha_j<1`, `\kappa_j=0`, and `(w_j,d_j)\ne(0,0)`, Theorem 2.1 gives the full ambient **continuous-density** estimate

\[
\boxed{
\|p_Q\|_\infty
\le
C_{\rm sh,bank}
[W(1-\alpha_j)]^{-3/16}
L_j^{1/4}
[\lambda^2w_j^2\|Hv\|^2+d_j^2]^{-1/8}.}                    \tag{3.15}
\]
If in addition `\alpha_j\le1/2`,

\[
\boxed{
\|p_Q\|_\infty
<7.713\,(W/2)^{-3/16}L_j^{1/4}
[\lambda^2w_j^2\|Hv\|^2+d_j^2]^{-1/8}.}                    \tag{3.16}
\]

This is a new exact receiver for the r49 singular-T packet. It uses both literal outer hubs plus one literal environment coordinate as the three-coordinate curved packet and the **entire remaining environment product bank** on the other side. It does not replace that bank by a largest coefficient or a fiber maximum.

For completeness, if `\kappa_j\ne0`, the already-completed transverse-curvature theorem applies to the same packet with

\[
\|p_Q\|_\infty
\le C_{\rm tc}\,\Delta_j^{-3/7}|\kappa_j|^{-1/7},
\qquad C_{\rm tc}<9.068,                                    \tag{3.17}
\]
and also gives continuity. Equations (3.15)-(3.17) identify the only exact null packet as `\kappa_j=0`, `w_j=d_j=0`; a uniform collar around that null packet remains a separate quantitative problem.

## 4. Exact rank-three core volume of the singular-T normal form

The r49 small-pair-currency problem becomes clearer if the diagonal environment part is peeled off **algebraically but not probabilistically**. Define the rank-three nonseparable core

\[
A_0:=A-\operatorname{diag}(0,0,D)
=
\begin{pmatrix}
H&E\\ E^T&E^TUE
\end{pmatrix}.                                                \tag{4.1}
\]
The full target form is still `X^TA_0X+\sum_j d_jX_j^2`; the diagonal term is retained as a coordinate-separable perturbation below.

Let

\[
J_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.                  \tag{4.2}
\]
Introduce the `3 x (m+2)` frame

\[
R=
\begin{pmatrix}
I_2&H^{-1}E\\
0&v^TE
\end{pmatrix},                                                \tag{4.3}
\]
and the invertible `3 x 3` coefficient matrix

\[
M_3=\operatorname{diag}(H,\lambda).                           \tag{4.4}
\]
Then

\[
\boxed{A_0=R^TM_3R.}                                         \tag{4.5}
\]
Since `rank E=2`, `R` has row rank three and `A_0` has rank exactly three.

### Theorem 4.1 — `QFORM-SINGULART-CORE-PSEUDODET-SPLIT-v1`

Let `pdet_*(A_0)` denote the signed product of the three nonzero eigenvalues of `A_0`. Then

\[
\boxed{
|\operatorname{pdet}_*(A_0)|
=|\lambda|\left[
|\det H|\,v^TGv
+\frac{W}{|\det H|}\,\|Hv\|_2^2
\right].}                                                     \tag{4.6}
\]

#### Proof

The nonzero eigenvalues of `R^TM_3R` have product

\[
\operatorname{pdet}_*(A_0)
=\det(M_3)\det(RR^T)=(\det H)\lambda\det(RR^T).             \tag{4.7}
\]
Use Cauchy--Binet on the three-row frame `R`. A nonzero three-column minor is of one of two types.

1. Both physical hub columns plus one environment column. Their squared determinants sum to
   \[
   \sum_j(v^Te_j)^2=v^TGv.                                   \tag{4.8}
   \]
2. One physical hub column plus two environment columns. Summing over the retained hub and the environment pair gives
   \[
   W\,\|H^{-1}J_0v\|^2.                                    \tag{4.9}
   \]
Three environment columns give zero because all environment columns of `R` are images of a two-dimensional vector.

Hence

\[
\det(RR^T)=v^TGv+W\|H^{-1}J_0v\|^2.                         \tag{4.10}
\]
For symmetric `2 x 2` `H`,

\[
H^{-1}J_0=(\det H)^{-1}J_0H,                                 \tag{4.11}
\]
so

\[
\|H^{-1}J_0v\|^2=\|Hv\|^2/(\det H)^2.                      \tag{4.12}
\]
Substituting (4.10)-(4.12) into (4.7) proves (4.6). QED.

Equation (4.6) is the exact structural compensation sought in the small-pair-currency branch: as the outer pair degenerates, the second shear-volume term is multiplied by `1/|det H|`, not lost.

### Pure zero-diagonal hyperbolic pair

If

\[
H=\begin{pmatrix}0&c\\c&0\end{pmatrix},\qquad c\ne0,       \tag{4.13}
\]
then

\[
|\det H|=c^2,\qquad \|Hv\|^2=c^2.                           \tag{4.14}
\]
Therefore (4.6) becomes

\[
|\operatorname{pdet}_*(A_0)|
=|\lambda|\,[c^2v^TGv+W]
\ge |\lambda|W.                                              \tag{4.15}
\]
The rank-three core volume does **not** vanish as `c -> 0`.

Let `U_0` be any orthonormal basis of `range(A_0)` and write `A_0=U_0\Lambda_0U_0^T`. If its physical range leverage is diffuse,

\[
\max_i\|(U_0)_{i,*}\|^2\le\frac12,                          \tag{4.16}
\]
then the completed separable-phase Brascamp--Lieb theorem applies to

\[
X^TA_0X+\sum_jd_jX_j^2                                      \tag{4.17}
\]
with the **whole diagonal `D` retained as a coordinate-separable phase**. Consequently the full ambient form has a continuous `C_0` density and

\[
\boxed{
\|p_Q\|_\infty
\le3e\,|\operatorname{pdet}_*(A_0)|^{-1/3}
\le3e\,(|\lambda|W)^{-1/3}.}                                \tag{4.18}
\]
Numerically `3e=8.154845485377136...`.

If (4.16) fails, the rank-three range projection has trace three, so there are at most five literal physical coordinates with leverage `>1/2`. Thus the pure zero-diagonal small-pair face has been reduced to either the continuous-density payment (4.18) or a finite physical heavy-core certificate. This is a true structural reduction; it is not asserted that the target spectral hypothesis by itself forces `|lambda|W` to be uniformly bounded below.

## 5. Designated account04/B06 theorem applied to the new core split

The freshest completed designated-partner result read in this run is

`yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260924T001014Z-account04-B06-QFORM-r3/REPORT.md`,

`QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`.

Whiten the actual environment frame:

\[
F=G^{-1/2}E.                                                    \tag{5.1}
\]
Its two rows are orthonormal, and the physical coordinate leverages are exactly

\[
\alpha_j=e_j^TG^{-1}e_j.                                      \tag{5.2}
\]
Assume the actual diffuse inequality

\[
\max_j\alpha_j\le\frac12.                                    \tag{5.3}
\]
The rank-one Schur direction becomes a unit row `V` in this two-frame with coefficient

\[
\rho=\lambda v^TGv.                                           \tag{5.4}
\]
Choose the orthogonal row `L` in the same whitened plane. Then `L_j^2+V_j^2=\alpha_j<=1/2`, so the designated partner theorem applies directly. Taking its `beta=0` specialization, hence requiring no extra leakage at all, the off-fold joint pushforward of

\[
(L,\rho V^2)\mathbf1_{\{|V|>1/64\}}                           \tag{5.5}
\]
has a continuous density `g_off` satisfying the actual inequality

\[
\boxed{\|g_{\rm off}\|_\infty\le\frac{256}{|\rho|}.}        \tag{5.6}
\]

Let

\[
P:=|\operatorname{pdet}_*(A_0)|.                               \tag{5.7}
\]
The first term in the exact split (4.6) is precisely `|det H| |rho|`. Hence if that term carries at least half of the core volume,

\[
|\det H|\,|\rho|\ge P/2,                                     \tag{5.8}
\]
then the designated-partner result yields the concrete core inequality

\[
\boxed{\|g_{\rm off}\|_\infty\le512\,|\det H|/P.}           \tag{5.9}
\]

If (5.8) fails, the second term in (4.6) carries more than half the entire rank-three core volume:

\[
\boxed{
\frac{|\lambda|W}{|\det H|}\|Hv\|^2>P/2.}                   \tag{5.10}
\]
This is the exact shear-volume alternative that should feed the next compiler. I do **not** promote the partner's two-output off-fold estimate to a scalar density estimate through the same-bank diagonal `D`; that operation is outside its theorem. The full scalar payments in this report are (2.5)/(3.15) and the diffuse rank-three-core payment (4.18).

## 6. Checks

A deterministic finite checker accompanies this report. On random invertible symmetric `2 x 2` matrices, rank-two `E`, unit `v`, and nonzero `lambda`, it verifies:

- the factorization `A_0=R^TM_3R`;
- the Cauchy--Binet identity (4.10) and its simplified form (4.12);
- the packet identity (3.7);
- the kernel-curvature identity (3.8)-(3.9);
- the deletion determinant `det(E_JE_J^T)=W(1-alpha_j)`;
- the cross singular-product lower bound (3.14);
- the pure-zero-diagonal inequality `P>=|lambda|W`;
- the numerical constants in (2.8) and (4.18).

The numerical tests are sanity checks only; the proofs above are algebraic/analytic.

## 7. Scope and next exact debt

New proved supporting results in this run:

1. `QFORM-RANK2-CROSS-TRANSVERSE-SHEAR-RIGHTBANK-v1`: the zero-kernel-curvature shear receiver now allows an arbitrary original-coordinate right bank and gives a continuous density with constant `<7.713`.
2. `QFORM-SINGULART-CORE-PSEUDODET-SPLIT-v1`: the exact rank-three singular-T core has pseudodeterminant (4.6).
3. `QFORM-PURE-HYPERBOLIC-SINGULART-DIFFUSE-v1`: on the pure zero-diagonal outer pair, a diffuse rank-three core gives the continuous full-scalar bound (4.18), completely uniform in the vanishing outer coefficient `c`; failure gives at most five literal heavy core coordinates.
4. The designated account04/B06 r3 theorem is applied at the actual inequality (5.9), with its scope kept as a two-output off-fold density estimate.

The full QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.

The next exact B06 debt is

`QFORM-SMALLPAIR-SHEARVOLUME-HEAVYCORE-COMPILER-v1`:

> Starting from the exact split (4.6), if the physical pair currency `|det H| sigma_min(H)` is small and the diffuse rank-three-core gate fails, consume the resulting finite `>1/2` core-leverage hubs together with the shear-volume alternative (5.10), while retaining the diagonal environment phase `D` and all nonzero tail curvature. A successful compiler should either enter the completed physical-pivot/rank-two-cross receivers or a product-weighted three-coordinate curved packet without selecting a dimension-dependent largest fiber.

Repository transport has been used, but no authenticated native brain receiver was available in this run; execution therefore remains `WITHOUT_VERIFIED_BRAIN`.
