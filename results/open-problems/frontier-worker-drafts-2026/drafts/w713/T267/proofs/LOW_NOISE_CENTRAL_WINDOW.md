# Joint low-noise central-window bifurcation

T267 / Target 2 / C012 / proof draft (unaudited); novelty unestablished.
This is a local, rescaled noise-onset result in C010's restricted model.
It is not an exact global two-critical-noise-level theorem.

## 1. Precise scaling and result

Use C010's four-point stratified design, centered unit-norm ReLU teacher,
paired nonzero initialization with fixed nu in (0,1], both-layer GD with
step 1/2, and label-noise-averaged clean risk Q. Let alpha=alpha_e and
let b_h denote C009's full-kernel rates. Set

eta_e=(b2+b12)/b1 ~ e,
rho_e=kappa sqrt(eta_e), kappa>0 fixed,
sigma_e=2alpha sqrt(rho_e),
t0_e=log(1/sqrt(eta_e)).

Here sigma_e is the amplitude of independent symmetric label noise.
It is asymptotic to sqrt(kappa) e^(9/4). The network step size remains
1/2; eta_e in this proof is a spectral ratio, not that step size.

Let F_e(z) be the continuously interpolated frozen risk divided by
alpha^2. Define its central-time version
G_e(s)=F_e((t0_e+s)/b1). Then, uniformly on compact real s intervals,

G_e'(s)/(2 eta_e) -> H_kappa(s)
       =kappa exp(-s)-exp(-2s)-1,
G_e''(s)/(2 eta_e) -> H_kappa'(s)
       =-kappa exp(-s)+2exp(-2s).

Equivalently, the normalized value differences converge locally uniformly:

[G_e(s)-G_e(0)]/(2 eta_e) -> V_kappa(s)-V_kappa(0),
V_kappa(s)=-kappa exp(-s)+(1/2)exp(-2s)-s.

If kappa>2, define z_+=(kappa+sqrt(kappa^2-4))/2 and
z_-=(kappa-sqrt(kappa^2-4))/2. The frozen curve has a central strict local
minimum at scaled time tending to s_min=-log z_+, and a subsequent strict
local maximum at scaled time tending to s_max=-log z_-.
In small fixed neighborhoods of those two points there is exactly one
frozen stationary point of the indicated type for sufficiently small e.
The actual nonlinear discrete-GD risk has strict descent-rise-descent
witnesses near these points, with probability tending to one in the
iterated even-width-then-feature-scale limit. Its interval minimizers and
maximizers on these separate neighborhoods have the same scaled limits.
Its resulting central local peak obeys

b1 k_peak-t0_e -> s_max,
k_peak ~ (2pi/nu^2) e^(-1) log(1/e),

in that iterated probabilistic sense. The first assertion refers to every
maximizer in a chosen sufficiently small neighborhood of s_max; it does
not assert that all actual extrema are unique.

For 0<kappa<2, the FROZEN interpolated risk is strictly decreasing on any
fixed compact central s window for sufficiently small e. No monotonicity
of actual finite-width risk is asserted. At kappa=2 the leading derivative
has a degenerate zero; this proof does not resolve its finite-e unfolding.
Thus 2 is a threshold for this limiting central-window shape, not a proved
global critical noise level or a global absence theorem.

## 2. Uniform derivative limit

The exact frozen curve is
F_e(z)=rho_e(1-exp(-b0 z))^2
      +sum_(h=1,2,12)[exp(-2b_h z)+rho_e(1-exp(-b_h z))^2].
Its nonconstant h derivative with respect to z is
2 b_h q_h [rho_e-(1+rho_e)q_h], q_h=exp(-b_h z).
At z=(t0_e+s)/b1, q1=sqrt(eta_e)exp(-s). Therefore its contribution to
G_e'(s)/(2eta_e) is exactly
kappa exp(-s)-(1+kappa sqrt(eta_e))exp(-2s).

