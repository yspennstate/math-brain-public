# account01/B05 — weighted scalar-fiber supremum still loses the essential transport

**Run:** `20260922T182410Z-account01-B05-qform15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound  
**Classification:** `ESSENTIAL_ROUTE_CORRECTION / REFUTED_INTERMEDIATE_MECHANISM / PRECISE MISSING FACTOR IDENTIFIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Conditional end-to-end route and implication tested

The full target is unchanged: for independent real coordinates with probability densities at most one and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal bound on the essential density of `Q=X^TAX`, or give a target-valid counterexample. Continuity is tracked separately.

A natural repair of the now-refuted worst scalar-fiber bound is to retain the scalar-fiber probability weight. If

`Q=Q_3+Q'`,

then exactly

`p_Q(y)=int p_{Q'}(b) p_{Q_3|Q'=b}(y-b) db`.

After account03/B05 proved that `sup_b ||p_{Q_3|Q'=b}||_infinity` can diverge, the first plausible weighted replacement is

`int p_{Q'}(b) ||p_{Q_3|Q'=b}||_infinity db <= C`.                    (1.1)

If (1.1) held universally, it would again imply the full density bound. This report proves that (1.1) is also false inside the exact QFORM input class. In fact a single valid four-dimensional product law makes the left side infinite. The failure is not a QFORM counterexample: the peaks occur at different translated output locations. The new precise missing factor is therefore **peak-location transport across the scalar fibers**. A successful coarea argument must retain `y-b` inside the conditional density until after the `b`-integration.

The construction refines account03/B05 `QFORM-SCALAR-CONDITIONED-CORE-SUP-FALSE-v1`, canonical source

`yspennstate/math-open-problems@30ed85cae72f1ddc2d7f3d20de47f82369ec60dd`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260922T181101Z-account03-B05-QFORM-r14/REPORT.md`.

The assigned partner account02/B05 theorem is applied quantitatively in Section 7; its canonical source is

`yspennstate/math-open-problems@e74a5d8fabe1c914be1ca2d3689a2cd65ba58f5a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T155206Z-b05-qform-779c4c9b/REPORT.md`.

## 2. Fixed target matrix and one product source

Use the orthonormal basis of `R^4`

`v=(1,1,1,1)/2`,

`t=(3,-1,-1,-1)/sqrt(12)`,

`u=(0,1,-1,0)/sqrt(2)`,

`w=(0,1,1,-2)/sqrt(6)`.

Define

`Z=v dot X`, `T=t dot X`, `U=u dot X`, `W=w dot X`,

`Q_3=T^2+U^2-W^2`, `Q'=Z^2`.

Then

`Q=Q_3+Q'=X^T A X`, `A=I_4-2ww^T`,

and the spectrum of `A` is exactly `{1,1,1,-1}`. Thus this is a full target matrix.

Choose an integer `K` so large that, for every `k>=K`,

`40/[log k (log log k)^2] < 1/64`,                                  (2.1)

and

`log( log k (log log k)^2 /2560 ) >= (1/2) log log k`.                (2.2)

Also enlarge `K` so that the convergent tail below has total mass below `1/2`. Put

`a_k = 1/[k log k (log log k)^2]`, `k>=K`.                            (2.3)

Let

`L=1-sum_{k=K}^infinity a_k >1/2`,

`I_k=[10k,10k+a_k]`,

`E=[0,L] union union_{k=K}^infinity I_k`.                             (2.4)

The set `E` has Lebesgue measure exactly one. Take independent variables

`f_1=1_E`, `f_2=f_3=f_4=1_[0,1]`.

Every input density is a probability density bounded by one. There are no moment, convex-support, log-concavity or diagonal-basis assumptions.

## 3. Exact scalar fibers

Set `S=X_2+X_3+X_4`. With planar coordinates

`U=(X_2-X_3)/sqrt(2)`,

`W=(X_2+X_3-2X_4)/sqrt(6)`,

one has

`dX_2 dX_3 dX_4=(1/sqrt(3)) dS dU dW`.

Because `Z=(X_1+S)/2`, at fixed `z` the joint density in `(x,U,W,z)` is

