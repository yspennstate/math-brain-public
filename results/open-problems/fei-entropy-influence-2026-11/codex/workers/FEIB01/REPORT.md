# FEIB01 blinded referee report

All five formal statements in the permitted NOTES.md are valid, with the
boundary conventions and real-valued extension stated in `PROOFS.md`.
Proposition 4 admits the stronger universal bound `B <= A + 2 Gamma`.

Theorem 1 — PROVED. The empty-set summand is treated separately. The exact
equality characterization is in `PROOFS.md`: apart from constants, f must
be balanced, and every supported nonempty S must have all its restricted
coefficients either zero or the same signed value `2^(1-|S|)`.

Proposition 4 — PROVED. Both upper bounds, `Gamma<=B/2`, and `P<=A` hold.
Its upper bounds are not sharp as written: `B<=A+2Gamma` improves the second,
and the conditional-magnitude refinement in `PROOFS.md` improves the first.
The coefficient one-half in the Gamma bound is attained with B>0; the
coefficient one in P<=A is approached by odd majority.

Lemma 2 — PROVED. The proposed nu is a probability measure; the exact
slack is relative entropy. The general-kernel version includes infinite
right sides when its kernel gives zero probability to a supported S.

Lemma 3 — PROVED with `B(g)=sum ghat(S)^2 log(up_g(S)/ghat(S)^2)` for real g,
without normalizing its squared Fourier coefficients. Zero coefficients
contribute zero to J even when its displayed denominator vanishes.

Balanced disjoint-block composition — PROVED. The proof explicitly handles
the empty outer Fourier set and constant outer functions. It also gives
the unequal-balanced-block law. Balance is required: composing AND_2 with
AND_2 has B=0.7324877755992936 bits, whereas the formula applied without
balance would give two bits (`composition_real.log`). This refutes only
the extension with its balance hypothesis removed.

The informal “Jensen ... false by sqrt(n)” sentence — GAP IN SPECIFICATION.
It states no inequality, lambda, or comparison. The actual Jensen upper
bound written in `PROOFS.md` is valid. Its measured looseness on majority
is in `majority_levels.json`; no asymptotic verdict on the unspecified
sentence is claimed.

## Equality, sharpness, and coefficients

The four-variable census has 578 Theorem 1 equality functions in seven
input/output symmetry classes (`census4.log`, `census_analysis.json`).
The original first Proposition 4 bound has ten equality functions there:
the two constants and eight signed dictators. The proofs characterize
these cases in all dimensions.

The coefficient two multiplying I in Theorem 1 is best possible. The
balanced Boolean function

    q=(x1*x2+x2*x3+x3*x4-x1*x4)/2

has A=2 bits, B=0 bits, I=2, Var=1. Its r-fold disjoint-block self-composition
has I=2^r, A=2(2^r-1) bits, and B=0, so `(A-B)/I -> 2` bits per influence
unit. AND_n gives a second family with the same limit. Both are proved;
their exact formulas and high-precision evaluations are in
`precision_audit.json`.

The positive equality witness for Gamma<=B/2 is

    (1-x*y+x*z+y*z)/2,

with B=1/2 bit and Gamma=1/4 bit. Its embedded four-variable truth table
is 0x03c0 (`precision_audit.json`). The majority limit P/A->1 is proved
in `PROOFS.md`, rather than inferred from finite numerical values.

There is a tradeoff between coefficients, so there is no unique best tuple.
For nonnegative a, the complete observed four-variable frontier for
`A<=a B+b I` is

    b_4(a)=max(1,31/16-beta*a),
    beta=7/8+(49/16)log2(8/7)=1.4649755511985874... .

The breakpoint is 0.6399424203584647... . The 80-digit independent audit
of the 212 distinct normalized census constraints is in
`precision_audit.log`. These are finite-census results. Universally,
`(a,b)=(1,2)` is proved; b=2 is optimal for every a>=1, by the iterated
zero-B family. The full universal frontier for a<1 is not determined.

For `B<=a' A+b' I+c' Gamma`, the complete census answer is the upper
envelope `b'=max(0,max_f[B/I-a' A/I-c' Gamma/I])`. The 212 representative
constraints and their 15-row compression are saved in
`coefficient_constraints.json` and `coefficient_frontiers.json`.
`PROOFS.md` prints the compressed region and useful slices. In particular,
`(a',b',c')=(1,0,2)` is proved in every dimension, and b'=0 is optimal
at those fixed a',c' because dictators require b'>=0. Other displayed
census optima are not claimed universally.

The census optimum for the coefficient of I-Var in
`B<=d(I-Var)+P+2Gamma` is d=0.13657007572574492..., at truth table 0x0796
(`census_analysis.json`). Its optimal value over all dimensions remains
open in this report; the dimension-dependent improvement is proved.

## FEI equivalences, including constants

These quantify over every Boolean function in every dimension.

