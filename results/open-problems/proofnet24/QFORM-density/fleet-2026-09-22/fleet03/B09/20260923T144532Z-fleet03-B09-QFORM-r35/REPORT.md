SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T14:45:32Z.
attacking: the two-anchor localized-pair endpoint after the high-hub Pluecker dichotomy: convert fixed physical hub-pair concentration into a direct aggregate linear interval bound without requiring one large 3x3 minor.

# fleet03/B09 r35 — localized physical hub pair: exact core-stratum routing

## Status

**NEW SUPPORTING THEOREM / FULL QFORM OPEN.**

This run changes mechanism after the preceding aggregate/Pluecker high-hub runs. Instead of trying to push the selected-minor Hausdorff--Young argument through two compulsory physical hub rows (which is the borderline absolute-value endpoint), it freezes the literal physical pair supplied by r34 and uses physical-pair completion, coefficient-plane smoothing, and Schur-invariant anchored volume.

The result below proves that the localized-pair endpoint has no remaining *exact algebraic core-type* obstruction: zero, nonzero rank one, definite rank two, and indefinite rank two all have source-valid O(interval length) payments. The unresolved issue is quantitative interpolation when the physical 2x2 core approaches a lower-rank stratum while the allowed input supports remain unrestricted. No small coefficient is discarded.

The unrestricted owner target and full-target continuity remain OPEN. No Gaussian, moment, compact-support, connected-support, log-concavity, diagonal-basis, or post-rotation-independence assumption is used.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source state and completed inputs


Corrections retained: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint 3D coarea is false; normalized conditional projection caps cannot be used as independence; fiber-sup arguments can lose dimension; one universally good physical cross minor is false; and a small coefficient cannot be deleted under arbitrary unbounded supports.

Completed source results used at their exact scopes:

1. **This slot r32, aggregate compiler.** `QFORM-RANK2-HUBSTAR-AGGREGATE-COMPILER-v1`, canonical bundle `yspennstate/math-open-problems@640165d39efca44cf3cf7fe2d2e5638a823a335b`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T124906Z-fleet03-B09-QFORM-r32/REPORT.md`. It gives a leaf partition `S,T` with `W(S)>=(27/256)G_*` in the diffuse-singleton branch.

2. **This slot r34 checkpoint.** `yspennstate/math-open-problems@3fb21248b8a2c0947f7c48fcb11e5bf6f47a7b8c`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T141215Z-fleet03-B09-QFORM-r34/SUBSTANTIVE.md`. In the still-unpaid high-hub branch, with the concrete choice `delta=1/4`, either the one-anchor theorem is already payable, or there are two literal physical hub rows `a,b` whose Pluecker weight satisfies

   `w_ab=det(P[{a,b},:])^2 >=16/25`.                            (1.1)

3. **Exact-rank-one pair theorem.** This slot r25, `QFORM-RANKONE-HUBPAIR-RANDOM-SLOPE-v1`, canonical `yspennstate/math-open-problems@195447da931f086720afaa12ac902ed7d33dd32e`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T061516Z-fleet03-B09-QFORM-r25/REPORT.md`. If the physical pair core is `E=sigma r r^T`, `n perpendicular r`, and `Hn!=0`, then

   `||p_Q||_infinity <=4*2^(3/4)*e^(1/4)(|sigma| ||Hn||_2)^(-1/2)`.

4. **Two-zero-anchor coefficient-plane theorem.** fleet03/B07 `QFORM-TWO-ANCHOR-COEFFICIENT-PLANE-v1`, canonical `yspennstate/math-open-problems@309a7cf35906f05d767ff2fcf1be74367f479d1c`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T224159Z-fleet03-B07-qform-r19/REPORT.md`. If the physical two-anchor core is zero and the two random coefficient forms have row matrix `R`, then

   `||p_Q||_infinity <=2 sqrt(2) det(RR^T)^(-1/4)`,

with a continuous density; arbitrary outside quadratic curvature is allowed.

