# account03/B18 — conditional spectral-fiber moment obstruction and aggregate rescue

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B18, 2026-09-22T17:55:31Z.
attacking: the owner-proposed conditional 3-D projection-density `2/3`-moment bound, by an exact cube-fiber calculation and an aggregate-before-conditioning replacement using the account04/B18 square-smoothing lemma.

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control observed at mathematical start:** `b7325a4d01f03ddcd0dabbfbbdbecaec8e647a8d`, owner revision `2026-09-22.9`; refreshed before publication to the later owner revision `2026-09-22.10`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository retrieval is not native authenticated brain ingestion.  
**Full conjecture:** OPEN / NOT PROVED.

## 1. Exact target and purpose

The target is the unrestricted statement: for independent real coordinates with densities bounded by one and real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal finite `L^infinity` bound for the density of `X^T A X`, or give a valid counterexample.

The owner message proposed the following bridge for the full-rank case. Choose three large spectral directions `U` and condition on the orthogonal spectral complement `Z`; if one could prove

`E ||rho_(U^T X | Z)||_infinity^(2/3) <= C`

uniformly, then a rank-three coarea estimate could be averaged over `Z`.

This report proves that this conditional-moment bridge is false, even for admissible product uniforms and even for a full-rank target matrix with exactly three eigenvalues at the large threshold. The same geometry is nevertheless uniformly controlled by two aggregate-before-conditioning arguments. Thus the failure is a proof-method obstruction, not a counterexample to QFORM.

## 2. Source-valid literature input

Livshyts–Paouris–Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1, states: if `f(x)=prod_i f_i(x_i)`, every `f_i` is a probability density, and `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. For `k=1`, every unit linear form of the original independent coordinates has density at most `sqrt(2)`.

No Gaussianity, log-concavity, moment, compact-support, connected-support, or identical-law assumption is present. The theorem is used below only before any conditioning that would destroy the product structure.

Primary source: `https://arxiv.org/abs/1507.07949`, Theorem 1.1.

For the exact gamma-ratio lower bound below, Gautschi's inequality is used in the standard form

`x^(1-s) < Gamma(x+1)/Gamma(x+s) < (x+1)^(1-s)`, `x>0`, `0<s<1`.

## 3. The cube-fiber calculation

Fix `m>=2`. Let

`C_m=[-1/2,1/2]^m`, `u=m^(-1/2)(1,...,1)`, `H=u^perp`.

Let `X` be uniform on `C_m`, and write the orthogonal decomposition

`X = Y u + Z`, `Y=<u,X>`, `Z=P_H X`.

For `z in H`, the fiber of the cube along `u` is an interval in the `Y` coordinate. Its length is

`L_m(z)=sqrt(m) [1-(max_i z_i-min_i z_i)]_+`.

Indeed the constraints `-1/2 <= z_i + y/sqrt(m) <= 1/2` intersect to an interval whose length is exactly the displayed quantity.

Because the change `(y,z) -> yu+z` is orthogonal, the joint density of `(Y,Z)` is the indicator of the transformed cube. Therefore

`p_Z(z)=L_m(z)`,

and, for almost every `z` with positive fiber length,

`p_(Y|Z=z)(y)=1_(I_z)(y)/L_m(z)`.

Hence

`||p_(Y|Z=z)||_infinity = 1/L_m(z)`.

### Lemma 3.1 — exact conditional-sup moments

For `0<beta<2`,

`E ||p_(Y|Z)||_infinity^beta
 = m^(-beta/2) Gamma(m+1) Gamma(2-beta) / Gamma(m+1-beta).`

**Proof.** If `R=max_i X_i-min_i X_i` is the sample range, then subtracting the mean does not change the range, so

`L_m(P_H X)=sqrt(m)(1-R)`.

For `m` iid uniforms on an interval of length one, the range density is

`f_R(r)=m(m-1) r^(m-2)(1-r)`, `0<r<1`.

This follows directly from the joint density of the minimum and maximum. Therefore

