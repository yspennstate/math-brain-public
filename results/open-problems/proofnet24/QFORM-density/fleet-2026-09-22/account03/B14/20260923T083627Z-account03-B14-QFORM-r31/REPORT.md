SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T08:36:27Z.
attacking: rank-two semidefinite Schur-bank localization with exact range-translation removal, aggregate product-projection smoothing, and zero-loss transfer to unbounded fragmented laws.

# QFORM B14 r31 — rank-two semidefinite Schur-bank localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T083627Z-account03-B14-QFORM-r31`  
**Status:** `NEW SUPPORTING THEOREM PROVED / FULL QFORM OPEN`  
**Continuity:** not claimed for the full rough-law conclusion.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and scope

The full target remains open: for arbitrary dimension, independent real coordinates with marginal densities bounded by one, and real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal density bound for `X^T A X`, or give a valid counterexample.

This run proves a target-valid structural branch that was not covered by the preceding rank-one Schur-bank result. It keeps arbitrary translations, arbitrary unbounded and arbitrarily fragmented input supports, and arbitrary outside coordinates. The only structural hypothesis is on one physical indefinite pair and the **rank-two semidefinite Schur curvature of a disjoint original-coordinate bank**. A kernel-affine component is explicitly retained as unpaid rather than silently translated away.

The two completed external inputs actually used are:

1. `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1`, account02/B05: every two-dimensional Parseval projection of independent cap-one coordinates has density cap at most `e`. Source read at `yspennstate/math-open-problems@32e921cf63500a7118cf30724f9e67d7997185e0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T155206Z-b05-qform-779c4c9b/REPORT.md`.
2. The completed account04/B14 physical-pair logarithmic envelope and exact finite-mixture/affine localization compiler, read at the same repository snapshot from r7 and r5. In particular the envelope is

`p_Q(t) <= 2sqrt(2)/r + D^(-1/2) E log_+(2r^2/(kappa |t-R|))`,          (1.1)

for an invertible indefinite physical pair `B`, with `D=|det B|`, `kappa=sigma_min(B)`, and arbitrary dependence of the completed-pair translation on the residual original coordinates. The affine localization compiler transfers a uniform interval estimate from compact finite-fragment active product laws to arbitrary cap-one product laws with no loss.

No rotated input coordinates are declared independent. No moment, compact-support, connected-support, finite-fragment-count, or identical-law assumption is used.

## 2. Physical pair and exact Schur remainder

Split the original independent coordinates as

`X=(U,V,Z)`,

where `U in R^2` is an actual physical coordinate pair, `V in R^m` is a disjoint original-coordinate bank, and `Z` denotes every remaining original coordinate. Allow an arbitrary affine perturbation and scalar shift,

`F(X)=X^T A X + eta^T X + c`.

Write the `U` principal block as `B=A_UU`, and assume `B` is invertible and indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)`.

Completing the physical pair gives

`F=(U+B^(-1)(A_UY Y+eta_U/2))^T B (U+B^(-1)(A_UY Y+eta_U/2)) + R(Y)`,    (2.1)

where `Y=(V,Z)` and

`R(Y)=Y^T S Y + g^T Y + c'`,

`S=A_YY-A_YU B^(-1) A_UY`,

`g=eta_Y-A_YU B^(-1) eta_U`.                                            (2.2)

The shift of the physical pair in (2.1) may depend on the same `V,Z` which produce `R`; no independence between that shift and `R` is assumed or used.

Condition on `Z=z`. The residual becomes

`R_z(V)=V^T S_VV V + q(z)^T V+d(z)`,                                   (2.3)

with

`q(z)=2S_VZ z+g_V`.                                                      (2.4)

## 3. The new theorem

### Theorem — `QFORM-RANK2-SEMIDEFINITE-SCHUR-BANK-v1`

Assume:

1. `B` is an invertible indefinite physical `2x2` block;
2. `S0:=S_VV` is semidefinite of rank exactly two;
3. for every outside value `z`, the affine bank vector satisfies

`q(z) in Range(S0)`.                                                     (3.1)

Equivalently, a deterministic sufficient condition is

`Range(S_VZ) subset Range(S0)` and `g_V in Range(S0)`.                  (3.2)

Let

`P = pdet_abs(S0)`,

the product of the two nonzero eigenvalue magnitudes of `S0`, and put

`K = pi e / sqrt(P)`,

`tau = K D / kappa = pi e D/(kappa sqrt(P))`.                           (3.3)

Then the law of `F(X)` has an essentially bounded density and

`boxed(
||p_F||_infinity <= G(D,kappa,P)
)`                                                                           (3.4)

where

`G(D,kappa,P)=
  6 [pi e/(kappa sqrt(D) sqrt(P))]^(1/3),                 if tau<=1/8,
  D^(-1/2)[3+log(8 pi e D/(kappa sqrt(P)))],             if tau>=1/8.`   (3.5)

