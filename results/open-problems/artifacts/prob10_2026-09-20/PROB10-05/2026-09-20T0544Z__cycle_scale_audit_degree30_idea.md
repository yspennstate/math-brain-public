Runtime request: GPT-6 / maximum. Authenticated reasoning/model telemetry is unavailable here, so runtime is **UNVERIFIED**; I do not claim GPT-6 maximum.

# PROB10-05 idea before certification — audit the softened four-cycle scale, then salvage with a higher-degree quasimode

Frozen source model: centered standard fBM at `H=1/4`, `I(t)=int_0^t B_{1/4}(u)du`, continuous one-sided event `P{sup_{0<=t<=T} I(t)<=1}=T^{-theta_{2,1/4}+o(1)}`. Canonical owner remains `HARD7-05` under `operations/claims/MOLCHAN-2025-THETA2H.md`.

Current repository candidate before this run is `0.16798 < theta_{2,1/4} <= 1/4`, but its fourth-trace separation uses a softened four-cycle covariance that must be re-audited before any further endpoint sharpening.

## Attack A — audit the negation of the inherited fourth-trace cap

For a four-step AR loop, after normalizing the loop measure, the vertex **correlations** are

`a=(r+r^3)/(1+r^4)`, `b=2r^2/(1+r^4)`,

but the common vertex variance before standardization is

`G0=(1+r^4)/(1-r^4)>1`.

The hard-edge sign event is scale invariant, so replacing the loop vertices by unit-variance versions is harmless at `s=1`. The softened edge

`V_i=sqrt(s) S_i + sqrt(1-s) E_i`

is **not** scale invariant because the independent noise keeps variance one. Therefore any softened-cycle correlation computed from unit-variance loop vertices must include the `G0` factor in the signal variance/covariance before adding the noise. I will test whether the archived values

`rho_adj=168557580/170952323`, `rho_opp=167065920/170952323`

omit that factor. If so, I will certify the mismatch exactly and independently contradict the resulting trace cap using a finite Hermite compression, rather than merely asserting a derivation error.

## Attack B — salvage the lower-bound route without the suspect trace refinement

The earlier `2026-09-19T2148Z__softening_frontier_164700.md` bound uses only the pre-error hard-edge trace cap

`tr(K_{7/8,1}^4) < 553151/500000`

plus the on-page Gaussian-correlation monotonicity `tr(K_{r,s}^4)<=tr(K_{r,1}^4)`. That argument does not require a normalized softened-loop covariance. Keep this coarse but safe trace cap, and instead reduce the Temple residual by a genuinely new degree-30 Hermite--Galerkin quasimode at the same frozen comparator `r=7/8`, `s=24861/25000`.

Exploratory high-precision Galerkin work (coefficient selection only, not proof) gives approximately

`mu = 0.9120841320878648`, `eps^2 = 0.00012692860442193`,

versus the degree-22 residual about `0.00028549217`. If exact interval recomputation survives monomial cancellation, the coarse hard-edge trace cap should still allow a source-valid target near `theta=0.16994`, strictly stronger than both the last unaffected `0.1647` and the current `0.16798` candidate.

## Attack C — covariance/operator route instead of trace sharpening

A separate route is to prove an intrinsic contraction bound on the non-Perron spectrum (for example through a Doob transform/Poincare estimate for the positive kernel), which would remove dependence on high even traces. The immediate obstruction is that the killing factor couples adjacent AR states and the natural Doob-transformed invariant law is not explicit; a bare OU contraction only yields bounds at the scale `r`, weaker than the current fourth-trace separation. I therefore do not spend this run manufacturing a weak operator-norm certificate.

## Exact missing lemma to settle in this run

Either certify that the softened four-cycle trace cap is valid **with the original loop scale preserved**, or produce an exact contradiction to that cap and then re-prove a stronger exponent lower bound using only the last unaffected hard-edge trace input. No discrete sampling claim will be used in the reverse direction; the continuous-to-grid inclusion needed for a lower exponent bound remains exact.