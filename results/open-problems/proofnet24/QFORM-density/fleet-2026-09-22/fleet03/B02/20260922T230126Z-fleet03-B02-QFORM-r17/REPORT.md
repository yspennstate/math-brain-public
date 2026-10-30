SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-22T23:01:26Z.
attacking: the first unpaid two-sided square/rank-two Fourier step; isolate and close every transverse two-sided coupling by a new exact-rank-three physical cross-block L1 Fourier theorem, leaving only the span-aligned residue.

# fleet03/B02 QFORM r17 — exact-rank-three cross-block Fourier theorem and transverse closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T230126Z-fleet03-B02-QFORM-r17`  
**Assignment:** Integrated Fourier estimate  
**Fresh owner control at start:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  
**Continuity:** proved on the new cross-block branches below because the full characteristic function is in `L^1`; full-target continuity remains open.

## 1. Exact target and what changed from r16

The target is unchanged: for every finite `n`, every vector `X=(X_1,...,X_n)` of independent real coordinates with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `Q=X^T A X`, or give a target-valid counterexample. No moment, Gaussian, log-concavity, compact-support, connected-support, or post-rotation-independence assumption is introduced.

The preceding B02 run (`math-open-problems@864e0222357c77d628a7e3389a32e230f30b9321`) proved that a naive Gabor-line `L^2` restriction bridge for the genuinely two-sided square-plus-rank-two packet is false. It also proved a full `q>2` shifted-square Fourier family. The first unpaid step was therefore to remove the one-sided isolation without reusing the false Gabor-line interface.

This run changes mechanism. Rather than tracing one translation/modulation line after rank-two Plancherel, I first identify when the two-sided coupling itself creates an **exact rank-three original-coordinate cross block**. On that branch, a three-dimensional product-marginal theorem plus direct bilinear Plancherel gives the target `|t|^{-3/2}` tail with no leverage hypothesis. The result closes every transverse two-sided coupling and leaves only the precise span-aligned residue.

I still do **not** have a valid counterexample to a universal target-wide unweighted `L^1` characteristic-function estimate. The stronger criterion remains open at full scope.

## 2. Published input: three-dimensional marginals of product measures

I use one source-matching published theorem, not a post-rotation independence assumption:

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1.

If `Y=(Y_1,...,Y_m)` has product probability density `prod_i f_i` with `||f_i||_infinity<=1`, and `E` is a `k`-dimensional subspace, then the density of the orthogonal marginal onto `E` satisfies

`||rho_E||_infinity <= 2^(k/2)`.

For `k=3`, this gives `||rho_E||_infinity<=2^(3/2)`. If the bank itself has dimension exactly three, the trivial product bound `||rho||_infinity<=1` is even stronger. No independence of the projected coordinates is asserted or used.

## 3. Exact-rank-three physical cross-block theorem

### Theorem 3.1 — `QFORM-EXACT-RANK3-CROSSBLOCK-FOURIER-v1`

Let `I,J,W` be disjoint sets of **original** coordinates whose union is all coordinates. Let `X_I,X_J,X_W` therefore be mutually independent product banks with each scalar density bounded by one. Suppose the physical cross block

`M=A[I,J]`

has exact rank three. Let its three nonzero singular values be `sigma_1,sigma_2,sigma_3` and put

`Gamma=sigma_1 sigma_2 sigma_3>0`.

No restriction is imposed on `A[I,I]`, `A[J,J]`, `A[W,W]`, or on the couplings to `W`. Then

`|phi_Q(t)| <= min(1, (2*pi)^(3/2) Gamma^(-1/2) |t|^(-3/2))`,          (3.1)

hence

`||phi_Q||_1 <= 12*pi*Gamma^(-1/3)`,                                  (3.2)

and `Q` has a bounded **continuous** density satisfying

`boxed( ||p_Q||_infinity <= 6 Gamma^(-1/3) ).`                         (3.3)

More generally, if the two relevant three-dimensional projected bank densities have caps `M_L,M_R`, the same proof gives

