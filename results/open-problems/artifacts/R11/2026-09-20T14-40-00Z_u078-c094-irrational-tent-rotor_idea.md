# R11 / I0054 — pre-code idea note for U078 / C094

Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

This note is intentionally committed before checker code. It records the mathematical route only.

## New-method moves

- **#3 PROVE SOMETHING STRONGER.** Replace the finite cyclic phase alphabet of C091 and the shadow-refresh extractor of C092/C093 by a deterministic irrational rotation on the circle. Prove convergence uniformly for an arbitrary deterministic offset array at the active harmonic marks.
- **#20 FIND WHY THE ALGORITHM FAILS.** The tempting no-shadow hash of the last ordinary inactive *split* mark is not clean: conditioning on which visible carrier survives biases the harmonic mark through its Bernoulli coloring law. Avoid that conditioning completely by making mixing occur in proposal-count time, before any need to condition on an inactive mark.
- **#25 COUNT THE SAME THING TWICE.** Analyze active proposals both as a thinning of the full harmonic proposal stream (giving a geometric number of deterministic rotation steps) and through the limiting split generator (inactive Riemann sum + active tent-logit average). The two descriptions should identify the CTCS beta rates.

## Candidate theorem U078 — Abel/irrational-rotation tent compiler

For scale N let

\[
\lambda_{N,s}=\frac{N}{2s(N-s)},\qquad 1\le s\le N-1,
\]

and let the active marks be

\[
A_N=\{s:1/2\le s/N<4/5\}.
\]

Write

\[
H_N:=\sum_{s=1}^{N-1}\lambda_{N,s}=H_{N-1},\qquad
W_N:=\sum_{s\in A_N}\lambda_{N,s},\qquad q_N=W_N/H_N.
\]

Then `W_N -> log 2` and `q_N -> 0`.

Fix an irrational `omega in R/Z`. Each current clade carries a phase `theta in R/Z`. Every harmonic proposal, active or inactive, first advances

\[
\theta\leftarrow \theta+\omega\pmod 1.
\]

For inactive `s`, color leaves iid Bernoulli(`s/N`) exactly as in the source proposal mechanism. For active `s`, choose an arbitrary deterministic offset `a_{N,s} in R/Z` and set

\[
T(u)=2\min(\{u\},1-\{u\})\in[0,1],\qquad L=\log4,
\]
\[
p_{N,s,\theta}=\sigma\!\left(L T(\theta+a_{N,s})\right),
\qquad \sigma(y)=\frac{e^y}{1+e^y}.
\]

Color leaves iid Bernoulli(`p`). Trivial colorings leave the clade intact with the updated phase; a nontrivial split gives both children the updated phase and fresh harmonic clocks.

Claim: for every fixed visible restriction `[k]` and finite `T`, the entire partition-valued path converges in total variation to the corresponding CTCS path, uniformly over the deterministic offset array `a_{N,s}`.

### Mixing lemma to prove

Between successive active proposals along any visible carrier, the number `K` of harmonic proposals, counting the terminal active proposal, is geometric with parameter `q_N`:

\[
P(K=r)=q_N(1-q_N)^{r-1}.
\]

For a continuous 1-periodic function `f`, define the Abel average

\[
A_qf(x)=\sum_{r\ge1}q(1-q)^{r-1}f(x+r\omega).
\]

For each Fourier character `e_m(x)=e^{2\pi i m x}` with `m != 0`,

\[
A_qe_m(x)=e^{2\pi i m x}\frac{q e^{2\pi i m\omega}}
{1-(1-q)e^{2\pi i m\omega}},
\]

which tends to `0` uniformly in `x` because `omega` is irrational. Trigonometric-polynomial approximation then gives

\[
\sup_x\left|A_qf(x)-\int_0^1 f(u)du\right|\to0
\]

for every continuous periodic `f`. Translation of `x` absorbs every offset `a_{N,s}`, so the estimate is uniform over the offsets.

The tent map is continuous on the circle and pushes Lebesgue measure on the circle to Lebesgue measure on `[0,1]`: each `t in (0,1)` has the two inverse branches `u=t/2` and `u=1-t/2`, each with Jacobian `1/2`. Hence `L T(U)` is uniform on `[0,L]` when `U` is uniform on the circle.

For each fixed visible block size `m` and red count `r`,

\[
f_{m,r}(u)=p(u)^r(1-p(u))^{m-r},\qquad p(u)=\sigma(LT(u)),
\]

is continuous. Therefore the coloring kernel at an active proposal, conditional on any incoming phase and any active mark, converges uniformly to the fresh-uniform-phase coloring kernel.

Since at most `k` visible carrier blocks exist and each has active-proposal rate `W_N=O(1)`, the expected number of active proposals up to time `T` is at most `kTW_N`; coupling the finite coloring kernels at each such proposal should give whole-path TV distance `o(1)` from the fresh-uniform-phase comparator.

### Fresh-uniform-phase generator

With `U` fresh uniform on the circle at an active proposal, `LT(U+a)` is uniform on `[0,L]` for every offset `a`. For a specified `i|j` split let

\[
g_{i,j}(p)=p^i(1-p)^j+p^j(1-p)^i.
\]

The active contribution converges to

\[
\frac{L}{2}\cdot\frac1L\int_0^L g_{i,j}(\sigma(y))dy
=\frac12\int_0^L g_{i,j}(\sigma(y))dy,
\]

because `W_N -> L/2`. The inactive harmonic Riemann sum converges to the complementary integral. Using `dy=dx/[x(1-x)]`, the total is

\[
\int_0^1\frac{g_{i,j}(x)}{2x(1-x)}dx
=B(i,j)=\frac{(i-1)!(j-1)!}{(i+j-1)!}.
\]

Thus the finite visible generators converge entrywise to CTCS. Common uniformization gives whole-path TV convergence for the fresh comparator, and the Abel coupling transfers it to the deterministic irrational rotor. Exact restriction consistency follows from iid colors plus inheritance of the phase at every split.

## Concrete model C094 and exact finite witness plan

Take zero offsets `a_{N,s}=0`. For all `N>=5`, use the fixed golden irrational rotation

\[
\omega=(\sqrt5-1)/2\pmod1.
\]

A finite prefix does not affect the limit; for `2<=N<=4` set `omega_N=1/2` so an exact rational finite witness is available.

At `N=4`, harmonic embedded mark probabilities are `(4/11,3/11,4/11)` for `s=1,2,3`. Mark `s=1` is inactive and uses `p=1/4`; marks `s=2,3` are active. The phase toggles at every proposal. Starting from phase `0`, the first active bias is `4/5` because `T(1/2)=1`; from phase `1/2`, the next active bias is `1/2` because `T(0)=0`.

Let `B_0,B_1` be eventual balanced-root (`2|2`) probabilities from the two phase states. Exact mask enumeration should give

\[
A_0=3489/20000,\quad N_0=7563/20000,
\]
\[
A_1=111/352,\quad N_1=69/352,
\]

with recurrences

\[
B_0=A_0+N_0B_1,\qquad B_1=A_1+N_1B_0.
\]

Solving predicts

\[
B_0=2067621/6518153,
\]

and

\[
B_0-3/11=3189372/71699683>0.
\]

This is invariant under deterministic leaf relabeling and common positive time rescaling, so it should certify non-equivalence to source CTCS(4). A small exact checker will verify these finite calculations and basic harmonic identities; the theorem-sized Abel and generator arguments remain written proofs, not checker substitutions.
