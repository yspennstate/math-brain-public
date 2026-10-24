# B15 / A071 — exhaustive edge-partition neighborhood of the two-address endpoint

**Run ID:** `20261011T210906Z-account01-B15-A071-two-address-domain`  
**Primary packet:** A071 (Search-space design)  
**Attempt:** `A071-attempt-01-C022-edge-partition`  
**Status:** `FINITE_DOMAIN_EXHAUSTED / NO_STRONGER_WITNESS`  
**Full FEI:** **OPEN**

## 1. Frozen target

The selected live target is campaign claim C022:

> Find a finite explicit constant for genuine Boolean spectra whose retained
> laws, conditional on at most two spectral address coordinates, are product.

The exact one-address theorem has constant two.  The archived genuine
six-variable two-address Boolean function has

\[
H=5,\qquad I=\frac{17}{8},\qquad \frac HI=\frac{40}{17}>2.
\tag{1.1}
\]

Thus the obsolete helper `H<=2I` is already refuted.  This run does not retry
it.  The bounded question frozen before the computation was:

> In the complete four-physical-bit edge-partition family defined below, does
> any genuine Boolean function with all four address-conditioned spectral laws
> product have `H/I>40/17`?

This targets the immediate combinatorial neighborhood of the known witness
while preserving actual Booleanity and every conditional product hypothesis.

## 2. Search family and completeness at its stated scope

Write `x in F_2^4` and `y in F_2^2`.  Choose three pairwise vertex-disjoint
edges `E_01,E_10,E_11` of the four-cube.  Let their six-vertex union be `Z`,
and let

\[
g:F_2^4\to\{0,\pm1\}
\]

vanish exactly on `Z` and take arbitrary signs on the ten-point complement.
Define

\[
F(y,x)=g(x)+\chi_{01}(y)1_{E_{01}}(x)
             +\chi_{10}(y)1_{E_{10}}(x)
             +\chi_{11}(y)1_{E_{11}}(x).
\tag{2.1}
\]

Exactly one summand is nonzero at each `x`, so `F` is genuinely Boolean.  Its
four Walsh slices in the address frequency are `g` and the three edge
indicators.  Every normalized edge-indicator squared spectrum is a product
law, with three fair marginals and one deterministic marginal.  The program
retains a candidate precisely when the normalized squared spectrum of `g` is
also a product law.  Therefore every retained `F` satisfies C022's exact
two-address hypothesis.

The four-cube has 32 edges and 2,496 matchings of three disjoint edges.  These
produce exactly 1,984 distinct six-vertex unions `Z`.  For `H/I`, it is complete
to take one edge partition of each union:

- the residual slice depends only on `Z` and the complement signs;
- every edge slice has the same entropy and expected physical degree;
- assigning the three edges to address labels `01,10,11` always gives total
  address degree `1+1+2=4`;
- signs on an edge slice do not affect squared Fourier masses;
- global output negation does not affect `H` or `I`.

Fixing the first complement sign to `+1` leaves `2^9=512` sign patterns for
each union.  Hence the exact precomputed case count is

\[
\boxed{1984\cdot2^9=1,015,808.}
\tag{2.2}
\]

No cube-automorphism quotient was used, so the enumeration is redundant but
complete for the stated metric question.  It is not complete for all
six-variable Boolean functions or all C022 functions.

## 3. Exact engine and formulas

For a residual truth table `g`, let

\[
w_S=\sum_{x\in F_2^4}g(x)(-1)^{S\cdot x}.
\]

All transforms are integers.  The residual squared masses in the full
six-bit spectrum are `w_S^2/256`.  The three edge slices contribute 24 atoms
of mass `1/64`, hence exactly `9/4` entropy bits.  Consequently

\[
H(F)=\frac94+
\sum_{S:w_S\ne0}\frac{w_S^2}{256}
     \log_2\frac{256}{w_S^2}.
\tag{3.1}
\]

The influence is

\[
I(F)=\frac1{256}\sum_S |S|w_S^2+rac{17}{16}.
\tag{3.2}
\]

Here `9/16` is the total physical influence of the three edge slices and
`1/2` is their total address influence.  The program independently reconstructs
the full 64-value Boolean truth table and its 64-point Walsh transform for the
maximizer, verifies Parseval, and checks (3.2) against direct full-spectrum
influence.

The residual product-law test is exact: for `q_S=w_S^2`, total `Q=sum q_S`,
and one-bit marginals `m_i(0),m_i(1)`, it checks

\[
q_S Q^3=\prod_{i=1}^4m_i(S_i)
\]

for all 16 subsets.  Final logarithms are enclosed using rational atanh-series
bounds.  Zero masses are omitted, and Parseval is checked in the full Boolean
reconstruction.

## 4. Exhaustive result

The complete search produced:

