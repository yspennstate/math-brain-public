# The Kesten–Stigum bound is sharp for the three-state Potts model on regular trees

Yitzchak Shmalo

This repository contains the paper and the programs behind its computer-assisted steps.

For the ferromagnetic three-state Potts channel on the $d$-ary tree, reconstruction holds if and only if
$d\lambda^2>1$, for every $d\ge2$. Here $\lambda$ is the second eigenvalue of the channel. Sly proved that
the bound is sharp for all sufficiently large $d$; the paper covers every degree.

## Contents

- `paper/q3/main.tex`, `paper/q3/main.pdf`: the paper.
- `code/`: the certificates used in Section 7. Each check has a producer, which writes the certificate, and a
  replay, which reads it and checks it with separate code.

## The checks

Numbering follows the paper.

| Result in the paper | What is checked | Producer | Replay |
|---|---|---|---|
| Lemma 3.2, inequality (CF) | Bernstein positivity of the cubic fusion polynomial | `cubic_invariant_certificate.py` (driver `cubic_invariant_run.py`) | `cubic_invariant_independent_check.py` |
| Lemma 3.2, inequalities (C), (F), (F1) | Bernstein positivity of the cubic and fourth-moment fusion polynomials | `ternary_cubic_certificate.py`, `ternary_fourth_certificate.py` | `ternary_moment_independent_check.py` |
| Proposition 3.4 ($d=2$) | Bernstein positivity of the local polynomial in four variables | `fourth_polynomial_certificate.py` | `fourth_polynomial_independent_check.py` |
| Proposition 3.6, $d\ge3$ | exact constants and finite-law identities | `ternary_local_constants.py`, `three_state_moment_identities.py` | (exact rational arithmetic) |
| Proposition 3.6, $d\ge4$ | the local curve | `local_curve_certificate.py` | `replay_local_curve.py` |
| Proposition 3.6, $d\ge5$, $20$, $80$ | the local radii | `uniform_local_certificate.py` | `replay_selected_local_certificates.py`, `uniform_local_fast_independent_check.py`, `uniform_local_extension_independent.py` |
| Proposition 4.4, Table 1 | the exact belief-propagation upper bounds at the entry depths | `ternary_bp_int.py`, `balanced_bp_fast.py`, `radix_unit_fusion.py`, `universal_fusion.py` with `TernaryBp.cs`, `RegularBp.cs`, `RegularBandBp.cs`, `BalancedBp.cs` | `validate_radix_unit_fusion.py` |
| Lemma 5.1 | Gaussian quadrature for the gap, 96 intervals | `gaussian_gap_arb.py`, `gaussian_gap_dyadic.py` | `gaussian_gap_verify.py` |
| Lemma 5.2 | the replacement constants | `compensated_replacement_constants.py` | |
| Lemma 5.3, the ten inequalities for $F_1$ | Bernstein covers, 68 leaves | `softmax_derivative_certificate.py` | `softmax_derivative_independent.py` |
| Lemma 5.3, the eight inequalities for $Q$ | Bernstein covers, 124 leaves | `fourth_derivative_certificate.py` | `fourth_derivative_replay.py` |
| Proposition 5.6, (12), Lemma 7.1 | the quadrature sums at the 86 endpoints and the gate for $d\ge91$ | `gaussian_fourth_refined_arb.py` | `gaussian_fourth_refined_replay.py`, `verify_compensated91.py` |

Each producer records the SHA-256 of its own source in its output, and the replays check these hashes, so the
programs are kept exactly as they were when the certificates were written, including the status strings they
print.

## Running the checks

The final replay is

    python code/verify_compensated91.py

which reads the endpoint files in `code/gaussian_fourth_gate_refined_v1/` and writes `code/compensated91_gate.json`.

Large intermediate files are not included. The Bernstein stages `bern1` to `bern4` of the fourth-moment
polynomials, and of the polynomial of Proposition 3.4, are rebuilt from the included `raw` files by running the
producer once per stage, in order, for example

    python code/fourth_polynomial_certificate.py --phase bern1
    python code/ternary_fourth_certificate.py --mode prefix --phase bern1

and likewise for `bern2`, `bern3`, `bern4` and for `--mode merge`. The cubic polynomials of (C) need the
stages `bern1` to `bern3` rebuilt the same way with `ternary_cubic_certificate.py --mode upper|lower`. The
replays can then be run.

## Requirements

Python 3.10 or later, with `sympy`, and `python-flint` for the ball-arithmetic steps. The entry
computations of Section 4 are in C# and build with the .NET SDK.
