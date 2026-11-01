# PROB10-10 idea checkpoint — six-step local-SAW entropy compiler

Runtime request: GPT-6 maximum. Authenticated scheduler model/effort metadata is not exposed here; report runtime as UNVERIFIED unless independently supplied. Do not claim GPT-6 from prompt text.

Frozen model: nearest-neighbor undirected FPP on Z^2 with iid Exp(1) physical edge weights. Parent source: Auffinger–Damron–Hanson Question 4, specialized to Exp(1). Full source status remains OPEN.

## New mathematical idea before code

The newest P04 companion theorem has moved the dependence-safe axis upper bound to

mu(e1) <= a6 = 0.6082984009464644...

and, with the canonical four-window local-self-avoidance compiler, enlarged the reflected strict-triangle cone to |y| >= 1.716 x. The canonical owner report's next suggested path was to increase local memory analytically rather than return to the retired R08 local-detour route.

This run attacks precisely that entropy bottleneck. Replace the 4-local-SAW shift by the 6-local-SAW shift: states are six-step nearest-neighbor words whose seven visited vertices are all distinct; transitions shift by one direction and retain six-step self-avoidance. Every global self-avoiding walk lies in this finite-state shift, so an exact Collatz certificate for a tilted transfer matrix yields a rigorous endpoint-count upper bound with no independence assumption on geodesics.

Candidate rational parameters chosen from a separate exploratory calculation, to be accepted only if an exact checker verifies every inequality:

A = 1939/1000,
B = 2795/1000,
r = 623/125 = 4.984,
nu = 997/200 = 4.985,
s = nu-1 = 797/200,
q = r/nu = 4984/4985,
c = 6083/10000 = 0.6083,
rho0 = 857/500 = 1.714.

Target certificate:

1. exact six-local state/transition enumeration;
2. a positive rational Collatz vector z with Mz <= r z componentwise;
3. startup control for path lengths 1,...,5;
4. exact proof beta(rho0)<9997/10000 for
   beta(rho)=A^{-1} B^{-rho} exp(sc) q^{1+rho};
5. exact positivity 2(c-a6)>0;
6. explicit finite residual error after combining the oblique lower tail with P04's carry-lane axis correction.

If all six pass, the intended theorem is

mu(x,y)+mu(x,-y)-mu(2x,0) >= 2(c-a6)x > 0

for x>0 and |y| >= (857/500)x, plus D4 images. This would move the currently certified cone boundary 429/250=1.716 -> 857/500=1.714. It remains PARTIAL and does not move the canonical axis/diagonal c_*.

## Three materially different attacks considered

A. Six-local-SAW transfer (primary). This changes the oblique entropy class while preserving a direct global-SAW inclusion. It is nonduplicating relative to P04, which owns the carry-lane axis policy, and P20, which owns the Busemann route.

B. Busemann support-vector/policy disagreement. The latest P20 report gives qualitative policy separation but still lacks a quantitative disagreement-density/bypass estimate. Without that paid density, no strict-triangle constant in the central sector follows. Do not promote this route in this run.

C. Planar cutset/barrier dualization. A deterministic dual barrier can lower-bound every path only if one controls the minimum total weight over a family of crossing cutsets. For Exp(1), exponentially many candidate barriers and shared edges reintroduce an entropy/dependence problem; no source-valid positive defect emerged without a new cutset large-deviation theorem. This route is recorded as an obstruction, not a claim.

## Negation test planned

The primary claim will be attacked at its finite core: exact enumeration must reject any candidate transition violating six-step local self-avoidance, and every component of Mz<=rz must be checked in Fraction arithmetic. The general inclusion of global SAWs in the six-local shift will be proved on the page; finite enumeration is only a certificate for the transfer matrix, not a substitute for that proof.
