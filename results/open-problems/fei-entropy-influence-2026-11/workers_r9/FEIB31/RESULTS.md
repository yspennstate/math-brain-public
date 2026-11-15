# FEIB31 results

Task: FEIB31 monotone good-coordinate brief, for the author's 9 Nov 22:20 FEI request.
Started 2026-11-10 12:43 +04.

Every logarithm below is base two unless written ln. E_i/Inf_i is measured in bits
per unit coordinate influence. Constants are ignored when taking a minimum over
coordinates: only coordinates with positive influence are eligible.

## Initial findings (resolved by the checks below)

UNCHECKED: FLOW 12(u) already disproves the maximum-influence rule, using a hidden
coordinate and substitution of balanced majorities into its other coordinates.

UNCHECKED: FLOW 12(y)'s perfect-matching tower is built from gates M and -M. Every
root-to-leaf path crosses the same gate signs, so all leaves have the same monotone
orientation. If this observation is correct, an output complement makes this a
monotone function with the same squared spectrum. Thus the brief's description of
the known 4.50505 tower as non-monotone needs correction. I will rederive this and
compute its value independently before claiming it.

The shared memory helped locate established pitfalls in FLOW; no memory or math
store was modified, and no recall process was started (this is a mathematics brief,
and the brief states that the math store is absent).

## Verified first pass (2026-11-10 12:55 +04)

CHECKED NUMERICALLY: `./search 24 600` evaluated 85,686 candidates in 144 starts,
24 at each n=8..13. Boundary flips and whole-term insertions/removals preserve
monotonicity. The objective is the exact Fourier expression evaluated in double
precision, not a sample estimate. `python3 experiments.py` rebuilt all 144 saved
winners from their DNFs: the largest absolute G discrepancy was
3.4727776210274897e-13 (hill_audit.json). Best hill result: 3.541677755509652,
the OR of six disjoint pairs on 12 variables.

CHECKED NUMERICALLY: experiments.py evaluated 180 cyclic DNFs, 20 at each n=12..20.
The best was 3.428002703877404 at n=20, the cyclic orbit of the term {1,5,9}
(one-based variables). All coordinate influences and erasure costs agree within
the tolerances asserted in the script. Data: cyclic.json.

CHECKED NUMERICALLY: families.json contains connectivity, Hamiltonicity, cliques
and perfect-matching properties on K4, K5, K6, K3,3 and K4,4 wherever the property
is nontrivial. Best graph value: 3.3965247927188287 for perfect matching on K6.
Best directly transformed base overall: the known eight-pair tribes value
3.606847..., with the precise digits in families.json.

PROVED: any level-uniform composition of M and -M is unate with the same direction
at every leaf. Negating the output when necessary produces a monotone function
without changing its squared spectrum. Equivalently, absorb signs into the dual
gate D(x)=-M(-x). The seven-level record is the monotone word M,D,D,M,M,D,D
from bottom to top. Its arity is nine at each level; all leaves are equivalent.

CHECKED NUMERICALLY WITH INTERVALS: `python3 audit.py`, tower_certificate.json,
gives 4.50504996749762792695710133416697266496036181147958908467... at depth seven,
with a directed interval narrower than 3e-78. Thus G_mon > 4.50504996749762.
The function has 4,782,969 variables and an explicit recursive positive DNF;
the two gate DNFs are in checks.json and will be spelled out in PROOFS.md.
This reclassifies an existing fleet example; it is not a new numerical value.

CHECKED NUMERICALLY: audit.py also checked the transform against direct character
sums and influences against edge counts (both errors zero), 20 composition cases
against truth tables (maximum error 2.220446049250313e-16), and 100 independent-guard
identities against truth tables (maximum ratio error 1.3322676295501878e-15).
Data: checks.json.

## Proof results and expanded adversary pass

PROVED: for every leaf of a monotone read-once AND/OR formula,
E_i/Inf_i < pi/ln 2 = 4.5323601418271938096... . This is the sharp supremum
for a fixed leaf over that class, not a claim about the sharp best-coordinate
constant. The proof uses the independent-guard identity and adapts the potential
from the author's FEI19 selector-path proof to the erasure kernel. The previous
kernel has a different integral. Full details and attribution: PROOFS.md Section 3.
class_checks.json independently evaluates the integral and records a family
converging to it; its m=12 member has distinguished-leaf ratio 4.5321828959295285.
Other leaves can be better, so this is not a lower bound of that size for G_mon.

