SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T11:49:41Z.
attacking: high-leverage rank-three projection by mixed third/second-volume product-Fourier rearrangement.

# fleet03/B04 r32 — mixed-volume rescue of a dense high-leverage rank-three projection

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** revision `2026-09-22.15`; QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport only  
**Full QFORM:** OPEN  
**Continuity:** proved for the explicit family below through an `L^1` characteristic function; not proved for the full target.

## 1. Dependency actually used at an equation

I apply fleet03/B02's completed supporting theorem `QFORM-WEIGHTED-MIXED32-FOURIER-L1-v1`, source

`yspennstate/math-open-problems@ff8ec2ee90d4846f39e728e1ca20d50c717cc894`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T085705Z-fleet03-B02-qform-r25/REPORT.md`.

Its exact specialization used here is this. Let `B=A[I,J]` be an original-coordinate cross block, let `x in I`, `y in J`, let

`J3 = sum_{|S|=|T|=3, x in S, y in T} det(B[S,T])^2`,

and let `N=B[I\{x},J\{y}]`, `E2=e2(N^T N)`. If the equal mixture (`theta=1/2`) of the incident third-minor row marginals and residual second-minor row marginals is at most `1/2` coordinatewise (or the analogous column condition), then the full ambient quadratic-plus-affine form has a continuous `C_0` density and

`||p_Q||_infinity <= (5e/2^(1/5)) (J3 E2)^(-1/10)`.        (1.1)

This is the actual inequality consumed below. I do not use law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, or a fiber-supremum estimate.

The designated partner `fleet04/B04` had no completed current-QFORM handoff at the fresh direct repository lookup, and recent commits found for that slot were historical FEI/BT4 work. I therefore did not invent a partner theorem; the completed peer theorem above is the result actually applied.

## 2. A dense genuinely rotated indefinite target

Define the `5 x 5` rational matrix

`P =`

```
[ 9/10,   3/20,   3/20,   3/20,   3/20 ]
[ 3/20,  21/40,   1/40,   1/40, -19/40 ]
[ 3/20,   1/40,  21/40, -19/40,   1/40 ]
[ 3/20,   1/40, -19/40,  21/40,   1/40 ]
[ 3/20, -19/40,   1/40,   1/40,  21/40 ] .
```

Every entry of `P` is nonzero. Put

`A_* = [[0,P],[P,0]]`                                            (2.1)

on ten original independent coordinates. The form is therefore

`Q_*(X,Y)=2 X^T P Y`,

not diagonal in the independent coordinates and genuinely indefinite.

### 2.1 Exact projection factorization

Let

`H = (1/2) [[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]`

and define the `5 x 3` matrix `U` by

`U[0,:]=(3/sqrt(10),0,0)`

and, for the four lower rows `r`,

`U[r+1,:]=( H[r,0]/sqrt(10), H[r,1], H[r,2] )`.

Then direct orthogonality of the Hadamard columns gives

`U^T U=I_3`,                                                     (2.2)

and a direct multiplication gives

`P=UU^T`.                                                       (2.3)

Hence `P^2=P`, `rank(P)=3`, and its nonzero eigenvalues are all one. Consequently

`spec(A_*)={+1,+1,+1,-1,-1,-1,0,0,0,0}`.                       (2.4)

Thus `A_*` satisfies the exact target hypothesis with six eigenvalues of absolute value one.

## 3. Why the natural pure third-volume gate fails

For a rank-three projection `P=UU^T`, Cauchy--Binet gives

`sum_{|S|=|T|=3} det(P[S,T])^2=1`,                              (3.1)

and the row inclusion marginal of the canonical squared `3 x 3` minor law is the projection leverage `P_ii`. In particular

`alpha_0^(3,full)=P_00=9/10`.                                   (3.2)

The standard fractional third-volume Fourier gate requires `alpha_i <= q/2` with `q<3/2`; therefore it can only tolerate marginals strictly below `3/4`. The natural pure-third-volume gate fails at the first physical row because `9/10>3/4`.

This is the point of the example: the form is spectrally perfect (exact rank three on the cross block) yet the most direct canonical third-volume product-Fourier weighting is blocked by one heavy physical coordinate.

## 4. Mixed `3+2` determinant rearrangement pays the heavy coordinate

Choose the physical row and column anchors `x=y=0`.

### 4.1 Incident third-volume currency

Because `P[S,T]=U_S U_T^T` for `|S|=|T|=3`,

`det(P[S,T])=det(U_S)det(U_T)`.                                  (4.1)

For a projection DPP, or directly by Cauchy--Binet differentiation,

`sum_{S:0 in S, |S|=3} det(U_S)^2=P_00=9/10`.                   (4.2)

Therefore the double-anchored third-volume resource is

`J3=(9/10)^2=81/100`.                                           (4.3)

The lower four rows form a transitive Walsh orbit. Conditional on row `0` being included, exactly two of the lower four rows are included and symmetry makes their incident-third marginals equal. Hence

`alpha^(3)=(1,1/2,1/2,1/2,1/2)`,                               (4.4)

and the same vector holds on the column side.

For completeness, the four nonzero anchored row-triple weights after summing over anchored column triples are each `81/400`; the other two possible anchored row triples have zero weight. Their normalized inclusion marginals are nevertheless exactly (4.4).

### 4.2 Residual second-volume currency

Delete the anchor row and column and write

`N=P[{1,2,3,4},{1,2,3,4}]`.

The nonzero eigenvalues of `N` are those of

`U_-^T U_- = diag(1/10,1,1)`.                                  (4.5)

Therefore the squared singular values of `N` are

`1/100,1,1`,

so

`E2=e2(N^T N)=1+1/100+1/100=51/50`.                            (4.6)

The lower `4 x 4` block is translation-invariant under the Walsh group. The canonical squared `2 x 2` minor law is therefore transitive on its four physical rows and on its four physical columns. Every minor uses two rows, so each residual row marginal is exactly `1/2`; similarly for columns:

`alpha^(2)=(0,1/2,1/2,1/2,1/2)`.                               (4.7)

### 4.3 Equal mixing exactly saturates the sharp `q=1` gate

Take `theta=1/2`. The mixed row marginals are

`alpha_i=(alpha_i^(3)+alpha_i^(2))/2=1/2` for every `i`.         (4.8)

The column marginals are identical. Thus the peer theorem applies with its strongest allowed Hausdorff--Young parameter `q=1`.

Substituting (4.3) and (4.6) into (1.1) gives

`||p_{Q_*}||_infinity`
` <= (5e/2^(1/5)) [(81/100)(51/50)]^(-1/10)`
` = (5e/2^(1/5)) (4131/5000)^(-1/10)`
` = 12.060073872851982...`.                                    (4.9)

Therefore, for every choice of ten independent real inputs whose densities are bounded by one,

`boxed: ||p_{X^T A_* X}||_infinity <= 12.061`.                  (4.10)

Moreover the characteristic function furnished by the mixed-volume theorem lies in `L^1(R)`, so this family has a continuous density vanishing at infinity.

## 5. What is genuinely new in this application

The pure canonical third-volume law is blocked by leverage `9/10`; no admissible `q<3/2` can pay that marginal. The mixed determinant rearrangement pairs the heavy incident `3 x 3` volume with the anchor-deleted `2 x 2` volume, and the heavy coordinate disappears from the latter. At equal mixing every physical marginal becomes exactly `1/2`, which is the `q=1` product-Hausdorff--Young threshold.

Thus a high-leverage rotated rank-three projection can be controlled without selecting a tiny physical minor and without requiring low leverage of the rank-three spectral projector. The resource used is aggregate and explicit:

`J3 E2 = 4131/5000`.                                            (5.1)

This is a concrete mechanism for part of the finite-hub survivor appearing in preceding B04 runs: a single physical hub can be diluted by a lower compound order before Fourier inversion.

## 6. Exact symbolic/numerical checks

The deterministic checks used no Monte Carlo. They verify:

1. `U^T U=I_3` exactly.
2. `P=UU^T` and `P^2=P` exactly.
3. Every displayed entry of `P` is nonzero.
4. `spec(A_*)` consists of three `+1`, three `-1`, and four zeros.
5. Total squared third-minor volume `E3(P)=1`.
6. Anchored third volume `J3=81/100`.
7. Incident anchored row marginals are `(1,1/2,1/2,1/2,1/2)`.
8. Residual squared second-minor volume is `E2=51/50`.
9. Residual row marginals are all `1/2` on the four lower coordinates.
10. The final constant in (4.9) is `12.060073872851982...`.

## 7. Scope and remaining implication

This is a complete **supporting estimate for an explicit genuinely rotated indefinite target family**, contingent only on the completed B02 mixed-volume theorem cited in section 1. It is not a proof of the unrestricted conjecture.

The next B04 target should be a structural compiler:

`QFORM-HUB-DILUTION-BY-LOWER-COMPOUND-v1` — given a third-volume canonical law with a finite set of heavy physical coordinates, systematically mix incident `E3` packets with anchor-deleted `E2` (and, when needed, `E1`) packets so that all product exponents fall below the Hausdorff--Young threshold while retaining a dimension-free geometric mean of determinant volume. The present matrix is the exact one-hub model where that programme closes with equality in every marginal.

Full QFORM remains OPEN, and full-target continuity remains OPEN.
