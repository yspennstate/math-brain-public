SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T07:25:49Z.
attacking: replace the rotated SVD packet in the double-nested survivor by an actual-original-coordinate crisscross chain, then perform a Desnanot-Jacobi degree drop to an anchored E2 bank or two one-pivot minor stars.

# fleet03/B08 r31 — actual crisscross chain and Desnanot-Jacobi degree drop

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / quantitative inequalities  
**Run:** `20260923T072549Z-fleet03-B08-qform-diffuse-r31`  
**Classification:** `NEW SUPPORTING STRUCTURAL THEOREMS + NEW CLEAN CONTINUOUS ENDPOINT / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Scope, source pins, and corrections

The full target remains OPEN: for every dimension, independent real ORIGINAL coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `Q=X^T A X`, or give a valid counterexample. Continuity is tracked separately.

No Gaussian, moment, compact-support, connected-support, log-concavity, post-rotation independence, pointwise law-uniform Fresnel decay, arbitrary-joint coarea bound, positive conditional projection-height moment, worst-fiber supremum, or one-good-minor selector is used below. In particular, the physical-minor banks below are aggregated before any reciprocal operation.

Fresh owner control was read from `yspennstate/math-research-brain` main and remained revision `2026-09-22.15`, QFORM only. The live correction set was refreshed before publication. The argument explicitly respects the hidden-shear correction: the exterior/Dodgson quantities below are deterministic identities for the ACTUAL physical cross block and are not called the true Schur complement of the full quadratic form.

Immediate predecessor:

`yspennstate/math-open-problems@3ae967e80c1d47013c756555785a38aa0aeca199`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T064830Z-fleet03-B08-qform-diffuse-r30/REPORT.md`.

Completed compatible fleet04 result actually applied below:

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.

That source gives, for any coefficient vector `u` on an original-coordinate cap-one product bank,

`||p_(u^T X)||_infinity <= sqrt(2)/||u||_2`.                    (1.1)

The designated `fleet04/B08` current-QFORM handoff directory was still absent on the fresh check, so no partner output is fabricated. The completed compatible B18 theorem is the fleet04 result actually used.

A second completed theorem used for the scoped clean endpoint is fleet03/B07 `QFORM-TWO-DISJOINT-PRODUCT-DENSITY-v1`:

`yspennstate/math-open-problems@2357dd6b61a8d631b6fca2d63e998b27585c8f21`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T221112Z-fleet03-B07-qform-r18/REPORT.md`.

## 2. Incoming r30 state

Use r30's strict-higher-rank double-nested survivor. Thus an ACTUAL original-coordinate cross block is partitioned

`B = [ C  R ]`
`    [ S  N ]`,                                                  (2.1)

where `C` is `2x2`, `R` contains the two fixed anchor rows and residual columns, `S` contains residual rows and the two fixed anchor columns, and `N` is the residual cross block.

The fixed double-nested third-volume is

`D = sum_(r,c) det B[{i,k,r},{a,b,c}]^2`                         (2.2)

and satisfies

`boxed: D > L^6/16875.`                                         (2.3)

The four full physical anchor stars obey

`R_i,R_k,C_a,C_b <= L`.                                         (2.4)

The determinant-times-residual-core branch from r30 has already been separated. This report treats the complementary aligned branch

`||S adj(C) R||_F > sqrt(D)/2.`                                  (2.5)

Since `16875=75^2*3`, (2.3) gives the exact useful form

`boxed: sqrt(D) > L^3/(75 sqrt(3)).}`                            (2.6)

## 3. Actual-coordinate crisscross extraction

For `p,q in {1,2}`, let

`s_p = S e_p`, `r_q = R^T e_q`.                                 (3.1)

Then

`S adj(C) R = sum_(p,q) adj(C)_(p,q) s_p r_q^T`.                 (3.2)

Each summand is rank one and has Frobenius norm

`|adj(C)_(p,q)| ||s_p||_2 ||r_q||_2`.                           (3.3)

By the triangle inequality and (2.5), some pair `(p,q)` obeys

`|adj(C)_(p,q)| ||s_p||_2 ||r_q||_2 > sqrt(D)/8.`                (3.4)

For a `2x2` matrix, `adj(C)_(p,q)` is, up to sign, the complementary ACTUAL entry `C_(bar q,bar p)`. Define

`a := C_(bar q,bar p)`,
`g := ||s_p||_2`,
`h := ||r_q||_2`.                                                (3.5)

The full-star bounds (2.4) imply

`|a|<=L`, `g<=L`, `h<=L`.                                       (3.6)

Combining (2.6) and (3.4),

`boxed: |a| g h > L^3/(600 sqrt(3)).}`                           (3.7)

Since each of the other two factors is at most `L`, every factor is individually nontrivial:

`boxed:
 |a|, g, h > L/(600 sqrt(3)).
