# account01/B07 — full-spectrum row-volume transfer from a localized Pluecker packet

**Run:** `a01-b07-20260922T160118Z-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Coordinate minor selection  
**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source state

The target is the full arbitrary-product-law statement: for every dimension, independent real coordinates with scalar densities at most one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal `L^infinity` bound for the density of `Q=X^T A X`, or give a target-valid counterexample. No moment, compact-support, connected-support, sign, Gaussian, log-concavity, or post-rotation independence assumption is used. Continuity remains a separate desired conclusion.

The live corrections are respected: law-uniform pointwise quadratic-phase decay is false; a one-good-cross-minor reduction is false; a one-principal-block-or-rank-three-cross-cut dichotomy is false; and selected spectral-core minors can be cancelled in the full matrix by the orthogonal spectral complement.

### Partner result actually applied

I use the completed assigned-partner result account02/B07, `QFORM-PLUCKER-STRATUM-COLLAR-v1`, canonical report

`yspennstate/math-open-problems@55751ad6d9915a2600d42385d41388c900d29a26`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T143520Z-account02-B07-QFORM-r11/REPORT.md`.

Its localized branch supplies a selected rank-three spectral frame `U` (`U^T U=I_3`), an original-coordinate set `J`, `1<=|J|<=3`, and a nonempty `T subset J` such that

`m_T(J):=sum_{|R|=3, R cap J=T} det(U_R)^2 >= 1/8`.                 (1.1)

The same partner report exhibits the stress matrix `A=I_4-J_4/3`, showing that (1.1) does **not** imply a good principal or ordinary cross minor of the full `A`. The present run repairs exactly that transfer step at the aggregate determinant level.

## 2. Conditional end-to-end route

A sufficient B07 route would be:

1. obtain a determinant-weighted spectral packet from the selected three-large-eigenvalue subspace;
2. transfer that packet to **physical full-matrix** determinant mass without reciprocal-minor loss and without cancellation by the orthogonal spectral complement;
3. split the transferred mass into the four overlap types `h=0,1,2,3` between row and column triples;
4. pay each overlap type by a product-preserving density mechanism.

Step 2 was the first essential missing structural implication after the partner's cancellation example. It is proved below. Step 4 remains open in general, but the completely disjoint `h=0` branch now gives a concrete density estimate whenever the existing `q=1` leverage gate holds.

## 3. New theorem: Pluecker packet -> physical full-spectrum row-volume

Choose any three orthonormal eigenvectors of `A` whose eigenvalues satisfy `|lambda_j|>=1`, and let `U` be the `n x 3` matrix with those eigenvectors as columns. Put

`P=U U^T`.

Because the selected three eigenvalues have squared magnitude at least one,

`A^2 - P >= 0`                                                     (3.1)

in the Loewner order.

For each physical coordinate triple `R`, define its full row-volume

`V_R(A):=det((A^2)[R,R])`.

By symmetry of `A` and Cauchy--Binet,

`V_R(A)=det(A[R,:] A[R,:]^T)
      =sum_{|K|=3} det(A[R,K])^2`.                                 (3.2)

### Theorem `QFORM-PLUCKER-TO-PHYSICAL-ROWVOLUME-v1`

Assume a packet `(J,T)` satisfies (1.1). Then

`sum_{|R|=3, R cap J=T} V_R(A) >= m_T(J) >= 1/8`.                  (3.3)

Equivalently,

`sum_{R cap J=T} sum_{|K|=3} det(A[R,K])^2 >= 1/8`.                (3.4)

Thus an arbitrary orthogonal spectral complement cannot erase the packet after passing from `A` to the physical row-Gram matrix `A^2`; the determinant mass survives with the **same constant**.

### Proof

From (3.1), for every coordinate triple `R`,

`(A^2)[R,R] >= P[R,R] = U_R U_R^T >=0`.

For positive semidefinite `3 x 3` matrices, Loewner order implies monotonicity of each ordered eigenvalue and hence of the determinant, so

`det((A^2)[R,R]) >= det(U_R U_R^T)=det(U_R)^2`.                    (3.5)

Summing (3.5) over exactly the packet triples `R cap J=T` gives (3.3). Equation (3.4) follows from (3.2). QED.

This theorem is the key structural point of the run: the partner's counterexample kills direct selected-core -> full-`A` minor transfer, but it does **not** kill selected-core -> full-`A^2` row-volume transfer, because squaring removes spectral-sign cancellation while retaining exact physical-coordinate Cauchy--Binet weights.

## 4. Exact four-overlap decomposition

For the packet from Theorem 3, define

`E_h(A;J,T)
 := sum_{R cap J=T} sum_{|K|=3, |R cap K|=h} det(A[R,K])^2`,

for `h=0,1,2,3`.

Then (3.4) is exactly

`E_0+E_1+E_2+E_3 >= 1/8`.

Hence for at least one `h`,

`boxed( E_h >= 1/32. )`                                            (4.1)

This produces a dimension-free physical determinant bank in one of four geometrically distinct packet types:

- `h=0`: a genuine `3+3` disjoint cross-minor bank;
- `h=1`: one shared physical coordinate plus a `2+2` cross bank;
- `h=2`: two shared physical coordinates plus a `1+1` cross bank;
- `h=3`: a principal-triple bank.

The decomposition is exact and uses the full `A`, not the selected spectral core.

## 5. A single coordinate coloring captures a constant fraction

The determinant bank in (4.1) can be localized to one physical coordinate coloring without selecting one tiny minor.

Fix the winning `h`. Color each coordinate independently as `P` (shared pivot), `L` (row-only), or `R` (column-only). A pair `(R_0,K_0)` with `|R_0|=|K_0|=3` and `|R_0 cap K_0|=h` is captured when

