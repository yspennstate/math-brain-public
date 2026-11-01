SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T23:42:26Z.
attacking: the r43 unique-heavy-row collar when the hub-star-orthogonal transverse crossing has rank two; use the exact rank-three constraint to trade a vanishing physical pivot for a growing three-dimensional source crossing, then splice it with the scalar-pivot theorem.

# fleet01/B11 — rank-two transverse crossing / scalar-pivot interpolation

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW STRUCTURAL IDENTITY / PARTNER RESULT APPLIED / NEW PIVOT-UNIFORM SUBBRANCH / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full owner target remains open. This report proves a new exact-rank-three structural theorem for indefinite forms and pays the branch in which a unique physical hub has two genuinely transverse source-crossing directions. It does not handle the remaining rank-one/coplanar collar, and it does not handle arbitrary additional nonseparable spectrum.

No Gaussian, log-concave, moment, compact-support, connected-support, post-rotation independence, conditional-density cap, arbitrary-joint coarea, pointwise law-uniform van-der-Corput decay, or deletion of a small nonzero coefficient is used.

## 1. Sources consumed


The designated fleet02/B11 result actually used below is its completed three-dimensional cross-bank theorem, source-pinned by the handoff commit `23238b312e50d10be9d313e44a514bcbff7217c2`, with canonical mathematics at

`yspennstate/math-open-problems@25c25e15fa0f570e7b0b1a2a9fab0811eda07113:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260923T201026Z-fleet02-B11-QFORM-auto11/REPORT.md`.

For two disjoint ORIGINAL-coordinate product banks, arbitrary within-bank phases, orthogonal three-dimensional projections with density caps `M_X,M_Y`, and invertible cross matrix `C`, it proves

\[
\|p_Q\|_\infty\le 3\left(\frac{M_XM_Y}{|\det C|}\right)^{1/3}.
\]

Using the product-projection cap `M_X,M_Y\le 2^{3/2}` gives

\[
\boxed{\|p_Q\|_\infty\le6|\det C|^{-1/3}},
\tag{1.1}
\]

with a continuous `C_0` density. The theorem retains arbitrary self-quadratic and affine phases in each bank.

