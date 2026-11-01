# Completion and reproduction record

This immutable bundle separates one proved restricted lemma from two exact
obstructions to tempting proof routes.  Read the source/scope check before
using any conclusion.

## Proven restricted lemma

`continuation_20261003_C4_twostate_PROOF.md` proves nonnegativity of the
four-edge square coefficient on a two-state quotient.  The author program
enumerates all 1,024 source labelings and emits the exact quartic and its
66-positive-coefficient discriminant.  The independent program fixes each
of 32 left labelings, eliminates the five right labels separately, and
reconstructs the same complete certificate.

Run:

```text
python3 continuation_20261003_C4_twostate_discriminant.py
python3 C4_twostate_ant_independent_check.py
```

Both exited zero on 3 October 2026.

## Exact failed-route result

`continuation_20261003_C6_actual_host_obstruction.md` gives the strictly
positive sixteen-state host and the exact negative C6 numerator.  Its author
regenerator and the independent audit intentionally use different routes.
The latter checks the literal graph's 64 even edge sets by full pair
transfers, Walsh translation blocks, and 3,932,160 exact Fourier-flow terms.

Run:

```text
python3 continuation_20261003_C6_actual_host_obstruction.py
python3 global_colored_ant_exact_obstruction_check.py
python3 continuation_20261003_global_colored_exact_checks.py
```

All exited zero on 3 October 2026.  The independent result is
`PASS exact actual-host negative C6; no Sidorenko counterexample claimed`.

## Numerical boundary

The q=32 and q=64 translation-block searches found no substantial negative
C4 value.  They do not prove positivity.  The exact q=4 example with one
negative character contribution shows why a termwise Walsh proof fails even
though its total C4 contribution is positive.

Every JSON proof certificate is stored beside its generator.  Numerical
search reports are labeled as such and are not dependencies of either exact
result.

