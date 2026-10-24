# Root independent audit: spectral-center slab FEI

2 October 2026 UTC. **PASS for the stable final proof and all its explicitly
stated corollaries.** Root read the entire candidate, separate final proof,
K's complete independent audit, actual full checkers, and exact/numerical
outputs. The earlier ordinary slab and wide-gap union proofs were already
fully inspected in this campaign. Root independently rederived the new
argument below and reran both new checkers successfully. This is an internal
audit, not external specialist review or a certificate of historical novelty.

## Universal gluing and normalization

For any signed Boolean split f=A+x_iB, Parseval makes the pair masses
P_S=Ahat(S)^2+Bhat(S)^2 a probability law. The exact restricted entropy
calculation gives Delta=sum P[1+h2(q)-h2(r)], with q=b^2/P and
r=(a+b)^2/(2P). Both the empty Fourier atom and all coefficient signs
are included. The positive even series for 1-h2((1+x)/2), whose
coefficients sum to one, proves h2(t)>=4t(1-t). Since
r(1-r)=(1-2q)^2/4, one obtains Delta<=2 sum P h2(q)<=2h2(I_i).
Zero pair masses are omitted without a limiting or division problem.

For minority density p, every i-pivotal undirected edge has one minority
endpoint, so I_i<=2p in the physical-flip convention. The fully reproduced
edge-isoperimetric induction yields I>=2p log2(1/p); its two sections and
cross-boundary factor are correct. For p<=1/4, h2(I_i)<=h2(2p)<=
2p[log2(1/p)+log2(e)]<=4p log2(1/p)<=2I. For p between1/4 and1/2,
2p log2(1/p)>=1 and h2(I_i)<=1. Therefore Delta<=4I for every Boolean
conditional function. This is a total-influence bound; it is not the
unproved or false local bound by the pivot's centered influence.

Revealing any fixed b coordinates telescopes full entropy. At every depth,
the expected remaining influence equals the original sum over unrevealed
coordinates, hence is at most the original I. Thus H<=average terminal H
+4bI. If the terminal restrictions satisfy ordinary FEI with C, one gets
H<=(C+4b)I. Intermediate centered functions need not be ordinary slabs.

## Centering and the high-coordinate count

A slab is a Boolean combination of two endpoint halfspaces in a common
coordinate orientation. A slab flip implies a flip of at least one
endpoint predicate. Chow and Parseval give sum I_i(h)^2<=1 for each
endpoint halfspace; Cauchy-Schwarz yields sum I_i(g)^2<=4. Every
strictly high coordinate has I_i>1/2, so there are strictly fewer16,
at most15. Coordinates exactly one half are not selected. Endpoint ties,
single attained-score slabs, rays and constants remain valid endpoint
predicates. No unateness of the slab is assumed.

Multiplication by the character on precisely those high coordinates
preserves entropy and realizes J=sum min(I_i,1-I_i). After these coordinates
are assigned, the character is an output sign and the remaining base
function is a slab restriction. Apply universal gluing to the centered
function, and ordinary slab FEI only at the leaves, to obtain

H(g)<=(C_slab+60)J(g).

Every other character modulation has influence at least J and the same
entropy. J=0 is handled directly: the centered function has zero influence
and is constant on the connected cube. The proof makes no division by J.

## Extensions and their precise premises

The conditional restriction-class closure C+4b is correct for any ordinary
FEI class with a uniformly bounded number b of high coordinates. For at
most m genuine common-score crossings, sum I_i^2<=m^2, so b<=4m^2-1.
Ordinary FEI for arbitrary nearby crossings is retained as a premise,
not silently concluded.

The wide-gap union class already has ordinary FEI with
C_union=r C_slab+log2(e)(1+1/e). Restriction translates its intervals and
can only decrease the remaining largest weight, preserving the strictly
wide separating gaps. There are at most2r endpoint predicates, hence
b<=16r^2-1. Therefore the displayed C_union+4(16r^2-1) centered bound
is valid even when the component intervals are arbitrarily narrow.

The separate bounded-unate-combination conditional lemma also checks:
for any Boolean combination of at most m unate gates, possibly with
different coordinate orientations and shared inputs, I_i(g)<=sum_r I_i(h_r)
and |hat h_r({i})|=I_i(h_r). Parseval gives the same m^2 square bound.
The lemma explicitly assumes ordinary FEI and restriction closure of its
base class; it supplies no ordinary theorem for arbitrary halfspace
combinations or shared-input circuits.

## Full failure proof and verification

The two-bit middle-layer slab has I-Var=1,J=0,H=0. It disproves a general
comparison of the older budget with J but is consistent with the theorem.
The new two-crossing local obstruction has branches -majority and
majority+2 times the all-minus indicator, with pivot influence1-2^-N.
It is the old three-crossing function times the pivot character, so its
entropy increment is identical. Root independently checked the majority
central-layer coefficient formula, the Vandermonde/log-concavity lower
bound, the exact even-degree contribution2epsilon, and the odd-degree
entropy lower bound. The final ratio grows at least as
(N+3)/2-log2[N(N+1)/2]. Thus a local bound by min(I_i,1-I_i) fails even
for slabs. The successful global proof never needs it.

Root reran the generic/slab checker:65,814 Boolean functions,262,948 pivots,
3,951 slab instances and61,396 character checks. Physical flips, integer
Walsh permutations and Chow-square bounds are exact; entropy comparisons
are numerical checks on a complete analytic argument. Root also reran the
separate local obstruction checker:7 truth-table realizations,33,125 exact
Fraction coefficient assertions over250 odd dimensions, and50 high-
precision Decimal entropy checks. Decimal logs are numerical, not exact
symbolic entropy certificates.

No full Boolean FEI, arbitrary polynomial-threshold theorem, arbitrary
nearby-crossing theorem, nonuniform-input result or shared-input circuit
result is inferred. All stated final-proof additions are continuous with
the candidate and the independently audited upstream ordinary theorem.
