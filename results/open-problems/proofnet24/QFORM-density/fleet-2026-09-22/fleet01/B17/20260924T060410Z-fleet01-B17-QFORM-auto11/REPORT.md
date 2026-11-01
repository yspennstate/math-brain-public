# QFORM-ESCAPING-MODE-DIVERGENT-SUBCRITICAL-MASS-v1

**Worker:** fleet01 / B17 — sharp constant and witnesses  
**Status:** supporting sharp-witness theorem; full unrestricted QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains separate.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

This run strengthens the source-valid lower-obstruction family in three directions at once: the witness matrices are full rank and strictly beyond the three-eigenvalue threshold, the aggregate absolute mass of the remaining subcritical spectrum diverges, and the near-sharp density peak escapes to output levels tending to infinity. A second version permits remote fragmented cap-one input supports and gives an exact variance-tax profile. The strongest source-valid lower obstruction remains
\[
C_{\rm univ}\ge 3\sqrt2.
\]
No claim that `3 sqrt(2)` is the unrestricted sharp constant is made.

## 1. Exact full-rank dense strict-target family

Let
\[
B=I_3-\frac23\mathbf 1\mathbf 1^T
=\frac13\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix},\qquad B^2=I_3,
\]
so `spec(B)={1,1,-1}`. For an integer `k>=2`, set
\[
m=k^4,\qquad N=3m.
\]
Partition the physical coordinates into three banks of size `m`. Let `R` be the `3m x 3` synthesis matrix whose rows in bank `j` are all `e_j/sqrt(m)`. Then
\[
R^TR=I_3,\qquad P:=RR^T
\]
is the orthogonal projection onto the bank-constant subspace.

Put
\[
\alpha_k=1+\frac1m=1+k^{-4},\qquad
\eta_k=\frac{k}{m}=k^{-3},
\]
and, for either sign `sigma in {+1,-1}`, define
\[
\boxed{
A_k^\sigma=\alpha_k RBR^T+\sigma\eta_k(I-P).
}\tag{1.1}
\]
The two summands act on orthogonal invariant subspaces. Therefore
\[
\boxed{
\operatorname{spec}(A_k^\sigma)=
\left\{\alpha_k,\alpha_k,-\alpha_k,
\underbrace{\sigma\eta_k,\ldots,\sigma\eta_k}_{3m-3}\right\}.
}\tag{1.2}
\]
Every matrix is full rank, and the three target eigenvalues satisfy `|lambda|=1+k^{-4}>1`.

The subcritical spectrum is individually tiny but collectively large:
\[
\boxed{
\sum_{j=4}^{3m}|\lambda_j(A_k^\sigma)|
=(3m-3)\eta_k
=3k-\frac3{k^3}\longrightarrow\infty.
}\tag{1.3}
\]
Thus a proof cannot infer a fixed gain below the sharp known obstruction merely from full rank or from large total absolute mass in eigenvalues below one.

### 1.1 Entrywise density

For coordinates in different banks,
\[
(A_k^\sigma)_{ij}=-\frac{2(k^4+1)}{3k^8}\ne0.
\]
For distinct coordinates in the same bank,
\[
(A_k^\sigma)_{ij}=
\frac{k^4+1-3\sigma k}{3k^8}.
\]
For `k>=2`, `k^4-3k+1>0`, so these entries are nonzero for both signs. On the diagonal,
\[
(A_k^\sigma)_{ii}
=\frac{k^4+1+3\sigma k(k^4-1)}{3k^8}.
\]
For `sigma=+1` this is positive; for `sigma=-1`,
`3k(k^4-1)>k^4+1` for `k>=2`, so it is negative. Hence **every physical entry is nonzero**.

### 1.2 Target spectrum remains invisible to every small physical principal block

For a physical subset `S`, let `s=|S|`. If `k_j` coordinates are selected from bank `j`,
\[
R_S^TR_S=\operatorname{diag}(k_1/m,k_2/m,k_3/m),
\qquad
\|R_S\|_{op}^2\le s/m.
\]
Hence
\[
\|A_k^\sigma[S]\|_{op}
\le \alpha_k\frac{s}{m}+\eta_k.
\tag{1.4}
\]
If `s<=m-k-1`, then the right-hand side is exactly bounded by
\[
\alpha_k\frac{m-k-1}{m}+\eta_k
=1-\frac{k+1}{k^8}<1.
\tag{1.5}
\]
Therefore any original-coordinate principal submatrix having even **one** eigenvalue of modulus at least one must contain at least
\[
\boxed{m-k=N/3-N^{1/4}/3^{1/4}}
\]
coordinates. Bounded-coordinate extraction is maximally incompatible with this near-sharp family.

