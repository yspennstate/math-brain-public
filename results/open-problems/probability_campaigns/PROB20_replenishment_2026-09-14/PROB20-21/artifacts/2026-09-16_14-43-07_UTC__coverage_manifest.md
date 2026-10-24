# PROB20-21 coverage manifest — 2026-09-16_14-43-07_UTC

## Scope

Target metric: largest `n` with exhaustive all-function, full-noise-interval certification of the
Courtade–Kumar inequality under the frozen source-valid reduction/enumeration convention.

This manifest records executed code and coverage. It does **not** claim universal closure.

## Runtime metadata

- Model: GPT-5.6 Sol (visible to this run).
- Reasoning effort: UNVERIFIED. GPT-6 / maximum was requested, but the scheduler exposes no
  reasoning-effort selector and no verified GPT-6 runtime setting.
- Compiler: `g++ (Debian 14.2.0-19) 14.2.0`
- Architecture: `x86_64`
- MPFR library: `/lib/x86_64-linux-gnu/libmpfr.so.6`
- Exact rational arithmetic: GMP / `mpq_class`
- Log/entropy enclosure: MPFR 256-bit directed rounding from exact rational inputs.

## Final n=5 checker

Source local SHA-256:
`b51678a839ca47ad692b2d49e4f5ec465bd4a3e32d65b86dcea333d2e9bb4252`

Output local SHA-256:
`72c5e222b87c30f59cddcb1f72371077dee2599b0b7b7c9492c4afbe78e7670d`

GitHub source creation commit:
`98600d532765fc0be5c08db6f99d7f83adbd8ada`

GitHub output creation commit:
`b607a7d7d49bf131acf384f601358e9d7048e2ad`

Compilation / execution actually used:

```sh
g++ -O3 -std=c++17 prob20_21_n5.cpp -o prob20_21_n5 -lgmpxx -lgmp -l:libmpfr.so.6
./prob20_21_n5 > prob20_21_n5_output.txt
```

Executed output:

```text
PROB20-21 N<=5 FULL-NOISE-INTERVAL CERTIFICATE
model_runtime_metadata=UNVERIFIED
source_defined_compressed_candidates=119
constant_candidates=2
dictator_candidates=1
nontrivial_candidates=116
balanced_nondictator_candidates=6
biased_nontrivial_candidates=110
min_balanced_nondictator_avg_sensitivity=11/8 mask=357913943
min_Delta_var_minus_W1=13/128 mask=1
full_alpha_interval=[0,1/2]
low_noise=[0,1/8192]
middle=[1/8192,63/128]
high_noise=[63/128,1/2]
biased_low_noise_lower_gap_nat=0.00073237068691549994
balanced_low_noise_uniform_margin_over_alpha=0.16006667575037495
high_noise_rational_margin=3187/524288
counterexample_grid_alpha=j/256,j=0..128
counterexample_grid_certified_negative=0
grid_smallest_interior_lower_D_nat=3.1115679161655743e-06 mask=357913941 alpha=127/256
middle_leaf_intervals=8949
middle_max_bisection_depth=14
middle_min_outward_lower_D_nat=5.1083634992863697e-08 mask=357913943 a=2052291/4194304 b=1028161/2097152
log_engine=MPFR_shared_library_directed_rounding_256_bits_exact_rational_inputs
checker_runtime_seconds=20.634993477999998
RESULT=PASS
```

### Frozen enumeration convention

For `n=5`, a 32-bit mask encodes the source set `B=b^-1(0)` by putting bit `x`
equal to one iff `x in B`, where integer binary digits give source coordinates in increasing
coordinate order. The candidate family is **exactly** the sets whose every singleton and
two-coordinate section is an initial lexicographic segment in the sense of Courtade–Kumar
Definitions 1–2 and Corollary 1.

The generator builds all ideals of the induced prefix constraints and then independently checks
the source definition section-by-section. It produced exactly `119` candidates, agreeing with
Courtade–Kumar Table I for `|S_5|`.

