# B15 / A075 — row-wise bent lifts give an infinite two-address family

**Run ID:** `20261011T231103Z-fleet01-B15-A075-bent-row-lifts`  
**Primary packet:** A075 (Search-to-theorem bridge)  
**Attempt:** `A075-attempt-01-rowwise-bent-lift`  
**Status:** `AUTHOR_PROVED_PARAMETERIZED_FAMILY_PENDING_REVIEW`  
**Full FEI:** **OPEN**

## 1. Exact target and previous value

A071 exhausted 1,015,808 representatives in a six-variable two-address
family and proved that its maximum ratio is `40/17`.  Its next analytic run
proved that every admissible signed two-point product row is a coordinate
edge and that alternating signs only increase influence.  The remaining
suggested direction was higher-support product rows and their address-degree
payment.

This A075 run freezes one specific finite-to-family question:

> If each address row of the `40/17` seed is enlarged by an arbitrary
> quadratic bent factor on fresh data variables, can the resulting genuine
> Boolean family have a ratio larger than `40/17`?

This is not a search over dimensions.  The construction and all metrics are
proved for every parameter vector.  The bounded computation reconstructs five
small instances only as an exact validation.

## 2. PROVED general row-wise lift theorem

Let

\[
 F_0(y,x)=\sum_{z\in\mathbb F_2^a}\chi_z(y)h_z(x),
 \qquad h_z:\mathbb F_2^m\to\{0,\pm1\},
\]

where exactly one row `h_z(x)` is nonzero for each `x`.  Put
`alpha_z=E h_z^2`, and suppose each normalized row law

\[
 P_z(s)=\widehat h_z(s)^2/\alpha_z
\]

is product.

For `k>=0`, define the quadratic bent sign

\[
 B_k(u)=(-1)^{u_1u_2+\cdots+u_{2k-1}u_{2k}}.
\]

Its squared Walsh law is uniform on `2k` bits, with entropy `2k` and
mean degree `k`.  Given arbitrary integers `k_z>=0`, put `K=max_z k_z`,
let every `B_{k_z}` use the first `2k_z` coordinates of a common
`u in F_2^{2K}`, and define

\[
 F_{\boldsymbol k}(y,x,u)
 =\sum_z\chi_z(y)h_z(x)B_{k_z}(u).                    \tag{2.1}
\]

### Theorem `B15-A075-ROWWISE-BENT-LIFT-01-v1`

For every seed satisfying the hypotheses and every finite parameter vector
`boldsymbol k`:

1. `F_boldsymbol{k}` is a genuine Boolean sign.
2. Every address-conditioned normalized squared spectrum remains product.
3. The exact metric identities are

\[
 \boxed{H(F_{\boldsymbol k})=H(F_0)+2\sum_z\alpha_zk_z},\qquad
 \boxed{I(F_{\boldsymbol k})=I(F_0)+\sum_z\alpha_zk_z}. \tag{2.2}
\]

#### Proof

Exactly one row is active at each `x`, so (2.1) is always a product of signs.
Orthogonality of the address characters yields the coefficient factorization

\[
 \widehat F_{\boldsymbol k}(z,s,t)
 =\widehat h_z(s)\widehat B_{k_z}(t),                 \tag{2.3}
\]

with deterministic zero frequencies on the unused `u` coordinates.
Conditional on `z`, this is a tensor product of the original row product law,
`2k_z` fair spectral bits, and deterministic bits.  Hence it remains product.

The row masses stay `alpha_z`.  Applying the entropy chain rule to the
orthogonal address rows gives

\[
 H(F_{\boldsymbol k})
 =H(\alpha)+\sum_z\alpha_z\{H(P_z)+2k_z\}.
\]

Fourier degree in (2.3) is `|z|+|s|+|t|`.  The first two components give
`I(F_0)`; the last has conditional mean `k_z`.  This proves (2.2).

The argument does not rely on the false overlapping-product subadditivity:
factorization is proved inside each orthogonal address row.

## 3. Exact infinite family from the `40/17` seed

The A071 seed has four address rows with masses

\[
 (\alpha_0,\alpha_1,\alpha_2,\alpha_3)
 =\left(\frac58,\frac18,\frac18,\frac18\right),
\]

and

\[
 H(F_0)=5,\qquad I(F_0)=\frac{17}{8}.
\]

For

\[
 L=5k_0+k_1+k_2+k_3,
\]

(2.2) becomes

\[
 H=5+\frac L4,\qquad
 I=\frac{17+L}{8},\qquad
 \boxed{\frac HI=\frac{40+2L}{17+L}}
 =2+\frac6{17+L}.                                      \tag{3.1}
\]

Therefore

\[
 \frac{40}{17}-\frac HI
 =\frac{6L}{17(17+L)}\ge0,                              \tag{3.2}
\]

