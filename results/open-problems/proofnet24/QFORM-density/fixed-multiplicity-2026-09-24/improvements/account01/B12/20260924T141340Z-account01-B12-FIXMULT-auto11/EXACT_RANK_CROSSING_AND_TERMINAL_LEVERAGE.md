# B12 improvement — exact-rank crossing Plancherel receiver and terminal `s_16` leverage polarization

Run: `20260924T141340Z-account01-B12-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **two new supporting theorems and sharper `17 -> 16` survivor; no unconditional 16-eigenvalue theorem is claimed.** All statements preserve arbitrary independent rough coordinate laws, arbitrary affine terms, arbitrary signs, and arbitrary ambient dimension.

## 1. Exact-rank crossing Plancherel theorem

The manuscript's determinant theorem is designed to work for arbitrary crossing rank without selecting or rotating random coordinates. When the entire physical crossing itself has **exact finite rank**, one can do better by combining the manuscript's product-projection lemma with a bilinear Plancherel estimate. The rotations below are only deterministic maps used to form marginal densities; independence after rotation is never asserted.

### Theorem 1 — `QFORM-EXACT-RANK-CROSS-PLANCHEREL-v1`

Let `I,J` be disjoint original-coordinate banks. Let their coordinates be independent and have probability densities bounded by one. Let

\[
Z=F(X_I)+2X_I^TMX_J+G(X_J),
\]

where `F,G` are arbitrary real measurable functions finite almost surely, and suppose

\[
\operatorname{rank}M=r\ge3.
\]

Let `sigma_1,...,sigma_r>0` be the nonzero singular values of `M` and put

\[
\Delta_r(M)=\prod_{j=1}^r\sigma_j(M).
\]

Then for every nonzero real `t`,

\[
\boxed{
|\phi_Z(t)|
\le
\left(\frac{\pi e}{|t|}\right)^{r/2}
\Delta_r(M)^{-1/2}.
}
\tag{1.1}
\]

Consequently `Z` has a continuous `C_0` density and

\[
\boxed{
\|p_Z\|_\infty
\le
\frac{er}{r-2}\,\Delta_r(M)^{-1/r}.
}
\tag{1.2}
\]

In particular, if `rank M=4`, then by Cauchy–Binet

\[
Z_4(M)=\det{}'(M^TM)=\Delta_4(M)^2
\]

and

\[
\boxed{
\|p_Z\|_\infty\le2e\,Z_4(M)^{-1/8}.
}
\tag{1.3}
\]

If `rank M=3`, the corresponding bound is `3e Z_3(M)^{-1/6}`.

### Proof

Take a thin singular-value decomposition

\[
M=U\Sigma V^T,
\]

where `U^TU=V^TV=I_r` and `Sigma=diag(sigma_1,...,sigma_r)`. For fixed `t`, define a complex measure on `R^r`

\[
\alpha_t(E)
=\mathbb E\left[e^{itF(X_I)}\mathbf1_{\{U^TX_I\in E\}}\right].
\]

Its total variation is dominated by the probability law of `U^T X_I`. By the manuscript's product-projection lemma, that law has a density `p_U` with

\[
\|p_U\|_\infty\le e^{r/2}.
\]

Hence `alpha_t` has a density `a_t` satisfying

\[
|a_t|\le p_U,
\qquad
\|a_t\|_1\le1,
\qquad
\|a_t\|_2\le e^{r/4}.
\tag{1.4}
\]

Define `beta_t,b_t` from `V^T X_J` and `G` in the same way. Then also

\[
\|b_t\|_2\le e^{r/4}.
\tag{1.5}
\]

Independence of the two **original banks** gives the exact representation

\[
\phi_Z(t)
=
\int_{\mathbb R^r}\int_{\mathbb R^r}
 a_t(u)b_t(v)e^{2it u^T\Sigma v}\,du\,dv.
\tag{1.6}
\]

With the manuscript convention `hat a(xi)=int e^{i xi dot u}a(u)du`, the inner integral is `hat a_t(2t Sigma v)`. Cauchy–Schwarz and Plancherel therefore give

\[
\begin{aligned}
|\phi_Z(t)|
&\le \|b_t\|_2
\left(\int|\widehat a_t(2t\Sigma v)|^2dv\right)^{1/2}\\
&=\|b_t\|_2(2|t|)^{-r/2}\Delta_r(M)^{-1/2}
(2\pi)^{r/2}\|a_t\|_2\\
&\le
\left(\frac{\pi e}{|t|}\right)^{r/2}\Delta_r(M)^{-1/2},
\end{aligned}
\]

which is (1.1).

Together with `|phi_Z|<=1`, write

\[
|\phi_Z(t)|\le\min\left\{1,\left(\frac{u}{|t|}\right)^{r/2}\right\},
\qquad
u=\pi e\,\Delta_r(M)^{-1/r}.
\]

Since `r/2>1`, the manuscript's power-envelope lemma gives

\[
\|p_Z\|_\infty
\le
\frac{u(r/2)}{\pi(r/2-1)}
=
\frac{er}{r-2}\Delta_r(M)^{-1/r}.
\]

The majorant is integrable, so Fourier inversion gives a continuous `C_0` representative. QED.

### Scope note

Exact crossing rank is essential to this proof as stated. If `M` has additional nonzero singular directions, simply deleting them is not justified: after singular-vector projection the retained and omitted projected coordinates need not be conditionally independent. This theorem therefore does **not** silently convert a general high-rank crossing into its top three or four modes.

## 2. Four-column slice receiver

The exact-rank theorem has a useful completely physical formulation requiring no leverage condition.

For a fixed original-coordinate four-set `T`, put

\[
W_T(A)
:=
\sum_{\substack{S\subset T^c\\|S|=4}}
\det(A_{S,T})^2.
\tag{2.1}
\]

Take the physical partition `J=T`, `I=T^c`. Its crossing is

\[
M=A_{T^c,T},
\]

which has exactly four columns, and Cauchy–Binet gives

\[
\det(M^TM)=W_T(A).
\]

Therefore whenever `W_T(A)>0`, `rank M=4`, and Theorem 1 gives

\[
\boxed{
\|p_{X^TAX+b^TX+c}\|_\infty
\le2e\,W_T(A)^{-1/8},
}
\tag{2.2}
\]

with a continuous `C_0` density. All coefficients within `T`, within `T^c`, and all affine terms are absorbed into the arbitrary functions `F,G`; no coefficient is deleted.

Moreover

\[
\boxed{V_4(A)=\sum_{|T|=4}W_T(A).}
\tag{2.3}
\]

Thus the no-pivot `s_16(A)>=1` hypothesis, which already implies `V_4>=kappa^4`, has the following rigorous branch. For any fixed `N>=1`, if

\[
\max_T W_T(A)\ge\frac{\kappa^4}{N},
\]

then

\[
\boxed{
\|p_Q\|_\infty
\le160e\,N^{1/8}.
}
\tag{2.4}
\]

For example `N=256` gives

\[
\boxed{\|p_Q\|_\infty\le320e<960.}
\tag{2.5}
\]

Hence any still-unpaid normalized `s_16` no-pivot state must, for this concrete branch choice, satisfy

\[
W_T<\kappa^4/256
\quad\text{for every four-set }T,
\]

and therefore its order-four disjoint volume is spread across more than 256 distinct physical four-column banks. This does not close `s_16`, but it turns part of the previous seed-preimage issue into an explicitly **column-diffuse** survivor.

## 3. Terminal `r=4` double-leverage polarization

I next combine the completed B09 terminal determinant-escalation theorem with an exact leverage calculation. This produces a new quantitative geometry of every low-residual terminal seed.

Use the normalized manuscript constants

\[
\eta=10^{-2},
\qquad
a=\sqrt{\eta+\eta^2}=\frac{\sqrt{101}}{100}.
\]

The completed predecessor

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account01/B09/20260924T124412Z-account01-B09-FIXMULT-auto11/TERMINAL_R4_ESCALATION.md`

