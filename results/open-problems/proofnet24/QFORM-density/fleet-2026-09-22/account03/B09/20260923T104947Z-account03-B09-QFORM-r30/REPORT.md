SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T10:49:47Z.
attacking: grouped cross-rank-three smoothing with arbitrary same-bank curvature, using the new account04/B09 dense-self-coupling theorem as the physical-coordinate endpoint.

# account03/B09 r30 — grouped cross-rank smoothing and the exact rank-two residual

## Status

This run proves a new source-coordinate theorem: **any disjoint original-coordinate cut whose physical cross block has rank `r>2` with quantitative product of nonzero singular values yields a continuous density and a linear small-interval bound, even when both same-side quadratic blocks are completely arbitrary and dense.** The proof aggregates each side of the cut to the singular subspace before taking any reciprocal minor. It uses only product-projection density caps, disintegration, Cauchy--Schwarz and Plancherel.

The full three-large-eigenvalue QFORM conjecture remains **OPEN**. The new theorem does not force such a rank-three cut from the bare spectral hypothesis. Continuity is proved only in the stated cross-rank branch.

No Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis assumption, post-rotation independence, law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea bound, or naive fiber supremum is used.

Execution status: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval and writes were used; no verified native learned-memory receiver use occurred.

## 1. Source pins actually consumed

Fresh control before the run resolved `yspennstate/math-research-brain@96b95ee808d5b5e5600fb45e2ea4de41ac7c111e`, owner control revision `2026-09-22.15`, still exclusively QFORM.

The designated partner `account04/B09` now has a completed current-QFORM theorem:

- `QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1`
- canonical mathematics: `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`
- blob: `a2292a47ee56cf3d66556e324bd8b234bd2157f1`.

For two equal-size **physical** banks of size `r>2` and invertible physical cross block `C`, that theorem proves

\[
\|p_Q\|_\infty\le {r\over r-2}|\det C|^{-1/r},
\tag{1.1}
\]

with arbitrary same-side quadratic blocks and affine terms, and with continuous density.

The projection ingredient used below is account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical proof

