# fleet03/B06 independent fixed-multiplicity audit — graph determinant, exact identities, and endpoint barrier

Run: `20260924T122226Z-fleet03-B06-fixedmult-r01`  
Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned source manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`  
Pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Pinned git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Fresh source blob at pre-publication master: unchanged (`183ccd294763214e6a707e8d4749ff9a8cf7006d`).

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent fleet03/B06 audit.** I read the complete 790-line manuscript and checked the dependency chain end to end. I found no fatal mathematical defect in the candidate theorem

\[
 s_{17}(A)\ge s>0
 \quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for arbitrary real symmetric `A`, arbitrary affine `b,c`, and independent real coordinate densities bounded by `K`.

This is one independent worker review, not formal verification, not a self-awarded two-review certificate, and not a proof of the unrestricted three-eigenvalue conjecture.

Two nonfatal gaps were found:

1. **Projection-lemma wording gap (roughly source lines 256–287).** After rows with `b_i=0` have been dropped, the proof writes `sum_i(1-b_i)=d`. Over the retained rows the correct statement is
   \[
   \sum_{b_i>0}(1-b_i)\le d.
   \]
   This is the favorable direction for the upper bound, so replacing the equality by `<=` repairs the sentence with no change to the theorem or constant.
2. **Repository-package gap.** The current root README names `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` as canonical supplementary files, but the root listing inspected in this run did not contain them, and direct retrieval of `proof_map.csv` returned 404. The mathematical manuscript is self-contained, so this is a reproducibility/release-package gap, not a mathematical failure. I therefore mark those supplemental checks **UNCHECKED / unavailable in the repository snapshot** rather than treating the self-audit's reported finite checks as independent evidence.

No lower multiplicity is certified in this run. I do prove below two precise method barriers: the present graph-regularizer calculation cannot convert order-four crossing volume into an integrable absolute Fourier envelope by retuning the scalar regularizer, and a borderline `1/|t|` Fourier bound plus a finite full half-potential does not, as an abstract analytic interface, imply an `L^infinity` density.

## End-to-end audit ledger

### A1. Theorem statement, quantifiers, normalization, scaling — lines 1–80 — PASS

The theorem keeps arbitrary dimension, signs, remaining spectrum, affine terms and rough independent coordinate laws. No moments, centering, identical laws, bounded support, connected support, log-concavity or post-rotation independence are introduced. With `Y=KX`, the density caps become one, and

\[
 \widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q.
\]

The normalized bound therefore rescales exactly to `10^4 K^2/s`.

### A2. Fourier normalization, Gaussian inversion, and Riesz half-potential — lines 81–161 — PASS

The convention `fhat(t)=int exp(itx)f(x)dx` is used consistently. Plancherel has factor `2pi`; inversion has factor `(2pi)^(-1)`. The Gaussian identity is consistent with `g_epsilon(x)=(4pi epsilon)^(-1/2)exp(-x^2/(4epsilon))`.

The negative-half-moment computation gives exactly

\[
 \mathbb E|Z-a|^{-1/2}
 \le (2\pi)^{-1/2}\int |t|^{-1/2}|\phi_Z(t)|\,dt.
\]

For `|phi(t)|<=min(1,(u/|t|)^(3/4))`, the weighted integral is `12 sqrt(u)`, so the manuscript's constant follows. The proof correctly does not infer direct density inversion from the `3/4` exponent.

### A3. Singular-value perturbation and Schur spectral count — lines 162–223 — PASS

The low-rank perturbation statement is valid for nonsymmetric matrices by the best-rank approximation formula for singular values. For the symmetric Schur complement, when `A` is invertible, the complementary principal block of `A^{-1}` is `S^{-1}`. Positive and negative min-max/interlacing counts separately imply that a principal compression has no more eigenvalues outside `[-t^{-1},t^{-1}]` than the full inverse. Since

\[
 \#\{|\lambda(S^{-1})|>t^{-1}\}=(n-k)-N_S(t),
\]

the desired `N_S(t)>=N_A(t)-k` follows. The `A+epsilon I` passage handles singular `A` without changing the pivot in the limit.

### A4. Geometric rank-one Brascamp–Lieb heat flow — lines 224–255 — PASS

From `sum c_i u_i u_i^T=I`, the matrix with columns `sqrt(c_i)u_i` is a contraction from `R^N` to `R^d`, giving

\[
 \sum c_i v_i^2-\left|\sum c_i u_i v_i\right|^2\ge0.
\]

The heat-flow monotonicity sign is therefore correct. Compact support supplies the stated Gaussian domination for integration by parts and the large-time limit. The extension to general nonnegative integrable inputs via truncation and monotone convergence is legitimate.

### A5. Product-projection density — lines 256–287 — PASS WITH LOCAL WORDING GAP

The orthogonal-complement marginalization keeps all original coordinate factors. For `b_i=|w_i|^2`, the positive-`b_i` rows satisfy the required geometric frame relation, and the functions

\[
 h_i(t)=f_i((Uy)_i+\sqrt{b_i}t)^{1/b_i}
\]

obey `int h_i <= b_i^(-1/2)` because `0<=f_i<=1`. Thus

\[
 p(y)\le\prod b_i^{-b_i/2}.
\]

The entropy inequality gives the advertised `e^{d/2}` bound. The only correction is that after omitting `b_i=0`, the retained sum of `1-b_i` is at most `d`, not necessarily equal to `d`; the inequality direction only strengthens the result.

### A6. Integrated scalar Fourier powers — lines 288–300 — PASS

For `m=floor(p/2)>=p/4`, `|fhat|<=1` gives `int|fhat|^p<=int|fhat|^(2m)`. The latter is integrable already because it is bounded by `|fhat|^2` and `f in L^2`. Fourier inversion identifies it with `2pi` times the density at zero of a sum of `m` independent differences. The scalar product-projection bound applied to the `2m` original independent signed coordinates gives

\[
 \int|\widehat f|^p\le 2\pi\sqrt{2e}/\sqrt p.
\]

No independence of a rotated coordinate system is used.

### A7. Cross-block decoupling — lines 301–328 — PASS

Cauchy–Schwarz in the original `X_I` law, followed by an independent copy of `X_J`, gives

\[
 |\phi_Z(t)|^2\le\mathbb E_D\prod_i|\widehat f_i(2t(MD)_i)|.
\]

Jensen on this nonnegative right-hand side gives the fourth-power version with squared Fourier factors. The coordinates of `D=X_J-X'_J` remain independent and have densities bounded by one.

