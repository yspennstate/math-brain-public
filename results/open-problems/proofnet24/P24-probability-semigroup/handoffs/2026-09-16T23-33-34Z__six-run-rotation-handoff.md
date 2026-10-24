Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum. GPT-6 / maximum was requested, but the exposed scheduler/runtime has no model-family selector or reasoning-effort selector, so I do not claim otherwise.
Problem/source: Antonio Agresti and Mark Veraar (2025), *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), article 123, Problem 3; canonical intake I0063=I0069. **NO MOVEMENT: frozen metric `r_*=3 -> r_*=3`; this is the sixth consecutive unchanged run and triggers the mandatory CLOSABLE retirement/handoff.**

# P24 six-run rotation handoff — Agresti–Veraar Problem 3

Track/root: `proofnet24/P24-probability-semigroup`  
Category: CLOSABLE OUTSIDE  
Source status: **PARTIAL**  
Frozen fixed-pair endpoint status: **PROVED at the P24 proof level, closure audits incomplete**  
Operational status after this handoff: **ATTACK RETIRED / ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED**

This file preserves the exact mathematical state needed to resume the source without re-deriving settled work. It does not declare the full source Problem 3 closed and does not fabricate a replacement problem when the current queue has no lawful unassigned READY/CLOSABLE successor.

## 1. Exact source and frozen conventions

The current journal version (NoDEA 32, article 123, published 1 September 2025) states Problem 3:

> Suppose `(A,B) in SMR^bullet_{p,0}` for some `p in [2,infinity)`. Does one have `(A,B) in SMR^bullet_{r,0}` for all `r in (2,infinity)` (or at least some large range for `r`)?

The source immediately records only a small interval `[2,2+epsilon)` in the self-adjoint variational setting.

Frozen P24 candidate and source scale:

- `X_0 = H^{-1}(T)`;
- `X_{1/2}=L^2(T)`;
- `X_1=H^1(T)`;
- `A=Lambda=I-partial_x^2`;
- `B=beta Lambda^{1/2}` driven by one real Brownian motion;
- user-frozen pair: `beta=1`.

Definition 3.7 scope retained throughout: arbitrary progressive drift input `f`, arbitrary progressive stochastic input `g`, arbitrary starting times and stopping times, and the source `L^p(Omega;L^p_t(X_1))` output norm. A restricted sufficient condition is never substituted for the source problem.

## 2. Frozen metric and exact endpoint theorem

For the commuting family `(Lambda,beta Lambda^{1/2})`, P24 proved

`r_*(beta)=1+2/beta^2`, with endpoint nonmembership.

For the exact frozen pair `beta=1`,

`r_*=3`, and `(A,B) notin SMR_{3,0}`.

Thus the metric history has saturated at the exact value `3`. The full outside Problem 3 remains only PARTIAL because it quantifies over arbitrary `(A,B)` and leaves the pair-dependent phrase “some large range” unresolved.

## 3. Positive side — corrected source-scale Bellman proof

The valid Bellman functional is

`Phi_p(x)=integral_0^infinity ||A e^{-sA}x||_{X_0}^p ds`,

not the earlier superseded half-order functional. On the actual source realization it gives

`D Phi_p(x)[-Ax] = -||Ax||_{X_0}^p`,

`D^2 Phi_p(x)[A^{1/2}x,A^{1/2}x] <= (p-1)||Ax||_{X_0}^p`,

and

`D^2 Phi_p(x)[g,g] <= [p(p-1)/2] ||Ax||_{X_0}^{p-2} ||g||_{X_{1/2}}^2`,

using the exact square-function identity

`integral_0^infinity ||A e^{-sA}g||_{X_0}^2 ds = (1/2)||A^{1/2}g||_{X_0}^2`.

After finite Fourier projection, stopped Itô, the positive-semidefinite Hessian cross-term estimate, Hölder, and projection limit, absorption is possible exactly when

`beta^2(p-1)<2`.

The explicit certified upper constant for the stochastic-input component is

`C_{p,beta}^2 = p(p-1) / [2 (sqrt(2)-|beta|sqrt(p-1))^2]`.

