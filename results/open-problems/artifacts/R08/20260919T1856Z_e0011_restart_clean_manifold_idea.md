# R08 E0011 — recovery idea before checker code: test the full-hazard fuel-strip restart class, not another rare word

Run: 2026-09-19 UTC. Methods selected by the preceding stuck report: **B2 / B8 / B20**.

Entering frozen metric: `B_cat >= b21_desc`, with diagnostic `log10(b21_desc) ~= -48.42893853604687`; supported unchanged count enters at `4`.

The mandatory stuck report isolated the missing ingredient as a restartable oriented seed class. The chosen recovery is to reduce the simplest fixed-boundary version to a finite computation.

## B2 — attack the restart architecture from the negative side first

Use the width-ten oriented seed from the preceding run: two vacant rows `y=0,1`, a CO fuel rail `y=2`, a second CO rail `y=3`, and the four lateral vacant guards `(-1,1),(10,1),(-1,2),(10,2)`. Freeze every site outside this finite patch to CO. At `p=1/2` the effective rates are `1/2` per vacant-site CO clock and `1/4` per vacant-vacant edge O2 clock.

The first question is not whether a five-edge prescribed word can translate the seed — that is already known. It is whether a natural restart class survives *ordinary* full-hazard evolution. I will first test the largest clean pure-vacancy manifold that keeps the two original strip rows and guards vacant, keeps the second CO rail intact, and records only which sites of the first fuel rail have been consumed. Any event that leaves this clean manifold is conservatively declared FATAL; events that leave the manifold state unchanged are RETRY; rail-consuming events are progress; success is complete removal of the first rail, i.e. the one-row translated vacant strip.

This is intentionally an attack on the proposed route. If even this maximally permissive clean-manifold trial has a success/fatal ratio far below `63`, it identifies exactly which ordinary marks must be absorbed into any viable larger seed class.

## B8 — exact finite discretization

A clean state is a subset `A subset {0,...,9}` of already-consumed fuel-rail sites, so there are only `2^10=1024` states.

After deleting literal RETRY self-loops, rates can be multiplied by four and represented by integer weights. The non-self transitions are:

- `y=0 -- y=1` vertical O2 at column `x`: if `x notin A`, consumes rail site `x` and sends `A -> A union {x}`; if `x in A`, it leaves the clean manifold and is FATAL.
- top-row horizontal O2 on `(x,1)-(x+1,1)`: if neither endpoint is in `A`, consumes both rail sites; otherwise FATAL.
- either lateral-guard/top-row O2 edge: consumes the endpoint rail site if present, otherwise FATAL.
- a CO arrival at a consumed rail site refills that site, `A -> A\{x}`.
- CO arrivals on the permanently vacant two-row strip or four guards are FATAL in this clean trial.
- O2 events using newly vacant `y=2` fuel sites are FATAL because they can damage the second rail or create an O defect.

Bottom-row horizontal O2 events and the two vertical guard O2 events are exact RETRY self-loops under the fixed all-CO boundary and cancel from the harmonic equation.

The resulting finite hitting probability is a linear fixed point. I will compute monotone fixed-grid lower and upper iterates: floor updates from zero give certified lower bounds, and ceiling updates from one give certified upper bounds. This gives an exact-arithmetic interval rather than a Monte Carlo estimate.

## B20 — find why the algorithm fails

In parallel I will attempt the literal full 44-cell Markov expansion, where every patch cell may be vacant/CO/O and the exterior is frozen CO. The purpose is diagnostic: determine whether exact state growth remains tractable, and if not, record the first state-count explosion rather than pretending the clean-manifold result covers repair excursions.

The expected decision is therefore one of two useful outcomes:

1. the clean restart probability is unexpectedly near one, which would justify enlarging the source-valid seed class immediately; or
2. it is tiny, and the exact rate decomposition identifies the missing repair states (CO/O defects) that any next route must include.

No source-level metric movement is claimed by this idea note. A fixed all-CO exterior and one-child transport remain only a deformation of Durrett Problem 5.
