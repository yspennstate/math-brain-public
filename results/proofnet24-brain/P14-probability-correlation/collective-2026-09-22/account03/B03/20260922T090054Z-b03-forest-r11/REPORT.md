# FOREST degree-four realizability-deficit theorem

Run: `20260922T090054Z-b03-forest-r11`  
Account/slot: `account03/B03`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Context: `WITHOUT_VERIFIED_BRAIN`  
Outcome: **ESSENTIAL_STEP_APPLIED**. The parent FOREST conjecture remains **OPEN**; no public solved-problem, priority, or novelty claim is made.

## Assignment and named partner result consumed

The exact B03 row asks for exact forest-pair counts on structured adversaries, using failures to derive the missing structural constraint rather than producing a census-only report. The assigned partner is `account04/B01`.

This run directly read the completed `account04/B01` report at commit `3b53272eba18cdec04e029651173b1410e3b8b12`. Its exact two-vertex-separator transfer identities, together with the independently checked fixed-host Cocks weighted upgrade, imply that any edge-minimal simple counterexample to the unit uniform-forest conjecture must be 3-vertex-connected. I use only that mathematical conclusion; the peer's PASS is not substituted for any new argument below.

The previous B03 cubic-star theorem then says that in such a 3-connected candidate a violating adjacent pair cannot be two edges incident to a cubic vertex. The first local adjacent-edge case not disposed of by that mechanism is therefore a degree-four vertex. This run changes mechanism to a full four-terminal partition expansion.

## Exact four-terminal boundary representation

Let `G` be a finite simple graph with a vertex `v` of degree four and distinct neighbours labelled `0,1,2,3`. Mark

`e0=v0`, `e1=v1`,

and let `H=G-v`. For each forest `F` of `H`, let `pi(F)` be the connectivity partition induced on terminals `{0,1,2,3}`. There are 15 set partitions. Write `N_pi` for the number of forests of `H` inducing partition `pi`.

All forests are retained: the empty forest, disconnected forests, and every size. There is no rooting and no conditioning on the number of components.

For a fixed `H`-forest of terminal partition `pi`, adding a subset of the four star edges remains acyclic iff at most one chosen star edge terminates in each block of `pi`. Therefore its exact star-extension polynomial is

`P_pi(x0,x1,x2,x3) = product_{B in pi} (1 + sum_{i in B} x_i)`.

At unit star weights define

- `w_pi = P_pi(1,1,1,1)`,
- `a_pi =` number of allowed extensions containing `e0`,
- `b_pi =` number of allowed extensions containing `e1`,
- `c_pi =` number of allowed extensions containing both.

If `B0,B1` are the blocks containing terminals 0 and 1, then exactly

`w_pi = product_B (1+|B|)`,

`a_pi = w_pi/(1+|B0|)`, `b_pi = w_pi/(1+|B1|)`,

and

`c_pi = 0` when `B0=B1`, otherwise `c_pi=w_pi/((1+|B0|)(1+|B1|))`.

Thus the source Rayleigh difference is the exact quadratic form

`Delta = Z_0 Z_1 - Z Z_01`,

where

`Z=sum_pi N_pi w_pi`, `Z_0=sum_pi N_pi a_pi`, `Z_1=sum_pi N_pi b_pi`, `Z_01=sum_pi N_pi c_pi`.

No approximation is used.

## New theorem: the entire negative support is a 2-by-3 product

Expanding the quadratic form in the 15 nonnegative variables `N_pi` gives 120 unordered quadratic monomials. Exactly 68 have positive coefficient, 46 have zero coefficient, and only six have negative coefficient. The six are

- coefficient `-4` on `N_{0|1|2|3} N_{0123}`,
- coefficient `-4` on `N_{0|1|2|3} N_{02|13}`,
- coefficient `-4` on `N_{0|1|2|3} N_{03|12}`,
- coefficient `-3` on `N_{0|1|23} N_{0123}`,
- coefficient `-3` on `N_{0|1|23} N_{02|13}`,
- coefficient `-3` on `N_{0|1|23} N_{03|12}`.

Consequently there is an exact decomposition

`Delta = P_+(N) - (4 N_{0|1|2|3} + 3 N_{0|1|23})`

`                 * (N_{0123} + N_{02|13} + N_{03|12}),`

