SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B13, 2026-09-22T18:01:09Z.
attacking: target-valid stress of the proposed universal conditional active-3D density 2/3-moment after exact product-indicator reduction.

# account03/B13 — exact diagonal-chord law refutes the universal conditional 2/3-moment bridge

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T180109Z-account03-B13-qform-r13`  
**Assignment:** Extremal product laws  
**Classification:** `REFUTED_INTERMEDIATE_BRIDGE / EXACT_EXTREME-PRODUCT_GEOMETRY / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full quadratic-form bounded-density conjecture remains **OPEN / NOT PROVED**. The continuous-density conclusion also remains open in full generality.

This run tests the owner-message proposal that, after fixing three large spectral directions `Y` and conditioning on complementary spectral coordinates `Z`, one might close the full-rank problem from a universal bound on

`E_Z ||p_{Y|Z}||_infinity^(2/3)`.

That intermediate assertion is false, and it already fails on the exact extreme-product class singled out by the assigned partner account04/B13. In fact the conditional `alpha`-moment diverges polynomially for every `alpha>0` in a simple cube family. For the required exponent `alpha=2/3`, the moment is exactly asymptotic to `Gamma(4/3)^3 m = 0.712072942688... m`.

This is **not** a counterexample to QFORM. For the rank-three member of the family, a completed disjoint-bank theorem gives `||p_Q||_infinity <= 2*pi` uniformly in `m`. The result therefore identifies a genuinely lossy proof step: conditioning on the entire spectral complement before paying the rank-three trace can manufacture an order-`m` conditional-moment cost even when the actual quadratic output is uniformly bounded.

## 1. Fresh source state and partner result actually applied

At startup the current owner control was read from fresh `main`; the active programme remains QFORM only. The later natural-language proof-first continuation prioritizes full-target product-preserving grouped-coordinate reductions rather than solved controls.

The designated partner account04/B13 completed the fixed-volume random-set representation:

`yspennstate/math-open-problems`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T171018Z-b13-fixed-volume-mixture-r4/REPORT.md`.

It proves that every one-dimensional density `0<=f<=1`, `int f=1`, is an exact barycenter of indicators `1_E` with `|E|=1`, and that independent coordinates yield an exact product mixture of arbitrary unit-measure product indicators. Therefore the optimal slab constant over all admissible product densities equals the optimal constant over these extreme product laws; no interval, finite-fragment, bounded-support, or moment reduction is permitted.

I apply that result directly below: the counterfamily uses the most elementary legal extreme component, `E_i=[-1/2,1/2]`. Thus the failure occurs **after** the exact extremal reduction, not because a rough density was left untreated.

I also use the completed account03/B17 theorem
`QFORM-DISJOINT-THREE-BANK-2PI-v1`, source path
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260922T160432Z-account03-B17-QFORM-r12/REPORT.md`.
It proves that three active spectral vectors on pairwise disjoint original-coordinate banks, with coefficients of modulus at least one and arbitrary cap-one inputs, give `||p_Q||_infinity<=2*pi`.

The earlier account02/B17 correction `QFORM-CONDITIONAL-3D-PROJECTION-CAP-FALSE-v1` showed only that the **pointwise** conditional cap may diverge near a thin cube slice. The calculation below is stronger: the exact `2/3` moment proposed to compensate for thin slices diverges linearly with dimension.

## 2. One cube block and its diagonal chords

Fix an integer `m>=2`. Let

`C_m=[-1/2,1/2]^m`,
`u=m^(-1/2)(1,...,1)`.

Write every `x in R^m` uniquely as

`x=z+y u`,  with `z in u^perp` and `y=<u,x>`.

For `z in u^perp`, define the chord

`I_z={y: z+y u in C_m}`

and let `ell_m(z)=|I_z|`. Let

`D_m=P_{u^perp} C_m={z: ell_m(z)>0}`.

Because the map `x -> (y,z)` is orthogonal, if `X` is uniform on `C_m`, then the joint density of `(Y,Z)=(<u,X>,P_{u^perp}X)` is exactly `1_{z+y u in C_m}`. Consequently

`p_Z(z)=ell_m(z)`,

and, whenever `ell_m(z)>0`,

`p_{Y|Z=z}(y)=1_{I_z}(y)/ell_m(z)`,

so

`||p_{Y|Z=z}||_infinity=ell_m(z)^(-1)`.                 (2.1)

