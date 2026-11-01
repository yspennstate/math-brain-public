# fleet03/B05 r20 — aggregate three-arm coarea with a diffuse bilinear core

Run: `20260923T014000Z-fleet03-B05-QFORM-r20`

Status: **ESSENTIAL_STEP_APPLIED / SUPPORTING COAREA THEOREM / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN**.

## 1. Scope and target

The full target remains: for independent real coordinates with densities bounded by one and a real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal output-density bound for `Q=X^T A X`, or give a valid counterexample. This report does not solve the full target. It proves a dimension-free coarea receiver that pays a diffuse bilinear core by its Frobenius norm, without selecting a singular direction, and identifies precisely what prevents immediate application to the current four-bank T4 survivor: same-side quadratic curvature on the smoothing side.

No moment, support, log-concavity, post-rotation independence, Gaussianity, or compactness assumption is used.

## 2. A linear-image small-ball corollary at Hilbert--Schmidt scale

### Lemma 2.1 (`QFORM-HS-LINEAR-SMALLBALL-v1`)

There is a universal finite constant `C_HS` such that the following holds. Let `Z=(Z_1,...,Z_N)` have independent real coordinates with densities bounded by one. For every nonzero real matrix `D` and every `rho>0`,

```
sup_z P( ||D Z-z||_2 <= rho )
    <= min(1, C_HS rho/||D||_HS).
```

#### Proof

Put `F=||D||_HS`, `s=||D||_op`, and

```
r=floor(F^2/s^2)>=1.
```

We use two standard bounded-density results of Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions* (arXiv:1402.4492): their one-dimensional projection-density theorem gives density at most `sqrt(2)` for every unit linear projection of a product law with coordinate density caps one, and their anisotropic concentration theorem gives, for any fixed `epsilon in (0,1)`,

```
L(DZ, t F) <= (C_epsilon t)^((1-epsilon) r).
```

Here `L` is the Euclidean concentration function, so translation of the target ball is already included.

If `r=1`, then `F^2/s^2<2`, hence `s>F/sqrt(2)`. Let `u` be a left singular vector for `s`. The scalar variable `u^T D Z` has density at most `sqrt(2)/s`. Therefore a ball of radius `rho` implies a scalar interval of length `2rho`, and

```
P(||DZ-z||<=rho)
 <= 2rho sqrt(2)/s
 < 4rho/F.
```

If `r>=2`, use the anisotropic theorem with `epsilon=1/2`. Writing `t=rho/F`,

```
L(DZ,rho) <= (C_{1/2} t)^(r/2).
```

When `C_{1/2}t<=1`, the exponent `r/2>=1` gives at most `C_{1/2}t`. When `C_{1/2}t>1`, the trivial bound one is at most `C_{1/2}t`. Thus the assertion holds with

```
C_HS=max(4,C_{1/2}).
```

This proves the lemma. Notice that it is linear, not merely `rho^alpha` with `alpha<1`, even when the singular mass of `D` is spread over arbitrarily many directions. The rank-one endpoint is paid by the sharp one-dimensional marginal estimate, while stable rank at least two is paid by the anisotropic concentration theorem.

## 3. The aggregate three-arm coarea theorem

### Theorem 3.1 (`QFORM-THREE-ARM-FROBENIUS-COAREA-v1`)

Let

```
X0,  X^(1), X^(2),  Y0, Y^(1), Y^(2), W
```

be mutually independent random blocks, where every scalar coordinate inside every block is independent of the others and has a density bounded by one. The block `W` may be absent. Let `r,c` be nonzero real vectors and `D` a nonzero real matrix of compatible dimensions. Let `H` be an arbitrary Borel function of `(Y0,Y^(1),Y^(2),W)`. Define

```
T = H(Y0,Y^(1),Y^(2),W)
    +2 X0 (r^T Y^(1))
    +2 Y0 (c^T X^(1))
    +2 (X^(2))^T D Y^(2).
```

Then `T` has a continuous density and

```
||p_T||_infinity
 <= K_3 [ ||r||_2 ||c||_2 ||D||_HS ]^(-1/3),
```

where

```
K_3 = (3/(2sqrt(2))) (4sqrt(2) C_HS)^(1/3)
```

is universal.

The key point is that the third arm is paid by the **whole Hilbert--Schmidt mass of `D`**. No entry of `D`, no singular direction of `D`, and no bounded-cardinality physical core is selected.

#### Proof

Write

```
R = r^T Y^(1),
C = c^T X^(1),
F = ||D||_HS,
R0=||r||_2,
C0=||c||_2.
```

Condition on the entire coefficient side `(Y0,Y^(1),Y^(2),W)`. The three remaining random blocks `X0,X^(1),X^(2)` stay independent.

By the one-dimensional bounded-density projection theorem,

```
||p_C||_infinity <= sqrt(2)/C0,
```

