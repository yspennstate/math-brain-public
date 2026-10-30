SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-23T06:56:57Z.
attacking: factorization-invariant two-area smoothing for a grouped bilinear packet, then transfer the bound to the exact signed-Fejer quantity.

# fleet03/B01 — determinant-area bilinear receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement  
**Classification:** `PROVED SUPPORTING TARGET-LEVEL ANALYTIC THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** essential boundedness is proved in the stated branch; continuity is not claimed.

## 1. Source boundary and the missing implication attacked


The immediate analytic debt left by B01 run r23 was an anisotropy loss in the grouped bilinear receiver. If

`Q = 2 (M X_I)^T (N X_J) + H(X_I, outside)`

with rank-two grouped maps, r23 gave a bound involving `sigma_min(N)^(-1)`. That can be much worse than the true two-area scale when the receiver is anisotropic. The first implication attempted here is to aggregate the full two-dimensional area on BOTH sides before inversion and to allow an arbitrary outside-generated affine term on the still-random receiver bank.

The only product-measure inputs used below are the already source-validated projection bounds:

1. for independent cap-one coordinates and any deterministic coefficient vector `a`,

   `||p_(a^T X)||_infinity <= sqrt(2)/||a||_2`;

2. for two orthonormal vectors `u_1,u_2` and independent cap-one coordinates,

   `||( <u_1,X>, <u_2,X> ) density||_infinity <= 2`.

These are exactly the one- and two-dimensional product-projection inputs used in the preceding B01 receiver theorem. No independence is asserted after a rotation; only the joint density cap of the orthogonal two-dimensional projection is used.

## 2. Anisotropic inverse-radius lemma

### Lemma 2.1

Let `Y` be a random vector in `R^2` with density bounded by `K`. Let `S` be an invertible `2x2` matrix. Then, uniformly in every deterministic translation `a in R^2`,

`E |S(Y-a)|^(-1) <= 2 sqrt(pi K) |det S|^(-1/2).`        (2.1)

#### Proof

The vector `Z=S(Y-a)` has density bounded by `L=K/|det S|`. Layer cake and the disk area bound give

`E |Z|^(-1)
 = int_0^infinity P(|Z|<1/t) dt
 <= int_0^infinity min(1, pi L t^(-2)) dt.`               (2.2)

Split at `t_0=sqrt(pi L)`. The right side equals

`t_0 + pi L/t_0 = 2 sqrt(pi L)
 =2 sqrt(pi K)|det S|^(-1/2).`                            (2.3)

This proves the lemma. The exponent and determinant scaling are exact under scalar dilation. QED.

## 3. Main theorem in cross-block invariant form

Partition the ORIGINAL independent coordinates into disjoint banks `I,J,D,W`. Let `K` be a deterministic real `|I| x |J|` matrix with at least two nonzero singular values

`kappa_1 >= kappa_2 > 0.`                                  (3.1)

Let `c=c(X_D,X_W) in R^{|J|}` and let `H=H(X_I,X_D,X_W)` be arbitrary measurable functions, finite almost surely. Thus all nonlinear/quadratic curvature may remain on the entire `I` bank and on the disjoint outside banks, while the `J` bank is required to enter the active packet only affinely. Set

`Q = 2 X_I^T K X_J + c(X_D,X_W)^T X_J + H(X_I,X_D,X_W).`  (3.2)

### Theorem 3.1 — `QFORM-CROSS-2AREA-AFFINE-RECEIVER-v1`

Under (3.1)-(3.2), `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 2 sqrt(pi) (kappa_1 kappa_2)^(-1/2).`  (3.3)

Equivalently, with `||wedge^2 K||_op = kappa_1 kappa_2`,

`||p_Q||_infinity <= 2 sqrt(pi) ||wedge^2 K||_op^(-1/2).`       (3.4)

If `K` has exact rank two then

`kappa_1 kappa_2 = sqrt(e_2(K K^T))`,

so

`boxed: ||p_Q||_infinity <= 2 sqrt(pi) e_2(KK^T)^(-1/4).`       (3.5)

The estimate is invariant under internal `GL_2` refactorization of the rank-two cross interaction and has the correct degree `-1` under `K -> lambda K`.

#### Proof

Take a singular value decomposition

`K = sum_r kappa_r u_r v_r^T`,                                (3.6)

and retain only the two leading singular directions for a lower bound on the receiver coefficient norm. Condition on `(X_I,X_D,X_W)`. Write `x=X_I`, and let

`q(x)=2K^T x + c`.                                             (3.7)

The untouched coordinates `X_J` remain independent with density caps one. Therefore the one-dimensional product-projection theorem gives the conditional density bound

`||p_(Q | X_I,X_D,X_W)||_infinity
 <= sqrt(2)/|q(x)|.`                                           (3.8)

Let `c_j=<c,v_j>` for `j=1,2`. Orthogonal projection cannot increase norm, hence

`|q(x)| >= 2 [ kappa_1^2 ( <u_1,x> + c_1/(2kappa_1) )^2
                + kappa_2^2 ( <u_2,x> + c_2/(2kappa_2) )^2 ]^(1/2).` (3.9)

Define the two-dimensional orthogonal projection

`Y=(<u_1,X_I>, <u_2,X_I>).`                                   (3.10)

Although the two coordinates of `Y` need not be independent, the source-valid two-dimensional product-projection theorem gives

`||p_Y||_infinity <= 2.`                                       (3.11)

Conditional on `(X_D,X_W)`, the translation in (3.9) is deterministic and independent of `X_I`. Apply Lemma 2.1 with

`S=diag(kappa_1,kappa_2)`, `K_density=2`.                      (3.12)

Then

`E [ kappa_1^2(Y_1+a_1)^2 + kappa_2^2(Y_2+a_2)^2 ]^(-1/2)
 <= 2 sqrt(2pi) (kappa_1 kappa_2)^(-1/2).`                     (3.13)

Combining (3.8)-(3.9) supplies the factor `sqrt(2)/2=1/sqrt(2)`, and therefore

`||p_Q||_infinity
 <= (1/sqrt(2)) 2 sqrt(2pi) (kappa_1 kappa_2)^(-1/2)
 = 2 sqrt(pi) (kappa_1 kappa_2)^(-1/2).`                       (3.14)

The exceptional set where the projected coefficient vanishes has probability zero because `Y` has an absolutely continuous planar law. Averaging the conditional densities gives an absolutely continuous global law with the stated essential bound. QED.

## 4. Equivalent factorization theorem and why this improves r23

Suppose the cross packet is written

`2 (M X_I)^T (N X_J)`                                         (4.1)

with rank-two matrices `M,N`. Then Theorem 3.1, or equivalently a direct anisotropic use of Lemma 2.1, gives

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(pi)
    [ det(MM^T) det(NN^T) ]^(-1/4).`                          (4.2)

