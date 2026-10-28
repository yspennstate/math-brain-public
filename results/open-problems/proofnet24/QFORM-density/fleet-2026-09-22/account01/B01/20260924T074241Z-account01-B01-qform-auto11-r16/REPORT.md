SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-24T07:42:41.853726Z.
attacking: repair the localized three-original-coordinate branch by proving a uniform 3x3 principal-block theorem with no pointwise scalar oscillatory-decay premise.

# account01/B01 — corrected localized three-coordinate theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T074241Z-account01-B01-qform-auto11-r16`  
Role: Oscillatory replacement  
Status: **NEW TARGET-LEVEL LOCALIZED THEOREM / FULL QFORM OPEN / INDEPENDENT REVIEW PENDING**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction boundary

All random coordinates are ORIGINAL independent coordinates with probability densities bounded by one. No Gaussian, iid, moment, compact-support, connected-support, log-concavity, or post-rotation independence assumption is used. The full owner target remains OPEN, and continuity is not asserted for arbitrary merely measurable input densities.

The phase-aligned fragmented-support obstruction remains binding. For every prescribed nonzero frequency `s` one can choose a finite union `E` of intervals of total measure one inside `{x: dist(sx^2,2pi Z)<=eta}` and take `f=1_E`; then `Re E exp(isX^2)>=cos eta`. Hence no law-uniform positive pointwise power decay for a scalar quadratic phase is used anywhere below.


The point of this run is to repair, with a product-preserving proof, the attractive but previously unsafe “localized 3x3 block” route. The older arbitrary-joint rank-three coarea lemma is false. The theorem below conditions only on OUTSIDE original coordinates and then proves the remaining three-coordinate statement directly from two source-valid fractional/physical-pair estimates.

## 2. Source-pinned inputs actually used

### 2.1 Orientation-free rank-two affine half-Riesz

Source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an invertible symmetric `2x2` matrix `Lambda`, two original cap-one coordinates, and an arbitrary affine term, the source gives

`H_(1/2)(Z^T Lambda Z + ell^T Z + c)
 <=128 |det Lambda|^(-1/4)`.

When the affine term lies in the quadratic range, including the full-rank literal two-coordinate case used here, the sharper constant is

`H_(1/2) <=16 sqrt(30) |det Lambda|^(-1/4)`.                    (2.1)

### 2.2 Logarithmic indefinite physical-pair theorem

Source:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite ORIGINAL-coordinate pair `P`, put

`D=|det P|`, `kappa=sigma_min(P)`.

After completing that pair, with critical remainder `R`, for every `r>0`,

`p_Q(t)
 <= 2 sqrt(2)/r
    + D^(-1/2) E log_+(2r^2/(kappa |t-R|)).`                   (2.2)

The pair shifts may depend arbitrarily on the remaining original coordinates. This is the averaged/distribution-function mechanism used in the small-diagonal branch.

### 2.3 Designated partner account02/B01 actually applied

Newest completed designated-partner theorem consumed in this run:

