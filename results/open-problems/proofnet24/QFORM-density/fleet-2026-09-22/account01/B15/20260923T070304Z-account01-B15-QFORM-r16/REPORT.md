SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T07:03:04Z.
attacking: a moment-free joint matrix/source limit theorem for the live volume-density estimates, so generic matrix perturbations and rough-law approximations can be removed without using continuity as the height argument.

# account01/B15 r16 — moment-free closed-envelope limit theorem and a sharp obstruction to uniform matrix perturbation

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** absolute continuity and regularity  
**Status:** `ESSENTIAL_STEP_APPLIED / JOINT_SOURCE-MATRIX_CLOSURE / FULL_QFORM_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted three-large-eigenvalue theorem remains OPEN.

## 1. Exact live obligation

The newest delivery plan asks B15 to supply the precise rough-law limit or trace justification used by new density estimates, with continuity kept separate from the central `L^infinity` bound. The current volume theorem proves a law-independent integrable characteristic-function envelope on a substantial original-coordinate cross-block class. The completed assigned-partner `account02/B15` theorem then gives quantitative source `L1 -> output L^infinity` and Holder stability for two laws under the same power envelope.

A remaining limiting issue appears whenever one first proves a density estimate after a generic or structural perturbation of the matrix and then wants to remove that perturbation without moments. The common but invalid heuristic is that a small operator-norm perturbation of the matrix produces a uniformly small random quadratic perturbation; arbitrary cap-one inputs may be translated arbitrarily far, so this is false.

This report gives the correct replacement. A common integrable Fourier envelope makes coefficient perturbations stable for every **fixed** source by dominated convergence, with no moment assumptions. Combined with the completed `account02/B15` source theorem, this yields a joint rough-source/matrix closure principle. I also give an exact target-class counterexample showing that no law-uniform modulus in matrix operator norm can exist.

## 2. Sources actually used

Current volume theorem:

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an original-coordinate cross block `M=A[I,J]`, if its volume marginals satisfy `alpha_i<=q/2`, `1<=q<3/2`, and `Z=e3(M^T M)>0`, that theorem gives

`|phi_Q(t)| <= min(1,K|t|^{-b}),`

`b=3/(2q)>1`,

`K=[e^3 q^(-3/2) pi^3 Z^(-1/2)]^(1/(2q))`,

and therefore

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`.

The estimate is law-independent over arbitrary cap-one product sources and retains all within-bank terms, outside couplings and affine terms.

Completed assigned-partner theorem actually applied:

