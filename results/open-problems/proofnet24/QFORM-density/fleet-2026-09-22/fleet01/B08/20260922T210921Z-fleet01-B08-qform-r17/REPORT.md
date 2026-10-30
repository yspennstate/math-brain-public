SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-22T21:09:21Z.
attacking: finite-rank spectral-window paving with arbitrary low-spectrum tail, plus a grouped-payment control in the leverage-heavy complement.

# fleet01/B08 — finite spectral-window floating paving with nonseparable tail

**Run:** `20260922T210921Z-fleet01-B08-qform-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** diffuse eigenvector case  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and conditional proof route

The target remains: for every dimension, every product law with independent real coordinate densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal finite bound on the density of `Q=X^T A X`, or give a valid counterexample. Continuity is tracked separately.

The useful conditional route is:

1. isolate a basis-invariant spectral window `P_eta=1_{|A|>=eta}`;
2. if that window has finite rank `m` and diffuse physical leverage, half-pave its frame by the finite-dimensional floating lemma rather than MSS;
3. use the resulting two-sided Gram lower bounds to create three large physical cross singular values;
4. absorb the arbitrary **nonseparable** low-spectrum tail by the one-scale ridge perturbation theorem;
5. apply the completed ridge Fourier inversion before any fiber supremum or post-rotation conditioning.

This run proves that route in a general finite-window form and obtains a clean rank-three-window corollary with leverage `1/7` at spectral cutoff `1/64`. The full conjecture remains open because no theorem forces an arbitrary target matrix into this finite-window diffuse branch.

## 2. Dependencies actually used

### 2.1 Finite-rank floating half-paving

Source: `yspennstate/math-open-problems@c37badc7438c808fa283f574d22a8cb4db87216e`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260922T144029Z-fleet01-B08-qform-r13/REPORT.md`.

If `U in R^{n x m}` has orthonormal columns, row leverage at most `epsilon`, and

`kappa_m=sqrt(m(m+1)/8)`,

then some physical cut `I|J` satisfies

`U_I^T U_I >= alpha I`, `U_J^T U_J >= alpha I`,

where

`alpha=1/2-kappa_m epsilon`.

The proof is by floating in `Sym_m`, leaving at most `m(m+1)/2` fractional atoms, followed by unbiased rounding and a Frobenius second-moment bound.

### 2.2 One-scale ridge theorem

