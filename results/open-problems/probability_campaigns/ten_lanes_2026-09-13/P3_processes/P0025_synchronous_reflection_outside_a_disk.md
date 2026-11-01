# P0025 - Synchronously coupled reflected Brownian motions outside a disk

Continuous-time stochastic processes, 13 September 2026. **Not settled.** What follows is exact
structure and a simulation that looked decisive and was not.

## The problem

Corpus id `P0025`, source `burdzy_open_20260906`, locator "Problem 5(ii)":

> For synchronously coupled reflected Brownian motions in the exterior of a nondegenerate closed
> disk, can their distance have positive limsup with positive probability?

The recorded attempt (`P0025-A001`) observed that at a boundary point the reflection can either
shrink or enlarge the separation, and stopped there. The point here is that the dichotomy
is completely explicit, and that saying so changes what the problem is.

Write D = {x in R^2 : |x| > R}, and let X, Y solve dX = dB + n(X) dL_X, dY = dB + n(Y) dL_Y with the
same Brownian motion B and the inward (to D) unit normal n(x) = x/R on |x| = R.

## The separation is a pure local-time process, and its sign is a tangent line

Under a synchronous coupling the noise cancels in the difference, so X - Y has no martingale part at
all: d(X-Y) = n(X) dL_X - n(Y) dL_Y. With n(x) = x/R and |X| = R at X's boundary visits,

    d|X-Y|^2 = 2<X-Y, n(X)> dL_X - 2<X-Y, n(Y)> dL_Y
             = (2/R) <X, X-Y> dL_X + (2/R) <Y, Y-X> dL_Y.                              (*)

So |X-Y|^2 is a continuous process of finite variation which moves only while one of the two
particles is on the circle - between boundary visits the separation vector is *frozen*.

Reading the sign off (*): **at a boundary visit of X the separation grows iff <X, X-Y> > 0, that is,
iff Y lies strictly on the disk side of the tangent line to the circle at the contact point, and
shrinks iff Y lies beyond that tangent line.** (Equivalently, with p = |X|^2 - R^2, q = |Y|^2 - R^2
the squared tangent lengths and V = |X-Y|^2,

    dV = (1/R) [ (V - q) dL_X + (V - p) dL_Y ],

and at an X-visit p = 0, so the criterion is V versus q.)

Both readings say the same thing, and together they explain why the problem is hard in exactly the
way it is hard. The separation vector X - Y is constant between boundary visits; the tangent line
rotates with the contact point. So the *same* separation vector is contracting at some contact
points and expanding at others, and which one happens is decided by where on the circle the pair
happens to arrive. In local terms near the boundary: if the contact happens while Y is displaced
radially outward from X, the distance shrinks; if Y is displaced tangentially, it grows (to second
order the threshold is radial offset of Y versus R (angular offset)^2 / 2). No monotone-distance
argument can exist, and that is not a gap in anyone's technique.

For contrast: in a convex domain the same computation gives both terms of (*) a sign, which is the
classical statement that synchronous couplings contract in convex domains (this is Problem 5(i)'s
background). The exterior of a disk is the cheapest domain in which the convexity sign fails, which
is presumably why Burdzy isolates it.

## Two further exact identities

*A local martingale.* With c = X ^ Y = X_1 Y_2 - X_2 Y_1 (twice the signed area of 0, X, Y),

    dc = (X - Y) ^ dB + c d(L_X + L_Y)/R,

because the reflection at X pushes c by (X ^ Y) dL_X / R and likewise at Y. Hence

    exp( -(L_X + L_Y)/R ) (X ^ Y)   is a local martingale.

*A function with no local-time terms.* Looking for F(V, p, q) whose reflection terms cancel means
solving 2R^2 F_p = -F_V (V - q) on {p = 0} together with its mirror on {q = 0}. One solution is

    F = ( |X-Y|^2 + p q / (2R^2) ) * exp( -(p + q) / (2R^2) ),     p = |X|^2 - R^2, q = |Y|^2 - R^2,

