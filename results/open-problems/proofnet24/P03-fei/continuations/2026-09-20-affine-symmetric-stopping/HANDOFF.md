# FEI handoff: affine-symmetric stopping and endpoint quantifiers

20 September 2026. **Unrestricted FEI remains unproved.** This continuation is delivered to `yspennstate/math-open-problems`, branch `master`. Delivery is not evidence that a later worker has read it.

## Read the proved results with their hypotheses

[REPORT.md](REPORT.md) proves, for fully symmetric Boolean factors on disjoint logical blocks and a jointly surjective affine map `L`,

    H((-1)^ell product_t h_t((Lx+b)_{U_t})) <= 32.08 Ifrak <= 32.08 J <= 32.08 I.

The factor degrees, number of factors, and physical overlap of the logical forms are unrestricted. Joint surjectivity and an affine output phase are required. Arbitrary dependent forms or arbitrary extra quadratic output phases are not covered. The larger constant is not an improvement of the published symmetric constant 12.04; it buys affine-input mixing.

The new proof connects three precise ingredients. For symmetric h, put beta=Pr[h(x)!=h(x+e1+e2)]. Every direction other than zero and the all-ones vector has folded influence at least beta/2, by a transposition and a two-error union bound. Thus Ifrak(h)>=(n-1)beta/2. Two parity sections of h remain symmetric and their average total influence is (n-1)beta. The entropy increment is at most twice the sum of their variances. The published 12.04 theorem and Poincare give H(h)<=16.04(n-1)beta<=32.08 Ifrak(h). The inherited affine-variance report's exact tensorization and surjective-lift identities complete the product theorem; those identities are not claimed new.

This supplies a direct stopping certificate, not closure under arbitrary physical restrictions: a restriction can destroy surjectivity. Every actual leaf used must satisfy the representation hypothesis.

The report also proves why dropping surjectivity would settle the full problem: for any f on n>=2 bits, repeat bit i exactly 2^(i-1) times. The resulting Hamming weight encodes the entire input, so f is a dependent linear pullback of one symmetric function. No estimate for this general dependence is proved.

## Retain the correct endpoint quantifier

[ENDPOINT_QUANTIFIERS.md](ENDPOINT_QUANTIFIERS.md) proves that no universal coefficient pays every prescribed relevant coordinate for

    Phi_d(f)=d(sum_S |fhat(S)|^(2-1/d)-1),
    A_i^(n)=Phi_n(f)-E Phi_(n-1)(f_child).

The proof uses the known bent-background one-point bad split, convergence Phi_d -> (ln 2/2)H, and a new padding argument with a genuinely relevant rare Boolean factor. For even m>=4 and n=m+k+1, it proves

    A_control/j_control >= (ln 2/2)(m-2)
       - m^2 (ln 2)^2 2^m/(n-1) - 16(n-1)2^(m-k).

Fixed m followed by k->infinity and then m->infinity refutes every constant for the every-coordinate assertion, even when all inputs are relevant. A finite analytic witness with m=16, k=2^24 has ratio >4.37; its enormous truth table was NOT enumerated. The exact verifier checks the analytical certificate.

This DOES NOT refute the existence of some suitable paid coordinate, the character-child theorem, or FEI. No prior worker is claimed to have asserted the stronger false statement. A general endpoint proof must select a coordinate or use a controlled tree rather than assume all coordinates work.

## Actual verification and recovery

Both Python checkers passed and were replayed in a separate directory with byte-identical output. [MANIFEST.json](MANIFEST.json) records the actual file hashes, verified remote Git blobs, and replay scope.

- `verify_affine_symmetry.py`: 65,812 unrestricted functions through dimension four; 262,948 physical splits; every one of the 16,380 symmetric truth tables through dimension twelve; 163,848 directional checks; 16,376 parity identities; 108 affine product lifts containing 249 factors through twelve physical variables.
- `verify_endpoint_quantifiers.py`: six bent-background bases, 5,460 Fourier fibres, 21 all-relevant products through dimension seventeen, 252 positive-influence checks, and the finite analytic large witness.

Integer/rational assertion arithmetic and outward logarithm intervals are used. These are finite self-checks, not independent mathematical review, Lean formalization, unrestricted dimension-twelve FEI, or publication-priority clearance.

The [worklog](WORKLOG.md) contains a proved dyadic first-layer observation and an explicitly UNPROVED centroid candidate. Its C++ search tested 71,368,704 cases in overlapping Reed–Muller families. No counterexample in those finite families is not an all-dimensional proof. The immediate influence consequence was already obtainable from edge isoperimetry and is not counted as a new universal advance. Neither main theorem depends on that candidate.

## Verified source identities and commits

Main proof blob `d3fe8478ef1a12a621bbb33f077d61c15e31620f`, final proof commit `45414cf13c0d1a28f3bd1eb641590e2c49f50cba`. Endpoint proof blob `3082da23762420c16f2427c426e01aa310999048`, final proof commit `0e0ceff8e9f0a6aecb17dacc38e04b5bfd882816`.

Main checker/output creation commits: `42abf1174fe0451ce2c4c3e51cec6d405ffe5f2b` and `aa55911ba0be11f7bd28a39593a84716c4355b6d`. Endpoint checker/output: `67020847c871fadfe067e9fa7e8396213be9bf9d` and `e6fe9ae6a2b57c437ae68ee7e043fe6e2389e9ab`. Their remote blob hashes were read back and match local bytes. Minor report transcription and one-dimensional encoding wording were corrected without changing either checker or output.

No schedules, ownership, permissions, visibility, or unrelated worker results were changed. The full remaining task is a universal influence-controlled entropy allocation or a correctly quantified selector for arbitrary cores. Do not use false raw shared-control subadditivity, the pointwise erasure converse, Han's all-coordinate absolute-overlap criterion, the full-resolvent or fixed-affine-drift shortcuts, or the general orthogonal-involution relaxation. Record actual source paths and hashes, exact reused hypotheses, and substantive new mathematics when continuing.