`E L_m(Z)^(-beta)
 = m^(-beta/2) m(m-1) int_0^1 r^(m-2)(1-r)^(1-beta) dr`

`= m^(-beta/2) m(m-1) B(m-1,2-beta)`

`= m^(-beta/2) Gamma(m+1) Gamma(2-beta)/Gamma(m+1-beta)`.

QED.

For `beta>=2`, the same integral diverges at `r=1`, so the conditional-sup moment is already infinite.

## 4. Three blocks: the owner's `2/3` moment diverges linearly

Take three independent copies of the preceding `m`-coordinate cube block. Let `Y_1,Y_2,Y_3` be the three normalized block sums and let `Z=(Z_1,Z_2,Z_3)` collect the three orthogonal complements. Conditional on `Z`, the `Y_r` remain independent uniforms on their respective fiber intervals. Thus

`M_m(Z):=||rho_(Y_1,Y_2,Y_3 | Z)||_infinity
        = prod_(r=1)^3 L_m(Z_r)^(-1).`

By block independence and Lemma 3.1,

`E M_m(Z)^beta
 = [m^(-beta/2) Gamma(m+1) Gamma(2-beta)/Gamma(m+1-beta)]^3`

for `0<beta<2`.

At the exact exponent required by the owner bridge, `beta=2/3`,

`E M_m(Z)^(2/3)
 = m^(-1) [Gamma(m+1) Gamma(4/3)/Gamma(m+1/3)]^3.`

Gautschi's inequality with `x=m`, `s=1/3` gives

`Gamma(m+1)/Gamma(m+1/3) > m^(2/3)`.

Therefore

`boxed( E M_m(Z)^(2/3) > Gamma(4/3)^3 m ).`

In particular the proposed universal conditional `2/3`-moment estimate is false. More strongly, every positive conditional-sup moment is dimension-unbounded in this family (and moments `beta>=2` are infinite).

## 5. This obstruction occurs inside the exact QFORM spectral geometry

Let `u_1,u_2,u_3` be the normalized constant vectors on three disjoint size-`m` blocks and set `U=[u_1,u_2,u_3]`.

First consider

`A_m = U diag(1,1,-1) U^T`.

Its spectrum is `{1,1,-1,0,...,0}`, so it is an admissible QFORM matrix. Its quadratic form is

`Q_m = Y_1^2 + Y_2^2 - Y_3^2`.

The conditional moment from Section 4 diverges even though this is a legal target instance.

To put the same obstruction into the owner's stated full-rank conditioning geometry, fix `epsilon=1/128` and define

`A_(m,epsilon) = A_m + epsilon (I-UU^T).`

Its spectrum is exactly

`1,1,-1, epsilon,...,epsilon`.

Thus it is invertible, has exactly three eigenvalues with absolute value at least one, and all remaining spectral directions are precisely the `Z`-space used above. The conditional law `rho_(U^T X | Z)` is unchanged by the choice of eigenvalues, so

`E ||rho_(U^T X | Z)||_infinity^(2/3) > Gamma(4/3)^3 m -> infinity.`

Therefore the proposed conditional-moment bridge cannot follow from the bare full-rank three-large-eigenvalue hypothesis.

This is **not** a counterexample to the density conjecture. It only refutes that intermediate reduction.

## 6. Aggregate-before-conditioning rescue using the designated partner result

I substantively apply account04/B18's completed theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical report

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3:proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

That theorem proves: if `R` has density at most `M` and the conditional density of `V` given `R=r` is at most one, then

`||p_(R+aV^2)||_infinity <= 2 sqrt(M/|a|)`.

By scaling, if the conditional density cap is `K`, the bound becomes

`2 K sqrt(M/|a|)`.

Apply the LPP one-dimensional marginal theorem to each normalized block sum before conditioning. It gives

`||p_(Y_r)||_infinity <= sqrt(2)`.

Hence the density of `Y_r^2` satisfies, for `t>0`,

`p_(Y_r^2)(t) <= sqrt(2)/sqrt(t)`.

