SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B14, 2026-09-22T18:46:26Z.
attacking: translation-uniform indefinite-pair smoothing by a mass-weighted bounded-density Schur remainder; derive an explicit log compiler and test it on a full-rank target family.

# account01/B14 — pair-log / mass-linear Schur localization

Programme: `QFORM-DENSITY-3EIG-20260922`. Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING_LOCALIZATION_COMPILER`. Full QFORM remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

Control source used: `yspennstate/math-research-brain@00c2e0f7f944eb39a3ed29defa72695ed344db4f`, OWNER CONTROL revision `2026-09-22.11`, programme revision `2026-09-22.5`; immediately before publication main had advanced only by worker records and the correction-inbox blob remained `6335a8d51fc8081123635a8d0848738b615cb082`. No later stop was found.

## 1. Exact dependencies actually read and applied

1. `QFORM-PHYSICAL-PAIR-LOG-ENVELOPE-v1`, complete proof:
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   If `U,V` are independent cap-one coordinates and `B` is an invertible indefinite physical `2x2` quadratic block, write
   `D=|det B|`, `kappa=sigma_min(B)`. For every affine perturbation with critical value `t0` and every `r>0`, its density has the a.e. envelope
   
   `p_F(t) <= 2 sqrt(2)/r + D^(-1/2) log_+(2 r^2/(kappa |t-t0|))`.       (1)

2. Named partner account02/B14, run `20260922T181403Z-account02-B14-QFORM-r17`, complete report:
   `yspennstate/math-open-problems@aa249c164c1518faa5a9a001baa00e8de3d10346:proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T181403Z-account02-B14-QFORM-r17/REPORT.md`.
   Its mass-linear localization ledger says that if a scalar output measure is decomposed into positive submeasures of masses `w_alpha` and each normalized piece has density cap `C_alpha`, then the unnormalized caps are `D_alpha=w_alpha C_alpha`; in particular the aggregate ordinary density cap is at most `H=sum_alpha w_alpha C_alpha`. The same report proves the more general Riesz ledger. Here I use its ordinary cap consequence inside (1), before any normalization of fragments.

No arbitrary-joint coarea bound, no conditional projection-density positive moment, no scalar-Q_rest conditional supremum, no law-uniform one-dimensional oscillatory decay, no moment bound, and no bounded-support or bounded-fragment assumption is used.

## 2. New theorem: exact pair-log / density-cap compiler

### Theorem 2.1 (`QFORM-PAIR-LOG-DENSITYCAP-COMPILER-v1`)

Let `X=(U,V,Z)` have independent real coordinates, each with density at most one. Let the quadratic form, after grouping the two ORIGINAL coordinates `U,V`, be

`Q = x^T B x + 2 x^T E z + q_0(z) + affine terms`,                 (2)

where `x=(U,V)`, `B` is symmetric, invertible and indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)>0`.

Complete the physical pair, without rotating the input law:

`Q = (x+m(z))^T B (x+m(z)) + T(z)`,                              (3)

where `m(z)` is arbitrary and `T(Z)` is the Schur-completed scalar remainder. Suppose the law of `T` has density cap `H<infinity`. Then for every `r>0`,

`||p_Q||_infinity <= 2 sqrt(2)/r + D^(-1/2) Psi(4 H r^2/kappa)`,  (4)

where

`Psi(x)=x` for `0<=x<=1`, and `Psi(x)=1+log x` for `x>=1`.       (5)

Consequently, with `xi=8 H D/kappa`, the optimized bound is

`||p_Q||_infinity <= 6 H^(1/3) kappa^(-1/3) D^(-1/6)`           (6)

when `xi<=1`, while

`||p_Q||_infinity <= D^(-1/2) [3+log xi]`                       (7)

when `xi>=1`.

A simple all-regime consequence is

`||p_Q||_infinity <= D^(-1/2) [3+log_+(8 H D/kappa)]`.          (8)

All estimates are uniform over translations of every input coordinate, arbitrary support separation, disconnected or unbounded supports, arbitrary outside quadratic coefficients/couplings, and all laws satisfying only the original density caps.

### Proof

Condition on `Z=z`. The two original coordinates remain independent with density caps one; the shift `m(z)` in (3) can be arbitrarily large. Apply (1), whose critical value is now exactly `T(z)`. For every output point `t`,

