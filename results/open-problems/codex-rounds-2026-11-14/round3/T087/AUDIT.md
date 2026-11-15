# Audit of the volume-tail extension

## Independent check of the covering and its numbers

The centers are m times the integer shell of radius 12. Counting all
integer points of the outer cube and subtracting its interior gives
25^d-23^d centers. In dimension three this is

    25^3-23^3 = 15625-12167 = 3458.

An independent partition by the first coordinate attaining absolute
value 12 gives

    2*25^2 + 2*23*25 + 2*23^2
      = 1250+1150+1058 = 3458.

The same value follows from the exact cubic shell formula
24*12^2+2=3458. The argument needs only a finite constant depending on d,
so the large size of this covering constant causes no exponent loss.

For a center of norm 12m, a box of radius 2m has minimum possible norm
12m-2m=10m and maximum possible norm 12m+2m=14m. Both lie strictly
between 8m and 16m. A boundary point of B_{16m} is at distance at least
16m-12m=4m from the center, so the forward path must cross its box of
radius 2m. These checks use the reverse triangle inequality, and also
follow coordinatewise by inspecting a coordinate attaining the norm.

The covering counts components, not disjoint paths. Distinct annulus
components cannot merge in a small box that is a subgraph of the annulus.
They may merge outside the annulus; this does not affect the injection.
Conversely, a single annulus component may split into several small-box
components; this only enlarges the right side of the covering inequality.

## The largest-cluster factor, derived a second way

At a good scale let r=ceil(m^epsilon), A=V_{4m}pi(20m), and
q=P(J_m>r). Choose a uniform vertex S of B_{4m}, independently of the
edges. It has probability at least pi(20m) of reaching partial B_{16m}.
For that to happen when J_m>r, it must first reach partial B_{7m}.
The latter event, conditional on S=x, depends only on inner edges and
has probability at most pi(3m). Thus its joint probability with the
outer bad event is at most pi(3m)q. Averaging over x preserves the bound.

At good scales pi(3m)<=C pi(20m) and eventually q<=1/(2C).
Consequently the expected number of core vertices reaching the boundary
on the complementary event is at least A/2. There are at most r
components containing those vertices there. The largest such component
has at least their total divided by r, configuration by configuration.
Therefore E M_m>=A/(2r), exactly as in (20).

This checks both the single factor r and the half in (20). It uses no
independence of component masses and counts, nor an expectation of J_m.
The inner/outer independence is conditional on a deterministic vertex,
between edge sets at norms at most 7m and at least 8m.

For conversion to the volume tail, sample a uniform vertex T of B_{16m}.
On M_m>=q its conditional chance of belonging to a largest component
is M_m/V_{16m}. Its unrestricted cluster contains that component. Hence

    F(q) >= E[M_m 1_{M_m>=q}]/V_{16m}
         >= (E M_m-q)/V_{16m}.

This independently checks (22) without assuming translation invariance
of finite-box cluster sizes.

## Exponent arithmetic checked by a second route

The upper volume-tail estimate balances an arm probability n^{-a} with
the mass bound n^{d-2a}/t. Equating these orders gives t=n^{d-a} and
F(t) at order t^{-a/(d-a)}. Independently, the lower bound uses a
component of mass m^{d-a-o(1)} contributing mass divided by box volume,
which is m^{-a-o(1)}. Eliminating m gives the same exponent.

For the averaged growth exponent, the product tF(t) at
t=n^{(1-h)(d-a)} has exponent

    (1-h)(d-a) * [1-a/(d-a)] = (1-h)(d-2a).

Separately, with delta=(d-a)/a,

    (d-a)(delta-1)/delta = d-2a.

These two expressions agree. The sign is positive exactly in the stated
range a<d/2. As algebraic consistency tests only: substituting d=2 and
a=5/48 gives delta=91/5 and d-2a=43/24. Substituting a=2 and d>6 gives
delta=d/2-1, rather than the mean-field value 2; the theorem cannot be
used in that regime without its unproved (and incompatible there)
count hypothesis. At d=6 the same algebra gives delta=2.

## Attempts to break the argument

1. **Rare large counts.** A count n^2 with probability 1/n and 1
   otherwise satisfies (P), yet its expectation is n+1-1/n. This is an
   abstract example, not a percolation construction. It refutes the
   inference (P)=>(H). The proof instead bounds the expected *inner
   mass* on the outer bad-count event by an independent inner arm times
   its probability. Arbitrarily large bad counts do not enter this bound.

2. **Nonmonotonicity of component counts.** No BK inequality is applied
   to {K_n>=k} or {J_m>=k}, which need not be increasing. All comparisons
   of counts are deterministic injections. No disjoint-path count is
   substituted for a component count.

3. **Wiring and whole-lattice connections.** All box and annulus
   components in the proof are induced free-boundary components.
   Connections used to define pi, tau, F and X are unrestricted.
   Boundary wiring would invalidate the interpretation of components
   and is absent throughout.

4. **Path return through the core.** A path may enter and leave B_{8m}
   many times. Its segment after the *last* visit to partial B_{8m}
   remains in A_m until its endpoint on partial B_{16m}. Thus every
   B_{16m} component containing a counted core vertex contains an annulus
   crossing component. Different box components contain different ones.

5. **Touching boundaries and shared edges.** J_m may use tangential
   edges on partial B_{8m}. The auxiliary U_m stops at partial B_{7m},
   so no edge is shared. Stopping at partial B_{8m} instead would require
   a separate check; it is deliberately avoided.

6. **Only logarithmic exponent existence.** A slowly varying remainder
   is not assumed. Good-scale extraction telescopes the exact sequence
   pi(3*8^j); the o(j) errors at the two endpoints are o(log N), whereas
   the contradiction gap is zeta log N. This works for every fixed
   zeta>0. It does not bound pi(3m)/pi(20m) at every m.

7. **Filling all sizes.** The lower tail is first proved only for good
   m. For every sufficiently large real t, a good scale exists between
   t^{1/(D-3epsilon)} and its (1+zeta) power. The direction
   F(t)>=F(m^{D-3epsilon}) is correct because that threshold is at least
   t. The final estimate thus holds at every large t, not just a sequence.

8. **Order of parameters.** Fix epsilon with 3epsilon<D, then fix
   zeta>0, then send t to infinity. Afterwards send zeta and epsilon to
   zero. For recovering X, fix h>0 before sending n to infinity, and
   only then send h to zero. All thresholds may depend on the fixed
   parameters; no uniform limit in those parameters is required.

9. **Infinity atom.** Since a>0, pi(n) tends to zero, so there is no
   positive probability of an infinite cluster under the theorem's
   assumptions. The upper tail estimate would itself rule out such an
   atom. Continuity at p_c is not an extra assumption silently inserted.

10. **Circularity.** The upper X estimate in Section 1 comes only from
    the one-arm law. This gives the upper volume tail. The annulus and
    largest-cluster argument gives the lower volume tail. Only then is
    the lower X estimate obtained. The earlier forward theorem under
    expected-count control is not invoked.

11. **Scope.** The theorem requires the one-arm exponent to exist.
    It supplies neither a one-arm existence proof under (P) alone, nor
    the earlier reverse implication from X exponent existence under the
    weakened hypothesis. No uniform pointwise two-point law or
    near-critical matching follows here.

All numerical constants in this audit are exact arithmetic. No numerical
percolation data or executable computation is used.
