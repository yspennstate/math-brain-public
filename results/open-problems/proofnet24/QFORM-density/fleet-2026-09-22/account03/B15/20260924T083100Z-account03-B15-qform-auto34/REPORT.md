SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-24T08:31:00Z.
attacking: translation-robust instability of near-rank operator perturbations, to delimit exactly what the B19 determinant-collapse funnel may infer before the universal height estimate is paid.

# account03/B15 — near-rank operator perturbation is not a law/height continuity mechanism

Programme: QFORM-DENSITY-3EIG-20260922.  
Assignment: absolute continuity and regularity.  
Status: NEW QUANTITATIVE REGULARITY OBSTRUCTION / PARTNER APPLIED / FULL QFORM OPEN.  
Execution: WITHOUT_VERIFIED_BRAIN.

## 1. Control and source boundary


The live corrections are retained: no law-uniform pointwise quadratic-phase decay, no arbitrary-joint 3D coarea height theorem, no post-rotation independence, no naive fiber-sup dimension-free bound, and no bounded-support/fragment-radius assumption.

This run strengthens, but does not replace, the earlier account02/B14 coefficient-perturbation barrier at `math-open-problems@84093fddd5e3d3c692449d49c8b01537b28eb8d8`: that source gave a fixed positive TV gap under small operator perturbations. The new theorem below gives TV tending to one **even after arbitrary output translation**, while simultaneously proving an order-one discontinuity of the canonical density height.

The current proof-assembly motivation is account03/B19 r52 at `math-open-problems@5ec1cc2bf208bc0249ea89d86fd7298b62ac324e`: determinant collapse makes its four-latent carrier operator-close to rank at most three, but that source correctly does not discard the small fourth latent coefficient or the retained physical residual/tail.

The designated partner actually applied below is account04/B15 r8, `math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`, Theorem 6.1: for any fixed rank-at-least-three target instance, a separately proved interval bound `P(Q in I)<=M|I|` upgrades to a canonical `C_0(R)` density with the identical height `M`.

## 2. Main theorem: translation-robust near-rank instability

### Theorem 2.1 — `QFORM-OPNORM-RANKCOLLAPSE-TV-HEIGHT-BARRIER-v1`

For every `0<delta<1` and `0<eta<1` there exist two real symmetric target-valid matrices `A_0,A_e`, with

`||A_e-A_0||_op < delta`,

and one common cap-one independent product input law such that, writing `mu_0,mu_e` for the two quadratic-output laws,

`boxed: inf_{c in R} d_TV(mu_0, tau_c mu_e) >= 1-eta.`

Moreover both laws have canonical densities in `C_0(R)`, and they can be chosen so that

`boxed: ||p_0||_infinity >= 4/3,    ||p_e||_infinity <= 4 eta/3.`

Consequently the output law is not uniformly continuous in the matrix operator norm, even modulo arbitrary deterministic output translations, and the canonical density-height functional is not uniformly continuous in the matrix variable over the owner target when the admissible product law is allowed to vary with the perturbation.

This is **not** a counterexample to the universal upper-bound conjecture: in the construction the small perturbation makes the output much flatter.

### Proof

Choose

`0<e<min(delta,1)`

and put

`A_0=diag(1,1,1,0),     A_e=diag(1,1,1,e).`

Both matrices have at least three eigenvalues of absolute value at least one, and

`||A_e-A_0||_op=e<delta`.

Let `X_1,X_2,X_3` be independent `Uniform[-1/2,1/2]`. Set

`S=X_1^2+X_2^2+X_3^2`.

Then `S` is supported on

`E=[0,3/4]`.

The completed diagonal two-same-sign argument gives, for every interval `I`,

`P(S in I)<=pi |I|`.

In particular `S` has a bounded density. Since its entire mass one is carried by an interval of length `3/4`,

`||p_0||_infinity >= 1/(3/4)=4/3`.                         (2.1)

Now choose

`L>=3/(4 eta),      R=L/(2e),`

and let the fourth independent coordinate be `X_4~Uniform[R,R+1]`, again with density exactly one. Define

`Y=e X_4^2`.

Because `R>0`, change of variables gives the exact density

`g(y)=1/(2 sqrt(e y))`

