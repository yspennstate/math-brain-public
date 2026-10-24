SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-24T05:13:40Z.
attacking: the genuinely rotated indefinite near-coloop collar; quantify exactly how deleting the physical hub spends the spectral gap, then splice the designated account02/B11 Pluecker receiver into an actual same-bank (+,+,-) family.

# account01/B11 r11 — near-coloop spectral-defect ladder

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control at startup: revision `2026-09-22.15`; programme revision `2026-09-22.5`  
Fresh prepublication brain main observed: `d62d140eb28f4060f1901bae51cf7eadf76e13e6`  
Status: **NEW EXACT STRUCTURAL THEOREM / DESIGNATED PARTNER APPLIED / SOURCE-MATCH CORRECTION / FULL QFORM OPEN**  
Continuity: **not proved by the new structural theorem**. The designated partner branch cited below has the regularity stated in its own source; no full-target continuity claim is made.

The unrestricted owner target remains OPEN / NOT PROVED / NOT DISPROVED. No Gaussianity, log-concavity, moments, compact support, connected support, iid hypothesis, post-rotation independence, pointwise law-uniform van-der-Corput decay, arbitrary-joint coarea theorem, conditional-cap-as-independence step, or perturbative deletion of a small coefficient is used.

## 1. Integrity/source-match correction before new work

The interrupted account01/B11 run at

- `yspennstate/math-open-problems@5a4909d3e5c696bc6c23c036b60f04a46784157b`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260924T031514Z-account01-B11-QFORM-auto11/REPORT.md`,

proved an arbitrary-pivot theorem under `rank(A_{-i,-i})<=2` and initially labeled it as a new supporting theorem. That scope is source-matched by the earlier interactive theorem

- `proofnet24/QFORM-density/interactive/20260923T214000Z-all-exact-rank3-physical-coloops/REPORT.md`,

which already proves the entire exact-rank-three physical-spectral-coloop branch. Indeed the low-residual-rank lemma in the interrupted run itself proves `e_i in range(A)`, placing it inside that earlier theorem. Therefore the 03:15 result is retained as a derivation/check but is **not counted as new fleet progress**. The successor below changes mechanism to the non-coloop `q<1` geometry.

## 2. Exact setup: remove one physical near-coloop row

Let

`A=R M R^T`, `R^T R=I_3`,

with `M` real symmetric invertible. Put

`s=min_j |lambda_j(M)|>0`, `D=|det M|`.

Fix one ORIGINAL physical coordinate `h` with spectral leverage

`q=||R^T e_h||^2`, `0<q<1`,

and rotate only the deterministic three-dimensional spectral bookkeeping so

`R^T e_h=sqrt(q)e_1`.

Write

`delta=1-q`,

and delete row `h` from `R`, obtaining `R_-`. Parseval gives the exact residual Gram matrix

`R_-^T R_- = G := diag(delta,1,1)`.                         (2.1)

Define

`W=R_- G^{-1/2}`.                                             (2.2)

Then

`W^T W=I_3`, `R_-=W G^{1/2}`.                              (2.3)

The residual principal block is therefore

`C:=A_{-h,-h}=W B W^T`,

where

`B:=G^{1/2} M G^{1/2}`.                                      (2.4)

Thus the three nonzero singular values of the large physical matrix `C` are exactly those of the `3x3` matrix `B`.

This is a deterministic identity; no law has been rotated or declared independent.

## 3. New theorem — `QFORM-NEARCOLOOP-SPECTRAL-DEFECT-LADDER-v1`

Let

`s_1(C)>=s_2(C)>=s_3(C)>0`

mean the three nonzero singular values of the residual principal block. Then

`boxed: s_1(C) >= s,`                                           (3.1)

`boxed: s_2(C) >= s sqrt(delta),`                               (3.2)

`boxed: s_3(C) >= s delta,`                                    (3.3)

and the residual pseudodeterminant is exactly

`boxed: Delta_3(C)=delta D.`                                   (3.4)

In particular a near-coloop defect `delta=1-q` cannot collapse all residual spectral directions at the same rate: one remains at full scale, a second loses at worst `sqrt(delta)`, and only the weakest direction can lose the full factor `delta`.

### Proof

Equation (3.4) is immediate from (2.4):

`det B = det(G) det(M)=delta det(M)`.

For the singular-value ladder, write

`P=G^{-1/2}=diag(delta^(-1/2),1,1)`, `N=M^{-1}`.

Then

`B^{-1}=P N P`.                                                (3.5)

All singular values of `N` are at most `1/s`, while the singular values of `P` are

`delta^(-1/2),1,1`.

Use the standard singular-value product inequality

`s_{i+j-1}(XY) <= s_i(X)s_j(Y)`                               (3.6)

whenever `i+j-1<=3`.

First,

`s_1(B^{-1}) <= ||P||^2 ||N|| <= delta^(-1)/s`,

so

`s_3(B)>=s delta`.

Next,

`s_2(NP) <= s_1(N)s_2(P) <=1/s`,

and hence

`s_2(B^{-1})=s_2(P(NP)) <= s_1(P)s_2(NP)
 <=delta^(-1/2)/s`.

Therefore

`s_2(B)>=s sqrt(delta)`.

Finally apply (3.6) with `i=j=2` to `P(NP)`:

`s_3(B^{-1}) <= s_2(P)s_2(NP) <=1/s`.

Thus

`s_1(B)>=s`.

Because `W` is an isometric embedding, `C=W B W^T` has exactly the same three nonzero singular values as `B`. This proves (3.1)-(3.4). QED.

### Sharpness of the defect exponents

The powers cannot be improved from the stated hypotheses alone.

- For `M=diag(1,1,-1)`, `B=diag(delta,1,-1)`, so the weakest residual singular value is exactly `delta`.
- For the hyperbolic control

`M=[[0,1,0],[1,0,0],[0,0,1]]`,

`B=[[0,sqrt(delta),0],[sqrt(delta),0,0],[0,0,1]]`,

whose singular values are exactly `1,sqrt(delta),sqrt(delta)`. Hence the middle `sqrt(delta)` scale is attained.

The theorem is sign-free and in particular applies to both indefinite signatures `(2,1)` and `(1,2)`.

## 4. Exact probabilistic normal form attached to the ladder

The same calculation gives an exact source-provenance representation that is useful for the live collar. Let

`Z=W^T X_{-h}`.

Then `Z` is a three-dimensional orthogonal projection of the residual ORIGINAL product source, and it is independent of the literal original coordinate `H=X_h`. Moreover

`R^T X = (sqrt(q)H,0,0)+G^{1/2} Z`
`      = (sqrt(q)H+sqrt(delta)Z_1, Z_2, Z_3)`.                 (4.1)

Thus the full exact-rank-three quadratic is

`Q = (sqrt(q)H+sqrt(delta)Z_1, Z_2,Z_3)^T
      M
     (sqrt(q)H+sqrt(delta)Z_1, Z_2,Z_3)`.                     (4.2)

No coordinates of `Z` are declared independent. The only genuine source separation is `H independent of Z`.

This identity makes the near-coloop limit precise: `delta->0` suppresses only the residual contribution to the first spectral coordinate; it does **not** erase the two transverse product-projection coordinates, and Theorem 3 quantifies the surviving residual curvature.

## 5. Designated account02/B11 result applied to an actual genuinely rotated indefinite family

The fresh designated partner is account02/B11 r12:

- brain handoff commit `2fec8f73a1c8cc72ea36308039fe1fbeb4a7cb64`,
- canonical mathematics `yspennstate/math-open-problems@7a45322747438aa340df490db33a2fb2e1d6d31d`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260924T040707Z-account02-B11-QFORM-r12/REPORT.md`.

