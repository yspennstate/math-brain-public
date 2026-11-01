# fleet02/B19 — guarded integration of a complete nine-eigenvalue replacement

Run: `20260924T150913Z-fleet02-B19-fixedmult-r11`  
Baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Source-backed replacement audited here: fleet02/B12 artifact at master snapshot `e8370a03c655a2dcd76906089f81eec9565ee028`, blob `59f3bdeb3f2301ec10add15ad3a55559524e5cce`, `NINE_EIGENVALUE_5338_AND_PAIRED_KERNEL.md`.

## Guarded verdict

**PASS after two harmless statement-level repairs described below.** The source contains a complete replacement argument preserving the full baseline quantifiers:

> If `X_1,...,X_n` are independent real coordinates with densities bounded by `K`, `A=A^T`, `b,c` are arbitrary, and `s_9(A)>=s>0`, then `Q=X^TAX+b^TX+c` has an essentially bounded density with
> \[
> \|p_Q\|_\infty<5338\,K^2/s.
> \]

I independently reconstructed the analytic compiler, promotion tree, no-pivot branch, all pivot branches, and final scaling. This lowers the source-backed candidate threshold from 17 to 9. It does **not** prove multiplicity eight and does **not** solve the unrestricted three-eigenvalue conjecture.

## Dependency map

The replacement uses only the already-audited baseline ingredients:

1. Fourier inversion / Riesz half potential, baseline lines 91–160.
2. Schur spectral count / nonsymmetric singular-value perturbation, lines 161–207.
3. geometric BL and product-projection density, lines 219–282.
4. scalar Fourier powers, lines 284–301.
5. scalar square, definite pair, hyperbolic pair, quarter-power concentration, lines 404–525.
6. disjoint-minor interpolation/completion and spectral-to-volume conversion, lines 528–619.
7. fair original-coordinate cut, lines 621–630.
8. pivot half-potential estimates, lines 654–714.
9. New grouped product-Fourier compiler and determinant-mass promotion tree from the pinned B12 source.

No new support, moment, iid, sign, log-concavity, exact-rank, diagonal-basis, leverage, or post-rotation-independence hypothesis is used.

## New grouped product-Fourier lemma — reconstruction

Let `H,I,J` be disjoint **original-coordinate** banks. Retain `k` hub coordinates/directions in `H`, write their live projection as `W`, and write the relevant part of the polynomial as

\[
Q=F(X_H)+2\langle W,M_IY+M_JZ+\beta\rangle+R_I(Y)+2Y^TC_0Z+R_J(Z),
\]

with `Y=X_I`, `Z=X_J`, arbitrary same-bank/affine phases, and `M_J` of row rank `k`. Let `S` be the product of its nonzero singular values. Project rows of `C_0` orthogonally off `row(M_J)` to obtain `C`. For `ell>=1`, let

\[
Z_\ell=\sum_{|T|=\ell}\det(C_TC_T^T),\qquad
w_T=\frac{\det(C_TC_T^T)}{Z_\ell},\qquad
\alpha_i=\sum_{T\ni i}w_T,
\]

and assume the retained rows satisfy `0<alpha_i<=1/2`; rows with `alpha_i=0` are dropped because they enter no weighted determinant and their Fourier factor is at most one. Set `d=k+ell`.

Pushing the complex `H`-measure to `W` gives a density `a_t` with `|a_t|<=p_W`, so `||a_t||_2^2<=M_H`. Plancherel at frequency `2t` gives

\[
|\phi_Q(t)|^2\le M_H(\pi/|t|)^k\|\mu_t\|_2^2.
\]

Conditioning only on literal `Y` and using Hilbert-space Jensen, then expanding the squared `L^2` norm with an independent copy `Z'`, reduces to `D=Z-Z'` with independent cap-one coordinates and factors

\[
\kappa_\varepsilon(M_JD)\prod_i|\widehat f_i(2t\langle c_i,D\rangle)|.
\]

For each determinant subset `T`, the map