Source: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, path
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For a physical cross block `B`, `gamma>0`,

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`, `theta_gamma=tr K_gamma`.

If for some `q in [1,2]`

`max_i (K_gamma)_ii <= q/2`, `theta_gamma>2q`,

then the full ambient quadratic form, with arbitrary same-side blocks and outside couplings retained, has a continuous `C_0` density with

`||p_Q||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta_gamma/(theta_gamma-2q)`.

The same source proves the perturbative row-ridge estimate: if `B=B0+F`, `||F||<=eta`, `S=range(B0)`, then

`(K_gamma)_ii <= [sqrt((P_S)_ii)+eta/gamma]^2`.

### 2.3 Current assigned partner result actually applied

Partner: **fleet02/B08**, `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1`, source
`yspennstate/math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T204103Z-1dd824/REPORT.md`.

For an exact-rank-two physical cross bank `C` and fixed incident row/column `j,r`, define

`Delta_jr(C)=sum_(k!=j,s!=r) det C[{j,k},{r,s}]^2`.

The partner proves

`||p_R||_3 <= 3^(2/3)2^(1/3) Delta_jr(C)^(-1/6)`

while retaining arbitrary same-side quadratic-affine terms, and with a genuine outer scalar square of coefficient `a!=0`,

`||p_Q||_infinity <= C_grp |a|^(-1/2) Delta_jr(C)^(-1/8)`,

`C_grp=(2^(4/3)+1)sqrt(3)2^(1/4)`.

Section 5 below applies this theorem to an explicit target-valid family.

## 3. New general theorem: finite spectral window plus arbitrary low tail

### Theorem 3.1 — `QFORM-FINITE-WINDOW-FLOATING-RIDGE-v1`

Let `A` be real symmetric with at least three eigenvalues of modulus at least one. Fix `eta>0` and let

`P_eta=1_{|A|>=eta}`

have finite rank `m`. Write

`A=A_H+E`, `A_H=U Lambda U^T`,

where the columns of `U` span `P_eta`. Put

`epsilon=max_i (P_eta)_ii`,
`kappa_m=sqrt(m(m+1)/8)`,
`alpha=1/2-kappa_m epsilon`,
`sigma=alpha-eta`.

Assume `sigma>0`. If there exist `c>0` and `q in [1,2]` such that

`[sqrt(epsilon/alpha)+eta/(c sigma)]^2 <= q/2`,                 (3.1)

and

`3/(1+c^2) > 2q`,                                               (3.2)

then for every independent real input with coordinate densities at most one, `Q=X^T A X` has a continuous `C_0` density and

`||p_Q||_infinity
 <= sqrt(e)/(sqrt(2q)c sigma)
    * [3/(1+c^2)]/[3/(1+c^2)-2q].`                              (3.3)

No moment, support, centering, sign, log-concavity, or post-rotation independence hypothesis is used. The tail `E` may have arbitrary rank and sign and is not required to be coordinate-separable.

### Proof

Because `||E||<eta`, the high-window eigenvalue matrix `Lambda` is invertible. It contains at least three singular values at least one.

Apply the floating half-paving lemma to `U`. For some original-coordinate cut `I|J`,

`M_I:=U_I^T U_I >= alpha I`, `M_J:=U_J^T U_J >= alpha I`.

Let

`B0=A_H[I,J]=U_I Lambda U_J^T`.

Write `U_I=W_I M_I^(1/2)` and `U_J=W_J M_J^(1/2)` with `W_I,W_J` column isometries. The nonzero singular values of `B0` are those of

`M_I^(1/2) Lambda M_J^(1/2)`.

Hence

`s_3(B0)>=alpha s_3(Lambda)>=alpha`.                            (3.4)

Moreover `range(B0)=range(U_I)` because `Lambda` and `M_J` are invertible. Thus the physical coordinate leverage of that range obeys

`(P_range(B0))_ii=u_i^T M_I^(-1)u_i<=epsilon/alpha`.            (3.5)

For the true cross block

`B=A[I,J]=B0+F`, `F=E[I,J]`,

we have `||F||<=eta`, and Weyl gives

`s_3(B)>=sigma=alpha-eta`.                                      (3.6)

Choose

`gamma=c sigma`.

The three singular values in (3.6) imply

`theta_gamma>=3/(1+c^2)`.                                      (3.7)

The perturbative ridge-leverage estimate and (3.5) give

`max_i(K_gamma)_ii
 <=[sqrt(epsilon/alpha)+eta/(c sigma)]^2
 <=q/2`.                                                        (3.8)

By (3.2), `theta_gamma>2q`; therefore the one-scale ridge theorem applies. Since `x/(x-2q)` is decreasing for `x>2q`, substituting the lower bound (3.7) gives (3.3). Its `L^1` characteristic-function envelope supplies the continuous `C_0` representative. QED.

## 4. Clean rank-three-window corollary: leverage `1/7`

### Corollary 4.1 — `QFORM-RANK3-WINDOW-FLOATING-1OVER7-v1`

Assume

`rank 1_{|A|>=1/64}=3`,

and

`max_i (1_{|A|>=1/64})_ii <=1/7`.

Since the target already gives three eigenvalues of modulus at least one, the three high-window eigenvalues are exactly the three large directions; all remaining spectral mass is an arbitrary full-rank tail of operator norm `<1/64`.

Then `Q=X^T A X` has a continuous `C_0` density and

`boxed( ||p_Q||_infinity <253. )`                               (4.1)

#### Exact verification

For `m=3`,

`kappa_3=sqrt(3/2)=sqrt(6)/2`.

With `epsilon=1/7`,

`alpha=1/2-sqrt(6)/14=(7-sqrt(6))/14`,

and with `eta=1/64`,

`sigma=alpha-eta=(217-32sqrt(6))/448`.

Take

`c=2/5`, `q=5/4`, `gamma=(2/5)sigma`.

The effective-dimension bound is exact:

`theta_gamma>=3/(1+4/25)=75/29>5/2=2q`,                        (4.2)

since `75/29-5/2=5/58`.

For the row-ridge condition,

`sqrt(epsilon/alpha)=sqrt((14+2sqrt(6))/43)`,

and

`eta/gamma=35/[2(217-32sqrt(6))]`.

Use the rational upper bound `sqrt(6)<49/20`. Then

`sqrt((14+2sqrt(6))/43)
 <sqrt((14+49/10)/43)
 =sqrt(189/430)
 <663/1000`,

where the last inequality follows after squaring from

`189000000 < 430*663^2 = 189014670`.

Likewise

`35/[2(217-32sqrt(6))]
 <35/[2(217-392/5)]
 =175/1386
 <127/1000`,

since `175000<176022`. Therefore

`[sqrt(epsilon/alpha)+eta/gamma]^2
 <(663/1000+127/1000)^2
 =(79/100)^2
 =6241/10000
 <5/8=q/2.`                                                     (4.3)

The direct value is `0.6228431508...`, so the strict margin is genuine.

Finally, from (3.3), the ratio at the lower effective dimension is

`(75/29)/(75/29-5/2)=30`.

Hence

`||p_Q||_infinity
 <=30 sqrt(e)/(sqrt(5/2) gamma)
 =33600 sqrt(2e/5)/(217-32sqrt(6))
 =252.7563779721... <253.`                                      (4.4)

This is a materially larger leverage allowance than the all-rank spectral-window theorem because the floating partition exploits the fact that the high window has only three dimensions. The low-spectrum tail remains completely nonseparable.

## 5. Assigned partner result applied to an actual complementary family

The finite-window theorem does not address leverage-heavy physical geometry. To apply the current fleet02/B08 grouped-payment theorem on a genuine target family, fix an integer `r>=1`, put `m=2r+1`, and define `U in R^{m x2}` by

`u_1=(1/sqrt(2),0)`,

for `1<=k<=r`,

`u_(1+k)=(1/(2sqrt(r)),  1/sqrt(2r))`,
`u_(1+r+k)=(1/(2sqrt(r)),-1/sqrt(2r))`.

Then `U^T U=I_2`. Let

`C=U U^T`,

so `C` has exact rank two and singular values `1,1`. Form the symmetric target matrix

`A_r = diag(1, [[0,C],[C,0]])`.

Its spectrum contains

`1,+1,+1,-1,-1`,

so it satisfies the full target spectral hypothesis.

For the physical row and column `j=r=1`, every two-by-two minor factorizes through the two-frame, and the Cauchy-Binet identity gives

`sum_(k!=1) det U[{1,k}]^2 = ||u_1||^2=1/2`.

Consequently

`Delta_11(C)=1/4`.                                              (5.1)

Apply fleet02/B08 `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1` together with its genuine outer-square endpoint, with scalar coefficient `a=1`. This yields, for **arbitrary independent cap-one coordinate laws**,

`||p_(X^T A_r X)||_infinity
 <= C_grp (1/4)^(-1/8)
 =(2^(4/3)+1)sqrt(6)
 =8.6218171196... <8.622.`                                      (5.2)

This is an actual target-level inequality from the named partner theorem. It spends the whole determinant bank and never chooses a single small minor. Continuity is not asserted from the partner source; (5.2) is an essential `L^infinity` bound.

## 6. What changed and what remains unpaid

### Proved this run

1. `QFORM-FINITE-WINDOW-FLOATING-RIDGE-v1`: a general finite-rank spectral-window theorem with an arbitrary nonseparable low-spectrum tail.
2. `QFORM-RANK3-WINDOW-FLOATING-1OVER7-v1`: at cutoff `1/64`, a rank-three spectral window with physical leverage at most `1/7` has a continuous density bounded by `253`.
3. A literal application of the current fleet02/B08 grouped determinant-bank theorem gives the target-valid family (5.2) with universal bound `<8.622`.

### First unpaid implication

`QFORM-RANK3-WINDOW-HEAVY-OR-HIGHER-WINDOW-CLOSURE-v1`:

Starting from the invariant window `P=1_{|A|>=1/64}`, close one of the two complementary branches:

- `rank(P)=3` but some physical leverage exceeds `1/7`; or
- `rank(P)>=4`, where extra high-window directions can be arbitrarily localized and the finite-rank floating constant grows with the window rank.

A successful reduction must turn that complementary geometry into a product-preserving paid object already available in the fleet: an indefinite physical pair, scalar-pivot/ridge certificate, grouped double-incident determinant bank, or global ridge cut. It may not use a largest-minor selection, a conditional projection-density cap, arbitrary-joint coarea, or post-rotation independence. The latest partner theorem shows that an **aggregate** exact-rank-two determinant bank is already payable once such a bank is structurally forced.

The full QFORM conjecture therefore remains **OPEN**.

## 7. Corrections respected

The proof does not use law-uniform pointwise van-der-Corput decay, naive fiber suprema, independence after spectral rotation, the false arbitrary-joint rank-three coarea inequality, the false positive conditional-projection-density moment, a universal fixed good minor, or the refuted scalar conditional-density-cap route. It uses only original-coordinate cuts and source-pinned ridge/finite-frame identities.