`(2/sqrt(3)) 1_{x in E} 1_{(U,W) in D_{2z-x}}`,                      (3.1)

where `D_s` is the planar image of the cube section `X_2+X_3+X_4=s`.

For each tail packet define

`c_k=10k+a_k/2`, `z_k=(c_k+3/2)/2`,

`J_k=[z_k-1/32,z_k+1/32]`.                                            (3.2)

The intervals `J_k` are pairwise disjoint. If `z in J_k` and `x=c_k+d in I_k`, then

`S=2z-x=3/2+2(z-z_k)-d`,

so, for our large `K`,

`11/8 <= S <=13/8`.                                                    (3.3)

For every other tail packet and for the filler interval `[0,L]`, `2z-x` lies outside `[0,3]`; the packet spacing by ten makes this immediate. Thus only `I_k` contributes on `J_k`.

Let `r=1/8` and `R=[-r,r]^2`. From the inverse cube-section formulas, (3.3) implies

`R subset D_S`                                                        (3.4)

uniformly in `z in J_k` and `x in I_k`.

## 4. Hyperbolic coarea kernel and an essential-supremum lower bound

Define

`K_R(h)=int_R delta(h-(U^2-W^2)) dU dW`.

Under `alpha=U-W`, `beta=U+W`, the Jacobian is `1/2`, and the diamond image of `R` contains `[-r,r]^2`. Hence, for `0<|h|<r^2`,

`K_R(h) >= log(r^2/|h|)`.                                             (4.1)

Also

`T=(2x-z)/sqrt(3)`.

Put

`T_0(z)=(2c_k-z)/sqrt(3)`.

For `x=c_k+d`, `|d|<=a_k/2`, and our large `K`,

`|T^2-T_0^2| <= 4|T_0||d|/sqrt(3)+4d^2/3 <=20 k a_k`.                 (4.2)

Now take any `q` satisfying

`|q-T_0(z)^2| <= k a_k`.                                              (4.3)

Then, uniformly for all `x in I_k`,

`|q-T(x,z)^2| <=21 k a_k <40 k a_k <r^2`.                            (4.4)

Thus (4.1) gives, apart from null roots where the kernel is larger,

`K_R(q-T(x,z)^2) >= log(1/(2560 k a_k))`.                            (4.5)

Let `r_*(q,z)` denote the joint density of `(Q_3,Z)`. Restricting (3.1) to the common square (3.4) gives, for almost every `z in J_k` and almost every `q` in the positive-length interval (4.3),

`r_*(q,z)`

` >= (2/sqrt(3)) int_{I_k} K_R(q-T(x,z)^2) dx`

` >= (2/sqrt(3)) a_k log( 1/(2560 k a_k) )`.                         (4.6)

Because (4.6) holds on a nontrivial interval of `q`, all subsequent lower bounds concern the **essential supremum**, not a chosen pointwise representative of a density.

## 5. Weighted conditional supremum is infinite

Let

`M(z)=||p_{Q_3|Z=z}||_infinity`.

Since `r_*(q,z)=p_Z(z)p_{Q_3|Z=z}(q)`, (4.6) implies

`p_Z(z) M(z) >= (2/sqrt(3)) a_k log(1/(2560 k a_k))`                  (5.1)

for almost every `z in J_k`. Integrating over `J_k`, whose length is `1/16`, gives

`int_{J_k} p_Z(z)M(z) dz`

` >= a_k/(8sqrt(3)) log(1/(2560 k a_k))`.                            (5.2)

All physical coordinates are nonnegative and `Z>0` almost surely. The map `z -> b=z^2=Q'` is one-to-one almost surely, so regular conditioning by `Q'=b` agrees almost everywhere with regular conditioning by `Z=sqrt(b)`. Therefore

`E ||p_{Q_3|Q'}||_infinity = int p_Z(z)M(z) dz`.                      (5.3)

The `J_k` are disjoint. Summing (5.2) over every `k>=K` and using (2.2)-(2.3),

`E ||p_{Q_3|Q'}||_infinity`

` >= 1/(16sqrt(3)) sum_{k=K}^infinity 1/[k log k log log k]`

