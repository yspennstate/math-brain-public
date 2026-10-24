SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T05:13:56Z.
attacking: the balanced-sign pair-PSD survivor left by B11 r23; test whether the bare three-large-eigenvalue hypothesis can force the fixed-scale eight-coordinate packet needed by the local recoloring theorem.

# account03/B11 r24 — balanced three-bank obstruction to fixed-scale local packet extraction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T051356Z-account03-B11-QFORM-r24`  
**Assignment:** indefinite signatures `(2,1)` and `(1,2)`  
**Status:** `ESSENTIAL_STEP_APPLIED / EXACT COUNTEREXAMPLE TO A STRUCTURAL EXTRACTION / SOURCE-VALID AGGREGATE CONTROL / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not proved by the new balanced-family estimate or by the partner splice below; only essential boundedness is asserted. The full continuous-density conclusion remains open.

## 1. Exact obligation and source boundary

The full owner target remains open: for arbitrary independent real coordinates with densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound for `X^TAX`, or give a genuine counterexample.

This run follows the current B11 continuation: track indefinite signatures through physical/product-preserving reductions and obtain useful information on a remaining opposite-sign branch. It specifically attacks the first gap left by account03/B11 r23. That run proved a strong eight-original-coordinate packet theorem in the balanced pair-PSD chamber, but its first remaining implication was to derive a **fixed-scale** packet satisfying two child `s_2` lower bounds from the bare spectral hypothesis, or route its failure to an aggregate mechanism.

The exact construction below shows that this fixed-scale local extraction is false, already for exact rank three, signature `(2,1)`, unit physical diagonals, every physical principal pair PSD, and globally balanced positive edge signs. The same construction is uniformly controlled after **high-cardinality bank aggregation**, so it is not a QFORM counterexample. It changes the proof map: in this chamber aggregation must occur before local reciprocal payment.

Binding corrections are retained. No post-rotation independence, arbitrary-joint coarea theorem, conditional-density-cap replacement for independence, pointwise law-uniform van-der-Corput estimate, finite support/moment assumption, or perturbative deletion of small quadratic coefficients is used.

The newest source theorem actually applied to pay the balanced construction is the three-variable finite-dimensional result in

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`

`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`.

In dimension three it gives, for independent cap-one variables and a symmetric quadratic matrix whose three eigenvalues have modulus at least `sigma`,

`||p_Q||_infinity <= 6 sqrt(pi)/sigma`,                           (1.1)

uniformly in affine terms.

The designated partner result applied in Section 6 is account04/B11,

