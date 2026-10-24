SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T11:16:10Z.
attacking: the ultra-near heavy-null branch; isolate exactly which longitudinal leakage is genuinely dangerous by absorbing all support-disjoint longitudinal mass into the independent hub before any reciprocal-minor payment.

# account01/B05 r31 — exact disjoint-longitudinal absorption and mixed-support renormalization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / equivalent interval bound, preserving arbitrary product densities  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_THEOREM_PROVED / PARTNER_RESULT_APPLIED / PRECISE_MISSING_FACTOR_SHARPENED / FULL_QFORM_OPEN`  
**Continuity:** obtained on the leave-one-out Fresnel branch below; not proved on the new endpoint reduction by itself; unrestricted continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.

## 1. Scope and prior endpoint

Work in the exact-rank-three high-leverage null-pivot normal form already reached by B05 r30:

\[
A=RBR^\top,\qquad R^\top R=I_3,\qquad s_{\min}(B)\ge1,
\]

with a physical row `h` and a deterministic rotation only in the three-dimensional coefficient space such that

\[
r_h=\sqrt c\,e_1,\qquad c>127/128,\qquad B_{11}=0.
\]

After a transverse rotation,

\[
B=\begin{pmatrix}0&b&0\\ b&\alpha&\delta\\0&\delta&\gamma\end{pmatrix},
\qquad |b|\ge1,\qquad |\gamma|\ge1.
\]

For `j != h` write

\[
r_j=(u_j,v_j,w_j).
\]

Parseval gives

\[
\sum u_j^2=1-c,\qquad
\sum v_j^2=\sum w_j^2=1,
\]
\[
\sum u_jv_j=\sum u_jw_j=\sum v_jw_j=0. \tag{1.1}
\]

The pure quadratic target is

\[
Q=2b(\sqrt c X_h+U)V+\alpha V^2+2\delta VW+\gamma W^2, \tag{1.2}
\]

where `U=sum u_j X_j`, `V=sum v_j X_j`, `W=sum w_j X_j`.

B05 r30 showed that a small *total* longitudinal leakage can be pruned to a small graph perturbation, but the remaining obstacle is stability when the longitudinal and transverse projections use the same original coordinates.  This run proves that this support incidence is not merely a qualitative description: every longitudinal component on coordinates carrying no transverse coefficient can be eliminated **exactly and at zero density-cap cost**.

## 2. Main theorem — pure-longitudinal absorption

Define the pure-longitudinal and mixed-support sets

\[
D:=\{j\ne h:(v_j,w_j)=(0,0)\},\qquad M:=\{j\ne h\}\setminus D,
\]

and masses

\[
\rho_D:=\sum_{j\in D}u_j^2,\qquad
\rho_M:=\sum_{j\in M}u_j^2.
\]

Then

\[
c+\rho_D+\rho_M=1. \tag{2.1}
\]

### Theorem `QFORM-PURE-LONGITUDINAL-ABSORPTION-MIXED-MASS-v1`

Under the hypotheses above, the law of `Q` is exactly the law of an exact-rank-three quadratic form of **independent cap-one inputs** whose orthonormal coefficient frame has a synthetic heavy row of leverage

\[
\boxed{c_*={c\over c+\rho_M}}, \tag{2.2}
\]

and hence leakage

\[
\boxed{1-c_*={\rho_M\over c+\rho_M}.} \tag{2.3}
\]

The new active `3 x 3` matrix `B_*` satisfies

\[
\boxed{s_{\min}(B_*)\ge c,\qquad
|\det B_*|=(c+\rho_M)|\det B|,\qquad (B_*)_{11}=0.} \tag{2.4}
\]

Thus **only the longitudinal mass carried on coordinates that also carry a transverse coefficient is a genuine endpoint parameter**.  Arbitrarily much longitudinal mass on support-disjoint coordinates is absorbed into the independent hub without worsening its density cap.

### Proof

Put

\[
U_D=\sum_{j\in D}u_jX_j,\qquad U_M=\sum_{j\in M}u_jX_j,
\]

and define the synthetic scalar

\[
S:=X_h+{U_D\over\sqrt c}. \tag{2.5}
\]

The coordinates in `D` are disjoint from the coordinates in `M`; also `X_h` is independent of all residual coordinates. Hence `S` is independent of every `X_j`, `j in M`.

If `f_h` is the density of `X_h`, then, with expectation over `U_D`,

\[
p_S(s)=\mathbb E\,f_h\!\left(s-{U_D\over\sqrt c}\right). \tag{2.6}
\]