`                                                                    (3.8)

### Theorem 3.1 — `QFORM-DOUBLE-NEST-ACTUAL-CRISSCROSS-v1`

The r30 aligned double-nest survivor therefore contains an **actual physical crisscross chain**: one original-coordinate cross coefficient `a`, one complete residual star attached to the opposite anchor column, and one complete residual star attached to the opposite anchor row, with product reserve (3.7) and individual floors (3.8).

No anchor rotation is used. This strictly strengthens the provenance of the r30 SVD packet, which only produced two rotated anchor directions.

## 4. Actual application of fleet04 mathematics

Define the residual linear projections

`Y = s_p^T X_(I_res)`,
`Z = r_q^T X_(J_res)`.                                          (4.1)

Their source banks are disjoint ORIGINAL coordinate sets, hence `Y` and `Z` are genuinely independent. Apply fleet04/B18's product-projection theorem (1.1):

`||p_Y||_infinity <= sqrt(2)/g`,
`||p_Z||_infinity <= sqrt(2)/h`.                                (4.2)

Therefore

`||p_(Y,Z)||_infinity <= 2/(gh).`                               (4.3)

Using `|a|<=L` in (3.7),

`gh > L^2/(600 sqrt(3))`,                                       (4.4)

so the actual inequality is

`boxed:
 ||p_(Y,Z)||_infinity < 1200 sqrt(3)/L^2
 =2078.460969082653.../L^2.
`                                                                    (4.5)

This is retained as product-linear provenance currency. It is not promoted to a generic indefinite quadratic-pushforward bound.

## 5. A paid clean crisscross endpoint

There is one immediate nonlinear endpoint that is now completely paid. Suppose that, after conditioning only on genuinely disjoint outside original-coordinate blocks, the four star groups from (4.1) enter the remaining expression through

`2 X_(J,p) Y + 2 X_(I,q) Z`                                    (5.1)

up to separate affine translations of the two displayed products and an additive random term independent of these four groups. In particular, no same-bank quadratic curvature or residual cross-core coupling still involves these four groups.

Normalize

`U=Y/g`, `V=Z/h`.                                                (5.2)

By (4.2), `U,V` have density caps at most `sqrt(2)`. The completed two-disjoint-product theorem from fleet03/B07 then gives a continuous `C_0` density with

`||p||_infinity <= 2 sqrt(2) (gh)^(-1/2).`                      (5.3)

Using (4.4),

`boxed:
 ||p||_infinity
 < 2 sqrt(2) sqrt(600 sqrt(3))/L
 =91.180282278191.../L
 <92/L.
`                                                                    (5.4)

Convolution with the independent additive term cannot increase the sup norm. This is a scoped endpoint only; the general aligned branch still has arbitrary same-bank curvature and unused couplings and is not claimed paid by (5.4).

## 6. Desnanot-Jacobi degree drop around the actual physical pivot

Relabel the two anchor rows and columns so that the actual pivot `a` from Section 3 is the upper-left entry of `C`. Write

`C = [[a,b],[c0,d]]`,                                           (6.1)

and for a residual column `j` and residual row `r`, write

`R[:,j]=[x_j,y_j]^T`,
`S[r,:]=[s_r,t_r]`,
`N_(r,j)=n_(r,j)`.                                               (6.2)

Let

`delta = a d - b c0`,                                           (6.3)

and define the ACTUAL anchored order-two minors

`W_(r,j) = a n_(r,j) - s_r x_j`,                                (6.4)

`U_j = a y_j - c0 x_j`,                                        (6.5)

`V_r = a t_r - b s_r`.                                         (6.6)

Thus `W_(r,j)` is the `2x2` minor using the pivot row, residual row, pivot column and residual column; `U_j` and `V_r` are the two corresponding one-sided anchored `2x2` minor stars.

For the anchored `3x3` determinant

`d_(r,j)=det [[a,b,x_j],[c0,d,y_j],[s_r,t_r,n_(r,j)]],`         (6.7)

Desnanot-Jacobi (equivalently direct expansion) gives the exact identity

`boxed:
 a d_(r,j) = delta W_(r,j) - U_j V_r.
