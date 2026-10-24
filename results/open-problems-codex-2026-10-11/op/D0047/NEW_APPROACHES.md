# D0047 additional serious attempt — 2026-10-12

Two routes not executed in the previous attempt:

1. Quantitative late-first-hitting estimates. Combine the exact discounted-hitting representation with finite-horizon stopped-phase moment bounds and the total-drift estimate P(tau<infinity)<=s/(2pi). Split the discount expectation at a time growing with log(1/s). Target: a generator-only small-gap remainder strictly smaller than order s^2, excluding the exact exponential sigma-PV branch without using a determinantal formula. Then seek sharper exponents or a closed transform.

2. Adjoint or invariant-constraint propagation for the one-pole Lax selection. Define the first-order Lax residual of the physical carousel solution, derive a homogeneous evolution equation for that residual using compatibility, and ask whether its zero-drift data and bounds force it to vanish. Target: a selection theorem via an adjoint uniqueness argument. The moving pole Q(s)~1/s makes uniform endpoint control essential, so compact convergence alone will not justify it.

Route 1 is pursued first: it has a concrete probabilistic estimate and can supply precisely the branch datum missing from the previous attempt. Route 2 remains an unexecuted proposal; no selection theorem is inferred from formal compatibility.


Outcome of route 1: proved the generator-only inequality 0<=G_beta(s)-1+s/(2pi)<=((s/(2pi))^(p+1))/(p+1), p=min(2,(1+sqrt(1+2beta))/2)>1. The proof uses a stopped discounted power moment with epsilon regularization, improving on the proposed coarse time split. This excludes the exponential sigma-PV branch. Also proved unique formal nonlinear PV sector and conditional analytic-germ uniqueness with this branch datum. Exact symbolic and numerical checks passed; three finite algebraic statements passed Lean. Route 2 remains unexecuted. Main global physical/Lax selection is still open in this attempt; verdict PARTIAL.
