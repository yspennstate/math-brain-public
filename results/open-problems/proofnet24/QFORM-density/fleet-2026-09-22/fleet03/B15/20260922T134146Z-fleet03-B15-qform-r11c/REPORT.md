# fleet03/B15 — quarter-Hölder coupled-pivot stability and a new C0 branch

**Run:** `20260922T134146Z-fleet03-B15-qform-r11c`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
**Assignment:** Absolute continuity and regularity  
**Classification:** `ESSENTIAL_STEP_APPLIED / CONTINUITY-EXTENSION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and status

The owner target is: for every dimension `n`, every independent real `X_i` with measurable probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues with absolute value at least one, prove one universal finite `C` such that

`P{X^T A X in I} <= C |I|`

for every interval `I`. Equivalently, the output density should have universal essential supremum at most `C`. The owner separately requests a continuous representative.

These two obligations remain separate.

* **Absolute continuity:** already proved for every nonzero quadratic under an absolutely continuous joint law.
* **Essential boundedness for each fixed target matrix:** already proved by fleet01/B15, with a matrix-dependent principal-block constant.
* **Universal matrix- and dimension-independent height bound:** still **OPEN**.
* **Continuous representative:** this report proves a new fully-coupled low-dimensional principal-block branch, with no continuity assumption on the input densities.

I retain the current corrections. In particular I do not use law-uniform pointwise quadratic Fourier decay, independence after rotating to an eigenbasis, a single-cross-minor extraction, a good-local-block-or-rank-three-cut dichotomy, bounded support, moments, log-concavity, or connected support.

## 2. Completed mathematics actually consumed

### Assigned partner: fleet04/B15

Canonical source:

`yspennstate/math-open-problems@657566d3f5026e672f5cbe6b8c03fe63766bf0`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T132108Z-b15-qform-separator-regularity-r2/REPORT.md`

I use two exact pieces from it:

1. the affine principal-block bounds inherited from fleet01/B15 are uniform in every induced linear term;
2. if conditional densities are in `C_0(R)` and have one common height bound, averaging over the conditioning variable preserves continuity and vanishing at infinity by dominated convergence. This final averaging step is applied below to a fully coupled block, not merely cited.

### Coupled rank-two smoother: fleet01/B11

Canonical source:

`yspennstate/math-open-problems@2279571f59ade7a9ec478af1e4818f6c117ac224`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/QFORM-B11-20260922T121344Z/REPORT.md`

It proves:

* every nondegenerate indefinite affine binary quadratic in independent density-capped variables has an `L^3` density with
  `||p||_3 <= C_bin D^{-1/3}`, where `D=-det(S)>0` and
  `C_bin=max(sqrt(2) 5^(1/3) H_{1/2}, 6*2^(2/3)(25/24)^(1/3))`;
* if `R` has an `L^3` density and `V|R=r` has density bounded by one, then `R+dV^2` is essentially bounded.

### Definite binary branch: fleet03/B14

Canonical source:

`yspennstate/math-open-problems@5b82e40a37b4f475866e63f67d48cfd9e3909d0c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260922T123805Z-fleet03-B14-QFORM-r11/REPORT.md`

For a definite symmetric `2x2` block `S`, every affine quadratic in two independent density-capped variables has density height at most

`pi/sqrt(det S)`.

### Three- and four-variable fixed-block bounds: fleet01/B15

Canonical source:

`yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260922T120320Z-fleet01-B15-qform/REPORT.md`

For invertible symmetric blocks,

`K_3(B)=(2*pi+3*sqrt(3))/sigma_min(B)`

and

`K_4(B)=(4*pi+8)/sigma_min(B)`

bound every affine-quadratic output density, uniformly in the affine terms.

## 3. New finite-mass version of dependent-square smoothing

The fleet01/B11 lemma was stated for a probability base law. The exact stability problem needs a finite signed-difference envelope, hence a subprobability version.

### Lemma 3.1 — `QFORM-SUBPROB-DEPENDENT-SQUARE-v1`

Let `mu` be a finite positive law of a pair `(R,V)` with total mass `delta` in `[0,1]`. Assume:

1. the `R`-marginal has density `rho` with `||rho||_3=M`;
2. for `rho(r)dr`-almost every `r`, the conditional law of `V` given `R=r` is a probability density bounded by one.

For `d!=0`, the pushforward of `mu` under

`T=R+dV^2`

has a density `u` satisfying

`boxed( ||u||_infinity <= 4 |d|^(-1/2) M^(3/4) delta^(1/4). )`  (3.1)

The same statement holds after an arbitrary measurable translation of `V` already included in its conditional law.

### Proof

Assume `d>0`; reflection handles `d<0`. Conditional on `R=r`, the density of `dV^2` is bounded by

`d^(-1/2) s^(-1/2) 1_{s>0}`.

Therefore

`u(t) <= d^(-1/2) int_{r<t} rho(r)(t-r)^(-1/2) dr`.          (3.2)

For `L>0`, split at `t-r=L`. Holder gives

`int_{t-L}^t rho(r)(t-r)^(-1/2)dr
 <= M (int_0^L s^(-3/4)ds)^(2/3)
 =2^(4/3) M L^(1/6)`.                                       (3.3)

The far part is at most

`L^(-1/2) ||rho||_1 = delta L^(-1/2)`.                      (3.4)

Choose

`L=(delta/(2^(4/3)M))^(3/2)`

when `M,delta>0`. The two terms are each `2 M^(3/4)delta^(1/4)`. This proves (3.1); the zero cases are trivial. `QED`.

The factor `delta^(1/4)` is the crucial new regularity credit. It is absent if one simply applies the probability version and forgets the finite mass of the perturbation.

## 4. One residual marginal can be changed continuously even through a fully coupled square pivot

Let `B` be an invertible symmetric physical principal block of order `m in {3,4}`. Fix a pivot coordinate `k` inside the block with

`d=B_kk !=0`.

Write

`B=[[C,b],[b^T,d]]`

after putting the pivot last, and let

`S=C-bb^T/d`                                                   (4.1)

be the Schur complement. Since `B` and `d` are nonzero,

`det B=d det S`,                                               (4.2)

so `S` is invertible.

Fix any residual coordinate `i!=k`. Consider two admissible product laws which agree in every marginal except coordinate `i`, where the densities are `f_i,g_i`, and write

`delta=||f_i-g_i||_1 <=1`.                                    (4.3)

### Lemma 4.1 — `QFORM-COUPLED-PIVOT-L1-QUARTER-v1`

The corresponding output densities satisfy

`||p_f-p_g||_infinity <= L_k delta^(1/4)`,                    (4.4)

where `L_k<infinity` depends only on the fixed block `B` and chosen pivot, never on affine terms or on the other input laws.

More explicitly:

#### Four-variable block

Here `S` is invertible `3x3`. Put

`K_S=(2*pi+3*sqrt(3))/sigma_min(S)`.

Then

`boxed( L_k=4 |d|^(-1/2) K_S^(1/2). )`                       (4.5)

#### Three-variable block, definite Schur complement

If `det S>0`, put

`K_S=pi/sqrt(det S)`.

Then

`boxed( L_k=4 |d|^(-1/2) K_S^(1/2)
       =4 sqrt(pi)|d|^(-1/2)(det S)^(-1/4). )`                (4.6)

#### Three-variable block, indefinite Schur complement

If `det S<0`, put `D_S=-det S` and use the fleet01/B11 `L^3` constant. Then

`boxed( L_k=4 C_bin^(3/4)|d|^(-1/2)D_S^(-1/4). )`            (4.7)

### Proof

Condition first on every ambient coordinate outside the block. These values create only affine and constant terms inside the selected block, and all constants below are uniform in those terms.

Complete the square in the **original physical pivot coordinate**:

`Q=d(Z+m(U))^2+R(U)`,                                        (4.8)

where `U` denotes the residual `m-1` original coordinates and the quadratic matrix of `R` is exactly `S`.

The signed difference of the two residual input laws is dominated in total variation by the positive product submeasure obtained by replacing `f_i-g_i` with

`h=|f_i-g_i|`,

which has mass `delta` and pointwise cap one. Because `delta<=1`, extend `h` to a probability density `H>=h` with `H<=1` by adding mass on unused Lebesgue space. Positivity then shows that the residual output submeasure is dominated by the residual output under `H` and the unchanged probability marginals.

If `m=4`, fleet01/B15 gives the latter residual output a density bounded by `K_S`. If `m=3` and `S` is definite, fleet03/B14 gives the bound `K_S`. A positive density `rho` of mass `delta` dominated by `K_S` satisfies

`||rho||_3 <= K_S^(2/3) delta^(1/3) <= K_S^(2/3)`.            (4.9)

If `m=3` and `S` is indefinite, fleet01/B11 gives directly

`||rho||_3 <= C_bin D_S^(-1/3)`,                             (4.10)

because the submeasure is dominated by a completed probability input and the quadratic pushforward is positive.

Under the positive submeasure, `Z` is still independent of `U`. Conditional on `R(U)=r`, the variable

`V=Z+m(U)`

is a mixture of translations of the original `Z` density, hence its conditional density is bounded by one. Lemma 3.1 therefore applies. Substituting (4.9) or (4.10) into (3.1) yields (4.5)-(4.7). Averaging the conditional signed measures over the outside coordinates preserves the same domination. `QED`.

This is a genuinely fully coupled stability statement. No separator between the pivot and residual coordinates is required; the coupling is absorbed by the completed-square shift `m(U)`.

## 5. Main new continuity theorem: two physical square pivots suffice

The previous fleet03/B15 run required, for every rough marginal, a **disjoint smoothing block**. That condition fails precisely in important low-rank hyperbolic deletion cases. Lemma 4.1 gives a different mechanism.

### Theorem 5.1 — `QFORM-TWO-PIVOT-C0-v1`

Suppose the full symmetric matrix `A` contains an invertible physical principal block `B` of order `m=3` or `m=4` such that at least two diagonal entries of `B` are nonzero.

Then for every independent ambient input with arbitrary measurable probability densities `0<=f_i<=1`, the law of

`Q=X^T A X`

has a density with a representative

`boxed( p_Q in C_0(R). )`                                    (5.1)

In particular the density is bounded and uniformly continuous. No input-density continuity is assumed.

The height is still only the fixed-block bound

`||p_Q||_infinity <= K_m(B)`,                                (5.2)

with

`K_3(B)=(2*pi+3*sqrt(3))/sigma_min(B)`,

`K_4(B)=(4*pi+8)/sigma_min(B)`.

Thus this theorem is a regularity theorem, not the missing universal-height theorem.

### Proof

Let `I` be the coordinates of `B`. Because at least two diagonal entries of `B` are nonzero, for every `i in I` one can choose a pivot `k(i) in I\{i}` with `B_{k(i),k(i)}!=0`.

For each `i`, Lemma 4.1 supplies a finite constant `L_i` such that changing only marginal `i` by `L^1` distance `delta<=1` changes the conditional block-output density by at most

`L_i delta^(1/4)` in `L^infinity`, uniformly over all affine terms induced by coordinates outside `I`.                                               (5.3)

Approximate each rough block marginal `f_i` in `L^1` by smooth compactly supported probability densities `f_i^(r)` satisfying `0<=f_i^(r)<=1`. Such approximations were constructed explicitly in the preceding fleet03/B15 report: truncate, restore the lost mass on a disjoint interval without exceeding one, then mollify by a nonnegative compact probability kernel.

Fix the outside coordinates at `w`. For smooth block inputs, the conditional polynomial is a nondegenerate affine quadratic with matrix `B`; its characteristic function has the standard fixed-amplitude `|t|^{-m/2}` stationary-phase decay, hence its output density `p_{r,w}` lies in `C_0(R)` because `m>=3`.

For large `r,s`, telescope over the `m` block marginals and use (5.3):

`||p_{r,w}-p_{s,w}||_infinity
 <= sum_{i in I} L_i ||f_i^(r)-f_i^(s)||_1^(1/4) ->0`,       (5.4)

uniformly in `w`. Thus `p_{r,w}` converges uniformly to a function `p_w in C_0(R)`. Total-variation convergence of the block input laws identifies `p_w(t)dt` with the true conditional output law under the original rough block marginals.

Fleet01/B15 also gives, uniformly in `w`,

`0<=p_w(t)<=K_m(B)`.                                         (5.5)

Now apply the completed fleet04/B15 conditional-averaging step to the actual conditional family `{p_w}`:

`p_Q(t)=E[p_{X_{I^c}}(t)]`.                                  (5.6)

For any `t_n->t`, `p_w(t_n)->p_w(t)` for almost every `w` and (5.5) is a common dominating bound, so dominated convergence proves continuity of `p_Q`. Likewise `p_w(t)->0` as `|t|->infinity` for each fixed `w`, and another dominated-convergence application gives `p_Q(t)->0`. Hence `p_Q in C_0(R)`, and (5.2) follows from (5.5). `QED`.

## 6. What this closes relative to the preceding B15 run

The preceding fleet03/B15 continuity theorem already covered:

* every target matrix of rank at least five;
* any marginal having a disjoint invertible `3x3/4x4` smoothing block;
* any marginal having a disjoint definite `2x2` smoothing block.

The new theorem also covers low-rank **fully coupled** configurations where deletion leaves an indefinite rank-two block, provided a physical invertible `3x3` or `4x4` principal block has two nonzero square pivots. This is exactly a branch where the former disjoint-smoothing argument can fail.

The assigned partner fleet04/B15 required an exact original-coordinate separator between two smoothing groups. Theorem 5.1 does not: all block coordinates may couple to one another and arbitrarily to the outside coordinates. The price is a fixed-block, not universal, constant.

A remaining local continuity obstruction can therefore be stated more sharply:

> after using the previous rank>=5/disjoint-smoothing branches, the unresolved low-rank cases include matrices for which every usable invertible `3x3/4x4` physical block has at most one nonzero diagonal square pivot (together with any residual configurations not captured by those local blocks).

Zero-diagonal or single-square-pivot hyperbolic structures are the natural next mechanism to attack; repeating the same square-pivot proof cannot change their status.

## 7. Essential-boundedness ledger remains separate

This run does **not** promote continuity progress into the universal height theorem.

For every fixed target matrix `A`, fleet01/B15 already gives an essentially bounded density with a finite matrix-dependent constant. In particular, if `B` is the block of Theorem 5.1, (5.2) is a valid interval bound.

But the full target asks for one `C` independent of `A` and `n`. The fresh correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` gives a spectrum-`{1,1,-1}` family for which every nonsingular physical principal triple has singular scale of order `1/m` and every coordinate cut has cross rank at most two. Hence a universal proof cannot be obtained by asserting either a well-conditioned local block or a rank-three cross cut.

The first unpaid **central** implication remains a dimension-free aggregation/small-ball mechanism for that mixed localized/diffuse residual class, equivalently the finite-fragment extreme product class from the preceding fleet03/B15 reduction.

The first unpaid **continuity** implication after this report is narrower: control the zero-diagonal / single-nonzero-diagonal low-rank blocks without assuming continuity of the input densities, preferably by a bilinear or multi-pivot stability estimate rather than another generic approximation.

## 8. Exact status

**PROVED in this run:**

1. the finite-mass dependent-square estimate (3.1), retaining the perturbation-mass factor `delta^(1/4)`;
2. `L^1`-quarter-Hölder output-density stability for a residual marginal through a fully coupled nonzero square pivot, with explicit constants in (4.5)-(4.7);
3. a `C_0` continuous-representative theorem for any target matrix containing an invertible physical principal `3x3` or `4x4` block with at least two nonzero diagonal entries;
4. the ambient conditional-to-unconditional step by applying fleet04/B15's common-height dominated-convergence mechanism.

**NOT PROVED:**

* one universal `L^infinity` constant independent of `A,n`;
* continuity for every zero-diagonal/single-square-pivot low-rank configuration;
* the full QFORM conjecture.

No novelty or publication-priority claim is made.
