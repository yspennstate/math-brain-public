# B19 / A094 — independent review of the positive point-defect tower

## Verdict

**ACCEPT AT THE FORMAL THEOREM SCOPE; ONE SCOPE-WORDING CORRECTION.**

Review target:

- B05/A023 run `20261013T203102Z-account01-B05-positive-defect-retained-credit-a023`;
- canonical finalized commit `ed704e08ace97f8c295992ee560edfbe4d89a07a`;
- claims `B05_A023_POSITIVE_SCALAR_SLOPE_v1`,
  `B05_A023_POSITIVE_DEFECT_ENDPOINT_v1`, and
  `B05_A023_POSITIVE_DEFECT_RETAINED_v1`.

For `Q_r` equal to `+1` except at one point of the `r`-cube and

\[
F_1=A(wP),\qquad F_k=A(Q_{r_k}F_{k-1}),\qquad r_k\ge2,
\]

the original proof correctly establishes

\[
U(P)\le\frac83I(P)
\Longrightarrow
\boxed{U(F_d)\le\frac83I(F_d)}
\]

for every finite depth and arbitrary rank sequence.  It also correctly gives,
for any finite adaptive/pruned restriction tree on the physical variables of
`F_d` and one common disjoint terminal factor `h`,

\[
\boxed{U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h)
\le\frac83I(F_d).}
\]

The constant is independent of base dimension, rank, positive point-defect
bias, activation probability, depth, reveal order, pruning, and the complexity
of the common terminal factor.  The standard bridge gives
`H(F_d)<=22 I(F_d)/3`.

## Scope correction

The theorem is an endpoint retained-`U` telescope.  It does **not** construct
the A023 first-revelation stopping rule, identify individual
`mu[log(1/mu)-D]` credits, or prove that a physical rarity credit is owned once
and never reused by descendants.  Accordingly, the sentence that no
descendant “reuses a rarity credit” should be read only as cancellation in the
signed endpoint telescope, not as a proved credit-ownership mechanism.

This is a scope/wording correction, not a mathematical repair of the three
formal claims.  A023 correctly remains incomplete.

## Independent proof reconstruction

### Point-defect block

With `p=2^{-r}` and `beta=1-2p`, direct Walsh reconstruction gives one empty
coefficient `beta` and nonempty coefficients of magnitude `2p`.  Therefore

\[
I(Q_r)=2rp,
\qquad
U(Q_r)=\beta^2\log_2(1/\beta^2)+2rp\beta.
\]

For `r>=3`, `-ln(1-2p)<=2p/(1-2p)` yields

\[
\frac{U(Q_r)}{I(Q_r)}
\le\beta+\frac{2\beta}{r\ln2}<2.
\]

For `r=2`, `U(Q_2)=I(Q_2)=1`.  Hence `U(Q_r)<=2I(Q_r)` at every rank.

### Scalar inequality

Independent differentiation reproduces

\[
R'''(t)=\frac{4-t-t^2}{2\ln2\,t(1-t^2)}>0.
\]

Thus `R'` has a unique global minimum at the zero `tau` of `R''`.  The exact
rational certificate independently verifies

\[
0.49<\tau<0.51,\qquad |R''|<1\text{ on }[0.49,0.51],
\]

and

\[
R'(\tau)>-\frac{14807}{11200}
=-\frac43+\frac{379}{33600}.
\]

The certificate uses only finite Taylor bounds for `e^{3/4}`, the exact
comparison `2^{127}>3^{80}`, and the first two positive terms of the atanh
series for `ln 2`.  Hence

\[
R(t)\le\frac43(1-t),\qquad 0\le t\le1.
\]

The malformed `frac` glyph in the displayed `ln 2>56/81` line of the source
proof is a transcription defect only; the surrounding formula, rational
calculation, and checker all use the intended `56/81` inequality.

### Recurrence and physical accounting

For disjoint spectra, upper caps factor, so `U` is exactly additive.  The
half-activation spectrum independently gives

\[
\begin{aligned}
U(F_k)&=\frac12U(F_{k-1})+\frac12U(Q_r)+R(t),\\
I(F_k)&=\frac12I(F_{k-1})+\frac12I(Q_r)+\frac{1-t}{2},
\end{aligned}
\qquad t=(EQ_r)(EF_{k-1}).
\]

The first fair balancing character forces `EF_1=1/2`; later means stay
positive, so `t in [0,1]`.  The two preceding inequalities close the
`8/3` induction exactly.  No bias, physical input, or selector influence is
omitted.

For a finite tree, weighted signed node charges telescope to root `U` minus
the leaf average.  A common disjoint `h` contributes the same additive `U(h)`
at the root and every leaf, hence cancels.  Leaf `U>=0` then gives the claimed
bound.  This does not extend to a restricted, shared, or leaf-dependent core.

## Independent computation

`CHECK.py` is independent in structure and arithmetic from the author code.
It uses integer Walsh transforms and exact rational spectra/influences, with
100-digit decimal logarithms.  It separately verifies the exact scalar
certificate, direct towers, arbitrary-rank state recurrences, pruned trees,
and tensor cancellation.  See `CHECK.out` for the executed counts.

## Primary-literature comparison

O'Donnell--Tan's composition theorem assumes inner functions on disjoint
variable blocks and a product-biased outer FEI hypothesis.  It supports the
disjoint tensor/composition setting but does not state this upper-set
potential `U`, the scalar `R`, or the retained-tree endpoint:

- https://arxiv.org/abs/1304.1347

Potapov proves FEI for plateaued and partially bent Boolean functions.  A
point-defect `Q_r` is covered at the root only when it falls within those
spectral classes; the paper does not supply the nested upper-set activation
identity or the adaptive retained-`U` telescope:

- https://arxiv.org/abs/2609.21563

No novelty or priority claim is made here.

## Exact remaining gap

The accepted theorem still requires fair selectors and fresh disjoint
positive point-defect blocks.  It does not cover biased selectors, negative
near-constant balancers, reused variables, changing/overlapping coherent
cores, or the A023 first-revelation mismatch/KL ledger.  It is a proper-class
constant improvement, not a universal payment.  Full FEI remains **OPEN**.
