SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T20:20:07Z.
attacking: Schur-gauge localization—quotient all conditioning-generated affine shifts by the range of a physical block, identify the exact kernel residual, and apply fleet02/B14's completed Fisher translation-mixture theorem to a genuinely delocalized three-eigenvalue family with arbitrary remote components.

# fleet01/B14 auto11 — Schur-gauge zero-tax localization and a delocalized Fisher-mixture application

Programme: `QFORM-DENSITY-3EIG-20260922`
Status: **PROVED SUPPORTING LOCALIZATION THEOREM + STRICT TARGET-VALID PARTNER APPLICATION / FULL QFORM OPEN**
Execution context: `WITHOUT_VERIFIED_BRAIN`.
Continuity: not claimed for the unrestricted target.

## 1. New mechanism and statement

This run changes mechanism from the preceding truncation/extreme-law/Fisher-approximation arguments.  The point is purely algebraic: conditioning on outside original coordinates creates affine terms in an active block, and every affine component lying in the range of the active quadratic matrix is an exact gauge.  It can be removed by coordinate translations before any analytic estimate is paid.

For a real symmetric `k x k` matrix `B`, define its centered cap-one product small-ball constant

`K0(B) = sup [ P{X^T B X in J} / |J| ]`,                         (1.1)

where the supremum is over all intervals `J` of positive length and all vectors `X=(X_1,...,X_k)` with independent probability densities bounded by one.  The value `+infinity` is allowed.  Finiteness of `K0(B)` is exactly the assertion that every such centered quadratic pushforward is dominated by `K0(B)` times Lebesgue measure.

Let

`A = [[B,C],[C^T,D]]`                                           (1.2)

be an arbitrary symmetric extension in the original independent-coordinate split `(X,Y)`.  Write `B^dagger` for the Moore--Penrose inverse and

`P = B B^dagger = projection onto Ran(B)`,
`N = I-P = projection onto ker(B)`.                              (1.3)

### Theorem 1 — QFORM-SCHUR-GAUGE-LOCALIZATION-v1

For every fixed outside value `y`, set

`a(y)=B^dagger P C y = B^dagger C y`.                           (1.4)

Then the exact identity

`X^T B X + 2 X^T C y + y^T D y`
` = (X+a)^T B (X+a)`
`   + 2 (X+a)^T N C y`
`   + y^T (D-C^T B^dagger C) y`                                (1.5)

holds.

Consequently:

1. **Range-compatible zero tax.**  If `Ran(C) subset Ran(B)`, equivalently `NC=0`, then for every independent outside product law (indeed for every outside law independent of `X`),

`P{(X,Y)^T A (X,Y) in J} <= K0(B) |J|`                          (1.6)

for every interval `J`.  Thus

`||p_{(X,Y)^T A (X,Y)}||_infinity <= K0(B)`                     (1.7)

whenever `K0(B)<infinity`.

2. **Invertible active block.**  If `B` is invertible, the range condition is automatic.  Hence arbitrary outside quadratic curvature `D`, arbitrary active--outside coupling `C`, arbitrary support geometry, arbitrary translations, arbitrary remote fragments, and absence of moments cost **exactly zero** relative to the centered active constant.

3. **Exact residual for singular blocks.**  For general singular `B`, the only conditioning-generated affine term that cannot be removed by a coordinate translation is

`2 (X+a)^T N C y`,                                              (1.8)

the projection of the external coupling onto `ker(B)`.  Every range component of `Cy` is pure gauge.

4. **Optimal constant preservation as an extension principle.**  If one takes the supremum over all range-compatible ambient extensions (1.2), arbitrary outside dimensions and laws, the optimal extension constant is exactly `K0(B)`: the upper bound is (1.6), while the reverse inequality follows by taking `C=0,D=0`, so the outside variables do not enter the form.

No support truncation, diameter, moment, fragment count, regularity or centering hypothesis is used.

### Proof

Because `B` is symmetric, `Ran(B)` is orthogonal to `ker(B)`, `B B^dagger=P`, and `B^dagger N=0`.  With `a=B^dagger C y`, one has

`B a = P C y` and `a perpendicular N C y`.                      (1.9)

Expanding the right side of (1.5),

`(X+a)^T B(X+a)=X^T B X+2X^T P C y+a^T B a`,                   (1.10)

while

`2(X+a)^T N C y = 2X^T N C y`                                  (1.11)

because `a^T N C y=0`.  Finally

`a^T B a = y^T C^T B^dagger C y`,                              (1.12)

so the constant terms cancel exactly and (1.5) follows.

If `NC=0`, condition on `Y=y`.  The variables `X_i+a_i(y)` remain independent, and each translated marginal still has density cap one.  The final term in (1.5) is a scalar depending only on `y`; it does not affect interval length.  By the definition (1.1),

`P{Q in J | Y=y} <= K0(B)|J|`                                  (1.13)

for almost every `y`.  Integrating proves (1.6).  This small-ball proof does not presuppose a conditional density and therefore also proves existence of an essentially bounded output density when `K0(B)<infinity`.  The remaining assertions are immediate.  QED.

## 2. Affine constant equals centered constant on the range

