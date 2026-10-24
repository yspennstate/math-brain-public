# account03/B16 repaired-source audit — pass 3

Objective: QFORM-FIVE-270-REPAIRED-AUDIT-20260925

Exact source: yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa,
repaired-2026-09-25/paper.tex, blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a,
SHA-256 90f859b7e52d0f57574a4f2e93e522177a715a3107173884c142dd84484560bb.

Status: WITHOUT_VERIFIED_BRAIN.

## Result

Pass 3 independently reread and reconstructed all 683 physical source lines and all 26 proof
environments using a forward adversarial lens: quantifier leakage, equality boundaries, endpoint
domains, measurability order, original-coordinate independence, and essential boundedness versus
continuity.

No new mathematical GAP or FALSE clause was found.

The repaired proof again supports:
- s5(A)>=s>0 => essential density <=270 K^2/s;
- s3(A)>=s>0 => full negative-half-moment <=77 K/sqrt(s);
under arbitrary independent real density-capped coordinates, arbitrary real symmetric A,
dimension, signature, remaining spectrum and affine terms, without moments/support/iid/smoothness.

## Load-bearing rechecks

- Padded singular-value indices and singular/indefinite Schur loss: PASS.
- Heat-flow Brascamp-Lieb limiting/differentiation steps: PASS.
- Product projection: all beta_i=0 factors are fiber-independent and <=1; p(y)=0 is handled
  before logarithms; no rotated-coordinate independence is used.
- Fourier decay: total-variation domination, fixed-sequence measurability of
  x -> ||nu_x||_2^2 before its expectation and the terminal branch, measurable F_t and explicit
  Jensen all PASS.
- Scalar/pair endpoint repairs: p_T(v)=0, open polar chart/null seam, hyperbolic critical null
  level, J(0)=+infinity and h(0)=+infinity all PASS.
- Concentration: ordered crossing probability 1/4 and exact Gamma certificate <19 PASS.
- Random signs: only ordered pairs (p,q)=(i,j),(j,i) survive; no missing factor two.
  Singular-value duplication/compression and gamma thresholds PASS.
- Full s3 half-potential: no-pivot <26, pair 64, scalar-pivot <77 PASS.
- Main branches: no pivot <167; scalar pivot sqrt(12)*77<267; definite pair 16*pi<51;
  indefinite pair <269; a.e. K,s scaling PASS.
- Line 511 s^{-2} at the written endpoint s=0 is a null-endpoint/improper-integral notation
  issue only; PASS, optional editorial clarification.
- Two-star four-direction counterexample: PASS.

Numeric diagnostics:
sqrt(12)*77 = 266.735824365607...
16*pi = 50.265482457437...
16*(8+4 log 2+2 log 19)+1/e = 266.951346330334...

Rendered 15-page PDF/source equivalence is UNCHECKED_THIS_RUN because the reference PDF is not
a repository binary and no new permitted local materialization was available.

Complete repaired-source B16 passes after this run: 3.
Passing is not a stop condition; next run must repeat in a different reconstruction order.