Its completed fixed-transverse-Pluecker theorem says that in the exact-rank-three null physical-pivot chamber, if the hub leverage is `q` and the maximum squared transverse Pluecker atom is `omega_*`, then

`||p_Q||_(infinity,ess)
 <=3*2^(2/3)(q omega_* D)^(-1/3)`.                              (5.1)

Apply it to four arbitrary independent cap-one ORIGINAL variables `H,X_1,X_2,X_3`. Define the mutually orthogonal coefficient directions on the three-leaf bank

`T=(X_1+X_2+X_3)/sqrt(3)`,
`Y=(X_1-X_2)/sqrt(2)`,
`V=(X_1+X_2-2X_3)/sqrt(6)`.

These random variables are **not** asserted independent for general product laws. For `q in [63/64,1)` put

`Z_1=sqrt(q)H+sqrt(1-q)T`

and consider

`boxed: Q_q = 2 Z_1 Y + V^2.`                                  (5.2)

The coefficient frame for `(Z_1,Y,V)` is orthonormal in the four ORIGINAL coordinates, and the spectral matrix is

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`.

Hence the corresponding physical matrix has exact nonzero spectrum

`{1,1,-1}`,

so (5.2) is a strict owner-target `(2,1)` family. Its negative is a strict `(1,2)` family.

The physical hub has zero pivot and leverage `q`. For the three residual rows, the transverse coefficient pairs in `(Y,V)` have all three squared Pluecker determinants equal to

`omega_12=omega_13=omega_23=1/3`.

Thus `omega_*=1/3` and `D=1`. Substitution into the designated partner theorem gives the actual all-law inequality

`boxed:
 ||p_(Q_q)||_(infinity,ess)
 <=3*2^(2/3)(3/q)^(1/3)
 <=6.904434991977456
}`                                                                  (5.3)

for every `q>=63/64` and every choice of independent cap-one original-coordinate input laws.

This is genuinely rotated: the same three leaf variables feed `T,Y,V`, and no rotational invariance or post-rotation independence is used.

For this family the residual block has singular values exactly

`1, sqrt(1-q), sqrt(1-q)`.

Thus (5.2) simultaneously exercises the partner's Pluecker mechanism and the middle scale in the new defect ladder.

## 6. The designated partner's listed near-coloop debt is already source-matched by an existing receiver

Account02/B11 r12 lists as unpaid the null-pivot near-coloop form

`2 beta sqrt(q) X_0 C
 +2 beta sqrt(1-q) T C
 +alpha C^2+2 delta_0 C D_0+gamma D_0^2`,                       (6.1)

with `(T,C,D_0)` a genuine three-dimensional orthonormal projection of the residual product source.

That exact implication is already covered by the completed account02/B16 theorem `QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1`, source

`yspennstate/math-open-problems@be8062b160868bcc71aff45a77c56ff2d0501a9a`.

Indeed take the literal fresh scalar `H=X_0`, the receiver variables `(L,V)=(C,D_0)`, and the arbitrary light twist

`T_twist=beta sqrt(1-q) T`.

The two-dimensional product-projection theorem gives the genuine pair cap `M<=2`, while

`gamma_hub=beta sqrt(q)`, `kappa=gamma`,

and

`|gamma_hub^2 kappa|=q |beta^2 gamma|=q |det M|`.

Therefore

`boxed:
 ||p_Q||_(infinity,ess)
 <=3*2^(4/3)(q |det M|)^(-1/3)
 <=3*2^(4/3) q^(-1/3) s^(-1).
}`                                                                  (6.2)

At `q>=63/64` the right side is `<7.60/s`. The same-bank term `TC` is retained exactly; it is absorbed into a translate mixture of the literal original hub law, not deleted or called independent.

This closes that *null-pivot* debt. It does not close the genuinely punctured nonzero-pivot majority-sign collar isolated by account03/B11 r50.

## 7. Rank-two logarithmic benchmark and what the third direction now means

For centered unit uniforms `X,Y`,

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`,                       (7.1)

