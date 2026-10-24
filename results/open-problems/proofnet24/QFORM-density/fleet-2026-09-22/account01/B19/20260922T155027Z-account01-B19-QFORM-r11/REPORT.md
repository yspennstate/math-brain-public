# account01/B19 — cross-bank square-root-log splice closes the one-effective contaminated branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T155027Z-account01-B19-QFORM-r11`  
**Assignment:** Universal proof assembly  
**Outcome:** `ESSENTIAL_STEP_APPLIED / ONE-EFFECTIVE-CONTAMINATION-BRANCH-CLOSED / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction discipline

The target is the unrestricted one: for every dimension, every independent real coordinate family with one-dimensional densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a single universal finite essential-supremum bound for the density of `Q=X^T A X`. Continuity is tracked separately.

The live correction inbox was reread before publication. No law-uniform pointwise Fresnel decay, no post-rotation independence, no conditional density cap for a rotated aggregate, no fixed-good-triple assertion, no rank-three cross-cut dichotomy, and no fiber-supremum closure is used.

The assigned partner result actually used is account02/B19 run `20260922T151209Z-account02-B19-qform-r15`, canonical `yspennstate/math-open-problems@333ffdfd83679ff020bfb45c27257e651cde5130`, report blob `5e4928506aa238452599129b712318349b3626c3`. It pays the uncontaminated aggregate core and isolates the exact remaining normal form

`A = diag(a,-b,D_T) + lambda v v^T + R`,

with

`a,b>=7/8`, `|lambda|>=41/56`, `||v_T||^2>=27/41`, `max |(D_T)_{kk}|<1/7`, `||R||op<=1/8`, and `v_p^2,v_q^2<=7/41`,

leaving same-bank contamination as its first unpaid implication.

I also use account03/B19 run `20260922T154500Z-account03-B19-QFORM-r13`, canonical `yspennstate/math-open-problems@0e6d1715955458010d43193cab3dafc293c0e28c`. It proves the exact physical-pivot quarter-kernel and, in the above one-effective branch, forces either a physical Schur diagonal or an original-coordinate Schur cross cut with singular value `>27/2240`.

## 2. A product-preserving cross-bank concentration lemma

Let `I,J` be disjoint sets of original coordinates. Let `X=(X_i)_{i in I}` and `Y=(Y_j)_{j in J}` have mutually independent coordinates, each with density at most one. Let `C` be any real `|I| x |J|` matrix, put `sigma=s_1(C)>0`, and consider

`K(X,Y)=F(X)+2 X^T C Y+G(Y)`,

where `F,G` may be arbitrary measurable real functions for which the expression is defined. For the quadratic-form application, they are the two self-block quadratics plus affine terms.

### Lemma 2.1 — `QFORM-CROSSBANK-SQRTLOG-v1`

For every `t` and every

`0<r<=r_0:=sigma/(4e)`, one has

`P(|K-t|<=r)^2 <= (4 e r/sigma) [1+log(sigma/(4 e r))]`.          (2.1)

Equivalently,

`P(|K-t|<=r) <= sqrt((r/r_0)[1+log(r_0/r)]).`                    (2.2)

This holds for arbitrary signs and arbitrary self terms `F,G`.

### Proof

Let `X'` be an independent copy of `X`, independent also of `Y`, and write

`E={|K(X,Y)-t|<=r}`.

Conditioning first on `Y` and applying Cauchy--Schwarz,

`P(E)^2 <= E_Y P_X(E|Y)^2`
`          <= P(|K(X,Y)-K(X',Y)|<=2r).`                         (2.3)

The `G(Y)` term cancels exactly, and for fixed `X,X'` the difference is

`F(X)-F(X') + 2 (X-X')^T C Y`.                                  (2.4)

