SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B06, 2026-09-22T19:46:49Z.
attacking: the arbitrary-self-block near-coloop splice; extract a fractional L3 payment from an exact rank-two physical cross bank and spend it through a genuine original-coordinate square, without selecting a spectral fiber maximum.

# account03/B06 QFORM r17 — exact-rank-two cross-bank L3 payment plus dependent square smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T194649Z-account03-B06-qform-r17`  
**Assignment:** Curved fiber integration  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Fresh control at prepublication refresh:** `yspennstate/math-research-brain@fcca43e7d6be77bdfb3afc35d24d8719b4fc3fcd`, OWNER CONTROL revision `2026-09-22.15`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  
**Continuity:** not proved by the new theorem; the conclusion below is absolute continuity with an essential `L^infinity` bound.

## 1. Scope and live corrections

The exact target remains: for every finite `n`, every vector of independent real coordinates with probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal finite essential bound on the density of `X^TAX`, or give a target-valid counterexample.

This run does not use: post-rotation independence; the refuted law-uniform pointwise quadratic-phase decay; the false arbitrary-joint rank-three coarea bound; the false positive moment of a worst conditional projection density; unrestricted spectral-fiber suprema; a generic X-ray cap for an indefinite pushforward; or a claimed universally good single physical minor.

The mechanism is different from the preceding B06 ridge-collar run. It uses a **fractional exact cross-bank Fourier estimate at rank two**, which is not `L^1` in frequency but is exactly in `L^(3/2)`, then spends that `L^3` output density through a genuine original-coordinate square. The within-bank quadratic terms are never removed: they are kept inside complex fiber amplitudes.

### Source-valid inputs used

1. `QFORM-EXACT-CROSS-RANK-L2-v1`, account03/B19, canonical source `yspennstate/math-open-problems@9d55d9ca5a7beaed6f693a57bd32b5fc9949b981`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T172719Z-account03-B19-QFORM-r16/REPORT.md`. Its proof gives the mixed-Hessian Plancherel identity with arbitrary within-bank quadratic-affine phases. The published theorem used `rank>=3` only at the final `L^1` frequency integration. The rank-two fractional endpoint is proved explicitly below rather than inferred silently.

2. `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, account04/B18, source pinned in the current B06 chain at `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`. Before its final bathtub estimate, its proof gives the dependence-safe square-kernel domination

   `p_(R+aV_R^2)(t) <= |a|^(-1/2) int_0^infinity p_R(t-sgn(a)u) u^(-1/2) du`,

   whenever the conditional density of `V_R` is at most one. This exact inequality is applied below with an `L^3`, rather than an `L^infinity`, base density.

The designated partner `account04/B06` still has no completed current-QFORM canonical handoff or report at the fresh source check. No exact-partner theorem or PASS is fabricated; work proceeds asynchronously with the compatible completed account04/B18 result above.

## 2. Rank-two exact cross bank has a uniform L3 output density

Let `I,J` be disjoint sets of ORIGINAL coordinates. Condition on every coordinate outside `I union J`. For almost every conditioning value `w`, write

`Q_w(U,V)=F_w(U)+2 U^T C V+G_w(V)+c_w`,                       (2.1)

where `U=X_I`, `V=X_J`, `C=A[I,J]`, and `F_w,G_w` are arbitrary real quadratic-affine functions. The laws of `U` and `V` remain independent product laws with one-dimensional density caps one.

Assume

`rank(C)=2`,                                                   (2.2)

and let its two nonzero singular values be `sigma_1,sigma_2`. Put

`Pi_2(C)=sigma_1 sigma_2>0`.                                  (2.3)

### Theorem 2.1 — `QFORM-EXACT-RANK2-CROSSBANK-L3-v1`

Under (2.1)-(2.3), the conditional law of `Q_w`, uniformly in `w`, and hence the unconditional law, has a density in `L^3`. In the general-bank case,

`boxed( ||p_Q||_3 <= (3e)^(2/3) Pi_2(C)^(-1/3). )`            (2.4)

If one active bank consists of exactly two original physical coordinates, the bound improves to

`boxed( ||p_Q||_3 <= 3^(2/3) e^(1/3) Pi_2(C)^(-1/3). )`       (2.5)

If both active banks consist of exactly two physical coordinates,

`boxed( ||p_Q||_3 <= 3^(2/3) Pi_2(C)^(-1/3). )`               (2.6)

#### Proof

Take a thin SVD

`C=P Sigma R^T`, `Sigma=diag(sigma_1,sigma_2)`.                (2.7)

Set `Y=P^T U`, `Z=R^T V`. Disintegrate the two independent product laws over these two-dimensional projections and define

`alpha_t(y)=p_Y(y) E[exp(i t F_w(U)) | Y=y]`,
`beta_t(z)=p_Z(z) E[exp(i t G_w(V)) | Z=z]`.                  (2.8)

Then `|alpha_t|<=p_Y`, `|beta_t|<=p_Z`. The completed weighted affine-fiber projection bound used in the B19 source gives, in dimension two,

`||p_Y||_infinity<=e`, `||p_Z||_infinity<=e`.                 (2.9)