5. **Indefinite pair plus one Schur cross direction.** fleet01/B09 `QFORM-INDEFINITE-PAIR-PLUS-ONECROSS-v1`, canonical report commit `yspennstate/math-open-problems@450fc77b41e4f29ae8e535b6edf03db5cf732c5e`, produced in `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B09/20260923T141440Z-fleet01-B09-QFORM-auto11/REPORT.md`. For an invertible indefinite physical pair `E`, `D=|det E|`, `kappa=sigma_min(E)`, pair-row wedge `Delta`, and pair-anchored physical third volume `V_P>0`, it proves

   `||p_Q||_infinity
     <=11.463 D^(-2/5) kappa^(-1/10) Delta^(1/20) V_P^(-1/20)`, (1.2)

and the same coefficient times interval length. Continuity is not claimed there.

6. **Designated partner fleet04/B09.** `QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1`, canonical `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`. A literal invertible physical `3x3` cross block `K` gives

   `||p_Q||_infinity <=3 |det K|^(-1/3)`,                       (1.3)

with arbitrary dense same-side blocks and a continuous density. Section 6 applies (1.3) to an actual target-valid matrix.

## 2. Setup: rank-two hub/star and the localized hub pair

Let `H,I` be disjoint sets of ORIGINAL coordinates and suppose the physical hub-to-leaf cross block is rank two,

`A[H,I]=P C^T,       P^T P=I_2`,                               (2.1)

with completely arbitrary symmetric within-leaf block `D=A[I,I]`. For each leaf `k`, r32 defines `Gamma_k` and

`G_*=sum_k Gamma_k^2`.                                         (2.2)

In the diffuse-singleton compiler let `S subset I`, `T=I\S`, be the literal leaf partition with

`W(S)>=27 G_*/256`.                                            (2.3)

Now enter the r34 localized-pair branch and fix physical hub rows `a,b in H` satisfying (1.1). Write

`P_ab=P[{a,b},:]`,
`w=det(P_ab)^2`,                                                (2.4)

and let

`B_T=A[{a,b},T]=P_ab C_T^T`.                                  (2.5)

Define the pair-row wedge

`Delta_T=det(B_T B_T^T)`.                                      (2.6)

Because both matrices in (2.5) have two coefficient directions,

`boxed: Delta_T=w det(C_T^T C_T).`                             (2.7)

In particular, the localized Pluecker condition gives

`Delta_T >=(16/25) det(C_T^T C_T)`.                            (2.8)

Let the physical pair core be

`E=A[{a,b},{a,b}]`.                                            (2.9)

All hub coordinates in `H\{a,b}` and all outside coordinates may be conditioned. This preserves independence of the physical pair and the leaf coordinates and changes only affine terms in the active polynomial.

## 3. Fixed-pair compiler: the diffuse third volume survives with a universal fraction

For the actual cross cut from `{a,b} union S` to `T`, define the squared physical third volume anchored on the fixed pair

`V_ab(S)
 =sum_(k in S) sum_(J subset T, |J|=3)
    det A[{a,b,k},J]^2`.                                      (3.1)

The r32 physical-minor factorization is

`det A[{a,b,k},J]
 =det(P_ab) det([C_J^T;D[k,J]]).`                              (3.2)

Therefore, **exactly**,

`boxed: V_ab(S)=w W(S).`                                      (3.3)

Combining (1.1) and (2.3),

`boxed: V_ab(S) >=(16/25)(27/256)G_* =27G_*/400.`              (3.4)

Thus localization of the hub plane does not destroy the diffuse leaf third-volume currency. It converts it into one fixed-pair anchored physical volume, before any reciprocal individual minor is taken.

Moreover `V_ab(S)>0` forces `Delta_T>0`: any nonzero determinant in (3.1) contains the two pair rows, so those two rows must be linearly independent on `T`.

## 4. Main theorem — every exact algebraic type of the localized physical core is paid

### Theorem `QFORM-LOCALIZED-HUBPAIR-EXACT-CORE-ROUTING-v1`

Assume the setup above and `V_ab(S)>0`. Then each exact algebraic type of the physical `2x2` core `E` has a direct source-coordinate linear-interval estimate.

