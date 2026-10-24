SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T23:07:34Z.
attacking: two-square fractional-potential lift of a contaminated rank-one cross packet, then application to the partner finite-leak endpoint.

# account01/B01 — two-square lift of the subcritical rank-one packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T230734Z-account01-B01-qform-auto11`  
Role: Oscillatory replacement  
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction boundary

The full owner target remains open. All random coordinates below are ORIGINAL independent coordinates or disjoint original-coordinate banks. No spectral rotation is declared to preserve independence. No moment, support, Gaussian, log-concavity, connected-support, or diagonal-basis assumption is added.

The phase-aligned fragmented-support counterexample to any law-uniform scalar pointwise estimate `|E exp(itX^2)| <= C|t|^{-alpha}` remains valid and is not used around. The mechanism here is a composition of (i) the already proved subcritical fractional potential of a JOINT rank-one bilinear packet with arbitrary same-bank phases and (ii) exact square-density kernels in original scalar coordinates.

Fresh prepublication owner control was read from `yspennstate/math-research-brain/main` at head `37f68521a96c96fbfa924525e017538682fcb35c`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no B01 pause/stop. The live correction inbox was reread at blob `47b2ff15d8ca6acfe35d9fd3de3b6281a86439f3`.

## 2. Source-pinned premise: subcritical rank-one potential

The preceding B01 proof is