\[
D\mapsto\bigl(M_JD,(\langle c_i,D\rangle)_{i\in T}\bigr)
\]

has Gram determinant `S^2 det(C_TC_T^T)`. The audited product-projection lemma, followed by deterministic linear scaling, gives density cap

\[
\frac{e^{d/2}}{S\sqrt{\det(C_TC_T^T)}}.
\]

Weighted Hölder with the `w_T` and the scalar Fourier estimate at power `1/alpha_i>=2` yields

\[
\int |\widehat f_i(2t(y+u))|^{1/\alpha_i}\,dy
\le \frac{\pi\sqrt{2e\alpha_i}}{|t|}.
\]

If an `ell`-subset with law `w` is uniformly ordered, entropy subadditivity gives exactly

\[
H(w)+\sum_i\alpha_i\log\alpha_i
\le \ell\log\ell-\log(\ell!).
\]

Combining these factors and taking the square root proves

\[
|\phi_Q(t)|\le\min\{1,K_{k,\ell}|t|^{-d/2}\},
\]

where

\[
K_{k,\ell}=M_H^{1/2}\pi^{d/2}2^{\ell/4}e^{(k+2\ell)/4}
\left(\frac{\ell^\ell}{\ell!}\right)^{1/4}
S^{-1/2}Z_\ell^{-1/4}.
\]

For `d>2`, direct integration of this envelope and Fourier inversion gives

\[
\|p_Q\|_\infty\le
\frac d{d-2}M_H^{1/d}2^{\ell/(2d)}e^{(k+2\ell)/(2d)}
\left(\frac{\ell^\ell}{\ell!}\right)^{1/(2d)}
S^{-1/d}Z_\ell^{-1/(2d)}.
\]

All rotations/projections here are deterministic integral manipulations. Product provenance is retained by conditioning on original coordinate banks.

## Two harmless repairs to the source statement

1. **Zero determinant marginal.** The displayed source writes `1/alpha_i` without explicitly excluding `alpha_i=0`. Repair: discard every row with `alpha_i=0` before Hölder. Such a row belongs to no positive-weight determinant subset and its characteristic factor has modulus at most one. No constant changes.
2. **Zero-hub convention.** For the `(k,ell)=(0,3)` and `(0,2)` diffuse branches, explicitly set the zero-dimensional projection cap `M_H=1` (the source already sets the empty singular-value product `S=1`). Again no constant changes.

These are statement/notation repairs, not mathematical gaps.

## Marginal-free third-volume density receiver

For a literal cross block `M`, put `E_3(M)=e_3(MM^T)`. Starting from the determinant-squared row marginals:

- if all third-volume row marginals are at most `1/2`, use `(k,ell,d)=(0,3,3)`;
- if a row `w` is heavier than half, Gram–Schmidt gives the exact identity
  \[
  \|w\|^2 e_2(CC^T)>E_3(M)/2;
  \]
  use `(1,2,3)` if the residual order-two marginals are diffuse;
- if a second row is heavy, the promoted two-row Gram determinant times residual one-volume exceeds `E_3(M)/4`; use `(2,1,3)` if diffuse;
- a third heavy row gives a literal three-row Gram determinant `>E_3(M)/8`, closed by the exact physical rank-three endpoint.

The largest branch constant is the diffuse one,

\[
C_3=3\sqrt2\,e(9/2)^{1/6}=14.818337662843\ldots,
\]

so, with arbitrary same-bank and affine phases retained,

\[
\boxed{\|p_Q\|_\infty\le C_3E_3(M)^{-1/6}}.
\]

## Marginal-free second-volume full half-potential receiver

The identical promotion tree one dimension lower gives

\[
\boxed{\sup_a\mathbb E|Q-a|^{-1/2}\le C_2E_2(M)^{-1/8}},
\qquad
C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots .
\]

This is deliberately a full half-potential theorem, not a rank-two density theorem.

## Complete normalized `s_9` proof

