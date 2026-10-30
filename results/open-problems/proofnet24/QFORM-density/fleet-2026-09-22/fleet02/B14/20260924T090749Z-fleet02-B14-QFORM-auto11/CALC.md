# fleet02/B14 early calculation — reflection bank translation lift

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260924T090749Z-fleet02-B14-QFORM-auto11
Status: substantive checkpoint; full QFORM still open.

## First unpaid implication

`QFORM-BANK-REFLECTION-FACTOR-OR-SAMEBANK-CURVATURE-EXIT-v1`:
from the bare hypothesis s_3(A)>=1, expose a product-preserving three-bank compression whose paid 3x3 core remains uniformly nondegenerate after all same-bank curvature is retained, with the remaining sources entering only through translations/Schur boundary; otherwise trigger an existing D'/D5/projected-crossing/shared-bank/pair/ridge exit. The calculation below shows why physical-coordinate reciprocal payment cannot replace this bank step.

## Reflection translation-mixture compiler

Let

B_* = I_3 - (2/3) 11^T,

so B_*^2=I_3 and spec(B_*)={1,1,-1}. Let S=(S_1,S_2,S_3) have independent coordinates, each with density cap at most K, and let T be an arbitrary R^3-valued random vector independent of S. No density, moment, support, coordinate-independence, or boundedness is assumed for T.

For

Q=(S+T)^T B_*(S+T),

conditioning on T=t and setting Y=KS gives cap-one independent coordinates and

Q=K^{-2}(Y+Kt)^T B_*(Y+Kt).

The completed fixed-source three-dimensional theorem (Theorem A in COUNTEREXAMPLE_SEARCH.md at e5f71d79eff325201dd0274053d20268ce65b837) allows arbitrary affine terms and gives height 6 sqrt(pi) for the inner reflected form. Scaling back and averaging the interval bound over T therefore gives

||p_Q||_{infty,ess} <= 6 sqrt(pi) K^2.                                  (1)

This is exactly mass-linear in the translation mixture. Arbitrarily remote/discrete/correlated/unbounded translation laws cost zero.

## Exact owner-target lift to original product coordinates

Split original coordinates into three disjoint active banks and an outside bank. Let U be a 3 x p matrix whose rows are supported on the three disjoint active banks and satisfy UU^T=I_3. Let Z be the outside coordinates and L any real 3 x q matrix. Put

F=[U,L],     A=F^T B_* F.

Then Q=(UX+LZ)^T B_*(UX+LZ), so (1) applies with S=UX and T=LZ whenever the three bank projections have density cap <=K.

Moreover this A is automatically in the exact spectral target. Since

FF^T=I_3+LL^T >= I_3,

write R=(FF^T)^{1/2}>=I_3. The three nonzero eigenvalues of A equal those of R B_* R. On the two-dimensional space R^{-1}E_+(B_*),

x^T R B_* R x / ||x||^2 = ||Rx||^2/||x||^2 >=1,

so the two positive eigenvalues are >=1. On R^{-1}E_-(B_*), the same quotient is <=-1, so the negative eigenvalue is <=-1. Thus A has at least three eigenvalues of modulus >=1 for every L, without any smallness condition.

In the compressed variables (S,Z), the block matrix is

[[B_*, B_*L],[L^T B_*, L^T B_*L]].

Its Schur remainder relative to B_* is exactly zero:

L^T B_*L - (B_*L)^T B_*(B_*L)=0.

Hence the newest fleet03/B14 Schur-boundary theorem applies exactly to this family: it is the flat-boundary branch where sheetwise edge jumps must cancel in the assembled full density. The estimate (1) therefore does not require absoluteizing the two sheets.

## Diffuse flat-bank instance and physical-triple obstruction

Take an even bank size m=2r. In each bank let

S_a=m^{-1/2} sum_{j=1}^m X_{a,j},

with all X_{a,j} independent and density <=1. The Rogozin/Ball estimate used in the fixed source's Lemma 1 gives

||p_{sum_{j=1}^m X_{a,j}}||_infty <= 1/sqrt(r),

hence ||p_{S_a}||_infty <= sqrt(2). Therefore, with L arbitrary,

||p_Q||_{infty,ess} <= 12 sqrt(pi).                                   (2)

No support, moment, connectedness, fragment-count, or translation restriction occurs.

Now set L=0. Then A_m=U^T B_* U has exactly the three nonzero eigenvalues {1,1,-1}. Every physical coefficient is O(1/m). A physical 3x3 principal block is singular unless it chooses one coordinate from each of the three banks; every invertible one is a permutation of

m^{-1} B_*,

so its least absolute eigenvalue is exactly 1/m. Applying fixed-source Theorem A after conditioning on all other coordinates therefore gives only

||p_Q||_infty <= 6 sqrt(pi) m

from every physical triple, while the grouped-bank estimate (2) is 12 sqrt(pi), independent of m.

Likewise a physical pair from two different banks is

m^{-1} [[1/3,-2/3],[-2/3,1/3]],

with eigenvalues 1/m and -1/(3m), while a same-bank pair is singular. Thus physical-pivot/pair reciprocal payment also degenerates throughout this exact-target family.

This is a proof-interface obstruction, not a QFORM counterexample: aggregate the product banks before paying curvature. Once that aggregation is made, arbitrary outside translations are zero-tax.