### A8. Regularized crossing determinant — lines 329–379 — PASS; primary B06 lens

This calculation was rederived independently.

Set

\[
 a=2t,\qquad \alpha=(2\pi e)^2,\qquad
 H=\alpha I+a^2M^TM,
\]

and, with `m_i` the transpose of row `i` of `M`,

\[
 c_j=\alpha e_j^TH^{-1}e_j,
 \qquad d_i=a^2m_i^TH^{-1}m_i,
 \qquad \theta=\sum_i d_i.
\]

The rank-one matrices generated by `sqrt(alpha) H^{-1/2}e_j` and `aH^{-1/2}m_i` sum exactly to the identity. Therefore

\[
 0<c_j\le1,\quad0\le d_i\le1,
 \quad\theta=\sum_i d_i=\sum_j(1-c_j).
\]

After `x=H^{-1/2}z`, geometric BL yields the manuscript's exact Jacobian-weight product

\[
 \det(H)^{-1/2}
 \prod_j\alpha^{c_j/2}c_j^{-c_j/2}\|g_j\|_{1/c_j}
 \prod_i d_i^{-d_i/2}\|h_i\|_{1/d_i}.
\]

Here `g_j<=1` and has mass one, so `||g_j||_{1/c_j}<=1`. Since `h_i=|fhat_i|^2`, the scalar Fourier-power lemma with `p=2/d_i` gives