and, for every fixed nonzero vector `v`,

```
||p_{v^T X^(2)}||_infinity <= sqrt(2)/||v||_2.
```

Consequently the three conditional summands have density caps

```
1/(2|R|),
1/(sqrt(2) C0 |Y0|),
1/(sqrt(2) ||D Y^(2)||_2),
```

respectively. Convolution cannot increase the smallest of the three caps. Hence the conditional density `g_Y` of `T` satisfies

```
||g_Y||_infinity
 <= 1/[sqrt(2) M],

M=max( |R|, C0|Y0|, ||D Y^(2)||_2 ).          (3.1)
```

This is the coarea budget: the reciprocal Jacobian is averaged only after all three independent coefficient resources have been retained.

The three quantities inside the maximum are independent because they use the disjoint original-coordinate blocks `Y^(1)`, `Y0`, and `Y^(2)`. Their small-ball bounds are

```
P(|R|<t) <= 2sqrt(2) t/R0,
P(C0|Y0|<t) <= 2t/C0,
P(||D Y^(2)||<t) <= C_HS t/F,
```

where the last line is Lemma 2.1. Therefore, with

```
P0 = R0 C0 F,
a0 = 4sqrt(2) C_HS,
```

we have

```
P(M<t) <= min(1, a0 t^3/P0).                 (3.2)
```

Layer cake gives

```
E M^(-1)
 = integral_0^infinity P(M<1/s) ds
 <= (3/2) (a0/P0)^(1/3).                     (3.3)
```

Indeed the splitting point is `s0=(a0/P0)^(1/3)`; the portion below `s0` contributes `s0`, and the tail contributes `s0/2`.

Averaging (3.1) and using (3.3) proves

```
||p_T||_infinity
 <= (3/(2sqrt(2))) (4sqrt(2) C_HS/P0)^(1/3).
```

For continuity, outside a null set the three conditional coefficients are nonzero: `R` and `Y0` have absolutely continuous laws, while `P(DY^(2)=0)=0` because a nonzero linear map has a proper affine kernel and the product law is absolutely continuous. For such a coefficient realization, the conditional law is a convolution of at least two `L^1` densities and hence has a continuous density. The integrable domination in (3.1)--(3.3) permits dominated convergence after the arbitrary shift `H`. Thus the unconditional density is continuous.

This completes the proof.

## 4. Exact bank form

A useful original-coordinate reformulation is the following. Suppose six disjoint physical banks produce scalar projections `U_i,V_i` (`i=1,2,3`) whose coefficient-vector norms are `a_i,b_i`, and the form contains exactly

```
2 U_1 V_1 + 2 U_2 V_2 + 2 U_3 V_3
```

plus an arbitrary phase depending only on one side. The sharp one-dimensional product-projection estimate gives caps `sqrt(2)/a_i` and `sqrt(2)/b_i`. Applying the same argument (or Theorem 3.1 when the third arm is rank one) yields the scale

```
||p||_infinity <= 3 [ product_i (a_i b_i) ]^(-1/3).
```

This is the three-arm analogue of the earlier two-arm `E 1/max` coarea estimate, and it exhibits the correct aggregate-before-inversion principle directly.

## 5. Target-valid stress family: why the diffuse core must enter before reciprocal payment

The theorem eliminates a real dimension-loss mechanism, not merely a cosmetic one.

Fix an integer `m>=256`, put `q=16m` and `p=32m`. In `R^p`, let

```
u_1 = q^(-1/2) 1_{first q coordinates},
u_2 = q^(-1/2) 1_{last q coordinates},
```

and set

```
D_m=(m/sqrt(2))(u_1u_1^T+u_2u_2^T).
```

Then

```
||D_m||_HS=m,
s_1(D_m)=s_2(D_m)=m/sqrt(2),
max_ij |(D_m)_ij|=1/(16sqrt(2))<1/16.
```

Define the cross block, with row banks `(x,u,X_core)` and column banks `(y,v,Y_core)`, by

```
B_m = [ 0          m^(-1/2)     0
        m^(-1/2)   0             0
        0           0             D_m ].
```

Finally define the symmetric matrix

```
A_m = [ 0    B_m
        B_m^T 0 ].
```

The singular values of `B_m` are

```
m/sqrt(2), m/sqrt(2), m^(-1/2), m^(-1/2), 0,...,
```

so `A_m` has eigenvalues `+/-` these singular values. In particular it has four eigenvalues of magnitude `m/sqrt(2)>=1`; it is a fully valid target matrix. All its physical entries have magnitude at most `1/16` for `m>=256`, so the example is not paid by a large physical pivot.

The disjoint star--star--core packet has

```
||r|| ||c|| ||D_m||_HS
 = m^(-1/2) m^(-1/2) m
 = 1.                                             (5.1)
```