The scalar-pivot input is the completed orientation-free theorem

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`:
for an exact-rank-three form `A=RMR^T`, `R^TR=I_3`, physical pivot `a=A_{ii}\ne0`, and spectral-row leverage `\ell_i=\|r_i\|^2`,

\[
\boxed{
\|p_Q\|_\infty\le128\,[\ell_i|a||\det M|]^{-1/4}.
}
\tag{1.2}
\]

The newest fleet02/B11 correction at handoff commit `5f1b54e726852a38629191b92a02d0f2e694d662` is also retained: two disjoint leaf subsets attached to one shared hub still form only a rank-two saddle and can preserve a logarithmic singularity. The present argument therefore spends an actual transverse crossing; it does not count the hub twice.

## 2. Exact rank-three star/cross normal form

Let `A` be a real symmetric matrix of rank at most three. Fix one ORIGINAL coordinate `i` and disjoint ORIGINAL-coordinate sets `L,R`, disjoint also from `{i}`. Write the rectangular submatrix on rows `{i}\cup L` and columns `{i}\cup R` as

\[
B=\begin{pmatrix}
 a&r^T\\
 c&N
\end{pmatrix},
\qquad
a=A_{ii},\quad c=A[L,i],\quad r=A[i,R],\quad N=A[L,R].
\tag{2.1}
\]

Assume `c\ne0` and `r\ne0`. Set

\[
\alpha=\|c\|_2,\qquad \beta=\|r\|_2,
\qquad e=c/\alpha,\qquad f=r/\beta,
\tag{2.2}
\]

and let

\[
P_e=I-ee^T,\qquad P_f=I-ff^T,
\qquad C=P_eNP_f:e^\perp\leftarrow f^\perp.
\tag{2.3}
\]

Write `D_2(C)=s_1(C)s_2(C)` when `rank C=2`, where `s_1,s_2` are its two nonzero singular values.

### Theorem 2.1 — `QFORM-RANK3-SHAREDHUB-RANK2-TRANSVERSE-NORMALFORM-v1`

Under the hypotheses above:

1. `rank C\le2`.
2. If `rank C=2`, then necessarily `a\ne0`.
3. If `rank C=2`, then `N` has rank exactly three and its product of nonzero singular values satisfies the exact identity

\[
\boxed{
\Delta_3(N):=s_1(N)s_2(N)s_3(N)
=\frac{\alpha\beta}{|a|}\,D_2(C).
}
\tag{2.4}
\]

Equivalently, after source-orthogonal changes of coordinates on `L,R`, the rank-three crossing determinant is forced to grow like `1/|a|` as the nonzero physical pivot shrinks.

#### Proof

Decompose the left and right source spaces as

\[
\mathbb R^L=\operatorname{span}\{e\}\oplus e^\perp,
\qquad
\mathbb R^R=\operatorname{span}\{f\}\oplus f^\perp.
\]

Suppose first that `rank C=k`. Choose orthonormal bases in `e^\perp,f^\perp` in which the nonzero part of `C` is an invertible `k\times k` diagonal singular-value block `\Sigma`. Decompose the remaining first-column and first-row components of `N` into active and null parts. In block notation,

\[
B\sim
\begin{pmatrix}
 a&\beta&0&0\\
 \alpha&d&q_1^T&q_0^T\\
 0&p_1&\Sigma&0\\
 0&p_0&0&0
\end{pmatrix}.
\tag{2.5}
\]

Here the symbol `\sim` means multiplication on the left and right by orthogonal matrices, hence rank and nonzero singular values are preserved.

Because `\Sigma` is invertible, ordinary row/column elimination through this block gives

\[
\operatorname{rank}B
=k+\operatorname{rank}
\begin{pmatrix}
 a&\beta&0\\
 \alpha&\delta&q_0^T\\
 0&p_0&0
\end{pmatrix},
\qquad
\delta=d-q_1^T\Sigma^{-1}p_1.
\tag{2.6}
\]

The residual matrix has rank at least one because `\alpha,\beta>0`. Since `B` is a submatrix of `A` and `rank A\le3`, (2.6) immediately gives `k\le2`, proving (1).

Now take `k=2`. Then the residual matrix in (2.6) must have rank at most one. Its first two rows/columns contain

\[
\begin{pmatrix}a&\beta\\ \alpha&\delta\end{pmatrix}.
\]

Because both `\alpha` and `\beta` are nonzero, rank at most one forces

\[
q_0=0,\qquad p_0=0,
\qquad a\delta=\alpha\beta.
\tag{2.7}
\]

In particular `a\ne0`, proving (2), and

\[
\delta=\frac{\alpha\beta}{a}.
\tag{2.8}
\]

The vanishing of `p_0,q_0` means that `N` is supported entirely on the three-dimensional active row/column spaces `\operatorname{span}\{e\}\oplus\operatorname{range}\Sigma` and `\operatorname{span}\{f\}\oplus\operatorname{range}\Sigma^T`. Its active matrix is

\[
N_3=\begin{pmatrix}
 d&q_1^T\\
 p_1&\Sigma
\end{pmatrix}.
\tag{2.9}
\]

The Schur determinant formula and (2.8) give

\[
\det N_3
=\det\Sigma\,(d-q_1^T\Sigma^{-1}p_1)
=\det\Sigma\,\frac{\alpha\beta}{a}.
\tag{2.10}
\]

Hence `N_3` is invertible, `rank N=3`, and because all other singular values of `N` are zero,

\[
\Delta_3(N)=|\det N_3|
=D_2(C)\frac{\alpha\beta}{|a|}.
\]

This proves (3). QED.

### Corollary 2.2 — zero pivot forbids two transverse crossing directions

If `a=A_{ii}=0` while `c,r\ne0`, then

\[
\boxed{\operatorname{rank}(P_eNP_f)\le1.}
\tag{2.11}
\]

This is an exact algebraic reason that the literal zero-pivot endpoint cannot be paid by pretending two transverse crossing directions survive. It is compatible with the source-valid logarithmic same-hub obstruction.

## 3. Density bound in the rank-two transverse branch

Assume now that `A=RMR^T` has exact rank three, `R^TR=I_3`, and `M` is invertible with either indefinite signature `(2,1)` or `(1,2)`. Keep the notation above and suppose `rank C=2`.

Condition on the physical hub `X_i` and on every ORIGINAL coordinate outside `L\cup R\cup\{i\}`. The remaining `L` and `R` coordinates are still independent product banks. Every hub/outside interaction becomes an affine term internal to one of those banks, while `A[L,L]` and `A[R,R]` remain arbitrary within-bank quadratic phases. The only cross-bank quadratic term is

\[
2X_L^TNX_R.
\tag{3.1}
\]

By Theorem 2.1, `N` has rank three and `\Delta_3(N)=\alpha\beta D_2(C)/|a|`. Applying the completed fleet02/B11 three-dimensional crossing theorem (1.1), uniformly in all conditioned values, yields a continuous conditional density and

\[
\boxed{
\|p_Q\|_\infty
\le6\left(\frac{|a|}{\alpha\beta D_2(C)}\right)^{1/3}.
}
\tag{3.2}
\]

The same Fourier envelope is uniform in the conditioned phases, so averaging restores a continuous `C_0` unconditional density.

This is the promised actual application of the designated partner result. It has the useful direction that the bound improves when `|a|\downarrow0`: the rank-three constraint forces the source crossing determinant to increase.

## 4. Pivot/crossing interpolation

The scalar-pivot theorem (1.2) gives simultaneously

\[
\|p_Q\|_\infty
\le128(\ell_i|a||\det M|)^{-1/4}.
\tag{4.1}
\]

Combining (3.2) and (4.1), with `x=|a|`, gives

\[
\|p_Q\|_\infty
\le\min\left\{
128(\ell_i|\det M|)^{-1/4}x^{-1/4},
6(\alpha\beta D_2(C))^{-1/3}x^{1/3}
\right\}.
\tag{4.2}
\]

For positive constants `A_0,B_0`,

\[
\sup_{x>0}\min\{A_0x^{-1/4},B_0x^{1/3}\}
=A_0^{4/7}B_0^{3/7}.
\tag{4.3}
\]

Therefore:

### Theorem 4.1 — `QFORM-RANK2-TRANSVERSE-PIVOT-INTERPOLATION-v1`

In the exact-rank-three setting above, whenever `c,r\ne0` and `rank(P_eNP_f)=2`,

\[
\boxed{
\|p_Q\|_\infty
\le K_0\,[\ell_i\,\alpha\beta D_2(C)\,|\det M|]^{-1/7},
}
\tag{4.4}
\]

where

\[
K_0=(128^4\,6^3)^{1/7}=34.4836616886\ldots .
\tag{4.5}
\]

The law has a continuous `C_0` density. The estimate is completely uniform in the physical pivot `a`: no lower or upper bound on `|a|` is required.

The scale is correct. Under `A\mapsto sA`, `\alpha,\beta` scale like `s`, `D_2(C)` like `s^2`, `|\det M|` like `s^3`, while `\ell_i` is dimensionless, so the bracket in (4.4) scales like `s^7` and the density bound like `s^{-1}`.

## 5. Application to the r43 unique-heavy-row survivor

The source-pinned fleet03/B11 r43 report

`yspennstate/math-open-problems@d75835c958b5dcdd28649eb79af0faf3103b5d89:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T221215Z-fleet03-B11-QFORM-r43/REPORT.md`

reduces its exact-rank-three indefinite hard chamber, after earlier paid exits, to a unique physical hub `i` with

\[
\ell_i>\gamma_0:=\frac34\beta_0,
\qquad
\beta_0=\frac{289}{15984},
\tag{5.1}
\]

and two disjoint ORIGINAL-coordinate star banks with

\[
\alpha>\theta_0s,\qquad \beta>\theta_0s,
\qquad
\theta_0=\frac{\sqrt{191}}{32}\beta_0
=0.00780870609624\ldots ,
\tag{5.2}
\]

where `s=min_j|lambda_j(M)|`. If, for those source-valid banks,

\[
D_2(P_eNP_f)\ge\nu s^2
\tag{5.3}
\]

for some `\nu>0`, then `|\det M|\ge s^3` and (4.4) gives

\[
\boxed{
\|p_Q\|_\infty
<255.007\,\nu^{-1/7}s^{-1}.
}
\tag{5.4}
\]

This density is continuous and `C_0`. Thus the arbitrary-small/nonzero physical pivot is no longer an obstruction in the genuinely rank-two-transverse part of the unique-heavy-row collar. The deterioration in (5.4) is now only through the true geometric degeneration `D_2(C)\downarrow0`.

## 6. Rank-two logarithmic control and the role of the third direction

For independent centered unit uniforms `X,Y`,

\[
p_{2XY}(t)=\log\frac1{2|t|},\qquad 0<|t|<\frac12,
\tag{6.1}
\]

so the opposite-sign rank-two saddle is genuinely unbounded.

Theorem 2.1 identifies a precise third-direction mechanism in the current rotated branch. After removing the two star directions from the interbank crossing, two independent transverse crossing singular values give `D_2(C)>0`. Exact total rank three then forces the Schur compatibility

\[
a\delta=\alpha\beta,
\tag{6.2}
\]

and therefore forces a three-dimensional source crossing with volume

\[
\Delta_3(N)=\frac{\alpha\beta D_2(C)}{|a|}.
\tag{6.3}
\]

The partner Fourier theorem spends that source volume as an integrable `|t|^{-3/2}` gain. If the physical pivot is tiny, (6.3) makes the crossing stronger; if the pivot is large, the scalar-Schur theorem is stronger. Their balance is exactly the exponent `1/7` in (4.4). At `a=0`, (2.11) says the two-transverse-direction mechanism cannot exist at all, so no contradiction with the rank-two logarithmic example arises.

The conclusion is sign-symmetric: the argument uses invertibility and rank-three structure, not a preferred sign, and therefore covers both `(+, +, -)` and `(+, -, -)`.

## 7. Remaining implication

The first unpaid B11 implication is now

`QFORM-R43-RANKONE-COPLANAR-COLLAR-v1`:

in the unique-heavy-row/two-star survivor, control the regime

\[
\operatorname{rank}(P_eNP_f)\le1
\quad\text{or quantitatively}\quad
D_2(P_eNP_f)\ll s^2,
\]

without dropping the small transverse coefficients. The newest fleet03/B11 rank-one shared-hub tensor receiver pays the genuine rank-one crossing when its projected transverse component is bounded below; the missing splice is the near-rank-one/coplanar limit together with the inherited same-bank internal curvature. The source-valid fleet02/B11 same-hub logarithmic example forbids treating two leaf subsets as two independent smoothing hubs.

Even a complete exact-rank-three closure would still leave the arbitrary-additional-nonseparable-spectrum bridge required by the full owner quantifiers.

## 8. Verification scope

A deterministic numerical verifier in this bundle checks the exact identity (2.4) on random rank-three indefinite frames and reproduces the constants (4.5) and (5.4). Numerical checks are sanity checks only; the proof is the algebra above.

Privacy/source review: the changed files contain only mathematical statements, public-style repository pins already authorized by this research programme, and nonsecret run metadata. No credentials, private personal data, unrelated material, scheduler identifiers, signed URLs, or model/API keys are included.
