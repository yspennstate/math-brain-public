# HARD8-05 verification addendum — corrected exponent-four checkpoint

This append-only verification companion covers the corrected report and exact verifier produced in this run.

## 1. Corrected mathematical report

Path:

`hard8_2026-09-16/HARD8-05/runs/2026-09-16/2026-09-16T09-39-45Z__report.md`

Creation commit:

`276294dba742cf7bd13314a093cbbfefc8982acc`

Readback at that exact commit succeeded. GitHub returned content blob SHA:

`7e6c6aced7dc9f076c8aa5878f7b51ded7b94f2d`

Status:

**VERIFIED BY EXACT-SHA READBACK.**

This report explicitly supersedes the incorrect fixed-total simplifications in the earlier same-run report at commit `d0b3c5de08efd8df1491ffa29b359053e5ea2512`. The earlier file is preserved unchanged for audit history.

## 2. Exact verifier artifact

Path:

`hard8_2026-09-16/HARD8-05/artifacts/2026-09-16T09-39-45Z__exponent4_portal_verifier.py`

Creation commit:

`272919823155af7e5e998274720893eba43d05db`

Readback at that exact commit succeeded. GitHub returned content blob SHA:

`8221a35229cb83189734b99767045670e29d4a78`

Status:

**VERIFIED BY EXACT-SHA READBACK.**

## 3. Actual bounded execution record

The exact source archived above was executed before this addendum was written. It completed successfully with output:

```text
mod16 signatures/success/failure: (2048, 1969, 79)
mod20 C4xC2 transfer: OK
full-range exact box/special-branch checks: OK
hard-class primes <= 4,300,000: 37716
nine-portal residuals: 122
new portal counts: {(1, 4): 41, (4, 1): 31, (1, 5): 58, (5, 1): 59}
thirteen-portal union: 37706
thirteen-portal residuals: [345601, 670849, 1083289, 1113961, 1672609, 1740481, 2762761, 2764441, 2914921, 3819481]
residual exact certificates: {345601: ((7, 2), 279), 670849: ((1, 8), 319), 1083289: ((2, 5), 599), 1113961: ((6, 5), 61319), 1672609: ((3, 5), 59), 1740481: ((3, 4), 3311), 2762761: ((2, 5), 119), 2764441: ((5, 2), 119), 2914921: ((4, 5), 79), 3819481: ((3, 4), 143)}
ALL CHECKS PASSED
```

The verifier uses the Python standard library and exact integer arithmetic. It checks:

1. all `2048` truncated exponent signatures in `(Z/16Z)^× ≅ C4 × C2`;
2. the exact 14 minimal success signatures and eight maximal failure signatures;
3. the isomorphic modulo-20 transfer on every truncated signature;
4. for every hard-class prime through `4,300,000`, exact direct divisor reachability versus the eight-box criteria for all four portals `(1,4),(4,1),(1,5),(5,1)`;
5. the corrected special branch criteria for `K=(n+5)/2` and `L=(5n+1)/2` on the same entire finite range;
6. reciprocal gcd identities and `B=5A-4` with coprime `A,B`;
7. the previous nine-portal residual count `122`;
8. the four new portal counts and their union, leaving exactly ten finite residuals;
9. exact Type-II witnesses for those ten, including direct integer cross-multiplication of the resulting three-unit-fraction identity.

No floating point, randomization, external solver, or timeout-based inference is used.

## 4. Scope

The exact finite-group classification is a proved local theorem. The finite prime-range experiment is only bounded evidence. Neither establishes the full Erdős–Straus conjecture, which remains open.
