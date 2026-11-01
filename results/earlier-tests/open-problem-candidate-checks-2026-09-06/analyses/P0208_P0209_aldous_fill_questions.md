# Independent checks of two historical Aldous–Fill questions

Both complete candidate texts were read before these controls. The finite controls are
in checks/check_p0208_p0209.py. This
is mathematical review of the stated arguments, not a novelty certificate.

## Primary definitions and scope

The primary monograph was accessed at
https://www.stat.berkeley.edu/~aldous/RWG/book.pdf and the local archive matched
SHA-256 8f9b934111c30b3f8fd29d94a18794d4b86f824b19f7a3c27b1153cdfac08e79.
Printed pages 26, 115, 132, 136–137, 254 and 259 were independently extracted and
read. Page 137 asks for a chain-independent normal approximation controlled by
the exact sup norm of a centered, unit-variance function and time divided by
relaxation time. Page 259 asks three asymptotic bounds for arc-transitive graphs
other than cycles. Rates have no upper constraint; rate-one continuization
preserves the graph parameters used here. The arc-transitivity formula on page
254 has the index error disclosed by the candidate; the surrounding claims use
the standard directed-edge convention.

The book's own landing page, https://www.stat.berkeley.edu/~aldous/RWG/book.html,
explicitly says the recompilation did not update its content. Its current
availability is therefore not evidence that these 1994 questions remain open.

## P0208: rederivation from first-step equations

For the graph with vertices (j,b), j modulo m and b in {0,1}, adjacency joins
both vertices in each neighboring fiber. A rotation or reflection sends the
base directed edge to any desired base directed edge. Independent fiber swaps
then send its endpoints to any desired pair of endpoint bits. This proves the
standard arc-transitivity requirement; it does not use the erroneous printed
formula. For odd m at least five this is a simple connected 4-regular graph on
2m vertices, hence not a cycle.

The first coordinate is the ordinary cycle walk, with fresh independent fair
second coordinates at every step. The expected first arrival at fiber zero
from fiber j is j(m-j), as follows from the discrete Dirichlet equation. A
return to fiber zero starting there takes mean m. Starting at the target's
twin, a return succeeds with probability 1/2, giving h=m+h/2=2m. At a first
arrival from a different fiber, the extra expected cost is half of 2m. Thus
the candidate's added term is m, not 2m. Reversibility and the displayed
symmetries agree with symmetric hitting times here; symmetry of hitting times
is not being asserted for an arbitrary regular graph.

Summing over all 2m possible initial vertices gives
tau0=(m^2-1)/6+m. The largest hitting time is floor(m^2/4)+m, which exceeds
the same-fiber twin hitting time for m>=5. Consequently the maximal commute
time is 2 floor(m^2/4)+2m. The ratio to twice tau0 tends to 3/2.

Independently of that recurrence proof, the transition operator decomposes
into the m-dimensional fiber-constant subspace and the m-dimensional fiber-
antisymmetric subspace. On the former it is the cycle operator; on the latter
it vanishes. The second largest eigenvalue is cos(2 pi/m), so relaxation time
is asymptotic to m^2/(2 pi^2). Negative eigenvalues do not enter the continuous-
time gap. These formulas contradict each proposed order or limit in the
literal question. The graph size is 2m throughout, never m.

An independent exact linear-system checker constructs adjacency directly,
solves (I-P)h=1 with an absorbing target by Fraction Gaussian elimination,
and checks every resulting first-step equation for m=5,7,9,11,13. It agrees
with the formulas and verifies 360 explicit directed-edge automorphisms.
Five intentionally omitted fiber costs fail the first-step equations. These
finite checks support the analytic family argument; they do not replace it.

The graph is established prior art. Conder's 2013 primary lecture notes,
https://www.famnit.upr.si/sl/resources/files/konference/rogla2013/conderlecturenotes.pdf,
page 8, give precisely this graph and its arc-transitivity. This confirms the
construction's scope and undermines an unsupported claim of originality.
It does not date a published answer to the probability question.

