# Co-scaled noise phases: double descent versus preference for late stopping

T267 / Target 2 / C011 / proof draft (unaudited); novelty unestablished.
This is an asymptotic phase comparison in C010's restricted model, not
an exact finite-scale two-critical-noise-level theorem.

## 1. Model and statement

Keep the four-point design, unit-norm centered-ReLU teacher, paired
nonzero initialization and both-layer GD of BOUNDED_RELU_PAIRED.md.
Write alpha=alpha_e and replace label noise +/-2alpha by
+/-2alpha sqrt(rho), for any fixed rho>0. Thus the noise standard deviation
is c_e sqrt(rho), which tends to zero. Each Walsh noise variance is
rho alpha^2. Average clean risk over the sixteen noise patterns as before.
All width limits are over even widths m=2N, before e decreases to zero.

Let b_h be the full-kernel rates of C009, q_h=exp(-b_h), and define

K_e=ceil(e^(-3/2)), T_e=ceil(e^(-5/2)),
E(rho)=rho+2+rho/(1+rho),
L(rho)=2rho+2rho/(1+rho).

For small e, K_e<T_e. The following minima of the ACTUAL nonlinear risk
converge in probability in the iterated width-then-scale sense:

min_(0<=k<=K_e) Q_(m,e)(k)/alpha^2 -> min{3,E(rho)},
min_(K_e<=k<=T_e) Q_(m,e)(k)/alpha^2 -> L(rho),
min_(0<=k<=T_e) Q_(m,e)(k)/alpha^2 -> min{3,L(rho)}.

Here convergence means for every epsilon>0, lim_(e->0) limsup_(N->infinity)
P(absolute discrepancy>epsilon)=0. These statements do not control actual
nonlinear risk after T_e or exchange the two limits.

Moreover there are strict descent-rise-descent witnesses at every fixed
rho>0. With k0=ceil(e^(-1/2)),
k1=floor(log(1+1/rho)/b1), k2=K_e,
k3=floor(log(1+1/rho)/b2), their risks divided by alpha^2 converge to

rho+3, E(rho), 2rho+2, L(rho).

Their three limiting strict margins are
1/(1+rho), rho^2/(1+rho), 2/(1+rho).
For all fixed rho<1, the best risk in the late phase is strictly lower
than the best in the early phase with probability tending to one.
For all fixed rho>1, the early phase is strictly better. At rho=1 the
leading phase minima tie at 3; no finite-e ordering is asserted.

Thus rho=1 is the limiting late-versus-early preference boundary in this
model, whereas strict double descent survives on both sides. No lower
critical-noise rate or exact finite-e second threshold is established.

## 2. Exact frozen risk and nonlinear transfer

The frozen zero-output curve is

F_e(k)=Q_e^0(k)/alpha^2
      =rho(1-q0^k)^2
       +sum_(h=1,2,12)[q_h^(2k)+rho(1-q_h^k)^2].

This follows from Walsh Parseval, identical teacher coefficients alpha
and Walsh noise variances rho alpha^2. The paired initialization gives
zero output exactly. Let p_r(q)=q^2+rho(1-q)^2. Completing the square,

p_r(q)=(1+rho)(q-rho/(1+rho))^2+rho/(1+rho).

For each fixed e and rho the labels are bounded; indeed max|y_i| is at
most (3+2sqrt(rho))alpha, which tends to zero. For all sufficiently small
e the residual bound R_0=2 used in C010 is therefore valid. Its pairwise
finite-horizon transfer applies uniformly through T_e (a finite integer
for this fixed e), and over all noise patterns. It follows that

max_(k<=T_e)|Q_(m,e)(k)/alpha^2-F_e(k)| ->0 in probability as N->infinity.

For this step alpha^2 is a FIXED positive number; no uniform-in-e width
bound is inferred. Consequently it suffices to prove the deterministic
frozen limits for the two ranges and the four witnesses.

## 3. Early-phase minimum

At k=0, F_e=3 exactly. At
k1=floor(log(1+1/rho)/b1), the constant mode has learned, q1^k1 tends to
rho/(1+rho), and q2^k1,q12^k1 tend to one. Hence F_e(k1)->E(rho).
These give the upper bound min{3,E(rho)} for the limiting early minimum.

