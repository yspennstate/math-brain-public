SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-22T20:49:25Z.
attacking: translation-uniform square lifting of finite-Lp bilinear residuals and a sign-unified original-coordinate two-pivot endpoint.

# account01/B09 r17 — finite-Lp square lift and sign-unified physical-pair endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B09-20260922T204925Z-r17`  
Fresh control at start: `yspennstate/math-research-brain@db500d7c08947ef7050810af75725b0c2bfdcdee`; refreshed before publication at `5f5287423294b49cee78425e4a7cc98f4677f49d`; OWNER CONTROL revision `2026-09-22.15`.  
Outcome: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREMS / FULL TARGET OPEN**.  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The full universal quadratic-form density conjecture is not proved here. This run establishes two exact analytic payment mechanisms and uses the designated partner's completed results in quantitative inequalities. All conditioning below is on original-coordinate sigma-fields; no independence after a spectral rotation is asserted.

## 1. Dependency closure and live corrections

The newest completed designated-partner result consumed is account02/B09 r8:

`yspennstate/math-open-problems@cd083758331a386d7fccb353aea19e702ad0cdad:proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T201108Z-account02-B09-QFORM-r8/REPORT.md`.

It proves `QFORM-THREE-SCALAR-CURVED-COMPRESSION-v1`: for three independent cap-one scalars and a symmetric `3x3` quadratic matrix `H` with `sigma_min(H)>=s`, arbitrary affine perturbations satisfy

`||p||_infinity <=128*2^(1/4)/s`.

Its product-preserving three-bank corollary gives, for three disjoint original-coordinate banks whose active dependence factors through three scalar projections and whose normalized aggregate compression has `sigma_min(G)>=tau`,

`||p||_infinity <=256*2^(1/4)/tau`.

The same report gives the exact falsifier `(U+V+W)^2`, showing that three cross strengths alone cannot absorb arbitrary scalar self-curvature without a spectral gap.

The earlier designated-partner account02/B09 r2 result is source-pinned at

`yspennstate/math-open-problems@a47c679eb9f7788b5c3c2a900ce516ec11de8d9b:proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T124417Z-account02-B09-QFORM-r2/REPORT.md`.

For an original-coordinate split with rank-two cross block and nonzero singular-value product `Delta`, retaining arbitrary quadratic-affine terms on both sides,

`||p_R||_3 <=6^(2/3) Delta^(-1/3)`.                                    (1.1)

The arbitrary-rank indefinite physical-pair theorem used in Section 4 is

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

For `s_3(A)>=s>0` and an invertible indefinite ORIGINAL-coordinate principal pair `B`, with `D=|det B|` and `kappa=sigma_min(B)`, it proves

`||p_Q||_infinity <=3*400^(1/3)*(D^2*kappa*s)^(-1/6)`.                  (1.2)

Live corrections enforced in this derivation include: no law-uniform pointwise quadratic Fresnel decay; no independence after spectral rotation; no dimension-free naive fiber supremum; no universal single Schur rank-two extraction; no one-heavy-row/same-square absorption; the arbitrary-joint coarea lemma and positive conditional projection-density moment are false; the worst conditional spectral density cap is false. None of those interfaces is used below.

## 2. A finite-Lp to half-Riesz conversion

For a real random variable `R` with density `p_R`, define

`H_(1/2)(R)=sup_t E |R-t|^(-1/2)`.

### Lemma 2.1 — `QFORM-LP-HALFRIESZ-CONVERSION-v1`

Let `2<p<infinity` and `M=||p_R||_p<infinity`. Then

`H_(1/2)(R) <= C_p M^(p/(2(p-1)))`,                                  (2.1)

where

`C_p =4*((p-1)/(p-2))^(3/2)*((p-2)/p)^(p/(2(p-1)))`.                 (2.2)

For `p=3`,

`C_3=8*sqrt(2)/3^(3/4)`.                                             (2.3)

If instead `||p_R||_infinity<=M`, the sharper rearrangement bound is

`H_(1/2)(R) <=2*sqrt(2M)`.                                           (2.4)

#### Proof

Fix `t` and a radius `r>0`; put `q=p/(p-1)<2`. Split the singular integral at `r`. Holder on the near part gives

`int_(|u|<=r) |u|^(-1/2) p_R(t+u) du`
` <= M * [int_(|u|<=r)|u|^(-q/2)du]^(1/q)`
` = M * [4(p-1)/(p-2)]^((p-1)/p) * r^((p-2)/(2p)).`                  (2.5)

The far part is bounded only by total mass:

`int_(|u|>r)|u|^(-1/2)p_R(t+u)du <=r^(-1/2)`.                         (2.6)

Optimizing the sum in `r` gives (2.1)-(2.2). The optimizer can be written explicitly as

`r_*=[p/((p-2) A_p M)]^(p/(p-1))`,
`A_p=[4(p-1)/(p-2)]^((p-1)/p)`.