PROVED: width-w DNFs and CNFs, with no read restriction and even without
monotonicity, have min_i E_i/Inf_i < w+3+log2(e). This gives a complete O(w)
answer for this class. It refines the established relative-step method in FLOW
12(v); it does not introduce a new class. PROOFS.md Section 2.

PROVED: a monotone function can have an asymptotic fraction one of its coordinates
with E_i/Inf_i tending to infinity. The middle-layer hidden-bit construction has
two coordinate orbits; its smaller base orbit has much larger influences.
Consequently no universal weighted bound sum_i Inf_i^a E_i <= C sum_i Inf_i^(a+1)
holds for a<0. The single-hidden example plus majority substitution similarly
rules out a>1. The interval 0<=a<=1 remains open. PROOFS.md Sections 4--5.

CHECKED NUMERICALLY: hidden_symmetric.json gives at k=17: 24,310 hidden bits
with ratio 14.451731157696454, and 17 base bits with ratio 2.1426634341909123.
These values are computed exactly in the y spectrum, using Fourier factorization,
with logarithms evaluated as doubles. No huge truth cube was allocated.

PROVED: spectral positive association fails already for x1 OR (x2 AND x3):
P[1,2 in U]=1/8 < (3/4)(1/4). Minimizing the positive-log score is equivalent to
the good-coordinate problem up to 1+log2(e), rather than a proved selection rule.
The class I<=K sqrt(log n) with dummy variables allowed contains every monotone
function after padding. It is therefore not an easier version of Question M.
Details: PROOFS.md Section 6.

CHECKED NUMERICALLY: graph_search, with fixed seed 31022226, added 122 starts,
1,200 proposals each, from graph properties and their duals, extended by an
extra disjoint term when needed. All saved winners were rebuilt and checked in
class_checks.py. No record above the existing direct-transform tribes value
was found. graph_hill.jsonl and class_checks.json retain all DNFs and counts.

CHECKED NUMERICALLY WITH INTERVALS: mixed transitive compositions improve the
old record. record_certificate.json contains the exact words, gate DNFs, every
level's mean and influence, and 100-digit directed intervals. Floating values
at tiny influences drift by about 1e-8, so the report uses interval values.
The close depth-11 through depth-14 contenders have now been compared. The
largest certified value is 4.5064006455155684355071736704529973127..., on
112,844,396,298,240 variables, with interval width 1.1917974432473926069e-85.
It improves the old certified PM record by 0.00135067801794050855... bits per
unit influence. final_audit.json records the exact improvement interval.
The gate word and its recursive positive DNF are in PROOFS.md Section 7.
No claim of global optimality.

Literature is checked in LITERATURE.md, including the requested six author groups,
current November work, the author's read-once paper and internal FEI19/FEI21 proof.
Nothing checked resolves all monotone Shannon FEI. Min-entropy results do not
resolve the erasure question. The full Question M remains open here.

## Final reconciliation

CHECKED NUMERICALLY: `python3 final_audit.py` passes all assertions. The combined
boundary/term and graph searches have 266 starts and 232,208 objective evaluations.
All monotone truth tables through n=5 were generated by ordered cofactor pairs;
counts are 3, 6, 20, 168 and 7,581. The middle-layer identities differ from
direct transforms by at most 4.440892098500626e-16; edge influences agree exactly.

CHECKED NUMERICALLY: the final audit run measured 65,765,376 bytes peak resident
memory for audit.py and 49,119,232 bytes for class_checks.py. Elapsed times and
the inherited nice-10, one-thread settings are in audit_resources.json and
class_checks_resources.json. These are audit measurements, not measurements of
every earlier search. The numerical process designs use at most a 2^20 truth
table (8,388,608 bytes per float64 array). The local folder remains below 60 MB.
The system time utility could not query its resource counters under the sandbox;
the successful measurements use Python's resource.getrusage on macOS instead.

REPORT.md is the final handoff. General monotone FEI and Question M are unresolved.
