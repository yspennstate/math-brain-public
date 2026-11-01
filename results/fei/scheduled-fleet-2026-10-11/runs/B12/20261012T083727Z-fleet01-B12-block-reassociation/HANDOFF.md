# Handoff — A057 block reassociation

## Reusable result

For any finite physical block `B`, expand the source and selector in block
Fourier channels.  The product `F=a+hb` has the exact decomposition

`D_B(F)=S_B+sum_{alpha!=0}X_{B,alpha}+qD_B(h)+R_B^sh`.

For any sequential order `pi`, let `L_pi` be the weighted local
source/crossed sum and `M_pi` the weighted local child/remainder sum.  With
the simultaneous block values `L_B,M_B`, define `T_pi=L_pi-L_B`.  Then

`M_pi=M_B-T_pi` and `D_B(F)=L_pi+M_pi=L_B+M_B`.

This exact transfer law, not termwise channel cancellation, is the correct
two-query closure.

## Do not reuse the refuted mechanism

- Do not claim that internal `S/X` channels cancel under conditioning.
- Do not pay `R_i^sh` separately by the old one-node Bellman potential.
- Do not envelope all `2^|B|-1` selector-frequency channels separately and
  call the resulting block-size loss dimension-free.
- Do not treat the two-bit transfer witness as an FEI counterexample.

## Exact control witness

`g+=(-1,-1,-1,-1)`, `g-=(-1,-1,1,1)`, `h=(-1,-1,-1,1)`.
Both selector signs occur on the disagreement support `[2,3]`.

`T_(0,1)=-2ln2+(9/8)ln3<0`, while `T_(1,0)=0`.

The sign certificate is `3^9<2^16`.  The complete decrement is `2ln2` in
both orders.

## Next consumer action

Represent `T_pi` as an associator of normalized spectral mixtures.  For a
three-query block, compare all adjacent transpositions and test a cocycle
identity.  The target is an order-independent KL/terminal-reserve charge
that compresses the aggregate without expanding `2^m-1` channels.

Route to A058/A059 for overlap/depth use, A085/A091/A090 for independent
review, and A094/A097/B20 for campaign integration.  Both new claims remain
pending independent review; full FEI remains open.
