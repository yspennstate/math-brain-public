SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-22T23:00:03Z.
attacking: translation/localization closure for the rank-one heavy-star branch via logarithmic leakage, plus a target-valid remote-fragment obstruction to coefficient-perturbation arguments.

# account02/B14 — logarithmic leakage averaging and a remote-fragment perturbation barrier

Run: `20260922T230003Z-account02-B14-QFORM-r22`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Translations and localization` / complementary constructions and source-valid counterexamples  
Status: `NEW SUPPORTING THEOREMS + REFUTED INTERMEDIATE MECHANISM / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and first unpaid implication

The full target remains OPEN: for every finite `n`, every collection of independent real random variables with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a genuine counterexample.

No moment, support-radius, connected-support, centering, identical-distribution, Gaussian, log-concavity, or post-rotation independence assumption is used here. The live corrections excluding law-uniform pointwise quadratic-phase decay, arbitrary-joint three-dimensional coarea, positive moments of conditional projection-density suprema, bounded-diameter/fragment-count localization, fragmentwise cap renormalization, and near-zero half-Riesz substitution are all retained.

The preceding B14 run reduced the remaining rank-one leakage problem to a precise analytic question: a raw reciprocal kernel is critical in one leakage dimension, but a logarithmic kernel is integrable. The first unpaid implication attacked here is therefore:

> If an original-coordinate indefinite physical pair gives the established logarithmic conditional density envelope and its moving critical value has a one-dimensional density cap, average the logarithm *before* taking a worst-case supremum, with no support, shift, fragment, or moment parameter.

This run proves that compiler with an exact optimized constant, composes it with a fresh reverse-conditioned bank theorem, and separately proves that small matrix coefficients cannot be treated as uniformly small output-law errors because distant fragments amplify them at reciprocal scale.

## 2. Source-pinned inputs actually applied

### 2.1 Assigned partner account03/B14 r20

The newest completed assigned-partner result consumed is

`yspennstate/math-open-problems@3034661243d00674dd35b8c9f0959e68d9379543`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T223655Z-account03-B14-QFORM-r20/REPORT.md`.

It proves `QFORM-SAME-EXTREME-LP-FOURIER-LOCALIZATION-v1`: for every measurable real map `P`, every nonnegative Borel weight `w`, and every `p>=1`, the worst-case value of

`int w(t) |E exp(i t P)|^p dt`

is exactly the same over all cap-one product laws as over compact finite-fragment product laws whose one-dimensional marginals are indicators of unit-measure finite unions of intervals. It also proves that no positive polynomial Fourier weight is uniformly bounded over the full target class, even for `A=I_3` and fixed compact support.

The present counterexample below already belongs to that extreme class. Thus the obstruction is not an artifact of unbounded support or of passing from general laws to extreme finite-fragment laws; it survives the strongest zero-loss localization currently available.

### 2.2 Logarithmic physical-pair envelope

The source-complete supporting pair calculation used below is recorded at

`yspennstate/math-open-problems@b873b2b52f4c75c331153c9227d0a7fae0f02979`

path

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`,

with the underlying companion pair proof source-pinned there. If two ORIGINAL coordinates form an invertible indefinite principal pair `B`, put

`D=|det B|`, `kappa=sigma_min(B)>0`.

After completing that pair, let `R` be its outside critical-value/remainder random variable. For every cutoff `r>0`, the source proves the pointwise density envelope

`p_Q(t) <= 2 sqrt(2)/r
          + D^(-1/2) E log_+( 2 r^2 / (kappa |t-R|) ).`        (2.1)

All pair variables remain original-coordinate independent of the outside variables, and arbitrary affine terms are retained. The source status is a complete supporting analytic argument, pending independent review; the present run does not upgrade that review status.

### 2.3 Fresh compatible reverse-conditioned bank theorem

A fresh compatible result appearing during this run is account02/B05