Since both densities have mass one,

`||alpha_t||_2 ||beta_t||_2 <= e`.                            (2.10)

The exact conditional characteristic function is

`phi_w(t)=e^(it c_w) int int alpha_t(y) beta_t(z)
                         e^(2it y^T Sigma z) dy dz`.           (2.11)

For `t!=0`, Plancherel in the full two-dimensional active cross bank gives

`|phi_w(t)|
 <= pi |t|^(-1) Pi_2(C)^(-1/2)
       ||alpha_t||_2 ||beta_t||_2
 <= pi e Pi_2(C)^(-1/2) |t|^(-1).`                            (2.12)

Also `|phi_w(t)|<=1`. Averaging over the outside conditioning retains the same majorant, so with

`A_2=pi e Pi_2(C)^(-1/2)`                                     (2.13)

we have

`|phi_Q(t)|<=min(1,A_2/|t|).`                                 (2.14)

The key point is that rank two fails `L^1` only logarithmically, but it has the exact fractional integrability needed here:

`int_R |phi_Q(t)|^(3/2) dt
 <=2[ A_2 + A_2^(3/2) int_(A_2)^infinity t^(-3/2) dt ]
 =6 A_2.`                                                      (2.15)

Inverse Hausdorff--Young therefore produces an `L^3` density and, with the same Fourier convention as the B19 source,

`||p_Q||_3
 <=(2pi)^(-2/3)(6 A_2)^(2/3)
 =(3e)^(2/3) Pi_2(C)^(-1/3).`                                 (2.16)

This proves (2.4).

If, say, `|I|=2`, then `P` is a square orthogonal change on exactly two original coordinates. Their joint product density already has cap one and orthogonal change preserves it. Thus `||p_Y||_infinity<=1`, while `||p_Z||_infinity<=e`, so (2.10) improves from `e` to `sqrt(e)`. This replaces `A_2` by `pi sqrt(e) Pi_2^(-1/2)` and yields (2.5). If both banks have size two, the amplitude product is at most one and (2.6) follows. QED.

### Why arbitrary self blocks are genuinely retained

The terms `F_w(U)` and `G_w(V)` in (2.1) can contain arbitrary self quadratic forms and arbitrary affine terms. They appear only inside the conditional complex amplitudes in (2.8), whose modulus is bounded by the corresponding projection densities. Thus the theorem is not a zero-self theorem and does not require completing, diagonalizing, or discarding the two-row self block.

## 3. A dependence-safe L3-to-Linfinity square transducer

The account04/B18 square proof gives, for an original-coordinate scalar square completion

`T=R+a V_R^2`, `a!=0`,                                       (3.1)

with conditional density cap one for `V_R`,

`p_T(t)<=|a|^(-1/2) int_0^infinity p_R(t-sgn(a)u)u^(-1/2)du`. (3.2)

Assume `p_R` has mass one and `||p_R||_3<=M`. Split the integral at `U>0`. Holder with conjugate exponent `3/2` on `[0,U]` gives

`int_0^U p_R(t-u)u^(-1/2)du
 <= M (int_0^U u^(-3/4)du)^(2/3)
 = 4^(2/3) M U^(1/6).`                                       (3.3)

On `[U,infinity)`, mass one gives

`int_U^infinity p_R(t-u)u^(-1/2)du <= U^(-1/2).`              (3.4)

Choose `U=M^(-3/2)`. Then both terms scale as `M^(3/4)`, so

`boxed(
 sup_t int_0^infinity p_R(t-u)u^(-1/2)du
 <= (2^(4/3)+1) M^(3/4).
)`                                                             (3.5)

The same estimate holds with `t+u` for `a<0`.

Combining (3.5) with Theorem 2.1 yields the following.

### Theorem 3.1 — `QFORM-OUTER-SQUARE-RANK2-CROSSBANK-v1`

Suppose completing one ORIGINAL coordinate of coefficient `a!=0` gives

`Q=R+aV_R^2`,                                                  (3.6)

with the dependence-safe conditional cap-one property above. Suppose, after conditioning any additional outside ORIGINAL coordinates, the residual `R` contains an exact rank-two active physical cross bank `C` as in (2.1). Then

`boxed(
 ||p_Q||_infinity
 <= (2^(4/3)+1) sqrt(3e)
    |a|^(-1/2) Pi_2(C)^(-1/4).
)`                                                             (3.7)

Numerically the general-bank prefactor is `<10.052`.

If one active bank is exactly two physical coordinates,

`boxed(
 ||p_Q||_infinity
 <= (2^(4/3)+1) sqrt(3) e^(1/4)
    |a|^(-1/2) Pi_2(C)^(-1/4)
 <7.829 |a|^(-1/2) Pi_2(C)^(-1/4).
)`                                                             (3.8)

If both banks have exactly two physical coordinates, the prefactor is

`(2^(4/3)+1)sqrt(3)<6.097`.                                   (3.9)

No independence between `R` and the translated square variable is asserted or needed.

## 4. Application to the B06 transverse curvature bank

