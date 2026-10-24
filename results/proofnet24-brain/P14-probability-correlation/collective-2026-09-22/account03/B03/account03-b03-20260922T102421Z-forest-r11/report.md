# account03/B03 FOREST report — `FOREST-CUBIC-LIFT-DEG4-FINITEDIFF-v1`

Status: `ESSENTIAL_STEP_APPLIED`. Parent target remains **OPEN**. Execution context: `WITHOUT_VERIFIED_BRAIN`.

## Scope and consumed other-account result

This run stays on the exact account03/B03 FOREST assignment: exact structured forest-pair counts / structured adversaries, with logical partner account04/B01. It retains the source measure exactly: the uniform law on **all unrooted forests** (empty forest, disconnected forests, and every forest size included).

Named other-account result consumed directly from current `main`: account04/B01 handoff `FOREST-Q3C-ALL-EDGE-SIMPSON-v1`, creation commit `fdfa4f746b882ce15854ca763cd3d0457ba6471f`, handoff blob `7fb47d48c51a050b2cc085190a65b6e7ef90ee52`. Its load-bearing conclusion is used, not its PASS: if the conjecture fails, after enlarging only the contradiction class to positive-rational weighted loopless multigraphs and choosing a lexicographically minimal witness in `(nonisolated vertices, labelled edges)`, the witness is simple and 3-connected; a violating pair has positive covariance, every third edge is negatively correlated with both members, and the partner obtains the all-edge bound `0<a<1/beta`. The same handoff explicitly leaves as the first missing implication the exclusion of such a rational-weighted simple 3-connected witness.

## Convention

For positive edge activities `y_h`, let

`Z_G(y) = sum_{F forest of G} prod_{h in F} y_h`,

with `Z_e = y_e d_e Z`, `Z_ef = y_e y_f d_e d_f Z`, and

`Delta_G(e,f) = Z_e Z_f - Z Z_ef`.

Thus `Delta >= 0` is exactly pairwise negative correlation. All identities below are identities of the all-forest generating polynomial, not fixed-size or spanning-forest identities.

## 1. Exact weighted cubic lifting lemma

Let `v` have degree three, with neighbours `0,1,2`. Let the incident edges be

- `e=v0` of activity `a>0`,
- `f=v1` of activity `b>0`,
- `g=v2` of activity `c>0`.

Put `H=G-v`, retaining arbitrary positive activities on all edges of `H`. Partition the weighted forests of `H` by the connectivity partition induced on terminals `0,1,2`. Write

- `A = N_{012}`,
- `U = N_{0|12}`,
- `V = N_{01|2}`,
- `W = N_{02|1}`,
- `D = N_{0|1|2}`,
- `T=A+U+V+W+D`.

These are weighted sums over all forests of `H`; components not containing a terminal are allowed and require no special treatment.

Direct star-extension enumeration gives the exact quadratic

`Delta_G(e,f)/(ab) = (A+V)T + 2 c V T + c^2 L`,

where

`L = -A D + U V + U W + V^2 + V W + V D`.

Now use deletion-contraction in the activity `c`. Since `g` is not a loop,

`Z_G = Z_{G\g} + c Z_{G/g}`.

The coefficient of `c^2` in `Delta_G(e,f)` is therefore exactly `Delta_{G/g}(e,f)`. Consequently the preceding display can be rewritten in the much sharper form

> **Cubic lifting identity**
>
> `Delta_G(e,f) = ab(A+V)T + 2abc V T + c^2 Delta_{G/g}(e,f)`.

Every term before the contraction gap is manifestly nonnegative. Hence:

> **Cubic lifting lemma.** If `Delta_{G/g}(e,f) >= 0`, then `Delta_G(e,f) >= 0` for every positive activity `c` and for arbitrary positive activities on the rest of the graph.

This is stronger than the earlier unit-weight cubic-star theorem: only the contraction minor needs to be known good; the third star activity may be arbitrary.

### Consequence for the partner's minimal rational witness

In the account04/B01 minimal positive-rational loopless-multigraph contradiction class, contracting `g` strictly decreases the number of nonisolated vertices. Parallel labelled edges possibly created by contraction remain inside that contradiction class. Therefore `G/g` cannot itself contain a violating pair at the inherited rational weights. The cubic lifting lemma then rules out a violation between two edges incident at any degree-three vertex of the minimal witness.

Combining with the partner's 3-connectivity reduction:

> In a minimal rational-weighted simple 3-connected FOREST counterexample, an **adjacent** violating pair can meet only at a vertex of degree at least four. In particular, if the minimal witness is cubic, every violating pair must consist of vertex-disjoint graph edges.

This attacks the partner's first remaining 3-connected-witness implication without invoking the disputed fixed-host Cocks upgrade.

## 2. Degree-four mechanism change: finite-difference realizability obstruction

To move beyond repeated cubic/separator calculations, this run changed mechanism to finite differences in the two unmarked star activities.

Let `v` have degree four with neighbours `0,1,2,3`, mark `e=v0` and `f=v1`, and put `H=G-v`. For each forest of `H`, let `pi` be its connectivity partition on the four terminals and let `N_pi` be the number (or positive weighted mass) of forests inducing `pi`. For star activities `(1,1,x,y)`, the exact extension response of a fixed partition is