The two positive terms are independent across blocks, so for

`R=Y_1^2+Y_2^2`

we obtain the exact beta-integral bound

`||p_R||_infinity <= 2 int_0^s [u(s-u)]^(-1/2) du / 1`

that is,

`||p_R||_infinity <= 2 pi.`

Since `Y_3` is independent of `R` and has density cap `sqrt(2)`, the partner theorem with `a=-1`, `M=2pi`, `K=sqrt(2)` yields

`boxed( ||p_(Y_1^2+Y_2^2-Y_3^2)||_infinity <= 4 sqrt(pi) ).`

Thus the same rank-three family whose conditional `2/3` moment diverges linearly has a dimension-free target density bound after **aggregating each independent block first**. This rigorously isolates the loss: conditioning on the entire orthogonal complement destroys the useful product aggregation.

## 7. Full-rank perturbation is also uniformly controlled by an existing theorem

The completed spectral-window theorem in the live brain handoff

`scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/interactive/20260922T151048Z-ridge-window.md`

states that if `P` projects onto all eigenspaces with `|lambda|>=1/64` and `max_i P_ii<=1/32`, then the full form has a continuous density bounded by

`288 sqrt(3e)/13 < 64`.

For `A_(m,1/128)`, the high spectral projection is exactly `UU^T`, because `1/128<1/64`. Every physical coordinate belongs to one block and has leverage

`(UU^T)_(ii)=1/m`.

Therefore for every `m>=32`,

`max_i P_ii = 1/m <= 1/32`,

so the spectral-window theorem gives

`boxed( ||p_(X^T A_(m,1/128) X)||_infinity <= 288 sqrt(3e)/13 < 64 )`

and a continuous density, while simultaneously

`E ||rho_(U^T X | Z)||_infinity^(2/3) > Gamma(4/3)^3 m`.

This is an especially clean proof that the divergent conditional moment is a methodological artifact rather than actual concentration of the quadratic form.

## 8. Consequence for the full proof architecture

The following intermediate claim must be retired:

> Uniformly over product cap-one laws and spectral decompositions with three large directions, the `2/3` moment of the conditional `3`-dimensional projection density after conditioning on the entire orthogonal spectral complement is bounded by an absolute constant.

It is false even for uniform cubes and even when the matrix is full-rank with spectrum `{1,1,-1,1/128,...,1/128}`.

A successful proof must keep enough original-coordinate randomness unconditioned until after an aggregate smoothing step. Two source-valid replacements are now explicit:

1. aggregate disjoint independent banks first, then use the account04/B18 dependence-safe square smoothing; and
2. in diffuse high-spectral-leverage geometry, use the one-scale ridge/spectral-window theorem without conditioning away the small-eigenvalue directions.

The remaining full-target implication is an exhaustive product-preserving dichotomy combining such aggregate/ridge mechanisms with the high-leverage grouped-coordinate branches. The present run does not prove that dichotomy.

## 9. Regularity and status

* New correction `QFORM-CONDITIONAL-3D-SUP-MOMENT-UNIFORM-FALSE-v1`: **proved**.
* Exact formula for all conditional sup moments of the cube-fiber example: **proved**.
* Rank-three aggregate rescue `||p_Q||_infinity<=4sqrt(pi)`: **proved**, by LPP plus account04/B18 square smoothing.
* Full-rank `epsilon=1/128`, `m>=32` rescue `<64`: **proved by direct application of the completed spectral-window theorem**.
* Continuity: supplied by the spectral-window theorem for the full-rank perturbation; not claimed from the account04/B18 square-smoothing wrapper alone.
* Full universal QFORM conjecture: **OPEN / NOT PROVED**.

## 10. Source pins

1. Livshyts, Paouris, Pivovarov, arXiv:1507.07949, Theorem 1.1.
2. DLMF 5.6.4 / Gautschi inequality for the exact gamma-ratio lower bound.
3. account04/B18 partner report at commit `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, exact path above.
4. Live ridge-window handoff, full proof source `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7:proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.
