# account01/B16 — conditional rank-three projection sup-moment obstruction

**Run:** `20260922T181326Z-account01-B16-qform-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control source:** `yspennstate/math-research-brain@1f592e9d683afe480b7b004ec26caa38c262501c` (owner-control revision `2026-09-22.11`; later source revalidation observed `a2a38404d3cefcaf4530aa41a2725887a9373d29`)  
**Assignment:** Projection-product interaction  
**Classification:** `ESSENTIAL_STEP_APPLIED / SOURCE-VALID REFUTATION OF CONDITIONAL-MOMENT ROUTE / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and exact implication tested

The full target remains open: for independent real coordinates with densities bounded by one and a real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `Q=X^TAX`.

The owner message records the tempting rank-three conditioning reduction

`||p_Q||_infinity <= K E_Z ||rho_{E|Z}||_infinity^(2/3)`

for a three-dimensional spectral subspace `E`, and identifies a dimension-free bound on the conditional `2/3`-moment as a possible route to the full-rank theorem. This report shows that the required conditional-moment bound is false even for cap-one product cubes and even when the selected three-dimensional subspace is exactly the spectral range of a rank-three target form.

The failure is not a counterexample to QFORM. On the same family the actual quadratic output is uniformly bounded, and this is proved below by applying the completed designated partner theorem account02/B16.

## 2. Product-cube family

Fix `m>=2`. Let

`X=(X_0, X^(1)_1,...,X^(1)_m, X^(2)_1,...,X^(2)_m)`

have independent `Uniform[-1/2,1/2]` coordinates. Thus the joint density is exactly one on the cube and zero outside.

Let

`u_1 = m^(-1/2)(1,...,1)` on block 1,
`u_2 = m^(-1/2)(1,...,1)` on block 2,

and define the three-dimensional orthogonal subspace

`E = span{e_0,u_1,u_2}`.

Let `F=E^perp`, and write `Y=P_E X`, `Z=P_F X`. The rank-three quadratic form

`Q_m = <X,e_0>^2 + <X,u_1>^2 - <X,u_2>^2`

has nonzero eigenvalues exactly `{1,1,-1}`.

## 3. Exact fiber geometry for one diffuse block

Consider first a single block `x=(x_1,...,x_m) in [-1/2,1/2]^m`. Put

`u=m^(-1/2)(1,...,1)`, `t=<x,u>`, `z=P_{u^perp}x`.

For fixed `z`, the admissible values of `t` are the intersection of the `m` intervals imposed by

`z_k+t/sqrt(m) in [-1/2,1/2]`.

Since subtracting the common mean does not change coordinate range, the fiber length is

`L(z)=sqrt(m) [1-R(z)]_+`,

where `R(z)=max_k z_k-min_k z_k`. If `X_1,...,X_m` are iid uniform on an interval of length one and `R=max X_i-min X_i`, then the orthogonal change `(t,z)<->x` has Jacobian one, and therefore for every real `alpha` for which the integral is finite,

`integral_{u^perp} L(z)^alpha dz = E[L(P_{u^perp}X)^(alpha-1)]`.

For `alpha=1/3`,

`J_m := integral L(z)^(1/3) dz
      = m^(-1/3) E[(1-R)^(-2/3)].`

The range of `m` iid `Uniform[0,1]` variables has density

`f_R(r)=m(m-1) r^(m-2)(1-r),  0<r<1`.

Hence

`J_m
 = m^(-1/3) m(m-1) B(m-1,4/3)
 = m^(-1/3) Gamma(m+1) Gamma(4/3) / Gamma(m+1/3).`      (3.1)

By the standard gamma-ratio asymptotic,

`J_m = Gamma(4/3) m^(1/3)(1+o(1)).`                    (3.2)

## 4. Exact divergence of the conditional 2/3-moment

In the full two-block construction, the `e_0` coordinate contributes a fiber interval of length one. The two diffuse blocks factor orthogonally. Thus the `E`-fiber volume at `z=(z_1,z_2)` is

`H(z)=L(z_1)L(z_2)`.

