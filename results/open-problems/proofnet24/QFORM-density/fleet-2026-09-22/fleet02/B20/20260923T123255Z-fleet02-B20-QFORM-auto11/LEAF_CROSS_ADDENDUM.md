# Addendum — the surviving general leaf operator forces a robust physical cross cut

This addendum strengthens Section 4/8 of the canonical report for the same run.

## Theorem `QFORM-THREEBANK-LEAF-CROSS-NORM-v1`

Assume the surviving class of `QFORM-N3-SPECTRALWINDOW-OR-THREEBANK-v1`: `tau=1/2048`, `s_3(A)>=1`, `h` is the original physical hub, and `B=A[h^c,h^c]` is the complementary physical principal block. Then there is a partition of the original leaf coordinates into disjoint physical banks `U sqcup V=h^c` such that

`||B[U,V]||_op >= (1-tau)/2 = 2047/4096 = 0.499755859375`.     (A.1)

### Proof

The hub-removal lemma in the report gives `||B||_op>=1`. The no-pivot scalar condition is inherited by the leaf block, so

`||diag(B)||_op=max_j |B_jj|<tau`.                              (A.2)

For a Rademacher sign vector `eps` on the leaf coordinates let `D_eps=diag(eps)`, and let `U={j:eps_j=+1}`, `V={j:eps_j=-1}`. Define

`C_eps=(B-D_eps B D_eps)/2`.

In the physical decomposition `U sqcup V`, `C_eps` is exactly

`[[0,B[U,V]],[B[V,U],0]]`,

hence

`||C_eps||_op=||B[U,V]||_op`.                                  (A.3)

Averaging over independent signs kills every off-diagonal entry of `D_eps B D_eps` and preserves each diagonal entry, so

`E_eps[D_eps B D_eps]=diag(B)`.

Therefore

`B-diag(B)=E_eps[B-D_eps B D_eps]=2 E_eps C_eps`.               (A.4)

Taking operator norms and using convexity,

`||B-diag(B)||_op <=2 E_eps ||C_eps||_op`.

Consequently some physical cut satisfies

`||B[U,V]||_op >=(1/2)||B-diag(B)||_op`
`                 >=(1/2)(||B||_op-||diag(B)||_op)`
`                 >(1-tau)/2`.                                 (A.5)

This proves (A.1). QED.

## Consequence for the first unpaid implication

The surviving arbitrary-rank `N3(1/2048)` class can now be required to carry **all three** of the following source-coordinate resources simultaneously:

1. one original hub `h` with three disjoint original star banks `J_1,J_2,J_3`, each of energy at least `8 tau^2=1/524288`;
2. a complementary physical leaf operator `B` with `||B||_op>=1`;
3. an original-coordinate leaf cross cut `U sqcup V=h^c` with `||B[U,V]||_op>2047/4096`.

If any physical cross block has fifth volume at least `1/1024`, the pinned D5 theorem already pays by `10sqrt(2e)<23.317`; hence the first unpaid class may additionally assume all invoked fixed-scale D5 exits fail.

This does **not** yet imply three robust cross singular directions. In particular, the cut in (A.1) may be essentially rank one and may align with the hub star. The remaining mathematical task is to combine the robust leaf cross direction with the three independent source-coordinate star banks, or route the aligned/low-rank endpoint into an existing grouped-square / mixed-hub / Pluecker receiver, while retaining arbitrary same-side leaf curvature. No post-rotation independence is used.