For later reuse, define

`K_aff,R(B)=sup_{ell in Ran(B),c} sup_{cap-one product X,J}`
`             P{X^T B X+ell^T X+c in J}/|J|`.                  (2.1)

Then

`boxed{ K_aff,R(B)=K0(B). }`                                   (2.2)

Indeed, write `ell=2Ba` and complete the square

`X^T B X+ell^T X+c=(X+a)^T B(X+a)+c-a^TBa`.                    (2.3)

Coordinate translations preserve both independence and the cap-one condition.  The reverse inequality is obtained with `ell=0`.  In particular, if `B` is invertible,

`boxed{ K_aff(B)=K0(B). }`                                     (2.4)

This is useful because a centered theorem for an invertible physical block automatically becomes fully affine-uniform with *the same constant*.  No separate affine proof is needed.

## 3. Immediate exact-target corollary: the `pi` branch survives arbitrary outside couplings

Take

`B=diag(b_1,b_2,b_3)`, `|b_j|>=1`.                              (3.1)

Among the three coefficients, two have the same sign.  The standard beta-integral argument for two independent shifted squares gives

`K0(B)<=pi`.                                                    (3.2)

Since `B` is invertible, Theorem 1 gives for every ambient extension

`A=[[B,C],[C^T,D]]`                                             (3.3)

and every cap-one independent product vector `(X,Y)`,

`boxed{ ||p_{(X,Y)^T A(X,Y)}||_infinity <= pi. }`               (3.4)

Here `C` and `D` are completely arbitrary.  Thus three large diagonal entries with zero mutual active cross terms already give the sharp diagonal constant even if those three coordinates are coupled arbitrarily strongly to every outside coordinate.  By positive/negative interlacing the ambient matrix has at least three eigenvalues of modulus at least one, so (3.4) is a strict full-target family, not a rank-deficient control.

This is exactly the sort of localization needed in B14: conditioning may induce arbitrarily large random translations, but the translations are range-gauge and cost nothing.

## 4. Material application of the completed partner `fleet02/B14`

The newest completed `fleet02/B14` report is