Courtade–Kumar Theorem 2 says every two-coordinate compression of `b^-1(0)` cannot decrease
`I(b(X);Y)` at fixed noise, and Corollary 1 says a maximizer is contained in this candidate family.
Therefore certifying all 119 candidates certifies **all** five-variable Boolean functions.

The checker evaluates the indicator of `B` rather than the original `b`; this is an output complement,
so mutual information is unchanged.

### Interval coverage

- Entire target interval: `[0,1/2]`
- Analytic low-noise regime: `[0,1/8192]`
- Certified interval-subdivision regime: `[1/8192,63/128]`
- Analytic high-noise regime: `[63/128,1/2]`
- Middle-regime leaves: `8949`
- Maximum dyadic bisection depth: `14`
- Smallest outward-rounded certified lower gap in middle:
  `5.1083634992863697e-08` nats
- Counterexample-first exact grid: `alpha=j/256`, `j=0,...,128`,
  zero certified negative gaps. This grid is **not** credited as interval coverage.
- Final result: `PASS`.

Because every Boolean function on fewer than five variables embeds as a five-variable function
independent of the extra coordinates, the `n=5` certification also implies the same source inequality
for every `n<5`. The tracked metric is therefore `5`.

## n=6 executed diagnostics — no metric credit

The exact source-defined candidate enumerator found `1173` candidates, matching Courtade–Kumar
Table I. Diagnostic exact invariants were:

- `1170` nontrivial candidates;
- `40` balanced nondictators;
- minimum balanced nondictator average sensitivity `5/4`;
- minimum `Delta = Var(f)-W_1(f)` equal to `57/1024`;
- the candidatewise high-noise sufficient condition first passed among tested reciprocal integer
  thresholds at `rho=1/70`, with exact squared margin
  `254319669/6294077440000` for the worst diagnostic candidate.

A full n=6 middle-interval checker was then compiled and executed, but the container call hit the
`300000 ms` timeout. The exact tool status was:

`Command failed because it timed out.`

Its redirected output file was 0 bytes because stdout remained buffered when the process was killed.
Accordingly **n=6 is not certified and receives no metric credit**.

The diagnostic source/output variants were retained locally and identified by SHA-256 below. Their
mathematical content is summarized here; they are exploratory and are not part of the n=5 coverage proof.

## Artifact integrity

- final n5 source SHA-256: `b51678a839ca47ad692b2d49e4f5ec465bd4a3e32d65b86dcea333d2e9bb4252`
- final n5 output SHA-256: `72c5e222b87c30f59cddcb1f72371077dee2599b0b7b7c9492c4afbe78e7670d`
- n6 probe source SHA-256: `889fb14961ed7fe634d50e1c443332644fef6112886eebd550ba093fd28a0775`
- n6 probe output SHA-256: `969886605f320b248a547263e555ed7f4ee60f9cc0062e3da109c8df6b59090b`
- n6 high probe source SHA-256: `bcadfc810a1d17f5fa0dc6295a59a45d81f332983feb348cf6c10ce175ab215e`
- n6 high probe output SHA-256: `f03d320cf68c89d7aaf418b56f77d91b61449705bbac6cd6f3349bd5087e8ada`
- n6 threshold probe source SHA-256: `c4f59709427cdcf213e15e3574c422d2bae5f7e9736615a0fde4e46c2c902887`
- n6 threshold probe output SHA-256: `4fe36472dad3d0c0fbe24b25c2ba3d42215ffcc5df66ce2e372b64c905623f75`
- n6 full attempt source SHA-256: `74c53161b0837f94dc9e62dc00ef6e636a66e3684d06c90e5c0cb1d3f479b260`

## Review boundary

The finite checker and analytic end-regime derivations were self-reviewed in this run.
This is not an independent audit, not formal verification, and not universal Courtade–Kumar closure.