The two formulas agree at `tau=1/8`.

The bound is uniform in:

- `m` and the outside dimension;
- all raw pair-to-bank and pair-to-outside couplings already absorbed into the Schur complement;
- the outside quadratic block `S_ZZ`;
- every physical-pair affine term;
- every range-compatible bank translation `q(z)`;
- support locations, support diameters, fragment count and fragment separation;
- all moments.

Only the kernel component `P_Ker(S0) q(z)` is excluded by (3.1). It is not silently discarded.

## 4. Range-compatible translations cost exactly zero

Write the orthogonal decomposition

`q(z)=q_R(z)+q_K(z)`,

with `q_R(z) in Range(S0)` and `q_K(z) in Ker(S0)`.

Under the theorem hypothesis `q_K(z)=0`. Define

`h(z)=1/2 S0^+ q(z)`.                                                    (4.1)

Then `2S0 h(z)=q(z)`, hence exactly

`V^T S0 V+q(z)^T V
=(V+h(z))^T S0(V+h(z))-h(z)^T S0 h(z)`.                             (4.2)

For each fixed `z`, `h(z)` is deterministic. Therefore translating the **original physical coordinates** `V_j` by `h_j(z)` preserves their conditional independence, preserves every marginal density cap `<=1`, and preserves arbitrary finite-fragment structure when present. No rotation of the input product law occurs.

Formula (4.2) is the precise localization statement for translations: the complete range component is free, while a kernel component would survive as `q_K(z)^T V` and is a genuine separate analytic obligation.

## 5. Aggregate rank-two bank density

Because `S0` is semidefinite rank two, there are `eps in {+1,-1}` and a full-row-rank `2xm` matrix `L` such that

`S0=eps L^T L`.                                                         (5.1)

The two nonzero eigenvalues of `L^T L` are the eigenvalue magnitudes of `S0`, so

`det(LL^T)=P`.                                                          (5.2)

Let

`W=L(V+h(z))`.

Set `G=LL^T` and whiten the two-dimensional output:

`Y=G^(-1/2) W=(G^(-1/2)L)(V+h(z))`.                                     (5.3)

The coefficient matrix in (5.3) is Parseval:

`(G^(-1/2)L)(G^(-1/2)L)^T=I_2`.

Account02/B05 therefore gives

`||p_Y||_infinity<=e`.                                                   (5.4)

Undoing the two-dimensional linear change of output variables gives

`||p_W||_infinity<= e/sqrt(det G)=e/sqrt(P)`.                           (5.5)

Now the translated remainder is

`R_z=eps |W|^2 + d_*(z)`.                                               (5.6)

For `T=|W|^2`, polar coarea gives for almost every `s>0`

`p_T(s)=1/2 int_0^(2pi) p_W(sqrt(s)(cos theta,sin theta)) dtheta`

and hence

`||p_T||_infinity <= pi ||p_W||_infinity <= pi e/sqrt(P)=K`.            (5.7)

Reflection and scalar translation do not change density height, so uniformly in `z`,

`||p_(R_z)||_infinity<=K`.                                              (5.8)

Averaging over `Z` gives the same cap for the unconditional remainder law:

`||p_R||_infinity<=K`.                                                   (5.9)

This is the aggregate-before-inversion step: no individual coordinate coefficient in the bank is selected or inverted.

## 6. Apply the account04/B14 pair-log theorem at the actual inequality

Apply (1.1) to (2.1). Since (5.9) gives a genuine density cap for the exact same remainder `R`, for every `A0>0`, layer cake gives

`E log_+(A0/|t-R|)
 =int_0^infinity P{|t-R|<A0 exp(-s)} ds
 <=int_0^infinity min{1,2K A0 exp(-s)} ds
 =Psi(2K A0)`,                                                         (6.1)

where

`Psi(z)=z` for `0<=z<=1`, and `Psi(z)=1+log z` for `z>=1`.

With `A0=2r^2/kappa`, equations (1.1) and (6.1) give

`||p_F||_infinity
 <= inf_(r>0) [2sqrt(2)/r + D^(-1/2) Psi(4Kr^2/kappa)]`.                (6.2)

This is the designated partner result applied to an actual inequality.

### Low branch

When `4Kr^2/kappa<=1`, minimize

`2sqrt(2)/r + 4K r^2/(kappa sqrt(D))`.

The stationary point is

`r_* = sqrt(2) D^(1/6) kappa^(1/3)/(2K^(1/3))`,                         (6.3)

and its value is

`6 K^(1/3)/(D^(1/6)kappa^(1/3))
 =6 [K/(kappa sqrt(D))]^(1/3)`.                                        (6.4)

At (6.3),

`4Kr_*^2/kappa =2(DK/kappa)^(1/3)`,                                    (6.5)

so this stationary point belongs to the low branch iff

