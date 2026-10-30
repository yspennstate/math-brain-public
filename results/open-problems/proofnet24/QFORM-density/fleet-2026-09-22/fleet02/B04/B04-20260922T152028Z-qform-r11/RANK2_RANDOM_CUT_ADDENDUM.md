# fleet02/B04 addendum — random-cut exterior mass for a diffuse rank-two Schur range

Run: `B04-20260922T152028Z-qform-r11`  
Status: `ESSENTIAL_STEP_APPLIED / STRUCTURAL SUBCASE PROVED / FULL TARGET OPEN`

This addendum attacks the first structural implication left by `QFORM-SQUARE-ASSISTED-EK-AGGREGATE-v1`: rather than selecting a second cross singular value, extract a physical cut whose **aggregate** rank-two exterior mass is large.

## 1. Rank-two random-cut lemma

Let

`S = V D V^T`,

where `V` is an `n x 2` matrix with orthonormal columns and `D=diag(mu_1,mu_2)` with `mu_1 mu_2 !=0`. Write the physical row vectors as `v_i in R^2`, their leverages as

`r_i=||v_i||^2`,  `rho=max_i r_i`.

For a coordinate cut `I,J`, let

`M = V_I^T V_I`,

so `V_J^T V_J=I_2-M`, and let `B=S[I,J]=V_I D V_J^T`.

### Lemma 1 — `QFORM-RANK2-RANDOM-CUT-E2-v1`

If `rho<1/2`, there exists a physical cut `I,J` such that

`det(M) det(I_2-M) >= (1-2 rho)/16`,                            (1.1)

and therefore

`E_2(B)=s_1(B)^2 s_2(B)^2
 >= (mu_1 mu_2)^2 (1-2 rho)/16.`                                (1.2)

Moreover, for this same cut,

`max_{i in I} (P_range(B))_{ii}
 <= 16 rho/(1-2 rho),`                                          (1.3)

and the analogous bound holds on the `J` side. In particular, if

`rho <= 1/34`,                                                    (1.4)

then this cut satisfies the `q=1` regularized-determinant leverage gate on both sides and

`E_2(B) >= (mu_1 mu_2)^2/17.`                                   (1.5)

### Proof

Put

`w_ij = det(v_i,v_j)^2`  for `i<j`.

Cauchy--Binet gives

`sum_{i<j} w_ij = det(V^T V)=1.`                                (1.6)

For each fixed `i`, use `det(x,y)^2=||x||^2||y||^2-<x,y>^2` and `sum_j v_j v_j^T=I_2`:

`sum_{j!=i} w_ij
 = r_i sum_j r_j - sum_j <v_i,v_j>^2
 = 2 r_i-r_i
 = r_i.`                                                         (1.7)

Thus the `w_ij` form a probability distribution on unordered edges, and the weighted degree of vertex `i` is exactly its leverage `r_i`.

Choose `I` by independent fair Bernoulli choices, with `J=I^c`. Cauchy--Binet again gives

`det M = sum_{e subset I} w_e`,
`det(I_2-M) = sum_{f subset J} w_f.`                             (1.8)

Hence

`E[det M det(I_2-M)]
 = (1/16) sum_{e,f: e cap f=empty} w_e w_f.`                    (1.9)

If `e={i,j}`, the total `w`-mass of edges meeting `e` is at most

`r_i+r_j <=2 rho`                                                (1.10)

(the edge `ij` is merely double-counted in this upper bound). Therefore two independent `w`-distributed edges are disjoint with probability at least `1-2rho`. Equations (1.9)-(1.10) give

`E[det M det(I_2-M)] >= (1-2rho)/16`,

so some cut satisfies (1.1).

For that cut, both determinants are positive. The cross block has rank two, and

`B B^T = V_I D (I_2-M) D V_I^T`.

The product of its two nonzero eigenvalues equals

`det(M) det(D)^2 det(I_2-M)`,                                   (1.11)

because the nonzero eigenvalues may be computed in the two-dimensional coefficient space. Since `E_2(B)` is exactly the product of the two squared singular values for a rank-two matrix, (1.11) proves (1.2).

Also `range(B)=range(V_I)`. The range projector is

`P_range(B)=V_I M^{-1} V_I^T`.

Because `0<=M<=I_2`, `lambda_max(M)<=1`, hence

