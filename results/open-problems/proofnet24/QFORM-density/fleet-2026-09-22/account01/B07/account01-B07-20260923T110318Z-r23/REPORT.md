SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T11:03:18Z.
attacking: the fixed double-pair third-volume survivor; compress its entire determinant bank to a physical edge and a quantitative principal-pair/high-tail or rank-two-tube alternative, without choosing one tiny minor.

# account01/B07 r23 — a double-pair third-volume bank forces a physical edge, then a paid pair-tail or a low-rank survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / GEOMETRY  
Run: `account01-B07-20260923T110318Z-r23`  
Status: `ESSENTIAL_STEP_APPLIED / NEW DOUBLEPAIR EXTENSION IDENTITY + EDGE EXTRACTION + PARTNER PAIRTAIL PAYMENT / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

## 1. Target, controls, and source boundary

The target remains the unrestricted one: for every dimension, independent real ORIGINAL-coordinate inputs with probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with one universal essential-supremum bound, or give a target-valid counterexample. No Gaussianity, moments, compact or connected support, log-concavity, iid assumption, or independence after spectral rotation is used. Continuity is tracked separately.

Fresh protected control immediately before this report remained OWNER CONTROL revision `2026-09-22.15`, QFORM-only, with no B07 pause. The live correction inbox was reread. In particular this argument does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, positive conditional projection-height moments, naive fiber-supremum integration, perturbative deletion of a small nonzero quadratic tail, or a one-good-minor assertion.

Completed sources used at equations:

1. This slot's preceding double-anchor compiler:
   `yspennstate/math-open-problems@dbdedece92b8abf88ad0eee0860011f88764fca4`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T100306Z-r22/REPORT.md`.
   Its unpaid survivor contains a fixed two-row/two-column anchored third-volume bank `H>G/5`; on the inherited r29 scale this gives `H>F^6/64123518131896320`.