`yspennstate/math-open-problems@572f6cd066c9cdef7b5a509917b4dcd79cea2fda`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T021512Z-account04-B11-sign-frustrated-triangle-r4/REPORT.md`.

For a physical triple with positive diagonals and normalized edges within `eta<1/2` of a sign-frustrated `+/-1` triangle, it gives

`||p_Q||_infinity <= 6 sqrt(pi)/[m_0(1-2 eta)]`,                 (1.2)

where `m_0` is the smallest physical diagonal in the triple.

## 2. A balanced pair-PSD exact-rank-three target family

Fix an integer `m>5`. Split `3m` ORIGINAL physical coordinates into three disjoint banks

`G_1, G_2, G_3`, each of cardinality `m`.

Define a real symmetric `3m x 3m` matrix `A_m` by

- `A_ii=1` for every coordinate;
- `A_ij=1` for distinct `i,j` in the same bank;
- `A_ij=1-5/m` for `i in G_1, j in G_2`;
- `A_ij=1-1/(10m)` for the pairs `G_1-G_3` and `G_2-G_3`.

Every entry is positive. Therefore every nonzero edge sign is `+`, so every physical triangle is sign-balanced.

Every physical principal pair is PSD. A within-bank pair has determinant zero. A cross-bank pair is

`[[1,rho],[rho,1]]`

with `0<rho<1`, hence determinant `1-rho^2>0`.

Thus this family lies precisely in the one-sign / pair-PSD / balanced chamber surviving the sign-frustrated and definite-pair exits.

## 3. Exact spectrum: hidden indefinite signature is collective

Let

`e_g = m^(-1/2) 1_{G_g}`.

The range of `A_m` is contained in `span{e_1,e_2,e_3}` and the compressed matrix in this orthonormal basis is

`B_m = [[m,     m-5,   m-1/10],
        [m-5,   m,     m-1/10],
        [m-1/10,m-1/10,m]].`                                    (3.1)

The vector `(1,-1,0)` is an eigenvector with eigenvalue `5`.

On the orthogonal symmetric two-plane `x_1=x_2`, the trace and determinant are

`T=3m-5`,

`D=-(23/5)m-1/50`.                                               (3.2)

Therefore

`det B_m = 5D = -(230m+1)/10 <0`,                               (3.3)

and the two remaining eigenvalues have opposite signs. If

`p(lambda)=lambda^2-T lambda+D`,

then exactly

`p(-3/2)=-(10m+527)/100<0`.                                     (3.4)

Since the negative root is the left root and the positive root is positive, (3.4) gives

`lambda_-(B_m)<-3/2`.                                            (3.5)

The third eigenvalue is `5`, and the remaining positive root is positive and larger than the trace correction. Hence all three nonzero eigenvalues have modulus greater than one, and

`inertia(A_m)=(2,1),  rank(A_m)=3`.                              (3.6)

Negating `A_m` gives the `(1,2)` companion.

This is a useful signature phenomenon: **every physical 2x2 principal block is PSD, but the rank-three aggregate is indefinite**. The minority direction is invisible to every physical pair and appears only after all three banks are combined.

## 4. Exact falsifier for fixed-scale eight-coordinate packet extraction

Normalize by the physical diagonals. Here every diagonal is already one, so the normalized coefficient matrix is simply `A_m`.

Take any `2x2` submatrix `C` of this normalized physical matrix. Every entry belongs to

`{1, 1-5/m, 1-1/(10m)}`.

Let `J_2` be the all-ones `2x2` matrix. Then entrywise

`|C-J_2| <=5/m`,

and therefore

`s_2(C)
 <= ||C-J_2||_op
 <= ||C-J_2||_F
 <=10/m`.                                                        (4.1)

This bound holds for **every** physical `2x2` submatrix, irrespective of how its rows and columns are selected from the three banks.

Consequently, for every fixed `c>0`, choosing

`m>10/c`                                                         (4.2)

makes it impossible to find even one child `2x2` block with `s_2>=c`, let alone the two disjoint child blocks required by the B11-r23 robust recoloring packet.

### Theorem 4.1 — `QFORM-BALANCED-FIXED-PACKET-EXTRACTION-FALSE-v1`

There is no universal `c>0` such that the bare three-large-eigenvalue hypothesis, even after restricting to exact-rank-three `(2,1)` matrices with unit physical diagonals, pair-PSD physical pairs and globally balanced positive edge signs, forces an eight-coordinate B11-r23 packet whose two child cross blocks both have second singular value at least `c`.

The family `A_m` above is an explicit target-valid counterexample to that **intermediate structural implication**.

It is not a counterexample to QFORM itself.

## 5. The same family is uniformly paid after original-coordinate bank aggregation

Let the independent input coordinates have arbitrary probability densities bounded by one. Define the three disjoint-bank linear forms

`Y_g = m^(-1/2) sum_{i in G_g} X_i`,   `g=1,2,3`.                (5.1)

Because the banks are disjoint, `Y_1,Y_2,Y_3` are genuinely independent. By the standard sharp product-linear marginal bound for a unit coefficient vector,

`||p_{Y_g}||_infinity <=sqrt(2)`.                                (5.2)

The block-constant form collapses **exactly**, with no approximation:

`X^T A_m X = Y^T B_m Y`.                                        (5.3)

Set

`Z_g=sqrt(2)Y_g`.

Then the `Z_g` are independent and have densities at most one, while

`Q = Z^T (B_m/2) Z`.                                             (5.4)

By (3.5), every eigenvalue of `B_m/2` has modulus at least `3/4`. Apply the source-pinned three-variable theorem (1.1) with `sigma=3/4`:

`boxed: ||p_Q||_infinity <= 8 sqrt(pi)
       =14.179630807244127... .`                                 (5.5)

This bound is uniform in `m` and in all input laws satisfying the original density cap.

Thus the obstruction in Section 4 is strictly about **operator order**. Localizing first loses the collective spectral currency; aggregating the original product banks first converts the hidden signature into a fixed three-variable problem and pays it uniformly.

This is exactly analogous to the previously observed flat-bank heavy-isotropic phenomena, but here it occurs inside the B11 pair-PSD balanced-sign chamber and directly falsifies the proposed next local-packet extraction.

## 6. Designated account04/B11 partner applied at an actual inequality

The balanced sign in `A_m` is not cosmetic. Flip only the sign of the `G_1-G_2` cross bank and keep all magnitudes unchanged. Thus define a companion `A_m^fr` with normalized inter-bank signs

`epsilon_12=-1,  epsilon_13=epsilon_23=+1`,                      (6.1)

and the same magnitudes

`|rho_12|=1-5/m`,
`|rho_13|=|rho_23|=1-1/(10m)`.                                  (6.2)

Every triple containing one physical coordinate from each bank has sign product `-1`. Its three diagonals equal one, and every normalized off-diagonal entry lies within

`eta=5/m`                                                        (6.3)

of the corresponding sign in the exact frustrated matrix

`C_0=[[1,-1,1],[-1,1,1],[1,1,1]]`,                              (6.4)

whose eigenvalues are `{2,2,-1}`.

For `m>10`, the designated partner theorem applies to this actual physical triple. Since `m_0=1`, it gives

`boxed: ||p_{X^T A_m^fr X}||_infinity
 <= 6 sqrt(pi)/(1-10/m).`                                       (6.5)

In particular, for `m>=20`,

`boxed: ||p_{X^T A_m^fr X}||_infinity <=12 sqrt(pi)
       =21.269446210866192... .`                                 (6.6)

This is an equation-level use of the completed account04/B11 result, not a copied citation.

The companion is itself target-valid. On the bank-constant three-space its compressed matrix is a perturbation of `m C_0`; the perturbation has maximum absolute row sum at most `51/10`. Since the smallest absolute eigenvalue of `m C_0` is `m`, Weyl gives

`s_min >= m-51/10>1`                                             (6.7)

for every integer `m>=7`.

Therefore merely changing the macroscopic **bank sign product** from balanced to frustrated changes the proof mechanism completely: frustration creates a uniformly invertible three-coordinate physical core paid by the partner, while the balanced family has no fixed-scale local child curvature at all and must be aggregated at high cardinality.

## 7. Relation to the mandatory rank-two logarithmic control

The opposite-sign rank-two control remains genuine. For independent

`X,Y ~ Uniform[-1/2,1/2]`,

`p_{2XY}(t)=log(1/(2|t|))`,  `0<|t|<1/2`,                       (7.1)

so a bare hyperbolic pair has an unbounded logarithmic density at zero.

The family `A_m` shows a complementary way in which the **third direction removes the singular endpoint**. No physical pair is indefinite at all; each physical pair is PSD. The negative direction is a collective rank-three effect produced by two `O(1/m)` deviations from a rank-one positive correlation background accumulated over `m` coordinates per bank. Once those banks are aggregated while preserving their original independence, the resulting three-variable quadratic matrix has a fixed negative eigenvalue below `-3/2` and the full density is bounded by (5.5).

Thus the third direction is not merely another local square glued to one saddle. In this chamber it is a genuinely collective product-bank direction that makes the hidden indefinite signature visible only after aggregation.

## 8. Exact computation record

The companion file `CHECK.md` records the exact characteristic-polynomial factorization and the actual numerical spot checks. The principal identities are

`det B_m=-(230m+1)/10`,

`char_B(lambda)
 =-(lambda-5)(-50lambda^2+150m lambda-250lambda+230m+1)/50`,     (8.1)

and

`p(-3/2)=-(10m+527)/100`.                                       (8.2)

Actual eigenvalue checks in this run were

`m=6:   (-1.8588276689976089, 5, 14.858827668997609)`,
`m=20:  (-1.6250751071992946, 5, 56.625075107199294)`,
`m=100: (-1.5512328026843258, 5, 296.55123280268435)`.

The attempted executable checker upload was blocked by the connector's safety classifier, so the exact algebra and the already executed numerical outputs were preserved as plain mathematical text in `CHECK.md`; no installation or bypass was attempted.

## 9. Proof-map consequence and next B11 implication

The new counterexample rules out the simplest continuation of B11 r23:

`three large eigenvalues + balanced pair-PSD signs => fixed-scale finite recoloring packet`.

That implication is false even in exact rank three.

The surviving obligation is now more precise:

**`QFORM-BALANCED-CORRELATION-BANK-AGGREGATION-v1`.** In the pair-PSD balanced-sign chamber, detect and aggregate high-cardinality groups of nearly collinear normalized physical rows **before** paying inverse local curvature. Prove that either the aggregate quotient has a fixed indefinite three-direction core (as in `A_m`), or a previously paid diffuse/ridge/cross-volume mechanism fires. The theorem must tolerate non-block-constant errors without treating small matrix coefficients as small random quadratic errors on unbounded inputs.

The full arbitrary-dimensional QFORM conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`. No full continuity conclusion is claimed. Independent end-to-end review of this new structural falsifier/payment pair is pending.