proves the following. If `A=A^T` has no `eta`-pivot, `s_16(A)>=1`, and an invertible disjoint four-seed

\[
B=A_{S,T}
\]

has interpolation completion residual `||E||_F<=1/16`, then there is a four-set `H` disjoint from `S union T` such that, writing

\[
C=A_{H,T},
\qquad
G=A_{S,H},
\qquad
P=C B^{-1}G,
\]

one has

\[
\boxed{s_4(P)\ge\delta},
\qquad
\delta:=\frac{74-3\sqrt{101}}{100}
=0.438503731366\ldots .
\tag{3.1}
\]

Every entry of `C,G` is an off-diagonal original coefficient, hence has modulus `<a`, so

\[
\|C\|_{op},\|G\|_{op}<4a.
\tag{3.2}
\]

Define

\[
\gamma:=\frac{\delta}{4a}
=
\frac{74-3\sqrt{101}}{4\sqrt{101}}
=1.090818801888\ldots>1,
\tag{3.3}
\]

and

\[
h_*:=\frac1{1+\gamma^2}
=0.456644846316\ldots<\frac12.
\tag{3.4}
\]

### Theorem 2 — `QFORM-S16-TERMINAL-DOUBLE-LEVERAGE-POLARIZATION-v1`

Under the preceding terminal hypotheses,

\[
\boxed{s_4(CB^{-1})>\gamma,
\qquad
s_4(B^{-1}G)>\gamma.}
\tag{3.5}
\]

Consider the two exact-rank-four physical crossings

\[
M_T=
\begin{pmatrix}B\\ C\end{pmatrix}
=A_{S\cup H,T},
\qquad
M_S=
\begin{pmatrix}B^T\\ G^T\end{pmatrix}
=A_{T\cup H,S}.
\tag{3.6}
\]

For a full-column-rank crossing `M`, let

\[
\ell_i(M)=e_i^TM(M^TM)^{-1}M^Te_i
\]

be its physical row leverage. Then