`R_0 cap K_0 subset P`,
`R_0\K_0 subset L`,
`K_0\R_0 subset R`.

With role probabilities `p_P,p_L,p_R`, the capture probability is

`p_P^h p_L^(3-h) p_R^(3-h)`.

Choosing the symmetric optimum `p_L=p_R=(1-p_P)/2` gives:

- `h=0`: `p_P=0`, capture probability `1/64`;
- `h=1`: `p_P=1/5`, `p_L=p_R=2/5`, probability `16/3125`;
- `h=2`: `p_P=1/2`, `p_L=p_R=1/4`, probability `1/64`;
- `h=3`: no coloring is needed, probability `1`.

Therefore some deterministic coloring satisfies the physical mixed-bank lower bounds

`h=0:  >=1/2048`,
`h=1:  >=1/6250`,
`h=2:  >=1/2048`,
`h=3:  >=1/32`.                                                     (5.1)

This is a genuine dimension-free averaging/selection statement. It never takes the reciprocal of an individual minor.

## 6. Concrete density consequence on the disjoint branch

On the `h=0` branch, the coloring is just a cut `S,S^c`. The captured determinant bank is a sub-sum of

`E_3(A[S,S^c])
 =sum_{|R|=|K|=3, R subset S, K subset S^c} det(A[R,K])^2`.

Hence some physical cut satisfies

`E_3(A[S,S^c]) >= 1/2048`.                                        (6.1)

Apply account01/B07's preceding theorem `QFORM-AGGREGATE-CROSSMINOR-DETERMINANT-v1` (canonical report `yspennstate/math-open-problems@22acf813ef825872ffe594818d6adb27e9d4e41f`) to `B=A[S,S^c]`. If either side of this cross block satisfies the `q=1` range-leverage gate `max diagonal <=1/2`, then the full quadratic form has a continuous density and

`||p_Q||_infinity
 <= C_3 E_3(B)^(-1/6)
 <= C_3 2048^(1/6)
 = C_3 2^(11/6)
 < 20.155`,                                                       (6.2)

where

`C_3 = e/(6 sqrt(2)) Beta(1/6,1/12)=5.655763773...`.

Thus the partner's localized packet now yields an actual universal continuous-density bound on the disjoint+leverage subbranch, despite arbitrary additional eigenvalues of either sign.

The remaining disjoint debt is exactly the high-leverage case; the `h=1,2,3` mixed banks require their own product-preserving payment rather than a cross-block-only theorem.

## 7. Exact stress test: the partner cancellation matrix is absorbed by h=2

Take the partner's full-spectrum cancellation example

`A=I_4-(1/3)J_4`,

with spectrum `{1,1,1,-1/3}`. Let `U` span the three `+1` eigendirections, so `P=I_4-J_4/4` and every selected-core triple weight equals `1/4`.

Take `J={1,2}` and `T=J`. Then the packet contains the two triples `{1,2,3}` and `{1,2,4}`, so

`m_T=1/2`.                                                         (7.1)

The partner observed that every full physical principal `3 x 3` minor of `A` is zero. Nevertheless

`A^2=I_4-(2/9)J_4`,

and every `3 x 3` principal row-Gram determinant equals `1/3`. Therefore

`sum_{R cap J=T} det((A^2)[R,R]) = 2/3 >= 1/2`.                    (7.2)

For each of the two packet row triples, the principal `h=3` determinant is zero, while the three column triples differing in exactly one coordinate each have determinant `+/-1/3`. Consequently

`E_2(A;J,T)=6*(1/9)=2/3`,
`E_0=E_1=E_3=0`.                                                   (7.3)

So the exact matrix that refuted direct principal/cross-minor transfer is **not** an obstruction to the new theorem: all of the lost principal volume reappears as a two-shared-coordinate mixed-minor bank. This pinpoints the next analytic payment very sharply.

## 8. First surviving implication

The structural transfer debt from the partner run is closed. The next target is

`QFORM-MIXED-OVERLAP-BANK-PAYMENT-v1`:

> Starting from one of the physical determinant banks (5.1), prove a universal density bound while preserving the original-coordinate product law. For `h=0`, only the high-leverage subcase remains after (6.2). For `h=1` and `h=2`, exploit the shared pivot coordinates jointly with the disjoint bank rather than Schur-complementing through a potentially singular tiny principal block. For `h=3`, use the aggregate principal-triple bank without selecting one dimension-dependent tiny determinant.

A useful exact object for `h=2` is the bordered-minor kernel

`C_S(i,j)=det A[S union {i}, S union {j}]`, `|S|=2`,

because the stress matrix above places all surviving determinant mass in these kernels. Any next proof that discards them cannot handle the known cancellation example.

## 9. Status

`ESSENTIAL_STEP_APPLIED`:

- a completed account02/B07 Pluecker packet of mass at least `1/8` is transferred to **full-matrix physical determinant mass with no loss**;
- one of four exact row/column overlap classes carries at least `1/32`;
- one coordinate coloring captures a dimension-free fraction, with explicit constants `1/2048`, `1/6250`, `1/2048`, `1/32`;
- on the `h=0` plus `q=1` leverage subbranch, the full law has a bounded **continuous** density with constant `<20.155`;
- the partner's cancellation matrix is checked exactly and lands entirely in the `h=2` bank, showing that the new transfer addresses the real obstruction rather than bypassing it.

`FULL_TARGET_OPEN`: the mixed-overlap payment and disjoint high-leverage branch remain unresolved for arbitrary symmetric `A`.