The one-coordinate action also vanishes. Since
\[
(A_k^\sigma)^2=\alpha_k^2P+\eta_k^2(I-P),\qquad P_{ii}=1/m,
\]
we have
\[
\boxed{
\|A_k^\sigma e_i\|_2^2
=\frac{\alpha_k^2}{m}+\eta_k^2\left(1-\frac1m\right)
=\frac{k^2(k^4-1)+(k^4+1)^2}{k^{12}}
\longrightarrow0.
}\tag{1.6}
\]

## 2. Centered unit intervals: the near-sharp peak escapes to infinity

First take all physical inputs iid
\[
X_i\sim U[-1/2,1/2].
\]
Let
\[
Y=R^TX,
\]
so the three coordinates of `Y` are independent normalized sums of `m` centered unit intervals, each with variance `1/12`. Hence
\[
Y\Rightarrow G\sim N(0,I_3/12).
\tag{2.1}
\]
Write
\[
S_k=\frac1m X^T(I-P)X=T_k-U_k,
\]
where
\[
T_k=\frac1m\sum_{i=1}^{3m}X_i^2,
\qquad
U_k=\frac1m\sum_{j=1}^3Y_j^2.
\]
Since `E X_i^2=1/12` and `Var(X_i^2)=1/180`,
\[
E T_k=\frac14,\qquad
\operatorname{Var}(T_k)=\frac1{60m}=\frac1{60k^4},
\]
while `E U_k=1/(4m)`. Consequently
\[
E\left|k\left(S_k-\frac14\right)\right|
\le \frac1{\sqrt{60}\,k}+\frac1{4k^3}\longrightarrow0.
\tag{2.2}
\]
Since
\[
X^TA_k^\sigma X
=\alpha_kY^TBY+\sigma k S_k,
\]
define the translated output
\[
W_k^\sigma=X^TA_k^\sigma X-\sigma\frac{k}{4}.
\]
By (2.1)-(2.2),
\[
\boxed{
W_k^\sigma\Rightarrow G^TBG.
}\tag{2.3}
\]
Because the Gaussian limit is isotropic and `B` is a reflection,
\[
G^TBG\stackrel d=G_1^2+G_2^2-G_3^2.
\]
Its density is globally maximized at zero and
\[
\boxed{
\|p_\infty\|_\infty=p_\infty(0)=3\sqrt2.
}\tag{2.4}
\]

### 2.1 Uniform convergence of the complete finite-stage densities

