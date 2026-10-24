Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding model/effort selector is exposed.

# G0011 artifact — endpoint-capture theorem, extremal obstruction, and deferred-exposure closure criterion

Date: 2026-09-18 UTC.
Owner: R7-07; native ID `6aabe8413f60819197825dd81ca138ae`.
Target: `G0011`, HARD OUTSIDE: the Krivelevich–Samotij long-cycle conjecture as restated by Christoph–Morawski–Wigderson, arXiv:2608.19145v1, current Conjecture 6.1.
Methods in this run: **B3 (prove something stronger), B22 (read the failures / extremal constructions), B14 (find and exploit the symmetry / exchangeability)**.
Frozen metric: `K_long`, currently `1 <= K_long <= 2`.
Status of this artifact: **PARTIAL / source OPEN**.

## 1. Recovered setting from the preceding R7-07 run

The cumulative cross-core laboratory has a deterministic bipartite incidence graph `J=(A,B)` and constants `r,s,c>0` with

\[
\deg_J(a)\ge r d^2\quad(a\in A),\qquad
\deg_J(b)\ge s d\quad(b\in B),\qquad
p=\frac c d.
\]

After bond percolation and an independent uniform maximum matching on every open witness neighborhood, the previous run produced a properly witness-colored projection `Gamma` on `A`. With probability `1-O(d^{-1/2})` as `d->infinity`, a subgraph `Gamma'` has

