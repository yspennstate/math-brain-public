# account01/B08 r45 addendum — q=3 three-bank rank-two carrier tube

This addendum strengthens the overlap-only survivor in `REPORT.md`. It is a deterministic/source-pinned reduction only; the unrestricted QFORM conjecture remains open.

## Setup

Let `H1,H2,H3` be three pairwise-disjoint ORIGINAL-coordinate banks. Write

`X=A[H1,H2]`, `Y=A[H1,H3]`, `Z=A[H2,H3]`.

Define the three natural physical crossings

`B1=A[H1,H2 union H3]=[X Y]`,

`B2=A[H2,H1 union H3]=[X^T Z]`,

`B3=A[H3,H1 union H2]=[Y^T Z^T]`.

The completed designated-partner theorem account02/B08 r34 states for every actual physical crossing block `B=A[S,T]`

`||p_Q||_infinity <= 6^(4/3) e_3(BB^T)^(-1/6)`

whenever the third compound is nonzero, retaining arbitrary same-side quadratic curvature, outside couplings, affine terms and complementary spectrum; the resulting density is in `C_0`.

Set

`C3=6^(4/3)`,

`C*=197.7780678260685`,

`theta*=C3/C*=0.05512604949999305`.

## Theorem — `QFORM-Q3-THREEBANK-RANK2-CARRIER-TUBE-v1`

For every `L>0`, one of the following holds:

1. one of the three natural crossings pays the full ambient quadratic form,

   `||p_Q||_infinity <= C*/L`, `p_Q in C_0(R)`;

or

2. there exist orthogonal projections `P_i` on `R^{H_i}`, each of rank at most two, such that for every `i!=j`

   `||A[H_i,H_j]-P_i A[H_i,H_j] P_j||_op < 2 theta* L`.

Equivalently, if `R_cross` denotes the tripartite off-diagonal operator on `H1 direct_sum H2 direct_sum H3` and

`R_0` is obtained by replacing every off-diagonal block by `P_i A[H_i,H_j] P_j`, then

`rank(R_0)<=6`

and

`||R_cross-R_0||_op < 4 theta* L = 0.2205041979999722 L`.

Thus every unpaid q=3 overlap packet is trapped in a product-preserving **two-dimensional carrier per original-coordinate bank**; no random-coordinate rotation is used.

## Proof

Assume alternative 1 fails. For each `i=1,2,3`, the partner bound applied to the actual physical crossing `B_i` gives

`e_3(B_i B_i^T)^(1/6) < theta* L`.

Let the singular values of `B_i` be `s_1>=s_2>=s_3>=...`. Since

`e_3(B_iB_i^T) >= s_1^2 s_2^2 s_3^2 >= s_3^6`,

we obtain

`s_3(B_i) < theta* L`.

Let `P_i` be the orthogonal projection onto the top-two left singular subspace of `B_i` (or the whole left range if its rank is below two). By Eckart--Young,

`||(I-P_i)B_i||_op=s_3(B_i)<theta*L`.

Because `A` is symmetric, for each pair `i!=j`, the block `A[H_i,H_j]` is a column subblock of `B_i`, while its transpose is a column subblock of `B_j`. Hence

`||(I-P_i)A[H_i,H_j]||_op<theta*L`,

`||A[H_i,H_j](I-P_j)||_op<theta*L`.

Therefore

`A[H_i,H_j]-P_iA[H_i,H_j]P_j`

`=(I-P_i)A[H_i,H_j]+P_iA[H_i,H_j](I-P_j)`,

so its operator norm is `<2 theta*L`.

The range of every block `P_iA[H_i,H_j]P_j` lies in `Ran(P_i)`, hence the range of `R_0` is contained in

`Ran(P_1) direct_sum Ran(P_2) direct_sum Ran(P_3)`,

which has dimension at most six. Finally, if `E=R_cross-R_0`, every off-diagonal block of `E` has norm `<2 theta*L`. For `x=(x_1,x_2,x_3)`,

`||(Ex)_i|| <= 2 theta*L sum_{j!=i} ||x_j||`.

The scalar `3x3` matrix with zero diagonal and off-diagonal entries `2 theta*L` has operator norm `4 theta*L`, giving

`||E||_op<4 theta*L`.

This proves the theorem.

## Application to the r45 q=3 survivor

In the unpaid diffuse Pluecker branch, r45 inherits from account03/B08 r25 three disjoint banks `H1,H2,H3` carrying principal-triple packet mass

`P_3>2L^6/27`.

Applying the theorem to those exact banks gives a new exhaustive q=3 sub-router:

- either the full ambient QFORM already has a continuous density `<197.779/L`;
- or all three inter-bank coefficient blocks are simultaneously within `0.110252099L` (operator norm, blockwise) of a common rank-two-per-bank carrier, and the full tripartite cross interaction is within `0.220504198L` of rank at most six.

This does not by itself pay the arbitrary same-bank curvature, so it is not a full q=3 solution. It does, however, replace the former unconstrained q=3 packet by a fixed local-carrier geometry while preserving the original-coordinate product decomposition. The next analytic receiver should therefore act on this six-dimensional carrier **before** any reciprocal single-minor selection, while leaving same-bank quadratic terms untouched.

## Scope audit

No Gaussianity, moments, support regularity, log-concavity, post-rotation independence, pointwise van-der-Corput decay, arbitrary-joint coarea, or Monte Carlo input is used. The only basis changes are deterministic singular-subspace projections on coefficient matrices. All probabilistic crossings are on disjoint original-coordinate banks.
