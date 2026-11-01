# MOC4 fleet02/B07 — exact Spin(4) scalar margins from pair-roof reserves

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T063443Z-b07-11689214`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## Sources actually consumed


Latest complete campaign lead visible at that prewrite snapshot: fleet03/B07 `20260922T060726Z-fleet03-B07-MOC4-r11`, `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`, report blob `3c11567e275d39376f217a9b9e3c10693efa3127`. Its exact pair-Hessian normalization is

`[ -2(T-C) I_2   M ; M^T   -2(T+C) I_2 ] <= 0`.

Named partner source re-read from its immutable historical handoff commit `86ade870bb739fe4d52b3a54fe90e2c87522a807`, blob `734da3d26e5444f410cd64d0d82e1024ca091e2d`: fleet03/B08 `MOC4-PAIR-BLOCH-ENVELOPE-v1`. On every genuine embedded coordinate `SU(2)` pair orbit the determinant is affine in the Bloch vector, inverse-free and valid at singular determinant points. I also consumed the partner's current complete `MOC4-DENSE-CAYLEY-ADVERSARY-v1`, report blob `f20f1fae1ee8a3b9b2fa56b243612cdaeb6d8c83`, as an exact true-unitary regression datum.

Named OTHER-account dependencies applied directly:

- fleet04/B08 `MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`, immutable handoff commit `db7322e4995935e482d4a8204c0ff07b42d8e5d7`, handoff blob `d03a42d9f1e418302986f301a47a78a8ae3f3b91`: for every row or column transposition `tau`, `(h(U)+h(tau U))/2 <= M`.
- fleet04/B08 current `MOC4-STRICT-ROOT-MIXED-SCHUR-RESIDUAL-v1` handoff blob `5d9e2a6f85bc897abb35aa2d575802276d02925e`: exact root dictionary `01 <-> 23`, `02 <-> 13`, `03 <-> 12` between coordinate `SU(2)` roots and the conformal/anticonformal Spin(4) scalar sectors, plus the mixed-Schur boundary kernel and cubic/quartic gates.
- fleet01/B07 `MOC4-SPECTRAL-CONDITIONED-FLAT-RIGIDITY-v1`, handoff blob `f66ce110764290fb970ff4febb0dc59bdcb36529`: `sum_beta(R_{alpha beta}^2-D_{alpha beta}^2) <= 4(Q_{alpha gamma}+Q_{alpha delta})/sigma_alpha^2`, where `Q=T^2-C^2`.
- own preceding `MOC4-PAIR-CURVATURE-SANDWICH-v1` and `MOC4-CONJUGACY-CASIMIR-BALANCE-v1`, report blob `725731dc96b039169fbf6298a2d3204ee12fcdaa`.

No benchmark artifact or held-out answer was read or used.

## 1. Conditional end-to-end route

Fix a real support functional `h(U)=Re(eta det(A+UBU*))`, normalize `|eta|=1`, and let

`M=max_sigma Re(eta prod_i(a_i+b_sigma(i)))`.

If MOC4 fails, compactness gives a genuine global unitary maximizer `U_*` with

`h(U_*)=M+gamma`, `gamma>0`.

Repeated spectra are already closed exactly by the previous pair-common-lift argument. The latest lead and fleet04/B08 remove scalar Spin(4) saturation from a violator; fleet01/B07 controls block nonconformality by the strict scalar margins `Q=T^2-C^2`. The first unpaid point is therefore quantitative: identify those `Q` margins with target-level quantities already controlled by the 24 permutation roof, rather than treating them as independent Hessian variables.

That identification is the new step below.

## 2. New theorem `MOC4-SPIN4-PAIR-ROOF-RESERVE-IDENTITY-v1`

For either physical side (row/left or column/right), and every coordinate transposition `tau`, put

`h_tau=h(tau U_*)`,
`g_tau=h(U_*)-h_tau`,
`r_tau=M-(h(U_*)+h_tau)/2`.

The pair-symmetrized common lift gives `r_tau>=0`. Pure algebra gives the exact identity

`g_tau = 2(gamma+r_tau)`.                                      (2.1)

In particular `g_tau>=2 gamma` for all six row swaps and all six column swaps.

Now group the six coordinate transpositions into the three complementary pairs

`(01,23)`, `(02,13)`, `(03,12)`.

For a given complementary pair `(tau,tau^c)`, let `T,C` be the corresponding lead Spin(4) scalar-sector quantities. In the fleet04/B08 root normalization, the two diagonal scalar Hessian sectors are

`-2(T-C) I_2`, `-2(T+C) I_2`.                                  (2.2)

By the fleet04/B08 root dictionary, these are exactly the two coordinate pair-root planes for `tau` and `tau^c`. By the fleet03/B08 Bloch theorem, at a global pair maximum the support on each such `SU(2)` sphere has north-minus-south gap `g_tau`, and along either standard great-circle coordinate its Hessian is `-2 g_tau I_2`. (This follows directly from `A_0+c_z cos(2t)` at a north-pole maximum.) Therefore, up to exchanging the conformal and anticonformal labels,

`T-C = g_tau`, `T+C = g_(tau^c)`.                               (2.3)

Consequently

`T = 2 gamma+r_tau+r_(tau^c)`,
`C = +/- (r_(tau^c)-r_tau)`,                                    (2.4)

and the lead scalar Schur reserve is not a free variable at all:

`Q:=T^2-C^2 = g_tau g_(tau^c)
               =4(gamma+r_tau)(gamma+r_(tau^c)).`               (2.5)

In particular every positive-gap maximizer satisfies the quantitative strictness

`T-|C| = 2 gamma+2 min(r_tau,r_(tau^c)) >= 2 gamma`,             (2.6)
`Q >= 4 gamma^2`.                                                (2.7)

This strengthens the previous qualitative `T>|C|`: a violator is separated from every scalar Spin(4) saturation face by an amount proportional to the actual target support gap.

All statements are singular-safe. They use only the pair common lift and the Bloch-sphere determinant polynomial; no determinant inverse or eigenvector division is present.

## 3. Three-partition and spectral budgets

Let

`G=sum_(six transpositions) g_tau`.

The preceding conjugacy-class balance theorem gives the same `G` on the row and column sides. Since `r_tau=g_tau/2-gamma`,

`sum_tau r_tau = G/2-6 gamma`.                                  (3.1)

For either side define

`P=Q_(01|23)+Q_(02|13)+Q_(03|12)
  =g_01 g_23+g_02 g_13+g_03 g_12`.                              (3.2)

Writing `g_tau=2gamma+u_tau`, `u_tau>=0`, gives the exact reserve expansion

`P=2 gamma G-12 gamma^2
   +4(r_01 r_23+r_02 r_13+r_03 r_12)`.                          (3.3)

Hence

`P >= 2 gamma G-12 gamma^2 >= 12 gamma^2`,                      (3.4)

because the six pair roofs imply `G>=12 gamma`. Conversely, orient the three complementary pairs as `(x_i,y_i)`; then

`P=sum_i x_i y_i <= (sum_i x_i)(sum_i y_i) <= G^2/4`.           (3.5)

So all three continuous Spin(4) scalar reserves live inside one discrete transposition-class budget:

`2 gamma G-12 gamma^2 <= sum Q_i <= G^2/4`,                     (3.6)

with the same `G` on both physical sides.

The previous singular-safe adjugate estimate gives, with

`R=max_i|a_i|+max_j|b_j|`,

`g_rs <= 2 R^3 |a_r-a_s|` on the row side, and the analogous bound with `b` on the column side. Combining with (2.5)-(2.7), for every complementary partition `{r,s}|{t,u}`,

`4 gamma^2 <= Q_(rs|tu)
 <= 4 R^6 |(a_r-a_s)(a_t-a_u)|`,                               (3.7)

and likewise for `b`. Therefore

`|(a_r-a_s)(a_t-a_u)| >= gamma^2/R^6`,                          (3.8)

for all three complementary partitions, and analogously for `b`. This is stronger than merely excluding repeated eigenvalues: a positive normalized gap forces all three complementary spectral-gap products away from zero. These are exactly the product factors that enter the fleet01/B07 cross-ratio conditioning determinant. Equation (3.8) controls their magnitudes; it does not control their relative complex arguments, so the real-cross-ratio locus remains a genuine separate issue.

## 4. Direct insertion into spectral-conditioned flat rigidity

Fleet01/B07 proves for a block row `alpha`, with the other rows `gamma,delta`,

`sum_beta(R_{alpha beta}^2-D_{alpha beta}^2)
 <= 4(Q_{alpha gamma}+Q_{alpha delta})/sigma_alpha^2`.           (4.1)

Using the root dictionary and (2.5), each `Q` on the right is an exact product of two complementary pair deficits, hence

`sum_beta(R_{alpha beta}^2-D_{alpha beta}^2)
 <= (4/sigma_alpha^2)
    (g_tau g_(tau^c)+g_mu g_(mu^c))`                            (4.2)

for the two complementary root partitions adjacent to that block row. Equivalently, in target-roof reserves,

`<= (16/sigma_alpha^2)
   ((gamma+r_tau)(gamma+r_(tau^c))
    +(gamma+r_mu)(gamma+r_(mu^c))).`                            (4.3)

There is an identical column formula. Thus the strict-margin payment problem is now expressed entirely through target-level pair-roof reserves plus the explicit spectral conditioning `sigma`; `Q` need not be estimated as an independent Hessian unknown.

## 5. Mixed-Schur boundary consequence

Fleet04/B08 leaves, after scalar strictness, a possible mixed Schur equality. In its notation

`a=T-C`, `b=T+C`,

and a kernel vector has the form

`Z_*=sqrt(b) u + sqrt(a) v`                                     (5.1)

in the conformal and anticonformal root planes. By (2.3), `{a,b}={g_tau,g_(tau^c)}`. Therefore at a positive-gap violator

`a,b >= 2 gamma`,                                                (5.2)

and the kernel weights are exactly square roots of genuine pair deficits, equivalently `sqrt(2(gamma+r_tau))` and `sqrt(2(gamma+r_(tau^c)))` up to exchange. The Schur-boundary kernel can never degenerate toward a pure conformal/anticonformal direction while `gamma` stays positive. The fleet04/B08 cubic gate `J3(Z_*)=0` and quartic gate `J4(Z_*)<=0` can therefore be attacked with these discrete reserve weights rather than unconstrained positive parameters.

## 6. Exact named-partner regression

I re-used the current fleet03/B08 exact dense Cayley datum

`a=(18-17i,-20+2i,15-22i,-21+2i)`,
`b=(-19+4i,25-5i,18-i,-18+i)`,
`L(z)=-5782 Re z+19099 Im z`,

with its exact rational unitary. This datum is target-safe and is **not** a global violating maximizer, so I use it only to regression-test the pair-roof arithmetic and the already-proved left/right transposition-class balance; I do not apply the global-maximizer Spin(4) conclusion (2.3) to it.

The exact Fraction verifier reproduces

`M=-61633500`,
`h=-2411727095/13`,
`gamma=h-M=-1610491595/13`,

checks all twelve pair-roof reserves are nonnegative, checks (2.1) for all twelve row/column swaps, and checks exact class balance

`G_row=G_column=81782105414143/1781`.

The smallest row and column reserves are respectively

`909310641145/7124`, `896927260225/7124`.

For completeness its complementary-product sums are

`P_row=63465783339507613398125580/3171961`,
`P_column=18178531158853875064137945/487994`.

Exact code: `verify_pair_roof_reserve.py`. Captured exact output: `VERIFY_OUTPUT.txt`.

## 7. Sharpened first missing implication

The parent MOC4 problem remains open. Repeated spectra are already closed exactly; singular determinant points are retained by the inverse-free algebra.

The first sharpened interior obligation is now:

**`MOC4-STRICT-RESERVE-SPECTRAL-PAYMENT-v2` (OPEN).** At a positive-gap true-unitary global maximizer, combine the exact identities

`Q_(tau|tau^c)=4(gamma+r_tau)(gamma+r_(tau^c))`,
`G=12 gamma+2 sum_tau r_tau`,

with the structured spectral conditioning matrices, subgroup/V4 roofs, full mixed Hessian inequalities and, on mixed-Schur equality, the explicit cubic/quartic kernel gates, to force `gamma<=0`; or produce a genuine complex-spectrum true-unitary point violating one common target support direction.

A particularly concrete next substep is to substitute the exact reserve-weighted kernel (5.1)-(5.2) into the fleet04/B08 `J3=0`, `J4<=0` conditions and determine whether the target roofs force a positive quartic direction or whether a source-valid stationary adversary survives.

This run does not claim that implication solved and does not claim a target counterexample.