`yspennstate/math-open-problems@beba6425b1130ce83dd870c447fc0e87bcc5bd58`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T060010Z-account02-B15-QFORM/REPORT.md`.

If two sources for the same phase have joint-density `L1` distance `Delta` and both output characteristic functions obey

`|phi_F(t)|,|phi_G(t)| <= min(1,K|t|^{-b}), b>1`,

then

`||p_F-p_G||_infinity <= [b/(pi(b-1))](2K)^(1/b) Delta^(1-1/b)`.      (2.1)

For `0<alpha<min(1,b-1)`, the partner also proves an explicit `C^{0,alpha}` difference estimate. At the current `q=4/3`, `b=9/8`,

`||p_F-p_G||_infinity <39.233 Z^(-1/6) Delta^(1/9)`,                  (2.2)

and for `alpha=1/16`,

`[p_F-p_G]_{C^{0,1/16}} <166.572 Z^(-17/96) Delta^(1/18)`.           (2.3)

These partner inequalities are applied below to an actual joint perturbation estimate.

## 3. Moment-free matrix-perturbation closure under a common envelope

### Theorem 3.1 — fixed-source coefficient closure

Let `mu` be any probability law on `R^n`. Let

`q_m(x)=x^T A_m x+b_m^T x+c_m`,

`q(x)=x^T A x+b^T x+c`,

with `A_m->A`, `b_m->b`, `c_m->c` coefficientwise (equivalently in any finite-dimensional norm). Write

`phi_m(t)=int exp(i t q_m(x)) dmu(x)`,

`phi(t)=int exp(i t q(x)) dmu(x)`.

Assume that one function `H in L^1(R)` satisfies

`|phi_m(t)|<=H(t)` for every `m,t`.                                      (3.1)

Then:

1. `|phi(t)|<=H(t)` for every `t`;
2. every `q_m(X)` and `q(X)` has a `C_0(R)` density `p_m,p`;
3.

`boxed{ ||p_m-p||_infinity <= (2pi)^(-1)||phi_m-phi||_1 ->0. }`       (3.2)

No moment of `mu` is required.

If additionally `|t|^alpha H(t) in L^1(R)` for some `0<alpha<=1`, then

`boxed{ [p_m-p]_{C^{0,alpha}} ->0. }`                                  (3.3)

#### Proof

For every fixed `x`, coefficient convergence gives `q_m(x)->q(x)`. Therefore

`exp(i t q_m(x))->exp(i t q(x))`

for every fixed `t,x`. The integrands have modulus one, so ordinary dominated convergence against the probability measure `mu` gives

`phi_m(t)->phi(t)`                                                      (3.4)

for each `t`.

Taking limits in (3.1) gives `|phi(t)|<=H(t)`. Thus

`|phi_m(t)-phi(t)|<=2H(t)`,                                             (3.5)

and dominated convergence on the Fourier side yields

`||phi_m-phi||_1->0`.                                                    (3.6)

Since every `phi_m` and `phi` belongs to `L^1`, Fourier inversion gives `C_0` densities. The inversion estimate gives (3.2).

For (3.3), use

`|e^{-ith}-1|<=2^(1-alpha)|t h|^alpha`.

Hence

`[p_m-p]_{C^{0,alpha}}`
` <= 2^(1-alpha)/(2pi) int |t|^alpha |phi_m(t)-phi(t)| dt`.             (3.7)

The integrand tends pointwise to zero and is dominated by `2|t|^alpha H(t)`, proving (3.3). QED.

### Why this is the correct perturbation statement

The proof never bounds `|q_m(X)-q(X)|` in expectation or probability by a moment of `X`. It only uses pointwise convergence for each finite `x` and the integrable Fourier envelope already paid by the density mechanism. Thus arbitrary fragmented/unbounded cap-one inputs are allowed.

## 4. Weak-source plus matrix closure

The previous theorem can be widened beyond `L1` source approximation.

### Theorem 4.1 — weak-source closed-envelope theorem

Let `mu_m => mu` weakly on `R^n`. Let `q_m,q` be continuous and assume `q_m->q` uniformly on compact subsets. Put

`nu_m=(q_m)_# mu_m`, `nu=q_# mu`.

Suppose their characteristic functions satisfy one common envelope

`|hat nu_m(t)|<=H(t)`, `H in L^1(R)`.                                   (4.1)

Then `nu_m=>nu`, `|hat nu(t)|<=H(t)`, all `nu_m,nu` have `C_0` densities, and

`boxed{ ||p_m-p||_infinity ->0. }`                                      (4.2)

If `|t|^alpha H in L^1`, then convergence also holds in the `C^{0,alpha}` seminorm.

#### Proof

Weak convergence makes `{mu_m}` tight. For any bounded continuous `g` on `R`, `g(q_m(x))->g(q(x))` uniformly on each fixed compact set. Tightness therefore gives

`int g(q_m)dmu_m -> int g(q)dmu`,

so `nu_m=>nu`. In particular their characteristic functions converge pointwise. The rest is exactly the Fourier dominated-convergence argument of Theorem 3.1. QED.

### Cap-one product class is closed under marginal weak limits

Suppose for each physical coordinate `i`,

`mu_{i,m}=f_{i,m}(x)dx`, `0<=f_{i,m}<=1`,

and `mu_{i,m}=>mu_i`. For every nonnegative `psi in C_c(R)`,