on `[eR^2,e(R+1)^2]` and zero elsewhere. Therefore

`||g||_infinity=1/(2eR)=1/L`.                              (2.2)

The two outputs are

`Q_0=S,      Q_e=S+Y`,

with `S` and `Y` independent. Hence for every interval `I`, conditioning on `S` and using (2.2),

`P(Q_e in I)<=|I|/L`.                                      (2.3)

Apply the completed account04/B15 same-constant regularity compiler to the **actual inequality (2.3)**. Since `rank(A_e)=4`, it gives the canonical representative

`p_e in C_0(R),       ||p_e||_infinity<=1/L<=4 eta/3`.      (2.4)

Applying the same partner theorem to the diagonal interval inequality for `A_0` gives a canonical `p_0 in C_0(R)` as well (with upper bound `pi`); (2.1) is independent of that upper bound.

For any deterministic translation `c`, the translated law `tau_c mu_e` still has density cap `1/L`. Therefore

`(tau_c mu_e)(E)<=|E|/L=(3/4)/L<=eta`,

whereas `mu_0(E)=1`. By the event characterization of total variation,

`d_TV(mu_0,tau_c mu_e)>=|mu_0(E)-(tau_c mu_e)(E)|>=1-eta`.

This is uniform in `c`, proving the theorem. QED.

## 3. Quantitative interpretation: tiny quadratic curvature creates a huge affine scale

Write `X_4=R+U`, with `U~Uniform[0,1]`. Then

`eX_4^2=eR^2 + (2eR)U + eU^2
       =eR^2 + L U + eU^2`.                                  (3.1)

After subtracting the irrelevant deterministic shift `eR^2`, an operator-size-`e` quadratic coefficient has generated an affine slope exactly `L`, which can be arbitrarily large independently of `e`.

For example, with `eta=10^-2`, choose `L=75`, `e=10^-6`, so `R=37,500,000`. Then

`||A_e-A_0||_op=10^-6`,
`inf_c d_TV(mu_0,tau_c mu_e)>=0.99`,
`||p_e||_infinity<=1/75=0.013333...`,
while `||p_0||_infinity>=4/3`.

Thus the obstruction survives removal of every deterministic output translation. What fails is the unbounded-support amplification of the perturbing curvature into a macroscopic random affine term.

## 4. Exact implication for the B19 determinant-collapse branch

The r52 statement

`dist_op(H_L,{rank<=3}) < 1.07e-4`

cannot, by itself, justify replacing the four-latent carrier by its rank-three truncation through weak/TV/uniform-density continuity that is uniform over all cap-one product sources. Theorem 2.1 shows that no such operator-only regularity principle exists even for diagonal target matrices.

This does **not** say the r52 small fourth latent direction is harmful. It says the proof must either retain it exactly, or absorb it through a receiver whose estimate is uniform in the conditioning-generated affine translations. The exact pair-log, affine half-Riesz, grouped-bank and Fresnel/Brascamp--Lieb receivers developed elsewhere have precisely this translation-uniform character; a bare `||tail||_op<<1` step does not.

## 5. Absolute continuity remains separate

For completeness, if `A!=0` and the joint input law is absolutely continuous, then `q(x)=x^T A x` has an absolutely continuous pushforward. Indeed the critical set `ker A` is a proper linear subspace and is Lebesgue-null. On `E_k={|grad q|>=1/k}`, coarea gives zero Lebesgue measure to `q^{-1}(N) intersect E_k` for every one-dimensional null set `N`; the union over `k`, plus `ker A`, proves that the full inverse image of `N` is null. This gives no useful universal `L^infinity` bound.

## 6. Status

- New: arbitrarily small operator perturbations can produce output laws arbitrarily close to TV distance one **modulo every output translation**, inside the exact owner target and under one common cap-one product law.
- New: the canonical `C_0` density height can change by at least `(4/3)(1-eta)` under the same arbitrarily small matrix perturbation.
- Partner account04/B15 applied at the actual interval inequality (2.3), yielding `C_0` with the same `1/L` height.
- Full universal QFORM height theorem: OPEN / not proved / not disproved.
- Product-preserving retained-tail endpoint in the B19 determinant-collapse funnel: still the first relevant global debt.
