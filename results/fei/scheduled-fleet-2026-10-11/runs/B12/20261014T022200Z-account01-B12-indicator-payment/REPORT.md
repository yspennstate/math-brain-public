# B12 / A058 — indicator remainder coefficient obstruction

## Outcome

**PROVED an exact tensor law and an all-depth coefficient obstruction;
REFUTED the coefficient-two unsigned indicator payment.  Independent review
pending.**

For a nonzero indicator `q`, define

\[
 \Phi(q)=\mathcal E(q)-p\log_2(1/p),\qquad p=\mathbb E q.
\]

The normalized Fourier law `P_q(S)=\widehat q(S)^2/p` gives exactly

\[
 \Phi(q)=pH(P_q),\qquad \mathcal I(q)=p\mathbb E_{P_q}|S|.
\]

For products on disjoint physical blocks these normalized laws tensor, so

\[
 \frac{\Phi(\prod_jq_j)}{\prod_jp_j}
 =\sum_j\frac{\Phi(q_j)}{p_j},\qquad
 \frac{\mathcal I(\prod_jq_j)}{\prod_jp_j}
 =\sum_j\frac{\mathcal I(q_j)}{p_j}.
\]

Thus a seed's ratio `\Phi/I` survives every tensor power with no dimension,
weight-group, address-count, or depth dependence.

## Exact falsifiers and new bound

The two-bit NAND indicator `(1,1,1,0)` already has

\[
 \frac{\Phi}{I}=6-\frac32\log_2 3
 =3.622556248918266\ldots,
\]

so `\Phi(q)\le2I(q)` fails by `0.405639062229566...`.  Its tensor square is
the exact maximizer of this gap among all 65,808 nonzero indicators through
dimension four.

A stronger certified five-bit seed, truth-table mask `4146264055`, has

\[
 p=23/32,\qquad I=23/64,
\]

and normalized spectral masses

\[
 529/736,quad5\times25/736,quad7\times9/736,quad19\times1/736.
\]

It forces

\[
 \boxed{K\ge K_*=3.921809106893846\ldots}
\]

in every inequality `\Phi(q)\le K I(q)`.  The exact certificate
`K_*>3.921` is

\[
 2^{139817}>23^{20125}5^{15625}3^{7875}.
\]

Its tensor powers form a growing family in dimension `5k` with equality
`\Phi=K_*I` for every `k`; this distinguishes a persistent multiplicative
coefficient from an additive error erased by tensorization.

## Genuine Boolean control

For `f_k=2s^{\otimes k}-1`, the exact formula in `PROOF.md` gives

\[
 \lim_{k\to\infty}\frac{H(f_k)}{I(f_k)}
 =4.874685194779820\ldots.
\]

Hence the family is a genuine Boolean, growing-dimension control, not an FEI
counterexample.  Full FEI remains open.

## Why this matters for the active coherent gap

The preceding signed-ensemble theorem left the actual-sign correlation gap.
Paying its agreement/disagreement activation indicators independently with
coefficient two would have closed that route at constant four.  This run
rules out that projection even for a two-bit seed and proves that the loss
persists at arbitrary depth.  Any unsigned indicator payment of the same
form needs coefficient at least `K_*`; a universal finite coefficient would
itself be an FEI-strength theorem.

Therefore the next B12 step should not continue the coefficient-two unsigned
projection.  It should restore the sign information in the requested
near/separated split and seek a companion-sign, posterior-activation, or
terminal-reserve refund under the actual changing node weights.

## Verification scope

- Exact integer Walsh reconstruction for the two-bit and five-bit seeds.
- Exact Parseval and influence numerators.
- Exact integer sign certificates.
- Direct tensor-power checks through dimension 20 for NAND and dimension 15
  for the five-bit seed.
- Exhaustive enumeration of all 65,808 nonzero indicators in dimensions
  one through four; deterministic random probe of 100,000 additional
  indicators in dimensions five through nine.
- The five-bit seed is a certified witness, not a certified dimension-five
  optimum.

No independent review was observed.  Full FEI is **OPEN**.