### (A) Zero core

If `E=0`, then

`boxed:
 ||p_Q||_infinity <=2 sqrt(2) Delta_T^(-1/4).`                  (4.1)

The density is continuous. In the r34 localized branch, (2.8) yields

`boxed:
 ||p_Q||_infinity
 <=sqrt(10) det(C_T^T C_T)^(-1/4).`                            (4.2)

**Proof.** After conditioning the other hub/outside coordinates, the polynomial has the exact two-zero-anchor form

`Q=2X_a L_a(X_I)+2X_b L_b(X_I)+H(X_I)`,                        (4.3)

with arbitrary measurable quadratic-affine `H`. The two coefficient rows restricted to `T` are precisely the rows of `B_T`; adding the `S` columns can only increase the second compound. Apply the completed coefficient-plane theorem and (2.6). Equation (4.2) follows from `w>=16/25`. QED.

### (B) Nonzero rank-one core

Suppose

`E=sigma r r^T`, `|r|=1`, `sigma!=0`,                          (4.4)

and let `n` be its unit null direction. Then

`boxed:
 ||p_Q||_infinity
 <=4*2^(3/4)*e^(1/4)
   |sigma|^(-1/2) ||B_T||_F^(1/2) Delta_T^(-1/4).`             (4.5)

Numerically the leading constant is `8.637859...`. In the localized branch,

`boxed:
 ||p_Q||_infinity
 <9.658 |sigma|^(-1/2)
    ||C_T||_F^(1/2) det(C_T^T C_T)^(-1/4).`                    (4.6)

The same coefficient multiplies every interval length. Continuity is not claimed by this route.

**Proof.** The full complementary coupling of the pair contains the `T`-bank coupling `B_T`. Hence

`||H n||_2 >=||B_T^T n||_2 >=sigma_min(B_T)`.                  (4.7)

For a two-row matrix,

`sigma_min(B_T)^2
 >=det(B_TB_T^T)/tr(B_TB_T^T)
 =Delta_T/||B_T||_F^2`.                                       (4.8)

Insert (4.7)--(4.8) into the invariant r25 rank-one theorem. This proves (4.5). Since `P_ab^T P_ab<=I_2`, `||B_T||_F<=||C_T||_F`; combine with (2.8) to obtain (4.6), where

`4*2^(3/4)*e^(1/4)*(25/16)^(1/4)=9.657420...<9.658`. QED.

### (C) Invertible definite core

If `E` is positive or negative definite, then

`boxed:
 ||p_Q||_infinity <=pi / sqrt(|det E|).`                        (4.9)

The same coefficient gives the interval estimate.

**Proof.** Condition on every complementary original coordinate. The remaining pair polynomial is `x^T E x+ell^T x+c`; completing the square only translates its center. The pair joint input density is at most one. An interval of output length `epsilon` cuts an elliptic annulus of area exactly `pi epsilon/sqrt(|det E|)` (after reflection for negative definite `E`). Average the conditional inequality. No rotation of the random input law is used as an independence claim. QED.

### (D) Invertible indefinite core

Let

`D_E=|det E|>0`, `kappa_E=sigma_min(E)>0`.                     (4.10)

Then the fixed-pair anchored third volume pays the logarithmic pair singularity:

`boxed:
 ||p_Q||_infinity
 <=11.463 D_E^(-2/5) kappa_E^(-1/10)
     Delta_T^(1/20) V_ab(S)^(-1/20).`                          (4.11)

Consequently, in the r34 localized branch,

`boxed:
 ||p_Q||_infinity
 <13.117 D_E^(-2/5) kappa_E^(-1/10)
     Delta_T^(1/20) G_*^(-1/20).`                              (4.12)

The same constants multiply interval length. Continuity is not claimed by this route.

**Proof.** Apply fleet01/B09 `QFORM-INDEFINITE-PAIR-PLUS-ONECROSS-v1` to the literal pair `{a,b}`, source bank `S`, and column bank `T`. Its exact Schur wedge identity says the pair-anchored physical third volume cannot be erased by completing the indefinite pair, and yields (4.11). Insert (3.4):