`||p_Q||_infinity <= 3 (M_L M_R)^(1/3) Gamma^(-1/3)`.                 (3.4)

The universal value in (3.3) follows from `M_L,M_R<=2^(3/2)`.

#### Proof

Condition on `X_W=w`. The conditional polynomial can be written

`Q_w(x,y)=F_w(x)+G_w(y)+2 x^T M y+c_w`,                               (3.5)

where `F_w,G_w` are arbitrary real quadratic-plus-affine functions. The argument below actually tolerates arbitrary measurable real `F_w,G_w`; only the unit modulus of their phases is used.

Take a thin singular-value decomposition

`M=U Sigma V^T`,
`Sigma=diag(sigma_1,sigma_2,sigma_3)`,                                (3.6)

with `U,V` having orthonormal columns. Decompose `x=Us+x_perp` and `y=Vr+y_perp`. Define the frequency-dependent complex projected amplitudes

`a_t(s)=int_{U^perp} f_I(Us+x_perp) exp(i t F_w(Us+x_perp)) dx_perp`,  (3.7)

`b_t(r)=int_{V^perp} f_J(Vr+y_perp) exp(i t G_w(Vr+y_perp)) dy_perp`.  (3.8)

Let `rho_U,rho_V` be the positive projected densities obtained by deleting the phases. Then pointwise

`|a_t|<=rho_U`, `|b_t|<=rho_V`,                                       (3.9)

and

`int |a_t|<=1`, `int |b_t|<=1`.                                      (3.10)

Consequently

`||a_t||_2^2 <= ||rho_U||_infinity`,
`||b_t||_2^2 <= ||rho_V||_infinity`.                                 (3.11)

By the published product-marginal theorem, both right sides are at most `2^(3/2)` (with the trivial full-bank case handled separately), so

`||a_t||_2 ||b_t||_2 <= 2^(3/2)`.                                   (3.12)

The conditional characteristic function, apart from an irrelevant unit phase, is

`I_w(t)=int_R3 int_R3 a_t(s)b_t(r) exp(2 i t s^T Sigma r) ds dr`.      (3.13)

Use the Fourier convention

`hat b(xi)=int exp(i xi.r)b(r)dr`.

Then

`I_w(t)=int a_t(s) hat b_t(2t Sigma s) ds`.                           (3.14)

Cauchy-Schwarz, the change of variables `xi=2t Sigma s`, and Plancherel give

`|I_w(t)|
 <= ||a_t||_2 [(2|t|)^(-3) Gamma^(-1) int |hat b_t(xi)|^2 dxi]^(1/2)
 = pi^(3/2) ||a_t||_2||b_t||_2 Gamma^(-1/2)|t|^(-3/2).`              (3.15)

Using (3.12),

`|I_w(t)| <= (2*pi)^(3/2) Gamma^(-1/2)|t|^(-3/2)`.                   (3.16)

The bound is uniform in `w`. Averaging the conditional characteristic functions and using `|phi_Q|<=1` yields (3.1).

Let

`C_0=(2*pi)^(3/2) Gamma^(-1/2)`,
`T=C_0^(2/3)=2*pi Gamma^(-1/3)`.                                     (3.17)

Then

`||phi_Q||_1
 <=2[T + C_0 int_T^infinity t^(-3/2)dt]
 =2[T+2C_0 T^(-1/2)]
 =6 C_0^(2/3)
 =12*pi Gamma^(-1/3).`                                               (3.18)

Fourier inversion therefore produces a bounded continuous density and gives (3.3). Retaining `M_L,M_R` rather than their universal caps gives (3.4). QED.

### Scope relative to the fleet's Theorem D

The Claude-attributed volume-sampling theorem D controls a general physical cross block under a row-inclusion/leverage gate. The present theorem is different: it assumes the physical cross block has **exact rank three**, but then needs **no** volume-sampling marginal gate. For example `M=I_3` has row inclusion probability one for each row and fails the theorem-D gate maximally, while Theorem 3.1 applies directly. At exact rank three, `Z=e_3(M^T M)=Gamma^2`, so (3.3) is `6 Z^(-1/6)` without the gate.

