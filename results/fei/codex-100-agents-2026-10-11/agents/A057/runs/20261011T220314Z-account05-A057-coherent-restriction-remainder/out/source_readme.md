# Coherent balanced composition: reviewed control

Status: **PARTIAL; full FEI remains OPEN**. This package establishes a scoped
balanced/disjoint composition identity and refutes one proposed remainder
estimate. It is not a full-FEI proof, an FEI counterexample, an all-coordinate
obstruction, a novelty claim, or proof-assistant verification.

## Independently checked mathematical conclusion

For Boolean sign functions `F=g(h_1,...,h_m)` on disjoint blocks, with every
inner balanced, fix leaf coordinate `i` in block `j`. Set
`q=Inf_j(g)` and `alpha=hat h_j({i})`. Entropies use natural logarithms and
`D_i` is parent spectral entropy minus the fair average of physical-child
spectral entropies. Writing `g=a+y_j b`, the exact formulas are

```
Inf_i(F) = q Inf_i(h_j)
D_i(F) = q D_i(h_j) + R(alpha)
R(alpha) = q alpha^2 ln(1/alpha^2) + Eraw(a) + alpha^2 Eraw(b)
           - (Eraw(a+alpha b)+Eraw(a-alpha b))/2
```

The other-block child entropy coefficients are
`a_T^2+b_T^2+2s alpha a_T b_T`. Their coherent cross terms cancel after fair
averaging over the two physical children, not within either child. The
nonnegative remainder is the equal-mass noisy-outer entropy decrement:
`R=M(B_i+JS)>=0`, with `M=1-q+alpha^2 q`. The zero-mass case is handled
separately. Also `abs(alpha)<=Inf_i(h_j)`.

The fixed two-bit AND outer and explicit adjacent-pair parity modifications
give `R/(q alpha^2) -> infinity`. Thus no finite universal `C` can give
`R<=C q alpha^2` under these hypotheses. In this same family the selected
full-composition coordinate ratio `D_i(F)/Inf_i(F)` tends to zero. Nonzero
`alpha` produces biased physical-child inners, so the balanced class alone
does not yield a restriction-closed FEI reduction. The complete argument is
in [source/PROOF.md](source/PROOF.md).

## Review and reproducibility

The publication review independently read the complete proof and checker,
checked the raw tensor/sector derivation, influence factorization, noisy-outer
normalization, AND asymptotic, realizability of the parity family, and endpoint
cases. A fresh copy of the checker ran successfully with Python 3.12.14 and
passed compilation. This is an independent replay of the same checker, not
an independently implemented checker or an external expert audit.

- 16 two-bit outer tables times 70 balanced three-bit first inner tables,
  with a fixed three-bit majority second inner: 1,120 six-dimensional inputs,
  3,360 physical split checks, and 6,720 child checks
- Overlapping endpoint counts: `q=0`: 840; `alpha=0`: 1,728;
  `alpha=+1`: 48; `alpha=-1`: 48; `M=0`: 432
- The phase fixture has other-inner child entropy coefficients `3/4` and
  `1/4`, rather than `1/2` in each child
- Six specified parity-family controls with inner dimensions 3 through 8
  and composed dimensions 4 through 9; this is not an exhaustive search
  over all functions in the larger dimensions

All algebraic comparisons use exact integer Walsh transforms and rational
coefficients of prime logarithms. Decimal diagnostics are descriptive only;
the asymptotic claims follow from the analytic proof. The replay output
matches source/results.json exactly after removing only elapsed_seconds.
[REPLAY_VERIFICATION.json](REPLAY_VERIFICATION.json) records that comparison
and hashes; [REPLAY_LOG.txt](REPLAY_LOG.txt) is the actual execution output.

To replay without modifying the preserved outputs, copy `source/` to a
temporary working directory, then run:

```
python check_composition.py
python -m py_compile check_composition.py
```

## Provenance and preservation

The seven files under `source/` are byte-preserved from the reviewed original
research package. Statements there about a local-only stage describe its
earlier preparation state; this README records the later reviewed repository
copy. No source claim has been silently rewritten. Its original hashes remain
in source/SHA256SUMS. The top-level MANIFEST.json and SHA256SUMS cover this
delivery. Compare all delivered bytes at the immutable commit before relying
on a branch-tip link.

Only original mathematical prose, the self-contained synthetic checker,
generated mathematical outputs, and this review are included. The current
repository guidance was checked; this additive continuation leaves earlier
research and concurrent work intact. It does not change a policy, workflow,
schedule, permission, visibility, or Brain route map. Repository delivery
does not establish later worker adoption or held-out performance improvement.

A supplemental run of the unmodified Brain text scanner reported one
absolute-path match: the original checker's standard Python shebang on line
1. This is not a clean scanner-pass claim. The scanner is not an imported
publication gate for this math continuation; manual review identified the
match as a portable interpreter directive. The original source is preserved.

Prepared for the existing draft PR12 branch on 2026-10-01; no merge or deployment.

