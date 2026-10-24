# r42 addendum — physical-unit-shear bank E2 or slope-mismatch compiler

Status: **NEW SUPPORTING LEMMA / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

This addendum strengthens the exact-singular overlap-two branch in `REPORT.md` by returning from the determinant-equivalent renormalized frame to a **unit-Jacobian shear of the literal physical pair source**. The purpose is to expose which part of the tau-cancelled determinant packet can be consumed by a future dependence-safe analytic receiver without pretending that a non-unit coefficient normalization preserves the input density cap.

All coordinate indices below are original coordinates. No random variable is spectrally rotated and no independence after a rotation is asserted.

## 1. Incoming exact-singular data

Use the same exact-singular physical pair `H={h,h'}` as in r40b/r41/r42. Write, after ordering the pair so that the larger literal diagonal is first,

`B=A[H,H]=[[a,c],[c,b]]=tau ell ell^T`,

with `|a|>=|tau|/2>0`. Let the two physical outside-coupling columns be

`u=A[O,h]`, `v=A[O,h']`, `O=H^c`.

Put

`kappa=c/a`,
`w=v-kappa u`.

Because `B` has rank one,

`b=a kappa^2`.                                                     (1.1)

If `x=X_h`, `y=X_h'`, and `z=X_O`, then the pair and pair-to-outside terms admit the exact source-level identity

`a x^2+2cxy+b y^2+2x<u,z>+2y<v,z>`
` = a (x+kappa y)^2 +2(x+kappa y)<u,z>+2y<w,z>.`                  (1.2)

The map `(x,y)->(L,y)=(x+kappa y,y)` has determinant one. Hence the transformed pair source has joint density

`g(L,y)=f_h(L-kappa y)f_h'(y)<=1`,                                (1.3)

and remains source-disjoint from all outside variables. The two transformed pair coordinates need not be independent; no such claim is used.

Let `D_H` be the bordered-minor matrix from r39-r42. If `ell=(ell_1,ell_2)` in the chosen pair order and `k=(-ell_2,ell_1)`, then

`q=Uk=ell_1 w`, `a=tau ell_1^2`,

so the exact singular-star identity becomes the **literal physical-pivot identity**

`boxed: D_H=-a w w^T.`                                            (1.4)

Also the unit-determinant column shear `[u,v] -> [u,w]` preserves every physical 2x2 minor:

`det [[u_r,v_r],[u_s,v_s]] = det [[u_r,w_r],[u_s,w_s]]`.          (1.5)

Thus

`E2(U)=sum_{r<s}(u_r w_s-w_r u_s)^2`.                             (1.6)

The completed r40b/r41 inequalities give

`|a| ||w||^2=||D_H||op >=7/96`,                                  (1.7)

`max_r w_r^2/||w||^2 <1/7`,                                      (1.8)

and on the forced pair-to-outside third-resource branch

`|tau| E2(U)>6727/393216`.

Since `|a|>=|tau|/2`,

`boxed: |a| E2(U)>6727/786432.`                                  (1.9)

## 2. A better balanced physical cut for the unit shear

For a cut `O=R disjoint_union S`, put

`P_R=||w_R||^2/||w||^2`,

`E_RS=sum_{r in R,s in S}(u_r w_s-w_r u_s)^2`.                    (2.1)

Choose each outside coordinate independently into `R` with probability `1/2`. Then

`E E_RS=(1/2)E2(U)`.                                              (2.2)

By (1.8),

`Var(P_R)=(1/4)sum_r (w_r^2/||w||^2)^2 <1/28`.                    (2.3)

Take the rational balance threshold `eta=3/20`. Chebyshev gives

`P(P_R notin (3/20,17/20))
 < (1/28)/(7/20)^2 =100/343`.                                     (2.4)

Since always `0<=E_RS<=E2(U)`, the good cuts have aggregate expectation

`E[E_RS 1_good]
 > (1/2-100/343)E2(U)
 = (143/686)E2(U).`                                               (2.5)

Hence one literal physical partition satisfies simultaneously

`boxed: 3/20<P_R<17/20`,                                         (2.6)

`boxed: E_RS>(143/686)E2(U).`                                    (2.7)

Multiplying (2.7) by (1.9),

`boxed:
 |a| E_RS
 >137423/77070336
 =0.00178308551814... .
}`                                                                 (2.8)

On the same cut, (1.4) gives

`||D_H[R,S]||op
 =|a| ||w_R|| ||w_S||
 =(|a|||w||^2) sqrt(P_R(1-P_R))`
` > (7/96) sqrt((3/20)(17/20))`
` =7 sqrt(51)/1920`
` =0.0260364578124... .`                                          (2.9)

This improves the preceding safe same-cut star constant while keeping the cut attached to the literal unit-Jacobian physical-pair shear.

## 3. Exact three-term decomposition of the determinant packet

Because (2.6) makes both `w_R,w_S` nonzero, define the physical-bank regression coefficients

`alpha_R=<u_R,w_R>/||w_R||^2`,
`alpha_S=<u_S,w_S>/||w_S||^2`,                                   (3.1)

and orthogonal residuals

`r=u_R-alpha_R w_R`, `r perpendicular w_R`,
`s=u_S-alpha_S w_S`, `s perpendicular w_S`.                      (3.2)

The cross-cut matrix of physical 2x2 minors is

`M_RS=u_R w_S^T-w_R u_S^T`.

