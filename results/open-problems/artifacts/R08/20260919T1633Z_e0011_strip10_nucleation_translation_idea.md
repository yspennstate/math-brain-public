# R08 E0011 — new-method note before production certificate: sharp thin-strip nucleation threshold and oriented fuel-rail translation

Run: 2026-09-19 UTC. Methods selected from the preceding report: **B3 / B15 / B19**.

Entering frozen metric: `B_cat >= b21_desc`, diagnostic `log10(b21_desc) ~= -48.42893853604687`; supported unchanged count entering the run is `2`.

The controlling target is still `operations/claims/E0011.md` (Durrett 2009 Problem 5, original no-stirring catalyst/ZGB model). Hasebe--Ueda `I0082` remains RETIRED/FROZEN at `2/3`; it is not reopened.

## B3 — strengthen the seed question until it has a sharp finite threshold

The previous run identified `2 x 8` as the first rectangular bare-vacancy seed that simultaneously beats the single direct all-CO path and has positive initial vacancy drift. That is still too weak: the right local question is whether the *entire closed pure-state jump chain* reaches a stable mixed CO/O state before either monochromatic poison with probability greater than `63/64`.

For a closed `2 x w` rectangle started all vacant at `p=1/2`, before the first mixed state the configuration is necessarily one of three types: empty, CO-only, or O-only. Hence the exact pre-mixing process has only `1+2(2^(2w)-2)` transient states. Reaction-choice denominators are at most products of lattice degrees and can be cleared by a fixed branch scale `144`.

The production checker will prove two complementary statements with downward-rounded exact integer Bellman recursions:

1. for every `w <= 8`, monochromatic poison is hit by at most 19 effective adsorptions with probability already `>1/64`, so no `2 x w` closed strip with `w<=8` can possibly have eventual mixed-before-poison probability `>63/64`;
2. for `w=9`, a stable mixed state is hit before poison by at most 35 effective adsorptions with probability `>63/64`.

This makes `w=9` the exact thin-strip threshold for this closed local nucleation criterion, rather than merely a heuristic enlargement of the `2 x 8` strip.

## B15 — break symmetry on purpose: use all-CO surroundings as fuel, not only as an adversary

Odd width `9` is locally minimal for nucleation, but an even strip has a new deterministic transport mechanism. Take a `2 x 10` vacant strip, place a CO rail immediately above it, keep the two lateral neighbours of the top vacant row vacant, and keep a second CO rail above the first. For each of the five disjoint horizontal top-row edges

`(0,1)-(1,1), (2,1)-(3,1), ..., (8,1)-(9,1)`, 

an O2 adsorption has, at each endpoint, a unique CO neighbour directly above. Instantaneous reaction therefore removes exactly the two corresponding CO-rail particles while leaving the two adsorption sites vacant. If the five designated O2 events occur with no destructive mark on the protected support, in any order, the first CO rail has been converted into a full vacant row. The vacant strip has shifted upward by one row; the second CO rail is now the fuel rail for the next shift.

Thus a finite stack of CO rails gives an explicit deterministic oriented vacancy-transport algorithm. This is deliberately asymmetric: it turns the previously worst all-CO exterior into consumable propagation fuel. Width `10` is the first even width at or above the sharp local nucleation threshold `9`, and the production checker will also record that the closed `2 x 10` strip already exceeds the `63/64` mixed-nucleation threshold within 19 effective adsorptions.

This is not yet a source-valid high-probability two-child block: the clean five-edge rail-consumption word is still too rare if every other mark is killed. The point of the construction is to identify the correct finite automaton for the next restart/minorization attack: state = `(vacancy strip, consumed-fuel subset, local pure/mixed flag)` rather than a prescribed global cylinder.

## B19 — exact finite algorithm

Implement one production C++ checker for the pre-mixing pure-state jump chain on `2 x w` rectangles. It will compute rigorous lower bounds on either (a) hitting poison or (b) hitting a stable mixed state within a specified number of effective adsorptions. Every value is stored on the grid `10^-9`; each Bellman average is floored, so every printed target probability is a certified lower bound. The finite claim is worth certifying because it changes the architecture sharply; no source-metric movement will be claimed unless a complete two-child 1-dependent block certificate is also obtained.

The next source-level missing object is therefore not another seed-size scan: it is a restart/minorization automaton that allows ordinary strip events to return to the oriented seed class while keeping the fatal-to-success ratio below `1/63`.