so the opposite-sign rank-two saddle genuinely has an unbounded density.

The new defect ladder identifies a deterministic version of the missing third direction in a rotated near-coloop frame. After deleting the near-coloop physical row, the three residual singular scales obey

`(s_1,s_2,s_3) >= (s, s sqrt(1-q), s(1-q))`,                   (7.2)

with exact pseudodeterminant `(1-q)D`. Thus the third direction is not lost by rotation; its weakest possible collapse is quantified exactly by the physical leverage defect. In the null-pivot branch, the partner Pluecker receiver converts the surviving two-dimensional transverse area into a bounded output density. In the punctured majority-sign branch, account03/B11 r50 shows the same determinant currency migrates into a volume-one LDL shear instead of disappearing.

## 8. First remaining B11 implication

The first genuinely unpaid B11 step is now the same as the fresh account03/B11 r50 frontier, but with the residual defect geometry made explicit:

`QFORM-DEFECT-LADDER-TO-VOLUME1-LDL-TRACE-v1`.

In the exact-rank-three near-coloop chamber `q>=63/64`, `0<|A_hh|` small, and majority-sign pivot, combine

1. the volume-one LDL form
   `aU^2+gamma Y^2+dV^2`, `gamma d<0`, `a gamma d=det M`;
2. the exact residual defect ladder (3.1)-(3.4);
3. the genuine product characteristic-function factorization of the orthonormal residual frame;

and prove a density bound uniform as `a->0` without taking the known-divergent positive scalar-root majorant. A proof using only a bounded 3D joint density, only X-ray caps, or only a worst conditional cap is excluded by live corrections. The product numerator/factorization must be used before the absolute-value/fiber supremum step.

Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate full-target bridge.

## 9. Verification

A deterministic checker generated 20,000 random indefinite invertible `3x3` matrices with minimum absolute eigenvalue `s>=1`, random `q in (0.5,1)`, formed

`B=diag(sqrt(1-q),1,1) M diag(sqrt(1-q),1,1)`,

and tested (3.1)-(3.4). It recorded

- minimum `s_1(B)/s = 1.0000000323130669`,
- minimum `s_2(B)/(s sqrt(1-q)) = 1.0064242311509404`,
- minimum `s_3(B)/(s(1-q)) = 1.0000922633407252`,
- maximum relative determinant discrepancy `1.9148713492629204e-15`,
- zero violations.

The terminal marker is

`QFORM_B11_DEFECT_LADDER_CHECK_PASS`.

These finite tests are regression checks only; the proof is the exact algebra above.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full continuous-density conclusion: **OPEN**.
