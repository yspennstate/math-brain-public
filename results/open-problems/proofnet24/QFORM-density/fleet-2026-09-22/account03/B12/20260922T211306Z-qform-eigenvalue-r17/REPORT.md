SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-22T21:13:06Z.
attacking: additional-eigenvalue control via a three-disjoint-bank arbitrary-completion theorem; aggregate diffuse bank coordinates before inversion, then absorb arbitrary outside quadratic spectrum with the account04/B12 mixed-norm shear compiler.

# QFORM B12: three-bank arbitrary-completion theorem

## Status

This run proves a new grouped-coordinate additional-eigenvalue theorem and applies the assigned partner account04/B12 result to the final inequality. It does not prove or disprove the full QFORM conjecture. The result proves existence of an essentially bounded density in its stated scope; continuity is not established.

Control source at startup: `yspennstate/math-research-brain@145b8b967df6fa2c35473c8d3377cce44095999d`, OWNER CONTROL revision `2026-09-22.15`, programme revision `2026-09-22.5`. Pre-publication refresh: control README blob `fca13a89d221115332ce5e60d49554ee0e213efa`, live correction inbox blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`. Full QFORM remains OPEN.

## Source-valid dependencies actually read

1. Assigned partner account04/B12, `QFORM mixed-norm shear compiler`, complete proof:
   `yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260922T192552Z-account04-B12-mixed-shear-r1/REPORT.md`.
   If `(U,Z)` has joint density `h` and
   `M(h)=int esssup_u h(u,z) dz`, then for every measurable `psi`,
   `||p_(U+psi(Z))||_infinity <= M(h)`. No independence between `U` and `Z` is required.

2. B12 previous theorem `QFORM-ARBITRARY-COMPLETION-SCHUR-SHEAR-v1`, complete proof:
   `yspennstate/math-open-problems@b0886a84716141e3757395ba49a657c6acdaa5fa`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T201552Z-qform-eigenvalue-r16/REPORT.md`.
   For independent cap-one coordinates and a physical 3x3 principal block `M` with pivot `a!=0`,
   `||p||_infinity <=128 |a det M|^(-1/4)`, uniformly over affine terms and arbitrary outside completion.

3. Full-matrix indefinite-pair theorem, complete supporting proof:
   `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.
   If `s_3(A)>=s>0` and an original-coordinate 2x2 principal pair `B` is indefinite with `D=|det B|` and `kappa=sigma_min(B)`, then, uniformly over affine terms,
   `||p||_infinity <=3*400^(1/3) (D^2 kappa s)^(-1/6)`.

4. Projection density input recorded in account02/B18 from Rudelson--Vershynin: if independent cap-one variables are combined as `L=sum u_i X_i`, `sum u_i^2=1`, then `||p_L||_infinity<=sqrt(2)`.

5. For the sharpened stress-family corollary only, account01/B16 `QFORM-TRANSLATED-BANK-FROSTMAN-SMOOTHER-v1`, complete proof at
   `yspennstate/math-open-problems@1b7a876f7577cf99599322926154ce0032a034fd`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/account01-B16-20260922T161036Z-r11/REPORT.md`.

All uses below remain in original-coordinate product blocks. No spectral rotation is declared independent.

## Lemma 1: a uniform three-variable affine cap after bank aggregation

Let `Y_1,Y_2,Y_3` be independent real random variables with densities bounded by `sqrt(2)`. Let `M` be real symmetric 3x3 with

` s_min(M) >= s > 0 `.

For every affine vector `ell` and constant `c`, the random variable

`R=Y^T M Y+ell^T Y+c`

has an essentially bounded density satisfying

`boxed(||p_R||_infinity < 300/s).`                                      (1.1)

### Proof

Divide the output by `s`; it is enough to prove the statement for `s=1`, because density rescales by `1/s`. Put

`V=sqrt(2) Y`.

The three coordinates of `V` are independent and have densities bounded by one. In `V` variables the quadratic matrix is

`H=M/2`,

and `s_3(H)>=1/2`. We split according to the diagonal of `M` at the fixed threshold

`delta=9/16`.

### Case A: a diagonal entry is at least delta

Suppose `|M_ii|>=delta`. Since all singular values of `M` are at least one,

`|det M|>=1`.