`int psi dmu_i = lim_m int psi f_{i,m} dx <= int psi dx`.

Hence `mu_i<=Lebesgue` as measures, so `mu_i=f_i dx` with `0<=f_i<=1`. In fixed finite dimension, convergence of all marginals implies convergence of the product laws. Therefore Theorem 4.1 remains entirely inside the original cap-one product class.

This is useful when a proof reaches a source only by weak approximation rather than `L1` mollification. Tightness is the exact needed hypothesis; no unattained optimizer on the whole line is silently assumed.

## 5. Joint source/matrix closure: actual use of account02/B15

Let

`F_m=prod_i f_{i,m}`, `F=prod_i f_i`,

with

`Delta_m=||F_m-F||_1 ->0`.                                                (5.1)

Let `q_m->q` coefficientwise. Assume a law-independent matrix certificate gives the **same** power envelope

`min(1,K|t|^{-b}), b>1`,                                                   (5.2)

for the outputs of `q_m` under both sources `F_m` and `F`, uniformly in `m`.

Denote the corresponding densities by

`p_m=p_{F_m,q_m}`, `r_m=p_{F,q_m}`, `p=p_{F,q}`.

By the completed partner inequality (2.1),

`||p_m-r_m||_infinity`
` <= [b/(pi(b-1))](2K)^(1/b) Delta_m^(1-1/b).`                            (5.3)

By Theorem 3.1, applied to the fixed source `F`,

`||r_m-p||_infinity ->0`.                                                  (5.4)

Therefore

`boxed{
 ||p_m-p||_infinity
 <= [b/(pi(b-1))](2K)^(1/b) Delta_m^(1-1/b)+o(1).
}`                                                                           (5.5)

This is the promised actual application of the completed assigned-partner result. It simultaneously removes rough-source smoothing and coefficient perturbation, while the two mechanisms are kept logically separate.

If `0<alpha<b-1`, the partner's Holder estimate plus (3.7) gives the analogous

`[p_m-p]_{C^{0,alpha}} <= C_{K,b,alpha} Delta_m^{1-(alpha+1)/b}+o(1)`.      (5.6)

The height conclusion (5.5) is primary; continuity/Holder regularity is an additional consequence.

## 6. Concrete corollary for the live q=4/3 volume branch

Let `M_m` be the same physical cross block of `q_m`. Suppose

`alpha_i(M_m)<=2/3` for every row and every `m`,

and

`Z_m=e3(M_m^T M_m)>=Z_0>0`.                                                (6.1)

The current volume theorem gives a common power envelope with

`b=9/8`

and with `K` bounded above by the value obtained from `Z_0`. Therefore the limit output satisfies

`boxed{ ||p||_infinity <= (9 sqrt(3)e/2) Z_0^(-1/6). }`                    (6.2)

If `F_m->F` in `L1`, then the full joint approximation has the explicit estimate

`boxed{
 ||p_m-p||_infinity
 <39.233 Z_0^(-1/6) Delta_m^(1/9)+o(1).
}`                                                                           (6.3)

At `alpha=1/16`,

`boxed{
 [p_m-p]_{C^{0,1/16}}
 <166.572 Z_0^(-17/96) Delta_m^(1/18)+o(1).
}`                                                                           (6.4)

Thus a proof established first for smooth sources and generic coefficient matrices in the volume-certified class passes to arbitrary rough cap-one product sources and coefficient-limit matrices with **no loss in the density constant**, provided the integrable volume envelope remains uniformly nondegenerate (`Z_m>=Z_0`).

This is precisely where generic perturbation is legitimate. If the certificate degenerates, e.g. `Z_m->0`, this theorem deliberately gives no conclusion.

## 7. Source-valid obstruction: there is no law-uniform matrix-perturbation modulus

The preceding closure is instancewise in the limiting source. This restriction is necessary even inside the owner target.

For `0<epsilon<1`, take dimension four and

`A=diag(1,1,1,0)`,

