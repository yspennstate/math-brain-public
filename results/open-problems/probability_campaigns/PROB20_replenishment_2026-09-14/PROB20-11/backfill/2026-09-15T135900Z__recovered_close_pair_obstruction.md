# PROB20-11 recovered checkpoint — close-pair obstruction

**Recovered provenance:** mathematical content from an earlier completed PROB20-11 task response on 2026-09-15 that was not durably archived in the requested task root. This file is a backfill, not a claim that the earlier GitHub write succeeded. The task root was absent when the present run began.

**Original status: PARTIAL.**

## Target and certified bracket

For
\[
M_{12}=\max_{A\in\{\pm1\}^{12\times12}}\min_{\varepsilon\in\{\pm1\}^{12}}\|A\varepsilon\|_\infty,
\]
we had the exact bracket
\[
M_{12}\in\{4,6\}.
\]
The upper bound \(M_{12}\le6\) follows from the exact union bound
\[
12\,\Pr(|S_{12}|\ge8)=12\cdot 158/4096<1,
\]
while a Paley Hadamard matrix of order 12 was exhaustively checked over all \(2^{11}\) signings modulo global negation to have discrepancy exactly 4.

The value 6 is equivalent to 12 antipodal row classes covering the folded quotient
\[
G=\mathbb F_2^{12}/\langle\mathbf1\rangle,
\qquad |G|=2048,
\]
with folded radius-3 balls. Each such ball has size 299.

## Parity geometry

Because length 12 is even, parity is well-defined on antipodal quotient classes. A folded radius-3 ball contains 67 quotient points of the same parity as its center and 232 of the opposite parity. A necessary parity split for a 12-center cover is therefore between 2+10 and 10+2.

Call a center pair **close** if its folded distance is at most 4. A non-close same-parity pair has distance 6, and a non-close opposite-parity pair has distance 5.

Exact pair intersections are
\[
J_1=134,\;J_2=134,\;J_3=62,\;J_4=62,\;J_5=20,\;J_6=40.
\]
The earlier exhaustive quotient calculation also established the triple-intersection data needed for third Bonferroni estimates, including the variable-orbit types \((2,5,5)\) and \((4,5,5)\), whose triple intersections are either the stated high value or zero.

## Recovered structural theorem

Third Bonferroni, applied with exact pair and triple data, ruled out a 12-center cover with zero close pairs and then with exactly one close pair.

For exactly two close pairs, the coarse third-order relaxation left only a rigid family of same-parity distance-2 edge patterns. Exact finite geometry/high-triple searches eliminated those survivors. The recovered conclusion was:
\[
\boxed{\text{Every hypothetical 12-center folded radius-3 cover has at least three close center pairs.}}
\]
No solver timeout was used as an infeasibility certificate.

## Exactly-three-close-pair frontier recovered from the earlier response

Before quotienting by all graph/parity symmetries, the exact third-Bonferroni relaxation left 46 raw assignments, split by close-edge graph shape as:

- triangle: 14;
- three-edge matching: 24;
- length-2 path plus a disjoint edge: 6;
- path of length 3: 2;
- three-star: 0.

Those raw counts were not realizability claims. The next attack recorded in the earlier response was to quotient these survivors by graph automorphisms/parity exchange and then perform exact stabilizer searches.

## Recovery gaps

The earlier response referred to a companion exact source file, but that file was not present in the repository task root when the present run began. This backfill therefore archives only the mathematical writeup that is recoverable from the completed task response. New reproducible code is being reconstructed in the current run.
