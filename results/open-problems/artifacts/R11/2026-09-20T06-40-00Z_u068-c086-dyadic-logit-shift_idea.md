Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — not GPT-6 at maximum.

# R11 / I0054 idea note before checker: U068 noninvertible measure-preserving compiler and C086

This note records the mathematical route **before any checker for this run is written**.

## Continuity and source checks completed first

I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/claims/I0054.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest complete R11 report `runs/R11/2026-09-20T05-38-26Z_i0054-quenched-logit-shuffle-u067-c085-q7c1.md`, and current neighboring P13 material. The compact root R-series row is stale by its own warning, so the supported metric baseline is the newest immutable R11 report: `84 -> 85`. The old planar-SAW assignment remains retired.

`operations/claims/I0054.md` still gives R11 provisional exclusive ownership of Aldous--Janson arXiv:2303.02529v3 Open Problem 18 and still says `PENDING_ADMISSION, not READY`. Current P13 is on a distinct LCS/reset-language track and does not own I0054.

I refreshed the source PDF. Printed page 58 asks: “Are there superficially different discrete models whose limit is the same CTCS(infinity)?” and then asks whether the source subordinator-approximation mechanism can arise in another discrete tree model. The source formalizes CTCS(infinity) via the consistent exchangeable-partition restrictions. R11 therefore keeps the stronger frozen obligation: whole-path total-variation convergence on every fixed finite restriction, which implies finite-state `J_1` and projective finite-restriction convergence.

Fresh bounded web searches on 20 September 2026 for CTCS / critical beta-splitting together with doubling map, Bernoulli shift, logit, measure-preserving transformation and alternative discrete model recovered the Aldous--Janson v3 source, Part III, the 2025 contraction paper, and the August 2026 homogeneous-fragmentation paper, but no checked primary-source resolution of exact Open Problem 18 and no checked instance of the construction below. This is bounded negative evidence only, not a novelty certificate. The doubling map, Bernoulli shift, measure-preserving dynamics, bounded-variation quadrature, and CTMC uniformization are classical ingredients; novelty is claimed only, if at all, for their CTCS assembly.

## Methods actually being tried this run

- **#3 PROVE SOMETHING STRONGER.** Replace the previous interval-exchange/bijection compiler by a theorem for arbitrary Lebesgue-measure-preserving maps in logit space, including noninvertible maps. The sufficient condition is directly on the bounded variation of the induced split integrands.
- **#14 FIND THE GROUP ACTING.** In logit coordinates the CTCS dislocation measure is flat Lebesgue measure. The natural symmetry is therefore the full semigroup of Lebesgue-measure-preserving transformations, not merely translations or interval exchanges. The dyadic Bernoulli shift is the simplest noninvertible element of this symmetry semigroup.
- **#27 SWAP THE QUANTIFIERS.** Instead of fixing one transformation and then taking `N -> infinity`, allow a sequence `S_N` whose dynamical complexity grows with `N`; require only that the induced bounded variation be `o(N)` for each fixed split type. For the dyadic iterates this becomes `2^{r_N}=o(N)`.

## U068 candidate theorem: noninvertible BV logit compiler

Let

`σ(y)=e^y/(1+e^y)`, `ell(x)=log(x/(1-x))`.

For each `N`, let `S_N : R -> R` be a Borel map that preserves Lebesgue measure (invertibility is **not** required) and equals the identity outside one fixed compact interval `[a,b]`. Define

`tau_N(x)=σ(S_N(ell(x)))`.

At harmonic mark `s=1,...,N-1`, keep the standard proposal clock

`lambda_{N,s}=N/(2s(N-s))=1/(2N x_s(1-x_s))`, `x_s=s/N`,

but color every label independently red with probability `tau_N(x_s)`.

For a specified `i|j` visible split define

`F_{N;i,j}(x) = [tau_N(x)^i(1-tau_N(x))^j + tau_N(x)^j(1-tau_N(x))^i]/[2x(1-x)]`.

Because `S_N` is Lebesgue-measure-preserving,

`∫_0^1 F_{N;i,j}(x) dx = ∫_R Phi_{i,j}(S_N(y)) dy = ∫_R Phi_{i,j}(y)dy = B(i,j)`

**exactly for every N**, where

`Phi_{i,j}(y)=1/2[σ(y)^i(1-σ(y))^j+σ(y)^j(1-σ(y))^i]`.

If for every fixed `i,j>=1`

`Var(F_{N;i,j}) = o(N)`,

then the right-endpoint rectangle estimate gives

`|q_N(i,j)-B(i,j)| <= [Var(F_{N;i,j})+O_{i,j}(1)]/N -> 0`.

Fresh proposal colors make every finite visible restriction strongly lumpable, so finite-state generator convergence plus common uniformization yields whole-path TV convergence on every fixed `[k]` and finite time interval. Therefore the projective limit is CTCS(infinity).

This strictly strengthens U066/U067 because `S_N` need not be bijective and the condition is structural (`BV=o(N)`) rather than tied to interval-exchange cell counts.

## C086 candidate: iterated dyadic Bernoulli shift in logit space

Set `L=2 log 2 = log 4`. On `[0,L)` define the doubling map

`D(y)=2y mod L`,

and set `D(y)=y` outside `[0,L)`. For each `N`, take

`r_N=max(1,floor((1/2) log_2 N))`, `b_N=2^{r_N}`,

and use `S_N=D^{r_N}`.

On `[0,L)`, `S_N(y)=b_N y mod L`. This is `b_N`-to-1 and preserves Lebesgue measure exactly: for measurable `A subset [0,L)`, its preimage is the disjoint union of `b_N` affine copies each of measure `Leb(A)/b_N`. Thus this model is outside the interval-exchange/bijection class.

On the fixed compact `x`-interval `[1/2,4/5]`, each branch has derivative scale `b_N`, there are `b_N` branches, and branch jumps are uniformly bounded. Therefore for every fixed `i,j`

`Var(F_{N;i,j}) <= C_{i,j}(1+b_N)`.

Since `b_N<=sqrt(N)` up to a fixed factor,

`Var(F_{N;i,j})/N = O(N^{-1/2}) -> 0`.

U068 therefore gives the complete CTCS(infinity) path limit.

### Exact `N=4` witness to check next

Here `r_4=1`. In `x`-coordinates the map on `[1/2,4/5)` is

- for `1/2 <= x < 2/3`, `tau(x)=x^2/[x^2+(1-x)^2]`;
- for `2/3 <= x < 4/5`, `tau(x)=x^2/[x^2+4(1-x)^2]`;
- outside `[1/2,4/5)`, `tau(x)=x`.

Thus at harmonic grid `(1/4,1/2,3/4)` the biases are exactly

`(1/4, 1/2, 9/13)`.

Direct exact arithmetic predicts

`q(1,3)=406041/1827904`,
`q(2,2)=310519/1827904`,
`Lambda_root=2555721/1827904`,
`P(2|2)=310519/851907`.

The source CTCS(4) balanced-root probability is `3/11`, and

`310519/851907 - 3/11 = 859988/9370977 != 0`.

So if the checker confirms the arithmetic, leaf relabeling and positive global time rescaling cannot identify C086 with source CTCS.

No source-level closure is claimed here. This is an author-side candidate until the full proof and exact checker are written and archived.