with equality only for the unlifted seed.  Whenever `L` tends to infinity,
the ratio tends to two.  In particular, the diagonal family
`k_0=k_1=k_2=k_3=k` satisfies

\[
 H=5+2k,\qquad I=17/8+k,
 \qquad H/I=2+\frac6{17+8k}.                            \tag{3.3}
\]

This is an explicit genuine Boolean construction for every `k>=0`, not an
extrapolation from a table.  Its row supports grow without bound and retain
the required conditional product structure.  It is not an FEI counterfamily:
the ratios decrease.

## 4. Exact validation and resource cap

Before execution, the pilot was capped at five parameter vectors, largest
dimension ten, five integer FWHTs, 1,024 truth-table entries per largest case,
60 seconds, and 128 MiB.  No randomness or floating tolerance was permitted.

`CHECK.py` reconstructs the full truth table, verifies sign-valued Booleanity,
Parseval, the product identity for every conditional row, row norms, the
exact formulas (3.1), and total influence by a separate bichromatic-edge
count.  Arithmetic is integer plus `fractions.Fraction`.

Command:

```text
python CHECK.py | tee CHECK.out
```

Actual results:

| `(k0,k1,k2,k3)` | `H` | `I` | `H/I` |
|---|---:|---:|---:|
| `(0,0,0,0)` | `5` | `17/8` | `40/17` |
| `(1,0,0,0)` | `25/4` | `11/4` | `25/11` |
| `(0,1,1,1)` | `23/4` | `5/2` | `23/10` |
| `(1,2,0,2)` | `29/4` | `13/4` | `29/13` |
| `(2,2,2,2)` | `9` | `33/8` | `24/11` |

The checker passed 60 aggregate exact assertions with zero failures.  The
proof in Sections 2--3 establishes every parameter value; the pilot is an
independent finite sanity check of the implemented truth-table convention.

## 5. Obstruction and scope audit

- **Actual Booleanity:** exactly one partial row is active for each data input.
- **Signs:** every quadratic factor is a genuine sign; the seed signs are
  preserved.
- **Whole-set addressing:** address labels and their degrees are unchanged and
  paid once.
- **Rare events:** row masses are unchanged.  No rare logarithmic cost is
  hidden or claimed paid.
- **Near tensors:** the extra entropy/influence contribution has exact ratio
  two, so tensor amplification cannot turn this seed into an unbounded ratio.
- **Shared variables:** different rows may use the same `u` variables, but
  disjoint physical row supports and address orthogonality yield (2.3)
  directly; no independence claim between simultaneously active rows is made.
- **Prime gates:** the family is decomposable and supplies no theorem for
  arbitrary prime gates.

## 6. Sources and versions

- `assignments/B15.json`, blob
  `0b1f8d825bdfcc0bf36b86dab00edd1648a27444`.
- A071 exhaustive source report, open-problems commit
  `5aca95345e9eaef015d406af6f84bf74c5a3e01d`, blob
  `d60e96e63352d3a2edeeafe7d33b09b20bb28b3a`.
- Its exact engine, blob `9763a04341d579f84f14105f8faade08167cef35`,
  and output, blob `a21c432ff89a2ab96a360c86b108cd304ca807d9`.
- A071 signed-pair reduction, open-problems commit
  `b77c06c036e3fd6a206100e0fbde4fecb7c5e7e8`, report blob
  `b54f7ea3f226d9fe97cbc0d003619349d4cfa5ea`.
- `CURRENT_STATUS.md`, blob
  `74f6ae761739455083804505ba0e0fd7aaf2f3e2`.

No external novelty claim is made; this is a new campaign bridge derived from
the pinned finite witness and elementary Walsh factorization.

## 7. Packet delta and remaining gap

**Previous status:** `40/17` was proved only for a finite edge-partition family
and its complete signed two-point extension.

**New status:** an explicit infinite family in every even added dimension is
proved.  All row-wise quadratic-bent lifts preserve the two-address product
hypothesis and have exact ratio (3.1), never exceeding `40/17` and tending to
two.

This completes A075's construction/asymptotic deliverables for this recurring
pattern as author-side artifacts.  Independent review by A085 or A092 is
still required.

**Exact remaining obstacle:** this theorem does not classify arbitrary
partial signs with product squared spectra—especially product marginals other
than deterministic, fair, or the seed's `1/5` bias—and therefore does not
prove a constant for all C022 functions.

**Next action:** derive arithmetic constraints on general product marginals
from integer Walsh coefficients and `{0,±1}` inversion, using the A071
`(1/5,1/2,1/2,1/2)` residual row as the first non-fair control.  Consumers:
A025, A080, A082, A085, A092, and B20.

No full-FEI proof or counterfamily was obtained.
