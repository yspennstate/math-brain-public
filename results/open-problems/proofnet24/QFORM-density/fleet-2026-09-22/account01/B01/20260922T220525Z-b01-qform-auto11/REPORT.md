# QFORM account01/B01 — completion defects can migrate into diffuse grouped squares

Run: `20260922T220525Z-b01-qform-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Classification: `CANDIDATE_REFUTED / ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source boundary

The full target remains open: for every real symmetric `A` with at least three eigenvalues of modulus at least one and every independent input vector with one-dimensional densities bounded by one, prove a universal essential density bound for `X^T A X`, or give a target-valid counterexample. Continuity is a separate desired conclusion.

This report continues the prior B01 completion-defect analysis. The prior exact algebra says that for a nonzero scalar cross triangle

`C(a,b,c)=[[0,a,c],[a,0,b],[c,b,0]]`

the unique diagonal rank-one completion has diagonal `(ac/b,ab/c,bc/a)`. Therefore if a scalar three-bank core is uniformly nonsingular, at least two diagonal defects from that dangerous completion must survive. The unpaid question was whether those two defects can be harvested by descending to fixed physical coordinates.

The answer to that proposed mechanism is **no**. The family below has a uniformly conditioned three-bank core and two unit completion defects, but every physical coefficient carrying the defects is `O(1/m)`. The defects migrate into two diffuse grouped rank-one squares. Group aggregation pays the example uniformly; fixed physical-pivot extraction does not.

No Gaussian assumption is used as a premise for the conjecture. Gaussian inputs are used only as one explicit target-valid witness law for the mechanism test; their densities are `<1`.

## 2. Exact diffuse completion-defect family

Fix an integer `m>=1`. Split the physical coordinates into five disjoint blocks

`U,V,W,Z,T`, each of cardinality `m`.

Let `e_U,e_V,e_W,e_Z,e_T` be the normalized all-ones vectors on those blocks, so each is a unit vector and the five are pairwise orthogonal. Define

`r1=e_U+e_V+e_W`,
`r2=e_U+e_Z`,
`r3=e_V+e_T`,

and

`A_m = r1 r1^T + r2 r2^T + r3 r3^T`.

Let `R` be the `3 x 5m` matrix with rows `r1,r2,r3`. The nonzero eigenvalues of `A_m=R^T R` equal the eigenvalues of the Gram matrix

`G=R R^T=[[3,1,1],[1,2,0],[1,0,2]]`.

Its characteristic polynomial is

`(lambda-4)(lambda-2)(lambda-1)`.

Hence for every `m`,

`spec_nonzero(A_m)={4,2,1}`,

so this is an exact target matrix with `s_3(A_m)=1`.

On the other hand every coordinate of every `e_*` has magnitude `m^{-1/2}`. A physical coordinate belongs to at most two of the `r_j`. Consequently

`max_{i,j} |(A_m)_{ij}| <= 2/m`.

More generally, for every physical index set `S` of cardinality `k`,

`||A_m[S,S]||_op <= 2k/m`

by the row-sum bound. Thus no fixed-cardinality physical principal block, diagonal pivot, or off-diagonal edge remains quantitatively large as `m -> infinity`, despite `s_3(A_m)=1`.

## 3. The scalar three-bank core and its two unit defects

Write the five grouped coordinates

`u=e_U^T x`, `v=e_V^T x`, `w=e_W^T x`, `z=e_Z^T x`, `tau=e_T^T x`.

Then

`x^T A_m x = (u+v+w)^2 + (u+z)^2 + (v+tau)^2`.

If `z,tau` are regarded as internal directions of the first and second large banks, the compressed scalar core on `(u,v,w)` is

`M=[[2,1,1],[1,2,1],[1,1,1]]`.

Its characteristic polynomial is

`(lambda-1)(lambda^2-4lambda+1)`,

so

`spec(M)={1,2-sqrt(3),2+sqrt(3)}`

and in particular

`sigma_min(M)=2-sqrt(3)>0.2679`.

The cross triangle is the unit triangle, whose dangerous rank-one completion is

`M_*=J_3`.

Thus exactly

`M=M_*+diag(1,1,0)`.

The two completion defects are therefore both equal to one. But they are not physical scalar pivots: algebraically

`u^2+2uz+z^2=(u+z)^2`,
`v^2+2v tau+tau^2=(v+tau)^2`.

Each defect has migrated into a diffuse grouped square. Every physical coefficient inside those grouped squares is at most `2/m`.

This proves the following mechanism obstruction.

### Proposition — no fixed-physical-coordinate defect harvest

There is no dimension-free implication of the form

> a uniformly nonsingular three-bank scalar core plus two completion defects of size at least a fixed constant forces a fixed physical diagonal, fixed physical cross edge, or fixed-cardinality physical principal block of comparable size carrying either defect.

