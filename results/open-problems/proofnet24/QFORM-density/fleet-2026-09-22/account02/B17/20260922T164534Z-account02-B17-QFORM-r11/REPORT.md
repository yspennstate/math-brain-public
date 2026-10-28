# account02/B17 — conditional 3D-cap obstruction and a stronger shared-frame finite witness

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T164534Z-account02-B17-QFORM-r11`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `SUPPORTING_RESULT / REFUTED_INTERMEDIATE_BRIDGE + EXACT_ROTATED_WITNESS`  
**Full quadratic-form conjecture:** **OPEN / NOT PROVED**  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`

## 1. Current target and source pins

The target is unchanged: for every dimension, independent real inputs with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal dimension-free essential-density bound for `X^T A X`, or give a valid target-level counterexample.



`p(0)=91/36+(13/6)log 2 = 4.0295966689909926...`.

The live correction set was consumed. In particular this run does not use pointwise oscillatory decay, conditional cap preservation after sum/difference changes, rotated-coordinate independence, one-minor/cross-rank extraction, fiberwise trace suprema, or fixed-fragment reductions.

## 2. Exact target source refuting a uniform conditional 3D projection cap

Let `X_1,...,X_4` be iid `Uniform[-1/2,1/2]`; their joint density is exactly one on the unit four-cube. Define the orthogonal Hadamard coordinates

```
Y1 = ( X1 + X2 - X3 - X4)/2,
Y2 = ( X1 - X2 + X3 - X4)/2,
Y3 = ( X1 - X2 - X3 + X4)/2,
Z  = ( X1 + X2 + X3 + X4)/2.
```

Let `H` be this `4 x 4` orthogonal matrix and let

`Q = Y1^2 + Y2^2 - Y3^2`.

In the original independent coordinates its matrix is

```
A = (1/4) [[ 1,  1,  1, -3],
           [ 1,  1, -3,  1],
           [ 1, -3,  1,  1],
           [-3,  1,  1,  1]].
```

Because `A=H^T diag(1,1,-1,0) H`, its spectrum is exactly `{1,1,-1,0}`. Hence this is an honest instance of the full target, with no moment or rotation-independence assumption.

The orthogonal change of variables has Jacobian one, so the joint density `p_{Y,Z}` is exactly the indicator of a rotated unit cube. In particular its value is one throughout the interior of its support.

For `z in [1/2,1]`, the marginal density of `Z` is explicit. If `S=X1+X2+X3+X4`, then on `s in [1,2]`

`f_S(s)=(2-s)^3/6`,

by the upper Irwin--Hall simplex formula. Since `Z=S/2`,

`f_Z(z)=2 f_S(2z)=(8/3)(1-z)^3`.                         (2.1)

For every such `z` with positive slice volume, the regular conditional density of the active projection is

`p_{Y|Z=z}(y)=1_{(y,z) in H[-1/2,1/2]^4}/f_Z(z)`.

Therefore

`||p_{Y|Z=z}||_infinity = 1/f_Z(z) = 3/[8(1-z)^3] -> infinity`

as `z` increases to `1`. Thus:

### Theorem `QFORM-CONDITIONAL-3D-PROJECTION-CAP-FALSE-v1`

There is **no universal finite M** such that, for every cap-one product law and every orthogonal split into three active spectral coordinates `Y` and the complementary coordinates `Z`, the conditional density satisfies

`||p_{Y|Z=z}||_infinity <= M`

for almost every conditioning value `z`.

This remains false even for iid centered unit intervals and for a physical matrix whose nonzero spectrum is exactly `{1,1,-1}`.

This theorem refutes only the proposed conditional-projection bridge. It is **not** a counterexample to the quadratic-form density conjecture.

## 3. What survives: do not normalize thin fibers

The calculation also identifies the precise lost factor. Write the unnormalized slice density

`g_z(y)=p_{Y,Z}(y,z)`.

If a valid rank-three curved-trace estimate is applied at the joint-slice level, conditioning and then multiplying back by `f_Z(z)` cancels the dangerous denominator:

`f_Z(z) ||p_{Y|Z=z}||_infinity = ||g_z||_infinity`.       (3.1)

For the present Hadamard cube, `||g_z||_infinity=1` whenever the slice is nonempty and the `z` support has length two. Thus this particular source pays the finite joint-slice quantity `int ||g_z||_infinity dz = 2`, despite the unbounded conditional cap.

Equation (3.1) is only a repair principle for the failed normalization step, not a universal theorem. Existing cube-projection/fiber corrections show that a raw integrated fiber supremum can itself lose dimension. A full proof must therefore combine rank-three curved integration with original product provenance before or jointly with fiber normalization; it cannot demand a pointwise conditional projection cap.