Use the baseline `eta=1/100`, `kappa=1/80^2`.

### No pivot

Baseline `prop:volume` at `k=3` gives `V_3(A)>=kappa^3`. A fair literal coordinate cut gives

\[
E_3(M)\ge4^{-3}\kappa^3,
\qquad E_3(M)^{-1/6}\le160.
\]

Hence

\[
\|p_Q\|_\infty\le160C_3=2370.93402605488\ldots .
\]

### Scalar pivot

For `|A_hh|>=eta`, the Schur complement retains at least eight unit spectral directions.

If that Schur complement has a pivot, reusing the exact baseline pivot-half-potential branches gives

\[
H(S)\le10(20+12\log16)=532.71064666877\ldots,
\]

and therefore the full half potential is at most

\[
1+10(20+12\log16)=533.71064666877\ldots .
\]

If the Schur complement has no pivot, it has at least five unit spectral directions. Baseline `prop:volume` at `k=2`, the fair cut, and the new `E_2` receiver give

\[
\sup_a\mathbb E|S-a|^{-1/2}
\le C_2\sqrt{160}=152.99191115498\ldots .
\]

Thus the scalar-square profile gives the worst scalar branch

\[
\|p_Q\|_\infty
\le10\,[1+10(20+12\log16)]
=5337.10646668774\ldots<5338.
\]

### Pair pivots

A definite pair gives

\[
\|p_Q\|_\infty\le10\pi<32.
\]

An indefinite pair leaves at least seven unit spectral directions, in particular operator norm at least one. The baseline hyperbolic envelope and quarter-power logarithmic potential give a uniform bound below `251`.

All branches are exhaustive, so for `K=s=1`, `||p_Q||_infinity<5338`.

### Scaling

With `Y=KX` and

\[
\widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
\qquad Q=(s/K^2)\widetilde Q,
\]

we have `s_9(A/s)>=1` and hence

\[
\boxed{\|p_Q\|_\infty<5338K^2/s}.
\]

This preserves every theorem quantifier.

## Fleet02 counterexample stress at the eight-eigenvalue frontier

The source's paired-coordinate obstruction is valid and useful. If `X,X'` are independent with a cap-one density `f`, the symmetrized variables

\[
U=X-X',\qquad V=X+X'
\]

have joint density

\[
G(u,v)=\tfrac12 f((v+u)/2)f((v-u)/2).
\]

For the uniform law `f=1_{[-1/2,1/2]}`, `G=1/2` on the diamond `|u|+|v|<=1`. The normalized conditional density of `V|U=u` is

\[
\frac1{2(1-|u|)},
\]

which diverges as `|u|->1`. Therefore a future overlap-one/multiplicity-eight proof **cannot** condition on `U=u`, renormalize the paired slice, and then reuse cap-one product estimates. This is a concrete counterexample to that proof interface, not to the multiplicity-eight theorem.

The source also proves the safe integrated paired half-potential estimate

\[
\sup_a\iint G(u,v)|\gamma uv-a|^{-1/2}\,du\,dv
\le(33+4\log16)|\gamma|^{-1/2}<45|\gamma|^{-1/2}.
\]

A second obstruction remains: uniform fiberwise half-potential control by itself does not combine with an outer scalar square when the fiber critical shift depends on the shared coordinate. Thus the first honest `s_8` obligation is a dependence-safe receiver for the same-index overlap mass, not a conditional-cap shortcut.

## Threshold accounting

- Baseline 17-eigenvalue theorem: independently audited PASS in this run.
- Complete source-backed replacement at 9 eigenvalues: **PASS after the two no-cost statement repairs above**; explicit constant `<5338 K^2/s`.
- Multiplicity 8: **OPEN** in this proof architecture; valid overlap/paired-source currency exists but the dependence-safe `L^infinity` receiver is missing.
- Multiplicity 3 unrestricted conjecture: **OPEN**.

No baseline source was modified by this artifact. This is a guarded improvement for review, not a self-awarded independent-validation certificate.