`lambda_min(M)=det(M)/lambda_max(M) >= det(M).`

As `det(I_2-M)<=1`, (1.1) implies `det M >=(1-2rho)/16`. Therefore each row leverage satisfies

`v_i^T M^{-1}v_i <= r_i/lambda_min(M)
 <=16rho/(1-2rho)`,

which is (1.3). The same argument with `I,J` interchanged gives the other side. Finally `16rho/(1-2rho)<=1/2` exactly when `rho<=1/34`, and then `(1-2rho)/16>=1/17`. This proves (1.4)-(1.5). QED.

## 2. Consequence for the square-assisted aggregate theorem

Combine Lemma 1 with the same-run theorem `QFORM-SQUARE-ASSISTED-EK-AGGREGATE-v1` at `q=1,k=2`. If

`Q=a(X+m(Y))^2+Y^T S Y`,

where `X` is a genuine untouched original coordinate, `a!=0`, and `S` has rank two with maximum physical range leverage at most `1/34`, then

`||p_Q||_infinity
 <= 11.26662855015649 * 17^(1/8)
    (|a| |mu_1 mu_2|)^{-1/2}`                                   (2.1)

or numerically

`boxed(||p_Q||_infinity
 <= 16.0546222489 (|a| |mu_1 mu_2|)^(-1/2)).`                   (2.2)

The point is structural: no chosen physical cut, selected second singular value, or MSS partition is assumed. A good cut is produced directly from the wedge-mass distribution.

## 3. Exact rank-three scalar-pivot corollary

Now let

`A=U Lambda U^T`

have exact rank three, with `U` having orthonormal columns and invertible diagonal `Lambda`. Fix an original coordinate `i`, write its spectral-frame row as `u`,

`r=||u||^2`,  `a=u Lambda u^T !=0`,

and pivot that original coordinate. Let `S` be the resulting Schur complement.

For completeness, its rank-two spectral product can be derived directly. If `W` is `U` with row `u` removed, then

`S=W K W^T`,
`K=Lambda-Lambda u^T u Lambda/a.`                               (3.1)

The symmetric matrix `K` has kernel `span(u^T)` and range `u^perp`. Since

`W^T W=I_3-u^T u`,

this Gram operator is the identity on `u^perp`; hence the two nonzero eigenvalues of `S` are the two nonzero eigenvalues of `K`. The rank-one determinant identity gives

`adj(K)=det(Lambda) u^T u/a`,                                   (3.2)

so, in a basis whose third vector is `u^T/sqrt(r)`,

`mu_1 mu_2 = det(Lambda) r/a.`                                  (3.3)

The physical range leverage of row `j!=i` in `S` is likewise exactly

`c_{j|i}=||u_j||^2-<u_j,u>^2/r`,                                (3.4)

because `W:u^perp -> R^(n-1)` is an isometry.

Therefore, if

`rho_i=max_{j!=i} c_{j|i} <=1/34`,                              (3.5)

Lemma 1 supplies a physical cut of the rank-two Schur complement satisfying the `q=1` gate and

`E_2(B) >= (det(Lambda)^2 r^2/a^2)/17.`                         (3.6)

Substituting into the same-run aggregate theorem yields

`boxed(||p_(X^T A X)||_infinity
 <= 16.0546222489
    (|det Lambda| r |a|)^(-1/4)).`                              (3.7)

This is `QFORM-RANK3-DIFFUSE-PIVOT-AGGREGATE-v1`.

It is a genuine improvement over a selected-cross formulation: once a nonzero pivot has a diffuse rank-two Schur range, the full exterior mass automatically creates the needed physical product-space cut.

## 4. Remaining structural debt

This does not finish rank three, let alone arbitrary rank. The new first obstruction is narrower:

- either find a pivot with `|det Lambda| r |a|` bounded below and Schur-range leverage at most `1/34`, in which case (3.7) closes it;
- or handle the complementary **heavy Schur-range / tiny-pivot** regime by aggregate hyperbolic banks;
- the exact zero-pivot isotropic families remain outside any scalar-pivot argument and must use the bilinear/aggregate branch.

Thus the global `QFORM-AGGREGATE-PIVOT-CURRENCY-v1` debt survives, but its diffuse rank-two Schur subcase is now completely paid by an elementary random-cut argument.

No full-proof or continuity claim is made.