`math-open-problems@b2d5f5354dfe179e18e366cf49c485e5326e9288`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T193835Z-fleet02-B14-QFORM-auto11/REPORT.md`.

Its proved translation-mixture input is:

- for `g(x)=cos^2(pi x/2) 1_{[-1,1]}(x)`, `I(g)=pi^2`;
- for every probability measure `nu`, however remote, unbounded or moment-free,

`f=g*nu` satisfies `f<=1` and `I(f)<=pi^2`;                     (4.1)

- this survives arbitrary countable translation mixing with no information tax.

The projected-Fisher theorem used there is at

`math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2`
`proofnet24/QFORM-density/interactive/20260923T184054Z-fisher-continuation/FISHER_INFORMATION.md`.

Its analytic core has subsequently received a PASS in the requested B02 review at commit
`51058178f17c27df3f70279291a667a5c9e8cbb7`.

For an `r=3` invariant eigenspace with `s=min |lambda_j|`, leverage weights `ell_i`, and

`J_E=sum_i ell_i I(f_i)`,                                      (4.2)

the cap-improved bound is

`||p_Q||_infinity <= [3 d + sqrt(J_E d)]/(4s)`,                (4.3)

where

`d=min(D_3,J_E)`,
`D_3=6(4pi/3)^(2/3)=15.591108358883012...`.                    (4.4)

### A genuinely delocalized exact-target family

Let

`B_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`,             (4.5)

of dimension `2m+1`.  Its nonzero spectrum is exactly

`{1,1,-1}`.                                                    (4.6)

This is the standard stress family for which every fixed physical three-coordinate certificate degenerates at scale `1/m`; it is therefore not a hidden localized-principal-block example.

Give every active coordinate an arbitrary density

`f_i = g*nu_i`,                                                 (4.7)

where each `nu_i` is an arbitrary probability measure.  The `nu_i` may have arbitrarily distant atoms, unbounded support and no finite moments.

For the three-dimensional nonzero eigenspace of `B_m`, the leverage weights are

`1` on the singleton coordinate and `1/m` on each coordinate in each of the two `m`-banks.  Hence

`sum_i ell_i=3` and
`J_E <= pi^2 sum_i ell_i = 3 pi^2`.                            (4.8)

Since `3pi^2>D_3`, (4.3) gives the explicit partner-derived inequality

`boxed{ ||p_{X^T B_m X+b^T X+c}||_infinity`
`       <= [3D_3+pi sqrt(3D_3)]/4`
`       = 17.06474993087351... }`                              (4.9)

uniformly in `m`, every affine vector `b`, every constant `c`, and every choice of the remote/moment-free mixing laws `nu_i`.

This is a direct application of the completed partner localization result at an actual full-target inequality: the Fisher budget is paid on the **reassembled translated mixture**, not on its components.

### Arbitrary outside laws and couplings remain zero-tax

Now enlarge (4.5) to an ambient original-coordinate form

`A_m = [[B_m,C],[C^T,D]]`,                                     (4.10)

where `C,D` are arbitrary, and let the outside coordinates have **completely arbitrary** independent cap-one laws (they need not have finite Fisher information, moments, connected support, or bounded support).

Conditioning on the outside vector `Y=y` produces the affine term `b=2Cy` in the active variables.  Bound (4.9) is uniform in `b`; therefore

`boxed{ ||p_{(X,Y)^T A_m(X,Y)}||_infinity`
`       <= 17.06474993087351... }`                             (4.11)

for every `m,C,D`, all active mixtures (4.7), and all outside cap-one product laws.

The principal block `B_m` already has two eigenvalues `>=1` and one eigenvalue `<=-1`; Cauchy interlacing therefore puts every ambient extension (4.10) inside the owner's three-large-eigenvalue target.

Thus (4.11) simultaneously controls:
- a diffuse/no-good-local-minor spectral geometry;
- arbitrary conditioning-generated translations;
- arbitrary outside curvature and cross couplings;
- arbitrary remote active mixture centers and unbounded active support;
- arbitrary rough outside marginals;
- no moment bounds anywhere.

The only extra hypothesis is the finite-information translated-kernel structure on the active `2m+1` coordinates.  It is not asserted for arbitrary cap-one active laws.

## 5. Fragment ledger and why this is genuinely zero-loss localization

For the range-compatible theorem (1.6), let an outside law be decomposed into any finite or countable collection of subprobability pieces of masses `m_alpha`.  The conditional estimate is pointwise in every outside value, hence each piece contributes at most

`m_alpha K0(B)|J|`.                                            (5.1)

Summing gives exactly

`sum_alpha m_alpha K0(B)|J| = K0(B)|J|`.                       (5.2)

There is no fragment-count, diameter, separation, location or moment penalty.  In particular the components may escape to infinity.

For the partner application (4.9), fleet02/B14 proves the corresponding active-side zero tax for translations of a fixed Fisher-regular shape:

`I(g*nu)<=I(g)=pi^2`                                           (5.3)

independently of the number and positions of atoms/components in `nu`.

The two mechanisms are complementary:
- **outside localization:** conditional affine shifts are paid by Schur-gauge / affine-uniformity;
- **active translation localization:** positive translation mixtures are paid before reciprocal Fisher scale is introduced.

Neither mechanism normalizes remote active fragments one by one.

## 6. Exact obstruction isolated by the new normal form

Equation (1.5) says precisely what a future structural proof must pay when it chooses a singular physical block `B`:

`unpaid coupling = N C = P_{ker(B)} C`.                         (6.1)

Large range components of `C` are irrelevant after conditioning, regardless of their magnitude.  Small range eigenvalues are also irrelevant to the *translation algebra*; they matter only through whatever centered constant `K0(B)` one can prove.

Therefore a matrix extraction argument should not charge the full norm of a cross-coupling column to an active singular block.  It should first quotient by `Ran(B)` and charge only the kernel residual (6.1).  This is a concrete simplification for the overlap-compound / Schur branches now being pursued by the fleet.

No perturbative statement is made about a small but nonzero kernel residual: with arbitrary rough unbounded input laws, it cannot simply be deleted.

## 7. What remains open

The full owner target is still `OPEN / NOT PROVED / NOT DISPROVED`.

The new theorem is an exact localization compiler, not the missing global structural extraction.  Bare `s_3(A)>=1` does not force a uniformly conditioned finite principal block, and the live corrections contain explicit diffuse families defeating that shortcut.  The partner Fisher argument gives a complete dimension-free answer for the translated compact-kernel class, but Fisher information can diverge like `N^2` on legal unit-height `N`-fragment cap-one marginals; that approximation route therefore does not close the arbitrary-law target.

The first unpaid B14 implication is now:

**either** find a whole-law active certificate valid for arbitrary rough cap-one marginals,

**or** in a singular-block decomposition, show that the kernel residual `P_{ker(B)}C` feeds one of the already completed bank/volume/hub/pair receivers before any fragment normalization.

The range part of every conditioning-generated translation is fully solved by Theorem 1 and should no longer be charged.

## 8. Source discipline

Fresh owner control read in this run: QFORM only, owner-control revision `2026-09-22.15`, no B14 pause/stop observed.  Consumed live corrections include: false law-uniform pointwise quadratic Fourier decay; no independence after spectral rotation; spectral-fiber dimension loss; bounded-diameter localization failure; no universal fixed fragment-count reduction; and the local-cross-rank-three dichotomy failure.  None is used as a premise.

Sources actually used:
1. `math-research-brain` fresh control files and current QFORM state.
2. `math-open-problems@b2d5f5354dfe179e18e366cf49c485e5326e9288`, fleet02/B14 Fisher translation-mixture localization and scale barrier.
3. `math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2`, projected Fisher-information theorem.
4. `math-open-problems@51058178f17c27df3f70279291a667a5c9e8cbb7`, requested B02 review, PASS on the Fisher analytic core.

No pointwise quadratic Fourier decay, post-rotation independence, bounded-support reduction, bounded fragment count, moment assumption or public/remote workflow is used.

No email/push, scheduler mutation, new task, cross-account authentication, paid/remote call, public release or permission expansion was performed.
