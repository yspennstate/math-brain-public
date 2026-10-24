# Complete eight-state Boolean convolution certificate

The mathematical authority is continuation_20261002_cube8_sidorenko_FINAL.md,
with the complete independent cube8_k_independent_audit.md and
cube8_root_full_audit.md. All three agree: for every nonnegative eight-vector
p on the uniformly measured Boolean group F2^3, W(x,y)=8p(x+y) satisfies
t(ML10,W)>=(sum p)^15. Signed Fourier spectra are allowed. This proves only
the stated finite convolution-host family. General ML10 remains open here;
historical novelty and external specialist review are unverified.

The original pre-audit proof is preserved unchanged, including its earlier
creation status. The FINAL copy and complete audits supersede that status.
All failed stronger assertions are preserved and labeled as such. Numerical
smoothing and optimization do not enter the proof.

## Complete data, with no coefficient sampling

The archive contains all 53 original completed files, including all 89,168
host coefficients, every 3,964 Fourier coefficient, all 170,406 raw-gap
coefficients, every 345,312 positive multiplier coefficient, and separately
generated full maps. It also contains all generators, proofs, audits,
coverage data, failed approaches and the prior Klein-four dependency used
by one exploratory route. No executable binaries are included. Larger data
are archived rather than truncated or replaced by summary statistics.

From this directory, concatenate and verify the exact archive:

    cat cube8_exact_data.tar.xz.part01 cube8_exact_data.tar.xz.part02 > cube8_exact_data.tar.xz
    sha256sum cube8_exact_data.tar.xz

Expected SHA256:
222736d82ae16243010d557a6e425cca5660b470744bd3313c2263b83dedffac
Compressed bytes: 15,761,088. Original file bytes: 79,144,580.
EXACT_ARCHIVE_MANIFEST.json gives each original file's length and SHA256,
each part's hashes, and Git object hashes. Every archived byte was checked
by reopening the archive. GitHub's returned part blob hashes independently
match the local Git object hashes, verifying the uploaded binary bytes.

Extract into an empty work directory; paths intentionally retain the
original sidorenko_attempt/ directory expected by the author scripts:

    mkdir -p /tmp/cube8-reproduction
    tar -xJf cube8_exact_data.tar.xz -C /tmp/cube8-reproduction
    cd /tmp/cube8-reproduction
    python sidorenko_attempt/continuation_20261002_cube8_coverage.py
    g++ -O2 -std=c++17 sidorenko_attempt/continuation_20261002_cube8_vertex_polynomial.cpp -o /tmp/cube8-vertex
    /tmp/cube8-vertex
    g++ -O2 -std=c++17 sidorenko_attempt/cube8_k_independent_polynomial.cpp -o /tmp/cube8-independent
    /tmp/cube8-independent
    python sidorenko_attempt/cube8_k_independent_verify.py
    python sidorenko_attempt/cube8_root_exact_obstructions.py

Read each source for its complete output paths and additional forward-Walsh,
Python multiplier and C++ multiplier commands. Running the full independent
verifier requires the archived author and independent maps; all are supplied.
The root rebuilt all four C++ routes, ran the full rooted enumeration,
coverage, forward transform, inverse transform, exceptional chamber and
positive multiplier comparison. All checks exited zero. Arithmetic bounds
are proved in the audit; entropy/optimization roundoff is not used.

## Primary sources and scope

Fox--Himwich--Mani--Zhou, published 5 September 2025, identify ML10 as a
notorious unresolved general case:
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p38/pdf/
Rossman's May 2025 primary ladder transfer note is credited prior work:
https://users.cs.duke.edu/~br148/sidorenko-mobius.pdf
Zhao's paper submitted 21 July 2025 concerns even subdivisions and does not
cover this cubic source:
https://arxiv.org/abs/2507.15723
The paper submitted 22 June 2026 concerns two-sided correlation graphons;
its nonnegative-spectrum Boolean subcase does not supply this signed-spectrum
host theorem:
https://arxiv.org/abs/2606.23018
These full primary-source checks do not establish historical priority.
Arbitrary regular eight-state hosts, unequal atom measures, larger Boolean
groups and the unrestricted Sidorenko conjecture remain outside the proof.