- FEI with `H<=C I` implies `B<=C I`. A universal `B<=K I` implies
  `H<=(2K+2)I-2Var`, hence FEI with constant 2K+2.
- FEI with constant C implies `A<=C I` and `Gamma<=C I/2`.
  Universal bounds `A<=alpha I` and `Gamma<=gamma I` imply FEI with
  constant `2alpha+2gamma`, by the strengthened proposition.
- With the same constant K in both proposed conjectures, the implication
  to FEI gives 4K. The source's unstrengthened proof would give 1+4K.

These implications do not resolve FEI or supply the conjectured universal
bounds on B or Gamma.

## Computation and audit trail

Every verifier was written in this folder from scratch. No code from the
source's code directory was read. The exact function counts and numerical
residuals below are in `final_audit.json` and the named experiment logs.

| Check | Scope | Saved output |
| --- | --- | --- |
| Boolean census | All 65,536 four-variable truth tables; all recursion coordinates; three rational lambda values; general coding kernel | `census4.csv`, `census4.log` |
| Random Boolean functions | 1,200,000 draws; 100,000 for each of n=5,6,7,8 and negative-output biases 0.5,0.2,0.05 | `random.log`, `random_summary.csv` |
| Composition on every random draw | Entire grouped expanded spectrum for balanced mux substitution; exact integer mass and probabilities | `random.log` |
| Structured functions | 91 instances, including zero-dimensional constants, AND, OR, strict majority, tribes, address, parity times AND, and bent functions on four and six variables | `structured.csv`, `structured.log` |
| Independent full-table composition | 143,942 outer/inner pairs, including every four-variable outer and every balanced four-variable inner | `composition_real.log` |
| Real-valued recursion | 262,306 coordinate checks; rational-valued functions, zero g, zero a, zero d | `composition_real.log` |
| Independent census audit | Integer Walsh matrix and direct face sums for every census function; 80-digit audit of normalized constraints | `census_analysis.log`, `precision_audit.log` |

Random draws are with replacement and are not asserted distinct. Every
random draw checks all five statements, with one rotating coordinate for
recursion and lambda=1/2 for coding. Large random composition uses an exact
grouped spectral expansion; it does not allocate or transform a full
3n-variable truth table. The independent full-table composition suite
checks the factorization used by that grouped calculation.

Integer arithmetic verifies Walsh coefficients, direct restricted-coefficient
energies, the local inequalities, and coding normalizations. Final logarithms
use double precision, with 2e-10 absolute tolerance in their weighted bit
units; the second audit uses 80 decimal digits. Maximum discrepancies were
1.1102230246251565e-15 bits for the independent census metric calculation,
2.842170943040401e-14 bits for full-table composition B,
9.059419880941277e-14 bits for full-table composition H, and
3.469446951953614e-16 squared-amplitude bits for real recursion
(`final_audit.json`). Tiny negative floating slacks in the additional
conditional-Cauchy bound are recorded in the logs; the exact local
inequalities and proofs handle their signs.

An early real-recursion test had an erroneous factor of four in comparing
integer transform numerators. The independently derived common-denominator
calculation corrected the harness; the saved complete rerun passed.

The structured process inherited niceness 10 and its measured peak resident
size was 188,219,392 bytes (`resource_check.json`). An initial attempt to
increase niceness further was refused by the sandbox; all computations
retained the inherited 10. C++ experiments use one thread. Python numerical
audits were launched with OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1.
The folder remains far below its one-gigabyte limit; `final_audit.json`
records the measured file bytes.

## Reproduction

Compile `referee.cpp` and `composition_real.cpp` with
`c++ -O3 -std=c++17 -Wall -Wextra`, naming the executables `referee` and
`composition_real`. Then run, in order:

    ./referee census > census4.log
    ./referee random 100000 > random.log
    ./referee structured > structured.log
    ./composition_real > composition_real.log
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 analyze_census.py > census_analysis.log
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 precision_audit.py > precision_audit.log
    python3 audit_results.py > final_audit.log

The existing `resource_check.json` was produced by the Python subprocess /
getrusage wrapper shown in the command transcript. The final consistency
audit reads that resource record and the other saved outputs. It does not
rerun the experiments. NumPy, SciPy, and mpmath are needed for the Python
audits; the C++ programs have no third-party dependencies.

No startup memory, brain, recall, mesh, checklist, or compute-state file was
read or called. The only explicit file reads outside the workspace were
the required ../../RULES.md and the NOTES.md expressly allowed by BRIEF.md.
All writes were inside this workspace. No external publication occurred.

Final saved-output consistency audit: PASS (`final_audit.json`).

Task: “act as a hostile referee of Theorem 1, Proposition 4, Lemma 2, Lemma 3
and the composition law in NOTES.md.” Request clock time was not supplied;
first recorded local time was 2026-11-10 01:10:43 +04.
