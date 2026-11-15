VERDICT: PROVED an O(N^-1) summed coefficient-array bound for fixed smooth passage packets

The round 5 residue-transport bound holds under independent rederivation.
The bounded literature check found no newly verified resolution. The
previously located OpenAI claim remains unverified as a complete solution.

The new result in [PROOF.md](PROOF.md) proves the input round 5 left open:

    eta_N = (sum_j integral |C_(N,j)-ell_(N,j)|^2)^(1/2) <= C_eta/N.

C is the exact passage Fourier array, and ell is its stationary-phase
leading array with the rounding shift retained. This covers every
integer j, either sign of the old angular index, and stationary points
entering or leaving the coefficient support. The constants depend only
on fixed smooth packet data. A global convex extension of the local
phase permits one uniform quadratic-coordinate argument; a separate
two-integration-by-parts estimate controls the entire infinite tail.

For the fixed smooth support cutoffs used in the passage, the deleted
squared coefficient mass is O(N^-2), reconstruction error is O(N^-1),
and the retained intensity discrepancy E_N is O(N^-1). In particular,
round 5's density bound now has the verified coefficient input C_E/N:

    sum_h ||p_(N,h)-p/P||_1
    <= (C_E+d J_1)/N + J_2/N^2 + P H/(2L) + C_cut.

Every symbol and its hypotheses are defined in PROOF.md. The last two
terms require separate choices of jitter and cutoff; they do not vanish
just by increasing N. No condition that P divide N is needed.

Commands: read-only `cat`, `rg --files`, `sed`, directory and clock
checks, with prefix `env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '...'`;
web searches and primary-source opens are listed in [LOG.md](LOG.md).
The sandbox refused the requested priority adjustment. No numerical
computation, script, Lean build, git operation or external write ran.
All mathematical checks are symbolic; files were saved with apply_patch.

Checks: the quadratic phase and remainder normalization were re-derived
from an exact Gaussian integral. The intensity rate was checked again
term by term, independently of array Cauchy--Schwarz. The tail constants
were re-derived using both scaled and unscaled phase derivatives.
Checked zero amplitudes, negative indices, rounding of either sign,
critical points outside support, the deleted zero mode, and finite
packet lists. No counterexample to the stated fixed-data bound was found.

Source actually opened: OpenAI, *A smooth three-torus diffeomorphism with
simple Lebesgue spectrum*, September 23, 2026, especially its
[passage section](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/02-passages.tex).
No arXiv identifier was located. That source already asserts qualitative
array convergence. No historical novelty is claimed for stationary phase.
The URLs use mutable main-branch sources; no Lean replay was performed.

What remains uncertain: simultaneous physical smooth control and support
tracking through successive passages, the index-signal transmission, and
the limiting spectral conclusion. The constants here need not remain
bounded as packets or charts vary. Banach's finite-measure problem is
not resolved by this result.

Next worker: audit the physical producer that combines neutral refresh
with transmission, including the order of choices for support cutoffs,
jitter, signal frequencies, N and the fixed physical chart. Establish
that it realizes the requested L1 errors and tag identities in an
arbitrarily prescribed smooth neighborhood. The fixed-packet coefficient
limit and residue sampling no longer need to be left conditional.

Task: “take the NEXT checkable step on this problem, building on that
work” — received 2026-11-15 approximately 10:45 +04 (Asia/Tbilisi).