`A_epsilon=diag(1,1,1,epsilon)`.

Both matrices have at least three eigenvalues of modulus at least one and

`||A_epsilon-A||op=epsilon ->0`.                                           (7.1)

Let `X_1,X_2,X_3` be independent `Uniform[-1/2,1/2]` variables, and let

`X_4 ~ Uniform[epsilon^(-1/2), epsilon^(-1/2)+1]`,                         (7.2)

independent of them. Every marginal density is exactly one on a unit interval.

Write

`S=X_1^2+X_2^2+X_3^2`.

Then

`Q_A=S`,

so

`supp(Q_A) subset [0,3/4]`.                                                 (7.3)

But

`Q_{A_epsilon}=S+epsilon X_4^2`,

and (7.2) gives

`epsilon X_4^2 in [1,1+2 sqrt(epsilon)+epsilon]`.                          (7.4)

Therefore

`supp(Q_{A_epsilon}) subset [1, 7/4+2 sqrt(epsilon)+epsilon]`,              (7.5)

which is disjoint from `[0,3/4]`. Hence the two output probability laws have total-variation distance one for every `epsilon`.

Moreover, if `p_S` denotes the density of `S`, then because it is a probability density supported on an interval of length `3/4`,

`||p_S||_infinity >=4/3`.                                                   (7.6)

On `[0,3/4]`, the perturbed output density is identically zero, so

`boxed{ ||p_{Q_{A_epsilon}}-p_{Q_A}||_infinity >=4/3. }`                    (7.7)

Thus there is **no** universal modulus `omega(delta)->0` such that

`||p_{X^T B X}-p_{X^T A X}||_infinity <= omega(||B-A||op)`                 (7.8)

uniformly over the owner target and arbitrary cap-one product laws. There is not even uniform total-variation continuity.

This does not refute QFORM. It proves that matrix genericization must be removed either with the same fixed source (Theorem 3.1), with controlled source convergence (Theorem 5.1), or by some other source-sensitive argument. A bare small matrix norm is insufficient.

## 8. Absolute continuity, boundedness and continuity ledger

The logical separation is now precise.

- **Absolute continuity:** already holds for every nonzero quadratic form of an absolutely continuous joint input by coarea; target rank three is not needed.
- **Universal essential boundedness:** still the central OPEN implication. On the current volume branch it is supplied directly by the integrable envelope, not by continuity.
- **Continuity:** on an integrable-envelope branch, Fourier inversion gives a `C_0` representative as an additional output. Theorem 3.1 shows this regularity is stable under fixed-source coefficient limits. The partner theorem supplies quantitative Holder stability under source `L1` approximation.
- **No uniform raw regularity principle:** earlier partner constructions rule out target-uniform continuity/Besov moduli in general, so continuity cannot replace the universal-height argument.

## 9. What this changes in the proof map

A common-integrable-envelope branch is now closed under both of the limiting operations that repeatedly occur in the current proof programme:

1. rough original-coordinate source approximation;
2. generic or boundary coefficient-matrix approximation.

No moments, bounded supports, post-rotation independence, or pointwise law-uniform stationary-phase bound are used. The new obstruction (7.1)-(7.7) explains exactly why the matrix limit must be handled through the envelope rather than through direct control of the random quadratic error.

The remaining global theorem is still the structural one: every target matrix must be forced into a paid volume/ridge/physical-pivot/bank branch, or the surviving minority/two-sheet product-sensitive term must be bounded. Near-singular branches in which the available envelope constant degenerates remain genuinely unpaid.

## 10. Corrections respected

This report uses none of the refuted premises: no law-uniform pointwise quadratic Fourier decay; no independence after diagonalising the matrix; no arbitrary-joint rank-three coarea height theorem; no worst spectral-fiber supremum; no generic X-ray-only control of the two-sheet trace; no claim that a small operator-norm matrix perturbation is a uniformly small random perturbation.

Full QFORM remains OPEN.