We need only the following standard cap for normalized original-coordinate linear forms: if `Z=sum_j u_jY_j`, `sum u_j^2=1`, then `||p_Z||_infinity<=sqrt(e)`. If `max |u_j|>1/sqrt(2)`, conditioning on all other coordinates gives the sharper bound `<=sqrt(2)`; if all squared coefficients are `<=1/2`, the completed rank-one Fourier--Brascamp--Lieb estimate gives `<=sqrt(e)`. Thus for a nonzero coefficient vector `q`, `q^T Y` has density cap `sqrt(e)/||q||_2`.

Applying this to (2.4), conditionally on `U=X-X'`, gives

`P(|K(X,Y)-K(X',Y)|<=2r | U,X,X')`
` <= min(1, 2 sqrt(e) r / ||C^T U||_2).`                         (2.5)

Let `u` be a left singular vector of `C` for `sigma`. Orthogonality of singular directions gives

`||C^T U||_2 >= sigma |u^T U|`.                                  (2.6)

Put `L=u^T(X-X')`. The normalized linear form `u^T X` has density at most `sqrt(e)`, so its difference with an independent copy also has density at most `sqrt(e)` by convolution. Therefore, with

`alpha=2 sqrt(e) r/sigma`,

(2.3)--(2.6) imply

`P(E)^2 <= E min(1,alpha/|L|).`                                  (2.7)

For any probability density `g<=K_0` and any radially decreasing kernel, the bathtub principle maximizes the integral by taking `g=K_0` on the centered interval of length `1/K_0`. Here `K_0=sqrt(e)`. If `alpha<=1/(2K_0)`, equivalently `r<=sigma/(4e)`, this gives exactly

`E min(1,alpha/|L|)`
` <= 2 K_0 alpha [1+log(1/(2K_0 alpha))]`
` = (4 e r/sigma)[1+log(sigma/(4 e r))].`                        (2.8)

This proves (2.1). QED.

The logarithm is harmless for the quarter-kernel below. Importantly, it is obtained from a single Cauchy--Schwarz symmetrization and an original-coordinate linear-form cap; no conditional independence after rotation appears.

## 3. Negative quarter moment from one cross singular direction

### Corollary 3.1 — `QFORM-ONE-CROSS-QUARTER-MOMENT-v1`

Under Lemma 2.1,

`sup_t E |K-t|^(-1/4) <= (2+sqrt(pi)) (4e/sigma)^(1/4).`          (3.1)

### Proof

For `D=|K-t|`, layer cake gives

`E D^(-1/4)=(1/4) integral_0^infinity r^(-5/4) P(D<r) dr`.       (3.2)

On `(0,r_0]`, use (2.2); on `[r_0,infinity)`, use the trivial bound one. With `r=r_0 e^{-u}`, the first part equals at most

`(1/4) r_0^(-1/4) integral_0^infinity e^{-u/4} sqrt(1+u) du`.

Since `sqrt(1+u)<=1+sqrt(u)`, the integral is at most

`4+4 sqrt(pi)`.

The tail contribution in (3.2) is exactly `r_0^(-1/4)`. Since `r_0=sigma/(4e)`, (3.1) follows. QED.

## 4. Application: the partner's same-bank contamination splice is paid

Take the one-effective branch isolated by account02/B19 r15. Account03/B19 r13 chooses the two heavy original coordinates as an indefinite physical pivot

`B=[[a,c],[c,-b]]`, `a,b>=m:=7/8`,

with

`Delta=ab+c^2>=m^2`,

and writes the exact outside Schur complement

`S=C_0-K_0^T B^{-1}K_0`, `kappa(Z)=Z^T S Z`.

Its conditional density estimate is

`p_Q(t) <= 2 Delta^(-1/4)m^(-1/4) E|t-kappa(Z)|^(-1/4).`         (4.1)

The same source proves from the actual mixed compression `s_min>9/280` that either

1. some physical Schur diagonal satisfies `|S_ii|>=9/1120`, in which case the full branch already has `||p_Q||_infinity<25`; or
2. there is a bipartition of the original outside coordinates `T=I disjoint_union J` such that

`s_1(S[I,J]) > sigma_0:=27/2240`.                               (4.2)

