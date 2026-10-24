SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-24T01:06:59Z.
attacking: endpoint regularity at the square-kernel threshold, and a fully coupled indefinite physical-triple receiver; apply the newest account02/B15 Schur result at an actual target inequality without using continuity to pay height.

# account01/B15 — endpoint Lorentz square compiler and a sharper coupled physical-triple receiver

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.
Status: `NEW_ENDPOINT_REGULARITY_LEMMA / NEW_COUPLED_TRIPLE_RECEIVER / PARTNER_APPLIED / FULL_QFORM_OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN:

\[
\sup_{\substack{n\ge3,\ s_3(A)\ge1\\ X_i\text{ independent},\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty<\infty.
\]

The new result is a sharp endpoint regularity compiler at Lorentz `L^{2,1}`. It strengthens my preceding `p>2` square compiler, identifies the exact endpoint missed by that argument, and yields a cleaner quantitative receiver for a fully coupled physical triple. Continuity is proved after / together with the local height certificate; it is never used to manufacture the universal height.

## 1. Sources and corrections

Fresh owner control was reread before publication; QFORM remains the sole target and no later stop was observed. The live corrections are retained: no law-uniform pointwise quadratic Fourier decay; no independence after spectral rotation; no arbitrary-joint rank-three coarea height bound; no projection/X-ray-only shortcut; no worst-fibre grouped closure after adding arbitrary leaf curvature.

The latest designated-partner artifact present when this report was prepared is the account02/B15 checkpoint `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260924T004218Z-account02-B15-qform-auto11/CHECKPOINT.md`, blob `be05e4f670a374c97148c2a7da8c8ac5fa81119a`, read on master at head `12b802771377dbfec07f4da8601e99828c846b16`. It proves a collective rank-two Schur estimate and a sharper same-sign residual estimate. I apply that source at an actual target inequality in Section 7.

I also apply the completed preceding account02/B15 theorem `math-open-problems@81b639f85e91328176f0dcdd52b5f3c95ce71ab9`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T230534Z-account02-B15-qform-auto11/REPORT.md`, whose completed collective rank-one Schur theorem is used in Section 7. The physical-pair logarithmic envelope is source-pinned at `math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, path `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

The fixed-matrix qualitative regularity theorem is `math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`: for every fixed symmetric `A` with `rank(A)>=3`, every cap-one product input gives an instance-dependent bounded density with a representative in `C_0(R)`. Its constants are not universal in `A`.

## 2. Regularity ledger

**Absolute continuity.** If the joint input law is absolutely continuous and `A!=0`, then `X^TAX` is absolutely continuous. Neither independence, the cap, nor rank three is needed. This follows from coarea away from `ker A`, or by original-coordinate conditioning.

**Universal bounded density.** The still-open central target is `D_infinity(Law(X^TAX)) <= C/s_3(A)` with one matrix-, dimension-, and law-independent `C`.

**Continuous density.** In the target class `rank(A)>=3`, the source-pinned fixed-matrix theorem already gives an instancewise `C_0` representative. Therefore, if the missing universal essential bound is eventually proved, that same representative obeys the identical pointwise bound: a continuous function that exceeds the essential bound at one point exceeds it on an interval. Continuity is strictly stronger regularity, but it costs no extra constant after height is known.

## 3. Endpoint Lorentz square compiler

For a nonnegative integrable function `g` on `R`, let `g*` be its decreasing rearrangement and define

\[
\Lambda_2(g):=\int_0^\infty u^{-1/2}g^*(u)\,du.
\tag{3.1}
\]

### Theorem 3.1 — `QFORM-B15-L21-SQUARE-C0-COMPILER-v1`

Let `(R,V)` have a joint probability density `K(r,v)`. Assume: (i) for a.e. `r`, `K(r,.) in C_0(R)`; (ii) for a probability density `g`, `0<=K(r,v)<=g(r)` a.e.; (iii) `Lambda_2(g)<infinity`. For `b!=0`, put `T=R+bV^2`. Then `T` has a density in `C_0(R)` and

\[
\boxed{\|p_T\|_\infty\le |b|^{-1/2}\Lambda_2(g).}
\tag{3.2}
\]

**Height proof.** Set `a=|b|`, `sigma=sign(b)`. Change variables in `v`:

\[
p_T(t)=\frac1{2\sqrt a}\int_{\sigma(t-r)>0}
\frac{K(r,+\sqrt{|t-r|/a})+K(r,-\sqrt{|t-r|/a})}{\sqrt{|t-r|}}dr.
\tag{3.3}
\]

Hence

\[
p_T(t)\le a^{-1/2}\int_0^\infty g(t-\sigma s)s^{-1/2}ds.
\tag{3.4}
\]

The one-sided kernel `h(s)=s^{-1/2}1_{s>0}` has rearrangement `h*(u)=u^{-1/2}`. Hardy--Littlewood gives (3.2).

**Continuity.** Split (3.3) at `|t-r|<delta`. The near piece is uniformly at most