Therefore

\[
0\le p_S\le1,\qquad \int p_S=1. \tag{2.7}
\]

No density, moment, support or regularity assumption on `U_D` is needed; convolution with an arbitrary probability law preserves the cap `1`.

Equation (1.2) now becomes exactly

\[
Q=2b(\sqrt c S+U_M)V+\alpha V^2+2\delta VW+\gamma W^2. \tag{2.8}
\]

Treat `S` as one independent scalar input and retain the original independent coordinates indexed by `M`.  Their coefficient rows are

\[
r_S=(\sqrt c,0,0),\qquad r_j=(u_j,v_j,w_j),\ j\in M. \tag{2.9}
\]

Since the discarded set `D` has zero transverse coordinates, (1.1) implies

\[
G:=\sum_{j\in M}r_jr_j^\top+r_Sr_S^\top
=\operatorname{diag}(c+\rho_M,1,1). \tag{2.10}
\]

Let

\[
\widetilde R=R^\sharp G^{-1/2},\qquad
B_*=G^{1/2}BG^{1/2}. \tag{2.11}
\]

Then `widetilde R^T widetilde R=I_3` and the quadratic form is unchanged:

\[
R^\sharp B(R^\sharp)^\top
=\widetilde R B_*\widetilde R^\top. \tag{2.12}
\]

The synthetic heavy row has squared norm

\[
\|r_SG^{-1/2}\|^2={c\over c+\rho_M},
\]

which proves (2.2)--(2.3).  Since `G` has eigenvalues `c+rho_M,1,1` and `c+rho_M>=c`, congruence gives

\[
s_{\min}(B_*)\ge \lambda_{\min}(G)s_{\min}(B)\ge c. \tag{2.13}
\]

Also

\[
\det B_*=(\det G)\det B=(c+\rho_M)\det B, \tag{2.14}
\]

and `(B_*)_11=(c+rho_M)B_11=0`.  This proves the theorem. QED.

## 3. Exact leave-one-out identity after absorption

The normalized residual rows are

\[
\widetilde r_j=
\left({u_j\over\sqrt{c+\rho_M}},v_j,w_j\right),\qquad j\in M. \tag{3.1}
\]

The leave-one-out Gram after deleting the synthetic hub is

\[
H_*=I-r_*r_*^\top
=\operatorname{diag}\left({\rho_M\over c+\rho_M},1,1\right). \tag{3.2}
\]

Hence, for every `j in M`, the normalized leaf leverage is exactly

\[
\boxed{
\ell_j^{(-*)}
=\widetilde r_j^\top H_*^{-1}\widetilde r_j
={u_j^2\over\rho_M}+v_j^2+w_j^2.}
\tag{3.3}
\]

In particular

\[
\sum_{j\in M}\ell_j^{(-*)}=3, \tag{3.4}
\]

so at most five leaves can violate the strict gate `ell_j^(-*)>1/2`.  Importantly, neither `rho_D` nor the number of pure-longitudinal coordinates appears anywhere in (3.2)--(3.4).

## 4. Required application of account02/B05

Use the completed account02/B05 theorem `QFORM-EXACTRANK3-LEAVEONEOUT-FRESNEL-v1`, read at source commit

