VERDICT: PARTIAL exact second nonlinear residual derivative and improved small-time positivity window

The general polynomial-versus-exponential MFLD risk-time question remains
unresolved. The previous initial residual derivative holds. The new
result extends the local analysis of the same one-neuron sine teacher,
Gaussian inputs, fixed standard Gaussian parameter prior, and Gaussian
initialization.

Write G_t for the residual correlation and D=-dot G_0 as in round 5.
PROOF.md proves
\[
 \ddot G_0(w)=E(w)+\lambda Z(w),\qquad
 E(w)=\mathbb E[D(V)K(V,w)+D'(V)\partial_vK(V,w)],\quad
 Z(w)=-2D''(w)-wD'(w).
\]
The nonlinear kernel variation vanishes initially by output-weight
parity. Temperature contributes at second order. Both new far-frequency
tails are positive, with exact asymptotics
\[
 E(w)\sim\frac5{4096\sqrt2}w^4e^{-(5w^2-2w+5)/16},\qquad
 Z(w)\sim\frac2{81\sqrt3}w^4e^{-(w^2-w+1)/3}.
\]
The proof includes a closed Gaussian formula for E.

For the same W2-continuous weak energy solutions with locally bounded
fourth moments as in round 5, a third-generator estimate gives
\[
 |G_t-g+tD-\tfrac12t^2(E+\lambda Z)|
 \leq C3(T)t^3\min(|w|,1),
\]
uniformly over constant 0<lambda<=1. No stronger moment assumption is
needed. C3(T) is finite but is not explicitly evaluated.

The exact quadratic tangent is globally positive for sufficiently small
t. Consequently the actual solution satisfies G_t(w)>=g(w)/4>0 on
\[
 0<w\leq L_3(t),\qquad
 L_3(t)^2=6\log(1/t)-1-2\log(4C3(T)),
\]
for sufficiently small t. This improves the previous asymptotic window
from every coefficient kappa<2 to every kappa<sqrt(6) multiplying
sqrt(log(1/t)). It does not assert a larger numerical interval at a
specified time, since the new remainder constant is not evaluated.

AUDIT.md independently recovers E's tail coefficient and exponent by
input-space Gaussian square completion, and Z's coefficient by applying
the input operator twice. A separate single-branch differentiation checks
the full polynomial coefficients in the Gaussian formula. The moment
bound, third-derivative operator order, and logarithmic window coefficient
are re-derived separately. No discrepancy was found.

What failed: the cubic remainder is still absolute. It does not determine
the sign of G_t outside the expanding finite interval at a fixed positive
time. Positive initial derivative tails do not justify exchanging time
and frequency limits. No whole-tail sign theorem, trajectory-dependent
restricted gap, annealing remainder, or risk-time bound is obtained.
Existence and uniqueness for the unbounded network remain outside the
claim; the solution class is explicit.

The first-five-minute literature check found no whole-problem solution.
LITERATURE.md records the opened primary sources and their scope. The
check does not establish absence of a solution or novelty.

Commands and output are recorded in LOG.md. Earlier reports, logs and
proofs were read using rg, cat, head and wc; no scripts were present.
Shell reads requested `OMP_NUM_THREADS=1 nice -n 15`, but the sandbox
reported `nice: setpriority: Operation not permitted`. No numerical
program, simulation or heavy computation ran under unverified priority.
The contribution is analytic, with no computation script or dataset.
All writes used apply_patch inside this folder. Earlier folders were
read only; no git, subagents, shared-state commands or external mutations.

Next worker: obtain a remainder adapted to the broader Gaussian E tail,
or another representation controlling the full frequency half-line at
positive time. Formula (24) and the exact nonlinear third-generator
identity (34) are useful starting points. Repeated absolute Taylor bounds
only enlarge finite windows and do not settle remote lobes. Any later
learning-time obstruction must also quantify their prediction mass.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, approximately 11:23 Asia/Tbilisi.