`p_Q(t) <= 2 sqrt(2)/r + D^(-1/2) E log_+(L/|t-T|)`,             (9)

with `L=2r^2/kappa`.

Use the exact layer-cake identity

`log_+(L/|u|)=int_0^infinity 1_{|u|<L exp(-v)} dv`.              (10)

A density cap `H` implies

`P(|T-t|<rho) <= min(1,2 H rho)`.                               (11)

Hence Tonelli gives

`E log_+(L/|t-T|)`
` <= int_0^infinity min(1,2 H L exp(-v)) dv`
` = Psi(2 H L)=Psi(4 H r^2/kappa)`.                             (12)

This proves (4).

If `4Hr^2/kappa<=1`, the right side is

`2sqrt(2)/r + 4H r^2/(kappa sqrt(D))`.

Its critical point is

`r^3 = kappa sqrt(D)/(2sqrt(2)H)`.                              (13)

This point lies in the stated regime exactly when `8HD/kappa<=1`, and substitution gives (6).

If `4Hr^2/kappa>=1`, differentiate

`2sqrt(2)/r + D^(-1/2)[1+log(4Hr^2/kappa)]`.

The critical point is `r=sqrt(2D)`, it lies in this regime exactly when `8HD/kappa>=1`, and substitution gives (7). At the boundary both formulas equal `3/sqrt(D)`. Finally setting `r=sqrt(2D)` directly in (4), and using `Psi(x)<=1+log_+x`, yields (8). QED.

## 3. Actual application of the partner's mass-linear localization result

Suppose the Schur-remainder law is first localized into positive submeasures `mu_alpha` of masses `w_alpha`, and suppose the normalized pushforward of piece `alpha` under `T` has ordinary density cap `C_alpha`. Do NOT normalize the pieces and then take a supremum. Partner r17 gives the aggregate cap ledger

`H <= sum_alpha w_alpha C_alpha`.                                (14)

Substituting (14) into (4)-(8) gives, for example,

`||p_Q||_infinity`
` <= D^(-1/2)[3+log_+( (8D/kappa) sum_alpha w_alpha C_alpha )].` (15)

Thus arbitrary numbers of fragments, arbitrarily small fragment masses, distant translations and unbounded tails cost nothing beyond the mass-weighted remainder-density budget itself. This is an actual use of the partner theorem in the new inequality, not a citation-only dependency.

## 4. Definite Schur-pair corollary

### Corollary 4.1 (`QFORM-INDEFINITE-PAIR-PLUS-DEFINITE-SCHURPAIR-v1`)

In Theorem 2.1, suppose two further ORIGINAL coordinates `J={j,k}` have a definite principal block `C0` in the Schur complement

`S=A_(I^c,I^c)-A_(I^c,I) B^(-1) A_(I,I^c)`,                    (16)

and put `Delta=|det C0|>0`. Then

`H <= pi/sqrt(Delta)`,                                          (17)

and therefore

`||p_Q||_infinity`
` <= D^(-1/2)[2+Psi(8 pi D/(kappa sqrt(Delta)))]`               (18)

` <= D^(-1/2)[3+log_+(8 pi D/(kappa sqrt(Delta)))].`            (19)

If `8 pi D <= kappa sqrt(Delta)`, the sharper low-regime estimate is

`||p_Q||_infinity`
` <= 6 pi^(1/3) Delta^(-1/6) kappa^(-1/3) D^(-1/6).`           (20)

Proof of (17). Condition on every Schur variable except the two coordinates in `J`. Their quadratic block remains exactly `C0`; all other couplings become an arbitrary affine term. Completing the square in these two physical coordinates and applying the linear map `y=|C0|^(1/2)(x-x0)` sends an output interval of length `h` to a planar annulus of area at most `pi h`. The Jacobian is `Delta^(-1/2)`, while the two-coordinate joint density is at most one. Thus the conditional output density is at most `pi/sqrt(Delta)`, uniformly in the conditioning. Averaging proves (17), then Theorem 2.1 gives (18)-(20). QED.

The key point is compositional: the original matrix need not possess a definite physical pair at `J`; definiteness may appear only AFTER eliminating the indefinite physical pair `I` by a product-preserving conditional completion.

## 5. Boolean-free exact target family showing nontrivial new Schur credit

Let

`eps0=(8*pi)^(-1/3)=0.3413920316...`, and 0<eps<=eps0.