Substituting (3.2),

`M_RS=(alpha_R-alpha_S)w_Rw_S^T+r w_S^T-w_R s^T`.                (3.3)

The three matrices on the right are pairwise Frobenius-orthogonal. Therefore

`boxed:
 E_RS
 =(alpha_R-alpha_S)^2 ||w_R||^2||w_S||^2
  +||r||^2||w_S||^2
  +||w_R||^2||s||^2.
}`                                                                 (3.4)

This identity is exact and is the main new structural step of this addendum.

Also, because replacing `v` by `w=v-kappa u` is a unit determinant column shear,

`E2([u_R,v_R])=E2([u_R,w_R])=||w_R||^2||r||^2`,                  (3.5)

and analogously on `S`.

## 4. Main dichotomy — internal physical E2 or source-bank slope mismatch

### Theorem — `QFORM-EXACTSINGULAR-PHYSICAL-SHEAR-E2-OR-SLOPE-MISMATCH-v1`

On the exact-singular cross-E2 branch above there is a literal physical cut `O=R disjoint_union S` satisfying (2.6), (2.8), (2.9), and at least one of the following three alternatives.

**(R-internal E2)**

`boxed:
 |a| E2(A[R,H])
 >137423/1310195712
 =0.000104887383420... .
}`                                                                 (4.1)

**(S-internal E2)** the same bound with `R` replaced by `S`:

`boxed:
 |a| E2(A[S,H])
 >137423/1310195712.
}`                                                                 (4.2)

**(two-bank slope mismatch)**

`boxed:
 |a| (alpha_R-alpha_S)^2 ||w_R||^2||w_S||^2
 >137423/231211008
 =0.000594361839381... .
}`                                                                 (4.3)

In all cases the same cut simultaneously retains (2.9).

#### Proof

By (3.4), at least one of its three nonnegative summands exceeds `E_RS/3`. Multiplying by `|a|` and using (2.8), each winning summand is larger than

`137423/231211008`.                                                (4.4)

If the second term wins, (2.6) implies

`||w_R||^2/||w_S||^2 > (3/20)/(17/20)=3/17`.

Using (3.5),

`|a|E2(A[R,H])
 =|a| ||w_R||^2||r||^2`
` >(3/17)*(137423/231211008)`
` =137423/1310195712`,                                            (4.5)

which is (4.1). The third term gives (4.2) symmetrically. If the first term wins, (4.3) is exactly (4.4). QED.

The meaning of (4.3) is source-compatible. On each disjoint physical bank, the rank-one part of the pair-to-bank coefficient matrix points in the pair-coordinate direction `(alpha_R,1)` or `(alpha_S,1)`. Their determinant is `alpha_R-alpha_S`. Thus if neither bank itself carries a quantitative two-minor packet, two **source-disjoint physical banks** carry quantitatively mismatched pair-source directions. No transformed random variables are declared independent.

## 5. Designated account02/B07 theorem applied to the new internal branch

The latest completed designated partner result used here remains

`yspennstate/math-open-problems@ec29bb4321feffe020e5cb0185d148f2f6de847e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260924T013622Z-account02-B07-qform-auto11/REPORT.md`.

Its theorem `QFORM-E2-BOUNDED-SUPPORT-BALANCE-v1` states

`E2(K)<=(rank(K)-1)s2(K)^2||K||F^2`.                              (5.1)

On either internal branch (4.1) or (4.2), the actual physical two-column block `K_bank=A[bank,H]` has rank two. Applying (5.1) gives the equation-level consequence

`boxed:
 sqrt(|a|) s2(K_bank)||K_bank||F
 >sqrt(137423/1310195712)
 =0.0102414541653... .
}`                                                                 (5.2)

If a literal `m`-row subcore `J` of that winning bank carries at least half of its internal `E2` packet and all entries of `A[J,H]` have modulus at most `L0`, the partner's bounded-entry consequence gives

`boxed:
 s2(A[J,H])
 >0.00512072708 /(sqrt(m|a|) L0).
}`                                                                 (5.3)

No bounded core is inferred when the determinant packet is support-diffuse; that would contradict the partner stress example.

## 6. Why this is a mechanism change and what remains

The previous exact-singular runs built aggregate determinant currencies and balanced renormalized coefficient frames. This addendum changes mechanism on the same target: it performs a **literal unit-Jacobian physical-pair shear** and decomposes the same-cut determinant law into bank-internal two-volume versus a two-bank slope mismatch.

This is closer to an analytic receiver because (1.3) preserves an actual two-dimensional source density cap, while alternatives (4.1)--(4.3) live on disjoint original-coordinate banks. Nevertheless arbitrary same-bank and between-bank quadratic curvature is still present. It is not legitimate to delete that curvature, condition on a rotated complement, or apply the clean two-bank hyperbolic receiver as though its source-separation hypotheses had already been proved.

The next precise B07 implication is

`QFORM-PHYSICAL-SHEAR-INTERNAL-E2-OR-MISMATCH-RECEIVER-v1`:

* on (4.1)/(4.2), spend the physical scalar coefficient `a`, a bank-internal `E2` packet of size `~1/|a|`, and the retained bordered-minor star jointly, before a worst-slice square bound;
* on (4.3), spend the two source-disjoint slope directions while retaining arbitrary residual curvature and the same nonzero star.

The near-singular invertible-pair collar and r39 anchored-`E4` branch remain separate obligations.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**.