Thus Theorem 3.1 gives a universal density bound for the entire cross form, uniformly in `m`, for **every** allowed cap-one product input law.

Now take, only to diagnose the proof interface, all four star/anchor variables `x,u,y,v` to be independent `Uniform[-1/2,1/2]`. If the core is first thrown into the phase and one uses only the two anchor-star arms, the standard reciprocal-coefficient budget is

```
E [ 1/(2 max(|v|/sqrt(m), |u|/sqrt(m))) ]
 = (sqrt(m)/2) E[1/max(|u|,|v|)].
```

For two independent `Uniform[-1/2,1/2]` variables,

```
P(max(|u|,|v|)<=t)=4t^2,  0<=t<=1/2,
```

so `E[1/max(|u|,|v|)]=4`. Hence the two-arm budget equals

```
2 sqrt(m) -> infinity.                            (5.2)
```

This is not merely a loose upper-bound artifact: the two-arm subtotal

```
S_m=(2/sqrt(m))(xv+uy)
```

is a deterministic `m^(-1/2)` rescaling of a fixed nondegenerate law, so its density supremum grows like `sqrt(m)`.

Equations (5.1)--(5.2) isolate the missing factor exactly. A coarea argument that first pays only the two star coefficients must lose `sqrt(m)`. The diffuse core contributes the compensating factor, and it has to be retained through the same reciprocal-Jacobian average. Theorem 3.1 does precisely this via the Hilbert--Schmidt small-ball gate.

## 6. Relation to the live T4 survivor

The fresh fleet03/B07 structural packet `QFORM-O0-DISJOINT-STAR-STAR-CORE-v1` supplies four genuinely disjoint residual banks and, for one choice of colors,

```
C_* R_* F_* > 1/(256 sqrt(3)),                    (6.1)
```

where `C_*` and `R_*` are the two star norms and `F_*` is the Frobenius norm of the disjoint core block.

Theorem 3.1 shows that (6.1) is already quantitatively sufficient whenever, after the indicated physical-bank routing, the smoothing-side dependence is **affine and the three displayed arms are not contaminated by same-side quadratic curvature**. In that affine three-arm subcase,

```
||p_Q||_infinity
 <= K_3 (256 sqrt(3))^(1/3).                     (6.2)
```

The actual live T4 survivor is harder because the same original-coordinate banks can carry arbitrary same-side quadratic terms and additional cross couplings. Conditioning the coefficient side then leaves a genuine quadratic form, rather than the affine convolution used in (3.1). The present theorem therefore does not claim to close the full T4 packet.

What it does prove is that **diffuseness of the core is no longer itself an obstruction**. The full Frobenius mass can be paid dimension-free without choosing one entry or one singular vector. The remaining obstruction is the preservation of this three-way small-ball tensorization in the presence of same-side quadratic curvature.

This gives the next precise B05 implication:

`QFORM-THREE-ARM-SAMESIDE-CURVATURE-COAREA-v1` — replace the affine conditional convolution in (3.1) by a curved coarea estimate that still couples the two star small-ball factors with the Hilbert--Schmidt linear-image factor, instead of conditioning away one of the three resources or selecting a local minor.

## 7. fleet04 result actually consumed

The exact designated partner path `fleet04/B05` had no completed current-QFORM artifact at the fresh source lookup, so no exact-partner result is fabricated.

A compatible completed fleet04 result was nevertheless applied. fleet04/B18 r2 records the sharp bounded-density product-projection/Rogozin input used in its three-bank zero-pivot transfer; in particular unit linear projections of disjoint cap-one product banks have universal density cap and the banked zero-pivot branch is continuous. The present proof uses that projection estimate at the actual inequalities

```
||p_{c^T X^(1)}||_infinity <= sqrt(2)/||c||,
||p_{v^T X^(2)}||_infinity <= sqrt(2)/||v||,
```

which are exactly what produce the first two coefficient factors in (3.1) and the scalar endpoint of Lemma 2.1. As a separate already-paid sibling branch, fleet04/B18 r3 gives

```
||p_Q||_infinity
 <= 3e ((1+r^2)/(2r))^(1/3) < 8.785
```

for its exact-rank-three Schur-isotropic shear state with `1/2<=r<=2` and the stated row-marginal condition. No part of that theorem is extended beyond its source scope here.

## 8. Status

- Full arbitrary-dimensional QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- New proved support theorem: `QFORM-THREE-ARM-FROBENIUS-COAREA-v1`.
- New proved linear-image corollary: `QFORM-HS-LINEAR-SMALLBALL-v1`.
- Continuity: **proved for Theorem 3.1's scoped affine three-arm model**, not for the full target.
- Exact designated fleet04/B05 partner artifact: absent at source lookup.
- Next missing factor: same-side quadratic curvature must be included in the three-resource reciprocal-Jacobian average without destroying the independent coefficient-side tensorization.