`yspennstate/math-open-problems@fb7b0f71ead32ea608ff9ec45370edc246f7239e`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T063552Z-account02-B01-qform-auto11-r46/REPORT.md`, theorem `QFORM-RANK1-TWOHUB-ARROWHEAD-HALFRIESZ-v1`.

An equation-level application appears in Section 7.

## 3. Two elementary interfaces

### 3.1 Literal scalar-square peel

Suppose one original coordinate occurs as

`Q=a(X+h(Y))^2+R(Y)`, `a!=0`,                                  (3.1)

where `X` is independent of `Y` and has density at most one. Conditional on `Y`, the density of `a(X+h)^2` is bounded by

`|a|^(-1/2)|u|^(-1/2)`                                         (3.2)

on its sign-compatible half-line. Therefore

`boxed: ||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R).`            (3.3)

This is a direct distribution-function kernel and uses no characteristic-function pointwise decay.

### 3.2 Literal one-variable quadratic concentration

If `Z` is an original cap-one coordinate and

`R=s(Z+u)^2+v`, `s!=0`,                                        (3.4)

then for every center `t` and radius `rho>0`, the inverse image of `(t-rho,t+rho)` has total Lebesgue length at most

`2 sqrt(2rho/|s|)`.

Hence

`boxed:
 P(|R-t|<rho) <= H sqrt(rho),
 H=2 sqrt(2)|s|^(-1/2).`                                       (3.5)

Layer cake then gives, for every `A_0>0`,

`E log_+(A_0/|t-R|)
 = integral_0^infinity P(|t-R|<A_0 e^(-u)) du
 <=2 H A_0^(1/2).`                                             (3.6)

## 4. A new exact three-coordinate theorem

### Theorem 4.1 — `QFORM-LITERAL-3X3-UNIVERSAL-LINF-v1`

Let `X=(X_1,X_2,X_3)` be independent cap-one coordinates and let

`q(X)=X^T B X + ell^T X + c_0`,                                (4.1)

where `B` is real symmetric and

`sigma_min(B)>=1`.                                              (4.2)

Then `q(X)` has an essentially bounded density satisfying

`boxed: ||p_q||_infinity <101.`                                (4.3)

The estimate is uniform in the affine vector `ell` and constant `c_0`. No signature assumption is imposed.

### Proof

Fix the rational threshold

`tau=23/40=0.575`.                                              (4.4)

Because (4.2) holds,

`|det B|>=1`                                                    (4.5)

and, for every coordinate basis vector,

`||B e_i||_2>=1`.                                               (4.6)

We split into two exhaustive ORIGINAL-coordinate cases.

### Case A: a visible literal diagonal

Suppose `|B_ii|>=tau` for some `i`. Put `a=B_ii`. Completing the literal coordinate `X_i` gives

`q=a(X_i+h(Z))^2 + R(Z)`,                                      (4.7)

where `Z` is the other two original coordinates and the quadratic matrix of `R` is the exact `2x2` Schur complement

`S=B_(hat i,hat i)-B_(hat i,i)B_(i,hat i)/a`.                   (4.8)

The affine term of `R` is arbitrary, but in two physical coordinates it lies in the full range of the invertible matrix `S`. Since

`det B=a det S`,                                                (4.9)

(4.5) implies `S` is invertible. Apply (2.1) and then the scalar peel (3.3):

`||p_q||_infinity
 <=16 sqrt(30)|a|^(-1/2)|det S|^(-1/4)
 =16 sqrt(30)|a|^(-1/4)|det B|^(-1/4)
 <=16 sqrt(30) tau^(-1/4)
 =100.63838269447342... <101.`                                  (4.10)

### Case B: every literal diagonal is small

Assume

`max_i |B_ii|<tau`.                                             (4.11)

Choose any row `i`. By (4.6), the two off-diagonal entries in that row satisfy

`sum_(j!=i) B_ij^2 >1-tau^2`.

Hence one physical edge `m=B_ij` obeys

`|m|>=b_0:=sqrt((1-tau^2)/2)=sqrt(1071/3200)
 =0.5785218232703068...`.                                      (4.12)

Let

`P=[[B_ii,m],[m,B_jj]]`.                                       (4.13)

Since `b_0>tau`, `P` is automatically invertible and indefinite:

`det P=B_ii B_jj-m^2<0`.                                       (4.14)

Moreover, comparing `P` to `[[0,m],[m,0]]` gives by Weyl

`kappa:=sigma_min(P)
 >=|m|-max(|B_ii|,|B_jj|)
 >=kappa_0:=b_0-tau
 =0.003521823270306812...`.                                    (4.15)

Complete this physical pair. Because there is exactly one original coordinate left, the critical remainder has the scalar form (3.4), with quadratic coefficient equal to the one-dimensional Schur complement `s`. Determinants give the exact identity

`det B=(det P) s`.                                              (4.16)

Put `D=|det P|`. The physical-pair theorem (2.2), followed by (3.6) with

`A_0=2r^2/kappa`,                                               (4.17)

gives

`p_q(t)
 <=2sqrt(2)r^(-1)
   +2sqrt(2) H D^(-1/2) kappa^(-1/2) r`,                       (4.18)

where `H=2sqrt(2)|s|^(-1/2)`. Optimizing in `r>0` yields

`p_q(t)
 <=4 sqrt(2H) D^(-1/4) kappa^(-1/4)
 =2^(13/4) D^(-1/4) kappa^(-1/4)|s|^(-1/4).`                  (4.19)

Now use the exact determinant compensation (4.16):

`D^(-1/4)|s|^(-1/4)=|det B|^(-1/4)<=1`.                        (4.20)

Therefore

`||p_q||_infinity
 <=2^(13/4) kappa_0^(-1/4)
 =39.05310744041935... <101.`                                  (4.21)

Cases A and B are exhaustive, proving (4.3). QED.

### What replaced the false scalar oscillatory bound

The difficult small-diagonal branch never asks for pointwise decay of `E exp(itX^2)`. It completes an actual indefinite physical pair, retains the exact third scalar Schur curvature, uses the square-root **distribution function** (3.5), and averages the pair's logarithmic singularity by layer cake. The dangerous physical-pair determinant cancels exactly against the scalar Schur coefficient through `det B=(det P)s` before any universal constant is taken.

## 5. Main localized consequence in arbitrary dimension

### Theorem 5.1 — `QFORM-LOCAL-3X3-PRINCIPAL-BLOCK-LINF-v1`

Let `X_1,...,X_n` be independent cap-one coordinates and let `A` be real symmetric. Suppose there is a set `I` of THREE ORIGINAL coordinates such that the physical principal block

`B=A[I,I]`                                                       (5.1)

satisfies

`sigma_min(B)>=c>0`.                                            (5.2)

Then the FULL ambient quadratic form

`Q=X^T A X`                                                     (5.3)

has an essentially bounded density with

`boxed: ||p_Q||_infinity <101/c.`                              (5.4)

All outside coefficients and cross couplings are arbitrary. Continuity is not asserted.

### Proof

Condition on every original coordinate outside `I`. The three coordinates in `I` remain independent with their original cap-one densities, and the conditional polynomial is

`q_y(x)=x^T Bx + ell_y^T x + r_y`.                              (5.5)

The affine vector and constant depend arbitrarily on the conditioned variables, but Theorem 4.1 is uniform in both. Scaling `B` and the whole conditional polynomial by `c` reduces (5.2) to unit scale, so every conditional density is bounded by `101/c`. Averaging the conditional densities over the outside variables gives (5.4). QED.

This is a corrected product-preserving proof of the localized three-coordinate route. It does **not** assert that the bare global hypothesis `s_3(A)>=1` forces such a uniformly conditioned physical triple; diffuse examples show that it need not.

## 6. Strict target stress and exact constants

Take

`B_*=[[0,1,1],[1,0,1],[1,1,0]]`.                              (6.1)

Its eigenvalues are

`{-1,-1,2}`,                                                    (6.2)

so it is an exact three-coordinate owner target with all physical diagonals zero. Thus Case A is unavailable. Choose any physical pair. Then

`D=1`, `kappa=1`, `|det B_*|=2`,                               (6.3)

and (4.19) sharpens to

`||p_(X^T B_* X)||_infinity
 <=2^(13/4) 2^(-1/4)=8`.                                       (6.4)

This is a useful control because it lies exactly in the zero-diagonal branch where a scalar-pivot-first proof cannot even start.

A different algebraic stress is

`B_0=[[1,1,1],[1,1,-1],[1,-1,1]]`,                             (6.5)

with spectrum `{-1,2,2}` while **every physical 2x2 principal determinant is zero**. Theorem 4.1 still applies through Case A. Thus neither a nonzero scalar pivot nor a uniformly invertible physical pair is individually required in every orientation; the two mechanisms genuinely complement each other.

## 7. Required designated-partner application at an actual inequality

Apply the completed account02/B01 theorem from Section 2.3 to the strict four-coordinate target

`Q_partner
 =X_0^2 +2H[(sqrt(3)/2)Y_1 +(1/2)Y_2]`.                        (7.1)

The coefficient matrix has spectrum

`{-1,0,1,1}`                                                    (7.2)

because the hub-to-leaf slope vector has norm one. In the partner notation,

`s=||w||_2||c||_2=1`,
`|c_h|=sqrt(3)/2`, `T=1/2`,
`theta=|c_h|T/||c||_2^2=sqrt(3)/4`.                            (7.3)

The heavy-leaf-plus-nonzero-tail inequality (5.9) in that report therefore gives the concrete full-target estimate

`boxed:
 ||p_(Q_partner)||_infinity
 <=2^(23/8) (sqrt(3)/4)^(-1/4)
 =9.043490329708042... .`                                      (7.4)

This is an equation-level application of the designated partner result, not merely a comparison citation.

## 8. Remaining implication

The theorem closes the entire branch in which some three ORIGINAL coordinates carry a uniformly invertible physical principal block. It also gives a fully rigorous replacement for the earlier localized argument that depended on the false arbitrary-joint coarea interface.

The first unpaid implication for B01 remains genuinely global/diffuse:

`QFORM-DIFFUSE-NO-LOCAL3-AGGREGATE-CURRENCY-v1`:

> Under only `s_3(A)>=1`, when every physical `3x3` principal block has tiny smallest singular value, force a target-scale aggregate original-coordinate currency (disjoint-tetrad/overlap-minor, grouped star, exact rank-two cross volume, ridge leverage, or another averaged-frequency certificate) before any tiny local minor is inverted.

The previous B01 disjoint-tetrad aggregation theorem is designed for exactly this complementary regime. The full conjecture is still OPEN and no full-target continuity claim is made.

## 9. Audit status

- Full target: **OPEN**.
- New localized theorem: **proved here, pending independent mathematical review**.
- Input quantifiers: arbitrary independent densities `<=1`; no extra support/moment/smoothness assumptions.
- Signs: all signatures included.
- Degenerate cases: Theorem 5.1 assumes only `sigma_min(B)>=c`; within the proof zero diagonals and singular physical pairs are covered by the exhaustive Case A/Case B split.
- Continuity: **not claimed**.
- Pointwise scalar Fresnel decay: **not used**.
- Native brain ingestion: **not verified**; repository retrieval/write does not establish it.
