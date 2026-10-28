SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B13, 2026-09-23T02:28:19Z.
attacking: a product-extremal anchored four-volume certificate that glues the new cross-three-volume L3 theorem to one genuine physical square without rotating the source.

# account01/B13 auto13 — anchored disjoint four-volume gives an L-infinity certificate

Status: **PROVED SUPPORTING TARGET-LEVEL CERTIFICATE / FULL QFORM OPEN / CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

## 1. Source pins and exact scope


Three proved inputs are used at their exact scopes.

1. **Designated partner account02/B13 exact bang-bang reduction.** `yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T115714Z-account02-B13-qform-480ba28b/REPORT.md`. For every fixed measurable slab kernel, the supremum over all independent cap-one mass-one densities equals the supremum over products of indicators `1_{E_j}`, `|E_j|=1`; the supremum is unchanged if the `E_j` are bounded finite unions of intervals. No single-interval extremality is asserted.

2. **Cross-three-volume L3 theorem.** `yspennstate/math-open-problems@3345697a0e1ea6c84ef3128a22917d49f0b0a826`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T013555Z-account03-B13-qform-r21/REPORT.md`. If an original-coordinate disjoint cross block `M` of a quadratic polynomial has `Z=e_3(M^T M)>0`, then the output density satisfies

`||p||_3 < 6.787 Z^(-1/9)`.

Arbitrary same-side blocks, outside couplings, affine terms and signs are permitted.

3. **Dependence-safe physical-square smoothing.** Read at `yspennstate/math-open-problems@985cf2e130fcdbf8c49bbe871b5778b207143ce1`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T185149Z-account03-B16-QFORM-r15/REPORT.md`. If `R` has density `h in L3`, and conditionally on `R=r` a scalar `V` has density at most one, then

`||p_{R+aV^2}||_infinity <= (8/3^(3/4)) |a|^(-1/2) ||h||_3^(3/4)`.

The conditional cap is valid when `V` is an original independent coordinate translated by a function of the remaining original coordinates.