\[
a^{-1/2}\int_0^\delta u^{-1/2}g^*(u)du\to0.
\tag{3.5}
\]

On the far piece, sectionwise continuity and domination by `2g(r)/sqrt(delta)` give dominated convergence. Thus `p_T` is continuous.

**Vanishing at infinity.** Use the same near/far split. Make the near piece small by (3.5), then choose `M` so the `g`-mass outside `[-M,M]` is small. On `|r|<=M`, the active square-root argument tends to infinity as `|t|->infinity`, so `K(r,.) in C_0` and dominated convergence applies. Therefore `p_T(t)->0`. QED.

If `R` and `V` are independent, the section hypothesis is unnecessary: the square density is an `L^1` probability density dominated by `a^{-1/2}s^{-1/2}` on one half-line, Hardy--Littlewood gives the same height, and convolution of two `L^1` densities lies in `C_0`.

## 4. The endpoint is sharp in the Lorentz scale

On `0<x<e^{-2}`, take

\[
g_0(-x)=\frac{c}{\sqrt x\log(1/x)},
\tag{4.1}
\]

with `c>0` small and add a bounded density away from zero so total mass is one. Near zero `u^{1/2}g_0^*(u) asymp 1/log(1/u)`. Consequently

\[
g_0\in L^{2,q}\ \text{for every }q>1,
\qquad g_0\notin L^{2,1}.
\tag{4.2}
\]

Let `V` be independent with triangular density `(1-|v|)_+` on `[-1,1]`. For `T=R+V^2`, as `tau downarrow0`,

\[
p_T(-\tau)\gtrsim\int_0^{v_0}
\frac{dv}{\sqrt{\tau+v^2}\log(1/(\tau+v^2))}\to\infty.
\tag{4.3}
\]

Thus no compiler based only on bounded `L^{2,q}`, `q>1`, can imply boundedness after adding one square. `L^{2,1}` is the genuine endpoint for this abstract mechanism. This is not a QFORM counterexample.

## 5. Endpoint bound for an indefinite physical pair

Let `F` be an affine quadratic in two independent cap-one variables with an invertible indefinite ORIGINAL-coordinate matrix `S`. Put `D=|det S|`, `kappa=sigma_min(S)`. The completed pair theorem gives, for every `r>0`, a nonnegative decomposition `p_F=p_far+p_near` with

\[
\|p_{far}\|_\infty\le{2\sqrt2\over r},\qquad
p_{near}(t)\le D^{-1/2}\log_+{2r^2\over\kappa|t-t_0|}.
\tag{5.1}
\]

### Lemma 5.1 — `QFORM-B15-INDEFINITE-PAIR-L21-v1`

\[
\boxed{\Lambda_2(p_F)\le6\sqrt2(D\kappa)^{-1/6}.}
\tag{5.2}
\]

If a subdensity `h` has mass at most one and height at most `A`, the bathtub principle gives `Lambda_2(h)<=2sqrt(A)`. Hence

\[
\Lambda_2(p_{far})\le2^{7/4}r^{-1/2}.
\tag{5.3}
\]

For `e(x)=D^{-1/2}log_+(C/|x|)`, `C=2r^2/kappa`,

\[
e^*(u)=D^{-1/2}\log(2C/u),\quad0<u<2C,
\]

and direct integration gives

\[
\Lambda_2(e)={8r\over\sqrt{D\kappa}}.
\tag{5.4}
\]

`Lambda_2` is subadditive on nonnegative functions by rearrangement submajorization and integration against the decreasing weight `u^{-1/2}`. Therefore

\[
\Lambda_2(p_F)\le2^{7/4}r^{-1/2}+{8r\over\sqrt{D\kappa}}.
\]

The optimizer `r=2^{-3/2}(Dkappa)^{1/3}` gives exactly (5.2). QED.

## 6. Sharper fully coupled physical-triple receiver

### Theorem 6.1 — `QFORM-B15-COUPLED-PIVOT-L21-C0-v1`

Let `Y=(U_1,U_2,Z)` have independent probability densities bounded by one. Let

\[
B=\begin{pmatrix}C&a\\a^T&b\end{pmatrix},\qquad b\ne0,
\tag{6.1}
\]

be invertible symmetric, and put

\[
S=C-aa^T/b,\qquad D=|\det S|,\qquad\kappa=\sigma_{min}(S).
\tag{6.2}
\]

Assume `S` is indefinite. Then every affine quadratic `Y^TBY+2ell^TY+c` has a density in `C_0(R)` satisfying

\[
\boxed{\|p\|_\infty\le6\sqrt2\,|b|^{-1/2}(D\kappa)^{-1/6}.}
\tag{6.3}
\]

No assumption `a!=0` is required.

Translate the three ORIGINAL coordinates by `B^{-1}ell`; independence and the cap are preserved. Up to output translation,

\[
Y^TBY=R(U)+b(Z+M(U))^2,\quad R(U)=U^TSU,\quad M(U)=a^TU/b.
\tag{6.4}
\]