## P0209: normalization and the rare-event obstruction

Set e=s^-2 and R=s^4. The slow coordinate has rates e and 1-e and stationary
success probability e; the fast fair sign flips at rate R/2. Their independent
product is a four-state reversible continuous-time chain. Its eigenvalues are
0,-1,-R,-(R+1), so the relaxation time equals one.

Let A=2e+sqrt((1-e)(1-4e)) and B=(2-A)/(1-e). For 0<e<=1/9,
A is the positive root of A^2-4eA+5e-1=0. The other root is negative,
while the quadratic is positive at one. Thus 0<A<1 and B>1. Substitution
gives A^2+B^2 e(1-e)=1. The function g=AZ+B(Y-e) is centered, has stationary
variance one, and attains value two at (Y,Z)=(1,1). Because e<1/2,
A+B e <= A+B(1-e)=2; the other signs have no larger absolute value.
The sup norm is therefore exactly two for every chain, closing the otherwise
dangerous moving-first-argument loophole in a uniform bound.

The two independent coordinate eigenfunctions give covariance
A^2 exp(-Ru)+B^2 e(1-e) exp(-u). Hence the asymptotic variance rate is
sigma^2=2A^2/R+2B^2 e(1-e)>0. A second route solves the Poisson equation
(-Q)h=g with h=(A/R)Z+B(Y-e), and computes sigma^2=2 E_pi(g h).
The exact checker constructs all four generator rows from transition rates,
checks detailed balance and stationarity, verifies the Poisson equation and
an eigenbasis, and obtains precisely this same expression. All calculations
use rational pairs a+b sqrt(D), not floating point or simulated paths.

For a particularly direct independent attack on the limit, write F=A int Z
and H=B int(Y-e), integrating to time s. The chance of a slow-coordinate
success anywhere is at most e+s e. If no success occurs, H=-B e s.
Also E F^2 <=2A^2 s/R. Thus

    P(F+H > 0) <= e+s e + 2A^2/(R B^2 e^2 s)
                 <= 1/s^2+3/s,

using A<=1, B>=1 and R e^2=1. Positive normalization does not alter the event
at zero, so the Kolmogorov distance is at least

    1/2 - 3/s - 1/s^2.

This deterministic probability bound is enough to refute the proposed
uniform convergence at the fixed sup norm two. It avoids inferring a weak
limit from finite-time variance convergence and avoids any unjustified
interchange of the distributional supremum with a limit. The candidate's
convergence-in-probability argument is independently valid as well.

Finite-time variance divided by sigma^2 s does tend to one. For either
covariance term c exp(-lambda u), direct integration gives
2c[s/lambda-(1-exp(-lambda s))/lambda^2]. The relative slow-mode correction
is O(1/s), and the fast term is negligible in the variance rate. This is
compatible with collapse in probability because rare excursions carry the
second moment. Uniform integrability is absent.

Rescaling Q to Q/R and observing for R s units leaves the standardized
integral and t/tau2 unchanged. Outgoing rates then do not exceed one.
Thus an implicit rate cap would not rescue this uniform statement.

The exact checks cover s=3,4,10,100,1000. They verify the exact mean, variance,
sup norm, Poisson equation, covariance-derived variance rate and eigenbasis.
Five deliberately unbalanced rates fail the stationary-law check. These
controls do not establish a theorem for all parameters; the algebra and
probability bound above provide the infinite-family argument.

## Remaining strongest counter-cases

A hidden hypothesis on a minimum stationary mass, a lower asymptotic-variance
scale, a stronger symmetry class or a different time normalization could
exclude these examples. None appears in the exact displayed questions and
surrounding definitions read. Changed statements elsewhere would need new
review. The present constructions cannot be applied to such strengthened
questions without checking them separately.

A later published resolution would defeat novelty and the current-open designation
without changing the validity of these constructions. Searches for both precise problem
numbers, names and relevant graph/CLT terms, and the primary author and monograph pages,
did not establish a later disposition. This bounded search is incomplete.
