Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-04 idea checkpoint — a sharp heavy-tail dual-deficit coefficient for the postcritical collar

Target: `BHS-MST-CM-UNIV` (Bhamidi–Sen heavy-tailed configuration-model MST universality, tau in (3,4)).

Frozen source metric remains the diameter lower-exponent quantity from admission. Carry-in state is

`eta=(tau-3)/(tau-1) <= beta_MST^- <= 1`.

This checkpoint is idea-first. No code/checker is being manufactured: the new object is an analytic branching/duality identity, not a finite claim.

## Fresh method triple

The preceding target run used B1/B2/B19. This run uses a disjoint triple:

- **B6 DEFORM TO A POINT YOU CAN SOLVE.** Replace the full Kruskal complement by the exactly solvable extinction-tilted branching law at one percolation level and compute the first-order subcriticality after deleting the giant.
- **B20 FIND WHY THE ALGORITHM FAILS.** Ask how far one may sprinkle past a level `p` while keeping the dual branching proxy subcritical. The answer has a sharp first-order barrier.
- **B30 ONE SCALE AT A TIME.** Use that barrier to choose a geometric lambda-ladder with a collar ratio strictly below the barrier; the remaining graph theorem is then a uniform transfer problem, not an unknown choice of scale.

## Exact one-level identity

Let `D` be a nonnegative integer-valued limiting degree law with `0<E[D]<infinity`, and let

`h(s)=E[D s^(D-1)]/E[D]=E[s^X]`, where `X=D^*-1`.

Write `nu=h'(1)` and `p_c=1/nu`. For `p>p_c`, let `q=q(p)<1` be the extinction/failure root

`q = 1-p+p h(q)`.

Set `y=1-q`. Then the root equation gives the exact secant identity

`1/p = [1-h(1-y)]/y = (1/y) int_0^y h'(1-u) du`.

Define the same-level dual branching mean

`m_-(p):=p h'(q)`.

Then, with `g(u):=nu-h'(1-u)`, one has exactly

`p nu-1 = p (1/y) int_0^y g(u) du`,

and

`1-m_-(p) = p [g(y) - (1/y) int_0^y g(u) du]`.

Hence

`[1-m_-(p)]/[p nu-1] = [g(y)-A(y)]/A(y)`,

where `A(y):=(1/y) int_0^y g(u) du`.

Since a pgf has nonnegative derivatives, `g` is increasing and concave, with `g(0)=0`; therefore `A(y)>=g(y)/2`, so this ratio lies in `[0,1]`. Thus the dual deficit is never larger than the original supercritical excess.

## Heavy-tail coefficient

Assume now the canonical regularly varying degree tail

`P(D>=k) = k^(-(tau-1)) L(k) * c(1+o(1))`, `tau in (3,4)`.

Then `X=D^*-1` has tail index `tau-2 in (1,2)`. The Karamata Abelian theorem for Laplace/pgf derivatives gives

`g(y)=nu-h'(1-y)` regularly varying at zero with index

`beta=tau-3 in (0,1)`.

Karamata's integral theorem then yields

`A(y) ~ g(y)/(beta+1)`.

Consequently

`[1-m_-(p)]/[p nu-1] -> beta=tau-3` as `p downarrow p_c`.

Equivalently, if `p=(1+epsilon)/nu`,

`m_-(p)=1-(tau-3)epsilon+o(epsilon)`.

This is the precise first-order dual deficit that the CM analogue of the Bhamidi–Sen postcritical complement argument should exploit.

## Sharp collar barrier at the branching-proxy level

For a later level `p_delta=(1+(1+delta)epsilon)/nu`, the natural first-moment collar proxy obtained by retaining the same extinction tilt is

`m_proxy(delta):=p_delta h'(q(p))`.

Algebra gives

`p_delta/p = 1+delta epsilon+O(epsilon^2)`,

so

`m_proxy(delta)=1-(tau-3-delta)epsilon+o(epsilon)`.

Therefore:

- if `0<delta<tau-3`, the proxy is uniformly subcritical to first order;
- if `delta>tau-3`, the proxy is supercritical to first order;
- `delta=tau-3` is the first-order boundary.

This does **not** yet prove the corresponding statement for the actual conditioned configuration-model remainder across two weight levels. That transfer is exactly the missing random-graph step. The point of B20 is that a proof attempting a wider one-step collar than `tau-3` cannot succeed through this extinction-tilted mean mechanism; the obstruction is visible before any complicated MST argument.

## Consequence for the next graph-level attack

Bhamidi–Sen's rank-one proof controls the diameter outside the principal critical component at a slightly later lambda and then telescopes Hausdorff distances over a geometric lambda ladder. For the configuration model, the analytic calculation above supplies a canonical scale choice: choose any fixed `delta_0 in (0,tau-3)` and compare `lambda` with `(1+delta_0)lambda` one shell at a time.

The graph-level obligations are now sharply separated:

1. prove a **uniform triangular-array transfer** of the one-level dual deficit to the actual half-edge law outside the principal `p_lambda` component, for lambda growing through the barely-supercritical window;
2. dominate the `(1+delta_0)lambda` residual exploration by a subcritical process with mean at most `1-c lambda n^{-eta}`;
3. convert this to an `O_P(n^eta/lambda)` (or logarithmically weakened) residual-height bound and telescope the shells, as in the source's Section 6.

No claim of MST upper tightness is made at this checkpoint. The frozen beta metric therefore has not yet moved; the gain is an exact coefficient and a sharp barrier telling the next proof exactly what has to be uniformized.