## 4. Stronger finite shared-frame witness than the partner pair rotation

The partner theorem closes disjoint active supports and explicitly recommends stressing shared-coordinate active frames. The following exact six-variable construction does so and raises the finite peak above the partner's `4.029596...`, although it remains below the established `3 sqrt(2)` asymptotic lower bound.

Let `X_1,...,X_6` again be iid `Uniform[-1/2,1/2]` and put

`S1=X1+X2`, `S2=X3+X4`, `S3=X5+X6`.

The `S_j` are independent with triangular density

`tau(s)=(1-|s|)_+`.

Set `n=(1,1,1)/sqrt(3)` and

`M=I-2nn^T`.

Then `M` has eigenvalues `{1,1,-1}`. Define

`Q_bal=(1/2) S^T M S`.

If `B` is the three-by-six pair-sum matrix, then `R=B^T/sqrt(2)` has orthonormal columns and the physical matrix is

`A=R M R^T=(1/2) B^T M B`,

so the nonzero physical spectrum is exactly `{1,1,-1}`.

Choose the orthonormal basis

`u=(2,-1,-1)/sqrt(6)`, `v=(0,1,-1)/sqrt(2)`, `n=(1,1,1)/sqrt(3)`.

The zero cone of `Q_bal` has sheets

`S=r a_+(theta)` and `S=r a_-(theta)`,

where

`a_±(theta)=u cos(theta)+v sin(theta) ± n`.

For `b_i=|a_i|`, `M_theta=max_i b_i`, the radial coarea integral is elementary:

`J(theta)=1/M_theta - e1/(2 M_theta^2) + e2/(3 M_theta^3) - e3/(4 M_theta^4)`,

where `e_k` are the elementary symmetric functions of the three `b_i`. Both sheets have the same integral. Symmetry reduces the full cone to

`p_Qbal(0)=12 [ int_0^(pi/12) J_+(theta)dtheta + int_(pi/12)^(pi/3) J_-(theta)dtheta ]`.       (4.1)

On this sector, with

```
a1 = sqrt(2/3) cos(theta) + 1/sqrt(3),
a2 = -cos(theta)/sqrt(6) + sin(theta)/sqrt(2) + 1/sqrt(3),
a3 = -cos(theta)/sqrt(6) - sin(theta)/sqrt(2) + 1/sqrt(3),
```

`a1` is the maximal absolute coordinate; `a3` changes sign exactly at `pi/12`. Thus

`J_± = 1/(2a1) - (a2+|a3|)/(6a1^2) + a2|a3|/(12a1^3)`.

With `t=tan(theta/2)`, every term is rational and has an elementary antiderivative. The checker records the closed-form primitive and independently re-integrates the cone numerically. The exact elementary expression evaluates to

`p_Qbal(0)=4.06307061680603726012548442259349995675...`.      (4.2)

For comparison, the designated partner's exact rotated witness is

`91/36+(13/6)log 2 = 4.02959666899099261484844737427049...`,

so the new shared-frame construction gains

`0.0334739478150446452770370483230063...`.

However

`3 sqrt(2)-p_Qbal(0)=0.179570070313247886279581750035594... > 0`.

Therefore this is a strictly stronger **finite rotated stress witness**, but it does not improve the current target-level lower bound `C >= 3 sqrt(2)` and does not refute boundedness.

## 5. Consequence for the proof mechanism

Two currently attractive simplifications are now separated sharply:

1. **Disjoint active banks** are controlled by the completed account03/B17 theorem (`<=2*pi`).
2. **Condition on the complementary spectral coordinates and ask for a pointwise 3D density cap** is false, already for the four-dimensional Hadamard cube above.

The remaining full-target bridge must retain the unnormalized product mass through the rank-three curved trace, or else use a product-preserving grouped/ridge reduction that never divides by arbitrarily small slice mass. On the witness side, the new six-variable value shows that finite shared spectral loading can raise a rotated peak, but the best source-valid lower-bound mechanism still remains the diffuse `3 sqrt(2)` family.

A next sharp-witness attack should therefore stress at least two interacting macroscopic physical rows together with a diffuse residual, especially off-center levels, rather than repeat disjoint banks or one-heavy-row central limits.

## 6. Verification scope

`CHECK.py` performs exact rational checks of the Hadamard orthogonality and target matrix, verifies the explicit tail density (2.1), and checks the divergence of the conditional cap. It also evaluates the elementary antiderivative behind (4.1), independently quadratures both cone sheets, and checks

`p_Qbal(0) > 91/36+(13/6)log 2`

and

`p_Qbal(0) < 3 sqrt(2)`.

The checker supports algebra and exact source construction. It is not a proof of the unrestricted conjecture.