| quantity | exact count |
|---|---:|
| edge matchings before union quotient | 2,496 |
| distinct six-vertex zero supports | 1,984 |
| sign/support representatives | 1,015,808 |
| retained product-residual candidates | 3,584 |
| distinct ordered residual squared laws | 8 |
| certified `H/I>40/17` | **0** |
| certified `H/I<=40/17` | **3,584** |
| interval-ambiguous comparisons | **0** |

Every retained residual squared spectrum has eight Walsh squares equal to 4
and eight equal to 16.  Therefore every retained full function has

\[
H(F)=5.
\]

There are exactly two metric signatures among the representatives:

\[
(H,I,H/I)=\left(5,\frac{17}{8},\frac{40}{17}\right)
\quad\text{for 1,792 representatives},
\tag{4.1}
\]

and

\[
(H,I,H/I)=\left(5,\frac52,2\right)
\quad\text{for 1,792 representatives}.
\tag{4.2}
\]

Thus:

> **PROVED FINITE-DOMAIN THEOREM.** Within the family (2.1), the maximum
> Fourier entropy/influence ratio is exactly `40/17`; the archived witness is
> optimal in this family.

This neither proves `40/17` for the full two-address class nor supplies any
dimension-independent constant for C022.  It is also not an FEI
counterexample.  Its value is negative guidance: merely moving the three
address slices among disjoint four-cube edges and changing arbitrary residual
signs cannot improve the known ratio.

## 5. Reproduction and resource budget

Command:

```text
python exact_two_address_search.py > OUTPUT.txt
```

No randomness is used.  A clean rerun was byte-identical to `OUTPUT.txt`.

| resource | frozen cap | observed |
|---|---:|---:|
| representatives | 1,100,000 | 1,015,808 |
| wall time | 60 seconds | 14.165 seconds |
| peak RSS | 128 MiB | 11,264 KiB |
| candidate rate | — | about 71,700/second |
| exit status | 0 required | 0 |

Source SHA256:
`7b38732259f17f034c9fd4d28ad2a1c16bfbf4dc3e84beaf9d66525788955f84`.

Output SHA256:
`0198ecffd5c8be538d81cbf043d3eb3f63356a956ff0425fbbe7fb79d11932cf`.

## 6. Sources and obstruction checks

Sources read at current campaign state:

- open-problems head `3246f3d914cc3fe70f29f65aab13e795b99419bb`;
- `CURRENT_STATUS.md`, blob `8c9c63579ecdd4afa385bb94caf79ee6296addcf`;
- `assignments/B15.json`, blob `0b1f8d825bdfcc0bf36b86dab00edd1648a27444`;
- `EXECUTION_PROTOCOL.json`, blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`;
- supplement `CLAIMS.md`, blob `d7279735b4dcfaf7552cf271b7413fc5c0f427b6`;
- original `ONE_BIT_ENDPOINT.md`, blob
  `0848515367f7fc3493f51820de999a30234905a4`.

The Brain mirror's B15 contract and status had the same blobs as canonical.
The original C016/C022 proof and witness were read, not inferred from the
registry label.

Applicable guards:

- **Actual Booleanity:** equation (2.1) is sign-valued pointwise; the displayed
  maximizing truth table is archived.
- **Whole-set addressing:** address labels are charged once by their spectral
  degrees; no per-coordinate label repetition is introduced.
- **Rare events:** all slice masses here are fixed at `5/8,1/8,1/8,1/8`; this
  bounded family does not test a vanishing activation probability.
- **Near tensors:** no tensor extrapolation is made.
- **Prime gates/shared variables:** this is an actual six-variable gate, but no
  irreducibility or composition closure is claimed.
- **Conditional rows:** individual projection rows need not themselves be
  Boolean; the retained hypothesis is only their normalized squared product
  law, while the assembled `F` is Boolean.

No publication-novelty claim is made, so the finite result is reported as a
campaign search certificate rather than a literature claim.

## 7. Claim and packet delta

**Previous value/status:** C022 was open; `C=2` was refuted by the archived
ratio `40/17`, with no optimality statement even in the immediate edge-slice
neighborhood.

**New value/status:** exhaustive exact classification proves that the maximum
is `40/17` in family (2.1).  No larger witness exists among its 1,015,808
symmetry-reduced representatives.

**A071 acceptance:** both requested design artifacts are complete: the family,
symmetry reduction, exact case count, measured rate and hard caps are explicit.
This finite theorem is ready for A072 reuse.  A071 does not resolve C022 and
does not complete A073--A075.

**Review:** no independent review was observed.  Route to A085 and A092.

**Next action:** enlarge one structural axis without an uncontrolled truth-table
explosion: keep two address bits and four physical bits, but replace the three
edge indicators by all disjoint affine two-point cells with independently
signed characters, quotienting by the full affine automorphism group before
running the A072 exact engine.  If that produces no new metric signature,
switch A075 to an analytic classification of admissible residual product norms
rather than increasing physical dimension.

Full FEI remains open.
