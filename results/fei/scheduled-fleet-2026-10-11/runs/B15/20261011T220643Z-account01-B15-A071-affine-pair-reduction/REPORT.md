# B15 / A071 — signed affine two-point cells collapse to the edge baseline

**Run ID:** `20261011T220643Z-account01-B15-A071-affine-pair-reduction`  
**Primary packet:** A071 (Search-space design)  
**Attempt:** `A071-attempt-02-C022-affine-pair-reduction`  
**Status:** `PROVED_FINITE_FAMILY_REDUCTION_PENDING_INDEPENDENT_REVIEW`  
**Full FEI:** **OPEN**

## 1. Exact target and previous value

The preceding A071 run exhaustively classified 1,015,808 representatives in
the two-address family whose three nonzero address slices are constant-sign
indicators of disjoint four-cube edges.  All 3,584 retained candidates with a
product residual squared law satisfied

\[
\frac{H(F)}{I(F)}\le \frac{40}{17},
\]

and the archived six-variable witness attained equality.  That theorem did
not cover arbitrary signed two-point address slices.

This run freezes exactly one larger family: keep two address bits and four
physical bits, but allow each of the three nonzero address slices to be an
arbitrary signed two-point affine cell.  Retain C022's hypothesis that every
conditional squared Walsh law is product.  The objective is to determine
whether this extension contains a ratio larger than `40/17`.

The original C022 statement and construction were read at
`research_pushes/2026-10-11-full-fei-100-agents/sources/ONE_BIT_ENDPOINT.md`,
blob `0848515367f7fc3493f51820de999a30234905a4`.  The prior finite baseline is
the immutable B15 run at open-problems commit
`5aca95345e9eaef015d406af6f84bf74c5a3e01d`.

## 2. PROVED: two-point product classification

### Lemma `B15-A071-SIGNED-PAIR-PRODUCT-02-v1`

Let `m>=1`, let `u!=v` in `F_2^m`, and let

\[
h(x)=\sigma_u\mathbf1_{\{u\}}(x)+
     \sigma_v\mathbf1_{\{v\}}(x),\qquad
\sigma_u,\sigma_v\in\{-1,1\}.
\]

Put `d=u+v` and `epsilon=sigma_u sigma_v`.  The normalized squared Walsh
law of `h` is a product law if and only if `d` has Hamming weight one.

When `d=e_i`, the law is uniform on

\[
\{s:s_i=b\},\qquad b=\mathbf1_{\{\epsilon=-1\}},
\]

and therefore has entropy `m-1` and mean degree

\[
\frac{m-1}{2}+b.                                           \tag{2.1}
\]

#### Proof

For every Walsh character `chi_s`,

\[
2^m\widehat h(s)
=\sigma_u\chi_s(u)\{1+\epsilon\chi_s(d)\}.
\]

Thus the square is nonzero and constant precisely on the affine parity
hyperplane

\[
H_{d,b}=\{s:s\cdot d=b\}.
\]

The support of a product law on a Boolean cube is a coordinate subcube: in
each coordinate its marginal support is `{0}`, `{1}`, or `{0,1}`, and the
joint support is their Cartesian product.  Since `H_{d,b}` has size
`2^(m-1)`, if it is a product support it fixes exactly one coordinate.
Consequently `d=e_i`.  Conversely, `d=e_i` makes `H_{d,b}={s:s_i=b}`, which
is a product law with one deterministic and `m-1` fair coordinates.  Formula
(2.1) follows.  QED.

This proof also shows why a quotient by the full affine group is invalid for
the FEI ratio: a general linear change permutes characters but does not
preserve their Hamming degrees, hence does not preserve influence.  Only
translations and coordinate permutations are harmless here.

## 3. PROVED: the proposed extension cannot improve `40/17`

For `m=4`, the lemma says every admissible two-point slice is a physical cube
edge.  A constant sign has conditional spectral mean degree `3/2`; an
alternating sign has mean degree `5/2`.  Both have conditional entropy three.