Remark 3.10/deterministic maximal regularity handles `f`; Theorem 3.13 gives the comparison bullet class and Proposition 3.18 transfers base SMR to the source bullet class.

The preceding incorrect half-order Bellman functional was one derivative short on `H^{-1}->H^1` and must not be resurrected.

## 4. Negative side — direct deterministic-g endpoint certificate

Let `Lambda phi_n=lambda_n phi_n` with `lambda_n -> infinity`. Use source-admissible deterministic stochastic forcing

`g_n(t)=h 1_[0,1/lambda_n](t) phi_n`, `f=0`, zero initial data.

With scaled time `s=lambda_n t` and `Z_s=sqrt(lambda_n)x_n(s/lambda_n)`, the modal equation becomes

`dZ_s=-Z_s ds+(beta Z_s+h 1_[0,1](s))dWtilde_s`.

After the seed interval, the exact p-moment exponent is

`gamma_{p,beta}=(p/2)[beta^2(p-1)-2]`.

At `p_c=1+2/beta^2`, the post-seed `p_c` moment is constant and nonzero, while the physical fixed-time interval corresponds to a scaled horizon of length `lambda_n T`; hence the output/input ratio diverges. Above `p_c` it diverges exponentially. This is a counterexample within the source hypotheses and conventions, not an outside-hypothesis failure.

For `beta=1`, `gamma_p=p(p-3)/2` and the endpoint is exactly `3`.

## 5. Quantifier consequence for the source

For every `2<=p<r<infinity`, choose `q=(p+r)/2` and `beta^2=2/(q-1)`. Then the same operator family has exact endpoint `q`, so it belongs to `SMR^bullet_{p,0}` but fails base SMR at `r`.

Therefore:

- the source’s universal “all r>2” alternative is false;
- qualitative membership at one p does not imply any pair-independent positive right-neighborhood;
- the remaining source-level possibility is necessarily pair-dependent/quantitative.

This does **not** settle the phrase “at least some large range” for an arbitrary fixed pair.

## 6. Sharp one-shell constant and the remaining quantitative obstruction

For the scalar/Hilbert-shell equation

`dZ=-Z ds+(beta Z+Y)dW`,

the exact uniform-horizon `L^p(Omega x dt;H)` input/output norm is

`R_*(p,beta)=1/[sqrt(2/(p-1))-beta]`,

for `2<=p<1+2/beta^2`, independent of Hilbert multiplicity. Sharpness is obtained by a seed followed by the neutral progressive feedback

`Y=alpha_* Z`, `alpha_*=sqrt(2/(p-1))-beta`.

For the full torus stochastic-input constant,

`R_*(p,beta) <= C^g_{p,beta}(T) <= sqrt(p/2) R_*(p,beta)`.

For `beta=1`, `(3-p)R_*(p,1)->4`, so the blow-up power is exactly one as `p ↑ 3`; the remaining multiplicative constant is not known.

Equal-eigenvalue multiplicity is settled and cannot enlarge `R_*`. The simplest unresolved finite quantitative object is therefore two unequal scales with common Brownian motion and off-diagonal/adapted control:

`dZ_1=-lambda_1 Z_1 dt+sqrt(lambda_1)(beta Z_1+Y_1)dW`,

`dZ_2=-lambda_2 Z_2 dt+sqrt(lambda_2)(beta Z_2+Y_2)dW`,

with `lambda_1 != lambda_2`.

The sharp global-constant question can be written as

`sup_{T>0,g!=0} ||u||_{Lp(Omega x (0,T);X_1)} / ||g||_{Lp(Omega x (0,T);X_{1/2})} ?= R_*(p,1)`.

This is **not needed to know r_*=3**; it is the clean remaining quantitative obstruction if anyone resumes this exact pair.

## 7. Failed routes that must remain failed