The family `A_m` has scalar-core defect sizes `1,1`, `sigma_min(M)=2-sqrt(3)`, and full `s_3(A_m)=1`, while every physical coefficient is `O(1/m)` and every fixed `k x k` principal block has operator norm `O(k/m)`.

This refutes a proof mechanism only. It does not refute the QFORM conjecture.

## 4. Group aggregation closes the witness exactly

Take every physical input coordinate to be an independent standard Gaussian. This is a target-valid input law because its density is at most `(2pi)^(-1/2)<1`.

The five grouped variables `U,V,W,Z,T` are then independent standard Gaussians. Therefore

`Q_m=(U+V+W)^2+(U+Z)^2+(V+T)^2`.

Condition on `(U,V)`. Then the three terms become shifted squares of the independent variables `W,Z,T`:

`(W+U+V)^2`, `(Z+U)^2`, `(T+V)^2`.

For any real random variable `Y` with density bounded by one, the shifted square `(Y-a)^2` has density bounded by `y^{-1/2}` on `y>0`. Hence the convolution of the first two conditional square densities is bounded by

`integral_0^s [u(s-u)]^(-1/2) du = pi`.

Convolution with the third independent square cannot increase the `L^infinity` norm. Thus for every conditioning value `(U,V)`,

`||p_(Q_m | U,V)||_infinity <= pi`,

and averaging gives

`||p_(Q_m)||_infinity <= pi`.

The first two square densities are in `L^1`; their convolution is continuous and vanishes at infinity. The same is true after convolving with the third square, and dominated convergence under the uniform `pi` cap shows that `p_(Q_m)` is continuous. Thus this target-valid family is uniformly paid even though all physical coefficients vanish with `m`.

The correct currency is therefore grouped-coordinate curvature, not a bounded physical pivot.

## 5. Designated partner result applied to an actual inequality

The completed account02/B01 r27 theorem (`QFORM-CROSS-EDGE-POINTWISE-v1`) states that for every actual physical off-diagonal coefficient `b=A_ik!=0`, with all other couplings arbitrary,

`|phi_Q(t)| <= min(1,sqrt(pi/(|t b|)))`.

For the family above every physical off-diagonal coefficient obeys `|b|<=2/m`. Hence every application of that physical-edge corollary gives at best

`|phi_(Q_m)(t)| <= min(1, sqrt(pi m/(2|t|)))`.

The coefficient deteriorates like `m^(1/2)` inside the squared bound (equivalently `m^(1/2)` in `pi/(|tb|)` and `m^(1/2)` under the square root as written), and the exponent `1/2` is nonintegrable in time. Thus the partner theorem rigorously confirms that **physical-edge leakage currency alone cannot recover the two diffuse defect directions in this family**.

At the grouped level, however, the relevant aggregate cross coefficients in `(u+z)^2` and `(v+tau)^2` equal one. Applying the partner's unnormalized overlap theorem to these independent grouped variables has no `m`-loss. This is exactly the aggregation-before-inversion behavior required by the witness.

## 6. Consequence for the global proof architecture

The prior defect lemma remains useful, but its correct continuation is not

`two defects -> two physical pivots`.

The source-valid continuation must be something of the form

`two defects -> two grouped quadratic sources`,

followed by a product-preserving theorem that either:

1. pays a grouped rank-one square directly from the density of its linear aggregate;
2. if the defect is absorbed by internal coupling, promotes that coupling to a new grouped aggregate and recurses on a monotone spectral invariant; or
3. routes the resulting bank to an already-paid ridge/random-slope/two-pivot branch.

The family above shows why any recursion that pays a reciprocal largest physical entry or fixed principal minor can diverge even when the exact three-eigenvalue resource stays equal to one.

A promising next object is therefore a **grouped defect potential**: for each defect bank, measure the largest squared singular value of the map from the scalar aggregate to the entire orthogonal bank before selecting coordinates. The family has grouped potential exactly one while every physical coefficient is `O(1/m)`.

## 7. Status

Classification: `CANDIDATE_REFUTED / ESSENTIAL_STEP_APPLIED`.

Refuted intermediate mechanism: uniformly large completion defects do **not** force uniformly large physical pivots/edges/fixed principal blocks.

Positive result: the exact diffuse witness is uniformly bounded, with continuous density and `||p_Q||_infinity<=pi`, by conditioning after the correct group aggregation.

Full QFORM: **OPEN**. Full continuity theorem: **OPEN**.

First unpaid implication: prove a general grouped-defect recursion/energy inequality that pays the whole aggregate coupling norm before coordinate selection, and show that it terminates or routes to an existing paid branch under only `s_3(A)>=1`.