For `p=3` this reduces to (2.3).

For (2.4), among probability densities bounded by `M`, the integral against the symmetric decreasing kernel `|u|^(-1/2)` is maximized by density `M` on the centered interval of length `1/M`. Hence

`H_(1/2)(R) <= M int_(-1/(2M))^(1/(2M)) |u|^(-1/2)du=2sqrt(2M)`. QED.

The crucial point is that (2.1) uses only the **marginal** density norm of `R`; it does not take a worst conditional density over hidden variables.

## 3. Translation-uniform scalar-square lifting

### Theorem 3.1 — `QFORM-LP-SQUARE-LIFT-v1`

Let `X` have a density bounded by one and be independent of a random element `Y`. Let `a!=0`, and let `m(Y)` and `R(Y)` be arbitrary measurable functions. Assume the law of `R` has density in `L^p` for some `p>2`. Set

`Q=a(X+m(Y))^2+R(Y)`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity`
` <= |a|^(-1/2) H_(1/2)(R)`
` <= C_p |a|^(-1/2) ||p_R||_p^(p/(2(p-1))).`                         (3.1)

If `||p_R||_infinity<=M`,

`||p_Q||_infinity <=2sqrt(2M/|a|)`.                                  (3.2)

Consequently every interval `I` satisfies the direct linear estimate

`P(Q in I)<=||p_Q||_infinity |I|`.                                   (3.3)

No independence between `m(Y)` and `R(Y)` is required.

#### Proof

Condition on `Y=y`. A change of variables at the two square roots gives the universal conditional density envelope

`p_(a(X+m(y))^2 |Y=y)(u) <= |a|^(-1/2)|u|^(-1/2)`                     (3.4)

for the appropriate sign of `u` (and zero on the opposite sign). Therefore, for almost every `t`,

`p_Q(t) <= |a|^(-1/2) E |t-R(Y)|^(-1/2)`.

Take the supremum over `t` and apply Lemma 2.1. Tonelli justifies the conditional density mixture. QED.

This is a dependence-safe square lift: the random center `m(Y)` can contain every residual coordinate and can be perfectly correlated with `R(Y)`.

## 4. Designated partner applied to actual inequalities

### 4.1 Rank-two cross residual + arbitrary both-side curvature

Suppose after completing one genuine original-coordinate scalar pivot, the residual has a rank-two cross block between two disjoint original-coordinate banks with singular-product `Delta`, while both residual self blocks are arbitrary. Apply the designated partner inequality (1.1) with `p=3` in Theorem 3.1. Since

`(6^(2/3) Delta^(-1/3))^(3/4)=sqrt(6) Delta^(-1/4)`,

we obtain

`boxed: ||p_Q||_infinity <=16*3^(-1/4) |a|^(-1/2) Delta^(-1/4)`       (4.1)

with numerical coefficient `12.157371...`.

The partner's specialized dependent-square lemma gives a better constant `4sqrt(6)` in its exact Schur setting. Equation (4.1) is not advertised as a constant improvement; its value is that the `L^p -> H_(1/2) -> square` interface is modular and remains valid whenever only a finite-`p` residual certificate survives an earlier aggregation step.

### 4.2 Latest partner r8: a four-bank nested gapped-compression theorem

Now take one original scalar coordinate `X0`, three disjoint original-coordinate banks `I,J,K`, and an outside bank `W`. Condition on `W`. Complete the `X0` square, obtaining

`Q=a(X0+m(X_I,X_J,X_K,W))^2+R(X_I,X_J,X_K;W)+c(W)`,                  (4.2)

where `a!=0`. Suppose that, uniformly in the conditioning, the entire active quadratic dependence of `R` on `I,J,K` factors through three scalar projections as in account02/B09 r8, and the normalized aggregate `3x3` compression `G` satisfies

`sigma_min(G)>=tau>0`.                                                (4.3)

The designated partner theorem gives uniformly

`||p_(R|W)||_infinity <=256*2^(1/4)/tau`.                            (4.4)

Apply (3.2) conditionally on `W` and average. This gives the new nested endpoint

`boxed: ||p_Q||_infinity <=2^(45/8) (|a| tau)^(-1/2)`
`                              <49.351 (|a| tau)^(-1/2).`             (4.5)

Hence

`P(Q in I) <=2^(45/8)(|a|tau)^(-1/2)|I|`.                            (4.6)

The outside coordinates, outside quadratic terms and the square center are arbitrary. The only structural restriction is exactly the partner's three-bank scalar-compression hypothesis; arbitrary within-bank curvature orthogonal to the three active projections is **not** silently absorbed.

For three literal residual physical coordinates with `sigma_min(H)>=s`, the partner's scalar bound `128*2^(1/4)/s` yields the sharper nested physical endpoint

`boxed: ||p_Q||_infinity <=2^(41/8)(|a|s)^(-1/2)`
`                              <34.897 (|a|s)^(-1/2).`                (4.7)

This is a genuine `O(|I|)` four-coordinate/nested-bank payment and does not use a conditional spectral density supremum.

## 5. A sign-unified original-coordinate physical-pair endpoint

The full-matrix theorem (1.2) covers indefinite physical pairs. The complementary definite case has a simpler direct proof that does not require the three-eigenvalue hypothesis.

### Lemma 5.1 — `QFORM-DEFINITE-PHYSICAL-PAIR-v1`

Let `B=A[{i,j},{i,j}]` be a definite invertible ORIGINAL-coordinate principal pair and put `D=|det B|`. For independent cap-one inputs, arbitrary remaining coefficients/couplings, and arbitrary affine terms,

`boxed: ||p_Q||_infinity <= pi/sqrt(D).`                              (5.1)

Thus `P(Q in I)<=pi D^(-1/2)|I|`.

#### Proof

Condition on every original coordinate except `X_i,X_j`. The conditional polynomial is

`x^T B x+ell^T x+c`.

Complete the square. Translation preserves the joint density upper bound `rho<=1` of the two selected independent coordinates. If `B` is positive definite, set `v=B^(1/2)u`. Lebesgue measure under `u -> u^T B u` has density

`(det B)^(-1/2) int_(R^2) delta(y-|v|^2)dv = pi/sqrt(det B)`

for `y>0`. Since `rho<=1`, the conditional pushforward density is bounded by the same constant. Negative definite `B` is handled by reflection. Averaging over the conditioned coordinates preserves the bound. QED.

### Corollary 5.2 — `QFORM-SIGN-UNIFIED-PHYSICAL-PAIR-v1`

Under `s_3(A)>=s>0`, every invertible ORIGINAL-coordinate principal pair `B` is paid as follows:

- if `B` is definite,
  `||p_Q||_infinity <=pi D^(-1/2)`;
- if `B` is indefinite,
  `||p_Q||_infinity <=3*400^(1/3)(D^2 kappa s)^(-1/6)`,
  by the source-pinned full-matrix pair theorem.

In particular, if `sigma_min(B)>=eta`, then `D>=eta^2` and

`||p_Q||_infinity <= max{pi/eta, 3*400^(1/3) eta^(-5/6)s^(-1/6)}`.   (5.2)

At the target scale `s=1`, a physical pair with `sigma_min(B)>=1/4` is therefore uniformly paid with

`||p_Q||_infinity <70.18`.                                           (5.3)

This removes the pair-sign split from the structural reduction: a genuinely well-conditioned physical pair of **either** signature is sufficient. The still-hard geometry must therefore avoid all such pairs while also avoiding the already-paid ridge, grouped-bank, hollow, cross and square branches.

## 6. Compact conditional end-to-end route after this run

A full proof would follow if one proves the following product-preserving structural statement at a universal scale `c0>0`:

> Every symmetric `A` with `s_3(A)>=1` has, after conditioning only on disjoint original-coordinate banks, at least one of: (i) an original physical pair with `sigma_min>=c0`; (ii) a paid ridge/diffuse certificate; (iii) a scalar pivot whose residual has the partner's gapped three-bank scalar compression at scale `c0`; (iv) one of the already proved hollow/two-cross/disjoint-square/grouped-hyperbolic endpoints.

Cases (i) and (iii) are now paid by Corollary 5.2 and (4.5), respectively. Existing source-pinned results pay the listed remaining certificates.

The **first essential unpaid implication** is therefore sharpened to

`QFORM-NEAR-RANKONE-PAIR-OR-GENUINE-BANK-CURVATURE-v1`:

when every useful original-coordinate `2x2` principal pair is quantitatively near singular and every usable scalar pivot avoids a gapped three-bank scalar compression/ridge/cross/hollow endpoint, extract and pay the genuinely orthogonal within-bank curvature without taking a worst conditional density supremum. The singleton-plus-two-banks and same-square examples remain mandatory regressions: any valid reduction must aggregate whole coordinate banks before reciprocal tiny-minor payment.

This is still a structural gap, not a proof of the full conjecture.

## 7. Regularity and provenance

The new arguments establish **essentially bounded densities** and direct `O(|I|)` interval estimates in their stated scopes. Continuity is not established by the pair or finite-`p` square-lift endpoints. The unrestricted conjecture and the full-target continuity conclusion remain OPEN.

No Gaussian, moment, log-concavity, compact-support, connected-support, post-rotation independence, Monte Carlo extremality, or pointwise Fresnel-decay assumption is used.

Changed-file privacy review: this report contains only mathematical statements, public theorem-style constants, private-repository source pins and nonsecret logical run identifiers; no credentials, scheduler IDs, machine paths, personal/private unrelated data, email, Drive or benchmark material. No public release is made.
