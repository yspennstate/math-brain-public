SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-23T18:22:07Z.
attacking: the joint-maximal-curvature bridge; keep the partner's same-bank rank-two curvature and both independent scalar banks together, and test whether the new projected-crossing theorem can spend the transferred determinant before any Borel maximalisation.

# Early substantive checkpoint — a mixed 3-crossing hidden in the ratio packet

Full QFORM remains OPEN. This checkpoint records a new product-preserving branch inequality and an exact obstruction to a tempting but incompatible use of the grouped-hub projected-crossing theorem.

Use the fleet03/B05 r29 ratio packet. The first original-coordinate product bank has an orthonormal two-dimensional frame `U` (rows `u_i in R^2`) and aggregate `x=U^T X=(S,R)`. The two disjoint scalar product banks give normalized scalar projections `Y,Z`, independent of each other and of the first bank. In aggregate coordinates

`Q = x^T C x + 2 x^T P (Y,Z)^T + (Y,Z) B (Y,Z)^T + affine/outside terms`,

with

`B=[[a,c],[c,d]]`, `P=[[alpha,beta],[r,s]]`,
`C-P B^{-1}P^T = diag(L,0)`, `L=lambda*m`,
`Delta=det B<0`, `mu=|Delta| |lambda|`,
`z=B^{-1}(r,s)^T=(z1,z2)^T`.

The partner proves the conditional determinant/currency identities used below.

## 1. Exact mixed crossing determinant

Put `p_Y=(alpha,r)^T`, `p_Z=(beta,s)^T`. If the first product bank is split into original-coordinate sets `I,J`, and the entire `Y` bank is placed with `I` while the entire `Z` bank is placed with `J`, then the physical cross block factors through the `3 x 3` aggregate matrix

`K = [[C, p_Z],[p_Y^T,c]]`.

For a symmetric `2 x 2` matrix, `p_Y^T adj(C)p_Z=(J p_Y)^T C(J p_Z)`. Thus the partner's mixed-transverse identity gives

`det K = c det C - U_mix`,

where `U_mix=L r s+(c/Delta)(det P)^2`. Using its exact formula

`det C=(det P)^2/Delta + L (r,s) B^{-1}(r,s)^T`

and the explicit inverse of `B`, one obtains

`det K = - L Delta z1 z2`.

Therefore

`boxed{ |det K| = mu*m*|z1 z2|. }`                                      (1)

So the two conditional determinants `mu*m*z1^2` and `mu*m*z2^2` found by the partner have a genuinely joint original-coordinate manifestation: their geometric mean is the determinant of a three-direction physical crossing.

## 2. Product-preserving partition lemma for a diffuse two-frame

Let `h=max_i ||u_i||^2`. Define the Pluecker weights

`w_ij=det(u_i,u_j)^2`, `i<j`.

Cauchy-Binet gives `sum_{i<j} w_ij=1`, and Parseval gives the exact weighted degree identity

`sum_{j:j!=i} w_ij=||u_i||^2<=h`.                                      (2)

For a fair random partition `I union J` of the first-bank coordinates, put

`S_I=sum_{i in I}u_i u_i^T`, `S_J=I_2-S_I`.

Again by Cauchy-Binet,

`det S_I=sum_{i<j in I}w_ij`, `det S_J=sum_{k<l in J}w_kl`.

For a fixed edge `{i,j}`, the total Pluecker mass on edges disjoint from it is at least

`1-||u_i||^2-||u_j||^2+w_ij >= 1-2h`.

Hence

`E[det S_I det S_J]
 = (1/16) sum_{e cap f=empty} w_e w_f
 >= (1-2h)/16.`                                                       (3)

Therefore, whenever `h<1/2`, there is a deterministic original-coordinate split satisfying

`boxed{ sqrt(det S_I det S_J) >= (1/4)sqrt(1-2h). }`                  (4)

No spectral rotation of random variables occurs.

