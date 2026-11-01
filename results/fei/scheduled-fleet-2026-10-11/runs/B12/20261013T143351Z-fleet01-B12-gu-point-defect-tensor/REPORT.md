# B12 / A056 — GU tensorization and point-defect products

Run: `20261013T143351Z-fleet01-B12-gu-point-defect-tensor`  
Primary packet: **A056 — Balanced composition**  
Attempt: `A056-GU-POINT-DEFECT-TENSOR-01`  
Gap: `B12-A056-GU-COMPOSITION-v1`  
Status: **PROPER-CLASS GU THEOREM PROVED BY CONTRIBUTOR; FULL FEI OPEN**

## Outcome

The later owner amendment in the authoritative order makes the global
restriction inequality

`G(f)=sum_i Delta_i U(f) <= K I(f)`

the current fleet target.  This run turns B12's composition assignment onto
that inequality.

Two exact results are proved.

1. **GU tensorizes without loss.**  For Boolean `f,g` on disjoint physical
   blocks and `F=fg`,

   `U(F)=U(f)+U(g)`, `G(F)=G(f)+G(g)`, and `I(F)=I(f)+I(g)`.

   The proof uses the exact factorization of both the spectral law `p` and
   its upper-set mass `pi`; it is not inferred from ordinary Fourier entropy.

2. **Sharp all-parameter class.**  For every point defect `d_n`, and for
   every finite disjoint product of point defects of arbitrary arities,

   `G <= kappa_pd I`,

   where

   `kappa_pd = 37/4-(9/2)log_2(3) = 2.117668746754797...`.

   The constant is independent of total dimension, number of factors,
   factor arities, and product-tree depth.  It is sharp for this class and is
   attained by the three-variable point defect.

This is a strict extension from one point-defect gate to an arbitrary number
of disjoint biased gates combined by parity/product.  It is a proper class;
universal GU and full FEI remain open.

## Exact formulas and proof

For a point defect on `n` variables, set `N=2^n`.  Its spectral law is

- `p_empty=(1-2/N)^2`;
- `p_S=4/N^2` for every nonempty `S`;
- `pi(S)=4*2^(n-|S|)/N^2` for nonempty `S`.

Therefore

`U_n=(1-2^(1-n))^2 log_2(1/(1-2^(1-n))^2)+2n/2^n-4n/2^(2n)`.

Every coordinate restriction has one constant child and one point-defect
child, so

`G_n=n(U_n-U_(n-1)/2)`, while `I_n=2n/2^n`.

Writing `t=2^(1-n)` and
`phi(t)=(1-t)^2 log_2(1/(1-t)^2)`, the ratio is

`G_n/I_n=1+(n-2)t+[phi(t)-phi(2t)/2]/t`.

For `n>=4`, a second-derivative estimate gives the uniform bound `15/8`.
The dimensions `1,2` give `0,2`.  Dimension `3` gives `kappa_pd`; exact
integer certificates `3^18<2^29` and `3^12>2^19` place it strictly between
`2` and `17/8`, so it is the unique maximal dimension.

The complete proof is in `GU_POINT_DEFECT_TENSOR.tex`.

## Why the tensor law is exact

For disjoint blocks and `S=S_1 union S_2`,

`p_F(S)=p_f(S_1)p_g(S_2)` and
`pi_F(S)=pi_f(S_1)pi_g(S_2)`.

Thus the logarithm defining `U` splits.  If coordinate `i` belongs to `f`,
both restrictions are `f_(i,+/-) g`, so the same product law gives
`Delta_i U(F)=Delta_i U(f)`.  Summing over coordinates proves exact
additivity of `G`.  Hence every finite product inherits the maximum factor
constant, with no depth or address-count loss.

## Verification

Command:

```bash
python3 check_gu_point_defect_tensor.py
```

The checker uses exact `Fraction` Walsh arithmetic and 110-digit Decimal
logarithms.  It independently reconstructs `p`, every upper mass `pi`, `U`,
all physical restrictions, `G`, and `I`.

- 12 point-defect dimensions checked directly;
- all 138 integer partitions of total dimension through 10 checked as
  tensor products;
- exact maximizer dimension `3` recovered;
- both integer sign certificates checked;
- no randomness and no seed.

The all-dimension and arbitrary-factor claims are analytic; computation is a
reconstruction check, not finite extrapolation.

## Case extension and limitations

- Starting class: one point-defect/AND-or-OR sign gate.
- New class: any finite parity/product of disjoint point-defect gates, with
  arbitrary and unequal block arities.
- Previous constant: not recorded for GU on the composed class.
- New constant: the sharp factor constant `kappa_pd`, independent of every
  composition parameter.
- Bias: unrestricted across factors; each factor has its physical rare-event
  bias `2^-n_r`.
- Depth and address count: arbitrary; exact additivity removes both.
- Overlap: excluded.  Shared coordinates destroy product factorization of
  `pi`, so the earlier coherent-remainder work remains relevant outside this
  theorem.

This result does not assume FEI on the class.  It proves GU directly from the
upper-set masses.

## Acceptance and next unpaid step

- A056 exact composition interface: **ADVANCED** for the new `U,G` target.
- Independent review: **NONE OBSERVED**; route to A091, then A090.
- Universal GU: **OPEN**.
- Full FEI: **OPEN**.

The next composition step is an outer gate other than parity/product.  For a
balanced disjoint substitution `g(h_1,...,h_m)`, first prove the exact
upper-mass chain rule

`U(F)=U(g)+sum_j Inf_j(g) U(h_j)`

under the necessary zero-mean hypotheses, then track the bias created when a
physical coordinate of one child is restricted.  The obstruction is exactly
that the child restriction ceases to be balanced, so `Delta_i U` does not
follow by subtracting two copies of the root chain rule.

## Configuration and status

The later GU amendment, GU source notes, current B12 compact contract, current
status and obstruction registry were read from the immutable blobs listed in
`SOURCE_PINS.md`.  No protected source, held reroute, public release, email,
paid compute, new worker, scheduler edit, or peer-owned state mutation was
used.  The runtime exposed no model or reasoning-effort telemetry.