2. Designated partner account02/B07, `QFORM-PAIRTAIL-CURVATURE-RECEIVER-v1`:
   `yspennstate/math-open-problems@3e36370502df5afeb00457b74d05cdbfd87168b0`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T104812Z-account02-B07-qform-r13/REPORT.md`.
   Its actual pair-tail estimate is applied in Section 5.
3. The current required fractional-volume theorem:
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
   It is applied at the actual third-volume inequality in Section 4.

Full QFORM and the full continuity conclusion remain OPEN.

## 2. Exact two-anchor extension identity

Let `M` be an arbitrary real ORIGINAL-coordinate cross block. Fix two physical row anchors `P` and two physical column anchors `Q`. After physical permutations only, write

`M = [[B,U],[V,D]],`                                               (2.1)

where `B` is `2 x 2`, `U` is `2 x q`, `V` is `p x 2`, and `D` is `p x q`. Define the complete fixed-double-pair third-volume bank

`H := sum_(k,l) det M[P union {k}, Q union {l}]^2`,              (2.2)

where `k,l` range over residual physical rows and columns.

### Theorem 2.1 — `QFORM-DOUBLEPAIR-EXTENSION-MATRIX-v1`

With `Delta=det B`,

`boxed: H = || Delta D - V adj(B) U ||_F^2.`                    (2.3)

This identity is valid whether or not `B` is invertible.

#### Proof

For the residual row `k` and residual column `l`, let `v_k^T` be row `k` of `V`, `u_l` column `l` of `U`, and `d_kl` the corresponding entry of `D`. The elementary block determinant expansion gives, without division,

`det [[B,u_l],[v_k^T,d_kl]]
 = (det B)d_kl - v_k^T adj(B)u_l.`                              (2.4)

The matrix on the right of (2.3) has exactly these extension determinants as its entries. Squaring and summing proves (2.3). QED.

This is the correct object for the r22 double-pair survivor: the whole bank is a Frobenius norm before any local inverse appears.

## 3. Dimension-free physical-edge extraction from the entire bank

Put

`x=||B||_F,  u=||U||_F,  v=||V||_F,  d=||D||_F,
 F=||M||_F.`                                                     (3.1)

For every `2 x 2` matrix,

`|det B|<=x^2/2`,
`||adj(B)||_op=||B||_op<=x`.                                   (3.2)

Therefore Theorem 2.1 gives

`sqrt(H)
 <= |det B| d + ||V adj(B)U||_F
 <= (x^2/2)d + xuv
 = x(xd/2+uv).`                                                 (3.3)

By AM-GM,

`uv <= (u^2+v^2)/2`,
`xd/2 <= (x^2+d^2)/4`,                                         (3.4)

hence

`xd/2+uv <= F^2/2`.                                            (3.5)

Thus:

### Theorem 3.1 — `QFORM-DOUBLEPAIR-BANK-FORCES-EDGE-v1`

`boxed: sqrt(H) <= (1/2)||B||_F F^2.`                           (3.6)

Consequently

`boxed: ||B||_F >= 2 sqrt(H)/F^2,`                             (3.7)

and since one of the four entries of `B` has magnitude at least `||B||_F/2`, there is an actual physical cross edge `b` in the fixed anchor core satisfying

`boxed: |b| >= sqrt(H)/F^2.`                                   (3.8)

No individual third-order determinant has been selected, lower-bounded, or reciprocated. The only selection is an entry after the complete determinant bank has forced the Frobenius size of the whole `2 x 2` anchor core.

If

`H >= c F^6`,                                                   (3.9)

then

`boxed: |b| >= sqrt(c) F.`                                     (3.10)

For the live r22 inherited bank,

`c = 1/64123518131896320`,                                     (3.11)

so

`boxed: |b| > F/253226219.2820805.`                            (3.12)

The numerical constant is only a scale ledger; the structural point is the dimension-free linear-in-`F` edge forced by an aggregate order-three bank.

### A cancellation split retained for later receivers

Equation (2.3) also gives the exact positive alternative

`|det B| ||D||_F >= sqrt(H)/2`                                  (3.13)

or

`||V adj(B)U||_F >= sqrt(H)/2`.                                (3.14)

In the second branch,

`||B||_op ||U||_F ||V||_F >= sqrt(H)/2`.                       (3.15)

Thus cancellation of the anchor-determinant-times-core term can only move the currency into a quantitative two-star/anchor-core product; it cannot erase the bank.

### Exact singular-anchor face

If `rank(B)=1`, write `B=s a b^T` with `s=||B||_F` and unit vectors `a,b` in the physical row/column anchor spaces. Let `a_perp,b_perp` be unit orthogonal vectors. Then, up to an irrelevant sign,

`adj(B)=s b_perp a_perp^T`.                                   (3.16)

Since `det B=0`, (2.3) factorizes exactly:

`boxed:
 H = s^2 ||V b_perp||_2^2 ||a_perp^T U||_2^2.`                (3.17)

So an exactly singular physical anchor core is not a zero-information endpoint: its entire extension bank becomes a product of two coefficient-star norms on disjoint ORIGINAL-coordinate residual banks. This is retained as product-provenance currency; a bounded projection density alone is not promoted to a curved quadratic density bound.

## 4. Apply the newest fractional-volume theorem at the actual bank

Because every term in `H` is a physical `3 x 3` minor of `M`,

`E_3(M) >= H.`                                                 (4.1)

Normalize the complete squared third-minor law of `M`. If on either physical side its maximum inclusion marginal is at most `2/3`, the current fractional-volume theorem at `q=4/3` gives a continuous full-ambient density and

`||p_Q||_infinity
 <= (9 sqrt(3)e/2) E_3(M)^(-1/6)
 <= (9 sqrt(3)e/2) H^(-1/6).`                                 (4.2)

Thus for `H>=cF^6`,

`boxed:
 ||p_Q||_infinity
 <= (9 sqrt(3)e/2)c^(-1/6) F^(-1).`                           (4.3)

At the live value (3.11), the coefficient in (4.3) is

`13404.08521084.`                                              (4.4)

This is a genuine application of the newest required volume result to the current fixed-double-pair currency. It is a paid continuous-density exit, not a claim that the marginal gate is automatic.

The remaining geometry may therefore be treated as a high-leverage third-volume state. The next step below does not assume the volume gate.

## 5. Turn the forced edge into a quantitative physical principal-pair alternative

Let the edge from Theorem 3.1 be `b=A_rs`, with `r,s` distinct ORIGINAL coordinates inherited from the disjoint row/column banks. Consider the actual symmetric physical principal pair

`P_b = [[a,b],[b,d]],
 a=A_rr, d=A_ss.`                                               (5.1)

There is an exhaustive elementary split.

### Lemma 5.1 — `QFORM-EDGE-PAIR-DIAGONAL-OR-CONDITIONED-INDEFINITE-v1`

Either

`max(|a|,|d|) >= |b|/2`,                                      (5.2)

or `P_b` is indefinite and

`boxed: |det P_b| >= 3b^2/4,`                                 (5.3)
`boxed: sigma_min(P_b) >= |b|/2.`                              (5.4)

#### Proof

If (5.2) fails, then `|ad|<b^2/4`. Hence

`det P_b=ad-b^2 < -3b^2/4`,                                   (5.5)

so the pair is indefinite and (5.3) holds. Also

`||P_b||_op <= ||P_b||_infinity < 3|b|/2`.                    (5.6)

For an invertible `2 x 2` matrix, the product of the singular values is `|det|`; dividing (5.3) by the larger singular value bounded by (5.6) yields (5.4). QED.

Thus the aggregate determinant bank has forced either a physical diagonal at the same scale as the bank-forced edge, or an actually invertible, uniformly conditioned indefinite physical pair. The latter is exactly the scope of the newest designated-partner result.

## 6. Designated partner account02/B07 applied to an actual inequality

Assume the conditioned-indefinite branch (5.3)-(5.4). Complete the actual pair `P_b` in the full symmetric matrix. Let `C` be any inherited disjoint ORIGINAL-coordinate cross block in its exact Schur remainder, and write

`T_2(C)=sum_(j>=3) s_j(C)^2`.                                  (6.1)

The completed designated-partner theorem `QFORM-PAIRTAIL-CURVATURE-RECEIVER-v1` gives

`||p_Q||_infinity
 <=26.00795741955
   |det P_b|^(-2/5)
   sigma_min(P_b)^(-1/10)
   T_2(C)^(-1/20).`                                            (6.2)

This retains arbitrary same-bank curvature, affine terms, outside couplings, and extra spectrum. It does not require a pre-Schur determinant bank to survive unchanged.

Fix `tau>0`. If

`T_2(C) >= tau b^2`,                                           (6.3)

then (5.3)-(5.4) inserted into (6.2) give

`||p_Q||_infinity
 <=26.00795741955
   (3/4)^(-2/5)(1/2)^(-1/10)
   tau^(-1/20)|b|^(-1).`                                      (6.4)

The numerical prefactor is

`26.00795741955 (3/4)^(-2/5)(1/2)^(-1/10)
 =31.27409417897... .`                                        (6.5)

Using the aggregate edge lower bound (3.8),

`boxed:
 ||p_Q||_infinity
 <=31.274095 tau^(-1/20) F^2/sqrt(H).`                         (6.6)

If `H>=cF^6`, this becomes the correctly scaled full-form estimate

`boxed:
 ||p_Q||_infinity
 <=31.274095 c^(-1/2) tau^(-1/20) F^(-1).`                    (6.7)

For the live `c` in (3.11), the coefficient is

`7.9194206304e9 * tau^(-1/20).`                               (6.8)

At `tau=1/16`, it is approximately

`9.0970254507e9.`                                              (6.9)

The constants are deliberately not optimized. This is the required actual partner application: an aggregate anchored third-volume inequality has been converted, with no reciprocal individual minor, to the exact determinant/singular-value/tail hypotheses of the account02/B07 receiver.

I claim only essential boundedness from this partner branch; continuity is not promoted here because the cited partner result does not state it in this scope.

If (6.3) fails, the exact pair Schur remainder satisfies the quantitative low-tail conclusion

`boxed: T_2(C) < tau b^2,`                                    (6.10)

so `C` lies in a Frobenius rank-two tube of radius `sqrt(tau)|b|`. No nonzero tail has been deleted.

## 7. Main structural conclusion

Combining the preceding steps gives the following source-valid replacement for the previous raw double-pair bank.

### Theorem 7.1 — `QFORM-DOUBLEPAIR-BANK-EDGE-PAIRTAIL-OR-RANK2-v1`

Let an ORIGINAL-coordinate cross block `M` contain a fixed two-row/two-column anchored third-volume bank `H>0`, and put `F=||M||_F`. Then:

1. the complete bank obeys the exact extension identity (2.3);
2. a physical cross edge exists with `|b|>=sqrt(H)/F^2`;
3. for the symmetric physical principal pair on that edge, either
   - a physical diagonal has magnitude at least `|b|/2`, or
   - the pair is indefinite with `|det|>=3b^2/4` and `sigma_min>=|b|/2`;
4. in the latter branch, for the exact post-pair Schur cross block `C` and every `tau>0`, either
   - `T_2(C)>=tau b^2`, in which case the designated partner pays the full form by (6.6), or
   - `T_2(C)<tau b^2`, a genuine rank-two-tube survivor;
5. independently, if the complete third-volume law of `M` satisfies the current `2/3` marginal gate on either side, the newest fractional-volume theorem pays the full form continuously by (4.2).

For the inherited r22/r29 survivor `H>F^6/64123518131896320`, every unpaid branch now carries an actual edge of size `>3.9490381479e-9 F`; the former diffuse double-pair determinant bank cannot remain purely combinatorial.

This is an actual physical-core / low-tail alternative of the kind required by the current B07 assignment. It is not a full solution: the remaining cases are the **large-diagonal principal-pair branch** in (5.2) and the **nonzero rank-two Schur tube** in (6.10), with arbitrary same-bank curvature retained.

## 8. Why the previous one-anchor mixed-order compiler cannot simply be iterated

The r22 exact E3-to-E2 shadow avoids one fixed anchor row but, on a double-row-anchored E3 bank, necessarily keeps the other anchor with inclusion marginal one. Thus the r22 mixed-order Brascamp-Lieb gate cannot directly pay this state: a row marginal equal to one violates the required `p_i<=q/2` with `q<r/2` for the effective order `r<4`.

Using both one-anchor shadows symmetrically does not repair the issue. If the E3 packet has weight `w` and the two order-two shadows share weight `(1-w)/2` each, the effective determinant order is `r=2+w`, while each anchor marginal is `(1+w)/2`. Integrability requires `q<r/2`, hence `q/2<(2+w)/4`, but the gate would require

`(1+w)/2 <= q/2 < (2+w)/4`,                                   (8.1)

which is impossible for every `w>=0`.

So this run deliberately changes mechanism: rather than force another mixed-order shadow, it spends the double-anchor bank through the exact extension matrix (2.3), then through physical edge/pair geometry. This preserves the failed route instead of silently renaming it.

## 9. Numerical regression (not proof)

A deterministic random-matrix check over 20,000 real block matrices of varied residual sizes verified

`H <= (1/4)||B||_F^2 ||M||_F^4`

with zero violations; the largest observed ratio `H / [(1/4)||B||_F^2||M||_F^4]` was approximately `0.6767`. This is only a regression check. The proof is Sections 2-3.

The constants used in the partner splice are:

`1/sqrt(c)=253226219.28208053`,
`C_pair=31.27409417897166`,
`C_pair/sqrt(c)=7919420630.412716`,
`C_pair*(1/16)^(-1/20)/sqrt(c)=9097025450.68467`,
`C_volume=(9sqrt(3)e/2)c^(-1/6)=13404.085210837273`.

## 10. Remaining implication

The first B07 debt is now

`QFORM-LARGE-DIAGONAL-OR-RANK2-SCHUR-TUBE-RECEIVER-v1`:

- in the large-diagonal branch forced by (5.2), exploit the same bank-forced edge without paying a bad reciprocal determinant;
- in the low-tail branch (6.10), retain the nonzero rank-two-tube correction and route the strong rank-two core through an existing product-preserving rank-two affine half-Riesz / grouped-coordinate mechanism.

A useful exact singular-anchor endpoint is already isolated by (3.17). A future receiver must keep the two star banks and the arbitrary remaining curvature together; their bounded joint projection density alone is not enough.

No claim of full QFORM, global continuity, or novelty beyond the exact source-pinned statements above is made.
