SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-24T03:54:56Z.
attacking: the fully diffuse near-coloop two-sheet survivor; test whether the single-hub mixed slice norm can be controlled from product-projection provenance, and isolate the exact replacement when it cannot.

# account01/B10 — diffuse product projections do not control the single-hub mixed slice norm

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case  
Status: `NEW_RIGOROUS_INTERFACE_COUNTEREXAMPLE / PARTNER_RESULT_APPLIED / EXACT_TARGET_CONTROL / FULL_EXACT_RANK3_OPEN / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source and correction boundary

Fresh owner control was read from `yspennstate/math-research-brain` and refreshed before publication at commit

`56c207cafad78da449e2bd084dd9a746b5e03d4c`,


This report does **not** use independence after rotation, an arbitrary-joint coarea cap, a conditional projection-height bound, law-uniform pointwise quadratic-phase decay, moments, support regularity, compactness, finite fragmentation, or deletion of a small random term.

The newest completed designated partner input actually used is

`yspennstate/math-open-problems@2181d0927de1374b092152c7e6fb51920e5ae40d`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/account02-B10-20260924T004626Z-auto11/REPORT.md`.

Its Theorem 3.1 is the regression-clean endpoint theorem. In its notation, for

`Q=2r(sqrt(c)H+T)Y+aY^2+2bYW+dW^2`,

if on an ORIGINAL leaf set `I` one has `t_i=gamma y_i+eta w_i` and `delta=det sum_(i in I)(y_i,w_i)^T(y_i,w_i)>0`, then

`||p_Q||_infinity <= 1/(2|r|sqrt(c)) + 16 delta^(-1/2)(|r|sqrt(c))^(-1/2)|d|^(-1/2)`.   (1.1)

The partner also exhibits a fully diffuse harmonic survivor showing that a uniformly good exact regression-clean set need not exist in general. I use (1.1) below on an actual target family, not merely as a citation.

## 2. The mixed norm that one would like to bound

The current one-hub real-variable receiver naturally introduces, for a three-dimensional leaf projection density `rho(z,y,w)`,

`M(rho):=sup_y int_R sup_w rho(z,y,w) dz`.                              (2.1)

A tempting route through the remaining diffuse near-coloop chamber is to hope that `M(rho)` is bounded by an absolute constant whenever `rho` is an orthogonal projection of an independent cap-one product law and the physical row leverages are small.

The first substantive step of this run was to test that implication directly. It is false, even in fixed dimension and with leverage `<1/61`.

## 3. Theorem — diffuse orthogonal product projections have unbounded mixed slice norm

### Theorem 3.1 — `QFORM-DIFFUSE-PROJECTION-MIXED-NORM-UNBOUNDED-v1`

Fix `m=64`. For every `L<infinity` there are `3m=192` independent real random variables with probability densities bounded by one and a matrix `U in R^(3m x 3)` with `U^T U=I_3` such that every physical row has squared leverage exactly `1/m=1/64<1/61`, while the density `rho` of `U^T X=(Z,Y,W)` satisfies

`M(rho)=sup_y int_R sup_w rho(z,y,w) dz > L`.                           (3.1)

Moreover scaling the first projected coordinate by any nonzero factor leaves this mixed norm unchanged after the corresponding density rescaling. Hence a small longitudinal coefficient does not repair (3.1).

### Proof

Split the `3m` original coordinates into three blocks `A,B,C`, each of size `m`. Define

`Abar=(1/sqrt(m)) sum_(i in A) X_i`,
`Bbar=(1/sqrt(m)) sum_(i in B) X_i`,
`Y=(1/sqrt(m)) sum_(i in C) X_i`,

and

`Z=(Abar+Bbar)/sqrt(2)`, `W=(Abar-Bbar)/sqrt(2)`.                       (3.2)

Thus the rows of the coefficient matrix for `(Z,Y,W)` are

- on block `A`: `(1/sqrt(2m),0,1/sqrt(2m))`;
- on block `B`: `(1/sqrt(2m),0,-1/sqrt(2m))`;
- on block `C`: `(0,1/sqrt(m),0)`.

The three columns are orthonormal, and every row has squared norm `1/m`.

Let `h_m` be the density of `S_m=U_1+...+U_m` for iid `U_i~Uniform[0,1]`. Since `h_m` is continuous and strictly positive on `(0,m)`, fix a compact interval `J` around `m/2` with

`|J|=:ell_m>0`, `h_m(x)>=a_m>0` for `x in J`.                          (3.3)

Let `N` be a large integer and set the integer base `B_0=10N`. For the first `2m` original coordinates, indexed by `r=0,...,2m-1`, take

`E_r = union_(k=0)^(N-1) [k B_0^r, k B_0^r + 1/N]`,
`f_r=1_(E_r)`.                                                        (3.4)

Each `E_r` has Lebesgue measure one, so `f_r` is an admissible probability density with cap one. On the `C` block use `Uniform[0,1]` laws.

