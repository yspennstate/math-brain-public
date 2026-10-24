SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T07:10:28Z.
attacking: the punctured indefinite collar by a two-chart original-coordinate Jacobian estimate: force the rank-two logarithmic singular set to be simultaneously transverse in two coarea charts, without conditioning away product provenance.

# account03/B11 r52 — two-chart Jacobian product bound in the punctured indefinite rank-three model

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: genuinely rotated indefinite signatures `(2,1)` and `(1,2)`  
Status: **NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: **not proved by this run**.

The unrestricted owner conjecture remains OPEN / NOT PROVED / NOT DISPROVED. This report proves a puncture-uniform two-chart Jacobian theorem for the exact-rank-three near-null normal form. It does not add Gaussianity, log-concavity, moments, bounded or connected support, iid assumptions, or independence after rotation. It does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea bound, conditional-density-supremum shortcut, or X-ray-only two-sheet claim.

## 1. Source state and inherited normal form

Fresh owner control is QFORM-only, OWNER CONTROL revision `2026-09-22.15`. The live source still marks the full theorem and full continuous-density conclusion open. Relevant corrections retained here include: law-uniform pointwise quadratic-phase decay is false; general rotations do not preserve independence; bounded projection density alone does not control an indefinite quadratic pushforward; naive fiber-supremum integration can lose dimension; arbitrary bounded joint density does not satisfy the proposed rank-three coarea height bound; X-ray control alone does not bound the minority-sign two-sheet trace.

The immediate mathematical input is the exact null-puncture normal form proved in account03/B11 r45/r47. Let `H` be one literal ORIGINAL input coordinate, independent of the residual original-coordinate product bank. Let `(T,W,V)` be an orthonormal three-dimensional projection of that residual bank. For deterministic numbers

`a = kappa sqrt(q)`, `b = kappa sqrt(1-q)`, `a^2+b^2=kappa^2`,

and arbitrary real `eta,delta`, put

`V' = V+eta W`, `S=aH+bT`.

The active quadratic polynomial is exactly

`Q = 2 W S + c (V')^2 + delta W^2`,                         (1.1)

with `c != 0` and the spectral determinant identity

`kappa^2 |c| = |det M| =: D`.                               (1.2)

If `s=min_j |lambda_j(M)|`, then `D>=s^3`. The signs of `c` and the original inertia play no role in the estimates below, so the theorem covers both `(2,1)` and `(1,2)`.

The already-proved first coarea chart is the map

`F_W=(W,Q)`.

Its full ORIGINAL-coordinate two-Jacobian is

`J_W := |grad W wedge grad Q|`

and r47 proved the exact identity

`J_W^2 = 4[kappa^2 W^2+c^2(V')^2]`.                         (1.3)

This makes the rank-two singular line into a codimension-two point in the `(W,V')` chart and yields `E[J_W^{-1}]<=sqrt(2pi)/s`, but one reciprocal-Jacobian moment alone does not control the fiber trace.

This run adds a second transverse chart and proves a joint reciprocal-product estimate.

## 2. Second exact coarea chart

Let

`F_V=(V',Q)`,
`J_V := |grad V' wedge grad Q|`.

Write `t,w,v` for the orthonormal coefficient vectors of `(T,W,V)` in the residual ORIGINAL-coordinate space, and `e_H` for the literal hub coordinate. The coefficient vector of `S` is

`svec = a e_H+b t`,

so

`|svec|=kappa`, `svec perp w`, `svec perp v`.                 (2.1)

Also

`grad V'=v+eta w`.                                            (2.2)

Differentiating (1.1),

`grad Q = 2W svec +2S w +2cV'(v+eta w)+2delta W w`.          (2.3)

Wedging with `grad V'` kills the square term. Thus

`grad V' wedge grad Q
 =2W (v+eta w) wedge svec
  +2(S+delta W)(v+eta w) wedge w`.                            (2.4)

The two displayed two-forms are orthogonal because `svec` is orthogonal to both `w` and `v+eta w`. Their squared norms are

`|(v+eta w) wedge svec|^2=(1+eta^2)kappa^2`,
`|(v+eta w) wedge w|^2=1`.                                   (2.5)

Therefore:

### Theorem 2.1 — `QFORM-PUNCTURE-SECOND-TWOJACOBIAN-v1`

Pointwise,

`boxed: J_V^2
 =4[(1+eta^2)kappa^2 W^2+(S+delta W)^2].`                    (2.6)

In particular,

`J_V >= 2 sqrt(kappa^2 W^2+(S+delta W)^2)`.                  (2.7)

This identity is again uniform in the puncture `q`: only the invariant `kappa=sqrt(a^2+b^2)` appears.

## 3. Product-projection density in the correct three variables

Define normalized active coordinates

`X = kappa W`,
`Y = c V'`,
`Z = S+delta W`.                                              (3.1)

The coefficient vectors of `(S/kappa,V',W)` are a determinant-one shear of an orthonormal triple:

- `svec/kappa` is a unit vector orthogonal to `v,w`;
- `(V',W)=(V+eta W,W)` is a determinant-one shear of `(V,W)`.

Hence the completed three-dimensional product-projection theorem used in r50 gives

`||p_(S/kappa,V',W)||_infinity <= 2^(3/2)`.                  (3.2)

After scaling `S` by `kappa`,

`||p_(S,V',W)||_infinity <= 2^(3/2)/kappa`.                  (3.3)

The linear map `(S,V',W)->(Z,Y,X)` has determinant magnitude `kappa |c|`. Therefore

`boxed: ||p_(X,Y,Z)||_infinity
 <= 2^(3/2)/(kappa^2 |c|)
 = 2^(3/2)/D
 <= 2^(3/2)/s^3.`                                            (3.4)

This is only an input to the integrated Jacobian estimate below. It is NOT used as an arbitrary-joint coarea theorem.

Equations (1.3), (2.7), (3.1) give

`J_W = 2 sqrt(X^2+Y^2)`,                                     (3.5)

`J_V >= 2 sqrt(X^2+Z^2)`.                                   (3.6)

So the simultaneous singularity is the origin in the full three-dimensional `(X,Y,Z)` active coordinate space.

## 4. Exact superlevel volume of the two-chart reciprocal kernel

Set

`G(x,y,z)=1/[sqrt(x^2+y^2) sqrt(x^2+z^2)]`.                  (4.1)

The high-level sets of this kernel have finite volume, unlike the rank-two reciprocal `1/|x|` strip.

### Lemma 4.1 — exact hyperbolic-cylinder volume

For every `lambda>0`,

`|{G>lambda}| = C_* lambda^(-3/2)`,                           (4.2)

where

`C_* = (2pi/3)[Gamma(1/4)/Gamma(3/4)]^2
     = 18.333828848054324...`.                                (4.3)

#### Proof

Homogeneity gives the `lambda^(-3/2)` scaling, so it suffices to compute `lambda=1`. Away from the null set `x=0`, put

`y=xu`, `z=xv`.

The Jacobian is `|x|^2`, while

`(x^2+y^2)(x^2+z^2)
 =x^4(1+u^2)(1+v^2)`.                                        (4.4)

Thus for fixed `(u,v)` the allowed interval is

`|x|<[(1+u^2)(1+v^2)]^(-1/4)=:L(u,v)`.                       (4.5)

Consequently

`|{G>1}|
 = int_R2 [int_-L^L x^2 dx] du dv
 = (2/3)[int_R (1+u^2)^(-3/4) du]^2`.                        (4.6)

The beta integral gives

`int_R (1+u^2)^(-3/4) du
 = sqrt(pi) Gamma(1/4)/Gamma(3/4)`,                           (4.7)

which proves (4.3). QED.

### Lemma 4.2 — capped-density reciprocal-product estimate

If a probability density `h` on `R^3` satisfies `h<=K`, then

`boxed: E_h G <= 3(C_* K)^(2/3).`                             (4.8)

Indeed

`P_h(G>lambda)<=min(1,K C_* lambda^(-3/2))`.                 (4.9)

With `lambda_0=(KC_*)^(2/3)`, layer cake gives

`E G
 <= lambda_0 + K C_* int_(lambda_0)^infinity lambda^(-3/2) dlambda
 =3(KC_*)^(2/3)`.                                             (4.10)

## 5. Main new theorem: simultaneous two-chart reciprocal budget

Combine (3.5)-(3.6) with Lemma 4.2.

### Theorem 5.1 — `QFORM-PUNCTURE-TWOCHART-JACOBIAN-PRODUCT-v1`

In the exact punctured product model (1.1),

`boxed:
 E[1/(J_W J_V)]
 <= (3/2) C_*^(2/3) D^(-2/3)
 <= C_2 s^(-2),`                                              (5.1)

where

`C_2=(3/2)C_*^(2/3)
   =10.429417208172787...`.                                   (5.2)

#### Proof

By (3.5)-(3.6),

`1/(J_W J_V)
 <= (1/4) G(X,Y,Z)`.                                          (5.3)

By (3.4), `(X,Y,Z)` has density cap

`K<=2^(3/2)/D`.                                                (5.4)

Lemma 4.2 yields

`E[1/(J_WJ_V)]
 <=(3/4)(C_* 2^(3/2)/D)^(2/3)
 =(3/2)C_*^(2/3)D^(-2/3)`.                                   (5.5)

Finally `D>=s^3`. QED.

The estimate is uniform as `q->1`, as the puncture coefficient `b=kappa sqrt(1-q)` vanishes, and for either indefinite signature. It also permits arbitrary `eta` and `delta`; the `eta` contribution only increases the second Jacobian.

## 6. A quantitative simultaneous-small-Jacobian tail

