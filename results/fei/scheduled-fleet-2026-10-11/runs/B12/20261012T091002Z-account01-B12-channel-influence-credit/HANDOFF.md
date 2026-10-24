# Handoff — selector-channel collision credit

## Reusable theorem

For block channels

`C^alpha_gamma=h_alpha b_(gamma xor alpha)`, `alpha!=0`,

the aggregate block influence is exactly

`E[V_h J_b+p_b J_h-2 Overlap_B]`.

The overlap term is nonnegative and must be retained.  In particular,

`sum_alpha I_B(C^alpha) <= I_B(b)+I_B(h)`.

Over any adaptive nonreusing physical block hierarchy,

`sum_v w_v sum_alpha I_{B_v}(C_v^alpha) <= I(b)+I(h)`.

This removes the formal `2^|B|-1` multiplicity and all depth dependence at
the influence level.

## Exact control

For `g+=(-1,-1,1,1)`, `g-=(1,1,-1,-1)`, and
`h=(-1,-1,1,1)`, the gross channel influence is `2` and the overlap refund
is `2`; the unique channel is constant.  This is parity-zero erasure.

## Do not use the standalone entropy route

For arbitrary Boolean `k`, add a fresh bit `x` and choose

`h=x`, `g_+=xk`, `g_-=-xk`.

The unique selector channel is exactly `k`.  Therefore a universal estimate
of channel entropy by aggregate channel influence is full FEI itself, not a
smaller supporting lemma.

## Next consumer action

Keep `sum_alpha X_{B,alpha}` coupled to `R_B^sh` and the source channel.
At each spectral fiber, expand the signed entropy associator of the coherent
sum and pair it with the exact `-2 Overlap_B` credit before using an envelope.
Test a one-sided combined inequality; absolute values or separate FEI bounds
erase the available cancellation.  Also test the B01/A003 four-bit
KL-by-JS falsifier and its tensor powers.  Do not replace signed alignment by
coefficient-one restriction JS; that exact bridge is already refuted.

Route to A058/A059 for overlap and depth, A085/A091/A090 for review, and
A094/A097/B20 for integration.  New claims await independent review.  Full
FEI remains open.