The preceding B06/B08 transverse branch supplies, after a genuine original scalar pivot, a residual physical cross block `H` with singular values `h_j`, a scale `gamma>0`, and

`x_j=min(1,h_j^2/gamma^2)`,
`e_2(x)>=2/3`.                                                  (4.1)

The previous r15 theorem paid every fixed fine-scale branch whose ridge leverage was below an arbitrary `1-epsilon` collar. The high-leverage alternative was left as a near-coloop problem.

There is now a complete additional branch that does not use a ridge-leverage test at all.

### Theorem 4.1 — `QFORM-TRANSVERSE-EXACT-RANK2-SELFBLOCK-CLOSURE-v1`

In the transverse setup (4.1), suppose

`rank(H)=2`.                                                     (4.2)

Then the full ambient quadratic form has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity
 <= C_2 / sqrt(|a| gamma),

 C_2=(2^(4/3)+1)sqrt(3e)(3/2)^(1/8)
     <10.575.
)`                                                             (4.3)

All same-side self quadratic terms, affine shifts, outside couplings, signs, and additional terms already present in the scalar-Schur residual are retained.

#### Proof

Because `H` has rank exactly two, only `h_1,h_2` are nonzero, and (4.1) becomes

`x_1 x_2>=2/3`.                                                 (4.4)

Since `x_j<=h_j^2/gamma^2`,

`Pi_2(H)=h_1 h_2
 >= gamma^2 sqrt(2/3).`                                        (4.5)

Apply Theorem 3.1 with the whole exact-rank-two cross bank `C=H`. Then

`Pi_2(H)^(-1/4)
 <=gamma^(-1/2)(3/2)^(1/8)`.                                  (4.6)

Substitution into (3.7) gives (4.3). QED.

This is materially stronger than the preceding ridge-collar estimate on the exact-rank-two residual: it closes that branch with a small explicit constant and with **no row-leverage hypothesis**.

## 5. Direct splice to the live near-coloop pair currency

The newest account03/B08 theorem gives, in the surviving `99%` near-coloop branch at `g=gamma/16`, a physical row `j` satisfying the aggregate, shear-invariant currency

`sum_(k!=j) det Gram(h_j,h_k)
 > (4191/281804800) gamma^4.`                                  (5.1)

For any fixed `k` with

`d_jk:=det Gram(h_j,h_k)>0`,                                   (5.2)

condition on all other rows on the same physical side and keep the opposite bank active. The active cross matrix is the genuine two-row physical bank

`C_jk=[h_j;h_k]`,                                              (5.3)

so

`Pi_2(C_jk)=sqrt(d_jk)`.                                       (5.4)

The one-bank-exact version (3.8) therefore proves, **with the entire arbitrary two-row self block retained**, the explicit pair payment

`boxed(
 ||p_Q||_infinity
 < 7.829 |a|^(-1/2) d_jk^(-1/8).
)`                                                             (5.5)

This removes the zero-self restriction from the analytic payment attached to any individual pair in the live near-coloop currency. The previous zero-self grouped theorem was sufficient only after assuming the two-row self block vanished; (5.5) has no such assumption.

The remaining obstruction is now precisely the **aggregate-before-reciprocal pair selection**: (5.1) can be spread over arbitrarily many `k`, so it does not imply a dimension-free lower bound on one `d_jk`. This report does not hide that loss by taking a fiber supremum or selecting the largest pair and dividing by the number of rows.

## 6. Status and next implication

Proved here:

- `QFORM-EXACT-RANK2-CROSSBANK-L3-v1`: exact rank-two physical cross banks have a uniform `L^3` output density, with arbitrary within-bank quadratic-affine terms.
- `QFORM-OUTER-SQUARE-RANK2-CROSSBANK-v1`: a genuine original-coordinate square upgrades that `L^3` payment to `L^infinity` dependence-safely.
- `QFORM-TRANSVERSE-EXACT-RANK2-SELFBLOCK-CLOSURE-v1`: the B06 transverse branch with exact residual cross rank two is fully paid by (4.3), without a leverage condition.
- Every individual nondegenerate pair in the current near-coloop currency is paid by (5.5) even with an arbitrary physical two-row self block.

Not proved:

- no dimension-free passage from the aggregate sum (5.1) to one physical pair is claimed;
- no top-two-singular-direction truncation of a higher-rank cross bank is claimed, because residual mixed directions remain coupled inside the fibers;
- the zero/near-zero outer scalar-pivot and scale-payment problems remain separate structural debts;
- continuity of the new square-smoothed branch is not established;
- the full QFORM conjecture remains open.

The next exact B06 obligation is

`QFORM-NEAR-COLOOP-AGGREGATE-RANK2-FRACTIONAL-BL-v1`:

> combine the many valid two-row `L^3` cross-bank estimates before paying `d_jk^(-1/8)`, using the product structure and the shear-invariant sum in (5.1), or prove a structural reduction that concentrates a universal fraction of that currency in a bounded-cardinality physical packet. The operation must occur before reciprocal pair selection and must retain the arbitrary self block.

This is the live arbitrary-self-block/scale splice identified by the current proof assembly, now with the single-pair analytic side fully removed as an obstacle.