The same variables give a useful codimension-three tail estimate. If `J_W<=u` and `J_V<=v`, then

`X^2+Y^2 <= (u/2)^2`,
`X^2+Z^2 <= (v/2)^2`.                                         (6.1)

For radii `r=u/2`, `t=v/2`, the intersection of the two perpendicular cylinders has volume

`int_{|x|<=min(r,t)}
  4 sqrt(r^2-x^2)sqrt(t^2-x^2) dx`.                           (6.2)

If `r<=t`, bounding the second square root by `t` and using the semicircle integral gives at most `2pi t r^2`; the other ordering is symmetric. Therefore

`volume <= (pi/4) min(u^2 v,u v^2)`.                          (6.3)

With (3.4):

`boxed:
 P{J_W<=u, J_V<=v}
 <= min{1,
         (pi/sqrt(2)) s^(-3) min(u^2v,uv^2)}.`                (6.4)

Thus the rank-two logarithmic degeneracy cannot persist simultaneously in both natural coarea charts except in a genuinely codimension-three product-projection tube.

## 7. Designated account04/B11 result applied at an actual inequality

The completed account04/B11 theorem `QFORM-SPECTRAL-SCHUR-PSEUDODET-v1` states, for exact rank three and a nonzero literal physical pivot `alpha=A_hh` of spectral leverage `q_h`, that

`Delta_2(S_h)=q_h D/|alpha|`.                                 (7.1)

In the B11 heavy-row coordinates of r50, `alpha=q a`. Hence the partner theorem gives the exact equality

`boxed: Delta_2(S_h)=D/|a|=|gamma d|`.                        (7.2)

On the live near-coloop collar

`q>=63/64`, `0<|A_hh|<=s/64`,                                (7.3)

we have

`|a|=|A_hh|/q <= s/63`.                                       (7.4)

Since `D>=s^3`, the partner identity yields the actual quantitative inequality

`boxed: Delta_2(S_h)=|gamma d| >=63 s^2.`                     (7.5)

This confirms that the rank-two opposite-sign Schur curvature becomes stronger, not weaker, as the physical pivot closes. The new two-chart theorem spends the complementary third-direction determinant through `D= kappa^2|c|` and shows that the two natural Jacobian singular sets are jointly integrable with a universal `s^-2` budget.

## 8. Rank-two logarithmic control and interpretation

The mandatory two-direction control remains exact. If `X,Y` are independent centered unit uniforms, then for `0<|z|<1/2`,

`p_(2XY)(z)=log(1/(2|z|))`.                                   (8.1)

At rank two the relevant Jacobian is proportional to `|W|`; its reciprocal has the logarithmic divergence `int dw/|w|`.

The third direction now has two compatible quantitative manifestations:

1. r47: in the `(W,Q)` chart it adds `c^2(V')^2`, changing the singular set from a line to the point `(W,V')=(0,0)`;
2. this run: in the transverse `(V',Q)` chart, the remaining direction appears as `(S+delta W)^2`, so simultaneous degeneration requires `(W,V',S+delta W)=(0,0,0)`.

The exact superlevel exponent `3/2` in (4.2) is the quantitative dimension gain: the reciprocal product of the two chart Jacobians is integrable under the product-projection density cap. This is a direct, puncture-uniform mathematical expression of how the third direction destroys the rank-two logarithmic geometry.

## 9. What remains unpaid

The theorem above is an integrated two-chart estimate, not yet a bounded-density theorem. The live counterexamples prevent the invalid step

`integrated reciprocal Jacobian budget => uniform fiber trace`

for an arbitrary joint law. A valid closure must use the ORIGINAL product factorization before taking a worst fiber or a pointwise reciprocal minor.

The next exact B11 implication is therefore

`QFORM-TWOCHART-PRODUCT-TRACE-COMPILER-v1`:

> For the genuine product-projection law in (1.1), combine the two exact charts `(W,Q)` and `(V',Q)`, the simultaneous tail (6.4), and the original-coordinate characteristic-function / Brascamp-Lieb factorization to prove `P{Q in I}<=C |I|/s` uniformly through the puncture.

A proof may not replace the product projection by an arbitrary bounded 3D density, may not rely on X-ray control alone, and may not delete the small nonzero overlap. The existing r49 cancellation example shows why the provenance hypothesis must enter the final trace step.

Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate bridge to the full owner theorem. No new full-target continuity claim is made here.

## 10. Verification plan

The companion verifier checks on random orthonormal coefficient frames and random admissible parameters:

- the exact second-Jacobian identity (2.6) by Gram determinants;
- the inherited first-Jacobian identity (1.3);
- the linear-map determinant `kappa|c|` in (3.4);
- the analytic constant `C_*` and final constant `C_2`;
- numerical Monte Carlo sampling of the geometric superlevel volume only as a regression for the exact formula, not as proof.

The proof itself is analytic; numerical checks are not used to infer universality.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full continuous-density conclusion: **OPEN**.