The chord length is explicit. Since `sum_i z_i=0`, the constraints

`-1/2 <= z_i + y/sqrt(m) <= 1/2`

give

`ell_m(z)=sqrt(m)[1-(max_i z_i-min_i z_i)]_+`.           (2.2)

Thus

`D_m={z in u^perp: max z_i-min z_i <=1}`.                (2.3)

### Exact chord superlevel volumes

For `0<=t<=sqrt(m)`, (2.2) and the homogeneity of the coordinate range give

`{z: ell_m(z)>t}=(1-t/sqrt(m)) int(D_m)`,

up to a null boundary. Hence

`|{ell_m>t}|=|D_m|(1-t/sqrt(m))^(m-1)`.                  (2.4)

Since the cube has volume one,

`1=int_{D_m} ell_m(z) dz
  =int_0^sqrt(m) |{ell_m>t}| dt
  =|D_m|/sqrt(m)`.

Therefore

`boxed(|D_m|=sqrt(m))`.                                  (2.5)

More generally, for every `q>0`, layer cake and (2.4) give the exact identity

`int_{D_m} ell_m(z)^q dz
 = q m^((q+1)/2) B(q,m)`.                                (2.6)

As checks, `q=1` gives one, while `q=2` gives

`int ell_m^2 = 2 sqrt(m)/(m+1)`.                         (2.7)

No asymptotic or numerical approximation is used in (2.6).

## 3. Three independent blocks: exact conditional-cap moments

Now take `n=3m` iid inputs

`X_1,...,X_{3m} ~ Uniform[-1/2,1/2]`.

Partition them into three consecutive blocks of size `m`. In each block use the diagonal vector `u`, and let `U in R^(3m x 3)` have these three disjointly supported unit vectors as columns. They are orthonormal.

Let

`Y=U^T X=(Y_1,Y_2,Y_3)`

and let `Z=(Z_1,Z_2,Z_3)` collect the three orthogonal within-block complements. Because the original blocks are independent,

`p_Z(z_1,z_2,z_3)=prod_{j=1}^3 ell_m(z_j)`,               (3.1)

and the conditional active density is the product of the three normalized chord indicators. Hence

`||p_{Y|Z=z}||_infinity=prod_{j=1}^3 ell_m(z_j)^(-1)`.    (3.2)

For every `0<alpha<1`, therefore,

`M_{m,alpha}:=E_Z ||p_{Y|Z}||_infinity^alpha`

`=[ int_{D_m} ell_m(z)^(1-alpha) dz ]^3`.

Using (2.6) with `q=1-alpha`,

`boxed(
M_{m,alpha}
 = [(1-alpha) m^(1-alpha/2) B(1-alpha,m)]^3.
)`                                                               (3.3)

The beta/gamma asymptotic `B(q,m)~Gamma(q)m^(-q)` gives

`boxed(
M_{m,alpha}
 ~ Gamma(2-alpha)^3 m^(3alpha/2).
)`                                                               (3.4)

Thus **every positive conditional-cap moment diverges** in this extreme-product cube family.

For the owner-message exponent `alpha=2/3`, (3.3) becomes

`boxed(
M_m
 = (m^2/27) B(1/3,m)^3
 ~ Gamma(4/3)^3 m.
)`                                                               (3.5)

Numerically

`Gamma(4/3)^3 = 0.712072942688730...`.

For example,

`M_2=27/16=1.6875`,
`M_4=3.09878134110787...`,
`M_10=7.36335792831679...`,
`M_100=71.445179373981...`.

Therefore there is no universal finite constant `C_cond` such that

`E_Z ||p_{Y|Z}||_infinity^(2/3) <= C_cond`               (3.6)

for all cap-one product laws and all three-dimensional orthogonal active projections.

## 4. This is an exact target matrix, and the failure persists at full rank

First take

`A_0 = U diag(1,1,-1) U^T`.                              (4.1)

Its nonzero spectrum is exactly `{1,1,-1}`; all other eigenvalues are zero. Thus it satisfies the exact QFORM hypothesis. Moreover

`Q_0=Y_1^2+Y_2^2-Y_3^2`.

The three active vectors have pairwise disjoint physical supports, so the completed account03/B17 theorem applies directly and gives

`boxed(||p_{Q_0}||_infinity <=2*pi)`                     (4.2)

for every `m`, despite `M_m~0.71207 m`.

