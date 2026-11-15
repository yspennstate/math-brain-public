# Rolling count windows and a finite Poisson-bias certificate

Proposed route,15 October2026, codex-term-362ebe34. Frontier check clear.
This is a proposed physical comparison and finite certificate architecture;
independent correctness review is required before any directional bound is
admitted. No decreasing-increment conjecture is assumed. Initial numerical
pilots are only to decide whether this model is useful.

Fix a window width w>=2 and equal positive integer count caps C<=10000.
States are c in {1,...,C}^w. Put m=d-1 and use any certified horizontal
boundary lower rate sigma(c), for example2mc-2sum_{j<c}popcount(j) in the
new finite discrete certificate's range, when positive.

Births c->c+e_i, if c_i<C, have rates

 lambda_0=sigma(c_0),
 lambda_i=sigma(c_i)+max(c_(i-1)-c_i,0), i>=1.

Front advance has rate c_(w-1) and sends c to (c_1,...,c_(w-1),1).
Its displacement reward is1, including when the count state is unchanged.
Let L be the generator on count functions, counting this transition in
the usual rate*(h(child)-h(parent)) expression. For rational h on all
states and rational a, the desired finite certificate is

 Lh(c)+1-a*c_(w-1)<=0     for EVERY state c.

It is an exact integer check after clearing the bias denominator. Finding
h by numerical linear algebra is permissible; only the final rational
inequalities would be used. A candidate bias, however accurate numerically,
is not itself a certificate.

## Proposed physical realization: thinning, caps and shifts

Use the graphical rate1 independent Poisson-edge construction of Exp(1)
undirected bond FPP. The full infection has the Richardson pure-birth
generator, equivalently the Exp(1) bond FPP infection law from one source.
Restrict attention to infected sites in w consecutive slabs, with movement
forward between slabs only. Behind the window all infection edges are
disabled. In each current slab choose uniformly exactly sigma(c_i)
horizontal infected-to-uninfected edges. This is possible by the certified
boundary bound. Between neighboring slabs choose uniformly exactly
max(c_(i-1)-c_i,0) eligible forward edges, which always exist because at
most c_i predecessor columns can already be occupied. At a count cap
disable every birth into that slab. All other rings are ignored.

Choose these finite edge subsets afresh after each accepted birth or
shift, using independent auxiliary randomness. Different selected edges
have independent rate1 future rings; competing edges to one target simply
contribute their rates to the same birth transition. Thus the count law
is exactly the displayed finite process, independent of the actual
geometry. The eligibility rule is translation and transverse-reflection
equivariant in distribution. Ignored rings can only delay infection,
so every restricted infected point is infected by the full process by
the same chronological time.

There are exactly c_last forward edges into the empty next slab, one
from each last-slab site. Its first accepted ring creates one site there;
shift the window one slab forward and discard the former left slab.
Equal caps ensure the shifted state is allowed. Discarded slabs are
never reenabled. Keeping previous infected points in the full process
preserves the domination; discarding them only restricts future growth.

## Canonical regeneration, not merely a count-state reset

The state (1,...,1) has a unique geometry up to translation: a straight
vertical string. Within a slab that remains in the window the count
never decreases. If its current count is1, it has always had one site
since entering the window. Each of the current singletons was therefore
born from its predecessor's unique site, at the same transverse position.
This uses actual physical geometry, not an unsupported count lumping.

Successive return events to this count state are regenerations, with a
self front-shift at that state also counted as a return event. Future
Poisson increments and fresh selection randomness are independent of
the past. The canonical geometry makes successive blocks identically
distributed after translation. The transverse displacement has mean0
by reflection symmetry.

All block moments needed here are finite. From any positive count state,
w consecutive front advances return to (1,...,1). Each has conditional
probability bounded below by1/R for a finite uniform bound R on the total
accepted event rate, while the holding rate is at least1. Thus return
event counts have a geometric block tail. Time, advance count and
absolute transverse displacement have finite first moments; displacement
is bounded by the number of accepted infections plus the fixed startup
length. Every return cycle advances by at least one slab.

Start with a canonical string made by a finite initial vertical infection
run from the origin. Its finite startup cost disappears after division
by displacement. The iid-cycle law of large numbers yields displacement
per block (E A,0,...,0) and elapsed time E T. The FPP shape theorem,
applied to the actual restricted infected return points and their full
infection times, then gives mu_axis<=E T/E A. This avoids identifying a
first hyperplane hit with an axis point without justification.

## Why the bias inequality would certify the ratio

The front-advance counting process has compensator integral c_last dt.
For an integrable regeneration cycle, bounded h on the finite count
space satisfies Dynkin's formula, and its endpoint values cancel.
Integrating the displayed inequality therefore gives

 E T - a E A <=0.

Together with the cycle comparison this would prove mu_axis<=a. Signed
biases are allowed; finiteness makes them bounded. Self advances must
be included in the reward even though their generator h increment is0.

## Numerical plan and review targets

For w=2 and caps32,64,128 the state spaces have1024,4096,16384 states.
Use sparse uniformization to estimate the stationary mean advance rate
and to solve the Poisson equation by relative iteration. Round h to a
dyadic rational, then evaluate every finite inequality with integers.
The maximum (1+Lh)/c_last is a rigorous finite-model certificate conditional
on the physical comparison, regardless of how the bias was found.

The hard review targets are the Poisson graphical coupling for the
adaptive edge subsets, canonical spatial regeneration, and the matching
reward convention in the finite checker. A numerical a below a diagonal
floor would still be a candidate, not admission. If the bounded pilot
cannot beat the existing profile method, record that measured failure
and do not increase caps blindly. Existing dimension16 exact-profile
reviews take priority over this route.
