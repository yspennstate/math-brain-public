VERDICT: PROVED a quantitative weighted residue-transport bound with explicit coefficient discrepancy

The round 4 analytic block estimate holds. Direct pairwise integration
reproduces its variance and predictor identities; the loss coefficient
243/82 and the diagonal-transfer tolerance also check out. The bounded
literature check found no newly verified resolution of the finite-measure
problem. The previously located OpenAI claim remains unverified here.

The new result in [PROOF.md](PROOF.md) is a finite bound for the
residue-density step of a linear-jitter passage. For P residues, slope L,
and passage integer N, it bounds the sum of all folded residue errors by

    E_N + (B-A) J_1/N + J_2/N^2 + P H/(2L) + C_cut.

E_N is the actual coefficient-intensity discrepancy; the next two terms
bound sampling the slow argument; H is a weighted derivative integral;
C_cut is removed mass. Every quantity is defined in the proof. The
sampling terms have no factor P. The estimate allows negative indices,
arbitrary residue offsets, and all positive N, without requiring P to
divide N.

The derivative coefficient 1/2 in the underlying lattice quadrature
bound improves the coefficient 1 used in the inspected neutral-refresh
calculation. Two proofs and smooth extremizing bumps establish that
local coefficient's sharpness. No historical novelty is claimed for
this elementary inequality or for the qualitative residue-balancing idea.

A second bound expresses E_N using the L2 error eta_N between the
exact complex Fourier array and its proposed leading array, together
with an explicit rounding error. It shows exactly how eta_N->0 would
complete this density step. This convergence is not proved or assumed
as an unconditional construction result.

The inspected source is **OpenAI**, *A smooth three-torus diffeomorphism
with simple Lebesgue spectrum*, September 23, 2026; no arXiv identifier
was located. Its [passage section](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/02-passages.tex)
contains the fine-density and neutral-refresh formulas, especially
`neutral-riemann-error`. Its [signal section](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/03-signals.tex)
uses refreshed residues for transmission. These mutable main-branch
sources were opened; no formal proof replay was performed.

Commands and checks are in [LOG.md](LOG.md). Read all three earlier
reports, logs and available proofs; their directories contain no scripts.
Web searches were the exact title and `"Banach" "simple Lebesgue"
"2026" probability`, followed by primary-source opens. Tiny local reads
used `env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '...'`; the sandbox
refused priority adjustment. No numerical computation, script, Lean build,
git operation or external write ran. Files were saved with apply_patch.

What failed or remains uncertain: no contradiction to the geometric
producer was found. This verifies its weighted residue-density mechanism
conditional on a measured coefficient error. It does not certify the
stationary-phase estimate, simultaneous support and physical smooth
control, transmission, or the limiting spectral conclusion. Banach's
finite-measure problem remains unresolved here.

Next worker: prove or refute eta_N->0 for the exact coefficient array
with the retained support cutoffs. The required normalization and the
rounding-removal bound are now explicit in (16)--(18) of PROOF.md.
In particular check uniformity when a stationary point enters or leaves
the coefficient support and summability over all j. After that, audit
simultaneous physical smooth closeness and support tracking before
combining refresh with transmission. Repeating the scalar block or
residue quadrature proofs is unnecessary.

Task: “take the NEXT checkable step on this problem, building on that
work” — received 2026-11-15 approximately 08:13 +04 (Asia/Tbilisi).