For the lower bound, take any sequence e->0 and early-phase integers
k_e<=K_e. Choose a subsequence such that k_e is bounded or tends to
infinity, and such that b1 k_e converges in [0,infinity].
If k_e is bounded, all nonconstant q_h^k_e tend to one, so liminf F_e>=3.
If k_e tends to infinity, q0^k_e tends to zero. Uniformly for k<=K_e,
b2 k and b12 k tend to zero, since b2 K_e=O(e^(1/2)). Thus the slow-mode
contribution tends to two, while the fast-mode contribution is at least
rho/(1+rho) by the exact completed square. The limit inferior is at least
E(rho), whether the fast scaled time is finite or infinite. This proves
the matching early lower bound. The subsequence argument applies to
minimizers, which exist because the integer range is finite.

## 4. Late-phase minimum

Uniformly for k>=K_e, q0^k and q1^k tend to zero, since b1 K_e tends to
infinity. Their combined risk tends to 2rho, uniformly in this range.
Each of the two slow contributions is bounded below by rho/(1+rho),
so the late minimum has limit inferior at least L(rho).
For k3=floor(log(1+1/rho)/b2), both slow q's tend to rho/(1+rho), because
b12/b2->1. Also K_e<k3<T_e for all small e, since b2 K_e->0 and
b2 T_e->infinity. Thus F_e(k3)->L(rho), proving the matching upper bound.
Combining Sections 3-4 gives the full finite-horizon minimum as
min{3,E(rho),L(rho)}. The simplification in Section 6 proves the stated
min{3,L(rho)} form.

## 5. Strict double-descent witnesses

At k0 all nonconstant modes remain at one and the constant noise mode
has saturated, so F_e(k0)->rho+3. At k1 the limit is E(rho).
At K_e fast q1 tends to zero and the slow q's to one, giving 2rho+2.
At k3 the limit is L(rho). Subtraction gives exactly the three positive
margins in Section 1. This applies to every fixed rho>0, including rho>1.
The strict finite-e margins transfer to nonlinear GD by Section 2.

For rho=0 the frozen curve is sum_(h=1,2,12)q_h^(2k), strictly decreasing.
This zero-noise frozen statement does not imply monotonic actual nonlinear
risk for all times, nor locate a finite-e onset as rho_e tends to zero.
Pointwise positive-rho results must not be promoted to such a uniform
noise-window theorem.

## 6. Which phase wins?

Exact subtraction yields

E(rho)-L(rho)=(2-rho^2)/(1+rho),
L(rho)-3=(rho-1)(2rho+3)/(1+rho).

If 0<rho<1, then L<3 and L<E, so late training beats the entire early
phase, not just its fast-mode stationary point. If rho>1, then L>3,
so the early phase containing k=0 beats the late phase. Also E>3 for
rho>1, since E-3=(rho^2+rho-1)/(1+rho)>0. Consequently the overall
minimum is min{3,L}. At rho=1 the leading early and late values both
are 3, so a finer expansion is needed to decide finite-scale ordering.

Comparing ONLY E and L would instead produce sqrt(2). That would be the
wrong early-stopping boundary because it omits the allowed initialization
time k=0. This is why the early-phase minimization includes every time
from zero rather than only the first fast-signal minimum. The tiny initial
transient may shift the finite-e preference threshold; it does not change
these strict comparisons for rho bounded away from one.

## Scope and source distinction

Stephenson--Lee, arXiv:2108.12006, Section4, EDD-NES/EDD-ES phases and
P3/P4, distinguish onset of double descent from the higher noise level
where early stopping is preferable. This source does not supply this
model's threshold. Our computation is self-contained and restricted to
the paired four-point model. The lower onset at finite scale, its rate,
a full two-threshold window, iid Gaussian inputs, fixed-positive-noise
unit-teacher dynamics, high probability over label noise, and actual
nonlinear convergence after T_e remain open. Mathematical and novelty
review are pending; no independent audit or full Target2 solution.