\[
 \|h_i\|_{1/d_i}
 =\left(\int|\widehat f_i|^{2/d_i}\right)^{d_i}
 \le(2\pi\sqrt{e d_i})^{d_i}.
\]

This cancels the explicit `d_i^{-d_i/2}` exactly. Also

\[
 \prod_j c_j^{-c_j/2}\le e^{\theta/2}.
\]

Thus the entire non-determinant prefactor becomes

\[
 \alpha^{(d-\theta)/2}(2\pi\sqrt e)^\theta e^{\theta/2}
 =\alpha^{(d-\theta)/2}(2\pi e)^\theta
 =\alpha^{d/2},
\]

because `sqrt(alpha)=2pi e`. Since `det H=alpha^d det(I+a^2M^TM/alpha)`, the fourth-power decoupling majorant is

\[
 \det(I+a^2M^TM/\alpha)^{-1/2}.
\]

Taking fourth roots and substituting `a=2t`, `alpha=4pi^2e^2` gives exactly

\[
 \boxed{|\phi_Z(t)|\le
 \det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.}
\]

The Jacobian, BL weights, entropy factor, scalar-Fourier exponent, regularizer and final `-1/8` power all check. Same-bank terms `F,G` remain arbitrary measurable functions throughout.

### A9. Crossing-volume expansion and exponents — lines 380–400 — PASS

Cauchy–Binet gives

\[
 \det(I+zM^TM)=\sum_k z^k Z_k(M),
\]

with `Z_k` the squared-minor sum. Keeping only the positive order-`k` term produces exponent `k/4`. Thus order five gives `|t|^{-5/4}` and direct `L^1` Fourier inversion; order three gives `|t|^{-3/4}`, which is used only after multiplying by the Riesz weight `|t|^{-1/2}`. The manuscript keeps these analytic roles distinct.

### A10. Scalar, definite-pair, and hyperbolic changes of variables — lines 401–493 — PASS

The scalar-square profile is correctly formulated as conditional measure domination, not independence from the Schur remainder. The definite-pair quadratic polar Jacobian is `1/(2 sqrt(|det B|))`, yielding `pi M/sqrt(|det B|)` after angle integration. For the indefinite pair, the hyperbolic parameterization has absolute Jacobian `1/(2 sqrt D)`. The tail estimate uses only one original-coordinate cap-one density and mass one; the other factor is bounded by one. The exceptional critical level is null and is handled through nonnegative test functions/Tonelli rather than pointwise conditioning on a rough slice.

### A11. Quarter-power concentration — lines 494–536 — PASS

If no diagonal entry reaches `L/2`, the random-sign split of the off-diagonal part creates an original-coordinate cross block `M` with `||M||>=L/4`. Retaining one singular-value factor in the determinant theorem yields a `|t|^{-1/4}` characteristic-function envelope. Gaussian smoothing then produces the claimed `rho^{1/4}` small-ball bound. The later layer-cake logarithmic potential is valid and also excludes atoms.

### A12. Volume-sampled interpolation — lines 537–566 — PASS

For a disjoint invertible seed `B=A[S,T]`,

\[
 P=A_{\cdot,T}B^{-1}A_{S,\cdot}
\]

has rank at most `r`, agrees with `A` on rows `S` and columns `T`, and gives the bordered-determinant identity

\[
 \det A_{S\cup\{\ell\},T\cup\{m\}}^2
 =\det(B)^2(A_{\ell m}-P_{\ell m})^2.
\]

The extension multiplicity is at most `(r+1)^2`; singular seeds are not sampled, so an inequality rather than equality is the correct aggregate statement.

### A13. Completion, nonsymmetric support, both rank bounds — lines 567–584 — PASS