`P_pi(1,1,x,y) = prod_{B in pi} (1 + sum_{i in B} w_i)`.

This formula is exact because a star extension remains acyclic iff at most one selected star edge enters each component-block of the boundary forest.

Let `F_xy` denote the Rayleigh difference for `e,f` after setting `x,y` to the indicated values in `{0,1}`. Exact expansion over the 15 boundary partitions gives:

- `F_00`: 65 positive quadratic monomials, 0 negative, 55 zero;
- `F_10`: 66 positive, 0 negative, 54 zero;
- `F_01`: 66 positive, 0 negative, 54 zero;
- `F_11`: 68 positive, 6 negative, 46 zero.

Thus the degree-four difficulty is a genuinely joint interaction of the two additional star edges: deleting either one makes the adjacent-pair gap coefficientwise nonnegative for arbitrary nonnegative boundary masses.

Define the two finite-difference forms

`R = F_10 + F_01 - F_00`,

`M = F_11 - F_10 - F_01 + F_00`.

Then `F_11=R+M`. Their coefficient profiles are:

- `R`: 75 positive, **2 negative**, 43 zero;
- `M`: 42 positive, **15 negative**, 63 zero.

The two negative monomials of `R` are especially simple:

`R = P_R^+(N) - N_{0123}(N_{0|1|23}+N_{0|1|2|3})`,

where every coefficient of `P_R^+` is nonnegative.

For `M`, writing `P_M^+` for its nonnegative part, the complete negative part is

`-2 N_{0123}N_{0|1|23} -3 N_{0123}N_{0|1|2|3}`

`-3 N_{012|3}N_{0|1|23} -3 N_{012|3}N_{0|1|2|3}`

`-3 N_{013|2}N_{0|1|23} -3 N_{013|2}N_{0|1|2|3}`

`-2 N_{02|13}N_{03|12}`

`-3 N_{02|13}N_{0|1|23} - N_{02|13}N_{0|12|3} - N_{02|13}N_{03|1|2} -4 N_{02|13}N_{0|1|2|3}`

`-3 N_{03|12}N_{0|1|23} - N_{03|12}N_{0|13|2} - N_{03|12}N_{02|1|3} -4 N_{03|12}N_{0|1|2|3}`.

So arbitrary nonnegative partition masses are still insufficient, but the missing realizability content has been compressed into two explicit quadratic boundary inequalities `R>=0` and `M>=0`. Proving both for graph-realizable forest partition vectors would prove the unit adjacent-pair degree-four case immediately.

## 3. Exact exhaustive realizability check through six host vertices

A dependency-free integer checker enumerates every simple graph `H` on the six labelled vertices `{0,...,5}` (terminals `0,1,2,3`; two optional internal vertices), hence all `2^15 = 32768` hosts. It uses a subset-zeta transform over the complete graph to count **all** forest subsets of each host by their four-terminal connectivity partition. Isolated vertices, disconnected forests, the empty forest, and all forest sizes are retained.

Results over all 32768 hosts:

- `M`: 0 negative; 6732 zero; smallest positive 2; maximum 672988;
- `R`: 0 negative; 2504 zero; smallest positive 8; maximum 10270512;
- `F_11`: 0 negative; 2504 zero; smallest positive 8; maximum 10943500.

Thus no source-valid counterexample occurs in the complete degree-four adjacent-pair family obtained from any simple host on at most six vertices (equivalently resulting graphs on at most seven vertices, after harmless isolated vertices are added). This is finite evidence, not an all-graphs proof.

The same checker exhausts all 64 simple four-vertex hosts for the weighted cubic identity, using nontrivial integer activities on host edges and `c in {1,2,5}`. It performs 192 direct weighted all-forest identity checks plus 64 contraction-coefficient checks, all exact integers.

Checker SHA-256: `4b7bbde12e5989265ab1b3dca143e620fbf5cf818f0ba7313636d930a5097e70`.

Expected-output SHA-256: `035b7a61d8eccabe8e362ab235b14711d583a905a08dcaf2b23dfbf60e50b12e`.

## 4. First remaining implication and recommended recipient action

The parent conjecture is still **OPEN**. No source-valid counterexample was found.

The shortest new local target is no longer the raw 15-variable degree-four gap. It is the pair of graph-realizability inequalities

`R(H)>=0` and `M(H)>=0`

for the four-terminal forest partition vector of an arbitrary host `H`. `R` has only two negative monomials, so it should be attacked first by a weight-preserving two-forest exchange/injection. If `R` is established, attack the 15-term negative part of `M` by the same exchange with the crossing partition types `02|13` and `03|12` separated explicitly.

Recipient: account04/B01 and the FOREST lead. Combine this with `FOREST-Q3C-ALL-EDGE-SIMPSON-v1`: the rational minimal witness is already simple and 3-connected; the cubic lifting lemma removes adjacent violations at degree-three vertices, while `R/M` isolate the next degree-four adjacent obstruction. A graph-realizable violation of either inequality is also a high-value structured adversary to test directly for a true FOREST counterexample.

No full-proof, public-solution, priority, or novelty claim is made from this report.
