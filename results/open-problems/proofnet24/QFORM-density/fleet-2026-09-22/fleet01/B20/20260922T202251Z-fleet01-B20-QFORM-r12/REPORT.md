SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-22T20:22:51Z.
attacking: the first unpaid packet after fleet02/B20 r18 strong-hub gluing, by spending aggregate second exterior curvature before reciprocal minor selection and then forcing direct hub-direction alignment in the low-leverage residue.

# fleet01/B20 QFORM r12 — balanced-hub E2 payment and direct-alignment reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T202251Z-fleet01-B20-QFORM-r12`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL SUBBRANCH CLOSED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** no new full-target continuity claim.

## 1. Scope and correction boundary

The target remains the full arbitrary-dimensional statement: independent real physical coordinates `X_i` with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one; prove one universal finite essential bound for the density of `Q=X^TAX`, or give a valid target counterexample.

This report does not use the refuted law-uniform pointwise quadratic oscillatory decay, arbitrary-joint rank-three coarea, positive moments of worst conditional projection densities, independence after a spectral rotation, unrestricted fiber suprema, or a single-good-minor exhaustion. Every active bank below consists of original coordinates; arbitrary same-bank quadratic terms and outside couplings are retained exactly in the cited analytic inputs.

The full theorem remains **OPEN**.

## 2. Designated partner actually consumed: fleet02/B20 r18

Canonical source used:

`yspennstate/math-open-problems@8f7fc147ba50f1bcdf3a5c83c3722ae18238e9db`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260922T200120Z-fleet02-B20-QFORM-r18/REPORT.md`.

That run proves `QFORM-STRONG-HUB-CUT-GLUING-v1`. In the retained compact coherent-triangle physical-pivot setup, put

`m:=3501/8000`, `|a|>=m`,

and let `S` be the exact physical Schur complement after pivoting on the original coordinate with coefficient `a`. After the already-paid rank-two/ridge cuts are removed, fleet02/B20 r18 turns the externalized packet into three alternatives: pivot star, heavy Schur edge, or a balanced aligned-bank packet.

The result used here is its **balanced bank** alternative. There are a residual physical hub `p` and disjoint nonempty original-coordinate banks `U,V` such that, with

`c_U=S[p,U]`, `c_V=S[p,V]`, `M=S[U,V]`,

one has the actual inequalities

`r_U:=||c_U||_2 > g:=1/(8sqrt(2))`,
`r_V:=||c_V||_2 > g:=1/(8sqrt(2))`.                             (2.1)

The same partner also gives an abstract rank-one approximation to `M`, but the argument below does not need to use its rotated approximating vectors as random variables.

Numerically

`m=0.437625`, `g=0.0883883476483...`.                           (2.2)

## 3. Fresh compatible analytic input: one physical row plus aggregate E2

I also consume the completed fleet03/B06 r18 theorem `QFORM-ONE-ROW-E2-HYBRID-L3-v1`, canonical source

`yspennstate/math-open-problems@897d37adecb8f18c46b456569884b2ee22eeb3ee`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T201841Z-fleet03-B06-qform-r18/REPORT.md`.

For an original-coordinate cross block `H`, a fixed physical row of norm `r`, and `H_0` obtained by deleting that row, put

`E=E_2(H_0)=e_2(H_0H_0^T)`.

That theorem, combined there with the dependence-safe physical-square kernel, gives for an outer physical scalar pivot `a!=0`

`||p_Q||_infinity <= [8/3^(3/4)] / sqrt(2pi|a|) * sqrt(J)`,      (3.1)

where

`J <= pi e E^(-1/4)
     +2^(27/8) pi e^(13/16) r^(-3/8) E^(-5/32)`.                (3.2)

There is no range-leverage assumption, no support/moment hypothesis and no reciprocal single minor.

A second compatible completed input used in Section 5 is fleet03/B03 r17, canonical source

