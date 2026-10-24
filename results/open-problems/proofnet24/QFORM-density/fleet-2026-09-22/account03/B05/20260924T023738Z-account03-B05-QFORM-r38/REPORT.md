SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-24T02:37:38Z.
attacking: QFORM-NONSINGULAR-PAIR-ONE-THIRD-COAREA-v1 — remove the last signature split inside the live ratio packet by extending the determinant-only hyperbolic coarea kernel to every nonsingular symmetric scalar pair.

# account03/B05 r38 — determinant-only one-third coarea for every nonsingular scalar pair

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: quadratic coarea / equivalent interval bound preserving arbitrary original-coordinate product densities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING PRODUCT-PRESERVING THEOREM / ALL NONSINGULAR RATIO-PAIR SIGNATURES CLOSED / FULL QFORM OPEN**  
Full-target continuity: **OPEN**. The theorem below proves absolute continuity and an essential density bound in its scope; continuity is not claimed.

## 1. Fresh scope and first missing implication

Fresh owner control was reread before publication at `yspennstate/math-research-brain@c085c00714411980f6de9187a2de70dc1917689f`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The live correction inbox was reread. This run does not use arbitrary-joint rank-three coarea, positive conditional projection-cap moments, independence after rotation, pointwise quadratic van-der-Corput decay, a fiber supremum, compact support, connected support, moments, or a perturbative deletion of small coefficients.

Immediate predecessor:

- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T013705Z-account03-B05-QFORM-r37/REPORT.md`.

It proved the determinant-only one-third coarea kernel for every invertible **indefinite** scalar pair and obtained the affine ratio-packet bound

`||p_Q||_(infinity,ess) < 781 (mu m)^(-1/3)`.

The first remaining scalar-pair question was whether the signature split is intrinsic. It is not: the same coarea/curvature interpolation works for a definite pair. The only change is the sign inside the discriminant; the exact second derivative still has magnitude `D|t|/s^3`, so the same dyadic proof and the same constant survive.

## 2. Main pair theorem

### Theorem `QFORM-NONSINGULAR-PAIR-ONE-THIRD-COAREA-v1`

Let `X,Y` be independent real random variables with probability densities `f,g` satisfying

`||f||_infinity <= L_X`, `||g||_infinity <= L_Y`.

Let

`B=[[a,c],[c,d]]`

be any real symmetric invertible `2x2` matrix, and put

`D=|det B|>0`.

For arbitrary deterministic translations `x_0,y_0`, define

`R=(X+x_0,Y+y_0)^T B (X+x_0,Y+y_0)`.

Then `R` is absolutely continuous. For almost every noncritical output value `t`,

`boxed:
 p_R(t)
 <= C_H (L_X L_Y)^(2/3) (D |t|)^(-1/3),
 C_H=8(3+sqrt(2))<35.314.
`

For a definite pair the output is supported on one half-line after translating the critical value to zero, so the estimate is asserted only on that support. At the critical value the right side is infinite and no pointwise assertion is needed.

The estimate is uniform in the translations, the signature, and the condition number of `B`.

### 2.1 Indefinite case

This is exactly Theorem `QFORM-INDEFINITE-PAIR-ONE-THIRD-COAREA-v1` from r37. There the level roots satisfy

`s(x)^2=D x^2+d t`,
`|partial_y q|=2s`,
`|y''(x)|=D|t|/s^3`,

and a dyadic decomposition in `s` gives on each shell the competing bounds

`A_k <= min{
 L_Y/R_k,
 16 sqrt(2) L_X L_Y^(1/2) R_k^(1/2)(D|t|)^(-1/2)
}`.

Balancing them and summing the geometric tails gives the stated constant.

### 2.2 Positive-definite case: the same curvature identity

Translations preserve independence and density caps, so absorb `x_0,y_0` into the laws. Assume first `B>0`; then `d>0` and

`D=det B=ad-c^2>0`.

Write

`q(x,y)=a x^2+2cxy+d y^2`.

For `t>0`, solve `q(x,y)=t` in the `y` variable. Put

`s(x)=sqrt(d t-D x^2)`,
`Omega_t={x: d t-Dx^2>0}`.

The two roots are

`y_sigma(x)=(-c x+sigma s(x))/d`, `sigma in {+1,-1}`,

and

`partial_y q(x,y_sigma(x))=2 sigma s(x)`.

Hence for almost every `t>0`, the root/coarea formula gives

`p_R(t)
 =sum_sigma int_(Omega_t)
   f(x)g(y_sigma(x))[2s(x)]^(-1) dx.                    (2.1)`

Differentiate `s^2=dt-Dx^2`. One gets

`s'(x)=-D x/s(x)`,
`s''(x)=-D d t/s(x)^3`.