For one digit vector `alpha=(alpha_1,...,alpha_m) in {0,...,N-1}^m`, conditioning the `A`-block coordinates to their selected component intervals gives

`Abar = a_alpha + (1/(N sqrt(m))) S_m`,
`a_alpha=(1/sqrt(m)) sum_(r in A) alpha_r B_0^r`.                      (3.5)

The digit vector has probability `N^(-m)`. Therefore on the core interval

`I_alpha := a_alpha + J/(N sqrt(m))`,

its contribution to the unconditional density of `Abar` is at least

`p_Abar(x) >= a_m sqrt(m) N^(1-m)`, `x in I_alpha`.                    (3.6)

The same statement holds for every `B`-block digit vector `beta`, with core `I_beta'`.

Because the `2m` digit positions use distinct powers of the base `B_0>N`, every combined digit vector `(alpha,beta)` has a distinct integer base expansion. Consequently the centers of

`K_(alpha,beta):=(I_alpha+I_beta')/sqrt(2)`                            (3.7)

are separated by at least `1/sqrt(2m)`. For all sufficiently large `N`, the `K_(alpha,beta)` are pairwise disjoint. Each has length

`|K_(alpha,beta)| = sqrt(2) ell_m/(N sqrt(m))`.                        (3.8)

If `z in K_(alpha,beta)`, choose `a in I_alpha`, `b in I_beta'` with `(a+b)/sqrt(2)=z` and set `w=(a-b)/sqrt(2)`. The orthogonal change `(Abar,Bbar)<->(Z,W)` has Jacobian one, hence

`p_(Z,W)(z,w)=p_Abar(a)p_Bbar(b)
             >= a_m^2 m N^(2-2m)`.                                   (3.9)

There are `N^(2m)` disjoint intervals (3.7), so (3.8)-(3.9) give

`int_R sup_w p_(Z,W)(z,w) dz
 >= a_m^2 m N^(2-2m) N^(2m) sqrt(2) ell_m/(N sqrt(m))
 = a_m^2 ell_m sqrt(2m) N`.                                          (3.10)

The `C` block is source-disjoint from the first two blocks, so

`rho(z,y,w)=p_Y(y) p_(Z,W)(z,w)`.                                    (3.11)

At `y_0=sqrt(m)/2`,

`p_Y(y_0)=sqrt(m) h_m(m/2)=:b_m>0`.                                  (3.12)

Combining (3.10)-(3.12),

`M(rho) >= b_m a_m^2 ell_m sqrt(2m) N -> infinity`.                   (3.13)

This proves (3.1).

Finally, if `T=sqrt(epsilon) Z`, then

`rho_(T,Y,W)(t,y,w)=epsilon^(-1/2) rho(t/sqrt(epsilon),y,w)`,

and therefore the change `t=sqrt(epsilon)z` gives the exact scale invariance

`sup_y int sup_w rho_(T,Y,W)(t,y,w) dt = M(rho)`.                     (3.14)

Thus even arbitrarily small nonzero longitudinal leakage does not make the raw mixed norm finite uniformly over admissible rough laws. QED.

### Significance

This is stronger than the already-known high-dimensional fiber-supremum warning in one important sense: dimension is fixed (`192`) and the projection frame is genuinely diffuse (`1/64` row leverage). The failure comes entirely from allowed fragmentation/separation of the one-dimensional source laws.

It refutes only the proposed intermediate interface

`diffuse orthogonal product projection => universal M(rho)`.

It does **not** refute the quadratic-form conjecture.

## 4. Embed the barrier in an exact target-valid near-coloop family

Fix any `0<epsilon<1/64` and put `c=1-epsilon`. Add one independent ORIGINAL hub variable `H` with density cap one. Use the same three normalized leaf projections `(Z,Y,W)` from Section 3, and form the spectral frame with columns

`R_1 = sqrt(c) e_H + sqrt(epsilon) Z`,
`R_2 = Y`,
`R_3 = W`.                                                           (4.1)

In ORIGINAL-coordinate row notation this means

- hub row: `(sqrt(c),0,0)`;
- `A` leaves: `(sqrt(epsilon)/sqrt(2m),0,1/sqrt(2m))`;
- `B` leaves: `(sqrt(epsilon)/sqrt(2m),0,-1/sqrt(2m))`;
- `C` leaves: `(0,1/sqrt(m),0)`.

The columns in (4.1) are orthonormal. In particular the nonhub rows are diffuse; their squared leverages are at most `(1+epsilon)/(2m)<1/61` or `1/m<1/61`.

Take

`M_0 = [[0,1,0],[1,0,0],[0,0,1]]`,                                   (4.2)

whose spectrum is exactly `{1,-1,1}`. Then

`A_target=R M_0 R^T`                                                  (4.3)

is an exact-rank-three instance of the owner target, and its quadratic form is

`Q=2(sqrt(c)H+sqrt(epsilon)Z)Y+W^2`.                                  (4.4)