`DK/kappa<=1/8`.                                                        (6.6)

### Logarithmic branch

When `4Kr^2/kappa>=1`, minimize

`2sqrt(2)/r + D^(-1/2)[1+log(4Kr^2/kappa)]`.

The stationary point is

`r_*=sqrt(2D)`,                                                         (6.7)

at which

`4Kr_*^2/kappa=8DK/kappa`.                                             (6.8)

Thus (6.7) belongs to the logarithmic branch iff `DK/kappa>=1/8`, and the value is

`D^(-1/2)[3+log(8DK/kappa)]`.                                          (6.9)

Substituting `K=pi e/sqrt(P)` proves (3.5). At the boundary `DK/kappa=1/8`, both formulas equal `3/sqrt(D)`.

## 7. Rough-law and unbounded-support localization

The argument above is already law-uniform, but the assignment requires an explicit localization compiler. Apply account04/B14 r5 to the active original-coordinate block `(U,V)` while leaving `Z` completely arbitrary.

For compact finite-fragment indicator product laws, equations (4.2)--(6.9) give the interval estimate

`P{F in J | Z=z} <= G(D,kappa,P) |J|`                                   (7.1)

uniformly in `z`, in every induced range-compatible translation, and in all fragment locations and diameters. The partner finite-mixture compiler expands any cap-one active product law into total-variation limits of finite convex mixtures of such compact finite-fragment product laws and transfers (7.1) with the **identical constant**. Integrating in the untouched outside law then gives

`P{F in J} <= G(D,kappa,P)|J|`                                          (7.2)

for every interval `J` and arbitrary cap-one product laws, including unbounded supports and infinitely many arbitrarily distant fragments.

Thus this branch has zero localization tax. No moment, tail truncation, support radius, diameter, fragment-count or fragment-separation parameter occurs in the constant.

## 8. Diffuse stress family

Let `m>=1` and let `a_m,b_m in R^(2m)` be the normalized block-constant vectors

`a_m=m^(-1/2)(1,...,1,0,...,0)`,

`b_m=m^(-1/2)(0,...,0,1,...,1)`.

Take the physical pair

`B=[[0,1],[1,0]]`

and the Schur bank

`S0=a_m a_m^T+b_m b_m^T`.                                              (8.1)

Then

`D=1`, `kappa=1`, `P=1`.

Every nonzero entry of each dense bank block in (8.1) is `1/m`, so any one-coordinate curvature coefficient tends to zero, but the aggregate pseudo-determinant remains exactly one. The block-diagonal matrix `B direct_sum S0` has nonzero spectrum

`{1,-1,1,1}`,

so it is a valid target matrix in every dimension.

The theorem gives

`||p_Q||_infinity <=3+log(8 pi e)
 =7.224171427529236...`                                                 (8.2)

uniformly in `m` and for arbitrary cap-one marginals. This is exactly the desired aggregate behavior: no reciprocal `1/m` coefficient is paid.

## 9. What this does and does not close

This theorem extends the preceding B14 rank-one Schur-bank localization to a genuinely rank-two diffuse same-sign bank and preserves all range-compatible conditional translations.

It does **not** prove the full conjecture. The bare hypothesis `s_3(A)>=1` does not yet force a physical indefinite pair with controlled `(D,kappa)` together with a rank-two semidefinite Schur bank of controlled pseudo-determinant `P`. The remaining branches include:

1. an indefinite rank-two Schur bank, where the two-dimensional quadratic pushforward itself has a logarithmic singularity;
2. rank-two semidefinite curvature with a nonzero kernel-affine component `P_Ker(S0)q(z)`;
3. higher-rank or mixed-sign bank curvature not reducible to a two-dimensional same-sign aggregate;
4. the global no-pivot/N3 structural step proving that one of the currently paid exits must occur.

The present proof deliberately does not treat a small matrix perturbation as a small random quadratic error on unbounded supports.

Continuity is separate. Equation (7.2) proves essential boundedness; no common modulus of continuity is asserted for arbitrary rough laws.

## 10. Source / correction ledger

Fresh brain control at run start resolved `main` to `65fb446cab1d892af943943efad3599d8701ccdc`; the pre-publication refresh resolved `main` to `ecf8759877084342d928e5d605164fa5196c0aa5`. OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only, with no B14 pause.

Corrections consumed include: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no dimension-free naive fiber supremum; no bounded-diameter/fixed-fragment-count localization; no arbitrary-joint rank-three coarea; no replacement of product provenance by a conditional density cap; and no universal good single physical minor/cross-rank-three cut.

No new correction event is needed: no previously proposed premise is refuted here.

**Full QFORM:** OPEN.  
**Continuous density for full target:** OPEN.  
**Independent review of this new theorem:** not yet performed.  
**Native brain ingestion:** `WITHOUT_VERIFIED_BRAIN`.
