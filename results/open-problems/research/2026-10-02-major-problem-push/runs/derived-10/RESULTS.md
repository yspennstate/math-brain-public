# Derived checkpoint10: spectral-center slab FEI and exact proof-method boundaries

2 October2026 UTC. Parent master0aa4e8c56c0f1faf06597c59a8e857cf0b94d1a9.
Old files are preserved. Only this campaign's CURRENT.md changes in place.
Full new immutable bundles and this run's content-hash manifest are included.

## Complete positive FEI extension

Read the [entire final proof](../../../../proofnet24/P03-fei/continuations/2026-10-02-parity-slabs/parity_modulated_slabs_center_proof.md),
the complete K and root analytic audits, and its source/check records.
For every uniform-cube parallel slab g, arbitrary real defining weights,
all endpoint conventions, and J(g)=sum_i min(I_i,1-I_i),

H(g)<=(C_slab+60)J(g).

Here C_slab is the already proved ordinary slab constant. Every parity
modulation of g consequently satisfies ordinary FEI with that same new
constant; its parity may overlap every input and have unbounded degree.
The argument is new relative to the prior all-LTF parity theorem: slabs
can have multiple high influences and the older I-Var budget is not
comparable to J. Exact two-bit parity proves that failed comparison.

The full proof supplies universal Delta H<=2h2(I_i)<=4I(f), a complete
edge-isoperimetric induction with physical-flip normalization, fixed-
coordinate entropy gluing, at most15 high slab coordinates by Chow and
Parseval, and the final centered-function restriction argument. The
terminal restrictions alone use ordinary slab FEI; intermediate functions
need not be ordinary slabs. Constants/J=0 are handled without division.

Wide-gap unions with arbitrarily narrow components have the explicit
centered constant C_union+4(16r^2-1), where
C_union=r C_slab+log2(e)(1+1/e). A separate generic closure lemma for
Boolean combinations of at most m unate gates retains an explicit
ordinary-FEI and restriction-closure premise. It does not prove ordinary
FEI for arbitrary intersections of halfspaces or shared-input circuits.

Both full independent analytic audits pass. Root reran the actual checker:
65,814 Boolean functions/262,948 pivots,3,951 slabs and61,396 character
checks. Integer flip/Walsh/Chow assertions are exact; entropy tests are
numerical corroboration of the analytic proof. The separate new exact
local-method failure is a genuine TWO-crossing slab: its largest-weight
pivot has influence1-2^-N but its entropy increment divided by2^-N
diverges. Thus Delta<=C min(I_i,1-I_i) cannot prove the theorem. Root
read and reran its full checker:7 realizations,33,125 Fraction coefficient
assertions over250 odd dimensions,50 high-precision Decimal entropy checks.
The analytic divergence proof, not those logarithmic tests, proves failure.

## Exact operator-method obstruction, not a Sidorenko counterexample

Read the [complete operator-boundary derivation](../../../../proofnet24/C30-sidorenko/continuations/2026-10-02-operator-boundaries/continuation_20261002_operator_boundaries.md)
and its complete independent ant audit. Classical Perron/Hölder tools give
rho(M(t))<=rho(A)^(2(1-t))||A||_F^(2t)<=tr(M(t)) in Rossman's actual
interpolated family. This valid upper bound supplies only the total
excluded-trace endpoint, not the required odd fifth-moment lower bound.
Its self-contained proof is included; historical novelty is not claimed.

The strictly positive rational nine-state matrix
B=J-(3/20)I+(17/20)S has the appropriate exchange symmetry, full-rank
six-positive/three-negative inertia, sector entrywise domination and
positive Perron-excluded trace. Yet its excluded fifth moment equals
-43193/20000. Its exchange entry37/20 exceeds the maximum17/10 allowed
by every product-family parameter inferred from its diagonal, so it lies
OUTSIDE Rossman's actual family. This rules out a generic spectral
shortcut, not Rossman's conjecture or Sidorenko.

Root read the full note, scripts and independent audit and reran both
exact obstruction/check scripts. The independent rational eigenbasis,
sector blocks, fifth power, product exclusion and direct ladder/trace
normalization agree. Separate numerical gradients agree to5.5e-11.
All saved search outputs remain numerical evidence only. The audit
explicitly records an incorrect sign in a search-code COMMENT whose
implemented objective is correct, and clarifies that a radial gradient
test occurs once per script invocation. Original files are preserved.

## Three-crossing route: verified negative result and honest gap

Read the [complete candidate/status note](../../../../proofnet24/P03-fei/continuations/2026-10-02-three-crossing-boundary-route/three_crossing_component_comparison_candidate.md)
and [full trace reduction](../../../../proofnet24/P03-fei/continuations/2026-10-02-three-crossing-boundary-route/three_crossing_trace_candidate.md).
Weights(33,34,36,40,48), cuts(-34,0,34) give
I=11/8, both component sums23/8, ratio23/11>2. Root read and reran the
standalone exact reconstruction. This refutes tentative constant2,
not existence of a larger universal comparison.

The abstract increasing-region majority/dictator construction has
unbounded comparison ratio but cannot be realized by four ordered
intervals of a common positive linear score, as explicitly proved.
Therefore monotone-region geometry alone is insufficient. The middle-
threshold boundary trace identity and implication are rigorously derived:
if I(H)Var_(nu_H)(f)<=2I(f), then min component sums<=3I(f), which would
give the three-crossing FEI extension from the completed slab/union input.
The trace inequality itself remains UNPROVED. The307,503 triple-cut tests
on81 weight families are exact finite evidence, not a proof. Their
maximum trace ratio3/2 is not claimed as a global bound.

## Completion boundary

The spectral-center slab/character result is complete internally; the
operator and boundary failures are complete subsidiary obstructions.
Historical priority and external specialist review remain unverified.
General Boolean FEI, arbitrary nearby three-crossing FEI, full forest
pair/NA, unrestricted ML10 and Kaplansky/direct finiteness remain open
in this campaign. New regular-three-state, adjacent-terminal and bounded-
ascending-path candidates require their own independent completion records.