Therefore

`boxed:
 y_sigma''(x)=-sigma D t/s(x)^3.                       (2.2)`

The factor `d` cancels exactly. This is the same determinant-only curvature law as in the indefinite case.

### 2.3 Dyadic shell estimate

Choose `R_0>0`, put `R_k=2^k R_0`, and

`E_k={x in Omega_t: R_k<=s(x)<2R_k}`.

Each `E_k` is a union of at most two intervals. On every component and for each root branch, (2.2) has fixed sign and

`|y_sigma''(x)|>=D t/(8R_k^3)`.                         (2.3)

The same monotone-derivative composition lemma as in r37 says: if a probability density `g` has cap `L` and `phi''` has fixed sign with `|phi''|>=lambda`, then

`int_J g(phi(x))dx <=4 sqrt(L/lambda)`.                 (2.4)

Using only `g<=L_Y`, `s>=R_k`, and total mass of `f`, the shell mass estimate is

`A_k<=L_Y/R_k`.                                          (2.5)

Using (2.4), `f<=L_X`, at most two components, two roots, and `s>=R_k`, the curvature estimate is

`A_k
 <=16sqrt(2)L_X L_Y^(1/2)
   R_k^(1/2)(D t)^(-1/2)`.                              (2.6)

Thus (2.5)-(2.6) are literally the r37 shell bounds. Choose `R_0` so they agree at `k=0`. Their common value is

`T=8(L_XL_Y)^(2/3)(Dt)^(-1/3)`.                         (2.7)

For `k>=0`, sum the mass bound to get `2T`; for `k<0`, sum the curvature bound to get `(1+sqrt(2))T`. Empty shells above the maximum possible value of `s` only improve the estimate. Therefore

`p_R(t)
 <=(3+sqrt(2))T
 =8(3+sqrt(2))(L_XL_Y)^(2/3)(Dt)^(-1/3)`.               (2.8)

For `t<0` a positive-definite form has no mass. A negative-definite pair is reduced to the preceding case by replacing `B` and the output by their negatives.

### 2.4 Absolute continuity

A nonsingular quadratic pair has a unique critical point after translation. The independent product law is absolutely continuous, so that point has probability zero. The root formula constructs a density away from the critical value; deleting a ball about the critical point and shrinking it to zero shows there is no singular mass at the critical value. Thus the full pushforward is absolutely continuous.

This completes the proof for every nonsingular symmetric `2x2` pair.

## 3. Environment splice, now signature-free

### Corollary `QFORM-NONSINGULAR-PAIR-ONE-THIRD-SCHUR-v1`

Let `E` be an arbitrary environment. Let `Y,Z` be independent of each other and independent of `E`, with density caps `L_Y,L_Z`. Let `B` be any fixed invertible symmetric `2x2` matrix with `D=|det B|`. Let `h(E)` be an arbitrary measurable translation vector, and suppose a real random variable `T(E)` satisfies uniformly in `u` and `rho>0`

`P(|T-u|<rho)<=min(1,H sqrt(rho)).`                    (3.1)

Then

`Q=T(E)+[Y,Z+h(E)]^T B [Y,Z+h(E)]`

has an essentially bounded density satisfying

`boxed:
 ||p_Q||_(infinity,ess)
 <=3 C_H (L_YL_Z)^(2/3) D^(-1/3) H^(2/3).             (3.2)`

Proof: condition on `E`, use the translation-uniform pair envelope, and average `|u-T|^(-1/3)`. The layer-cake calculation from (3.1) gives exactly

`sup_u E|T-u|^(-1/3)<=3H^(2/3)`.                       (3.3)

No conditional density of a dependent projection is introduced.

## 4. Application to the live affine ratio packet: every invertible B

Use the live ratio packet

`Q=V^T C V+2V^T P W+W^T B W
   +ell_V^T V+ell_W^T W+q_0`,

where `V=(S,R)` is a two-dimensional projection of one original-coordinate product bank, while `W=(Y,Z)` consists of two normalized scalar projections on disjoint original-coordinate banks, independent of each other and of `V`, with

`L_Y,L_Z<=sqrt(2)`.

Assume only that `B` is invertible and