1. **Future stochastic propagator inside a forward Itô integral:** anticipative, hence illegal as an adapted representation.
2. **Scalarize all modes and glue afterwards:** incurs the sharp dimension loss `M^{1/2-1/p}` for `p>2`.
3. **Constant progressive feedback below endpoint as a counterexample:** the destabilizing feedback is charged at exactly the state scale and yields the finite sharp ratio `R_*`; it is an extremizer, not a refutation.
4. **Take p ↑ 3 in a uniform subcritical estimate:** impossible; the direct-g pulse shows actual endpoint failure.
5. **Translation/symmetry averaging of a bad feedback:** closed-loop growth is nonconvex under feedback averaging; a two-dimensional shell gives an exact counterexample to the averaging route.
6. **Use spectral multiplicity alone:** arbitrary Hilbert multiplicity at one eigenvalue has the same exact norm `R_*`; any enlargement must couple unequal scales.
7. **Use discrete stochastic maximal-regularity extrapolation as a solution:** the 2026 discrete theorem concerns stochastic-convolution/operator SMR and does not match the nonsmall state-multiplicative `(A,B)` source definition.

## 8. Sixth-run thinking record — no new claim

This retirement run intentionally makes no new theorem-sized claim.

### Move #3 — PROVE SOMETHING STRONGER

The strongest natural quantitative target is the exact global equality `C^g_{p,1}(T)=R_*(p,1)`. The prior source-scale Bellman argument stops at `sqrt(p/2)R_*`; its Hessian estimate does not preserve the scalar extremal geometry after different spectral scales are mixed. A proof would need a Bellman/function-space object whose quadratic form sees the shared Brownian direction before taking the spectral supremum and loses no factor in cross-scale coupling.

**Outcome:** precise stronger target retained; no proof and no metric movement.

### Move #7 — TAKE THE LIMIT

For the two-scale system set `rho=lambda_2/lambda_1` and examine `rho->infinity`. Rescaling to the fast clock makes the slow component nearly frozen over a fast excursion, but it remains correlated with the same Brownian driver and with an adapted controller. The naive “freeze slow mode and optimize fast mode” step is not justified uniformly because the slow state is random and carries the same filtration; conditioning does not turn the control problem into independent scalar copies.

**Outcome:** the large-scale-separation limit identifies the missing decoupling statement but does not close it.

### Move #26 — HUNT THE SPORADIC CASE

The smallest place a scalar extremizer could fail is two unequal modes with off-diagonal feedback. Equal modes, diagonal feedback and equivariant feedback are already settled. A sporadic two-scale witness would have to make the vector Itô Hessian exploit an angle between `Z` and `A^{1/2}Y` that cannot occur in one dimension while keeping the source input charge small. No such source-valid exact witness is currently known.

**Outcome:** exact minimal search object isolated; no fabricated finite counterexample.

## 9. Audit state

Distinct OTHER track P21 has audited the corrected source-scale positive proof:

`P21-AUDIT-P24-SOURCE-SCALE-BELLMAN-62 = PASS AT THE FROZEN TORUS / SOURCE-DEFINITION SCOPE`

in `proofnet24/P21-closure-mub-sos/runs/2026-09-16/2026-09-16T21-25-30Z__run-report.md`, creation commit `a9c9c88c7adcab3e8451be7eea3484af2325d6b5`.

P21 also checked the negative direct-g component. This is only one independent OTHER track. A repository search has not found a `P26-AUDIT-P24` complete audit. Therefore closure protocol is incomplete even for a paper-ready frozen-pair package.

P24’s directed audit duty to C27 has no fresh theorem to audit in this run: C27’s latest visible action is the mandatory handoff from Tóth to I0078 and its create-only successor claim under `proofnet24/C27-riesz-rigidity`; no new C27 successor theorem/report was recovered in the bounded current repository search. No redundant PASS is manufactured.

## 10. Current literature boundary

Dated current checks on 2026-09-16 UTC recovered:

- the current NoDEA version of Agresti–Veraar Problem 3, unchanged in the relevant wording;
- Bechtel–Veraar (2025), *An extrapolation result in the variational setting: improved regularity, compactness, and applications to quasilinear systems*, which gives some `p>2` under quantitative coercivity and self-adjointness, not an all-r theorem;
- Evangelopoulos-Ntemiris–Veraar (2026), *Discrete stochastic maximal regularity*, whose extrapolation statement is in the discrete/operator stochastic-convolution setting and does not match the nonsmall multiplicative pair in Problem 3;
- no bounded-search source-matching later theorem that removes the above distinction.