- `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

If `R` has orthonormal columns and row leverages `ell_i`, then for independent cap-one coordinates

\[
Y=R^TX,\qquad
\|p_Y\|_\infty\le
\mathcal B(R):=\prod_{i:\ell_i<1}(1-\ell_i)^{-(1-\ell_i)/2}
\le e^{k/2}.
\tag{1.2}
\]

This is a density theorem for the **joint projection**; it does not assert independence of its coordinates.

## 2. New theorem — `QFORM-GROUPED-CROSS-RANK-r-SMOOTHING-v1`

Let `S,T` be disjoint sets of original coordinates. Condition on every coordinate outside `S union T`. Write the conditional quadratic form

\[
Q_z(x,y)=x^TB_zx+2x^TBy+y^TD_zy+a_z^Tx+b_z^Ty+c_z,
\tag{2.1}
\]

where `B=A[S,T]` is the actual physical cross block, while `B_z,D_z` are arbitrary symmetric matrices and the affine terms may depend arbitrarily on the conditioned outside value `z`.

Assume

\[
r:=\operatorname{rank}B>2.
\]

Take the thin singular-value decomposition

\[
B=P\Sigma R^T,
\qquad P^TP=R^TR=I_r,
\qquad \Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_r),\quad \sigma_j>0.
\tag{2.2}
\]

Put

\[
\Delta_r(B):=\prod_{j=1}^r\sigma_j(B).
\tag{2.3}
\]

Then, for every admissible cap-one product input law,

\[
\boxed{
\|p_Q\|_\infty
\le {r\over r-2}
[\mathcal B(P)\mathcal B(R)]^{1/r}
\Delta_r(B)^{-1/r}.
}
\tag{2.4}
\]

Since `mathcal B(P),mathcal B(R)<=e^{r/2}`, the universal corollary is

\[
\boxed{
\|p_Q\|_\infty
\le e\,{r\over r-2}\,\Delta_r(B)^{-1/r}.
}
\tag{2.5}
\]

For every interval `L`,

\[
\boxed{
\Pr\{Q\in L\}
\le e\,{r\over r-2}\,\Delta_r(B)^{-1/r}|L|.
}
\tag{2.6}
\]

The characteristic function is integrable, so this branch has a **continuous density**.

For rank three,

\[
\boxed{
\|p_Q\|_\infty
\le 3[\mathcal B(P)\mathcal B(R)]^{1/3}
(\sigma_1\sigma_2\sigma_3)^{-1/3}
\le 3e(\sigma_1\sigma_2\sigma_3)^{-1/3}.
}
\tag{2.7}
\]

### Proof

Define the grouped singular coordinates

\[
U=P^TX_S,\qquad V=R^TX_T,\qquad W=\Sigma V.
\tag{2.8}
\]

The sets `S,T` are disjoint original-coordinate banks, hence the two source vectors `X_S,X_T` are genuinely independent. No independence is asserted among the coordinates of `U` or among those of `V`.

By (1.2),

\[
M_U:=\|p_U\|_\infty\le\mathcal B(P),
\qquad
\|p_V\|_\infty\le\mathcal B(R).
\tag{2.9}
\]

Scaling by `Sigma` gives

\[
M_W:=\|p_W\|_\infty
\le \mathcal B(R)\Delta_r(B)^{-1}.
\tag{2.10}
\]

For fixed `z,t`, disintegrate the `S`-bank amplitude over the fiber `P^Tx=u`:

\[
\alpha_{t,z}(u)
=\int_{P^Tx=u}
 e^{it(x^TB_zx+a_z^Tx)}\prod_{i\in S}f_i(x_i)\,d\mu_u(x).
\tag{2.11}
\]

The coarea Jacobian is one because `P` has orthonormal columns. Therefore

\[
|\alpha_{t,z}(u)|\le p_U(u),
\qquad
\|\alpha_{t,z}\|_2\le M_U^{1/2}.
\tag{2.12}
\]

Similarly disintegrate the `T`-bank same-side phase over `W=Sigma R^Ty`:

\[
\beta_{t,z}(w)
=\int_{\Sigma R^Ty=w}
 e^{it(y^TD_zy+b_z^Ty)}\prod_{j\in T}f_j(y_j)\,d\nu_w(y).
\tag{2.13}
\]

With the corresponding linear coarea normalization,

\[
|\beta_{t,z}(w)|\le p_W(w),
\qquad
\|\beta_{t,z}\|_2\le M_W^{1/2}.
\tag{2.14}
\]

The entire conditional characteristic function is now

\[
\phi_z(t)=e^{itc_z}
\int_{\mathbb R^r}\int_{\mathbb R^r}
\alpha_{t,z}(u)\beta_{t,z}(w)e^{2it u\cdot w}\,du\,dw.
\tag{2.15}
\]

All dense same-side curvature is still present in the two complex amplitudes; only its modulus has disappeared.

Using the Fourier convention

\[
\widehat\beta(\xi)=\int\beta(w)e^{i\xi\cdot w}\,dw,
\]

Cauchy--Schwarz and Plancherel give, for `t!=0`,

\[
\begin{aligned}
|\phi_z(t)|
&\le \|\alpha_{t,z}\|_2
\left(\int|\widehat\beta_{t,z}(2tu)|^2du\right)^{1/2}\\
&=(2|t|)^{-r/2}\|\alpha_{t,z}\|_2\|\widehat\beta_{t,z}\|_2\\
&=\pi^{r/2}|t|^{-r/2}\|\alpha_{t,z}\|_2\|\beta_{t,z}\|_2\\
&\le \pi^{r/2}|t|^{-r/2}(M_UM_W)^{1/2}.
\end{aligned}
\tag{2.16}
\]

By (2.9)--(2.10),

\[
|\phi_z(t)|
\le \pi^{r/2}|t|^{-r/2}
[\mathcal B(P)\mathcal B(R)]^{1/2}
\Delta_r(B)^{-1/2}.
\tag{2.17}
\]

The estimate is uniform in `z`, so averaging the outside conditioning preserves it. Combining with `|phi_Q(t)|<=1`, set

\[
\alpha={r\over2}>1,
\qquad
A=\pi^{r/2}[\mathcal B(P)\mathcal B(R)]^{1/2}\Delta_r(B)^{-1/2}.
\tag{2.18}
\]

Then

\[
|\phi_Q(t)|\le\min\{1,A|t|^{-\alpha}\}.
\tag{2.19}
\]

The majorant is integrable and

\[
{1\over2\pi}\int_{\mathbb R}\min\{1,A|t|^{-\alpha}\}\,dt
={\alpha\over\pi(\alpha-1)}A^{1/\alpha}.
\tag{2.20}
\]

Since `1/alpha=2/r`, this equals exactly the right side of (2.4). Fourier inversion yields a bounded continuous density and (2.6). `QED`

### Endpoint check against the designated partner

If `|S|=|T|=r` and `P,R` are coordinate selectors, every active leverage is one and the convention in (1.2) gives

\[
\mathcal B(P)=\mathcal B(R)=1,
\qquad
\Delta_r(B)=|\det B|.
\]

Thus (2.4) becomes

\[
\|p_Q\|_\infty\le {r\over r-2}|\det B|^{-1/r},
\]

which is exactly the completed account04/B09 theorem (1.1). In particular, for a literal invertible physical `3x3` cross block `C`, the designated partner gives the actual inequality

\[
\boxed{\|p_Q\|_\infty\le3|\det C|^{-1/3}.}
\tag{2.21}
\]

Whenever both a physical minor and the grouped singular-volume certificate are available, one may therefore use the genuine combined inequality

\[
\boxed{
\|p_Q\|_\infty\le
\min\left\{
3|\det C|^{-1/3},
3[\mathcal B(P)\mathcal B(R)]^{1/3}\Delta_3(B)^{-1/3}
\right\}.
}
\tag{2.22}
\]

The first term is the completed designated-partner result; the second is the new grouped extension.

## 3. Diffuse target-valid family where every physical minor loses dimension but grouped cross volume does not

Let `N` be a multiple of four. Let `P_N` be the `N x 3` frame whose rows are the four Walsh sign types

\[
{1\over\sqrt N}(1,\pm1,\pm1),
\tag{3.1}
\]

each repeated `N/4` times. Then `P_N^TP_N=I_3`. Put

\[
B_N=P_NP_N^T,
\qquad
A_N=\begin{pmatrix}0&B_N\\B_N&0\end{pmatrix}.
\tag{3.2}
\]

The three nonzero singular values of `B_N` are all exactly one. Hence the nonzero eigenvalues of `A_N` are

\[
-1,-1,-1,1,1,1.
\tag{3.3}
\]

So this is a literal target-valid family with six eigenvalues of modulus one.

Every row leverage of `P_N` is `3/N`, hence

\[
\mathcal B(P_N)=
(1-3/N)^{-(N-3)/2}.
\tag{3.4}
\]

The new theorem gives, for every admissible cap-one product input law,

\[
\boxed{
\|p_{X^TA_NX}\|_\infty
\le 3(1-3/N)^{-(N-3)/3}<3e<8.155.
}
\tag{3.5}
\]

This is uniform in `N`.

By contrast, every `3x3` physical minor factors as

\[
\det B_N[I,J]=\det P_N[I,:]\,\det P_N[J,:].
\tag{3.6}
\]

For three distinct Walsh row types,

\[
|\det P_N[I,:]|={4\over N^{3/2}},
\tag{3.7}
\]

and repeated row types give determinant zero. Therefore

\[
\max_{|I|=|J|=3}|\det B_N[I,J]|={16\over N^3}.
\tag{3.8}
\]

Even the best application of the designated partner's physical-minor theorem alone would have certificate

\[
3\left({N^3\over16}\right)^{1/3}
={3N\over16^{1/3}},
\tag{3.9}
\]

which grows linearly in `N`. This family therefore demonstrates the exact gain of **aggregate-before-minor** smoothing: physical coefficients and every fixed physical determinant vanish, while the grouped singular volume stays equal to one.

For `N=16`, the checker gives

\[
\|p_Q\|_\infty\le7.3771166865,
\tag{3.10}
\]

whereas the best physical-minor certificate is `19.0488126236`.

## 4. Exact rank-two residual: failure of every rank-three augmentation forces diagonal plus slope-span curvature

The preceding theorem sharply narrows the `r29` debt `QFORM-GROUPED-CROSS-TO-GENERAL-LEAF-CURVATURE-v1`.

Suppose a hub bank `H` and leaf bank `I` have a rank-two cross block

\[
A[H,I]=PC^T,
\qquad P^TP=I_2,
\qquad C\in\mathbb R^{m\times2},\quad \operatorname{rank}C=2.
\tag{4.1}
\]

Let

\[
D=A[I,I],
\]

and denote the `j`th row of `C` by `c_j^T`.

For each `k in I`, inspect the augmented physical cut

\[
(H\cup\{k\})\;|\;(I\setminus\{k\}).
\tag{4.2}
\]

Its cross block is

\[
\begin{pmatrix}
P C_{-k}^T\\
D_{k,-k}
\end{pmatrix}.
\tag{4.3}
\]

### Lemma 4.1 — `QFORM-RANK2-NOAUGMENT-DIAG-PLUS-SPAN-v1`

Assume

1. `rank(C_{-k})=2` for every `k` (no exact cross-frame coloop), and
2. every augmented cut (4.3) has rank at most two.

Then there exists a symmetric `2x2` matrix `M` and a diagonal matrix `Lambda` such that

\[
\boxed{D=CMC^T+\Lambda.}
\tag{4.4}
\]

Thus if **no** singleton leaf coordinate can create an aggregate rank-three cross cut, all off-diagonal leaf curvature is forced to live inside the existing two-dimensional slope span. The only curvature outside that span is diagonal in the original independent coordinates.

### Proof

Fix `k`. Since `P` has rank two and `C_{-k}` has rank two, the top block `PC_{-k}^T` in (4.3) has row space equal to the row space of `C_{-k}^T`, of dimension two. Assumption 2 therefore forces the last row into that row space. Hence there exists `alpha_k in R^2` such that

\[
D_{kj}=\alpha_k^Tc_j\qquad(j\ne k).
\tag{4.5}
\]

Choose indices `a,b` for which `c_a,c_b` are linearly independent. Define the unique linear map `M` by

\[
Mc_a=\alpha_a,
\qquad
Mc_b=\alpha_b.
\tag{4.6}
\]

Symmetry of `D` on the pair `(a,b)` gives

\[
\alpha_a^Tc_b=\alpha_b^Tc_a,
\tag{4.7}
\]

which is exactly the condition that the bilinear form associated with `M` is symmetric on the basis `c_a,c_b`; therefore `M=M^T`.

For any `k`, symmetry with `a` and `b` gives

\[
c_a^T\alpha_k=\alpha_a^Tc_k=c_a^TMc_k,
\qquad
c_b^T\alpha_k=\alpha_b^Tc_k=c_b^TMc_k.
\tag{4.8}
\]

Because `c_a,c_b` span `R^2`, these two scalar identities imply

\[
\alpha_k=Mc_k.
\tag{4.9}
\]

Therefore, for every `i ne j`,

\[
D_{ij}=\alpha_i^Tc_j=c_i^TMc_j.
\tag{4.10}
\]

So `D-CMC^T` is diagonal, proving (4.4). `QED`

### Structural fork

The exact rank-two grouped-cross branch now has the following source-coordinate fork.

- If some augmented cut `(H union {k}) | (I\{k})` has rank at least three with quantitative singular-volume product, Theorem 2.1 pays it directly, with **all** same-side curvature retained.
- If every such cut has rank at most two and there is no cross-frame coloop, Lemma 4.1 forces `D=CMC^T+Lambda`.
- If deleting one leaf row drops `rank C`, that leaf row is an exact coloop/high-leverage source coordinate and must be routed through the localized/physical-pivot branches rather than through a diffuse minor selection.

This is an exact algebraic reduction, not yet a quantitative stability theorem.

## 5. What remains open after this run

The full QFORM conjecture is still open. This run removes **arbitrary dense same-bank curvature** as an analytic obstruction whenever any disjoint original-coordinate cut has cross rank at least three with quantitative product of singular values.

For the rank-two grouped survivor, the first remaining B09 implication is now

`QFORM-RANK2-NOAUGMENT-QUANTITATIVE-STABILITY-v1`:

> Quantify Lemma 4.1. Starting from a normalized rank-two grouped cross frame `C`, show that if every augmented cut has small third singular volume and no row is a quantitative coloop/high-leverage exit, then the off-diagonal leaf block is quantitatively close, in the correct determinant-weighted norm, to `CMC^T` plus an original-coordinate diagonal. Then route either the resulting diagonal transverse curvature into the existing one-Fresnel / grouped-Pluecker payments or the coloop branch into an existing physical-pivot exit.

The critical restriction is that the approximation may **not** be discarded as a small random error: there are no moment or support assumptions. The small residual must be retained inside a phase or controlled by a translation-invariant deterministic inequality.

Full-target essential boundedness: **OPEN**.  
Full-target continuous density: **OPEN**.

## 6. Finite checks and privacy/write review

`CHECK.py` verifies:

- orthonormality of the Walsh frame;
- the six nonzero eigenvalues `{-1,-1,-1,1,1,1}`;
- grouped bounds at `N=4,8,16,64`;
- the exact maximum physical `3x3` determinant `16/N^3` on the enumerated small instances;
- the exact residual structure `D=CMC^T+diag` produces only rank-two singleton-augmented cuts.

The changed-file allowlist contains only this report and its deterministic checker/output under this run's private mathematical directory. Manual content review found no credentials, account secrets, personal/client/trading data, external signed URLs, or public-release action. The available connector does not expose the repository's local secret-scan command, so this is a narrow manual fallback rather than a claim that a full repository scanner ran.