Each such slice has squared norm `2/16=1/8`.  Replacing one alternating edge
slice by the constant-sign slice on the same edge therefore:

- preserves its mass and conditional entropy;
- preserves the address-character contribution;
- preserves the residual slice and Booleanity of the assembled function;
- decreases physical influence by exactly `1/8`.

If `k` of the three slices alternate, then for the same residual function and
edge supports

\[
H(F_k)=H(F_0),\qquad I(F_k)=I(F_0)+\frac{k}{8}.            \tag{3.1}
\]

The constant-sign function `F_0` lies in the previous exhaustive A071 domain.
Hence

\[
\boxed{
\frac{H(F_k)}{I(F_k)}\le
\frac{H(F_0)}{I(F_0)}\le\frac{40}{17}.
}                                                           \tag{3.2}
\]

This is complete for the frozen signed two-point family: arbitrary affine
pairs not parallel to a coordinate fail the product-law hypothesis, while
every remaining signed edge maps monotonically to a prior constant-sign
case.  Pairing choices within a fixed six-vertex support do not alter this
metric comparison.

For the archived equality witness, direct six-variable Walsh reconstruction
gives the four exact signatures

\[
\begin{array}{c|c|c|c}
k&\text{multiplicity}&H&I\\\hline
0&1&5&17/8\\
1&3&5&9/4\\
2&3&5&19/8\\
3&1&5&5/2.
\end{array}
\]

Thus the ratios are respectively `40/17`, `20/9`, `40/19`, and `2`.

## 4. Exact computation and resource cap

`affine_two_point_reduction.py` uses only integers and `Fraction` arithmetic.
It checks all

\[
2\binom{16}{2}=240
\]

signed two-point cells.  Exactly 64 have product squared laws: the 32 cube
edges with constant sign and the same 32 with alternating sign.  It then
reconstructs all eight relative-sign choices on the archived maximizer,
checks Parseval, exact entropy, and influence by the full 64-entry truth table.

The larger naive representative count is

\[
8\cdot1{,}015{,}808=8{,}126{,}464.
\]

Equation (3.1) replaces that scan by a complete analytic monotonicity
reduction.  Frozen resource caps were 240 local cells, eight assembled
controls, 30 seconds, and 64 MiB.  The observed run completed in under one
second.  No randomness or floating tolerance was used.

Command:

```text
python affine_two_point_reduction.py > OUTPUT.txt
```

## 5. Obstruction and scope audit

- **Actual Booleanity:** at each physical input exactly one residual or signed
  address slice is nonzero, with value `+1` or `-1`.
- **Conditional product laws:** proved exactly; non-coordinate affine pairs
  are rejected rather than silently included.
- **Whole-set labels:** address frequencies are charged once in the full
  Walsh degree.
- **Signs:** relative signs are retained; they are the entire new axis.
- **Rare restrictions:** slice masses remain fixed at `1/8`; this family does
  not probe a vanishing activation scale.
- **Near tensors and composition:** no tensor or composition extrapolation is
  made.
- **Affine symmetry:** full `AGL(4,2)` is not used because it does not preserve
  Hamming degree.

## 6. Packet delta and next action

**Previous status:** the constant-edge family was exhausted, but the proposed
signed affine-cell extension was untreated.

**New status:** every signed affine two-point cell compatible with C022 is a
signed coordinate edge, and alternating signs only lower `H/I`.  Therefore
the exact `40/17` maximum extends to the complete signed two-point product-cell
family.

This is a finite-family theorem, not a solution of C022 and not a full-FEI
bound.  No independent review was performed; route the complete package to
A085 and A092.

The next B15 natural run should move to **A075**, not enlarge dimension:
derive an analytic classification of possible dyadic product-row norms and
their address-degree payment for two spectral address bits.  The surviving
gap is in higher-support conditional rows, not two-point affine geometry.

