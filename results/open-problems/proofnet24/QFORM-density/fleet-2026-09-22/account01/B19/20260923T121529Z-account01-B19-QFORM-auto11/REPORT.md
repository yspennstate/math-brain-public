SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T12:15:29Z.
attacking: the strict-N3 STAR grouped-descent gap — combine the partner's two-channel/leaf-source obstruction with the collective-tail volume theorem and force the unpaid leaf cross block into near-rank-one/rank-two or two explicit double-anchor chambers.

# account01/B19 auto11 — STAR collective-tail payment and double-anchor reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED`; the full QFORM theorem remains OPEN. Continuity remains a separate global question.

## 1. Source-pinned inputs actually used

### 1.1 Previous B19 balanced STAR cut

The immediately preceding account01/B19 result is

`yspennstate/math-open-problems@0add399f3a15e6c846c8fdef7ea85d620788379c`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T111445Z-account01-B19-qform-r31/REPORT.md`.

In the strict `N3(1/256)` STAR state it constructs one partition of the leaf coordinates

`h^c=J disjoint_union K`

such that both original-coordinate hub-star banks retain energy at least

`beta0=1711/131072`,

and, for the actual leaf cross block

`N=B[J,K]=A[J,K]`,

one has

`E:=||N||_F^2 > c0:=65025/262144`.                                  (1.1)

It also applies the unrestricted D5 theorem. With `x_r=s_r(N)^2`, every state not already paid by

`||p_Q||_infinity<199.413`                                          (1.2)

satisfies

`x1+x2+x3+x4 > (63/64) E`.                                         (1.3)

No tail is deleted in (1.3).

### 1.2 Current designated partner account02/B19

The current partner report was read at the fresh pre-run math snapshot

`yspennstate/math-open-problems@27ae9c5fbf53787fac1d61d7f480e0283be8c1c5`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/account02-B19-20260923T111227Z-6af6679d/REPORT.md`.

It proves that the STAR packet `two quantitative star channels + one leaf eigenvalue >=1` does **not** force a fixed rank-three physical cross volume. Its exact-rank-three family has nonzero spectrum `{1,1,-1}` and can make every `Pi3(A[I,J])` tend to zero, while an exact grouped representation

`Q=Y1^2+2Y2Y3`                                                       (1.4)

is uniformly paid by the completed third-square/hyperbolic theorem. Thus a valid continuation must allow a genuine low-cross-rank grouped endpoint instead of trying to extract a fixed local three-volume.

### 1.3 Collective-tail theorem and D' actually applied below