Because the ambient cube density equals one, the marginal density of `Z` is exactly `H(z)`, while the conditional density of `Y|Z=z` is uniform on the rectangular fiber and therefore has

`||rho_{E|Z=z}||_infinity = H(z)^(-1)`

for almost every nonempty fiber. Consequently

`E_Z ||rho_{E|Z}||_infinity^(2/3)
 = integral H(z)^(1/3) dz
 = J_m^2.`                                                   (4.1)

Combining (3.1)-(3.2),

`boxed(
 E_Z ||rho_{E|Z}||_infinity^(2/3)
 = [m^(-1/3) Gamma(m+1)Gamma(4/3)/Gamma(m+1/3)]^2
 = Gamma(4/3)^2 m^(2/3)(1+o(1)) -> infinity.
)`                                                           (4.2)

Therefore there is no universal constant `C` such that

`E_Z ||rho_{E|Z}||_infinity^(2/3) <= C`

for all cap-one product laws and all three-dimensional orthogonal projections. This remains false even when `E` is the exact spectral range of a rank-three form with eigenvalues `{1,1,-1}`.

This strengthens the older fiber-supremum dimension-loss correction: the scaling-correct `2/3` conditional moment also diverges.

## 5. The quadratic output stays uniformly bounded: actual use of account02/B16

Now apply the completed designated partner theorem

`account02/B16, run 20260922T163840Z-account02-B16-qform-r13`,
canonical report `yspennstate/math-open-problems@d2e3dd1587a3fa93707631ea847c48279f3dc6dc`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T163840Z-account02-B16-qform-r13/REPORT.md`.

Take the rank-two projected variable

`Y_2=(X_0, <X,u_2>)`

with indefinite matrix

`S=diag(1,-1)`.

The physical row corresponding to `X_0` is `(1,0)`, so its leverage is exactly

`ell=1`.

The remaining positive square

`L=<X,u_1>`

is a normalized linear form on a disjoint original-coordinate bank and is independent of all variables determining `Y_2`. The one-dimensional bounded-density projection theorem used in the partner report gives

`||p_L||_infinity <= sqrt(2)`.

Equation (5.2) of the completed partner report therefore applies with

`ell=1`, `gamma=1`, `|det S|=1`.

Thus

`boxed(
 ||p_{Q_m}||_infinity
 <= 2^(3/4) C_ind
 = 2^(3/4) * 8*3^(3/4)*5^(1/4)/sqrt(e)
 = 27.8162566595...,
)`                                                           (5.1)

uniformly in `m`.

So the conditional `2/3`-moment surrogate in (4.2) diverges like `m^(2/3)` while the actual target density is bounded by one fixed constant on the same exact family.

This is a direct proof that product aggregation must occur before, or jointly with, the nonlinear quadratic trace; conditioning onto the full orthogonal complement and then paying only the conditional `L^infinity` norm discards the decisive disjoint-bank structure.

## 6. Consequence for the full-proof route

The following implication is now ruled out:

> bounded unconditional three-dimensional projection density + rank-three coarea + a universal bound on `E ||rho_{E|E^perp}||_infinity^(2/3)`.

The last bound is false by (4.2).

The source-valid replacement must preserve more of the original-coordinate product provenance. The partner theorem shows one successful pattern: retain a physical heavy row in an indefinite rank-two projection and supply the third square through a disjoint innovation bank. The still-unpaid full-target interface is genuinely overlapping innovation / arbitrary additional spectral components: one needs an aggregate inequality that identifies enough disjoint innovation before conditioning, or an overlap-safe analogue of the square smoother that does not assume a false conditional cap after rotation.

This report does not prove the full QFORM conjecture and makes no continuity claim.

## 7. Status

- `QFORM-FULL`: OPEN.
- New correction candidate: `QFORM-CONDITIONAL-RANK3-SUP-MOMENT-FALSE-v1`.
- Mathematical change: exact divergence formula (4.2), with a simultaneous uniform output-density bound (5.1) obtained from the designated partner theorem.
- Next step: replace full-complement conditioning by a product-preserving grouped-coordinate decomposition that extracts a disjoint innovation bank before the curved pushforward, or prove an overlap-safe smoother.