For `H=M/2`, the corresponding pivot is `a=M_ii/2` and

`det H=(det M)/8`.

Apply `QFORM-ARBITRARY-COMPLETION-SCHUR-SHEAR-v1` to the three cap-one variables `V`, retaining the arbitrary affine term. It gives

`||p_R||_infinity`
` <=128 |(M_ii/2)(det M/8)|^(-1/4)`
` =256 |M_ii det M|^(-1/4)`
` <=256 delta^(-1/4)`
` =512/sqrt(3)`
` <300`.                                                          (1.2)

### Case B: every diagonal entry is smaller than delta

Assume `|M_ii|<delta` for `i=1,2,3`. Since `sum lambda_i(M)^2=||M||_F^2>=3`,

`2 sum_(i<j) M_ij^2`
` =||M||_F^2-sum_i M_ii^2`
` >3-3 delta^2`.

Hence some off-diagonal entry `b=M_ij` satisfies

`b^2 >(1-delta^2)/2 =175/512`.                                  (1.3)

For the corresponding physical pair

`B=[[a,b],[b,c]]`,

we have `|a|,|c|<9/16`. Therefore

`D:=|det B|=b^2-ac >=b^2-|ac| >175/512-81/256=13/512>1/40`.       (1.4)

In particular the pair is indefinite. Also, viewing `B` as `[[0,b],[b,0]]+diag(a,c)`, Weyl's singular-value inequality gives

`kappa:=s_min(B) >= |b|-max(|a|,|c|)`
` >sqrt(350)/32-18/32`
` =(sqrt(350)-18)/32`
` >1/50`,                                                         (1.5)

because `(466/25)^2=347.4496<350`.

In the cap-one variables `V`, the pair is `B/2`; hence its determinant magnitude is `D/4`, its minimum singular value is `kappa/2`, and the full 3x3 matrix has `s_3>=1/2`. The full-matrix indefinite-pair theorem yields

`||p_R||_infinity`
` <=3*400^(1/3) [ (D/4)^2 (kappa/2) (1/2) ]^(-1/6)`
` =6*400^(1/3) (D^2 kappa)^(-1/6)`
` <6*400^(1/3)*80000^(1/6)`
` <300`.                                                          (1.6)

The last inequality is exact after taking sixth powers:

`6^6 *400^2 *80000 =597196800000000 <729000000000000=300^6`.

This proves (1.1). QED.

## Theorem 2: QFORM-THREE-DISJOINT-BANK-ARBITRARY-COMPLETION-v1

Partition a subset of the ORIGINAL coordinates into three pairwise disjoint nonempty banks `T_1,T_2,T_3`, with all remaining original coordinates denoted by `Z`. For each bank choose a deterministic vector `u_j` supported on `T_j` with `||u_j||_2=1`, and define

`Y_j=u_j^T X_(T_j)`.

Assume the full quadratic form can be written

`Q = Y^T M Y + 2 Y^T C Z + psi(Z)`,                              (2.1)

where

- `M` is arbitrary real symmetric 3x3 with `s_min(M)>=s>0`;
- `C` is arbitrary, with no size or sign restriction;
- `psi` is an arbitrary measurable function of the remaining ORIGINAL coordinates `Z`.

In particular `psi(Z)=Z^T D Z` is allowed for every symmetric `D`, so the outside block may carry arbitrarily many additional eigenvalues of arbitrary signs and magnitudes, while `C` supplies arbitrary couplings through the three bank statistics.

Then

`boxed(||p_Q||_infinity <300/s).`                                (2.2)

### Proof

The banks are disjoint original-coordinate sets, so `Y_1,Y_2,Y_3,Z` are mutually independent at the block level. Rudelson--Vershynin gives

`||p_(Y_j)||_infinity <=sqrt(2)`                                  (2.3)

for every `j`, uniformly in bank size and coefficient spread.

Fix `Z=z`. Then the non-remainder part

`U_z=Y^T M Y+2Y^T C z`

is exactly the affine three-variable polynomial covered by Lemma 1, so

`||p_(U_z)||_infinity <300/s`                                     (2.4)

uniformly in `z` and in the arbitrary coupling matrix `C`.

Let `g(z)` be the product density of the outside original coordinates and define the joint density

`h(u,z)=g(z) p_(U_z)(u)`.

Then