`yspennstate/math-open-problems@7eb915c055ec899017e7b3cd409a826eea7c7212`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T220810Z-account01-B01-qform-auto11/REPORT.md`.

For disjoint original product banks `I,J`, arbitrary same-bank measurable phases `F,G`, nonzero vectors `u,v`, and `sigma!=0`, put

`R=F(X_I)+G(X_J)+2 sigma (u^T X_I)(v^T X_J)`,
`kappa=|sigma| ||u||_2 ||v||_2`.

For every `0<beta<1/2`, that report proves

`H_beta(R):=sup_s E|R-s|^(-beta) <= K_beta kappa^(-beta)`,       (2.1)

where

`K_beta=(2pi)^beta/[Gamma(beta) cos(pi beta/2) beta(1-2beta)]`.  (2.2)

It also proves the critical endpoint `H_(1/2)` is false in this scope: with independent cap-one `Y,Z`,

`R=-Y^2-Z^2+2YZ=-(Y-Z)^2`

has `E|R|^(-1/2)=infinity`.

## 3. Exact square-potential composition

The missing observation is that ONE ADDITIONAL source-disjoint square upgrades every subcritical `H_beta` to a supercritical potential, which is then strong enough to feed the final square.

### Lemma 3.1 — `QFORM-SQUARE-FRACTIONAL-UPGRADE-v1`

Let `R` be any real random variable. Let `Z` be independent of the sigma-field generating `R` and a measurable shift `m`, with density bounded by `M`. Let `b!=0` and

`S=R+b(Z+m)^2`.

For `0<beta<1/2`, set `gamma=beta+1/2`. Then

`H_gamma(S) <= M |b|^(-1/2) J_beta H_beta(R)`,                 (3.1)

where

`J_beta = max{ B(1/2,beta),
               B(1/2,1/2-beta)+B(1/2-beta,beta) }`.           (3.2)

#### Proof

Condition on the variables generating `(R,m)`. Translation does not change the cap of `Z`. The conditional density of `b(Z+m)^2` obeys

`p(u | R,m) <= M |b|^(-1/2) |u|^(-1/2) 1_{bu>0}`.             (3.3)

For `d=s-R` and, by reflection, `b>0`, integrate the envelope. If `d<0`,

`int_0^infinity u^(-1/2)(|d|+u)^(-gamma) du
 = |d|^(-beta) B(1/2,beta)`.                                  (3.4)

If `d>0`, split at `u=d`:

`int_0^d u^(-1/2)(d-u)^(-gamma) du
 = d^(-beta) B(1/2,1/2-beta)`,                                (3.5)

`int_d^infinity u^(-1/2)(u-d)^(-gamma) du
 = d^(-beta) B(1/2-beta,beta)`.                               (3.6)

The exceptional set `d=0` is harmless whenever `H_beta(R)<infinity`, since then `R` has no atom at `s`. Average (3.4)-(3.6) over `R` and take the supremum in `s`. This proves (3.1). QED.

### Lemma 3.2 — supercritical-to-critical monotonicity

For every probability law and `gamma>1/2`,

`H_(1/2) <= H_gamma^(1/(2gamma))`.                              (3.7)

Indeed, for each center `s`, Lyapunov/Jensen applied to the nonnegative variable `|R-s|^(-gamma)` gives

`E|R-s|^(-1/2) <= (E|R-s|^(-gamma))^(1/(2gamma))`.

## 4. Main theorem — `QFORM-TWOSQUARE-RANK1-SUBCRITICAL-LIFT-v1`

Let `X_0,Z` and the two banks `X_I,X_J` be mutually independent original sources. Allow an additional outside source `W`, conditionally throughout. Assume scalar density caps

`||p_(X_0)||_infinity <= M_0`, `||p_Z||_infinity <= M_1`.

Let the rank-one packet be

`R=F(X_I,W)+G(X_J,W)+2 sigma (u^T X_I)(v^T X_J)`,
`kappa=|sigma| ||u|| ||v||>0`,

where the bound (2.1) is uniform in `W`. Let `m_1=m_1(X_I,X_J,W)` and allow the OUTER shift to reuse everything,

`m_0=m_0(Z,X_I,X_J,W)`.

For `a,b!=0`, define

`Q=a[X_0+m_0]^2 + b[Z+m_1]^2 + R`.                             (4.1)

Then for every `0<beta<1/2`,

`boxed:
 ||p_Q||_infinity
 <= M_0 |a|^(-1/2)
    [ M_1 J_beta K_beta |b|^(-1/2) kappa^(-beta) ]^(1/(1+2beta)).}`  (4.2)

This proves essential boundedness. Continuity is **not claimed** for arbitrary merely measurable input densities.

#### Proof

Apply Lemma 3.1 conditionally in `W` to the inner original scalar `Z`, then (2.1):

`H_(beta+1/2)( b[Z+m_1]^2+R )
 <= M_1 |b|^(-1/2) J_beta K_beta kappa^(-beta)`.               (4.3)

Lemma 3.2 converts (4.3) to an `H_(1/2)` bound with exponent `1/(1+2beta)`. Finally condition on every variable except the original scalar `X_0`. The conditional density of `a[X_0+m_0]^2` is bounded by

`M_0 |a|^(-1/2)|u|^(-1/2)`

on the appropriate half-line. Therefore

`p_Q(q) <= M_0 |a|^(-1/2)
           E|q-[b(Z+m_1)^2+R]|^(-1/2)`,                        (4.4)

and (4.2) follows. All completions are in literal original coordinates; the shifts may be arbitrarily coupled to the remaining variables. QED.

At `beta=1/4`,

`J_(1/4)=12.660413817789727...`,
`K_(1/4)=3.781277348735446...`,

so

`boxed:
 ||p_Q||_infinity
 <= 13.184316586399616
    M_0 M_1^(2/3)
    |a|^(-1/2)|b|^(-1/3) kappa^(-1/6).}`                       (4.5)

At `beta=1/5`, the slightly smaller clean constant is

`12.391312874357480`,

with exponents

`M_1^(5/7)|b|^(-5/14)kappa^(-1/7)`.                            (4.6)

The homogeneity is exact: under multiplication of the entire quadratic form by `lambda`, the powers of `a,b,kappa` in (4.2) sum to `-1`.

## 5. The formerly critical parabolic cancellation is repaired by a second square

The previous run's sharp obstruction was

`R=-(Y-Z)^2`.

It has infinite `H_(1/2)`, so one outer square cannot be justified through a universal critical-potential interface. Theorem 4.1 shows that adding one more source-disjoint square repairs this endpoint even if BOTH square shifts overlap the bad packet.

For example, for four independent cap-one original variables and `epsilon=1/2`,

`Q=(X+epsilon Y)^2+(W+epsilon Z)^2-(Y-Z)^2`.                   (5.1)

This is exactly (4.1) with `a=b=kappa=M_0=M_1=1`. Its physical matrix, in order `(X,W,Y,Z)`, has characteristic polynomial

`lambda(4lambda-5)(4lambda^2+3lambda-8)/16`,                   (5.2)

hence eigenvalues

`0, 5/4, (-3+sqrt(137))/8, (-3-sqrt(137))/8`.                  (5.3)

The three nonzero eigenvalues have absolute value strictly bigger than one. Thus (5.1) is an actual owner-target family, with nontrivial overlapping square shifts, and (4.5) gives for **every** admissible product input law

`boxed: ||p_Q||_infinity <= 13.1843165864.`                    (5.4)

The point is not the numerical constant; it is that the critical parabolic cancellation is cured by the exact third smoothing resource without any scalar pointwise Fresnel estimate.

## 6. Actual use of the newest completed account02/B01 theorem

The newest completed designated partner is

`yspennstate/math-open-problems@8a05b72743a9dc1ffa5afd22be6a7fa66d59b8ba`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T220140Z-account02-B01-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-RANK1-LATENT-TRANSVERSE-WEDGE-v1` states that an exact-rank-one cut in a diagonal-plus-rank-two Schur residual can be re-cut to rank two whenever its latent triple currency `Zeta_3` is positive. On its concrete exact-W2 target family, conditioning the defining pair leaves