`yspennstate/math-open-problems@b6ded18bee0fe20353530653ce654308cac0631c`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T225232Z-account02-B05-QFORM-37473ccc/REPORT.md`.

Its proved theorem says that if `X,Y` are independent cap-one pivots, `U,V` are disjoint independent product banks, `L=L(U)` and `M=M(V)` have density caps `L0,M0`, and `H(U,V)` is arbitrary measurable, then

`R=H(U,V)+2 X M(V)+2 Y L(U)`

has

`||p_R||_infinity <= 2 sqrt(L0 M0).`                            (2.2)

This is applied in Section 5 below, not merely cited.

## 3. Exact one-dimensional logarithmic leakage averaging

The key analytic fact is elementary but exactly matches the critical one-dimensional leakage threshold.

### Theorem 3.1 — `QFORM-LOG-LEAKAGE-BATHTUB-v1`

Let `R` be a real random variable with probability density bounded by `H<infinity`. Then for every `t in R` and every `a>0`,

`E log_+( a/|t-R| ) <= Psi(2 H a),`                              (3.1)

where

`Psi(u) = u,                         0<=u<=1,`
`Psi(u) = 1+log u,                   u>=1.`                      (3.2)

The estimate is uniform in every translation of `R`. It is sharp among all one-dimensional probability densities bounded by `H`.

#### Proof

Use the layer-cake identity

`log_+(a/|t-R|)
 = int_0^infinity 1_{|t-R|<a e^{-v}} dv.`                       (3.3)

A density cap `H` gives

`P(|t-R|<rho) <= min(1,2H rho).`                                (3.4)

Therefore, with `u=2Ha`,

`E log_+(a/|t-R|)
 <= int_0^infinity min(1,u e^{-v}) dv.`                         (3.5)

If `u<=1`, the last integral equals `u`. If `u>=1`, split at `v=log u`; the value is `log u+1`. This proves (3.1)-(3.2).

For sharpness, take `R` uniform with density `H` on the interval of length `1/H` centered at `t`. Direct integration gives equality in (3.1) for every `a>0`. QED.

This sharpness is useful: without additional structure, the logarithmic dependence in the large-`Ha` regime cannot be removed by a better density-cap argument.

## 4. Optimized physical-pair + rank-one leakage compiler

Insert Theorem 3.1 into the source pair envelope (2.1).

### Theorem 4.1 — `QFORM-PAIRLOG-RANK1-LEAKAGE-v1`

Assume the setting of (2.1), and suppose the completed pair's critical-value variable `R` has density cap `H<infinity`. Define

`theta = 2 sqrt( 2 D H / kappa ).`                              (4.1)

Then `Q` has an essentially bounded density satisfying

`boxed:
||p_Q||_infinity <= C_log(D,kappa,H),`

where

`C_log(D,kappa,H)
 = 6 [ H/(kappa sqrt(D)) ]^(1/3),                 theta<=1,`    (4.2)

and

`C_log(D,kappa,H)
 = D^(-1/2) [ 3 + 2 log(theta) ],                 theta>=1.`   (4.3)

The two formulas agree at `theta=1`. The estimate is uniform in arbitrary translations of `R` and of the physical pair; no support, diameter, fragment count or moment enters.

#### Proof

By (2.1) and Theorem 3.1,

`p_Q(t)
 <= A/r + B Psi(q r^2),`                                         (4.4)

where

`A=2 sqrt(2)`, `B=D^(-1/2)`, `q=4H/kappa`.

Put `x=q r^2` and `a0=A sqrt(q)=4 sqrt(2H/kappa)`. Then

`p_Q(t) <= a0 x^(-1/2) + B Psi(x).`                             (4.5)

For `x<=1`, minimize

`a0 x^(-1/2)+Bx`.

The stationary point is

`x0=(a0/(2B))^(2/3)=theta^(2/3).`                               (4.6)

It lies in `[0,1]` exactly when `theta<=1`; its value is

`3*2^(-2/3) a0^(2/3) B^(1/3)
 =6 [H/(kappa sqrt(D))]^(1/3).`                                 (4.7)

For `x>=1`, minimize

`a0 x^(-1/2)+B(1+log x).`

Its stationary point satisfies `sqrt(x)=a0/(2B)=theta`. It lies in `[1,infinity)` exactly when `theta>=1`, and its value is

`2B+B[1+2log(theta)]
 =B[3+2log(theta)].`                                             (4.8)

At `theta=1`, both values equal `3B`. This proves (4.2)-(4.3), uniformly in `t`. Tonelli and the conditional density formula give absolute continuity. QED.

### Corollary 4.2 — product-linear moving critical value

If

`R = ell dot Z + b`

for independent cap-one original-coordinate variables `Z`, then the product-safe one-dimensional projection theorem used in the preceding B14 run gives

`H <= sqrt(e)/||ell||_2.`                                       (4.9)

Therefore Theorem 4.1 gives a completely translation-uniform density bound depending only on `(D,kappa,||ell||_2)`. In particular, whenever `D`, `kappa`, and `||ell||_2` are bounded below by universal positive constants, this rank-one logarithmic-leakage branch is universally paid.

This is precisely the favorable alternative anticipated by `QFORM-RANK2-LEAKAGE-OR-LOG-STAR-BRIDGE-v1`: one leakage dimension is enough once the conditional singularity has been softened from reciprocal to logarithmic order.

## 5. Composition with arbitrary bank leakage

The fresh B05 theorem (2.2) can be used as the critical-value density input in Theorem 4.1.

### Corollary 5.1 — `QFORM-PAIRLOG-OVER-REVERSEBANK-v1`

Suppose an invertible indefinite original-coordinate physical pair has parameters `(D,kappa)` as above, and after pair completion its outside critical value has the original-coordinate product representation

`R=H0(U,V)+2 X M(V)+2 Y L(U),`                                  (5.1)

where `X,Y,U,V` are mutually independent in the exact B05 sense, `H0` is arbitrary measurable, and the scalar slopes have density caps `L0,M0`. Then

`||p_R||_infinity <= H_R := 2 sqrt(L0 M0),`                     (5.2)

and hence

`boxed:
||p_Q||_infinity <= C_log(D,kappa,2 sqrt(L0 M0)).`              (5.3)

No size, moment, regularity, translation, support, or fragment assumption on `H0` is required.

If the slopes are linear bank aggregates with Euclidean coefficient norms `s=||c||_2`, `r=||b||_2`, the source product-marginal estimate gives

`L0<=sqrt(2)/s`, `M0<=sqrt(2)/r`,

so

`H_R <= 2 sqrt(2)/sqrt(rs).`                                    (5.4)

Thus any structural branch with `D`, `kappa`, and `rs` quantitatively bounded below is closed by an explicit universal constant even when the completed remainder contains arbitrary measurable interactions between the two outside banks.

#### Why this is a genuine composition

The B05 theorem spends arbitrary bank leakage *before* the logarithmic pair singularity: it produces a true one-dimensional density cap for the whole critical value `R`. Theorem 4.1 then integrates the moving pair singularity against that law. No conditional-cap surrogate is used and no independence is asserted after a rotation. Every conditioning step is on disjoint original-coordinate product blocks.

## 6. Target-valid remote-fragment obstruction to coefficient perturbation

A common possible way to bridge a near-span or small-coefficient structural state is to say that a matrix entry of size `epsilon` is a uniformly small perturbation. Under the present hypotheses this is false, even if both matrices already satisfy the full three-large-eigenvalue target and even if all input laws are compact finite-fragment extremes.

### Proposition 6.1 — `QFORM-NO-UNIFORM-COEFFICIENT-PERTURBATION-CONTINUITY-v1`

There is no function `omega(delta)->0` such that for every pair of target-valid symmetric matrices `A,B` with `||A-B||_op<=delta` and every admissible cap-one product law `mu`,

`d_TV( Law_mu(X^TAX), Law_mu(X^TBX) ) <= omega(delta).`          (6.1)

In fact, for every `0<epsilon<=1` there are target-valid `A_0,A_epsilon` with

`||A_epsilon-A_0||_op=epsilon`                                  (6.2)

and one compact finite-fragment extreme product law `mu_epsilon` such that

`d_TV( Law(Q_epsilon), Law(Q_0) ) >= 1/128.`                    (6.3)

#### Construction

Take `n=4` and

`A_0 = diag(1,1,1,0),`

`A_epsilon = A_0 + epsilon(e_1 e_4^T+e_4 e_1^T).`               (6.4)

Then `||A_epsilon-A_0||_op=epsilon`. The spectrum of `A_epsilon` is

`1, 1, (1+sqrt(1+4epsilon^2))/2,
        (1-sqrt(1+4epsilon^2))/2.`                              (6.5)

Hence both `A_0` and `A_epsilon` have at least three eigenvalues of absolute value at least one.

Let `X_1,X_2,X_3` be iid `Uniform[0,1]`. Let `X_4` have density one on

`E_epsilon = I_- union I_+,`

`I_-=[-epsilon^(-1)-1/4,-epsilon^(-1)+1/4],`
`I_+=[ epsilon^(-1)-1/4, epsilon^(-1)+1/4].`                    (6.6)

Each interval has length `1/2`, so `1_{E_epsilon}` is a cap-one probability density. It is a compact two-fragment extreme law for each epsilon.

Now

`Q_0=X_1^2+X_2^2+X_3^2 >=0` almost surely,                     (6.7)

whereas

`Q_epsilon=Q_0+2epsilon X_1X_4.`                                (6.8)

Consider the event

`G={X_4 in I_-, X_1 in [3/4,1], X_2,X_3 in [0,1/4]}.`          (6.9)

Its probability is

`P(G)=(1/2)(1/4)^3=1/128.`                                     (6.10)

On `I_-`,

`epsilon X_4 <= -1+epsilon/4`,

so for `x=X_1 in [3/4,1]`,

`x^2+2epsilon xX_4
 <=x^2-(2-epsilon/2)x.`                                         (6.11)

The right side is convex in `x`; on `[3/4,1]` its maximum occurs at an endpoint. For `epsilon<=1`,

at `x=3/4`: `-15/16+3epsilon/8 <= -9/16`,

at `x=1`:   `-1+epsilon/2 <= -1/2`.

Hence the first-coordinate contribution is at most `-1/2`. Also

`X_2^2+X_3^2 <= 2(1/4)^2=1/8` on `G`. Therefore

`Q_epsilon <= -3/8` on `G`.                                    (6.12)

Thus

`P(Q_epsilon<0)>=1/128`, while `P(Q_0<0)=0`, proving (6.3). QED.

### Interpretation

The coefficient `epsilon` is small, but a support component at distance `1/epsilon` turns the perturbation `2epsilon X_1X_4` into an order-one affine displacement in `X_1`. Therefore a near-span/small-cross-coefficient proof cannot rely on uniform output-law continuity in the matrix coefficients unless it also introduces a forbidden support/moment parameter.

This does **not** refute QFORM: both output laws may still have universally bounded densities. It refutes only the perturbative proof mechanism. The correct localization strategy must quotient the large fragment-center contribution as an affine translation or aggregate it before taking a reciprocal/singularity estimate.

The construction is already in the assigned partner's finite-fragment extreme class. Hence exact finite-fragment localization does not make coefficient perturbation uniformly continuous; it merely shows that no more general supports are needed to witness the failure.

## 7. Consequences for the live heavy-star / near-span debt

The two results above sharply separate a viable mechanism from an invalid one.

1. **Viable:** if the remaining one-dimensional leakage enters through a logarithmic pair singularity and the moving critical value has a genuine density cap, Theorem 4.1 pays it exactly. A product-linear critical value is enough, and Corollary 5.1 allows the critical value itself to contain arbitrary reverse-conditioned bank leakage.
2. **Invalid:** if a near-span residual coefficient is merely numerically small, Proposition 6.1 shows that it cannot be discarded or treated as a uniformly small random perturbation. Distant finite fragments at reciprocal scale defeat that step.
3. **Localization status:** assigned partner r20 proves that `L^p`, `p>=1`, Fourier energies localize with zero loss to the same finite-fragment extreme law, while its positive-weight obstruction rules out buying the missing full-target step with a universal polynomially weighted Fourier moment. Therefore the remaining branch should use an unweighted/small-ball or logarithmic critical-value aggregate, not support truncation plus coefficient continuity.

The first unpaid B14 implication is now:

`QFORM-HEAVYSTAR-CRITICALVALUE-CAP-OR-SCALEFREE-TRACE-v1`.

For each surviving heavy-star/near-span branch under `s_3(A)>=1`, either:

- identify an original-coordinate logarithmic physical-pair envelope whose moving critical value has a dimension-free density cap (possibly via the reverse-conditioned bank theorem), then apply Theorem 4.1; or
- prove a scale-free joint trace/positive-copy estimate that keeps the small leakage coefficient inside the exact product geometry.

A proof may not replace the second alternative by “the coefficient tends to zero,” because Proposition 6.1 gives a target-valid finite-fragment obstruction to that reasoning.

## 8. Scope and status

- Full QFORM: `OPEN`.
- New proved theorem: `QFORM-LOG-LEAKAGE-BATHTUB-v1`.
- New proved supporting theorem: `QFORM-PAIRLOG-RANK1-LEAKAGE-v1`, conditional only on the source-pinned established pair envelope and a true critical-value density cap.
- New proved composite branch: `QFORM-PAIRLOG-OVER-REVERSEBANK-v1` using the fresh B05 theorem.
- New rigorous target-valid mechanism counterexample: `QFORM-NO-UNIFORM-COEFFICIENT-PERTURBATION-CONTINUITY-v1`.
- Arbitrary shifts: controlled uniformly in all positive results.
- Distant fragments/unbounded supports: no parameter appears; the counterexample shows why they must not be suppressed by perturbative reasoning.
- Moments: none used.
- Continuity of the full-target output density: not proved.
- Native brain retrieval/receiver use: not observed; execution remains `WITHOUT_VERIFIED_BRAIN`.