## 3. A new paid branch by the exact-rank-three crossing theorem

Let `R_I` be the physical-to-aggregate map from the left group `(I,Y-bank)` to `(S,R,Y)`, and `R_J` the analogous right map `(J,Z-bank)` to `(S,R,Z)`. Because the scalar aggregate coefficient vectors are normalized and live on disjoint original-coordinate banks,

`R_I^T R_I=diag(S_I,1)`, `R_J^T R_J=diag(S_J,1)`.

The physical cross block is

`M_cross=R_I K R_J^T`.

Whenever `det K!=0` and the split from (4) is used, it has exact rank three and its product of nonzero singular values is

`Gamma = |det K| sqrt(det S_I det S_J)
       >= (mu*m*|z1 z2|/4) sqrt(1-2h).`                               (5)

Apply the completed exact-rank crossing theorem from `NEW_PROJECTED_CROSSING.md`: arbitrary quadratic/internal functions on the two physical sides are allowed. Each three-dimensional singular projection of an original-coordinate product law has density cap at most `2^(3/2)`, so for rank three

`||p_Q||_infinity <= 6 Gamma^(-1/3)`.

Combining with (5),

`boxed{
 ||p_Q||_infinity
 <= 6 [4/(mu*m*|z1 z2| sqrt(1-2h))]^(1/3).
}`                                                                        (6)

In the clean diffuse packet `h<=3/8`,

`boxed{ ||p_Q||_infinity <= 12 (mu*m*|z1 z2|)^(-1/3). }`               (7)

This is an essential-density bound for the full ambient form: all terms internal to either side, outside affine terms, and same-bank curvature remain inside the arbitrary functions permitted by the crossing theorem. It uses the two scalar banks jointly with the first-bank curvature and never takes a frozen-fiber supremum.

## 4. Exact obstruction to the grouped-hub projected-crossing route

There is a complementary algebraic obstruction. If `(Y,Z)` are first grouped as a `k`-dimensional hub and one tries to use the *projected crossing remainder* of the same new theorem, then the first-bank curvature can never supply enough new directions.

For any light split `I,J`, write `E_J=row(U_J^T)`, so `dim E_J<=2`. The hub-light cross matrix on `J` is a compression of `P^T U_J^T`; hence its row space lies in `E_J`. If its rank is `k`, then the projected light crossing

`U_I C U_J^T (I-Pi_row(M_J))`

has row space contained in `E_J intersect row(M_J)^perp`, and therefore rank at most `2-k`. Consequently every nonzero projected volume order `ell` obeys

`boxed{ k+ell <=2. }`                                                   (8)

But the grouped-hub crossing theorem becomes density-integrable only when `k+ell>2`. In particular, when `P` is invertible and `U_J` has rank two, `row(M_J)=E_J` and the projected crossing is identically zero, even if `|det C|` is arbitrarily large.

Thus the partner's low-`Psi` compensation `chi |det C| >= (mu*m*theta^4)/8` cannot be spent by first projecting away the hub-visible directions: that operation removes precisely the two-dimensional plane in which the transferred curvature lives. The successful branch (6) instead splits the two scalar banks to opposite physical sides and keeps the mixed `3 x 3` crossing determinant (1) intact.

## 5. First remaining implication after the checkpoint

The joint-maximal problem is now narrower. In the r29 low-`Psi` chamber, the diffuse first-bank branch is paid whenever `mu*m*|z1 z2|` is quantitative. A survivor must therefore exhibit at least one of:

1. a heavy first-bank row (`h` close to `1/2` or larger),
2. strongly imbalanced inverse-pair shear (`|z1 z2|` small relative to `z1^2+z2^2`), or
3. collapse of the aggregate shear scale itself.

The next step is to couple the partner's strong half-Riesz estimate to the appropriate one-scalar/one-heavy-row branch, rather than Borelising it or projecting away the same plane.