`Q_cond=x_0^2+2xy+(w^T Y)^2`, `||w||=1`,                       (6.1)

and the partner constructs a literal re-cut with

`Delta=1/2`.

Applying its completed rank-two half-Riesz receiver gives the actual inequality

`boxed: ||p_Q||_infinity <=8(1/2)^(-1/4)
                         =8*2^(1/4)
                         =9.5136569200... .}`                  (6.2)

The present theorem supplies an independent direct payment of the same conditioned formula WITHOUT re-cutting the `Y` bank. The normalized projection `w^T Y` has density cap at most `sqrt(2)`, while `2xy` is a rank-one packet with `kappa=1`. Therefore (4.5) gives

`||p_Q||_infinity
 <=13.1843165864*(sqrt(2))^(2/3)
 =16.6111979957... .`                                         (6.3)

The partner estimate is sharper on this example; (6.3) is structurally complementary because it spends the third curvature as a square-potential upgrade rather than as a rank-two physical re-cut.

More importantly, the partner proves that when `rank U_J=2` but `Zeta_3=0`, its transverse latent vector is supported on at most two literal original coordinates. The new theorem therefore pays every such finite-leak subbranch in which one support coordinate `j` has a nonzero physical scalar pivot `b_j` and, after literal completion in `j`, the surviving exact rank-one cross has scale `kappa_j>0`:

`||p_Q||_infinity
 <=13.1843165864 |a|^(-1/2)|b_j|^(-1/3)kappa_j^(-1/6)`          (6.4)

for cap-one scalar coordinates. For instance `|a|,|b_j|>=1/64` and `kappa_j>=1/4` give `<531.559`.

This is a strict narrowing of the partner's finite-leak endpoint. It does not claim that every support-two state necessarily has such a quantitatively nondegenerate scalar completion.

## 7. Remaining implication

The first unpaid implication is now

`QFORM-W2ZERO-FINITELEAK-ZEROPIVOT-OR-CROSSLOSS-ROUTING-v1`.

Inside the partner's exact-rank-one, zero-`Zeta_3` endpoint, the branch with a target-scale localized scalar square and retained rank-one cross is paid by (4.2). What remains is concentrated on:

1. localized transverse support coordinates whose self-pivots are zero or quantitatively tiny;
2. scalar completion that annihilates the rank-one cross scale (`kappa_j` zero/tiny), requiring an exact Schur identity rather than perturbative deletion;
3. the genuine nonzero collar `0<s_2<1/256` rather than exact rank one.

These states should be routed to a physical hyperbolic pair, the partner rank-two re-cut, the aggregate-E2 receiver, or another exact zero-diagonal/grouped-square mechanism. Small coefficients cannot be discarded on unbounded inputs.

The full conjecture and the full continuity claim remain OPEN. No two independent end-to-end reviews exist for a full candidate.

## 8. Verification and provenance

The beta-integral constants and the exact characteristic polynomial in (5.2) were checked independently by a deterministic symbolic/numerical script saved beside this report. The script is a sanity check, not a proof review. The proof itself is the analytic calculation above.

No public release, scheduler mutation, notification change, email, paid API/model call, cross-account authentication, or installation work was performed.