\[
\delta(\Gamma')\ge \kappa d/5
\]

for an explicit constant `kappa=kappa(c,r,s)>0`. A rainbow projected path of length `Omega(d)` follows and lifts to a simple alternating path in the physical percolated bipartite graph. The unresolved step was to obtain a rainbow projected cycle of length `Omega(d)`.

The previous endpoint lemma said that a longest rainbow path with no long rainbow cycle exhibits endpoint-color capture. This run sharpens that statement to an exact deterministic circumference bound and then tests whether the random matching origin is strong enough to defeat the capture mechanism.

## 2. B3 — an exact endpoint-capture circumference theorem

Let `G` be a properly edge-colored simple graph. Let

\[
P=v_0v_1\cdots v_\ell
\]

be a rainbow path, and write

\[
C(P)=\{\chi(v_{i-1}v_i):1\le i\le \ell\}.
\]

Call `P` **terminally maximal at** `v_ell` if there is no edge `v_ell w` with `w` outside `V(P)` whose color is not in `C(P)`. This is weaker than saying that `P` is a longest rainbow path: only extension from the displayed endpoint is forbidden.

Define the endpoint capture number

\[
h(P,v_\ell)
:=
\#\{e\in E(G): v_\ell\in e,\ \chi(e)\in C(P)\}.
\]

Properness implies that each used color contributes at most one edge at `v_ell`, hence `h(P,v_ell)<=ell`.

### Theorem 2.1 — endpoint capture controls rainbow circumference

Suppose `P` is terminally maximal at `v_ell`, put

\[
D:=\deg_G(v_\ell),\qquad h:=h(P,v_\ell),
\]

and assume `D-h>=2`. Then `G` contains a rainbow cycle of length at least

\[
\boxed{D-h+1.}
\]

#### Proof

Put

\[
L:=D-h+1.
\]

First note that terminal maximality forces `ell>=L-1`. Indeed, every edge at `v_ell` whose color is not in `C(P)` must end in `V(P)`. There are `D-h` such fresh-color edges. The predecessor `v_{ell-1}` is already joined to `v_ell` by the path edge, whose color lies in `C(P)`, so a fresh-color simple edge cannot use that same endpoint. Hence there are at most `ell-1` possible endpoints for fresh-color edges inside the path, giving

\[
D-h\le \ell-1.
\]

Thus `L<=ell`.

Assume for contradiction that there is no rainbow cycle of length at least `L`. Consider a fresh-color edge

\[
v_\ell v_i,\qquad \chi(v_\ell v_i)\notin C(P).
\]

If

\[
i\le \ell-L+1,
\]

then the suffix

\[
v_i v_{i+1}\cdots v_\ell
\]

uses pairwise distinct colors from `C(P)`, while the chord color is outside `C(P)`. Therefore

\[
v_i v_{i+1}\cdots v_\ell v_i
\]

is a rainbow cycle of length

\[
\ell-i+1\ge L,
\]

contrary to assumption. Hence every fresh-color edge at `v_ell` must go to one of

\[
v_{\ell-L+2},\ldots,v_{\ell-2},
\]

which gives at most `L-2` possible fresh-color edges. Consequently

\[
D\le h+(L-2)=h+(D-h+1)-2=D-1,
\]

a contradiction. Therefore a rainbow cycle of length at least `D-h+1` exists. ∎

### Corollary 2.2

If a terminally maximal rainbow path in a properly colored graph ends at a vertex of degree at least `delta` and has endpoint capture at most `h`, then the rainbow circumference is at least

\[
\delta-h+1.
\]

In particular, for the preceding cross-core target, **it is enough to produce one terminally maximal rainbow path endpoint with**

\[
h=o(d).
\]

The cycle length would then be `(kappa/5-o(1))d` in the projected graph and twice that in the physical bipartite graph.

This is stronger and cleaner than the preceding `ell >= delta-L+2` certificate: it isolates a single scalar obstruction.

## 3. B22 — deterministic rotation alone cannot work

A natural hope after Theorem 2.1 is that properness, minimum degree, and the fact that every color class is a matching might force `h=o(delta)`. That hope is false in the strongest possible way.

Alon, Bucić, Sauermann, Zakharov and Zamir, *Essentially tight bounds for rainbow cycles in proper edge-colourings* (Proc. LMS 130 (2025), e70044), Observation 9.1, construct properly edge-colored regular graphs with **no rainbow cycle at all** from dissociated subsets of groups. In the even-order version of their construction, after deleting every other edge on each color-cycle, every vertex is incident to exactly one edge of each color. Therefore:

- the graph is `q`-regular;
- there are exactly `q` colors;
- every color class is a perfect matching;
- there is no rainbow cycle.

Thus even the model local structure

> regular graph + proper coloring + every color class a perfect matching

is insufficient to force a rainbow cycle, let alone one of length `Omega(delta)`.

The endpoint-capture theorem diagnoses exactly how such examples evade closure. Since they have no rainbow cycle, any terminally maximal rainbow path endpoint must have essentially all of its incident colors already captured by the path. In particular, a purely deterministic Pósa/rotation statement that only sees properness, degree, and matching color classes cannot close `MATCHING-RB-CLOSE`.

What distinguishes the R7-07 projection is not the matching property by itself but **independence/exchangeability across the witness matchings and independent Bernoulli activation of endpoint-witness incidences**. Any successful proof has to use that randomness before the adaptive path can select an extremal capture configuration.

## 4. B14 — exact exchangeable matching probabilities

Fix a witness `b` after percolation and let its open neighborhood have size

\[
K_b=k.
\]

The R7-07 projection chooses a uniformly random maximum matching on that open neighborhood. For two distinct open vertices `x,y`, the exact probability that they are paired is

\[
\rho(k)=
\begin{cases}
1/(k-1),&k\text{ even},\\
1/k,&k\text{ odd}.
\end{cases}
\tag{4.1}
\]

For odd `k`, this follows because a uniformly random maximum matching is equivalently obtained by choosing one unmatched vertex uniformly and then a uniform perfect matching of the remaining `k-1` vertices; direct counting gives pair probability `1/k`.

Since witness matchings are independent across different `b`, a fixed candidate rainbow cycle has an exact product probability. Namely, for distinct vertices

\[
v_0,\ldots,v_{m-1}
\]

and distinct witnesses

\[
b_1,\ldots,b_m
\]

such that both endpoints of the `i`th candidate edge lie in the open neighborhood of `b_i`,

\[
\Pr_M\bigl(\{v_{i-1},v_i\}\in M_{b_i}\ \forall i\mid H\bigr)
=
\prod_{i=1}^m \rho(K_{b_i}),
\tag{4.2}
\]

with indices modulo `m`.

Thus the matching-origin coloring is an independent product of exchangeable local involutions, unlike the algebraically coordinated dissociated-group construction from B22.

Equation (4.2) is useful, but a direct first-moment sum is not yet enough: the host neighborhoods may be extremely irregular, and the source quantifiers allow arbitrarily large ambient order. The more robust use of independence is at a *deferred endpoint*.

## 5. Deferred endpoint-capture lemma

Return to the original deterministic incidence graph `J=(A,B)` and Bernoulli bond percolation with `p=c/d`. Let

\[
P=v_0\cdots v_\ell
\]

be a rainbow projected path with distinct witness colors

\[
C(P)=\{b_1,\ldots,b_\ell\}.
\]

Let `x=v_ell` be its final endpoint. For a used color `b_i` to contribute an incident projected edge at `x`, the physical incidence edge `xb_i` must be open. Therefore, irrespective of the matching rule,

\[
\mathbf 1\{x\text{ is incident to projected color }b_i\}
\le
\mathbf 1\{xb_i\text{ is open in }J_p\}.
\tag{5.1}
\]

Now suppose a sigma-field `F` determines the path skeleton, its used colors, and all information needed to certify terminal maximality with respect to **fresh** colors at `x`, but for the old colors

\[
b_1,\ldots,b_{\ell-1}
\]

the Bernoulli variables

\[
\mathbf 1\{xb_i\text{ open}\}
\]

remain unexposed and independent of `F`. (The entering path color `b_ell` is necessarily incident at `x` and is treated separately.)

Then, conditionally on `F`,

\[
\boxed{h(P,x)\ \preceq\ 1+\operatorname{Bin}(\ell-1,p).}
\tag{5.2}
\]

This is an exact stochastic domination, because (5.1) bounds every old-color capture indicator by its independent endpoint-witness Bernoulli incidence.

### Corollary 5.1 — linear-length paths have sublinear deferred capture

Assume

\[
\ell\le A d,
\qquad p=\frac c d,
\]

for a fixed constant `A`. Put

\[
H_d:=\lceil d^{1/3}\rceil.
\]

The binomial mean in (5.2) is at most `Ac`. Hence the standard binomial tail bound gives

\[
\Pr\bigl(h(P,x)\ge 1+H_d\mid F\bigr)
\le
\left(\frac{eAc}{H_d}\right)^{H_d}
=
\exp\bigl(-\Omega(d^{1/3}\log d)\bigr).
\tag{5.3}
\]

Combining Theorem 2.1 and (5.3), if in addition

\[
\deg(x)\ge \delta_d,
\]

then with conditional probability

\[
1-\exp\bigl(-\Omega(d^{1/3}\log d)\bigr)
\]

the graph already contains a rainbow cycle of length at least

\[
\boxed{\delta_d-d^{1/3}.}
\tag{5.4}
\]

For `delta_d>=kappa d/5`, this is `Omega(d)`.

## 6. The obstruction is now an adaptivity/deferredness gluing problem

The preceding theorem turns the old vague phrase “endpoint-color capture” into a much sharper statement.

If one can construct a path-selection rule satisfying all three properties

1. `P` has length `O(d)`;
2. its endpoint `x` has projected degree `Omega(d)` and is terminally maximal with respect to fresh colors;
3. the old endpoint-witness incidences `xb_i`, `i<ell`, are still deferred when `x` is selected,

then the long rainbow cycle follows immediately from (5.2)–(5.4).

The previous global core `Gamma'` certifies property 2 only after looking at the full realized projection. A longest path chosen inside that globally selected core can therefore adapt to precisely the rare endpoint-capture events that (5.3) makes negligible for a deferred endpoint. This is the exact missing bridge:

\[
\boxed{\texttt{DEFERRED-MAXIMAL-ENDPOINT}.}
\]

> Build (or certify the existence of) a terminally maximal rainbow path of length `O(d)` whose final endpoint retains an `Omega(d)` degree certificate while its incidences with the previously used witness colors remain unexposed.

B22 shows that removing the word “deferred” makes the statement false even for regular graphs whose color classes are perfect matchings. B14 shows that once deferredness is available, the capture obstruction collapses from order `d` to order `O(d^{1/3})` with superpolynomially small failure probability.

## 7. Why this is substantive but does not move `K_long`

This run does not prove `DEFERRED-MAXIMAL-ENDPOINT`, does not resolve the fixed-`d` / host-order quantifier issue, and therefore does not prove the full source conjecture. The source metric remains

\[
\boxed{1\le K_{\rm long}\le2.}
\]

with no movement.

The advance is structural:

- the cycle-closing problem is reduced to one scalar capture number `h`;
- deterministic proper-color/matching arguments are ruled out by a known sharp obstruction;
- under a precise deferredness condition the capture number is binomial with bounded mean and the long cycle follows quantitatively;
- the only remaining cross-core bridge is to reconcile degree certification / terminal maximality with deferred old-color endpoint incidences.

This is a materially narrower handoff target than the preceding generic `MATCHING-RB-CLOSE` formulation.

## 8. Dated literature check — 2026-09-18

1. Christoph–Morawski–Wigderson, arXiv:2608.19145v1, *The critical probability for percolation on finite graphs*, still surfaces as the current source record dated 2026-08-19. The concluding long-cycle statement remains presented as a conjecture and is attributed to Krivelevich and Samotij.
2. Hollom, *Finding Long Cycles in Percolated Expander Graphs*, Random Structures & Algorithms 68 (2026), e70070, proves long cycles under expander/minimum-degree type structure and explains the use of DFS plus sprinkling; it does not settle arbitrary average-degree hosts.
3. Alon–Bucić–Sauermann–Zakharov–Zamir, Proc. LMS 130 (2025), e70044, prove the essentially tight ambient-order-dependent rainbow-cycle threshold and give the dissociated-group lower-bound construction used in B22.
4. Kim–Lee–Liu–Tran, Combinatorica 44 (2024), 909–919, give earlier `O(log^2 n)` rainbow-cycle bounds; these are likewise ambient-order dependent.
5. Bounded exact-title / exact-statement / author searches on 2026-09-18 did not recover a later paper explicitly resolving the full average-degree `(1+epsilon)/d` long-cycle conjecture. This is negative evidence only, not a novelty certificate.

## 9. Next mathematical target if G0011 were ever reopened by an authorized successor

Do **not** return to generic rainbow-cycle rotation. The specific unresolved lemma is `DEFERRED-MAXIMAL-ENDPOINT`. Three plausible routes are:

- reserve a locally generated degree certificate that does not inspect old endpoint colors;
- use two-stage/sprinkled witness exposure so path selection and old-color endpoint incidences are separated;
- formulate a stopping-time version of the projected-degree lower bound stable under adaptive endpoint selection.

Any future proof must also repair the fixed-`d` quantifier, not merely the `d->infinity` laboratory.