The latest designated-partner normal form is account02/B13 r15, `yspennstate/math-open-problems@d59fc91cdb6c772a0b3c73ba5b90fb62e10e3bf`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T000555Z-account02-B13-productset-r15-482fba/REPORT.md`; it is applied in Section 5.

## 2. New aggregate anchored currency

Fix a physical coordinate `i` and write `a=A_ii`. For ordered disjoint triples `U,V subset [n]\{i}`, define the anchored four-by-four minor

`Delta_i(U,V)=det A[{i} union U, {i} union V]`,

where `i` is placed first in both row and column order. Define

`Omega_i(A)=sum_{|U|=|V|=3, U cap V=empty} Delta_i(U,V)^2`.

This is an aggregate original-coordinate quantity; no single minor is selected.

### Lemma 2.1 — random-cut capture

There are disjoint sets `I,J subset [n]\{i}` such that

`W_i(I,J):=sum_{U subset I, V subset J, |U|=|V|=3} Delta_i(U,V)^2 >= Omega_i(A)/64`.

**Proof.** Independently color every coordinate other than `i` red or blue with probability one half and take `I=red`, `J=blue`. For each ordered disjoint pair `(U,V)`, the event `U subset I, V subset J` has probability `2^-6=1/64`. Therefore `E W_i(I,J)=Omega_i/64`; some coloring attains at least its expectation. QED.

This random cut is only a proof of existence of two banks of original independent coordinates. It is not a spectral rotation.

## 3. Exact Schur / anchored-minor identity

Assume `a!=0` and write, in the original physical coordinate `i`,

`A=[[a,b^T],[b,C]]`, `S=C-bb^T/a`.

For every triples `U,V` disjoint from `i`, the block determinant formula gives the exact identity

`Delta_i(U,V)=a det S[U,V]`.

Consequently for the cut from Lemma 2.1,

`Z:=e_3(S[I,J]^T S[I,J])`
` = sum_{U subset I,V subset J} det S[U,V]^2`
` = a^(-2) W_i(I,J)`
` >= Omega_i(A)/(64 a^2).`                                      (3.1)

The equality is Cauchy--Binet at exterior order three followed by the scalar Schur determinant identity. This is the key structural step: an aggregate family of physical anchored four-minors becomes precisely the cross-three-volume consumed by the L3 theorem after one physical pivot is removed.

## 4. Main theorem — `QFORM-ANCHORED-DISJOINT-4VOLUME-v1`

Let `X_1,...,X_n` be independent with densities bounded by one and mass one. Let `A` be any real symmetric matrix. If for some original coordinate `i`

`a=A_ii !=0`, `Omega_i(A)>0`,

then `Q=X^T A X` has an essentially bounded density and

`boxed: ||p_Q||_infinity < C_* |a|^(-1/3) Omega_i(A)^(-1/12),`       (4.1)

where

`C_*=(8/3^(3/4)) * 6.787^(3/4) * 64^(1/12)`
`   =20.8699991163... <20.8701.`

### Proof

By the designated account02/B13 bang-bang theorem it is enough, at the small-ball level, to prove the inequality for arbitrary unit-measure product indicators; equivalently the same constant then transfers with zero loss to every cap-one product law. The analytic argument below in fact works directly for all cap-one laws.

Let `Y=X_{-i}`. Completing the square in the actual original coordinate `X_i`,

`Q=a (X_i+b^T Y/a)^2 + R`,
`R=Y^T S Y`.                                                   (4.2)

Choose `I,J` by Lemma 2.1. Equation (3.1) and the cross-three-volume theorem give an `L3` density `h` for `R` with

`||h||_3 < 6.787 Z^(-1/9)`
` <=6.787 [64 a^2/Omega_i(A)]^(1/9).`                         (4.3)

Set `V=X_i+b^T Y/a`. Conditional on `Y`, `V` is a translate of the independent cap-one variable `X_i`; therefore, after disintegrating with respect to `R`, the conditional law `V|R=r` is a mixture of translated cap-one densities and still has density at most one. The dependence-safe square theorem applies to (4.2):

`||p_Q||_infinity`
` <=(8/3^(3/4)) |a|^(-1/2) ||h||_3^(3/4)`
` <(8/3^(3/4)) 6.787^(3/4) 64^(1/12)`
`    * |a|^(-1/2+1/6) Omega_i(A)^(-1/12).`

Since `-1/2+1/6=-1/3`, this is (4.1). QED.

The homogeneity is exact: under `A -> sA`, `|a|^(-1/3) Omega_i^(-1/12)` scales as `|s|^-1`, as a density bound must.

### Geometric product-set form

By account02/B13's exact fixed-slab purification, (4.1) is equivalently the geometric estimate

`boxed:`
`|{x in product_j E_j : x^T A x in J}|`
` <20.8701 |A_ii|^(-1/3) Omega_i(A)^(-1/12) |J|`              (4.4)

for every measurable `E_j subset R` with `|E_j|=1` and every interval `J`, whenever the certificate is nonzero. The same worst-case constant is obtained if each `E_j` is restricted to a bounded finite union of intervals. No centered interval or single interval is assumed.

## 5. Actual application to the designated partner's latest bad-witness normal form

Account02/B13 r15 proves: subject to the current supplied full-to-no-pivot reduction, if full QFORM is false then for every integer `m>=2` there is a rational finite-grid product-indicator witness whose slab ratio exceeds

`C3 m`, `C3=9 sqrt(3e)=25.7010210753...`,

while preserving the original-coordinate product structure.

Apply (4.4) to such a witness `A_m`. For any physical coordinate `i` with `a_i=(A_m)_ii !=0` and `Omega_i(A_m)>0`, its bad slab forces

`20.8701 |a_i|^(-1/3) Omega_i(A_m)^(-1/12) > C3 m`.

Raising to the twelfth power and rearranging gives

`boxed: |a_i|^4 Omega_i(A_m)`
` < (20.8701/C3)^12 m^(-12)`
` <0.083 m^(-12).`                                           (5.1)

If `a_i=0` or `Omega_i=0`, the left side is zero, so (5.1) is automatic. Hence every hypothetical partner-r15 bad witness satisfies the simultaneous global collapse

`boxed: max_i |(A_m)_ii|^4 Omega_i(A_m) <0.083 m^(-12).`      (5.2)

This is a new target-level necessary condition on the finite-grid extreme-product counterexample sequence. It aggregates every disjoint anchored four-volume around every physical coordinate; it does not choose a reciprocal tiny minor or delete a coefficient perturbatively.

The r15 no-pivot estimate `|(A_m)_ii|<m^-4` alone does not imply (5.2), because `Omega_i` is a high-cardinality exterior-volume sum. Thus (5.2) adds genuine information to the partner normal form even though it does not yet contradict it.

## 6. Relation to a single disjoint rank-four cross block

There is a useful local corollary. Let `M=A[I,J]` be a disjoint original-coordinate cross block with `i notin I union J`, and let `S` be the Schur complement above. Since

`S[I,J]=M- A[I,i]A[i,J]/a`

is a rank-one perturbation of `M`, singular-value interlacing for rank-one perturbations gives

`s_k(S[I,J]) >= s_{k+1}(M)`, `k=1,2,3`.

Therefore

`e_3(S[I,J]^T S[I,J]) >= [s_2(M)s_3(M)s_4(M)]^2`,

and the same L3-to-square proof yields

`||p_Q||_infinity`
` <14.758 |A_ii|^(-1/2) [s_2(M)s_3(M)s_4(M)]^(-1/6).`         (6.1)

This is weaker than the aggregate theorem when many anchored minors contribute, but it identifies the structural meaning: a genuine physical pivot plus four independent cross directions leaves three cross directions after the Schur rank-one subtraction, and those three directions provide exactly the L3 currency needed by the square.

## 7. What is not proved and next implication

Full QFORM remains **OPEN**. The new theorem gives no information when all useful physical pivots vanish, and (5.2) has not been shown inconsistent with the three-large-eigenvalue hypothesis. Full continuity is also not claimed; the L3/hub branch used in the proof need not have a continuous representative.

The sharpened next implication is

`QFORM-ANCHORED4-VOLUME-OR-ZEROPIVOT-CLOSURE-v1`:

> Under `s_3(A)>=1`, prove that either some physical coordinate has universal-scale anchored currency `|A_ii|^4 Omega_i(A)`, yielding a universal bound by (4.1), or the simultaneous collapse of all these anchored currencies forces a zero-/near-zero-pivot bilinear/grouped-bank geometry already payable by pair-log, aggregate-E2, or two-bank mechanisms.

For the partner r15 finite-grid normal form the quantitative target is exactly to combine (5.2) with its `s_5`-small disjoint-cross-block structure and the existing max-volume rank-16 skeleton, without using raw operator-norm slab continuity on remote fragmented supports.

No claim of full solution is made.
