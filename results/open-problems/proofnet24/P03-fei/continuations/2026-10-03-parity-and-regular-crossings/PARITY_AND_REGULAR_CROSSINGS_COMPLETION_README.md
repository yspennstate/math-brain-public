# FEI continuation: parity outputs and regular finite crossings

Read the full proofs and audits, not this summary alone.  All statements use
the uniform Boolean cube, base-two Fourier entropy (including the empty
atom), and physical bit-flip influence.  These are restricted subsidiary
theorems; unrestricted Boolean FEI remains open.

## Strongest ordinary finite-crossing result

`input_regular_balanced_finite_crossing_fei_candidate.md`, together with its
fresh independent audit, proves ordinary FEI for every fixed finite number
of genuine crossings of one weighted score when

* `max_i |w_i| <= B ||w||_2/sqrt(n)` for fixed `B`, and
* both output labels have probability at least a fixed `r0>0`.

Crossing locations and spacings are arbitrary, the crossing count may be
even or odd, and individual weights may be zero or arbitrarily small.  The
new step extracts two protected opposite-label score intervals from the
Gaussian mass forced by output balance, then applies a localized signed
translation identity between them.  Uniform block resampling gives an
`Omega(sqrt(n))` influence lower bound, while established halfspace-noise
machinery gives `O(sqrt(n))` entropy.  The endpoint/CDF comparison uses the
actual half-open/closed label sets; open interiors are used only for their
equal Gaussian measure.  The author checker includes exact even-crossing
translation identities and 35,259 balanced truth-table cases.  This result
does not give a constant uniform as `r0` tends to zero or `B` tends to
infinity.

The separately preserved
`input_regular_moderate_bias_odd_crossing_fei_proof.md` is an incomparable
ordinary theorem: it permits arbitrarily biased output, but requires an odd
number of crossings whose normalized locations are bounded.  It removes all
minimum-weight and crossing-separation assumptions.  Its full independent
heat audit, author mask audit, and three exact checkers are supplied.

## Output-character theorems

`output_parity_unate_gate_combinations_logarithmic_proof.md` proves, for
`g=F(g_1,...,g_m)` with arbitrary outer Boolean `F` and unate gates that may
share inputs and use unrelated orientations,

    H(chi_T g) <= [log2(4m^2+2q)+3] I(chi_T g),
    q=n-|T|.

Full output parity has constant `2 log2(m)+5`.  The underlying universal
form replaces `m` by an upper bound on the Euclidean norm of the influence
vector.  The weak `O(log n)` FEI input is established prior work; the file
includes a complete elementary Gibbs derivation to retain the empty Fourier
atom and fix constants.  Author and independently implemented checkers pass
1,053,853 and 4,366 principal exact finite comparisons, respectively.

`output_parity_bounded_alternation_fei_proof.md` gives the separate path
theorem

    H(chi_T g) <= 4 cot^2(pi/[2(m+q+2)]) I(chi_T g)

when `g` changes sign at most `m` times on every ascending cube path.  It
therefore covers arbitrary-spaced finite-crossing scalar scores under a
nearly full output character.  For a unate `g` and full parity it gives the
sharp constant 2.  Its independent analytic audit and 1,051,466 finite
function/character checks pass.  The earlier quadratic gate-count proof is
retained and explicitly marked superseded by the logarithmic theorem.

## Failed three-crossing routes retained honestly

The trace route reduces the missing middle-crossing inequality to the exact
four-flux inequality `4xy <= o^2+2t(x+y+o)`.  No proof or counterexample to
that actual inequality was obtained.  A generic common-score trace theorem
is disproved by a complete family with exponentially diverging ratio, and
score-ordering does not make the cube noise kernel TP2 (an exact `-3/32`
minor is supplied).  Exhaustive positive integer weights `1,...,8` through
dimension eight cover 47,693,379 triple cuts, with maximum observed actual
trace ratio `3/2`; this is finite evidence only.

The full-retention construction proves that all three crossings can remain
genuine in both largest-weight restrictions while the local entropy-split
ratio diverges.  A direct signed-halfspace decomposition can also lose an
unbounded factor.  These are proof-method obstructions, not FEI
counterexamples.  The known lacunary/superincreasing derivation is credited
as prior-class coverage and is not promoted as a new result.

## Reproduction and source status

Run the supplied standard Python scripts from this directory.  The principal
fresh commands are:

    python verify_input_regular_balanced_finite_crossing.py
    python verify_input_regular_odd_crossing_heat.py
    python verify_input_regular_odd_crossing_mask.py
    python verify_regular_moderate_bias_odd_crossing.py
    python verify_output_parity_unate_gate_combinations_logarithmic.py
    python verify_output_parity_logarithmic_heat.py
    python verify_output_parity_bounded_alternation.py
    python three_crossing_trace_k_route_obstructions.py
    python verify_three_crossing_direct_entropy_heat.py
    python three_crossing_routes_ant_independent_check.py

The precise primary-source check is in
`finite_crossing_and_parity_source_check.md`.  KOS, CKLS, Berry--Esseen,
weak logarithmic FEI, the regular-LTF and symmetric-function overlaps are
credited.  Recent September 2026 plateaued-function work and May 2026
stopping-tree work were inspected and concern distinct subclasses.  No
bounded search can certify originality.  Historical priority and external
specialist review remain unverified.