`yspennstate/math-open-problems@924b3c4c70f86a64402863fe228f641bf3db60b2`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T175531Z-fleet03-B03-QFORM-r17/REPORT.md`.

Its `q=1,k=2` determinant-bank theorem says that if an original-coordinate residual cross block `N` has maximum selected-side range leverage at most `1/2`, then

`H_(1/2)(R):=sup_t E|R-t|^(-1/2)
 <= C_E E_2(N)^(-1/8)`,

with

`C_E=7.673759290384858`.                                       (3.3)

Behind the outer physical square this gives

`||p_Q||_infinity <= |a|^(-1/2) C_E E_2(N)^(-1/8)`.            (3.4)

## 4. New theorem I: balanced-bank aggregate E2 is already paid

### Theorem 4.1 — `QFORM-BALANCED-HUB-E2-PAYMENT-v1`

In the fleet02/B20 balanced packet (2.1), if

`E_2(M)>=E_0:=2^(-20)`,                                        (4.1)

then the full ambient quadratic form satisfies

`boxed(||p_Q||_infinity < 92).`                                (4.2)

All same-bank self blocks and all outside couplings remain arbitrary.

### Proof

Use the residual physical cut

`H=S[{p} union U,V]`.

Its physical row indexed by `p` is exactly `c_V`, hence its row norm satisfies `r=r_V>g`. Deleting that physical row leaves exactly

`H_0=M=S[U,V]`.

Therefore fleet03/B06 r18 applies to the **actual residual form**, not to a spectral compression. Equations (3.1)-(3.2), together with `|a|>=m`, `r>=g`, and `E>=E_0`, give

`J <= J_0
 := pi e E_0^(-1/4)
   +2^(27/8)pi e^(13/16)g^(-3/8)E_0^(-5/32)
 =1864.7873899162066...`                                       (4.3)

and hence

`||p_Q||_infinity
 <= [8/3^(3/4)] / sqrt(2pi m) * sqrt(J_0)
 =91.3950577823511... <92.`                                    (4.4)

This proves the theorem. QED.

### Consequence of failure

Every still-unpaid balanced-bank state now satisfies

`E_2(M)<2^(-20).`                                               (4.5)

Since, for singular values `s_1>=s_2>=...` of `M`,

`E_2(M)=sum_(j<k)s_j^2s_k^2
       >=s_1(M)^2 sum_(k>=2)s_k(M)^2`,                          (4.6)

failure of (4.1) gives the quantitative alternative

`||M||_op<g/2=1/(16sqrt(2))`                                   (4.7)

or

`dist_F(M,{rank<=1})
 =sqrt(sum_(k>=2)s_k(M)^2)
 <sqrt(E_0)/(g/2)
 =sqrt(2)/64
 =0.02209708691... .`                                          (4.8)

Thus the prior `0.0988...` abstract near-rank-one bank is sharpened, without a leverage assumption, to either a genuinely weak `U-V` operator compared with the two hub arms, or a `0.0221` Frobenius rank-one tube.

## 5. New theorem II: hub-wedge payment or direct hub-direction alignment

The preceding theorem controls rank-two curvature intrinsic to `M`. A different obstruction is that a nearly rank-one `M` may point in directions unrelated to the actual physical hub arms. This too can be paid unless a genuine high-leverage localization occurs.

Put

`u=c_U/r_U`, `v=c_V/r_V`,                                      (5.1)

so `u,v` are algebraic unit vectors supported on disjoint original-coordinate banks. No independence is asserted for these rotated scalar projections.

Define

`D_U:=||(I-uu^T)M||_F`,
`D_V:=||M(I-vv^T)||_F`,                                       (5.2)

and the two honest physical cross blocks

`N_U=S[U,{p} union V]=[c_U,M]`,
`N_V^T=S[V,{p} union U]=[c_V,M^T]`.                            (5.3)

Let `ell_U` be the maximum physical-coordinate leverage of `range(N_U)` on the selected side `U`, and `ell_V` the corresponding maximum leverage of `range(N_V^T)` on `V`.

### Exact wedge identity

Cauchy--Binet gives

`E_2(N_U)=e_2(N_UN_U^T)
 >= sum_(z in V)||c_U wedge M[:,z]||_2^2
 =r_U^2 D_U^2`,                                                (5.4)

and symmetrically

`E_2(N_V^T)>=r_V^2 D_V^2`.                                    (5.5)

These are sums of squared **physical 2 x 2 cross minors**. Nothing has been localized to one tiny determinant.

### Theorem 5.1 — `QFORM-HUB-WEDGE-OR-DIRECT-ALIGNMENT-v1`

Set

`xi:=1/64`.                                                     (5.6)

For every balanced packet (2.1), each side obeys the following dichotomy:

- either its augmented block has selected-side leverage `>1/2`;
- or `D_side<xi`;
- or the full target density is universally paid with

`boxed(||p_Q||_infinity <61).`                                 (5.7)

In particular, if both `ell_U<=1/2` and `ell_V<=1/2` and the full form is still unpaid, then with

`lambda=u^T M v`

one has the direct, source-coordinate hub alignment

`boxed(||M-lambda u v^T||_F<1/32).`                            (5.8)

### Proof

Suppose `ell_U<=1/2` and `D_U>=xi`. By (5.4) and (2.1),

`E_2(N_U)>=g^2 xi^2`.                                          (5.9)

Apply the fleet03/B03 determinant-bank theorem (3.3) to the actual residual cross bank `N_U` and then the outer physical square:

`||p_Q||_infinity
 <=C_E m^(-1/2)(g xi)^(-1/4)
 =60.1732335553453...<61.`                                     (5.10)

The same proof applies on the `V` side. Hence an unpaid low-leverage side must have `D_side<xi`.

If both sides are low leverage and unpaid, let `P_u=uu^T`, `P_v=vv^T`. Then

`M-P_uMP_v=(I-P_u)M+P_uM(I-P_v)`,                              (5.11)

so

`||M-P_uMP_v||_F
 <=D_U+D_V<2xi=1/32`.                                          (5.12)

Finally `P_uMP_v=(u^TMv)uv^T=lambda uv^T`, proving (5.8). QED.

## 6. The sharpened surviving packet

Combining fleet02/B20 r18 with Theorems 4.1 and 5.1, the balanced aligned-bank part of the current coherent-triangle branch no longer has an arbitrary cutwise orientation. Every still-unpaid state satisfies all of the following:

1. two genuine physical hub arms remain strong:

   `||S[p,U]||_2, ||S[p,V]||_2 >1/(8sqrt(2));`                 (6.1)

2. the interbank second exterior curvature is tiny:

   `E_2(S[U,V])<2^(-20);`                                      (6.2)

3. either one augmented physical cross bank has range leverage `>1/2`, or else

   `S[U,V]` is within `1/32` in Frobenius norm of the **specific** rank-one direction determined by the two hub arms:

   `S[U,V]=lambda
     [S[U,p]/||S[U,p]||]
     [S[p,V]/||S[p,V]||]^T + E`,
   `||E||_F<1/32`;                                             (6.3)

4. independently, either `||S[U,V]||_op<1/(16sqrt(2))`, or its distance to rank one is `<sqrt(2)/64`.  (6.4)

This is a materially stronger endpoint than generic `dist_F(cut,rank1)<sqrt(10)/64`: the aligned rank-one direction is now pinned to actual source-coordinate hub coefficients, and all aggregate second exterior curvature above a fixed scale has been paid with no leverage gate.

## 7. Conditional proof map and first unpaid implication

The current P1/coherent branch now runs as follows.

- Existing pair/triple theorems pay the noncompact cell.
- fleet02/B20 r17 externalizes every compact analytically unpaid coherent triangle.
- fleet01/B20 r11 plus fleet03/B20 r16 pay every residual physical cut with `s_2>=1/64` or ridge effective dimension at least five.
- fleet02/B20 r18 performs dimension-free strong-hub gluing and reduces the survivor to pivot-star / heavy-Schur-edge / balanced-bank packets.
- **New here:** in the balanced-bank packet, `E_2(M)>=2^-20` is paid by `<92`; and any low-leverage hub-wedge deviation `>=1/64` is paid by `<61`. The low-leverage unpaid survivor is forced into the direct two-arm one-factor geometry (6.3).

Therefore the first unpaid implication has narrowed to:

`QFORM-TWO-ARM-ONEFACTOR-OR-HIGHLEVERAGE-PAYMENT-v1`:

> In the retained physical-pivot branch, pay either (a) the pivot-star / dominant-heavy-Schur-edge packet, (b) a balanced hub packet for which an augmented bank has physical range leverage `>1/2`, or (c) the direct two-arm one-factor packet (6.1)-(6.4) with arbitrary same-bank self curvature and all outside couplings retained. Equivalently, force one of these states into an already-paid physical pair, grouped square, ridge or rank-two determinant packet without treating the algebraic vectors `u,v` as independent random coordinates.

The natural next attack is now **self-curvature versus one-factor geometry**, not cutwise gluing: if the within-`U` or within-`V` curvature has a dimension-free component transverse to the hub directions, it must be aggregated before reciprocal payment; if it does not, the surviving quadratic geometry becomes an almost three-scalar two-arm star, where the full `s_3(A)>=1` condition should force a third curvature source.

The physical pivot-star and dominant-heavy-edge alternatives from r18 are not claimed paid here. The full QFORM theorem remains OPEN.

## 8. Regression arithmetic

The deterministic arithmetic used above is:

`m=3501/8000=0.437625`

`g=1/(8sqrt(2))=0.08838834764831843...`

`E0=2^(-20)=9.5367431640625e-7`

`J0=1864.7873899162066...`

`K_E2=[8/3^(3/4)](2pi m)^(-1/2)sqrt(J0)
     =91.3950577823511...`

`K_wedge=7.673759290384858 m^(-1/2)(g/64)^(-1/4)
        =60.1732335553453...`

`sqrt(E0)/(g/2)=sqrt(2)/64=0.02209708691207961...`.

These numerical evaluations only verify constants; the inequalities are analytic.
