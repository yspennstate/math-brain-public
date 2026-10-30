# fleet01/B09 — rank-r bilinear-cut Plancherel theorem and rank-three definite closure

Run: `20260922T114609Z-fleet01-B09-qform-bilinear-v1`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: `Bilinear block mechanism`  
Classification: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and corrections

The live target is the arbitrary-dimensional quadratic-form density conjecture for independent real coordinates with densities at most one and at least three eigenvalues of absolute value at least one. FEI is superseded by the later owner control.

Consumed corrections: `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, and the fresh partner event `QFORM-CROSSMINOR-ALONE-FALSE`. In particular no law-uniform one-variable Fresnel decay, rotated-coordinate independence, or unrestricted spectral-fiber supremum is used.

Named partner actually applied: fleet02/B09, run `20260922T115241Z-fleet02-B09-QFORM-r1`, canonical report commit `fa592b592c61bd1597aa8cf3270c3c9f58f410bf`. Its exact counterexample

`Q=(X1+Y1)^2-(X2+Y2)^2`

has an invertible rank-two cross block but logarithmically unbounded density. This is used below as the sharp `r=2` boundary of the new rank-`r>=3` theorem. The partner's safe zero-pivot theorem is complementary: it succeeds already at rank two because it conditions to a genuinely linear pivot packet.

Other source-backed inputs actually used:

1. fleet04/B18, handoff `20260922T113729Z-fleet04-B18-qform-r1`: if `R` has density at most `M` and conditionally on `R` a variable `V` has density at most one, then `R+aV^2` has density at most `2 sqrt(M/|a|)`.
2. fleet02/B06, run `b06-20260922T113045Z-d47192d10a82`: fixed physical-pair localization fails on a delocalized rank-three Hadamard family, while exterior determinant mass remains normalized.
3. Livshyts--Paouris--Pivovarov, arXiv:1507.07949: if `F(x)=prod f_i(x_i)` with each one-dimensional density bounded by one, every `r`-dimensional orthogonal marginal density is bounded by `2^(r/2)`.

## 2. A global bilinear-cut theorem

### Theorem 2.1 — `QFORM-RANKR-BILINEAR-PLANCHEREL-v1`

Let `X=(X_1,...,X_n)` have independent coordinates with densities `f_i<=1`, and let `A` be real symmetric. Let `S,T` be disjoint coordinate sets and put `B=A[S,T]`. Suppose `rank(B)=r>=3`, with nonzero singular values `s_1,...,s_r`, and set

`D=prod_{j=1}^r s_j(B)`.

Then `Q=X^T A X` has a bounded continuous density and

`||p_Q||_infinity <= [2r/(r-2)] D^(-1/r)`.

Equivalently, every interval `L` satisfies

`P{Q in L} <= [2r/(r-2)] D^(-1/r) |L|`.

For `r=3`,

`||p_Q||_infinity <= 6 (s_1 s_2 s_3)^(-1/3)`.

The theorem allows arbitrary principal curvature on both sides and arbitrary coupling to coordinates outside `S union T`.

### Proof

Condition on every coordinate outside `S union T`. Under this conditioning the two blocks `u=X_S` and `v=X_T` remain independent with product densities bounded coordinatewise by one, and

`Q = g(u)+2 u^T B v+h(v)+c`,

where `g,h` are arbitrary real quadratic-affine functions and `c` is fixed.

Take a thin singular-value decomposition `B=U Sigma V^T`, where `U,V` have `r` orthonormal columns and `Sigma=diag(s_1,...,s_r)`. Complete `U,V` to orthogonal bases and write

`u=Uy+U_0 xi`, `v=Vz+V_0 eta`.

Define the complex marginal amplitudes

`a_t(y)=int exp(i t g(Uy+U_0 xi)) F_S(Uy+U_0 xi) dxi`,

`b_t(z)=int exp(i t h(Vz+V_0 eta)) F_T(Vz+V_0 eta) deta`.

Their absolute values are bounded by the genuine `r`-dimensional projection densities `rho_S(y),rho_T(z)`. By the Livshyts--Paouris--Pivovarov marginal theorem,

`||rho_S||_infinity, ||rho_T||_infinity <= 2^(r/2)`.

They are probability densities, hence

`||a_t||_2,||b_t||_2 <= 2^(r/4)`.

The conditional characteristic function becomes

`phi(t)=e^(itc) int int a_t(y)b_t(z) exp(2 i t y^T Sigma z) dy dz`.

With Fourier convention `hat a(xi)=int a(y)e^(i xi.y)dy`, Plancherel gives

`|int int a(y)b(z)e^(2it y^T Sigma z)dy dz|`
`<= pi^(r/2) |t|^(-r/2) D^(-1/2) ||a||_2 ||b||_2`.

Therefore

`|phi(t)| <= min(1,(2 pi)^(r/2)|t|^(-r/2)D^(-1/2)).`

Put `t0=2 pi D^(-1/r)`. Since `r>2`, direct integration yields

`int_R |phi(t)|dt`
`<= 2[t0+(2pi)^(r/2)D^(-1/2) int_{t0}^infinity t^(-r/2)dt]`
`=4 pi [r/(r-2)]D^(-1/r)`.

Fourier inversion therefore gives a bounded continuous conditional density with

`||p||_infinity <= (1/(2pi)) int |phi| <= [2r/(r-2)]D^(-1/r)`.

The constant is uniform in all conditioned coordinates, so averaging over them preserves the same bound. QED.

### Square-block improvement

If `|S|=|T|=r`, no projection theorem is needed: the original block joint densities have `L2` norm at most one. The identical calculation gives

`||p_Q||_infinity <= [r/(r-2)] |det B|^(-1/r)`.

For a nonsingular `3x3` cross block this is `3 |det B|^(-1/3)`.

## 3. Why rank two is exactly excluded

The fresh fleet02/B09 partner correction is not a technical nuisance; it is the endpoint obstruction. For independent `Uniform[-1/2,1/2]` variables,

`Q=(X1+Y1)^2-(X2+Y2)^2`

has cross block `diag(1,-1)` of determinant `-1`. If `Z=X+Y`, then `Z` has triangular density `1-|z|` on `[-1,1]`, and `Z^2` has density `h(s)=s^(-1/2)-1` on `(0,1)`. Hence the density of the difference at zero contains

`int_0^1 h(s)^2 ds=infinity`.

In Theorem 2.1 the time tail is `|t|^(-r/2)`; exactly at `r=2` it becomes `1/|t|`, reproducing the logarithmic endpoint. Thus `r>=3` is sharp for this general separable-phase bilinear mechanism. This does not contradict the partner's rank-two zero-pivot theorem, where the same-side quadratic obstruction is absent and direct linear conditioning is stronger.

## 4. Rank-three determinant-mass cut

### Proposition 4.1 — `QFORM-RANK3-VOLUME-CUT-v1`

Suppose `rank(A)=3` and write

`A=R Lambda R^T`,

where `R` is `n x 3` with orthonormal columns and all three diagonal entries of `Lambda` have absolute value at least one. Put

`ell_i=||R_{i,*}||_2^2`, `delta=max_i ell_i`.

For each three-set `I`, let

`w_I=det(R_I)^2`.

Then

`sum_I w_I=1`, `sum_{I containing i}w_I=ell_i`.

Consequently the total weight of ordered disjoint basis pairs obeys

`M_disj:=sum_{I cap J=empty}w_Iw_J >= 1-sum_i ell_i^2 >= 1-3 delta`.

If `M_disj>0`, there exists a coordinate cut `S,T=S^c` for which the cross block `A[S,T]` has rank three and singular product `D` satisfying

`D >= sqrt(M_disj)/8`.

Therefore

`||p_Q||_infinity <= 12 M_disj^(-1/6) <= 12(1-3delta)^(-1/6)`

whenever `delta<1/3`.

### Proof

Cauchy--Binet gives `sum_I w_I=det(R^T R)=1`. To get the one-point marginal, scale row `i` of `R` by `t`. Cauchy--Binet gives

`det(R(t)^T R(t))=1+(t^2-1) sum_{I containing i}w_I`,

while the matrix determinant lemma gives the same determinant as

`det(I+(t^2-1)R_i^T R_i)=1+(t^2-1)ell_i`.

Thus the inclusion identity follows. For two independent three-sets with law `w`, a union bound gives

`P(I cap J != empty)<=sum_i ell_i^2`,

proving the lower bound for `M_disj`.

Now put each coordinate independently in `S` or `T` with probability `1/2`. Cauchy--Binet gives

`det(R_S^T R_S)=sum_{I subset S}w_I`,
`det(R_T^T R_T)=sum_{J subset T}w_J`.

Taking expectations of the product leaves only disjoint `(I,J)` and each such ordered pair is separated with probability `2^-6`, so

`E[det(R_S^T R_S)det(R_T^T R_T)]=M_disj/64`.

Some cut therefore has at least this product. Thin QR factorizations of `R_S,R_T` give the exact cross singular-product identity

`prod_{j=1}^3 s_j(A[S,T])`
`=|det Lambda| sqrt(det(R_S^T R_S)det(R_T^T R_T))`.

Since `|det Lambda|>=1`, the claimed lower bound on `D` follows; Theorem 2.1 then gives the density estimate. QED.

This directly defeats the fixed-minor delocalization obstruction recorded by fleet02/B06: the argument never selects one large physical minor. It aggregates all Pluecker mass first and only then chooses a cut.

## 5. Complete bounded-density theorem for rank-three definite forms

### Theorem 5.1 — `QFORM-RANK3-DEFINITE-UNIVERSAL-v1`

Assume in addition that `A` has rank exactly three and its three nonzero eigenvalues have one sign, with absolute values at least one. Then, for arbitrary independent coordinate densities bounded by one,

`||p_{X^TAX}||_infinity < 13.5`.

No dimension, support, moment, continuity, or identical-law assumption is required.

### Proof

By replacing `A` with `-A`, assume `Lambda=diag(lambda_1,lambda_2,lambda_3)` with each `lambda_j>=1`. Let `delta=max ell_i` as above.

**Delocalized case: `delta<1/6`.** Proposition 4.1 gives `M_disj>1/2`, hence

`||p_Q||_infinity <=12*2^(1/6)<13.5`.

**Localized case: `delta>=1/6`.** Choose `i` with `ell_i=delta`, write the coordinate block decomposition

`A=[[a,b^T],[b,C]]`, `a>0`,

and let `S=C-bb^T/a` be the Schur complement. Then

`Q=a(X_i+b^T Y/a)^2+Y^T S Y`.

Because `A` is positive semidefinite of rank three, `S` is positive semidefinite of rank two. We claim the exact identity

`pdet(S)=det(Lambda) ell_i/a`.

Indeed, writing `q=R_{i,*}` and `R_-` for the remaining rows,

`S=R_- M R_-^T`,
`M=Lambda-Lambda q^T q Lambda/a`.

Since `Mq^T=0` and `R_-^T R_-=I-q^Tq`, the two nonzero eigenvalues of `S` equal those of `M`. The rank-two adjugate identity gives

`adj(M)=det(Lambda) q^Tq/a`,

so `pdet(M)=tr adj(M)=det(Lambda) ell_i/a`, proving the claim.

Let the two positive eigenvalues of `S` be `mu_1,mu_2`. The two-dimensional spectral projection of the product law of `Y` has density at most `2` by Livshyts--Paouris--Pivovarov. After scaling by `sqrt(mu_1),sqrt(mu_2)`, the planar density is at most `2/sqrt(pdet S)`. Passing to squared radius gives

`||p_{Y^T S Y}||_infinity <=2pi/sqrt(pdet S)`.

Now apply fleet04/B18's dependent square-smoothing lemma to

`R=Y^T S Y`, `V=X_i+b^TY/a`.

Conditionally on any value of `R`, `V` is a mixture of translates of `X_i`, so its density is still at most one. Therefore

`||p_Q||_infinity`
`<=2 sqrt((2pi/sqrt(pdet S))/a)`
`=2 sqrt(2pi) (a det(Lambda) ell_i)^(-1/4)`
`<=2 sqrt(2pi) ell_i^(-1/2)`
`<=2 sqrt(12pi)<12.3`.

Combining the two cases proves the displayed universal bound. QED.

This closes a genuine rotated, high-dimensional family that fixed coordinate triples need not control. It is still only the rank-exactly-three definite subclass and is not the full owner conjecture.

## 6. Conditional end-to-end route and first missing implication

A compact route now is:

1. If some disjoint coordinate cut has cross rank `r>=3` with singular geometric mean bounded below, Theorem 2.1 closes the target directly, allowing arbitrary same-side curvature.
2. In an exactly rank-three delocalized spectral subspace, Proposition 4.1 manufactures such a cut from aggregate Pluecker mass.
3. In the exactly rank-three definite localized branch, fleet04/B18 square smoothing closes the remaining case, yielding Theorem 5.1.
4. The full conjecture therefore reduces, on this pathway, to handling extra spectral components and the localized indefinite rank-three geometry without allowing those components to cancel the useful cross cut.

The first essential unpaid implication is:

`QFORM-INDEFINITE-LOCALIZED-OR-EXTRA-SPECTRUM-BRIDGE-v1`: from the full hypothesis of at least three eigenvalues `|lambda|>=1`, prove a product-coordinate decomposition/averaging which either produces a rank-`>=3` cross cut with controlled singular product, or produces one of the existing local square/definite-pair/nonsingular-triple smoothers, with constants stable under all remaining spectral components.

The fresh partner counterexample shows why a bare rank-two cross minor cannot be one of those alternatives unless the pivot-side curvature is also controlled.

## 7. Status

Outcome: `ESSENTIAL_STEP_APPLIED`.

Proved this run:
- `QFORM-RANKR-BILINEAR-PLANCHEREL-v1`;
- `QFORM-RANK3-VOLUME-CUT-v1`;
- `QFORM-RANK3-DEFINITE-UNIVERSAL-v1`.

Full QFORM conjecture: `OPEN / NOT PROVED / NOT DISPROVED`.

No numerical experiment is used as proof. The only external theorem invoked is the sharp bounded-marginal theorem of Livshyts--Paouris--Pivovarov; all remaining arguments are explicit analytic identities plus the named source-backed worker lemmas above. Novelty beyond the fleet context is not asserted.