`                                                                    (6.8)

Summing squares over all residual rows and columns yields

### Theorem 6.1 — `QFORM-DOUBLE-NEST-DODGSON-DROP-v1`

`boxed:
 a^2 D = ||delta W - V U^T||_F^2.
`                                                                    (6.9)

This is again an exterior identity for the ACTUAL cross block, not a statement about the true full-matrix quadratic Schur complement.

By the triangle inequality,

`|a| sqrt(D) <= |delta| ||W||_F + ||U||_2 ||V||_2.`             (6.10)

Using (2.6) and the physical pivot floor (3.8),

`|a| sqrt(D)/2 > L^4/270000.`                                   (6.11)

Hence one of two exhaustive alternatives holds.

### A. Anchored order-two bank

`|delta| ||W||_F > L^4/270000.`                                 (6.12)

Both anchor rows have full cross-star norm at most `L`, so Hadamard gives

`|delta|<=L^2`.                                                  (6.13)

Therefore

`boxed:
 ||W||_F > L^2/270000,
 sum_(r,j) W_(r,j)^2 > L^4/270000^2.
`                                                                    (6.14)

The second quantity is a genuine aggregate bank of ACTUAL physical `2x2` minors of `B`, all sharing the actual pivot row/column. Thus the aligned double-nest has been lowered from order three to explicit anchored `E_2` currency without selecting one minor.

### B. Two one-pivot minor stars

`||U||_2 ||V||_2 > L^4/270000.`                                (6.15)

Normalize only the coefficient vectors, not the random variables, by the actual pivot:

`u_hat=U/a`, `v_hat=V/a`.                                       (6.16)

Since `|a|<=L`,

`boxed:
 ||u_hat||_2 ||v_hat||_2 > L^2/270000.
`                                                                    (6.17)

The vectors have the explicit original-coordinate formulas

`u_hat_j = y_j-(c0/a)x_j`,
`v_hat_r = t_r-(b/a)s_r`.                                       (6.18)

No input-coordinate shear is performed. They are simply coefficient vectors on two disjoint ORIGINAL residual banks. Applying fleet04/B18 once more gives

`boxed:
 ||p_(u_hat^T X_(J_res), v_hat^T X_(I_res))||_infinity
 < 540000/L^2.
`                                                                    (6.19)

Again, (6.19) is product-linear currency, not by itself a curved-pushforward theorem.

## 7. What has changed in the B08 proof tree

The r30 aligned branch is no longer left at an SVD statement involving rotated anchor directions. It now has a completely original-coordinate router:

1. an actual physical crisscross chain with `|a|gh>L^3/(600sqrt(3))` and each factor `>L/(600sqrt(3))`;
2. an immediate clean continuous endpoint `<92/L` when the two star products are separated from same-bank curvature;
3. otherwise an exact Dodgson degree drop forcing either
   - an anchored physical `E_2` bank of squared mass `>L^4/270000^2`, or
   - two opposite one-pivot minor stars whose normalized product is `>L^2/270000` and whose two original-bank projections have joint density `<540000/L^2`.

The first unpaid implication is therefore narrower than r30's generic aligned curved receiver:

`QFORM-DODGSON-E2-OR-TWOSTAR-CURVATURE-RECEIVER-v1` — consume the anchored order-two bank (6.14), or the two one-pivot minor-star resource (6.17), while retaining arbitrary same-bank curvature and all unused couplings. The already completed aggregate-E2, physical-pair, ridge, and two-product mechanisms are natural candidate receivers, but no unsupported splice is asserted here.

The unrestricted conjecture remains OPEN. Global continuity remains OPEN; continuity is proved only for the clean crisscross endpoint (5.4) and previously paid subbranches.

## 8. Verification

A finite exact-arithmetic regression check verified (6.8) on 1,000 seeded integer `3x3` matrices. The constants are

`sqrt(D)/L^3 > 1/(75sqrt(3)) = 0.00769800358919501...`,

`|a|/L, g/L, h/L > 1/(600sqrt(3)) = 0.000962250448649376...`,

`L^(-4) * [|a|sqrt(D)/2] > 1/270000 = 3.703703703703704e-6`,

`1200sqrt(3)=2078.460969082653...`,

`2sqrt(2)sqrt(600sqrt(3))=91.180282278191...`.

The checker terminates `QFORM_B08_R31_CHECK_PASS`.

Repository transport occurred; verified native brain ingestion did not. Status remains `WITHOUT_VERIFIED_BRAIN`.
