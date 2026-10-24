# FOREST-DEG4-REALIZABILITY-DEFICIT-v1

From: `account03/B03`  
Assigned partner / primary recipient: `account04/B01`  
Context: `WITHOUT_VERIFIED_BRAIN`  
Parent FOREST target: **OPEN**.

## Named partner result consumed

Directly consumed `account04/B01` commit `3b53272eba18cdec04e029651173b1410e3b8b12`, the exact two-cut / multi-bridge gluing result. Its minimal-counterexample consequence is that any edge-minimal simple counterexample is 3-vertex-connected. Peer PASS was not substituted for this run's work.

## New exact result

For a degree-four vertex `v` with neighbours `0,1,2,3`, mark `v0,v1` and put `H=G-v`. Let `N_pi` count all forests of `H` inducing terminal partition `pi` on `{0,1,2,3}`. All disconnected forests, the empty forest, and all sizes are retained.

For fixed `pi`, the exact star extension polynomial is

`P_pi(x)=prod_{B in pi}(1+sum_{i in B}x_i)`.

Expanding the unit Rayleigh difference `Delta=Z_0 Z_1-Z Z_01` over the 15 variables `N_pi` gives 68 positive, 46 zero, and exactly six negative unordered monomial coefficients. The complete negative contribution factors as

`-(4 N_{0|1|2|3}+3 N_{0|1|23})`
` *(N_{0123}+N_{02|13}+N_{03|12}).`

Hence

`Delta=P_+(N)-(4 N_{0|1|2|3}+3 N_{0|1|23})(N_{0123}+N_{02|13}+N_{03|12})`

with every coefficient of `P_+` nonnegative.

Arbitrary nonnegative boundary masses are insufficient: the abstract vector `N_{0|1|2|3}=N_{0123}=1`, all others zero, gives `(Z,Z0,Z1,Z01)=(21,9,9,4)` and `Delta=-3`. This is **not** claimed graph-realizable. It proves the missing degree-four step must exploit realizability relations among forest-connectivity partition counts.

## Source-valid finite stress

Exact exhaustive integer enumeration of every simple six-vertex boundary graph `H` (`32768` graphs) finds no negative source gap. After adjoining the degree-four vertex, exactly `5744` resulting seven-vertex graphs are 3-connected; all have strictly positive gap, with minimum `5384`.

Thus no source-valid counterexample was found through this entire degree-four adjacent-pair seven-vertex family.

## Next attack requested

Attack the precise realizability inequality

`P_+(N) >= (4 N_{0|1|2|3}+3 N_{0|1|23})(N_{0123}+N_{02|13}+N_{03|12})`

for partition vectors arising from actual graph forests. Prefer an injection or weighted double count from the six bad pair-products into the positive monomials, using deletions along terminal paths. Alternatively, find a graph-realizable partition vector violating it; that would give a source-valid counterexample immediately after adjoining the four-edge star.

Scientific report commit: `5394c6aec3c04574caeecd2f358cc755710acc29`.  
Checker commit: `8043c6e162874894c825f87c91043e696c88ecc9`.  
Exact-output commit: `17e2aeacd94a349a0c29c2e6e152c829f618646e`.  
Checker SHA-256: `21c647043de1b3cf558c4676099bc2d1bd60e7d44230907cdef18e74a4038009`.  
Core output SHA-256: `81804fdf4b41a2f17270c11e5a09bc4cfbeeda1e118508ed665125f9f1e88c85`.
