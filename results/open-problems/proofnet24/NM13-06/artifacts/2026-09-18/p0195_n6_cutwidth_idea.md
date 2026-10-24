# P0195 connected-n=6 low-temperature / cutwidth route — idea before checker

Date: 2026-09-18 UTC
Track: `proofnet24/NM13-06`
Source: P0195, LPW Ising spectral-gap edge-addition clause
Frozen metric: `n_edge^* >= 6`

This note records the mathematical route before any new finite checker is written.

The previous run reduced every minimal counterexample to a connected source graph. At order six, 399 connected marked edge-addition types remain after the already certified dense source class. The next three fresh Section-B moves are #7, #13, #26.

## #7 TAKE THE LIMIT

Try the low-temperature limit `beta -> infinity`. A natural energy-barrier statistic is graph cutwidth. Existing canonical-path results bound the Ising relaxation time in terms of cutwidth, so the first question is whether an edge addition has a strictly larger barrier statistic and whether a theorem is strong enough to transfer that barrier comparison to the exact spectral gap.

Important honesty constraint: a one-sided relaxation-time bound in terms of cutwidth is not an exact asymptotic and cannot by itself prove the LPW edge-addition inequality. No low-temperature spectral-gap claim is made unless a matching theorem or direct capacity comparison is actually recovered.

## #13 FIND WHAT ONLY INCREASES

For a fixed vertex ordering, adding one edge weakly increases every cut size, hence weakly increases the ordering's maximum cut. Taking the minimum over all orderings shows that graph cutwidth is monotone under edge addition. This is a true graph-theoretic monovariant. It is not yet a Glauber-gap monovariant.

Use an exact six-vertex isomorphism census only to answer the route-selection question: among the 402 connected marked edge-addition types, how often does cutwidth rise strictly and how often is it tied? The checker will certify only this combinatorial statement.

## #26 HUNT THE SPORADIC CASE

Isolate the exact cutwidth-tie types, because they are the cases where the proposed low-temperature barrier statistic cannot even distinguish source from target. In particular, identify the densest tie class. If the frozen metric does not move, this gives a concrete simplest special case for the mandatory Section-I stuck-recovery invocation that follows a third unchanged run.

No numerical spectral scan, floating-point eigenvalue comparison, or cutwidth computation will be reported as proof of spectral-gap monotonicity. Any finite claim from this run will have an exact integer/isomorphism checker and archived output.
