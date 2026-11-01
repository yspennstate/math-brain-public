Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# PROB10-10 idea before code — extend the proved wide-cone strict triangle by optimizing the non-backtracking tilt

The canonical source target remains strict convexity of the iid `Exp(1)` undirected nearest-neighbor FPP limit shape on `Z^2`. The canonical axis/diagonal defect `Delta_12=2 mu(e1)-mu(1,1)` is still unproved positive. The previous canonical run has now had three source-unchanged iterations and isolated the asynchronous-frontier carry obstruction, so this run does **not** add another frontier checker.

A genuinely different neighboring theorem is now available in `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T03-46-21Z__wide-cone-strict-triangle.md`: it proves

- `mu(e1) <= a0`, where
  `a0 = 127596793342690034600361684870097 / 197703921604834678505472000000000 = 0.6453933351799015...`;
- `mu(x,y) >= (2/3)x` for `|y|>=2x`;
- hence a positive strict-triangle defect in that cone.

This is a source-level restricted-direction theorem, not full strict convexity. The present route asks whether the cone boundary can be pushed strictly inward by re-optimizing the *same rigorous counting inequality*, rather than resuming the old canonical slab mechanism.

## Exact proposed strengthening

Try to prove, for every real `x>=0` and `|y| >= (15/8)x`,

`mu(x,y) >= c x`, with `c=1291/2000=0.6455`.

Since `c>a0`, this would imply for every `x>0`, `|y| >= 15x/8`,

`mu(x,y)+mu(x,-y)-mu(2x,0) >= 2(c-a0)x >0`,

strictly extending the P04 cone from slope `2` down to slope `15/8=1.875`.

Use tilted non-backtracking path counting with

- `A=189/100`, `B=291/100` for the E/W and N/S tilts;
- a rational Collatz spectral bound `r=5083/1000`;
- Chernoff parameter `s=1021/250`;
- `q=r/(1+s)=5083/5084<1`.

For endpoint `n(a,b)`, `b/a>=15/8`, the union bound has asymptotic base

`beta(rho)=A^{-1} B^{-rho} exp(sc) q^{1+rho}`.

Because `B>1>q`, this decreases in `rho`, so it suffices to certify the boundary slope `rho=15/8`. Raising to the eighth power removes fractional exponents:

`beta(15/8)^8 = A^{-8} B^{-15} exp(8sc) q^{23}`.

The exact checker should prove this is `<1` without floating-point dependence, e.g. from the elementary rational upper bound

`exp(x) < (1-x/m)^{-m}` for `0<x<m`,

with `x=8sc` and an integer `m` chosen large enough.

## Three materially different attacks considered this run

1. **Tilted non-backtracking cone optimization (chosen):** exploit the new P04 axis block theorem and optimize its entropy/Chernoff companion. Preliminary algebra indicates slope `15/8` is certifiable with positive margin.
2. **Two-terminal Busemann/Jensen accumulation (not chosen):** the newest P20 report gives an exact two-terminal residual metric and a local Jensen modulus, but still lacks the controlled fresh-block factorization required to convert local curvature to a linear unrestricted-FPP defect. No honest source movement can be claimed from that route in this bounded run without paying that dependence error.
3. **Asynchronous frontier Bellman carry (not chosen):** the preceding canonical report proved that synchronized `k`-frontiers pay an exact `H_k/2` toll and identified relative arrival-label vectors as the needed state. This remains promising but would require a new infinite-state average-cost Bellman certificate. Continuing it immediately would violate the required post-stall mechanism change and is less likely to move the source metric in this run.

## Negation test to run

The critical finite statement is the strict inequality `beta(15/8)^8<1`. If it fails under exact rational upper bounds, this cone extension is not proved and must be reported as a failed route. If it passes, the remaining proof is deterministic: non-backtracking count + Chernoff + geometric series + time-constant convergence + the already proved exact ladder axis bound.