`M(h)=int esssup_u h(u,z) dz`
`    <=(300/s) int g(z)dz`
`    =300/s`.                                                     (2.5)

Now apply the assigned partner account04/B12 mixed-norm shear theorem with the actual measurable remainder `psi(z)`. It gives

`||p_(U+psi(Z))||_infinity <=M(h)<300/s`,                         (2.6)

which is exactly (2.2). No independence between the final core value `U` and the added remainder `psi(Z)` is used. QED.

## Matrix interpretation and why this is additional-eigenvalue control

Let `U` denote the physical embedding of the three disjoint unit bank vectors. The theorem applies to every matrix whose quadratic form has the block representation

`A = [[U M U^T, U C], [C^T U^T, D]]`

relative to bank physical coordinates versus the remaining original coordinates, with arbitrary symmetric `D` and arbitrary `C`. There is no bound on the rank, norm, sign pattern or eigenvalue multiplicities of `D`, and the global spectrum can change drastically when `C,D` vary. The price stays `300/s`; all extra spectrum outside the protected three-bank compression costs zero.

This is strictly more flexible than selecting one physical coordinate from each diffuse bank. A bank may have arbitrarily many coordinates with all coefficients of order `m^(-1/2)`; its one-dimensional projection density remains capped before any reciprocal physical minor is paid.

## Corollary 3: the singleton-plus-two-banks obstruction survives arbitrary completion

Take

`Y_1=X_0`,
`Y_2=m^(-1/2) sum_(j=1)^m X_j`,
`Y_3=m^(-1/2) sum_(j=m+1)^(2m) X_j`,

and `M=diag(1,1,-1)`. For arbitrary outside original-coordinate vector `Z`, arbitrary `C`, and arbitrary symmetric `D`,

`Q=Y_1^2+Y_2^2-Y_3^2+2Y^T C Z+Z^T D Z`                       (3.1)

has a density bounded by `300`, uniformly in `m,C,D` and the cap-one input laws.

Using the sharper account01/B16 translated-bank Frostman theorem inside each fixed `z` fiber, pair `Y_2,Y_3` as the indefinite base and complete the square in `Y_1`. Since every bank density cap is at most `sqrt(2)`, its bound is

`C_ind * sqrt(2)*sqrt(sqrt(2)*sqrt(2)) =2 C_ind`,

where

`C_ind=8*3^(3/4)*5^(1/4)/sqrt(e)=16.53964516612327...`.

Thus the same partner shear step yields the sharper arbitrary-completion estimate

`boxed(||p_Q||_infinity <=2 C_ind =33.07929033224653... )`.       (3.2)

This strengthens the earlier disjoint-bank result, which allowed only an independent fourth-block remainder: arbitrary outside quadratic spectrum and arbitrary through-bank cross coupling are now retained.

## Exact remaining implication

The full conjecture remains open because an arbitrary matrix with `s_3(A)>=1` need not admit the structural factorization (2.1) with three disjoint physical banks and `s_min(M)` bounded below. The genuinely unpaid step is now an overlapping-frame/group-extraction statement:

> Starting from only three global singular values at least one, either produce a dimension-free protected physical core/pair/ridge certificate already covered by existing theorems, or extract three disjoint original-coordinate banks whose entire interaction with the rest factors through one scalar statistic per bank with a uniformly conditioned 3x3 bank matrix; otherwise control the overlap error without paying reciprocal one-coordinate minors.

The singleton-plus-two-banks obstruction no longer blocks the grouped branch itself; it is covered even after arbitrary outside completion. Hadamard/overlapping frames remain the structural stress case. A bare good-minor selection, worst conditional fiber, arbitrary-joint coarea estimate, or post-rotation independence claim is not used.

## Continuity and integrity

The theorem establishes an essentially bounded density only. The account04/B12 partner gives a sufficient mixed translation-modulus criterion for uniform continuity, but no dimension-free modulus is proved here under the bare cap-one hypotheses, so continuity remains open in this scope.

No Gaussianity, log-concavity, moments, compact support, connected support, pointwise van-der-Corput decay, fiber supremum shortcut, arbitrary-joint coarea bound, or spectral-coordinate independence is used. Repository transport occurred; authenticated native receiver-context brain retrieval did not: `WITHOUT_VERIFIED_BRAIN`.