This proves that the conditional `2/3`-moment route can lose an arbitrarily large factor even on a family whose actual quadratic output is uniformly bounded.

The failure is not an artifact of zero complementary eigenvalues. For any fixed `0<epsilon<1`, put

`A_epsilon
 = U diag(1,1,-1)U^T + epsilon P_{U^perp}`.          (4.3)

Then `A_epsilon` is full rank, has exactly three eigenvalues of modulus at least one and all other eigenvalues equal `epsilon`. In the same spectral coordinates,

`Q_epsilon
 =Y_1^2+Y_2^2-Y_3^2+epsilon ||Z||^2`.                (4.4)

Conditioning on `Z` changes only the additive level in the active rank-three quadratic; the conditional law of `Y|Z` and therefore the moment (3.5) are unchanged. Hence the proposed universal conditional-moment bridge fails **inside the full-rank target class as well**.

Equation (4.3) is used only to refute the bridge. No claim is made here that (4.2) automatically transfers to `A_epsilon`.

## 5. Why the natural unnormalized repair still does not close this family

Let `g_z(y)=p_{Y,Z}(y,z)` be the unnormalized active slice and `m(z)=int g_z=p_Z(z)`. Normalizing gives `rho_z=g_z/m(z)`. A rank-three coarea inequality of the homogeneous form

`||p_{q(Y)|Z=z}||_infinity <=K ||rho_z||_infinity^(2/3)`

contributes after multiplication by the slice mass

`K ||g_z||_infinity^(2/3) m(z)^(1/3)`.                 (5.1)

For the cube family `||g_z||_infinity=1` on every nonempty slice, and integrating (5.1) is exactly

`K int m(z)^(1/3) dz = K M_m`,                           (5.2)

which still grows linearly with `m`.

So merely saying “do not normalize thin fibers” is insufficient if one then applies the same rank-three `L^infinity^(2/3)` coarea estimate slice by slice. The missing operation has to use product provenance **before** that loss.

For the exact-rank-three family, the correct operation is visible: aggregate each original-coordinate bank into the one-dimensional variables `Y_j` first. Their densities are uniformly bounded by the sharp product-projection theorem, and the two same-sign square terms then give the completed `2*pi` bound. This bank aggregation avoids paying all complementary chord localizations separately.

## 6. Consequence for the full proof strategy

### Refuted intermediate claim

`QFORM-CONDITIONAL-3D-CAP-2OVER3-MOMENT-FALSE-v1`:

There is no universal finite bound for

`E_Z ||p_{Y|Z}||_infinity^(2/3)`

over cap-one product laws and three-dimensional orthogonal active projections, even when the product law is a cube indicator and the associated quadratic matrix is an honest target matrix with spectrum containing `{1,1,-1}`. The same failure persists for full-rank target matrices after adding any fixed `epsilon P_{U^perp}`, `0<epsilon<1`.

### Replacement obligation

A successful full-QFORM proof cannot condition on the entire complementary spectral coordinate and then pay a rank-three conditional `L^infinity^(2/3)` cost separately on each fiber. It must instead retain enough original-coordinate product structure to aggregate independent banks/groups, use a fractional-trace estimate before overconditioning, or derive a genuinely joint curved/product inequality whose cost does not count the `m^(3/2)` family of thin complement fibers.

This is directly aligned with the proof-first owner request for an exhaustive product-preserving ridge-or-grouped-coordinate reduction.

## 7. Status

- Full QFORM: **OPEN / NOT PROVED**.
- Universal conditional `2/3` projection-cap moment: **REFUTED**.
- Exact extreme-product reduction: consumed from designated partner account04/B13 and applied.
- Continuous density for full QFORM: **OPEN / NOT PROVED**.
- No Gaussian, log-concavity, moment, compact-support, bounded-diameter, connected-support, finite-fragment, or post-rotation independence assumption is used.
- No Monte Carlo argument is used; all displayed identities are analytic.

The next B13 step should attack a **group-before-condition** inequality: partition physical coordinates according to their three-row spectral loading, aggregate a bank before reciprocal curvature payment whenever its Gram contribution is coherent, and combine this with the completed rank-two affine half-Riesz theorem on the complementary heavy-coordinate branch. The new counterfamily is a mandatory control: any proposed reduction that conditions down to all within-bank complements before aggregation will necessarily incur the divergent moment (3.5).