` = infinity`.                                                        (5.4)

Consequently

`boxed( E ||p_{Q_3|Q'}||_infinity = infinity. )`                      (5.5)

This disproves any universal estimate of the form (1.1), already for one `n=4` product law and one fixed matrix with spectrum `{1,1,1,-1}`.

## 6. Why this is not a counterexample to the QFORM conjecture

The exact mixture is

`p_Q(y)=int p_{Q'}(b)p_{Q_3|Q'=b}(y-b) db`.

The invalid mixed-norm step replaces the translated evaluation at one common output `y` by a separate supremum inside every fiber. In this construction the large conditional peaks move apart with the packet index.

At the center `z=z_k`, writing `c=c_k`,

`z_k=(c+3/2)/2`,

`T_0(z_k)=(3c-3/2)/(2sqrt(3))`,

and therefore the corresponding full-output center is exactly

`T_0(z_k)^2+z_k^2 = c^2+3/4`.                                        (6.1)

Thus successive tail packets place their logarithmic conditional peaks at macroscopically different full-output values. Formula (5.5) diverges precisely because it discards this transport before mixing.

So the missing factor is not merely the scalar-fiber probability mass. It is the **joint control of fiber mass, curved trace, and translated peak location**.

A viable scalar-coarea target must control directly

`sup_y int p_{Q'}(b) p_{Q_3|Q'=b}(y-b) db`,                           (6.2)

using original-product provenance before any `sup` is moved through the integral.

## 7. Assigned partner result applied to an actual inequality

The completed account02/B05 theorem `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1` states that if independent cap-one inputs and row vectors `a_j in R^2` satisfy `sum a_j a_j^T=I_2`, then the two-dimensional projection has density at most `e`.

Here `t,u,w` are orthonormal coefficient vectors. Hence, for each of the pairs `(T,U)`, `(T,W)`, `(U,W)`, the physical row vectors satisfy the Parseval identity. The partner theorem gives

`boxed( ||p_{T,U}||_infinity <=e,  ||p_{T,W}||_infinity <=e,  ||p_{U,W}||_infinity <=e. )`    (7.1)

Therefore (5.5) persists even though **every two-dimensional spectral marginal of the rank-three core is universally bounded by the assigned partner theorem**. The obstruction is genuinely in the scalar-conditioned curved trace/translation, not in pair-projection concentration.

As a consistency check only, this same matrix has the indefinite physical principal pair on coordinates `(2,4)`

`B=[[2/3,2/3],[2/3,-1/3]]`,

whose eigenvalues are `1,-2/3`, so `D=|det B|=2/3`, `kappa=sigma_min(B)=2/3`, while `s_3(A)=1`. The current programme's full-matrix pair theorem therefore supplies a separate uniform full-output bound `<27.1` for this family. This supporting theorem is not needed for (5.5); it simply confirms that the construction attacks the proof interface rather than furnishing a QFORM counterexample.

## 8. Precise next implication

The first unpaid B05 implication is now

`QFORM-TRANSLATED-WEIGHTED-SCALAR-FIBER-TRACE-v1`:

> prove a dimension-free bound on the actual translated mixture (6.2), or on an equivalent unnormalized coarea expression, while preserving the original product-source geometry and without replacing it by either `sup_b` or `int p_{Q'}(b) sup_q`.

Any successful inequality must use the coupling between the scalar level `b` and the location in the rank-three quadratic output. The construction above is a mandatory stress test.

## 9. Status

Proved in this report:

1. a single target-valid four-dimensional product law with a fixed matrix of spectrum `{1,1,1,-1}`;
2. the rigorous essential-supremum divergence `E||p_{Q_3|Q'}||_infinity=infinity` in (5.5);
3. exact identification of peak-location transport as the factor lost by the weighted conditional-sup route;
4. direct application of account02/B05 giving the three pair-density bounds (7.1).

Not proved:

- unboundedness of the actual density of `Q`;
- the full QFORM theorem;
- the desired continuity conclusion.

**Full QFORM: OPEN / NOT PROVED. Continuity: NOT PROVED.**