`C-PB^(-1)P^T=lambda m e_1e_1^T`,
`mu=|det B| |lambda|`.

Completing the scalar pair gives

`Q=[W+h(V)]^T B[W+h(V)]+T(V)`,

where exactly

`T(V)=lambda m S^2+b^T V+q_1`.                       (4.1)

The source-valid rank-one affine small-ball theorem gives

`P(|T-u|<rho)
 <=min(1,10 sqrt(rho/(|lambda|m))).                    (4.2)`

Therefore, in Corollary (3.2),

`H=10/sqrt(|lambda|m)`,
`D=|det B|`,
`(L_YL_Z)^(2/3)<=2^(2/3)`.

It follows that, for **either signature** of an invertible `B`,

`boxed:
 ||p_Q||_(infinity,ess)
 <= C_RP (mu m)^(-1/3),
 C_RP=3*20^(2/3)*8(3+sqrt(2))
     =780.580886664... <781.
}                                                        (4.3)`

For the standard ratio packet `m>=3/20`,

`boxed:
 ||p_Q||_(infinity,ess)
 <1469.110 mu^(-1/3)
 <1470 mu^(-1/3).
}                                                        (4.4)`

Consequently every standard ratio packet with `mu>=1` and **any invertible scalar pair B** has the numerical universal branch bound `<1470`.

The new point is not the numerical constant. It is that signature, condition number, raw diagonals, scalar-bank leverage, and the ratio residual all disappear from this receiver. The same determinant product `mu m` is the only scalar-pair currency.

## 5. Designated partner account04/B05 applied to an actual inequality

Fresh designated-partner source:

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260924T011830Z-account04-B05-convex-pair-r3/REPORT.md`, theorem `QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1`.

For an actual original-coordinate pair with definite principal block `C` and cap-one coordinates it proves

`P(Q in I)<=pi |det C|^(-1/2)|I|`,
`||p_Q||_(infinity,ess)<=pi |det C|^(-1/2)`.             (5.1)

Apply it at the literal-scalar endpoint of the same ratio packet: if `q_Y=q_Z=1`, the normalized scalar projections are literal independent original coordinates up to signs. When their physical block `B` is definite,

`boxed:
 ||p_Q||_(infinity,ess)<=pi |det B|^(-1/2).
}                                                        (5.2)`

Thus, on the concrete branch `|det B|>=1/4`,

`boxed:
 ||p_Q||_(infinity,ess)<=2pi<6.284.
}                                                        (5.3)`

This is a strict sharp-type convex companion to the signature-free one-third estimate. The partner theorem is used only in its exact literal-coordinate scope; no post-rotation independence is inferred.

## 6. What this removes and what remains

The r37 signature split is now unnecessary. Once the upstream reduction produces a ratio packet with

`m>=3/20`, `mu>=1`, `det B!=0`,

the entire packet is paid by (4.4), regardless of whether `B` is definite or indefinite. Future B05 work should not reintroduce a sign split, `sigma_min(B)`, a raw diagonal, a scalar tail, or a collar assumption inside this branch.

The exact remaining factor is now upstream/degenerate rather than pair-coarea:

`QFORM-RATIOPACKET-NONSINGULAR-GLOBAL-COMPILER-v2`:

> prove that every hard three-large-eigenvalue configuration either yields a standard ratio packet with `mu` bounded below and `det B!=0`, enters an already-completed exact-slope/crossing/definite-physical-pair branch, or lands in one of the genuinely singular zero-pivot / isotropic-shear survivors already isolated by the fleet.

If this compiler fails, the obstruction must be quantified as collapse of `mu` or `det B=0`; it is no longer hidden in the signature or conditioning geometry of a nonsingular scalar pair.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**. This theorem establishes absolute continuity and essential boundedness only in the stated nonsingular-pair scope.

## 7. Source pins

- Fresh owner/control head before publication: `yspennstate/math-research-brain@c085c00714411980f6de9187a2de70dc1917689f`, OWNER CONTROL revision `2026-09-22.15`.
- Immediate predecessor: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T013705Z-account03-B05-QFORM-r37/REPORT.md`.
- Ratio-packet reduction: `proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T033640Z-account01-B05-QFORM-r26/REPORT.md`.
- Rank-one affine small-ball source: `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
- Designated partner: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260924T011830Z-account04-B05-convex-pair-r3/REPORT.md`.

Repository transport is not native learned-memory ingestion. `full_brain_connected=false` and execution remains `WITHOUT_VERIFIED_BRAIN`.