In case 2, decompose the exact critical value as

`kappa(X_I,X_J)=F(X_I)+2 X_I^T S[I,J] X_J+G(X_J)`.              (4.3)

All coordinates in the two banks remain original and independent. Corollary 3.1 applies directly to (4.3), with no restriction on the same-bank diagonal part, on the remainder `R`, on the signs of those terms, or on additional outside couplings already absorbed into the exact Schur complement. Hence

`sup_t E|t-kappa|^(-1/4)`
` <= (2+sqrt(pi))(4e/sigma_0)^(1/4).`                           (4.4)

Insert (4.4) into (4.1). Since `Delta>=m^2`,

`||p_Q||_infinity`
` <= 2(2+sqrt(pi)) [4e/(m^3 sigma_0)]^(1/4)`
` <45.705 <46. `                                                (4.5)

Thus:

### Theorem 4.1 — `QFORM-ONE-EFFECTIVE-CONTAMINATION-CLOSED-v1`

Every matrix in the exact contaminated one-effective normal form of account02/B19 r15 has, for every admissible independent cap-one input law, an essentially bounded output density with

`||p_{X^TAX}||_infinity <46.`

The result includes both signs of `lambda`, arbitrary tail signs, arbitrary `D_T`, arbitrary `R` satisfying the partner bounds, and all degeneracies outside the forced indefinite physical pivot. It does not require the ridge certificate and does not compile or condition on the diffuse aggregate. The same tail variables may generate both the aggregate direction and every contaminating term.

This directly pays the partner's open `QFORM-SAME-BANK-CONTAMINATION-SPLICE-v1`.

## 5. Compact conditional end-to-end architecture after this run

The current source-pinned B19 reductions now give the following conditional proof skeleton.

- Near-diagonal and definite physical two-plane cases are paid.
- In the low-offdiagonal-rank route, if `s_2(H)<=1/8` for `H=A-diag(A)`, same-sign heavy diagonals and a third moderate physical diagonal are paid; the only former residue was the one-effective contaminated normal form.
- Theorem 4.1 pays that residue completely, without any extra ridge or separability hypothesis.
- Therefore the low-rank obstruction surviving this chain is the genuinely two-offdiagonal-resource case `s_2(H)>1/8` (inside the previously reduced high-offdiagonal/low-stable-rank region). The known corrections prohibit replacing this by a universal good fixed triple or a rank-three cross cut.
- Separately, the reviewed/supplied diffuse and ridge-certified branches pay the scopes for which their leverage hypotheses hold.

Consequently, a full proof would follow from one remaining structural transfer of the following type:

`QFORM-TWO-OFFDIAGONAL-RESOURCE-EXTRACTION-v1` — from the surviving `s_2(H)>1/8` regime, extract in original-coordinate product geometry either (i) a paid rank-two mixed packet plus scalar curvature, (ii) an indefinite physical pivot whose exact Schur critical value has one cross singular direction bounded below, or (iii) a ridge-certified cross bank, with one universal quantitative scale.

The first essential inequality in that transfer is not another analytic density estimate: the new Lemma 2.1 shows that **one** fixed Schur cross singular value already supplies the precise quarter-moment needed by an indefinite pivot. The remaining debt is structural/product-preserving extraction of such a pivot-plus-cross resource from `s_2(H)>1/8`, without invoking any live-refuted fixed-minor dichotomy.

## 6. Continuity and nonclaims

Theorem 4.1 proves absolute continuity with an `L^infinity` density through the conditional quarter-kernel mixture. It does **not** establish a continuous representative. Continuity remains separate; branches with genuine `L^1` characteristic-function proofs retain their existing continuity conclusions.

The full QFORM conjecture remains **OPEN / NOT PROVED**. No claim is made that `s_2(H)>1/8` has been closed, nor that the pending ridge-window extension is independently reviewed. The contribution of this run is the complete removal of the previously explicit same-bank contamination obstruction and the reduction of the analytic burden of a Schur cross bank to the single inequality (2.1).