For the leaf statistic `T=sqrt(epsilon)Z`, the raw single-hub mixed norm from (2.1) is still the quantity in (3.13), by (3.14), and can be made arbitrarily large by increasing `N`.

Thus the failure of the raw mixed-norm bridge occurs **inside an exact target-valid near-coloop family**, not merely for an unrelated projection.

## 5. Designated account02/B10 partner theorem applied to the same target family

The family (4.4) simultaneously shows why Theorem 3.1 of the designated partner is a stronger, product-preserving object than the raw mixed norm.

Use the partner's notation `r=d=1`, `a=b=0`, and leaf longitudinal coefficients `t_i=sqrt(epsilon) z_i`. Choose the ORIGINAL clean reservoir

`I = A-block union C-block`,
`gamma=0`, `eta=sqrt(epsilon)`.                                       (5.1)

On the `A` block, `z_i=w_i`, so `t_i=eta w_i`; on the `C` block, `t_i=w_i=0`, so the regression identity also holds. The transverse Gram on this same physical set is exactly

`G_I = diag(1,1/2)`, `delta=det G_I=1/2`.                             (5.2)

Substituting (5.2) into the completed account02/B10 inequality (1.1) gives the actual target-level estimate

`||p_Q||_infinity
 <= 1/(2 sqrt(c)) + 16 sqrt(2) c^(-1/4)`.                            (5.3)

Since `c>63/64`,

`boxed: ||p_Q||_infinity < 23.221.`                                   (5.4)

This bound is independent of the fragmentation parameter `N`, even though the raw mixed norm in (3.13) tends to infinity linearly in `N`.

Therefore (3.13) is decisively an obstruction to a **proof interface**, not a counterexample to QFORM. It also shows that exact original-coordinate regression can recover information that is destroyed by taking `sup_w` before using the algebraic overlap.

No new continuity conclusion is claimed from the partner theorem here.

## 6. Exact structural identity for the genuinely unpaid branch

For the generic exact-null near-coloop normal form

`Q=2r(sqrt(c)H+T)Y+aY^2+2bYW+dW^2`,                                  (6.1)

let `rho(z,y,w)` denote the joint density of

`Z=sqrt(c)H+T`, `Y`, `W`.                                             (6.2)

Because the three coefficient columns are orthonormal, `(Z,Y,W)` is an orthogonal projection of the ORIGINAL product law. For `y!=0`, the density pushforward has the exact trace formula

`p_Q(q)
 = int_R int_R [1/(2|r y|)]
   rho((q-a y^2-2b y w-d w^2)/(2r y), y, w) dw dy`.                  (6.3)

Equation (6.3), rather than a joint-density cap or the mixed norm (2.1), is the actual object that the remaining proof must bound.

The partner's harmonic family shows that a uniformly nondegenerate exact regression-clean reservoir need not exist; Theorem 3.1 above shows that replacing exact regression by a universal bound on the raw mixed norm is also impossible. The two failures are complementary.

Crucially, (6.3) still contains the parabolic `w^2` trace **before** any `sup_w`. That curvature is precisely what is lost in (2.1). The new first unpaid implication is therefore

`QFORM-DIFFUSE-PARABOLIC-TRACE-RECEIVER-v1`:

> For the fully overlapping exact-rank-three near-coloop survivor, bound the parabolic trace (6.3) directly from ORIGINAL product provenance and the aggregate diffuse transverse frame, uniformly as `c -> 1`, without first taking `sup_w`, extracting an exact regression zero set, assuming moments/support regularity, or declaring the projected coordinates independent.

The canonical controls for this implication are now:

1. the account02/B10 harmonic frame, which kills uniformly good exact-regression reservoirs;
2. the current fragmented block construction, which makes the raw mixed slice norm arbitrarily large while leaving an exact target output uniformly bounded by (5.4);
3. the rank-two opposite-sign logarithmic singularity, which forbids throwing away the third curvature.

A successful receiver has to spend the `w^2` curvature and product structure **before** the supremum or absolute-value operation that creates these barriers.

## 7. Scope and status

What is proved in this run:

1. `QFORM-DIFFUSE-PROJECTION-MIXED-NORM-UNBOUNDED-v1`, with a complete fixed-dimensional cap-one construction and exact linear lower bound in the fragmentation parameter;
2. scale invariance of that obstruction under arbitrarily small nonzero longitudinal leakage;
3. an exact embedding of the obstruction in a target-valid exact-rank-three near-coloop family with spectrum `{1,-1,1}`;
4. an actual application of the newest completed account02/B10 regression-clean theorem to that same family, giving `||p_Q||_infinity<23.221` despite the divergent raw mixed norm;
5. the exact parabolic-trace identity (6.3), identifying what must replace both failed interfaces.

What is **not** proved: the fully overlapping two-sheet endpoint, punctured-to-null uniform gluing in the partner harmonic survivor, arbitrary exact rank three, or full QFORM. No counterexample to the owner conjecture was found. Full-target continuity remains open.

This run uses repository transport only and remains `WITHOUT_VERIFIED_BRAIN`.