This witness lies directly inside the completed Fresnel--Brascamp--Lieb theorem (`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, Theorem F).
Indeed
\[
A_k^\sigma
=\sigma\eta_k I+R(\alpha_kB-\sigma\eta_kI_3)R^T.
\tag{2.5}
\]
The residual `sigma eta_k I` is diagonal. After diagonalizing the latent rank-three matrix, the physical eigenframe still has Gram matrix `I_3` and every row has leverage `1/m<=1/2`. Its three latent eigenvalue magnitudes are among
\[
\alpha_k-\eta_k,\qquad \alpha_k+\eta_k,
\]
and for every `k>=2`, `alpha_k-eta_k>=15/16`. Thus Theorem F gives one source-law-independent integrable envelope
\[
|\phi_k(t)|\le
\min\{1,C_0|t|^{-3/2}\}
\tag{2.6}
\]
with one universal `C_0`. Translating by `sigma k/4` changes only the phase of the characteristic function. Pointwise convergence from (2.3), dominated convergence in `L^1(dt)`, and Fourier inversion give
\[
\boxed{
\|p_{W_k^\sigma}-p_\infty\|_\infty\longrightarrow0.
}\tag{2.7}
\]
In particular every finite-stage output in this family has a continuous bounded density and
\[
\boxed{
\|p_{X^TA_k^\sigma X}\|_\infty
=\|p_{W_k^\sigma}\|_\infty
\longrightarrow3\sqrt2.
}\tag{2.8}
\]
This is a source-valid lower obstruction for the unrestricted problem, but only a family-specific continuity statement.

The maximizing region escapes every fixed output compact. Put `c_k^sigma=sigma k/4`. For each fixed `R>0`, (2.7) implies
\[
\sup_{|s|\le R}p_{X^TA_k^\sigma X}(s)
\le
\|p_{W_k^\sigma}-p_\infty\|_\infty
+
\sup_{|u+c_k^\sigma|\le R}p_\infty(u)
\longrightarrow0,
\tag{2.9}
\]
whereas the global norm tends to `3sqrt(2)`. Thus a proposed sharp proof must be genuinely uniform in the output level; a cone-tip-at-zero estimate alone cannot capture all near-extremizers after subcritical full-rank perturbations.

## 3. Remote fragmented cap-one laws: exact variance-tax extension

The preceding escaping-mode effect survives genuinely remote fragmentation. Let now
\[
\varepsilon_k=\frac1k,\qquad \ell_k=1-\frac1k,
\]
and choose a bounded sequence `tau_k>=0` with
\[
\tau_k\to\tau\ge0,\qquad k\tau_k\to\infty.
\]
Put
\[
R_k=\sqrt{k\tau_k}.
\]
For every sufficiently large `k`, use in every physical coordinate the symmetric density
\[
\boxed{
\begin{aligned}
f_k(x)=&\;\mathbf1_{[-\ell_k/2,\ell_k/2]}(x)\\
&+\mathbf1_{[R_k-\varepsilon_k/4,R_k+\varepsilon_k/4]}(x)\\
&+\mathbf1_{[-R_k-\varepsilon_k/4,-R_k+\varepsilon_k/4]}(x).
\end{aligned}}
\tag{3.1}
\]
The total support length is `ell_k+epsilon_k=1`, so `f_k` is an exact probability density bounded by one. The support gap tends to infinity. In each bank the expected number of satellite samples is
\[
m\varepsilon_k=k^3\to\infty,
\]
and the all-main probability over all `3m` coordinates is
\[
(1-1/k)^{3k^4}\to0.
\tag{3.2}
\]
Thus this is not a central-cell perturbation in sample space.

### 3.1 Exact moments and bank CLT

The latest completed fleet02/B17 variance-tax report (`math-open-problems@7394e198725409756e0775da22e8dd9f0ef5900b`, run `20260924T054220Z-fleet02-B17-QFORM-auto11`) supplies the exact second and third absolute moments for this satellite law. In the present notation,
\[
\boxed{
v_k:=E X^2
=\frac{\ell_k^3}{12}+\varepsilon_kR_k^2+rac{\varepsilon_k^3}{48}
\longrightarrow v:=\frac1{12}+\tau,
}\tag{3.3}
\]
and
\[
E|X|^3
=\frac{\ell_k^4}{32}+\varepsilon_kR_k^3+rac{\varepsilon_k^3R_k}{16}.
\tag{3.4}
\]
Since `sqrt(m)=k^2` and
\[
\frac{\varepsilon_kR_k^3}{\sqrt m}
=\frac{\tau_k^{3/2}}{k^{3/2}}\to0,
\]
the Lyapunov ratio tends to zero. Therefore the three independent bank sums satisfy
\[
Y=R^TX\Rightarrow G\sim N(0,vI_3).
\tag{3.5}
\]

For the residual energy we need one more exact moment. Direct integration of (3.1) gives
\[
\boxed{
E X^4
=\frac{\ell_k^5}{80}
+\varepsilon_kR_k^4
+\frac{\varepsilon_k^3R_k^2}{8}
+\frac{\varepsilon_k^5}{1280}.
}\tag{3.6}
\]
Because `tau_k` is bounded and `R_k^2=k tau_k`, this is `O(k)`. Let
\[
T_k=\frac1m\sum_{i=1}^{3m}X_i^2,
\qquad U_k=\frac1m\sum_{j=1}^3Y_j^2,
\qquad S_k=T_k-U_k.
\]
Then
\[
E T_k=3v_k,
\qquad
\operatorname{Var}(T_k)\le \frac{3EX^4}{m}=O(k^{-3}),
\]
so
\[
k(T_k-3v_k)\to0\quad\text{in }L^1.
\tag{3.7}
\]
Also `E U_k=3v_k/m`, and hence
\[
k\left(U_k-\frac{3v_k}{m}\right)\to0\quad\text{in }L^1.
\tag{3.8}
\]
Thus
\[
\boxed{
k\left[S_k-3v_k\left(1-\frac1m\right)\right]\to0
\quad\text{in }L^1.}
\tag{3.9}
\]

Set the exact deterministic center
\[
\boxed{
c_k^\sigma=\sigma\,3kv_k\left(1-\frac1m\right).}
\tag{3.10}
\]
Then (3.5) and (3.9) give
\[
X^TA_k^\sigma X-c_k^\sigma
\Rightarrow G^TBG,
\qquad G\sim N(0,vI_3).
\tag{3.11}
\]
The same Theorem-F envelope (2.6) is independent of the detailed cap-one source law, so the argument of Section 2.1 again upgrades this to global uniform convergence of densities. The completed fleet02/B17 Gaussian profile then gives
\[
\boxed{
\|p_{X^TA_k^\sigma X}\|_\infty
\longrightarrow
\frac1{2\sqrt2\,v}
=\frac{3\sqrt2}{1+12\tau}.
}\tag{3.12}
\]
Moreover `|c_k^sigma|~3kv`, so the entire limiting profile travels to `+infinity` or `-infinity` according to `sigma`.

### 3.2 Near-sharp remote fragmentation with zero asymptotic tax

Take, for example,
\[
\tau_k=k^{-1/2}.
\]
Then
\[
R_k=k^{1/4}\to\infty,
\]
the expected satellite count is `3k^3`, the all-main probability tends to zero, the matrix is full rank with residual spectral `l1` mass `3k+o(1)`, and yet
\[
\boxed{
\|p_{X^TA_k^\sigma X}\|_\infty\to3\sqrt2.
}\tag{3.13}
\]
This packages remote fragmented supports, divergent residual spectral mass, strict target eigenvalues, vanishing physical leverage, entrywise-dense coupling, and an escaping near-sharp mode in one exact source-valid family.

## 4. Required concrete use of the completed fleet02/B17 theorem

The designated partner result is the completed and checked theorem `QFORM-SYMMETRIC-SATELLITE-DIFFUSIVE-GLOBAL-BARRIER-v1`, source report
`math-open-problems@7394e198725409756e0775da22e8dd9f0ef5900b`, with checker PASS at `5a583c1b2926d0ebfceb016de9e26e244c42a78b`.
It proves for its exact dense rank-three target family that under isotropic variance tax `tau`,
\[
\|p_{Q_m}\|_\infty\longrightarrow\frac{3\sqrt2}{1+12\tau}.
\tag{4.1}
\]
Apply the theorem at the actual value
\[
\tau=\frac1{12}.
\]
For the explicit satellite density (partner formula (2.2)) and exact dense target matrix with nonzero spectrum `{1,1,-(1+1/m)}`,
\[
\boxed{
\|p_{Q_m}\|_\infty\longrightarrow\frac3{\sqrt2}
=2.121320343559642\ldots .
}\tag{4.2}
\]
Therefore, without any heuristic numerical input,
\[
\boxed{
\exists m_0\ \forall m\ge m_0:\quad
\|p_{Q_m}\|_\infty<2.13<3\sqrt2.
}\tag{4.3}
\]
This is a concrete arbitrary-law-cap-one theorem application, not merely a citation. Section 3 shows that the same limiting inequality survives our additional full-rank subcritical perturbation when `m=k^4`.

## 5. Constraint on a proposed universal proof

The source-valid universal lower obstruction remains
\[
\boxed{C_{\rm univ}\ge3\sqrt2=4.242640687119\ldots .}
\]
The new family shows that a sharp or near-sharp proof cannot rely on any of the following as a concentration-reducing condition by itself:

1. full rank;
2. all three target eigenvalues being strictly beyond one;
3. a divergent sum of absolute values of all remaining subcritical eigenvalues;
4. entrywise-dense physical coupling;
5. an order-one physical entry or order-one one-coordinate leverage (both vanish here);
6. existence of a bounded-size target-scale principal block (none exists here);
7. localization of the output peak near zero or any fixed compact set;
8. concentration of the physical input near one connected central interval (the remote fragmented version violates this overwhelmingly).

A successful full proof must remain uniform in output translation and preserve aggregate product geometry. This theorem does not exclude stronger non-Gaussian multiscale mechanisms outside the present diffuse CLT basin, and it does not prove that `3sqrt(2)` is the sharp universal constant.

## 6. Corrections preserved

No independence after arbitrary finite-input spectral rotation is used. No law-uniform pointwise quadratic-phase decay is used. No arbitrary-joint coarea cap is used. No positive conditional-projection density moment is used. No fiber supremum is treated as dimension free. The finite-stage uniform-density convergence is obtained only inside the exact Theorem-F leverage/diagonal-residual scope. Full QFORM remains open, and continuity for the unrestricted target is not inferred.