A negative literature search is not proof of novelty or worldwide openness.

## 11. Successor screen and mandatory retirement

The current queue’s previously certified READY/CLOSABLE replacements are no longer available:

- I0004 has since acquired an exclusive P21 claim;
- I0075 has since acquired an exclusive PROB20-17 claim.

The higher queue front is likewise unavailable or ineligible in current evidence: I0006 is HOLD_SOURCE; I0011 is claimed/retired by P16 pending lawful reassignment; I0028 is claimed by HARD10-01 and classified HARD; I0035 is claimed by C31; I0054 is claimed by R11; I0055 is literature-resolved in its corrected scope; I0070 is R10-owned; I0068 has a P19 claim and is itself six-run retired; I0066 is P15-owned; I0077 is owned; I0079/I0078 are HARD and owned; I0082 is R08-owned; I0087 and I0105/I0106 still fail complete CLOSABLE admission; I0095 is owned; I0098 is on claimed-resolution hold; I0113/I0110/I0112 are owned; I0111 is hard reserve.

I0003 (Bou-Rabee–Peres 2026, Section 7 Problem 3) is source-open and apparently unclaimed in the bounded search, but its broad classification question is not currently certified READY/CLOSABLE. Recent independent P16/P19/C31 rotation screens reached the same current conclusion: no lawful unassigned READY/CLOSABLE successor is presently evidenced.

Therefore P24 creates **no successor claim** rather than silently promoting a PENDING/HARD/metadata-incomplete row. The correct state is `ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED`. The next authorized action is a fresh coordinator/P26 admission or another current source/status/ownership screen that identifies a genuinely READY unassigned CLOSABLE target.

## 12. Claim ledger at handoff

### PROVED

- Fixed frozen pair `beta=1`: exact endpoint `r_*=3`, endpoint excluded.
- Commuting family: `r_*(beta)=1+2/beta^2`, endpoint excluded.
- Corrected source-scale Bellman positive estimate for every `2<=p<r_*(beta)`.
- Deterministic-g source-valid failure at and above `r_*(beta)`.
- No pair-independent positive right-extrapolation radius from qualitative SMR membership alone.
- Exact scalar/Hilbert-shell norm `R_*(p,beta)` and neutral-feedback extremizer.
- One-shell spectral multiplicity does not enlarge `R_*`.

### CONDITIONAL / RESTRICTED

- Any theorem based on additional quantitative coercivity, commutation or smallness data is only a sufficient restricted class unless it answers the source quantifiers.

### DISPROVED ROUTES

- anticipative future-kernel representation;
- dimension-free modewise scalarize-then-glue;
- endpoint uniformization from subcritical constants;
- symmetry averaging of feedback as a preservation principle.

### OPEN

- Full Agresti–Veraar Problem 3 pair-dependent “large range” interpretation for arbitrary `(A,B)`.
- Exact full frozen-pair stochastic-input constant between `R_*` and `sqrt(p/2)R_*`.
- Unequal-two-scale off-diagonal/adapted control problem.
- Second independent complete P24 audit (P26 or another distinct track).
- Lawful READY/CLOSABLE successor admission for this slot.

## 13. Resume instructions

If this source is later reassigned, do **not** re-prove `r_*=3`. Start from the corrected Bellman proof and direct-g endpoint certificate above. The highest-value mathematical resume point is either:

1. prove a quantitative pair-dependent extrapolation theorem whose radius is expressed in actual source data and compare it to the exact `beta` family; or
2. solve/refute the unequal-two-scale sharp-constant problem without scalarize-then-glue.

If a second independent complete audit arrives, that closes only the frozen-pair package, not the full source Problem 3.

No email/Gmail, Drive, public posting, paid compute, permission/access change, shared-ledger edit, peer-file edit, workflow execution or new schedule was used.

**END_OF_P24_SIX_RUN_ROTATION_HANDOFF_2026-09-16T23-33-34Z**