With `E` supported on the off-diagonal of `LxL`, and `D` the diagonal residual on `L`, one has `R_LL=P_LL` and hence `rank R_LL<=r`. The difference `R-P` vanishes on rows `S`, columns `T`, and all of `LxL`; all remaining support lies in rows `T` or columns `S`. Splitting those two supports gives rank at most `r+r`. Together with `rank P<=r`,

\[
 \operatorname{rank}R\le3r,
 \qquad \operatorname{rank}R_{L,L}\le r.
\]

`D` vanishes on `S union T` by construction. Nonsymmetry is harmless because only singular-value perturbation and rank are later applied to `D+R=A-E`.

### A14. No-pivot spectral-to-volume conversion — lines 585–621 — PASS

A bad telescoping ratio gives `||E||<=1/16`. For `m=4k-3` and the bad-ratio index `r<=k-1`, global rank `<=3r` forces at least `m-3r>=r+1` diagonal entries of `D` to have magnitude at least `1-epsilon`. Since `D` vanishes on the seed, they lie in `L`.

On an `(r+1)`-subset `H` of these entries,

\[
 |R_{ii}|\ge371/400,
 \qquad |R_{ij}|<1/7+1/16,
\]

and for `r<=4`

\[
 \sum_{j\ne i}|R_{ij}|<23/28<371/400.
\]

The exact slack is

\[
 371/400-23/28=297/2800>0.
\]

Strict diagonal dominance makes `R_HH` invertible of rank `r+1`, contradicting `rank R_LL<=r`. The `r=0` Frobenius argument is also correct.

### A15. Random cut and no-pivot analytic consequences — lines 622–651 — PASS

Each ordered disjoint `k`-minor survives a fair cut with probability `4^{-k}`. From `V_k>=kappa^k`, one gets a cut with `Z_k>=4^{-k}kappa^k`, hence

\[
 Z_k^{-1/(2k)}\le2\kappa^{-1/2}=160.
\]

The order-three and order-five constants then follow as stated.

### A16. Singular kernels, pivot half-potentials, and nine-direction compiler — lines 652–721 — PASS

The distinction between the truncated half-potential

\[
 H(Z)=\sup_a\mathbb E[|Z-a|^{-1/2}\mathbf1_{|Z-a|\le1}]
\]

and the full half-potential is preserved. Scalar, definite-pair and indefinite-pair pivot branches all satisfy the hypotheses of the lemmas invoked. Under `s_9>=1`, either the pivot estimate gives truncated `H<=600`, or the no-pivot order-three Fourier estimate gives the stronger full half-potential `<200`; outside unit distance the kernel contributes at most one, yielding the full `<=601` statement.

### A17. Main theorem and limitations — lines 722–790 — PASS

No pivot uses order five and gives `<2400`. A scalar pivot removes at most one large direction, so the Schur complement has at least sixteen and in particular nine; the full half-potential then gives `6010`. A definite pair is directly bounded. An indefinite pair removes at most two directions and leaves a nonzero Schur quadratic norm, sufficient for the logarithmic-potential bound. The final scaling is correct. The manuscript correctly limits its continuity claim to the Fourier no-pivot branch and does not claim the three-eigenvalue conjecture.

## Exact B06 improvement analysis: why retuning the graph regularizer does not lower 17 to 13

Keep the scalar regularizer `alpha>0` free in the graph-BL proof. The same exact calculation before setting `alpha=(2pi e)^2` yields

\[
 |\phi_Z(t)|^4
 \le
 \det\!\left(I+\frac{a^2}{\alpha}M^TM\right)^{-1/2}
 \left(\frac{2\pi e}{\sqrt\alpha}\right)^\theta,
\]

where `a=2t` and

\[
 \theta=\operatorname{tr}\left[a^2M^TM(\alpha I+a^2M^TM)^{-1}\right].
\]