This does not imply that the bare three-large-eigenvalue hypothesis forces such a cut; live corrections already contain families where every coordinate cut has cross rank at most two.

## 4. Exterior identity for a rank-two bank plus one transverse row

Let `B` be any real matrix of exact rank two and let

`Delta=sigma_1(B)sigma_2(B)>0`.                                      (4.1)

For a row vector `beta` of compatible length, set

`M_beta=[ beta^T ; B ]`,
`eta_beta=dist(beta, Row(B))`.                                       (4.2)

### Lemma 4.1

`e_3(M_beta^T M_beta)=Delta^2 eta_beta^2`.                            (4.3)

In particular the product of the three nonzero singular values of `M_beta` is

`Gamma_beta=Delta eta_beta`.                                         (4.4)

#### Proof

Choose orthonormal coordinates on the column side so that `Row(B)` is the first two coordinate directions. Write `beta=beta_parallel+beta_perp`. Every three-fold exterior product containing two rows of `B` annihilates `beta_parallel`; only `beta_perp` contributes. Cauchy-Binet says that the sum of squares of all `3x3` minors of `M_beta` is `e_3(M_beta^T M_beta)`, while the sum of squares of all `2x2` minors of `B` is the product of its two nonzero squared singular values, `Delta^2`. Multiplication by `||beta_perp||^2=eta_beta^2` gives (4.3). QED.

The deterministic regression in `check_r17.py` tested (4.3) on fifty seeded random rank-two matrices of varying shapes. The maximum scaled floating-point error was `6.17284001691587e-14`; `CHECK_RESULTS.txt` records `STATUS=PASS`. This is only a regression check; (4.3) is proved symbolically above.

## 5. Application: close every transverse two-sided coupling from r16

After conditioning outside the active packet, the r16 unresolved phase has the form

`Q=d z^2 + 2z(alpha^T x + beta^T y + c)
   +F(x)+G(y)+2x^T B y`,                                             (5.1)

where `z` is one original coordinate, `x` and `y` are disjoint original-coordinate banks, `B` has exact rank two, and `F,G` may contain arbitrary same-bank quadratic and affine terms. Put

`Delta=sigma_1(B)sigma_2(B)`,
`eta_R=dist(beta, Row(B))`,
`eta_L=dist(alpha, Col(B))`.                                         (5.2)

If `eta_R>0`, use the coordinate cut `({z} union x) | y`. Its physical cross block is

`M_R=[ beta^T ; B ]`,                                                 (5.3)

which has exact rank three and singular-value product `Delta eta_R` by Lemma 4.1. Theorem 3.1 therefore gives

`||p_Q||_infinity <= 6 (Delta eta_R)^(-1/3)`.                         (5.4)

Crucially, the terms `d z^2+2z alpha^T x+F(x)` lie wholly inside the left bank and are harmless complex phases in the proof. Thus no one-sided isolation is needed.

Similarly, if `eta_L>0`, use the cut `x | ({z} union y)`. Its exact-rank-three cross block is `[alpha, B]`, giving

`||p_Q||_infinity <= 6 (Delta eta_L)^(-1/3)`.                         (5.5)

Therefore, with

`eta=max(eta_L,eta_R)`,                                               (5.6)

every transverse two-sided packet (`eta>0`) has a bounded continuous density with

`boxed( ||p_Q||_infinity <= 6 (Delta eta)^(-1/3) ).`                  (5.7)

This is the substantive r17 closure. It bypasses the false Gabor-line `L^2` bridge from r16 rather than repairing that bridge.

### Exact residue now isolated

The only two-sided rank-two packet not covered by (5.7) is

`alpha in Col(B)` **and** `beta in Row(B)`.                           (5.8)

In that span-aligned regime, adjoining `z` does not raise either natural cross block above rank two. The third curvature must be extracted from the scalar/self-block Schur geometry rather than from a transverse cross direction. This is a much smaller and algebraically explicit unpaid interface.