Consider the symmetric physical-coordinate matrix

`A_eps =`
`[[0, eps, eps^(-1/2), 0],`
` [eps, 0, 0, eps^(-1/2)],`
` [eps^(-1/2), 0, eps^(-2), eps^(-2)],`
` [0, eps^(-1/2), eps^(-2), eps^(-2)]].`                       (21)

Take `I={1,2}`. Then

`B=eps [[0,1],[1,0]],  D=eps^2,  kappa=eps`,                   (22)

and the cross block is `E=eps^(-1/2) I_2`. Since

`B^(-1)=eps^(-1)[[0,1],[1,0]]`,

while the original lower physical block is

`C=eps^(-2)(I+[[0,1],[1,0]])`,

its Schur complement is exactly

`S=C-E^T B^(-1)E=eps^(-2) I_2`.                               (23)

Thus `Delta=eps^(-4)` and the Schur-remainder density cap is

`H=pi eps^2`.                                                   (24)

Moreover

`8 H D/kappa = 8 pi eps^3 <=1`,                                (25)

so (6) yields the dimension-free bound

`||p_(X^T A_eps X)||_infinity <= 6 pi^(1/3) < 8.788`           (26)

for every independent cap-one input law, uniformly as `eps->0`.

This is not merely a diagonal/definite-pair example. Every physical `2x2` principal determinant of `A_eps` is nonpositive:

`det A_{12}=-eps^2`, `det A_{13}=-eps^(-1)`, `det A_{14}=0`,
`det A_{23}=0`, `det A_{24}=-eps^(-1)`, `det A_{34}=0`.         (27)

Hence there is NO definite physical `2x2` principal pair in this four-coordinate matrix. The definite curvature used in (26) appears only in the Schur complement (23).

The matrix is nevertheless genuinely in the target class. Simultaneously diagonalizing the `1<->2` and `3<->4` symmetries splits it into

`M_+=[[eps,eps^(-1/2)],[eps^(-1/2),2eps^(-2)]]`,
`M_-=[[-eps,eps^(-1/2)],[eps^(-1/2),0]].`                     (28)

`M_+` is positive definite and has a largest eigenvalue at least `2eps^(-2)>1`. The two eigenvalues of `M_-` are

`lambda_pm=(-eps +/- sqrt(eps^2+4/eps))/2`.                    (29)

The positive one is at least one whenever `eps^2+eps<=1`; the negative one then has magnitude strictly larger. Since `eps0<(sqrt(5)-1)/2`, (21) has at least three eigenvalues of absolute value at least one. It is full rank because `det A_eps=det(B)det(S)=-eps^(-2)`.

The same bound (26) survives arbitrary additional dimensions and arbitrary extra quadratic couplings as long as the displayed four-coordinate principal block is retained: conditioning the extra original coordinates only adds affine terms to these four coordinates, (23) is unchanged, and Cauchy interlacing preserves the three-large-eigenvalue property.

This family shows that the Schur localization credit is genuinely nonzero and can remain uniform even when direct definite-physical-pair extraction is unavailable. I do not claim that every other surviving QFORM theorem fails on this family; it is an explicit witness for the new mechanism, not a separation theorem.

## 6. What this does and does not settle

This theorem closes a concrete compositional branch:

`indefinite physical pair` + `mass-weighted bounded-density Schur remainder`
` ==> bounded full output density`,                                               (30)

with exact translation-uniform formulas (4)-(8). A definite Schur pair supplies one such remainder certificate even when no definite pair existed in the original matrix.

It does NOT show that every symmetric matrix with three eigenvalues `|lambda|>=1` contains a physical indefinite pair whose Schur remainder has a dimension-free weighted density-cap budget. The singleton-plus-two-banks and small-minor families remain mandatory structural obstructions. The full conjecture therefore remains OPEN.

First unpaid implication: prove an exhaustive product-preserving reduction from the bare spectral hypothesis to either an already-certified diffuse/ridge/full-matrix-pair branch or to a physical pair whose Schur remainder admits a dimension-free mass-weighted density-cap budget `H=sum w_alpha C_alpha`; alternatively produce a valid target-class product-law example where every such pair budget necessarily diverges. In the latter case the next mechanism must aggregate a coordinate bank before pair inversion.

No novelty claim is inferred from repository search. No independent end-to-end review is claimed for the new theorem in this run.