For h=2,12, b_h/b1=O(eta_e) and
q_h=1+O(eta_e log(1/eta_e)), uniformly on compact s sets. Their combined
contribution to G_e'(s)/(2eta_e) tends to -1, since their b_h/b1 weights
sum to eta_e. Differentiating with respect to s makes their contribution
tend to zero: the extra b_h/b1 factor is O(eta_e).
The constant-mode term and its s derivatives tend to zero after division
by eta_e. Indeed b0/b1 is of order 1/e, t0_e is of order log(1/e), and
exp[-(b0/b1)(t0_e+s)] decays faster than every power of e on compact s
sets. These exact formulas prove both uniform derivative limits.
Integration from zero proves the uniform value-difference limit.

## 3. Limiting stationary points and risk witnesses

Writing z=exp(-s)>0, H_kappa=kappa z-z^2-1.
For kappa>2 its roots are z_+>1 and z_-<1 with product one.
At s_min=-log z_+, H_kappa'=z_+ sqrt(kappa^2-4)>0;
at s_max=-log z_-, H_kappa'=-z_- sqrt(kappa^2-4)<0.
Thus V has a strict minimum then a strict maximum. Compact uniform
convergence of H and H' gives a unique frozen critical point near each,
of the same type; the derivative is bounded away from zero outside small
root neighborhoods inside a fixed central compact window.

Choose delta>0 sufficiently small. The four scaled times
s_min-delta, s_min, s_max, s_max+delta are increasing and have strict
limiting value inequalities descent-rise-descent. Rounded integer times
floor((t0_e+s)/b1) have scaled grid error at most b1, which tends to zero.
The associated frozen risk differences therefore have strictly positive
margins of order alpha^2 eta_e. The same value convergence provides a
strict gap away from the unique minimum or maximum in each separate
small neighborhood.

For 0<kappa<2, completion of the square gives
H_kappa=-(z-kappa/2)^2+kappa^2/4-1<0 for every z>0.
Its maximum is strictly negative, so compact uniform derivative
convergence implies the stated frozen decrease on each fixed compact
s window. This does not control scaled times escaping all compacts.

## 4. Actual nonlinear GD and order of limits

For each fixed e, rho_e, alpha_e and all interval endpoints are fixed
numbers, and all involved integer times lie below T_e=ceil(e^(-5/2))
for sufficiently small e. Labels remain bounded. C010's independent-pair
finite-horizon comparison therefore controls every involved actual risk
uniformly through T_e as width grows, including all sixteen noise
patterns. Multiplication of the error by the fixed positive factor
1/(alpha_e^2 eta_e) preserves convergence to zero for this FIXED e.
It follows, first taking width to infinity then e to zero, that the
actual risk value differences converge to the same V differences and
inherit the strict four witnesses. The positive local value gaps transfer
the interval minimizers and maximizers to s_min and s_max. No derivative
comparison for the actual nonlinear network is needed or claimed.

Finally eta_e~e, b1~nu^2 e/(4pi), so t0_e~(1/2)log(1/e) and the displayed
peak time follows. This theorem concerns a different joint-noise regime
from C011's fixed-rho phase comparison; neither proof exchanges limits.

## 5. Exact concrete witness certificate, kappa=5/2

Here z_+=2, z_-=1/2. Use z values 3,2,1/2,1/4 in decreasing order,
so the corresponding s=-log z and integer times increase. The primitive
values are respectively

-3+log 3, -3+log 2, -9/8-log 2, -19/32-2log 2.

Their required margins are
log(3/2), 15/8-2log 2, log 2-17/32, all strictly positive.
For fully checkable bounds, log(3/2)>1/3 and
7/12<log 2<3/4 follow from integrals of 1/t: the lower bound splits
[1,2] into [1,3/2] and [3/2,2] and uses right-endpoint rectangles.
For the upper bound write t=1+x and use
1/(1+x)<=1-x/2 on [0,1], strict in the interior, since the difference
has numerator x(1-x)/2. The margins exceed 1/3,3/8,5/96 respectively.
This certifies a specific joint-noise witness choice by exact rational
bounds, not a floating-point estimate of a bifurcation.

## Remaining scope

The exact finite-e global onset, the degenerate kappa=2 case, interaction
with the initial constant-mode transient, iid sampling, fixed-positive
noise and all-time nonlinear dynamics remain open. These restrictions
matter: a central-window derivative result cannot imply that no other
double-descent pattern occurs elsewhere in time. Pairing and finite
support remain as in C010. Dependencies C009/C010 and this argument
await independent mathematical review; specialist novelty is unestablished.