which therefore has no dL_X or dL_Y part; its remaining dt and dB parts are ordinary Ito terms. The
drift is not computed here; whether it has a sign is the obvious thing to try next: a signed
drift would turn F into a supermartingale or submartingale and could decide the problem.

## The simulation, and why it says nothing

(*) was simulated directly: projection scheme in the exterior of the unit disk, the same Gaussian
increments driving both particles, adaptive step dt <= (gap/4)^2, several seeds and several initial
separations, out to t = 10^4. The separation looked frozen at a positive value in almost every run,
which reads at a glance as "yes, the limsup is positive".

That reading is wrong. By (*) the separation moves on one clock only: A = (L_X + L_Y)/R. Over t = 10^4 the runs
accumulated between 0 and 19 units of boundary local time - in several seeds, exactly zero. Two
dimensional Brownian motion is only neighbourhood recurrent, so the disk is visited rarely and the
boundary local time grows very slowly in real time. A separation that is frozen over a horizon on
which its driving clock barely advanced is not evidence about its limsup; it is a picture of the
clock, not of the process. Any numerical attack on this problem must be run and reported in the
local-time clock A, not in t.

Rebuilt in the A clock, the experiment failed for a second, sharper reason. Making the step adaptive - dt = (gap/4)^2, so that far excursions are cheap - degenerates
in an unbounded domain: when the pair wanders to distance 10^6 the step becomes 10^11 and the run
jumps to t = 4 x 10^13 having interacted with the boundary a handful of times. Measured: 1.5 million
adaptive steps per seed reached A = 1 or A = 2, and several seeds got there only by way of those
runaway steps, which are not a simulation of anything. A 25-minute run targeting A = 400 did not
finish. (In one of the three initial separations Y started inside the disk and was projected back to
the circle, so that row is an experiment at separation 0.05, not 0.3.)

The conclusion is methodological and firm: path simulation is the wrong instrument for this problem.
Because the separation vector is frozen between boundary visits, the only object worth simulating is
the chain of boundary visits itself - the excursion/boundary-trace representation - which advances A
by construction and never wanders. Building that chain is step 2 of the obligations below.

## Status

- Identity (*), the tangent-line criterion, the local martingale, and the local-time-free F:
  **proved** (elementary Ito; each derived twice and checked back by differentiation).
- The question itself, limsup |X-Y| > 0 with positive probability: **open**, untouched.
- The real-time simulation: **uninformative**, and recorded as such.

## Remaining obligation

The identity reduces Problem 5(ii) to a question about one sequence of signs. Let tau_1 < tau_2 < ...
enumerate the boundary visits and let sigma_k = sign <X_{tau_k}, X_{tau_k} - Y_{tau_k}> (with the
mirrored expression at Y-visits). Then |X-Y|^2 is a multiplicative-looking functional of the
(sigma_k) weighted by the local time increments, and the whole problem is whether that functional
can avoid 0. The exact next step, in order of cheapness:

1. Compute the drift of F above. If it has a sign, F is a super- or submartingale and the
   convergence of |X-Y| follows or is obstructed.
2. Redo the simulation in the local-time clock - run until A reaches a few hundred rather than until
   t reaches a few thousand - and look at |X-Y| as a function of A. This is a different experiment,
   not a longer one.
3. Identify the law of the contact point given the frozen separation vector. Because the pair moves
   rigidly between visits, the pair (contact angle, separation vector) is a Markov chain on
   circle x R^2 driven by the excursion measure of reflected Brownian motion outside the disk, and
   the question is whether |separation| -> 0 for that chain.

## Literature

Not searched exhaustively. The obvious
neighbours are Benjamini, Burdzy and Chen on shy couplings and Burdzy's own work on mirror versus
synchronous couplings. Note that the sibling P0027 (rigidity of shy couplings) already records the
deterministic shy coupling Y = -X on an annulus, which is a *mirror* coupling, not a synchronous one
- the two questions do not transfer.