`11.463*(400/27)^(1/20)=13.11696...<13.117`,                   (4.13)

which gives (4.12). QED.

The four cases exhaust every exact real symmetric `2x2` core.

## 5. What has actually been removed, and the first unpaid implication

The high-hub survivor from r34 is therefore no longer an unexplained `two compulsory selected rows` endpoint. Once the hub Pluecker mass localizes on a literal pair, the aggregate diffuse third volume becomes the fixed-pair quantity (3.4), and **all exact core ranks/signatures have product-preserving payments**.

What remains is quantitative, not algebraic:

`QFORM-LOCALIZED-HUBPAIR-NEARSTRATUM-INTERPOLATION-v1`:

> Obtain a bound uniform as a nonzero physical pair core approaches the zero/rank-one strata, by spending the fixed pair cross wedge `Delta_T` and anchored third volume `V_ab(S)>=27G_*/400` jointly. The proof must retain the exact Schur remainder; a small nonzero quadratic coefficient cannot be discarded because the input laws have no support or moment bound.

This is a mechanism change from the preceding selected-minor absolute-value route. The zero and exact-rank-one endpoints are already finite; the missing theorem must interpolate to them rather than take a reciprocal determinant before the aggregate cross currency is used.

A useful warning is visible in (4.11): the indefinite pair theorem alone deteriorates as `det E ->0`, while the exact rank-one theorem (4.5) is finite at the limiting rank-one matrix. Therefore continuity of the *proof bound* across the rank stratum is precisely the missing analytic interface; no statement here treats the blow-up as genuine concentration.

## 6. Actual application of the designated fleet04/B09 theorem

Use six original coordinates ordered `(a,b,k,1,2,3)` and the symmetric coefficient matrix whose only nonzero upper-triangular entries are

`A[a,1]=A[b,2]=A[k,3]=1`.                                      (6.1)

Equivalently, for the literal cut `{a,b,k}|{1,2,3}` the physical cross block is

`K=I_3`.                                                       (6.2)

The full matrix is three disjoint hyperbolic edges and has spectrum

`{-1,-1,-1,1,1,1}`.                                           (6.3)

It is therefore a literal owner-target matrix. It also fits the localized rank-two hub/star picture with hub set `{a,b}`, leaf set `{k,1,2,3}`, `P=I_2`, rows of `C` equal to `(0,0),(1,0),(0,1),(0,0)`, and within-leaf edge `D[k,3]=1`.

Here

`w=1`, `Gamma_k^2=Gamma_3^2=1`, `G_*=2`,                      (6.4)

and choosing `S={k}`, `T={1,2,3}` gives

`W(S)=V_ab(S)=Delta_T=1`.                                     (6.5)

The designated partner theorem (1.3) applies at the actual inequality

`boxed:
 ||p_(X^T A X)||_infinity
 <=3 |det I_3|^(-1/3)=3,`                                     (6.6)

with a continuous density and `P{X^TAX in L}<=3|L|`.

For comparison, because this regression has zero pair core, (4.1) independently gives `||p_Q||_infinity<=2sqrt(2)`. The two estimates use different valid receivers; (6.6) is recorded specifically as the required application of the completed designated-partner result.

## 7. Integrity and next step

This report does **not** assert that `det(C_T^T C_T)`, `|sigma|`, `|det E|`, or `kappa_E` are individually bounded below by the three-large-eigenvalue hypothesis. It does not turn the exact-stratum routing into a universal constant by compactness, since arbitrary input supports rule out perturbative deletion of small coefficients.

The concrete next B09 step is to prove `QFORM-LOCALIZED-HUBPAIR-NEARSTRATUM-INTERPOLATION-v1`, preferably by averaging the pair logarithmic envelope against a fractional potential of the exact Schur cross while keeping the zero/rank-one random-slope endpoints in the same inequality. If that fails decisively, the remaining localized-pair configuration should be exported as a quantitative obstruction rather than silently treated as paid.

Full QFORM: **OPEN**. Full-target continuous density: **OPEN**.