where `P_+(N)` is an explicitly determined quadratic polynomial whose every coefficient is nonnegative. The checker computes every coefficient from the closed formulas above; no symbolic package is required.

This is the useful obstruction. The degree-three theorem succeeded from nonnegativity of boundary masses alone. Degree four cannot: the abstract nonnegative vector

`N_{0|1|2|3}=1`, `N_{0123}=1`, all other `N_pi=0`

gives `(Z,Z_0,Z_1,Z_01)=(21,9,9,4)` and hence `Delta=-3`.

That vector is **not asserted to be graph-realizable**. Rather, it proves that any degree-four local proof must use genuine realizability relations among terminal-connectivity counts. Treating the 15 partition masses as arbitrary nonnegative variables is provably insufficient.

## First missing structural inequality

The exact remaining local obligation can now be stated without ambiguity:

> For every graph-realizable four-terminal forest partition vector `N`, prove that the positive part `P_+(N)` dominates
> `(4 N_{0|1|2|3}+3 N_{0|1|23})(N_{0123}+N_{02|13}+N_{03|12})`.

Equivalently, a source-valid degree-four adjacent-edge counterexample must realize a partition vector violating this inequality. This identifies the exact three high-connectivity classes and two low-connectivity classes that a counterexample search or injection must exploit.

The natural next proof mechanism is therefore not another raw graph census: construct an injection or weighted double-counting from pairs in those six bad products into the positive-coefficient pairs, using edge deletions along terminal paths in the corresponding `H`-forests. The partition formula tells the receiving account exactly which terms must be paid.

## Exact finite source-valid stress test

To check whether the abstract obstruction appears in actual small graphs, a deterministic standard-library program exhausts every simple graph `H` on six labelled vertices, with `0,1,2,3` designated terminals. There are `2^15=32768` such `H`. For each one it counts **every** forest by terminal partition via exact integer subset-zeta transforms and evaluates the source Rayleigh difference after adjoining a new degree-four vertex `v` connected to terminals `0,1,2,3`.

Results:

- all 32,768 `H`: negative gaps = `0`; zero gaps = `2504`; minimum gap = `0`;
- among the `5744` cases for which the resulting seven-vertex graph `G` is 3-vertex-connected: negative gaps = `0`; zero gaps = `0`; minimum gap = `5384`.

The minimum 3-connected witness has

`E(H)={(0,4),(0,5),(1,2),(1,3),(2,5),(3,4),(4,5)}`

and `(Z,Z_0,Z_1,Z_01)=(1094,462,400,164)`, giving `Delta=5384`.

This finite computation is evidence and regression, **not** a proof of the all-graphs conjecture. Its value is that the six-term abstract obstruction does not immediately materialize in any degree-four adjacent-pair source graph through seven total vertices, while the symbolic expansion explains what a larger counterexample would have to do.

## Relation to the partner's all-graphs reduction

The consumed `account04/B01` result forces any edge-minimal counterexample to be 3-vertex-connected. Combined with the prior B03 cubic theorem and the present degree-four expansion, an adjacent violating pair in a minimal counterexample must now pass a sharply constrained local test:

1. it cannot sit at a cubic vertex;
2. at a degree-four endpoint, its four-terminal partition vector must overcome the explicit nonnegative remainder `P_+` using only the six bad cross-products above.

This does not close the parent conjecture. It replaces a vague degree-four obstacle by an exact realizability inequality and gives a source-valid counterexample criterion.

## Reproducibility

Deterministic checker: `degree4_boundary_checker.py`  
Checker SHA-256: `21c647043de1b3cf558c4676099bc2d1bd60e7d44230907cdef18e74a4038009`  
Core output SHA-256: `81804fdf4b41a2f17270c11e5a09bc4cfbeeda1e118508ed665125f9f1e88c85`

The checker separately verifies the six negative coefficients, the abstract negative vector, all 32,768 six-vertex boundary graphs, and all 5,744 3-connected seven-vertex star extensions.

## Status and recipient

Result identifier: `FOREST-DEG4-REALIZABILITY-DEFICIT-v1`.

Parent target status: **OPEN**. No source-valid counterexample was found. No internal candidate is promoted to a public theorem about all graphs.

Recipient / next attack: `account04/B01` and the FOREST lead. Use the exact six-term deficit to seek a graph-realizability injection/double count; alternatively search directly for a realizable `N` violating the displayed inequality. The 3-connected reduction should remain active throughout that search.