`yspennstate/math-open-problems@7082c8bddc546596fd36fd2afdb08344d38ee230`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T092247Z-account02-B05-QFORM-r19/REPORT.md`.

Whenever every leaf in (3.3) satisfies `ell_j^(-*)<=1/2`, that theorem gives

\[
\|p_Q\|_\infty
\le12\Bigl(|\det B_*|\det H_*\Bigr)^{-1/3}. \tag{4.1}
\]

But the factors cancel **exactly**:

\[
|\det B_*|\det H_*
=(c+\rho_M)|\det B|\,{\rho_M\over c+\rho_M}
=|\det B|\rho_M. \tag{4.2}
\]

Therefore

\[
\boxed{
\|p_Q\|_\infty
\le12\,(|\det B|\rho_M)^{-1/3}
\le12\rho_M^{-1/3}.}
\tag{4.3}
\]

The partner proof also gives a bounded continuous representative on this branch.  In particular, if `rho_M>=1/128`, then

\[
\boxed{\|p_Q\|_\infty<60.477.} \tag{4.4}
\]

This is an equation-level use of the designated partner result and shows that the Fresnel collar is governed by the **mixed-support mass** rather than the total longitudinal leakage.

## 5. Exact mixed-support endpoint

If

\[
\rho_M=0, \tag{5.1}
\]

then every residual longitudinal coefficient is on a support-disjoint coordinate.  The absorption theorem gives a genuine independent scalar `S` of density cap one, and the remaining pair `(V,W)` uses disjoint original coordinates from `S`.  Thus the quadratic form is exactly in the source-separated endpoint class.

Apply the completed account02/B05 theorem `QFORM-HEAVY-ROW-SUPPORT-SEPARATED-CLOSURE-v1` (account02/B05 r23; source pinned in previous B05 audit at commit `ad7874e3ee0f4541714b2376aa09154517e60867`).  Since (2.13) gives active scale at least `c`, scaling its `<248` unit-scale bound yields

\[
\boxed{
\|p_Q\|_\infty<{248\over c}< {248\cdot128\over127}<250.}
\tag{5.2}
\]

Thus **all support-disjoint longitudinal overlap is harmless even when nonzero and arbitrarily fragmented**.  The unresolved endpoint is not `U != 0`; it is `U` carried on the *same original coordinates* as `(V,W)`.

## 6. Mixed-only cube-root pruning

The theorem also sharpens r30's pruning parameter.  In the normalized representation (2.11), put

\[
\widehat\rho={\rho_M\over c+\rho_M}=1-c_*,\qquad
\eta=\widehat\rho^{1/3}. \tag{6.1}
\]

Applying the r30 deterministic pruning calculation to the normalized mixed rows gives

\[
H_\eta=\{j\in M: |u_j|/\sqrt{c+\rho_M}>
\eta\sqrt{v_j^2+w_j^2}\}. \tag{6.2}
\]

For their normalized Gram loss `K_eta`, exactly the same two-line proof gives

\[
\boxed{\|K_\eta\|_{op}\le\eta+\eta^3,} \tag{6.3}
\]

and every surviving mixed row satisfies the complementary graph bound.  Pure-longitudinal coordinates never need to be conditioned: they have already been absorbed into `S` at no density cost.  Hence future endpoint work should use `widehat rho`, not `1-c`, as its small parameter.

## 7. What is now genuinely unpaid

The first B05 debt is sharpened to

`QFORM-SAME-COORDINATE-MIXED-SHEAR-STABILITY-v1`:

> In the exact-rank-three heavy-null core, after first absorbing every pure-longitudinal original-coordinate bank as in Theorem 2, prove a universal coarea/interval bound as the strictly positive mixed-support mass `rho_M -> 0`, uniformly for arbitrary fragmented cap-one product laws. Equivalently, control the linear shear only on coordinates that simultaneously carry longitudinal and transverse coefficients.

This distinction matters.  A small or even large longitudinal component on a disjoint bank is **exactly harmless** by convolution.  Only same-coordinate incidence prevents conversion to the completed source-separated endpoint.  Small coefficient magnitude alone is not a probabilistic perturbation because no moments/support bounds are assumed.

The full QFORM conjecture is still `OPEN / NOT PROVED`.  The theorem above is for the exact-rank-three heavy-null branch and must not be promoted to arbitrary higher-rank Schur remainders without an additional reduction.  Continuity is separately established only on the partner Fresnel branch (4.3), not for the unrestricted target.

## 8. Correction and source audit

This argument does not rotate the independent random coordinates; only the deterministic three-dimensional coefficient space is whitened.  The synthetic scalar `S` is independent of the retained original coordinates because it uses a disjoint coordinate bank, and its cap-one density is proved by the explicit convolution formula (2.6), not assumed after a general projection.  No pointwise van-der-Corput estimate, arbitrary-joint coarea lemma, conditional-density-cap surrogate for independence, moment bound, compact support, connected support, or small-random-perturbation argument is used.

Source dependencies actually used:
- account02/B05 r19 `QFORM-EXACTRANK3-LEAVEONEOUT-FRESNEL-v1`, read at `yspennstate/math-open-problems@7082c8bddc546596fd36fd2afdb08344d38ee230`, exact path above;
- account02/B05 r23 `QFORM-HEAVY-ROW-SUPPORT-SEPARATED-CLOSURE-v1`, prior source pin `ad7874e3ee0f4541714b2376aa09154517e60867`;
- account01/B05 r30 cube-root pruning identity, current repository path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T102839Z-account01-B05-QFORM-r30/REPORT.md`.

Repository synchronization is not native learned-memory ingestion; execution status remains `WITHOUT_VERIFIED_BRAIN`.