Suppose `M` has fixed rank `r` with nonzero singular values `sigma_1,...,sigma_r`. If `alpha/a^2 ->0`, then each singular direction has effective weight tending to one, and its contribution to the fourth-power majorant is asymptotic to a constant multiple of `1/(|a| sigma_l)`. Hence the best power available after the fourth root is still `|t|^{-r/4}`. If `alpha` is comparable to `a^2`, each effective weight stays strictly below one and the determinant factors no longer generate a stronger power. If `alpha/a^2 ->infinity`, the determinant approaches one and decay weakens further.

Therefore the current scalar-regularizer family cannot turn an order-four crossing certificate into a strictly integrable absolute Fourier envelope. The present direct inversion route needs `r>4`, explaining why order five is the first closing integer order in this mechanism. This is a **method-specific barrier**, not a theorem that 17 eigenvalues are necessary for the density statement.

## Exact analytic endpoint obstruction: `1/|t|` Fourier + full half-potential is insufficient in the abstract

Let `U,V` be independent `Uniform[-1/2,1/2]` and

\[
 Q_0=2UV.
\]

The product change of variables gives

\[
 p_{Q_0}(q)=\log\frac1{2|q|}\,\mathbf1_{\{|q|<1/2\}},
\]

so the density is logarithmically unbounded at zero. On the other hand,

\[
 \phi_{Q_0}(t)=\frac{2\,\operatorname{Si}(t/2)}{t},
\]

so `|phi(t)|<=min(1,C/|t|)` for an absolute constant. Moreover

\[
 \int p_{Q_0}(q)^3\,dq
 =\int_0^1(-\log x)^3\,dx=6.
\]

Hölder with exponents `3` and `3/2` and the uniform translated integrability of `|q-a|^{-3/4}` on an interval of length one gives

\[
 \sup_a\mathbb E|Q_0-a|^{-1/2}<\infty.
\]

Thus the two abstract outputs

\[
 |\phi(t)|=O(|t|^{-1})
 \quad\text{and}\quad
 \sup_a\mathbb E|Z-a|^{-1/2}<\infty
\]

do not imply an essentially bounded density. Consequently a prospective `17 -> 13` argument cannot close merely by combining the manuscript's order-four Fourier endpoint with its nine-direction half-potential as black boxes. It must use additional quadratic/product structure at the endpoint (for example cancellation before absolute Fourier integration, or a genuinely weighted curved-fiber/product argument).

This example is **not** a counterexample to the fixed-multiplicity theorem or to the full QFORM conjecture: its quadratic matrix has only two nonzero eigenvalues and has a large principal indefinite pivot. It only rules out the stated abstract compiler.

## Threshold accounting

Within the current interpolation proof, the `17` appears only in the worst bad-ratio index `r=4`: global rank `<=3r` and the need for `r+1` large diagonal entries require `m>=4r+1=17`. At `m=16`, rank bookkeeping alone forces only four large diagonal entries, which is compatible with the restricted rank bound `rank R_LL<=4`. Thus lowering the spectral count using the existing skeleton requires either a sharper structural rank/support statement or an analytic endpoint that avoids order-five direct Fourier inversion.

No such full replacement is established in this run, so the certified theorem remains the 17-eigenvalue candidate.

## Review status and next proof obligation

- Mathematical 17-eigenvalue baseline: **PASS in this independent fleet03/B06 review**.
- Projection equality typo: **GAP, nonfatal; one-symbol repair `=` -> `<=`**.
- Named supplementary repository files: **UNCHECKED / unavailable** in the inspected root snapshot.
- Independent-validation gate: **not self-awarded**; this run is one review only.
- Lower threshold: **OPEN**.
- Full three-eigenvalue conjecture: **OPEN**.

The most concrete next B06 obligation is an order-four endpoint theorem that retains the original-coordinate product structure before absolute-value integration. A successful statement would need to beat the `1/|t|` barrier in a way invalid for the two-variable product witness above, rather than merely append a generic half-potential estimate.

Execution status: `WITHOUT_VERIFIED_BRAIN`; repository reads/writes occurred, but no authenticated native brain retrieval/receiver-use event was observed. No scheduler, task, notification, email, permission, or public-release state was changed.
