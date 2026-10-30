# B16 / A079 — exact two-point shared-input overlap family

**Run:** `20261012T043849Z-fleet01-B16-a079-two-point-overlap`  
**Primary packet:** A079 (Correlated auxiliaries)  
**Attempt:** `A079-TWO-POINT-OVERLAP-01`  
**Claim:** `B16-A079-TWO-POINT-OVERLAP-v1`  
**Gap:** `G-A080-UNIVERSAL-COUNTEREXAMPLE`  
**Status:** restricted all-parameter classification PROVED pending independent review; full FEI remains OPEN.

## New class and exact result

The previous A080 result classified every *disjoint tensor* of point
defects. This run leaves that closure. For `d>=2`, choose two vertices at
Hamming distance `h` and let `f_{d,h}` be negative exactly at those vertices.
Equivalently, `f_{d,h}` is the product of two point defects on the same
physical cube. It is a genuinely shared-input nonlinear surgery.

With `delta=2^-d`, its squared spectrum is

```
p_empty=(1-4delta)^2,
p_S=16delta^2 if |S intersect supp(z)| is even and S is nonempty,
p_S=0 otherwise.
```

Thus the nonempty spectrum is flat on `2^(d-1)-1` atoms. Writing
`m=8delta(1-2delta)`,

```
H=h2(m)+m log2(2^(d-1)-1).
```

The complete physical influence is

```
I=4(d-1)delta,  h=1,
I=4d delta,     h>=2.
```

The adjacent case exhibits real overlap cancellation: one shared cube edge
becomes internal, and the function is exactly a point defect on `d-1`
effective coordinates.

For the campaign upper-set potential `U`, the complete formula is

```
U = p_empty log2(1/p_empty)
    +4(d-2)delta-16(d-1)delta^2
    +1_{h even} 2^(4-h) delta                (h>=2),
```

with the point-defect `(d-1)` formula when `h=1`.

For every parameter pair,

```
H(f_{d,h}) < 4 I(f_{d,h}),
U(f_{d,h}) < 3 I(f_{d,h}).
```

Uniformly over arbitrary sequences `2<=h_d<=d`,

```
H/I -> 4,   U/I -> 1.
```

## Movement and interpretation

A080 left overlapping nonlinear surgery as the next viable mechanism. This
run gives the first complete all-parameter shared-input family after that
classification. Fourier coefficients were rederived directly; no disjoint
additivity was used.

The repaired actual ratios remain bounded even though tensor factorization
fails and adjacent overlap cancels influence. Hence a finite number of
overlapping rare atoms does not rescue the earlier biased-helper divergence.
A viable counterfamily must use a growing cluster geometry, a non-point-cell
gate, or another mechanism whose spectral entropy outgrows its complete
physical boundary.

## Verification

`python3 verify_two_point_overlap.py` used exact `Fraction` arithmetic for
Walsh squares and influence. It checked every `d=2,...,10` and every
distance `h=1,...,d`, totaling 18,756 exact rational assertions. Direct
upper-set summation matched the closed formula exactly in floating
conversion; the maximum entropy discrepancy was `2.220e-16`. The
all-dimensional result is the proof in `CORRELATED_AUXILIARY_CONSTRUCTION.tex`.

## Scope controls

- Genuine Booleanity: explicit two-point truth function.
- Shared inputs: both defects use all the same physical coordinates.
- Rare activation: the empty spectral atom and its logarithm are retained.
- Added influence: exact edge boundary, including adjacent cancellation.
- Nonflat terminal spectrum: all surviving spectral atoms are included.
- Tensor guard: no product-spectrum or additive `H/I/U` law is assumed.
- Counterexample standard: bounded `H/I` and `U/I` are reported as a negative
  result for this mechanism, not as progress toward a disproof.

## Sources and routing

- B16 contract blob `319bbb049c631c103a842cf9a530c7be91a319d0`.
- A077 compensated tower canonical commit
  `3428cf1d55810b1792ce2e38898f99229f6e428f`.
- A079 rare-cell barrier canonical commit
  `8e46b8d689ce8aa54c16242b4da13dd7be87d1f1`.
- A080 point-defect tensor classification report at run
  `20261012T034627Z-fleet01-B16-a080-point-defect-potential`.

Route the family to A080 and reviewers A092/A088. Next, replace the two-point
set by a growing Hamming cluster and derive its spectrum from the cluster's
indicator transform; test whether the bounded ratios persist.

No independent acceptance, literature novelty, native ingestion, or full-FEI
conclusion is claimed.