This strictly improves the preceding r23 estimate

`2 sqrt(pi) det(MM^T)^(-1/4) sigma_min(N)^(-1)`               (4.3)

whenever the receiver is anisotropic. If the singular values of `N` are `n_1>=n_2`, the improvement factor is

`(n_2/n_1)^(1/2)`                                              (4.4)

in the factorization coordinates of (4.2). More invariantly, (4.2) is unchanged under

`M -> T M`, `N -> T^(-T) N`, `T in GL_2`,                     (4.5)

which leaves the cross bilinear form unchanged. Thus no artificial internal basis condition number is paid.

For an exact rank-two cross block with thin SVD `K=U Sigma V^T`, choose

`M=Sigma^(1/2) U^T`, `N=Sigma^(1/2) V^T`.                     (4.6)

Then (4.2) reduces exactly to (3.3).

## 5. Distribution-function and signed-frequency consequences

The density estimate immediately yields, for every interval `I subset R`,

`boxed:
 P(Q in I)
 <= 2 sqrt(pi) |I| (kappa_1 kappa_2)^(-1/2).`                 (5.1)

This is a direct small-ball/distribution-function estimate in the required arbitrary fragmented-support class.

Now apply the completed partner result from fleet04/B01. For a law `mu` define

`D_T mu(y)=(1/(2pi)) int_{-T}^T (1-|t|/T)
                 Re(exp(-ity) phi_mu(t)) dt.`                 (5.2)

Fleet04/B01 proves the exact equivalence

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`                   (5.3)

for bounded densities, with the converse implication as well. Applying (5.3) to Theorem 3.1 gives the actual averaged-frequency estimate

`boxed:
 sup_(T>0,y in R) D_T law(Q)(y)
 <= 2 sqrt(pi) (kappa_1 kappa_2)^(-1/2).`                      (5.4)

This is the required signed/averaged oscillatory replacement. It is strictly weaker than absolute Fourier `L^1` control and uses no false pointwise Fresnel decay.

## 6. Phase-aligned scalar counterexample remains intact

For every prescribed nonzero frequency `s` and small `delta>0`, the set

`E_s(delta)={x: dist(sx^2,2pi Z)<=delta}`                      (6.1)

has infinite Lebesgue measure. Select a finite measurable subset of total measure one and put `f=1_E`. Then `0<=f<=1`, `int f=1`, and

`Re int exp(i s x^2) f(x) dx >= cos(delta).`                  (6.2)

Hence no law-uniform pointwise power decay can hold for the scalar quadratic phase. Theorem 3.1 bypasses this obstruction by retaining original-coordinate product structure until the receiver is linear and then averaging the two-dimensional inverse-radius singularity.

## 7. Actual target-level control family

If the active matrix is a pure cross block

`A = [[0,K],[K^T,0]]`                                         (7.1)

and `K` has singular values `kappa_1>=kappa_2>=1`, then `A` has eigenvalues `+kappa_1,+kappa_2,-kappa_1,-kappa_2` (plus zeros). Therefore it satisfies the target hypothesis with at least three eigenvalues of modulus at least one, and Theorem 3.1 gives

`||p_(X^T A X)||_infinity <= 2 sqrt(pi) < 3.545.`              (7.2)

The same bound survives arbitrary additional independent additive terms on disjoint coordinate banks by convolution. This is a genuine full-quantifier target family, not a proof that every three-large-eigenvalue matrix admits the required one-sided-affine cross decomposition.

## 8. What remains unpaid

The theorem removes the factorization/condition-number loss for every branch in which one active bank enters affinely. It does **not** pay arbitrary nonlinear self-curvature simultaneously on both active banks. It also does not prove that the bare three-large-eigenvalue condition forces a cross block with `kappa_1 kappa_2` uniformly bounded below; live corrections explicitly rule out several single-packet extraction claims.

The next B01 implication should therefore be one of:

1. use (3.3) after a product-preserving routing theorem that exposes a one-sided-affine rank-two cross packet with quantitative exterior area; or
2. extend the signed-Fejer/inverse-radius mechanism to a genuinely two-sided-curved bicore without taking coordinatewise absolute values; or
3. in the regime where every such two-area packet is tiny, transfer the accumulated exterior mass to an already-paid diffuse/grouped/ridge branch before inversion.

Full QFORM remains OPEN. Full-target continuity remains OPEN.