The required current volume package is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`.

For a physical cross block `M`, with squared singular values `y_r`,

`T2=sum_(r>=3)y_r`,

and `P2` the top-two left singular projection, it proves that

`max_i (P2)_ii<=1/2`,  `T2/y3>=225`                                (1.5)

imply

`||p_Q||_infinity
 <=(9sqrt(3)e/2)[y1 y2 T2]^(-1/6)`.                                (1.6)

The conclusion retains all self blocks, all outside couplings, affine terms, signs and extra spectrum, and gives a continuous density.

I also use Claude's completed fractional three-volume theorem D' at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

If `Z3=e3(M^T M)>0` and every three-volume row marginal is at most `h<3/4`, then

`||p_Q||_infinity
 <=6sqrt(e)(2h)^(-1/2)(3-4h)^(-1) Z3^(-1/6)`.                     (1.7)

Again self blocks and outside terms are arbitrary, and Fourier inversion gives continuity.

## 2. Main theorem — paid or genuinely low rank or doubly anchored

### Theorem 2.1 — `QFORM-STAR-TAIL-OR-DOUBLE-ANCHOR-v1`

Assume the strict-N3 STAR state and use the **same** original-coordinate partition `J,K` from (1.1). Put

`N=A[J,K]`, `E=||N||_F^2`, `x_r=s_r(N)^2`,

`T2=sum_(r>=3)x_r`.                                                  (2.1)

Then one of the following alternatives holds.

1. **D5 paid:**

   `||p_Q||_infinity<199.413`.

2. **Near rank one:**

   `x1>(15/16)E`, hence

   `sum_(r>=2)x_r<E/16`.                                            (2.2)

3. **Near rank two:**

   `x1+x2>(63/64)E`, hence

   `T2<E/64`.                                                       (2.3)

4. **Collective-tail paid:** the full law has a continuous density and

   `||p_Q||_infinity<340.320`.                                      (2.4)

5. **Double top-two leverage anchor:** for a fixed choice of top-two left/right singular projections `P_L,P_R`,

   `max_i (P_L)_ii>1/2`,  `max_j (P_R)_jj>1/2`.                    (2.5)

6. **Three-volume paid:** the full law has a continuous density and

   `||p_Q||_infinity<1018.124`.                                     (2.6)

7. **Double three-volume anchor:** `Z3=e3(N^T N)` obeys

   `Z3>E^3/58982400`,                                               (2.7)

   and there are a physical row `i in J` and physical column `j in K` whose normalized squared-minor inclusion marginals satisfy

   `alpha_i>2/3`,  `beta_j>2/3`.                                   (2.8)

   Consequently the **actual squared 3-minor volume containing both fixed physical coordinates** satisfies

   `sum_(S contains i, T contains j, |S|=|T|=3) det(N[S,T])^2
      >(1/3) Z3
      >E^3/176947200`.                                              (2.9)

Alternatives 2, 3, 5 and 7 are structural survivors, not density claims. The theorem is valid for singular `N`, repeated singular values, every sign pattern, arbitrary additional spectrum, and arbitrary independent one-dimensional input laws of density at most one.

### Proof

If the D5 exit from the preceding run applies, we are in alternative 1. Hence assume its failure, so

`x1+x2+x3+x4>(63/64)E`.                                             (2.10)

Fix

`delta=1/64`.                                                       (2.11)

#### Step A: small second singular value forces a true rank-one tube

If `x2<delta E`, then monotonicity `x3,x4<=x2` and (2.10) give

`x1 > (63/64)E-3x2
    > (63/64-3/64)E
     =(15/16)E`.                                                     (2.12)

Therefore `sum_(r>=2)x_r=E-x1<E/16`, proving alternative 2. This is a Frobenius statement about the exact matrix; no random quadratic perturbation is discarded.

#### Step B: small collective tail forces a true rank-two tube

If

`T2<E/64`,                                                          (2.13)

then `x1+x2=E-T2>(63/64)E`, proving alternative 3.

We may therefore assume for the rest of the proof that

`x2>=E/64`,  `T2>=E/64`.                                           (2.14)

In particular `s2(N)>0` and, because `T2>0`, also `s3(N)>0`.

#### Step C: high stable-rank tail is paid unless both top-two subspaces are physically heavy

Suppose first

`T2/x3>=225`.                                                       (2.15)

If a top-two left projection can be chosen with coordinate diagonal at most `1/2`, apply the completed peer-tail theorem (1.6) directly to the actual physical block `N`. From (2.14),

`x1 x2 T2 >= (E/64)^3`,                                             (2.16)

so

`||p_Q||_infinity
 <=(9sqrt(3)e/2) * 8 E^(-1/2)
 =36sqrt(3)e E^(-1/2)
 <36sqrt(3)e c0^(-1/2)
 =340.319935754...`.                                                (2.17)

This is alternative 4.

If the left gate fails, apply the same theorem to `N^T`. The singular values and `T2` are unchanged, while the constrained projection becomes the top-two **right** singular projection. Hence if either side has leverage gate at most `1/2`, (2.17) still pays the whole quadratic form. The only survivor of (2.15) is therefore alternative 5.

Repeated singular values cause no problem: fix any SVD/top-two projection. If one admissible choice satisfies the diffuse gate, the paid conclusion follows; otherwise the selected left and right projections furnish (2.5).

#### Step D: low stable-rank tail creates a quantitative third volume

Now suppose the complement of (2.15):

`T2/x3<225`.                                                        (2.18)

Then by (2.14)

`x3>T2/225>=E/(64*225)=E/14400`.                                   (2.19)

Since `x1>=x2>=E/64`, the third elementary symmetric polynomial satisfies

`Z3=e3(N^T N)
 >=x1 x2 x3
 >E^3/(64*64*14400)
 =E^3/58982400`.                                                    (2.20)

This is (2.7).

Let `alpha_i` and `beta_j` be the row and column inclusion probabilities under normalized squared `3x3` minors of `N`. If

`max_i alpha_i<=2/3`,                                               (2.21)

apply D' with `h=2/3`. Since

`6sqrt(e)(4/3)^(-1/2)(1/3)^(-1)=9sqrt(3e)`,                       (2.22)

(2.20) gives

`||p_Q||_infinity
 <=9sqrt(3e) (58982400)^(1/6) E^(-1/2)
 <9sqrt(3e)(58982400)^(1/6)c0^(-1/2)
 =1018.123741844...`.                                               (2.23)

This is alternative 6. If the row gate fails but all column marginals are at most `2/3`, apply D' to `N^T`; (2.23) is unchanged. Hence an unpaid state in (2.18) has indices `i,j` satisfying (2.8).

Under the normalized minor law `w_(S,T)=det(N[S,T])^2/Z3`, inclusion-exclusion gives

`P(i in S and j in T)
 >=P(i in S)+P(j in T)-1
 =alpha_i+beta_j-1
 >1/3`.                                                             (2.24)

Multiplying by `Z3` and using (2.20) proves (2.9). QED.

## 3. Why this directly answers the current partner obstruction

The current account02/B19 partner proves that STAR plus a leaf eigenvalue cannot force a uniform rank-three cross volume. Theorem 2.1 does not try to force one. It spends the **entire collective singular tail** when that tail is diffuse, and otherwise records the exact matrix-level low-rank/anchor structure.

For the partner's explicit near-coloop family, split the `E3` ray equally so both hub-star banks remain quantitative, split the independent `E1` ray equally, and put the residual `E2` ray on one side. The resulting leaf cross block has orthogonal nonzero singular values

`s1=1/2`,  `s2=sqrt(epsilon/2)`,  `s_r=0 (r>=3)`.                  (3.1)

Thus it lands **exactly** in alternative 3 for every `epsilon`, and for `epsilon<1/126` it also satisfies alternative 2. This is the correct route: the partner's completed grouped identity `Q=Y1^2+2Y2Y3` pays that model uniformly, while a fictitious rank-three-volume selector cannot.

So the new theorem separates the two mechanisms rather than making them compete:

- diffuse/higher-rank leaf cross energy is paid by D5, the collective-tail theorem, or D';
- the actual counterexample to rank-three extraction is routed into the low-rank grouped chamber where the completed square/hyperbola technology is relevant.

## 4. Compact conditional proof assembly after this run

The source-pinned owner/partner synthesis first removes the already-paid scalar-pivot, physical-pair, ridge/window, volume, semidefinite, ruled-side and other certified exits, leaving the strict no-pivot `N3` problem. The current compiler then has STAR and TRIANGLE-type difficult residues, together with the remaining arbitrary-extra-spectrum glue.

For STAR, account02/B19 supplies the quantitative hub and the current partner shows why rank-three-cross forcing is false. The preceding B19 run strengthens STAR to one **same** original-coordinate cut with two quantitative hub-star channels and `E>c0`. This run then proves that, on that cut, every higher-effective-rank configuration is either already paid or must carry one of two explicit double physical anchors. Therefore the first compatible STAR debt is no longer the four-direction statement from r31; it is the strictly narrower

### `QFORM-STAR-LOWRANK-DOUBLEANCHOR-GROUPED-DESCENT-v1`

Given the strict-N3 STAR cut of (1.1), close the union of:

- `sum_(r>=2)s_r(N)^2<E/16` (near rank one),
- `sum_(r>=3)s_r(N)^2<E/64` (near rank two),
- simultaneous left/right top-two physical leverage `>1/2`,
- simultaneous row/column three-volume marginals `>2/3` with the shared-minor mass (2.9),

by an exact product-preserving grouped square/hyperbola, hub, pair, ridge, or Schur payment. The matrix tail may be retained through a proved matrix/Fourier theorem but may not be dropped as a small random perturbation.

The partner's model (3.1) shows that the first two alternatives are not artifacts: true target-valid STAR states can converge to them while every rank-three physical cross volume vanishes. The double-anchor alternatives identify the only remaining ways substantial higher-rank leaf-cross energy can evade the completed volume theorems at the fixed constants above.

Closing this STAR debt is still not by itself the full conjecture: the parallel TRIANGLE third-source coupling and any remaining arbitrary-higher-rank/global-N3 glue must also be closed. Hence no full-proof claim is made.

## 5. Corrections, signs, degeneracies and continuity

- Every partition is among ORIGINAL coordinates; no spectral projection is declared independent.
- `P_L,P_R` and the volume marginals are deterministic matrix objects only.
- No arbitrary-joint coarea estimate or conditional-density supremum is used.
- The near-rank-one and near-rank-two conclusions are matrix classifications only. Their tails remain present in the random quadratic form.
- No single physical minor is inferred from Frobenius energy. In alternative 7 only the explicitly proved **aggregate** common-row/common-column minor mass is claimed.
- All signs of `A` and all signs of its additional eigenvalues are allowed; the paid bounds depend only on singular-volume quantities.
- Rank-one and rank-two `N` are included automatically in alternatives 2/3. Repeated singular values are harmless as described in Step C.
- The peer-tail and D' branches have continuous densities because their proofs give an `L^1` characteristic function. The full theorem's continuous-representative claim remains OPEN because the surviving low-rank/double-anchor branches are not yet paid here.
- The current partner's refutation is preserved: STAR does not imply a fixed positive physical rank-three cross volume.

## 6. Deterministic check

`CHECK.py` verifies exactly

`63/64-3/64=15/16`,

`1-1/64=63/64`,

`64*64*(64*225)=58982400`,

and numerically

`36sqrt(3)e c0^(-1/2)=340.31993575416476`,

`9sqrt(3e)(58982400)^(1/6)c0^(-1/2)=1018.1237418449542`.

It terminates with `QFORM_B19_STAR_TAIL_CLASSIFICATION_CHECK_PASS`.
