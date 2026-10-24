# B14 — exact ordinary-restriction barrier inside the Numaro source slice

**Outcome:** `AUXILIARY_ONLY / SOURCE-SLICE_RESTRICTION_BARRIER`. Full uniform-cube FEI remains **OPEN / NOT PROVED**. Execution is **WITHOUT_VERIFIED_BRAIN**.

## 1. Live target and method change

The live natural-language owner control supersedes the older account03/B14 adaptive-restriction assignment and asks every FEI worker to converge on the all-gate inequality (G): either prove a finite-cap potential works for every Boolean gate, or falsify a proposed gate-extremality claim by an explicit gate and bias. The current read-once fixed-point potential at `C0 = 6.4548` is already falsified by newer peer work, so this run does not try to repair the old AND-extremality claim.

The named peer artifact consumed is:

`proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0055Z-arity10-prime-falsifier/REPORT.md`, blob `d71f08f9a2fd0b417ac7b0cdbac19bacac85c01b`.

It gives an exact balanced composition-prime ten-input restriction `G10` of the recovered eighteen-input Numaro seed with

\[
I(G_{10})=257/128,
\qquad
\frac{H(G_{10})}{I(G_{10})-1}>6.4593722816378554,
\]

hence at uniform bias

\[
c_{G_{10}}>0.0182891265514229
\]

for the read-once candidate, beating the live two-input AND margin `0.0043974201` by more than a factor four. Thus the read-once-\(\Gamma\) / AND-extremality candidate is already `REFUTED`; full FEI is not.

I also consumed account04/B16's exact balanced arity-five theorem,

`proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260922T011015Z-arity5-balanced-exact/REPORT.md`, blob `397a5be2b5c5e9b3ce01823e470297300d919080`,

which proves no balanced-uniform five-input gate can provide the missing stronger obstruction.

This run therefore changed mechanism. Instead of another potential inequality, it asks whether the explicit ten-input prime falsifier can be compressed to smaller arity by **ordinary coordinate restrictions inside its exact source family**.

## 2. Exact candidate version and claim attacked

Use the source-exact Numaro truth table with SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

Write its variables as nine core bits `x0,...,x8` and nine auxiliary bits `y0,...,y8`. Form the complete 256-member family obtained by fixing `y0,...,y7` arbitrarily and leaving

\[
(x_0,\ldots,x_8,y_8)
\]

free. For every member, enumerate **every ordinary coordinate restriction** leaving `k=6,7,8,9,10` local variables free. A descendant is relevant to the balanced-uniform gate falsification target only if it is balanced and depends on every remaining coordinate.

The exact attempted statement was:

> Some ordinary coordinate restriction in this complete Numaro auxiliary-fixing slice yields a balanced essential gate of arity below ten with \(H/(I-1)>6.4559\), hence a smaller balanced-uniform falsifier of the old read-once potential.

This statement is **REFUTED for this source slice**.

## 3. Complete finite enumeration

The checker reconstructs the eighteen-input source from the exact source slices, verifies its SHA-256, and exhausts the family above. Its counts are:

| arity | restrictions | balanced | balanced and essential |
|---:|---:|---:|---:|
| 10 | 256 | 70 | 70 |
| 9 | 5,120 | 0 | 0 |
| 8 | 46,080 | 0 | 0 |
| 7 | 245,760 | 8,960 | 0 |
| 6 | 860,160 | 37,888 | 25,088 |

Thus no balanced codimension-one or codimension-two descendant exists in this complete slice. Balanced seven-input descendants exist, but **every one has at least one dummy coordinate**. The first balanced essential ordinary-coordinate descendants occur at arity six.

For the 70 balanced essential ten-input members, 69 have

\[
\frac{H}{I-1}>6.4559,
\]

and one is below. The maximum is the already identified `G10`; the auxiliary fixing integer is `216`, whose little-endian bits `(y0,...,y7)` are `(0,0,0,1,1,0,1,1)`.

For **all 25,088** balanced essential six-input descendants, the exact maximum is

\[
\boxed{
R_6=\frac{46}{5}-\frac95\log_2 3
=6.347067498701919\ldots
}
\]

with 6,656 equality cases and 18,432 strict cases. There are zero interval-inconclusive comparisons. In particular

\[
R_6<6.4559.
\]

Every equality case has

\[
I=13/8,
\]

and Walsh-square histogram

`16:32, 64:4, 256:4, 576:4`.

Equivalently its entropy is

\[
H=\frac{23}{4}-\frac98\log_2 3.
\]

The logarithm signs are certified with rational atanh-series intervals, so floating point does not decide either the cap comparison or the exact arity-six maximum.

## 4. What is proved, and what is not

**PROVED, finite/source-slice scope:** within the complete family obtained by fixing `y0,...,y7` of the exact Numaro source and then applying arbitrary ordinary coordinate restrictions, there is no balanced essential arity-6 through arity-9 descendant with `H/(I-1)>6.4559`. The obstruction appears at arity ten in this family and cannot be compressed below ten by this restriction mechanism.

**REFUTED, route-specific:** the next natural move “descend the known `G10` obstruction to a smaller balanced-uniform falsifier by ordinary coordinate restrictions of the same exact Numaro slice.”

**NOT PROVED:** arity ten is not shown globally minimal. This enumeration does not cover arbitrary Boolean gates of arity 6--9, and it does not cover the nonuniform-bias or unbalanced-output arity-five region. It does not establish any finite universal FEI constant and does not refute FEI.

## 5. Replacement obligation and next recipient

The remaining falsification search must leave this dead restriction mechanism. The highest-value next targets are a genuinely nonuniform-bias composition-prime five-input gate; an unrestricted composition-prime gate of arity 6--9 not obtained by ordinary restriction of this Numaro auxiliary-fixing family; or a replacement potential \(\Gamma\) with a cap already large enough to accommodate the stronger known balanced lower-bound constructions.

`next_recipient = account04/B16`: its exact arity-five exclusion and proposed nonuniform-bias next attack are directly sharpened by this result. The full-FEI implication is only a search-space reduction: it removes one tempting way to shrink the prime falsifier but leaves the universal all-gate inequality open.

## 6. Reproduction

`CHECKER.py` is the complete enumerator. It verifies the exact source digest, enumerates all restrictions in the table above, tests essentiality, computes Walsh spectra and total influence exactly, and certifies entropy comparisons by rational logarithm intervals. It exited 0 in this run.

Checker SHA-256: `9874489c6dbcd489ffd2e11be9fa2c110f2120f26eb83ece366ba713905a86ec`.

Output SHA-256: `f2efb84ab4feb5827617b3449f7045992e565fce240000692b3240efd85c0c8c`.

No novelty or publication-priority claim is made.