\[
\boxed{
\ell_s(M_T)<h_*<1/2\quad(s\in S),
\qquad
\ell_h(M_T)>1-h_*>1/2\quad(h\in H),
}
\tag{3.7}
\]

and symmetrically

\[
\boxed{
\ell_t(M_S)<h_*<1/2\quad(t\in T),
\qquad
\ell_h(M_S)>1-h_*>1/2\quad(h\in H).
}
\tag{3.8}
\]

Thus the terminal low-residual chamber does not leave an arbitrary high-leverage crossing: it forces the **same four cancellation coordinates `H` to be strictly high-leverage in both neighboring exact-rank-four crossings**, while all four rows of each old seed bank are uniformly below the one-half threshold.

### Proof

From `P=(CB^{-1})G` and the singular-value inequality

\[
s_{min}(XY)\le s_{min}(X)\|Y\|,
\]

(3.1)–(3.2) give

\[
s_4(CB^{-1})
\ge\frac{s_4(P)}{\|G\|}
>\frac\delta{4a}=\gamma.
\]

Likewise `P=C(B^{-1}G)` gives the second inequality in (3.5).

Put

\[
X=CB^{-1}.
\]

Then

\[
M_T=
\begin{pmatrix}I\\X\end{pmatrix}B.
\]

The row-leverage projection is

\[
\Pi_T=M_T(M_T^TM_T)^{-1}M_T^T.
\]

Its `S x S` principal block is exactly

\[
( I+X^TX)^{-1},
\tag{3.9}
\]

while its `H x H` block is

\[
X(I+X^TX)^{-1}X^T
=I-(I+XX^T)^{-1}.
\tag{3.10}
\]

Since every singular value of `X` exceeds `gamma`, (3.9) is bounded above by `h_* I`, while (3.10) is bounded below by `(1-h_*)I`. Taking diagonal entries proves (3.7). Apply the same argument to

\[
Y=G^TB^{-T}=(B^{-1}G)^T
\]

and `M_S=[I;Y]B^T` to obtain (3.8). QED.

## 4. Exact-rank receiver applied to the terminal collar

Theorem 1 applies directly to both crossings in (3.6), because each has exactly four columns and `B` is invertible. In particular

\[
Z_4(M_T)
=
\det(B)^2\det(I+X^TX)
>
(1+\gamma^2)^4\det(B)^2,
\]

so conditioning every coordinate outside `(S union H) union T` and then averaging gives the actual final-matrix inequality

\[
\boxed{
\|p_Q\|_\infty
<
\frac{2e}{\sqrt{1+\gamma^2}}\,|\det B|^{-1/4}.
}
\tag{4.1}
\]

The same bound follows from `M_S`.

The B09 predecessor also proves that with

\[
R=22.6532460869\ldots,
\]

at least one of `|det C|,|det G|` is at least `R|det B|`. Cauchy–Binet in the corresponding one of the two stacked crossings then gives the slightly sharper local estimate

\[
\boxed{
\|p_Q\|_\infty
\le
2e(1+R^2)^{-1/8}|\det B|^{-1/4}.
}
\tag{4.2}
\]

Both (4.1) and (4.2) prove a continuous density for every individual terminal seed, but their constants still depend on the seed determinant. The sampled seed determinant may be arbitrarily small in high dimension; therefore these inequalities do **not** constitute a universal `s_16` theorem.

## 5. What has been reduced and what remains

The unconditional fixed-multiplicity theorem remains at **17**. This run makes the `s_16` survivor more explicit in two independent ways.

1. **Column-slice diffusion.** A single physical four-column slice with universal order-four mass is already paid by (2.2), with no leverage hypothesis. Thus a hard `s_16` state must spread the guaranteed `V_4>=kappa^4` over many different four-column banks.
2. **Double high-leverage collar.** Whenever the terminal volume-sampling seed has small completion residual, the B09/B20 three-bank collar is quantitatively polarized: the same four `H` coordinates are above leverage `0.543355...` in both adjacent exact-rank-four crossings, while the old `S`/`T` rows are below `0.456645...`.

This is stronger than saying merely that the terminal restricted rank equals four. It identifies a concrete next analytic target:

> build a product-preserving receiver for a **common four-coordinate double-high-leverage collar**, or prove that determinant-squared mass spread over arbitrarily many four-column slices necessarily enters an already-completed diffuse/grouped receiver.

Neither implication is proved here, so **no replacement of 17 by 16 is claimed or validated**. Any future replacement still requires a full end-to-end proof and two genuinely separate reviews under the owner protocol.

## 6. Scope checks

- No Gaussianity, moments, support restrictions, identical laws, sign assumptions, or post-rotation independence are used.
- SVD/projection maps in Theorem 1 are deterministic integration maps; the manuscript's product-projection lemma supplies the needed marginal density bounds for the rotated projections.
- No spectral or coefficient remainder is deleted.
- Every conditioning is on original physical coordinates and changes only the arbitrary within-bank functions/affine terms.
- The exact-rank theorem explicitly does **not** claim stability under adding further nonzero crossing singular directions.
- Full three-eigenvalue QFORM remains open.