By Lemma 5.1, `Lambda_2(p_R)<=6sqrt(2)(Dkappa)^(-1/6)`. If `a=0`, use the independent special case of Theorem 3.1. If `a!=0`, the map `Psi(U)=(R(U),M(U))` has derivative rows `2SU` and `a^T/b`; rank fails only when `SU` is parallel to `a`, a line and hence a null set. By the area formula `(R,M)` has joint density `H(r,m)`. For `V=Z+M`,

\[
K(r,v)=\int H(r,m)f_Z(v-m)dm.
\tag{6.5}
\]

For a.e. `r`, `K(r,.)` is an `L^1*L^1` convolution and belongs to `C_0`; and since `f_Z<=1`, `K(r,v)<=int H(r,m)dm=p_R(r)`. Theorem 3.1 gives (6.3) and `C_0`. QED.

Conditioning on arbitrary outside ORIGINAL coordinates only changes affine/constant terms, so the same bound and `C_0` conclusion hold for an ambient form containing such a principal triple.

For the exact-target matrix

\[
B_*=\begin{pmatrix}5/4&-9/8&-9/8\\-9/8&5/4&-9/8\\-9/8&-9/8&5/4\end{pmatrix},
\]

`spec(B_*)={19/8,19/8,-1}` and every physical `2x2` principal pair is positive definite. Taking the third coordinate as pivot gives

\[
S=\begin{pmatrix}19/80&-171/80\\-171/80&19/80\end{pmatrix},
\quad spec(S)=\{19/8,-19/10\},
\]

so `D=361/80`, `kappa=19/10`, `b=5/4`. Thus

\[
\boxed{\|p_{X^TB_*X}\|_\infty\le{12\,2^{4/3}\over5^{1/6}\sqrt{19}}<5.305,\qquad p\in C_0.}
\tag{6.6}
\]

## 7. Local indefinite-triple dichotomy and partner applications

Let `B` be an invertible indefinite original-coordinate `3x3` block. For signature `(2,1)`, if a positive physical diagonal exists, use it as scalar pivot; inertia additivity forces its `2x2` Schur complement to have signature `(1,1)`, so Theorem 6.1 applies. If no positive physical diagonal exists, all physical diagonals are nonpositive. If no physical `2x2` pair were indefinite, all principal minors of `-B` would be nonnegative; since `det(-B)>0`, the principal-minor criterion would make `-B` positive definite, contradiction. Hence an indefinite pair exists, its scalar Schur complement is nonzero, and the completed account02/B15 collective rank-one Schur theorem gives

\[
\boxed{\|p\|_\infty\le8\sqrt2\bigl(|\det D_2|\sigma_{min}(D_2)|\sigma|\bigr)^{-1/4}.}
\tag{7.1}
\]

Signature `(1,2)` follows by sign reversal. Thus every invertible indefinite physical triple has one of these two explicit original-product receivers. The local parameters can still degenerate in diffuse high-dimensional matrices, so this is not the full QFORM theorem.

**Completed partner applied at an actual target inequality.** For

\[
B_0=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix},\qquad spec(B_0)=\{2,-1,-1\},
\]

choose `D_2=[[0,1],[1,0]]`, so `Delta=kappa=1` and the scalar Schur complement is `sigma=-2`. Equation (7.1) gives, for every independent cap-one input triple,

\[
\boxed{\|p_{X^TB_0X}\|_\infty\le8\,2^{1/4}<9.514.}
\tag{7.2}
\]

Since rank is three, the fixed-matrix theorem supplies a `C_0` representative carrying this identical pointwise bound. Continuity is added after the partner theorem pays height.

**Newest partner checkpoint applied at an actual target inequality.** Its same-sign rank-two Schur estimate states

\[
\|p_Q\|_\infty\le\Delta^{-1/2}\left[3+\log_+{16\pi\Delta\over\kappa\sqrt{|\eta_1\eta_2|}}\right].
\tag{7.3}
\]

For `Q=2XY+Z^2+W^2`, the matrix eigenvalues are `1,-1,1,1`. Taking `D=[[0,1],[1,0]]` and Schur residual `S=I_2` gives `Delta=kappa=eta_1=eta_2=1`, hence

\[
\boxed{\|p_{2XY+Z^2+W^2}\|_\infty\le3+\log(16\pi)<6.918.}
\tag{7.4}
\]

Again rank four gives a `C_0` representative with the same pointwise bound.

## 8. Exact remaining implication

This run proves an endpoint residual target: an `L^{2,1}` envelope is enough to turn a third square into `L^infinity cap C_0`, while `L^{2,q}`, every `q>1`, can fail. It also closes every single invertible indefinite physical triple by explicit original-coordinate receivers. What remains is global structural aggregation. The hypothesis `s_3(A)>=1` does not force a physical triple whose local determinants/Schur curvatures remain bounded away from zero. A full proof still has to aggregate product geometry before reciprocal local parameters are paid, or route the diffuse residual into a proved ridge/volume/grouped receiver with uniform parameters.

No uniform continuity modulus is claimed. Full unrestricted QFORM remains OPEN.