## 6. Designated partner result actually applied to an inequality

The designated partner `fleet04/B02` completed

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

canonical proof

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.

If a nonsingular physical `3x3` block `D` has a zero diagonal, it proves

`||p_Q||_infinity <=3*2^(2/3)|det D|^(-1/3)`                         (6.1)

and the genuine integrated estimate

`A_2:=int |phi_Q(t)|^2 dt
 <=6*pi*2^(2/3)|det D|^(-1/3).`                                      (6.2)

I now insert (6.2), not merely its citation, into the new rank-three tail. Suppose a form lies simultaneously in the partner branch and has an exact-rank-three cross block of singular product `Gamma`. From (3.1), write

`C=(2*pi)^(3/2) Gamma^(-1/2)`.

For every `T>0`, Cauchy-Schwarz on low frequencies and (3.1) on high frequencies give

`||phi_Q||_1
 <= sqrt(2 A_2 T) + 4 C T^(-1/2).`                                 (6.3)

Optimizing at `T=4C/sqrt(2A_2)` yields

`||phi_Q||_1 <=4 C^(1/2)(2A_2)^(1/4)`.                               (6.4)

Substitution of (6.2) gives the explicit overlap estimate

`boxed(
 ||p_Q||_infinity
 <=2^(29/12) 3^(1/4)
   |det D|^(-1/12) Gamma^(-1/4)
 <7.026993 |det D|^(-1/12) Gamma^(-1/4).
)`                                                                  (6.5)

The main value of (6.3)-(6.5) is Fourier, not necessarily improvement over taking the minimum of the two direct density estimates: it proves a concrete unweighted `L^1` characteristic-function bound on the intersection of the partner zero-diagonal branch and the new cross-rank-three branch. The deterministic constant check records `7.026992174105906`.

## 7. Full-target status and first unpaid implication

The unrestricted QFORM conjecture remains **OPEN**. The bare condition that `A` have three eigenvalues of modulus at least one does not force an exact-rank-three coordinate cross block, and therefore Theorem 3.1 is not an exhaustive reduction.

For B02's specific r16-to-r17 line, however, the first unpaid implication is now exact:

> **Span-aligned two-sided packet problem.** In (5.1), assume `rank(B)=2`, `alpha in Col(B)` and `beta in Row(B)`. Obtain a dimension-free integrated Fourier/small-ball estimate using the third scalar or same-bank curvature, while retaining original-coordinate product provenance and arbitrary same-bank quadratic phases.

An algebraic shear can formally absorb the aligned `z`-couplings into the two bilinear singular directions, but performing that shear on random variables destroys the product structure. It is therefore not by itself a legal reduction. A valid next mechanism must either keep the shear only in the phase/operator algebra, or route the aligned packet to a physical pivot/ridge/grouped-coordinate theorem without conditioning on rotated coordinates.

This run does not claim target-wide `L^1` Fourier integrability and does not infer full QFORM from the new branch.

## 8. Corrections and source integrity

The proof uses no law-uniform pointwise one-variable quadratic decay, no arbitrary-joint coarea lemma, no conditional projection-height positive moment, no fixed-good-minor dichotomy, no general rotation preserving independence, and no Monte Carlo density evidence. Product structure is used only on disjoint **original-coordinate banks**, followed by a published marginal-density theorem which explicitly permits dependence inside the projected three-dimensional vector.

The source theorem was rechecked at arXiv:1507.07949, Theorem 1.1. The designated partner's full canonical proof was read, not inferred from a summary. The numerical script is an algebra/constant regression only.

## 9. Artifacts

- `REPORT.md`: this proof.
- `check_r17.py`: deterministic exterior-identity/constant regression.
- `CHECK_RESULTS.txt`: actual local execution output.

Execution status remains `WITHOUT_VERIFIED_BRAIN`; repository reads/writes are not native learned-memory ingestion. Configured reasoning and provider reasoning-use telemetry were not exposed and remain `UNKNOWN/null`.
